# 博客待办与自定义清单

> 站点：https://hodgeli.github.io/
> 工程：`D:/blog/`　仓库：`Hodgeli/hodgeli.github.io`（main 分支放源码，Actions 构建发布）
> 行号对应 2026-09-29 时的配置快照，改配置前先搜关键词定位更稳妥。

---

## 一、必做 —— 现在站点还带着占位符

| # | 位置 | 现状 | 要做什么 |
|---|---|---|---|
| 1 | `_config.yml` L7 `title` | `站点标题待定` | 站点标题 |
| 2 | `_config.yml` L8 `subtitle` | `副标题待定` | 副标题（会显示在导航栏标题下方） |
| 3 | `_config.yml` L9 `description` | `站点描述待定…` | 站点描述，进首页 meta 与搜索引擎摘要 |
| 4 | `_config.yml` L11 `author` | `作者名待定` | 作者名，会进文章版权声明与 RSS |
| 5 | `_config.yml` L10 `keywords` | 空 | 站点关键词，逗号分隔 |
| 6 | `source/about/index.md` | 「待补充」 | 关于页正文（这是菜单「关于」的落地页） |
| 7 | `_config.butterfly.yml` L295 `card_announcement.content` | `This is my Blog` | 侧边栏公告文字，或 `enable: false` 关掉 |
| 8 | `_config.butterfly.yml` L59 `avatar.img` | `/img/butterfly-icon.png`（主题自带蝴蝶图标） | 换自己的头像：新建 `source/img/`，放图后改成 `/img/你的图.png` |
| 9 | `_config.butterfly.yml` L56 `favicon` | `/img/favicon.ico`（主题自带） | 同上，换自己的图标 |
| 10 | `source/_posts/hello-world.md` | 示例文章 | 删掉，或改写成第一篇文章 |
| 11 | `_config.butterfly.yml` L262 `footer.owner.since` | `2025` | 页脚版权起始年份，确认一下 |
| 12 | `_config.butterfly.yml` L206 `post_copyright.license` | `CC BY-NC-SA 4.0` | 确认用不用这个协议；不用就 `enable: false` |

> 说明：站点 `source/img/` 里的文件会**覆盖**主题自带的同名文件，所以自定义图标只需在站点侧建同名文件即可。

---

## 二、强烈建议 —— 做完才算「能被人找到」

- [ ] **`_config.butterfly.yml` L223 `post_edit`** —— 打开后文章页会出现「编辑此页」按钮，直接跳 GitHub 改 Markdown，对「源数据自持 + 网页端写作」这个方案是绝配：
  ```yaml
  post_edit:
    enable: true
    url: https://github.com/Hodgeli/hodgeli.github.io/edit/main/source/
  ```
- [ ] **`source/robots.txt`** —— 手写一个，指向 sitemap：
  ```
  User-agent: *
  Allow: /
  Sitemap: https://hodgeli.github.io/sitemap.xml
  ```
- [ ] **提交 sitemap 到搜索引擎** —— `https://hodgeli.github.io/sitemap.xml` 提交到 Google Search Console、Bing Webmaster。
- [ ] **`_config.butterfly.yml` L750 `site_verification`** —— 填各搜索引擎给的验证码（也可用 DNS/文件方式验证）。
- [ ] **百度收录** —— GitHub Pages 在百度的收录一直很差。想被百度搜到，得另装 `hexo-generator-baidu-url-submit` 主动推送，或考虑国内托管（见第六节）。
- [ ] **404 页面** —— `_config.butterfly.yml` L113 `error_404.enable: false`。注意 GitHub Pages 的 404 需要根目录有 `404.html`，光开主题开关不够，得在 `source/404.md` 建页并设 `permalink: /404.html`。

---

## 三、美化 —— 纯观感，按口味挑

### 首页
| 位置 | 说明 |
|---|---|
| L69 `index_img` / L66 `default_top_img` | **首页顶部大图。现在是空的，所以只有纯色顶栏。** 填图片 URL 或 `/img/xxx.jpg` 立刻提升观感 |
| L177 `index_layout` | 首页文章布局，**7 种**：1 左图右文 / 2 右图左文 / 3 左右交替（当前）/ 4 上图下文 / 5 图文叠加 / 6 瀑布流上图下文 / 7 瀑布流图文叠加 |
| L184 `index_post_content` | 首页摘要：`method` 1 用 description / 2 自动 / 3 截断（当前，`length: 500`） |
| L152 `subtitle.enable` | 首页副标题打字机效果（当前 `false`），开了可配 `source: 1/2/3` 拉一言/诗词 API |
| L146 `index_site_info_top` / L148 `index_top_img_height` | 首页站点信息的垂直位置、顶图高度 |

