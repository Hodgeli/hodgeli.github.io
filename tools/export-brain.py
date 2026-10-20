#!/usr/bin/env python3
"""把博客 Markdown 源导出成适合喂给 Gemini Notebook（原 NotebookLM）的干净文档。

用法:
    python tools/export-brain.py                 # 导出全部文章（跳过 hello-world 示例）
    python tools/export-brain.py --all           # 连示例文章一起导出
    python tools/export-brain.py --merge         # 额外输出一个合并版 _全部文章.md
    python tools/export-brain.py --out D:/somewhere

设计要点:
  * 输出文件名 = <日期>-<slug>.md，**必须保持稳定**。
    Google Drive 里的 Google 文档靠文件身份做自动同步，改名等于新文件，
    笔记本那边的来源就断了。所以每次重跑都是同名覆盖，不要手工改名。
  * front-matter 不直接丢，而是转成文档头部的元信息块，
    让 Gemini Notebook 能读到分类/标签/原文链接。
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

POSTS_DIR = Path(__file__).resolve().parent.parent / "source" / "_posts"
CONFIG = Path(__file__).resolve().parent.parent / "_config.yml"
DEFAULT_OUT = Path(__file__).resolve().parent.parent / "brain-export"

# Hexo 默认示例文章，默认排除
SKIP_SLUGS = {"hello-world"}

FRONT_MATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)


def site_url() -> str:
    """从 _config.yml 读站点 url，用来拼文章永久链接。"""
    try:
        cfg = yaml.safe_load(CONFIG.read_text(encoding="utf-8")) or {}
        return str(cfg.get("url", "")).rstrip("/")
    except Exception:
        return ""


def norm_list(v) -> list:
    """categories / tags 可能是字符串、列表或 None，统一成列表。"""
    if v is None:
        return []
    if isinstance(v, str):
        return [v]
    if isinstance(v, (list, tuple)):
        out = []
        for item in v:
            out.extend(norm_list(item))
        return out
    return [str(v)]


def norm_date(v) -> str:
    """日期可能是 datetime 对象，也可能是字符串。"""
    if v is None:
        return ""
    s = str(v).strip()
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    return f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else s


def build_doc(slug: str, meta: dict, body: str, base: str) -> str:
    title = str(meta.get("title") or slug)
    date = norm_date(meta.get("date"))
    cats = norm_list(meta.get("categories"))
    tags = norm_list(meta.get("tags"))
    desc = str(meta.get("description") or "").strip()

    url = ""
    if base and date:
        y, m, d = date.split("-")
        url = f"{base}/{y}/{m}/{d}/{slug}/"

    lines = [f"# {title}", ""]
    if date:
        lines.append(f"- **发布日期**：{date}")
    if cats:
        lines.append(f"- **分类**：{'、'.join(cats)}")
    if tags:
        lines.append(f"- **标签**：{'、'.join(tags)}")
    if url:
        lines.append(f"- **原文链接**：{url}")
    lines.append("")

    if desc:
        lines += [f"> {desc}", ""]

    lines += ["---", "", body.strip(), ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description="导出博客文章，供 Gemini Notebook 当知识库")
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="输出目录")
    ap.add_argument("--all", action="store_true", help="包含 hello-world 等示例文章")
    ap.add_argument("--merge", action="store_true", help="额外输出一个合并版 _全部文章.md")
    args = ap.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    base = site_url()
    posts = sorted(POSTS_DIR.glob("*.md"))
    if not posts:
        print(f"[!] 在 {POSTS_DIR} 没找到任何 .md", file=sys.stderr)
        return 1

    written, skipped, merged = [], [], []
    for p in posts:
        slug = p.stem
        if slug in SKIP_SLUGS and not args.all:
            skipped.append(slug)
            continue

        raw = p.read_text(encoding="utf-8")
        m = FRONT_MATTER.match(raw)
        if not m:
            print(f"[!] {p.name} 没有 front-matter，跳过", file=sys.stderr)
            skipped.append(slug)
            continue

        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError as e:
            print(f"[!] {p.name} front-matter 解析失败：{e}", file=sys.stderr)
            skipped.append(slug)
            continue

        date = norm_date(meta.get("date")) or "0000-00-00"
        doc = build_doc(slug, meta, m.group(2), base)
        name = f"{date}-{slug}.md"
        (out_dir / name).write_text(doc, encoding="utf-8")
        written.append(name)
        merged.append(doc)

    if args.merge and merged:
        (out_dir / "_全部文章.md").write_text("\n\n---\n\n".join(merged), encoding="utf-8")

    print(f"输出目录：{out_dir}")
    for n in written:
        size = (out_dir / n).stat().st_size
        print(f"  + {n}  ({size} B)")
    if args.merge:
        print(f"  + _全部文章.md  ({(out_dir / '_全部文章.md').stat().st_size} B)")
    if skipped:
        print(f"跳过：{', '.join(skipped)}")
    print(f"\n共 {len(written)} 篇。上传到 Google Drive 后不要改文件名。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
