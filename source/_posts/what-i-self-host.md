---
title: 我的自托管清单：28 个服务，和 6 件我明确不做的事
date: 2026-10-23 15:05:00
categories: 自托管
tags:
  - 自托管
  - HomeLab
  - 开源
  - 阅读笔记
description: 翻译整理自 viceconsole.fyi：一台 180 欧的 N100 小主机，16GB 内存跑 28 个服务，17 个原生、11 个 Podman。附作者的三条原则、六件不碰的事，以及「什么才算好的自托管项目」。
---

> **原文**：[What I Self-Host, What I Don't, and Why](https://viceconsole.fyi/blog/2026/10/10/what-i-self-host/)
> **作者**：viceconsole.fyi（2026-10-10）
> 本文为**中文翻译整理**，非逐字翻译。为便于对照，关键论述保留了英文原文引用；服务清单按用途重新分组，原文为字母序。

## 先说结论

这是一篇「自托管清单」，但它真正的价值不在清单本身，而在**取舍**：作者列了 28 个在跑的服务，又专门写了一节讲**他试过、但决定不做的 6 件事**——后者信息量比前者更大。

三个数字最能说明问题：

| 项 | 数据 |
| --- | --- |
| 硬件 | Beelink S12 Pro（Intel N100 / 16GB 内存 / 512GB SSD）+ 6TB 机械盘 |
| 服务 | **28 个**：17 个原生、11 个 Podman，全部由 systemd 管 |
| 负载 | 内存占用约 **7.5 GB**，CPU 在 **30%–40%** 之间波动 |

换句话说：**一台 180 欧的迷你主机，跑满了一整套家庭云。**

## 一、缘起：从床底下的 Linux 主机说起

作者的自托管史比「self-hosting」这个词还早：

> I've always had a foot in the self-hosting world, long before it was called that. My freshman year of university, I ran a website from a Linux box underneath my bed. There was some downtime when my roommate got tired of the fan noise and turned it off.

大学一年级，他就在**床底下**的 Linux 机器上跑网站。唯一的宕机事故是室友嫌风扇太吵，把机器关了。后来几年陆续跑过 MythTV，再到 XBMC（就是后来的 Kodi）。

真正的转折发生在他离开印度之后。印度的流媒体价格按西方标准便宜得离谱，Netflix、Disney+（当地叫 Hotstar）、Spotify 全都有。回国后他不愿意按西方价格续费，更受不了的是**「参与度跑步机」**——尤其对他儿子：

> We wanted to limit his viewing choices to certain programming, but the constant "recommended for you" and "up next" caused conflict. While there are ways to limit content to specific titles, or disable auto-play, doing this for each service and keeping track of when client applications change and need to be reconfigured is too much work.

他们想限制孩子能看什么，但满屏的「为你推荐」和「接下来播放」不断引发冲突。虽然每个服务都能限制内容、关掉自动播放，但**要一家家设、还要盯着客户端 App 改版后重新配**，工作量实在太大。

于是他换了个方式「剪线」——不用流媒体，改用自托管的 **Jellyfin**。接下来一年半，Jellyfin 打开了自托管的大门，其他服务一个个搬了进来。收益是「稳定」：

> No longer am I constantly confronted with unnecessary site redesigns, new features of questionable value, and a barrage of e-mails about terms-of-service updates, binding arbitration, data breaches, etc. I read the release notes of new versions of the software I host and decide if and when I want to upgrade.

不再被莫名其妙的改版、价值可疑的新功能、以及关于服务条款更新／强制仲裁／数据泄露的邮件轰炸。他只看自己托管软件的版本发布说明，然后**决定要不要升、什么时候升**。

## 二、三条原则

### 原则一：除 VPN 外，一个服务都不暴露到公网

> With the exception of VPN servers that run on my router, I do not expose any services directly to the public internet. I don't care how convenient it would be, or how secure an application is. Especially with AI-assisted hacking, I simply don't think it's wise.

除了跑在路由器上的 VPN 服务，**他不把任何服务直接暴露到公网**。不管多方便、不管应用多安全——尤其是在 AI 辅助攻击的时代，他认为这根本不明智。

他还有一个被动优势：ISP 对 IPv4 用了 [CGNAT](https://en.wikipedia.org/wiki/Carrier-grade_NAT)，家庭网络本来就没法从公网 IPv4 直接访问。VPN 只在 IPv6 上可达，代价是**几乎无法在公共 WiFi 下使用**（公共 WiFi 很少提供 IPv6），出门只能靠蜂窝数据——前提是有信号。

### 原则二：能原生就原生

> Love: a service that's a single Go binary. A service that only comes as a Docker compose file and wants to run MySQL, Redis, and three other containers? I'm already looking for an alternative.

**最爱的：一个 Go 单二进制的服务。** 而一个只提供 Docker compose、还要求跑 MySQL、Redis 加另外三个容器的服务？他已经在找替代品了。

只要依赖不夸张，原生部署**更快、更省资源**，而且管理工具和命令在所有服务之间通用。不用为了跑一条命令先 `docker exec` 进某个容器、发现里面没装 `curl`、发现另一个用的是 busybox 所以参数全不一样、还要对付虚拟网络和宿主机端口映射——**这些心智负担直接归零**。

### 原则三：不碰 Docker，用 Podman + systemd

> Related, I don't do Docker anymore. It's not really a principled position, but I grew tired of having to manage a completely separate service control system on my server. I'm already using systemd, and at this point Podman's integration with systemd is excellent.

这不算什么立场问题，纯粹是**不想在服务器上再维护一套独立的服务控制系统**。既然已经在用 systemd，而 [Podman 与 systemd 的集成](https://docs.podman.io/en/v5.0.1/markdown/podman-systemd.unit.5.html)现在足够好，那就统一用 systemd。

## 三、硬件：180 欧的小主机

| 部件 | 型号 / 规格 |
| --- | --- |
| 主机 | Beelink S12 Pro |
| CPU | Intel N100 |
| 内存 | 16 GB |
| 系统盘 | 512 GB SSD |
| 存储 | 外接 6 TB 机械盘（媒体库） |
| 价格 | **€180**（赶在内存涨价潮之前买的，同款现在 €359） |

他在 Hacker News 上的评论引来了不少疑问：**16 GB 内存怎么跑得动这么多东西？** 他的回答是——确实做了一些降低资源占用的选择，但归根结底：

> It turns out you don't need much hardware to run a lot of stuff.

跑很多东西并不需要很强的硬件。当然，这台机器上没有任何本地推理，但**所有非 AI 的东西，要么开箱即用，要么稍作配置就能跑**。

## 四、28 个在跑的服务

原文按字母序排列，这里按**用途**重新分组，方便扫读。「部署」列是作者实际采用的方式。

### 媒体：影视、有声书、音乐

| 服务 | 用途 | 部署 |
| --- | --- | --- |
| [Jellyfin](https://jellyfin.org/) | 影音服务器，自托管界的 Netflix 替代 | Podman |
| [Audiobookshelf](https://audiobookshelf.org/) | 有声书与播客服务器，章节处理做得很好 | 原生 |
| [Gonic](https://github.com/sentriz/gonic) | Subsonic 兼容的音乐服务器（Go 写的） | 原生 |
| [MPD](https://www.musicpd.org/) | 音乐播放守护进程，跑了 23 年的老牌方案 | 原生 |
| [Snapcast](https://github.com/snapcast/snapcast) | 全屋同步音频 | 原生 |
| [Yubal](https://github.com/guillevc/yubal) | 下载 YouTube Music 播放列表并正确命名、整理、打标签 | Podman |
| [Automatic Ripping Machine (ARM)](https://github.com/automatic-ripping-machine/automatic-ripping-machine) | 自动翻录并转码 DVD | Podman |
| [Transmission Daemon](https://github.com/transmission/transmission/) | BT 下载 | 原生 |
| [slskd](https://github.com/slskd/slskd) | 「懂的都懂」 | 原生 |

作者特别说明，2026 年了**他还在翻录 DVD**——因为「剪线」之后，这既是新内容的来源，也是拿到**英法双语**素材的途径。

**Snapcast** 是他认为值得单独写一篇的服务：

> Think Sonos, but without the expensive vendor lock-in and planned obsolescence.

像 Sonos，但没有昂贵的厂商锁定和计划性淘汰。配置起来确实复杂，但跑得很好——他打算再买几台设备专门当接收端。

### 照片与备份

| 服务 | 用途 | 部署 |
| --- | --- | --- |
| [Immich](https://immich.app/) | Google Photos 替代品 | Podman |
| [Backrest](https://github.com/garethgeorge/backrest) | [Restic](https://restic.net/) 备份的 Web 界面 | 原生 |
| [Syncthing](https://syncthing.net/) | 单向同步，给 Immich 的照片做异地副本 | 原生 |

**Backrest** 是整套方案里最不能省的一环：Restic 的去重和压缩很好用，而 Backrest 让保留策略变得容易管理，失败时通过 Gotify 告警。照片（Immich）尤其需要备份。

**Syncthing** 在作者的 MacBook 上配成「仅接收」的单向同步，让 Immich 里的所有照片最终都会有一份落到 MacBook 的外置硬盘上。

### 基础设施

| 服务 | 用途 | 部署 |
| --- | --- | --- |
| [Caddy](https://caddyserver.com/) | Web 服务器 + 反向代理，自动申请 Let's Encrypt 证书 | 原生 |
| [Cockpit](https://cockpit-project.org/) | Web 管理控制台，用系统自带的认证 | 原生 |
| [Beszel](https://beszel.dev/) | 轻量监控面板（CPU/内存/磁盘/温度/电池） | 原生 |
| [Uptime Kuma](https://github.com/louislam/uptime-kuma) | 服务存活探测 | Podman |
| [Gotify](https://gotify.net/) | 自托管推送通知 | 原生 |
| [Homepage](https://gethomepage.dev/) | 所有服务的统一入口面板 | Podman |
| [Samba](https://www.samba.org/) | 局域网文件共享 | 原生 |
| [Forgejo](https://forgejo.org/) | 自建 Git 远端（Gitea 的 fork，单二进制） | 原生 |
| [PocketBase](https://pocketbase.io/) | SQLite + Web 管理界面，被当成通用 CRUD 前端用 | 原生 |

几个细节值得抄：

- **Caddy 是「服务变多之后才懂的痛」**。一开始他觉得用本地 DNS 名甚至 IP+端口就够了，直到服务越加越多、有些强制要 HTTPS。现在所有服务在局域网（或 VPN）里都有 HTTPS 和好记的子域名，**加一个新服务只是改一行 Caddyfile**。
- **Uptime Kuma 是被老婆逼出来的**。在几次「X 又不好使了」之后，他意识到得有个东西盯着哪些服务在跑、哪些挂了。它支持 ping 设备、查 Podman 容器状态、探测 HTTP 2XX、甚至解析 JSON 做健康检查，挂了就通过 Gotify 通知（当然要重试几次）。
- **Homepage 是「服务多到自己都记不住」的产物**：

  > At some point I realized I was running so many services, I needed another service just to keep track of them all.

  某天他发现自己跑的服务太多，**需要再来一个服务专门用来管这些服务**。

- **Samba 是「老技术反而最好用」的典型**：

  > It's funny how a file sharing protocol first developed in the 1980s and most associated with Windows remains the best option for cross-platform file sharing on a LAN.

  一个 1980 年代开发、和 Windows 绑定最深的老协议，至今仍是局域网跨平台文件共享的最佳选择——这事挺有意思的。

### 家庭与安防

| 服务 | 用途 | 部署 |
| --- | --- | --- |
| [Frigate](https://github.com/blakeblackshear/frigate) | 网络录像机（NVR），带 AI 目标检测 | Podman |
| [Home Assistant](https://www.home-assistant.io/) | 智能家居中枢 | Podman |

**Frigate** 是作者最满意的服务之一：接 8 个 IP 摄像头，能识别「有人/有车进入车道」，并和 Home Assistant 联动（后院检测到人就打开摄像头补光灯）。他之前用 Zoneminder，「因为我这个年纪的人都知道它」，但很快就发现 Zoneminder 已经过了巅峰期。

这里有个很实用的资源优化技巧：**所有摄像头都跑在低于其标称分辨率下**，主要是为了避免 WiFi 拥塞；而大多数摄像头还提供一个更低分辨率的 RTSP 子码流，Frigate 就用它做移动侦测和目标检测。这样既避免了视频处理吃掉过多 CPU 和内存，也避免了录像撑爆硬盘。分辨率仍然足够认脸，而且他所在国家的隐私法禁止拍摄公共通道，所以摄像头本来也不对着远处。

**Home Assistant** 他认为值得单独写一篇：一旦用上，就很难想象怎么在 Google Home、Amazon Alexa、Apple Home 这类封闭生态里实现同样的效果。虽然设备厂商开始统一到 Matter 协议、情况好转了，但 HA 给的控制力和灵活度很难被超越。代价是**学习曲线陡**，而且他还在认真思考：万一服务器挂了，怎么在不牺牲家庭功能的前提下兜底。

### 个人事务

| 服务 | 用途 | 部署 |
| --- | --- | --- |
| [Vaultwarden](https://github.com/dani-garcia/vaultwarden) | Bitwarden 的开源兼容实现（密码管理） | Podman |
| [Actual Budget](https://actualbudget.org/docs/releases/) | 预算与记账 | Podman |
| [Vikunja](https://vikunja.io/) | 待办与看板（Trello 替代） | Podman |
| [Readeck](https://readeck.org/en/) | 网页剪藏与归档 | 原生 |
| [FreshRSS](https://www.freshrss.org/) | RSS 阅读器 | 原生 |

- **Vaultwarden**：他用了多年 KeePass，但一直没解决同步问题，索性不在手机上登录任何东西；而他太太用的 LastPass 出过多次泄露事故，自动填充也不太好用。Vaultwarden 是 Bitwarden 的开源 API 兼容实现，**能用官方 Bitwarden 客户端**，在局域网内自动同步，出门则走 VPN 手动触发。他的隐忧是 Bitwarden 官方哪天可能对 Vaultwarden 翻脸、破坏客户端兼容性——目前已知的另一个兼容客户端是 [Keyguard](https://github.com/AChep/keyguard-app)，但它不开源、还是免费增值模式。
- **Actual Budget**：虽然支持从银行自动导入流水，但他不用这个功能——每月底手动下载上个月的流水（优先 OFX，没有就 CSV）再导入。因为他主要拿它**记支出**，而不是真的「做预算」。投资账户仍在用云服务，他打算哪天再搬。
- **Vikunja**：用了十年 Trello，直到今年 Trello 那次[持续多日的大故障](https://trello.status.atlassian.com/incidents/h11gfkgvjhhk)才下决心换。筛选方案时他有一条硬标准：

  > I ruled out anything that involved spinning up a PostgreSQL or MySQL database for a service that will serve two users.

  **一个只服务两个用户的服务，就别让我为它开 PostgreSQL 或 MySQL。** Vikunja 默认用 SQLite，单二进制部署，正好。
- **Readeck**：研究生时代他是 Zotero 重度用户，但很多年不写参考文献了，只需要「保证以后还能打开读过的东西」。先试过 Wallabag，但**付费墙内容归档不了**（哪怕手机上已登录）；Readeck 则能把手机上看到的内容直接归档到服务器。
- **FreshRSS**：现在他基本只逛两个网站，用得不多，但订阅了若干自托管项目的 GitHub Releases，用来跟进新版本的功能和修复。

## 五、6 件我明确不做的事

这一节是全文最值得读的部分——**知道别人为什么不做什么，比知道他在做什么更有用**。

### 1. *arr 全家桶（Sonarr / Lidarr / Radarr）

> Every time I read about setting it up, it just sounds like a resource-intensive mess that's fundamentally prone to frequent breakage. That's the opposite of what I'm looking for when choosing self-hosted services.

每次读到它的部署教程，感觉都是一个**吃资源、且天然容易频繁出故障**的烂摊子。这和他选自托管服务的标准正好相反。

### 2. Collabora Online（网页版 Office）

彻底和 Google 分手很诱人，但 Google Docs 作为「方便存储和分享」的工具实在难打。他的做法是：**没有非上云不可的理由时，就用本地 LibreOffice Writer / Calc**。既然已经有共享网络盘了，再跑一个网页 Office 套件（Collabora）显得没什么意义。

### 3. Firefly III

在 Actual Budget 之前试过，本以为需要内置多币种支持。结果配置复杂、要跑多个容器（还有一个专门用来导入数据的容器）。Actual Budget 简单得多。外币账户他用自己写的小脚本做汇率换算，Actual Budget 里一切保持美元。

### 4. OwnTracks / Dawarich（位置记录）

他喜欢 Google Maps Timeline，但 Google 把位置数据限制在单设备之后，他想找个自托管替代。可惜 OwnTracks 的 Android 客户端**无论怎么调电池和定位设置，都没法稳定上报位置**。Dawarich 是另一个选项，但它「至少要」跑四个容器（PostgreSQL、Redis、Sidekiq、Web 应用）——**资源投入和能拿到的价值不成比例**。

### 5. Music Assistant

如果你本来没有满意的音乐方案，它可能不错。但作者已经有 Gonic + Snapcast + MPD 在良好运转，而 Music Assistant 给人感觉想「接管一切」——比如它会不停重排他的 Snapcast 设备分组。

### 6. 自建邮件服务器

> Self-hosting e-mail seems like a lot of work for very little benefit. I cannot risk not being able to send or receive e-mails.

自建邮件**工作量巨大、收益极小**，而他承担不起收发不了邮件的风险。他打算以后从 Gmail 迁到付费服务商，而不是自己搭。

## 六、结论：16GB 能跑多少

> That's 17 native services and 11 Podman services, all managed by systemd.

17 个原生 + 11 个 Podman，全部由 systemd 管理。`htop` 显示内存占用约 **7.5 GB**，CPU 在 **30%–40%** 之间波动。

> Given how expensive computer hardware has become due to the AI crunch, I hope we'll continue to see self-hostable projects that prioritize simplicity and efficiency.

考虑到 AI 热潮把硬件价格推得这么高，他希望社区能继续出现**优先考虑简洁与效率**的自托管项目。

**我的读后感**：这篇文章最反直觉的地方，是它把「自托管」从一种技术炫技拉回到一种**成本核算**。作者反复在算的其实只有一件事：*这个服务要我付出多少资源、多少心智负担，换回来多少价值？* ——所以他会为了一个只服务两个人的待办应用拒绝 PostgreSQL，会为了省掉一层容器管理而彻底放弃 Docker，会因为「至少四个容器」而放弃位置记录。而那台 180 欧的小主机能跑 28 个服务，靠的不是硬件，是**每个选择都足够克制**。

对想入门的人来说，最该抄的不是他那 28 个服务，而是他那三条原则和那一节「我不做什么」。

## 原文出处

- 原文：[What I Self-Host, What I Don't, and Why](https://viceconsole.fyi/blog/2026/10/10/what-i-self-host/)（viceconsole.fyi，2026-10-10）
- 作者在 Hacker News 上的相关[讨论](https://news.ycombinator.com/item?id=49985548#50014938)
