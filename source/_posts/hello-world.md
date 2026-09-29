---
title: Hello World
date: 2026-09-29 13:30:00
tags:
  - 建站
categories:
  - 随笔
description: 新博客的第一篇文章
---

这是新博客的第一篇文章。

## 为什么重建

旧的博客系统基于 Hexo + NexT 5.1.3，最后一次部署停在 2022 年 11 月。
这次推倒重来，换了 Butterfly 主题，并把构建完全交给 GitHub Actions ——
本地只需要写 Markdown 然后 push，构建和发布都在云端完成。

## 写作方式

在 `source/_posts/` 下新建 `.md` 文件，或者在项目根目录执行：

```bash
npm run new -- "文章标题"
```

写完后提交并推送：

```bash
git add .
git commit -m "新增文章：文章标题"
git push
```

推送后 GitHub Actions 会自动构建并发布，一两分钟后就能在线上看到。

## 代码块效果

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
```

## 待办

- [ ] 替换 `_config.yml` 里的站点标题、副标题、作者等占位符
- [ ] 配置 `_config.butterfly.yml` 里的社交链接
- [ ] 删除这篇示例文章