### 配色与排版
| 位置 | 说明 |
|---|---|
| L812 `display_mode` | `light` / `dark` / `auto`（跟随系统）。当前 `light` |
| L382 `darkmode` | 暗色模式按钮与自动切换时间 |
| L826 `font` / L833 `blog_title_font` | 正文字体、标题字体。**中文站建议指定中文字体**，否则不同系统渲染差异大 |
| L794 `mask` | 顶图遮罩层（让白色标题在浅色图上也能看清） |
| L815 `beautify` | 页面整体美化（标题图标、渐显动画等） |
| L91 `footer_img` / L96 `background` | 页脚背景图 / 整站背景（支持颜色或图片数组，数组则每次随机） |
| L98 `cover` | 文章封面。`default_cover` 现在是注释掉的 —— **没有封面时首页布局 3 会显得空** |
| L33 `code_blocks.theme` | 代码块配色：`light`（当前）/ `darker` / `pale night` / `ocean` / `false` |
| L34 `macStyle` | 代码块 Mac 三色圆点（当前 `false`） |
| L1066 `CDN.third_party_provider` | 当前 `jsdelivr`。**国内访问 jsdelivr 时好时坏**，可换 `staticfile`，或用 `custom` 指向自己的 CDN |

### 小彩蛋（都是开关，默认关）
L846 `activate_power_mode`（打字特效）、L857 `canvas_ribbon`（彩带）、L868 `canvas_fluttering_ribbon`、L874 `canvas_nest`（蛛网粒子）、L887 `fireworks`（烟花）、L893 `click_heart`（点击爱心）、L898 `clickShowText`（点击显示文字）、L799 `preloader`（加载动画）。

> 提醒：这些粒子/彩带类特效比较吃性能，手机端体验会明显下降，建议一次只开一个。

---

## 四、功能 —— 按需开

- [ ] **评论系统（最值得做的一个）** —— `_config.butterfly.yml` L536 `comments.use:` 现在是**空的**，文章底下没有评论区。
  - 推荐 **Giscus**（L632）：基于 GitHub Discussions，免费、无后端、无广告，和你的仓库天然契合
  - 备选 Waline(L591) / Twikoo(L623) / Artalk(L650)：都需要额外部署一个后端服务
- [ ] **数学公式** —— L453 `math.use:` 空。写算法/数学类文章就填 `mathjax` 或 `katex`
- [ ] **文章加密** —— 插件 `hexo-blog-encrypt` **已装好**，在文章 front-matter 里填 `password: xxx` 即生效，无需改配置
- [ ] **系列文章** —— L923 `series`，把多篇归到一个系列里，自动生成系列导航
- [ ] **Mermaid 流程图** —— L939，Markdown 里直接写 ` ```mermaid ` 画流程图
- [ ] **Chart.js 图表** —— L954，文章里嵌数据图表
- [ ] **访问统计** —— L441 `busuanzi` 三项全是 `false`（不蒜子，免费无后端，当前关闭）。也可用 L692 百度统计 / L695 Google Analytics / L701 Microsoft Clarity / L704 Umami
- [ ] **`noticeOutdate`** —— L244，文章超过 N 天自动提示「内容可能过时」，技术博客很实用
- [ ] **打赏** —— L210 `reward`
- [ ] **PWA** —— L1024，开启后可安装到手机桌面、离线访问
- [ ] **`instantpage`** —— L1008，改 `true` 可预加载链接目标页
- [ ] **分享按钮** —— L515 `share.use: sharejs` 已开，站点列表在 L520

---

## 五、工程与运维

- [ ] **更新 `README.md`** —— 现在写的是搭建期说明，改成「怎么写一篇文章 / 怎么发布」的日常操作手册
- [ ] **远端 `master` 分支的处置** —— 里面是你旧的 47 篇产物 HTML（推 main 时没删，等于一份远端备份）。确认不需要了就删掉，避免以后自己看混
- [ ] **`Hodgeli/blog` 空仓库** —— 已弃用，建议留着别删
- [ ] **本地写作预览** —— `cd D:/blog && node node_modules/hexo/bin/hexo server`，浏览器开 `http://localhost:4000`
- [ ] **新文章** —— `node node_modules/hexo/bin/hexo new post "标题"`，生成在 `source/_posts/`
- [ ] **`package.json` 的 `hexo` 字段** —— ⚠️ **千万别删**。`hexo-cli` 靠它识别站点根，删了 `hexo generate` 会只打印帮助信息不干活
- [ ] **`hexo` 命令必须走主包入口** —— `node node_modules/hexo/bin/hexo`，`node_modules/.bin/hexo` 会失败（hexo-cli 4.3.2 加载不了 Hexo 8 的命令）

---

## 六、访问与域名（可选，非必须）

- [ ] **自定义域名** —— 想用自己的域名，在 `source/CNAME` 写一行域名，再到域名商配 CNAME 记录。注意国内服务器绑域名要备案，GitHub Pages 不需要
- [ ] **国内访问速度** —— GitHub Pages 在国内时好时坏。若要稳定，可考虑在 Cloudflare Pages 或腾讯云 EdgeOne Pages 上做一份镜像（同一套源码，多平台部署），但**不用自定义域名就没法保证国内访问快**，这是物理限制
- [ ] **图片存放** —— 文章配图目前是「和 md 同目录走相对路径」。图片多了会让仓库变大，可考虑迁到图床（对象存储 + CDN）
