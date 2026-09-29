# hodgeli.github.io

Hodge 的个人博客。Hexo 8 + Butterfly 5.7，由 GitHub Actions 自动构建并发布到 GitHub Pages。

线上地址：https://hodgeli.github.io/

## 工作原理

```
本地写 Markdown  →  git push  →  GitHub Actions 构建  →  GitHub Pages 发布
```

源码（Markdown + 配置）存在 `main` 分支；构建产物 `public/` 只作为临时 artifact
传给部署步骤，**不会提交回仓库**。所以仓库里永远只有源码，不会被产物撑大。

## 本地开发

```bash
npm install          # 首次或依赖变更后
npm run server       # 启动本地预览 http://localhost:4000
npm run build        # 生成静态文件到 public/
npm run clean        # 清空缓存与 public/
npm run new -- "文章标题"   # 新建文章
```

## 目录说明

| 路径 | 说明 |
|---|---|
| `source/_posts/` | 文章（Markdown） |
| `source/` 其他目录 | 独立页面（about 等） |
| `scaffolds/` | 新建文章的模板 |
| `_config.yml` | 站点配置 |
| `_config.butterfly.yml` | 主题配置 |
| `.github/workflows/deploy.yml` | 自动部署流程 |

## 部署

推送到 `main` 分支即自动触发。也可在仓库 Actions 页面手动触发（`workflow_dispatch`）。

首次部署前需在仓库 **Settings → Pages → Build and deployment → Source** 选择
**GitHub Actions**。

## 待办

- [ ] 替换站点信息占位符（`_config.yml` 中的 title / subtitle / description / author）
- [ ] 填写主题配置中的社交链接（`_config.butterfly.yml`）
