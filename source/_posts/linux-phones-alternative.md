---
title: Linux 手机会成为 Android/iOS 双寡头的真正替代品吗？
date: 2026-10-20 16:40:00
categories: 开源生态
tags:
  - Linux
  - 移动操作系统
  - 开源硬件
  - 阅读笔记
description: 翻译整理自 Amos Batto：五年前 Linux 手机热潮为何没接住？如今 SoC、内核支持、移动界面三个瓶颈同时松动，剩下的障碍不再是技术，而是公司。
---

> **原文**：[Will Linux phones become a viable alternative to the Android/iOS duopoly?](https://amosbbatto.wordpress.com/2026/10/05/linux-phones-alternative/)
> **作者**：Amos Batto（2026-10-05）
> **授权**：原文以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) 发布，可自由转载与改编，需署名
> **原文下载**：[PDF](https://amosbbatto.wordpress.com/wp-content/uploads/2026/10/linuxphonesviablealternative-8.pdf) / [ODT](https://amosbbatto.wordpress.com/wp-content/uploads/2026/10/linuxphonesviablealternative-8.odt)
> 本文为**中文翻译整理**，非逐字翻译。为便于对照，关键论述保留了英文原文引用；数据表格按原文重排。

## 先说结论

作者的核心判断是：**Linux 手机这次可能真的要成了**，但不是因为它变强了，而是因为三个卡了十年的瓶颈同时松动了。

| 瓶颈 | 过去的状况 | 现在 |
| --- | --- | --- |
| **硬件性能** | Linux SoC 弱、能效差、驱动靠社区硬啃 | RK3588S 终于够用；高通把 IoT 芯片的 10–15 年支持带进来了 |
| **内核寿命** | Android 内核只活 2–4 年，手机跟着一起死 | 旗舰芯片给到 8 年，且承诺两次内核升级 |
| **移动界面** | 各家自建孤岛，随公司一起消失 | Phosh / Plasma Mobile / Lomiri 都长在桌面栈上，公司倒了软件还在 |

而**剩下的障碍不再是技术，是公司** —— 愿意做、会做、且撑得住的公司太少。这正是原文最后一节的标题，也是全篇的落点。

原文开篇把这种落差讲得很直白：

> Five years ago, Linux phones looked like they were poised to become a viable alternative to the Android/iOS duopoly that has an iron grip on the mobile phone industry. Sadly, after a brief flash of activity and community engagement with the release of the Purism Librem 5 and the PINE64 PinePhone in 2020, the Linux phone market has generally stagnated.

五年前，Linux 手机看起来正要成为 Android/iOS 双寡头的可行替代。可惜在 2020 年 Librem 5 和 PinePhone 带来一阵短暂的热闹之后，这个市场整体停滞了。

作者并不认为移动 Linux 会动摇 Google 或苹果的生意，但他认为**一个类似「Linux PC」的小市场已经成熟**——就像今天你可以从 TUXEDO、System76、Purism、Slimbook、Star Labs 等十几家小公司买到预装 Linux 的电脑那样。

## 一、五年前那波热潮，为什么没接住

2020 年前后的景象确实热闹：Linus Tech Tips 在测评这两台手机；Mrwhosetheboss 那条「Linux 手机会不会干掉 Android」的视频拿了 780 万播放；PinePhone 被移植到 20 个不同的 Linux 发行版；Waydroid 让 Android 应用可以跑在 Linux 容器里；KDE 采纳 Kirigami、GNOME 采纳 Adwaita，两边的应用都开始能在桌面和移动之间自适应。

但那个未来没来。作者归因于五件事：

- Purism 和 PINE64 自身出了状况
- 可用的 Linux SoC 根本撑不起一台现代智能手机
- 硬件行业拿不出驱动开源的替代方案
- Plasma Mobile 和 Phosh 当时都还很稚嫩
- 没有一个好发行版能在「正常的集成式移动 SoC + Android 内核」上跑这些界面

再叠加 PinePhone / Librem 5 的实际体验不佳、PinePhone Pro 的问题、Librem 5 的退款风波，人们既失去了热情，也不愿再赌下一台。

顺带一个冷知识：25 年来出现过 **29 种**商业移动 Linux——从 Sharp Zaurus、G.Mate Yopy、Motorola A760 算起，还有 EZX、MotoMagx、Maemo、LiMo、Moblin、Meego、Tizen、Firefox OS、webOS、Ubuntu Touch、Sailfish OS。它们大多被笼统地归到「Linux」这个标签下，但作者提醒：**Tizen 和 Firefox OS 在架构上和 Android 的距离，跟它们和标准桌面 Linux 的距离差不多远。**

这些系统并没有全死：MeeGo 的代码在 Jolla 手里继续长成 Sailfish OS；Firefox OS 变成低端机上的 KaiOS；Ubuntu Touch 由 UBports 志愿者接手；webOS 和 Tizen 则活在 LG 和三星的电视里。

## 二、SoC 的两难：弱而长寿，还是强而短命

这是全篇的技术地基。作者指出，支持 Linux 的 SoC 基本都用在单板计算机、机顶盒、IoT、工业和汽车嵌入式场景，价格点低，所以：

- **制程老**（28nm、16nm 这种），性能弱、能效差
- 但**支持周期极长**——汽车里塞几十颗 SoC，光设计就要 3–5 年，之后还得跑 20 年

而支持 Android 的移动 SoC 性能很强，**却只生产 2–3.5 年**。

根子是钱。芯片厂卖一颗 Linux SoC 能卖 10–15 年，但量太小，摊不平先进制程的成本：

> It is enormously expensive to design a chip at the cutting edge of the silicon industry. Silicon Analysts estimates that fabbing a wafer at TSMC costs an average of $19,500 at a 3nm node, but only $3000 at a 28nm node.

在硅工业的最前沿设计一颗芯片极其昂贵。Silicon Analysts 估算，台积电 3nm 节点每片晶圆平均 $19,500，而 28nm 只要 $3,000。要用 3nm，得多掏 **4–6 亿美元**，而且每代还在涨。

省钱的另一招是用老一代 Cortex 核（ARM 授权费更低）和一堆低功耗的 A5x 系列核。作者点名 NXP：i.MX 95 塞了 6 个 Cortex-A55，而「更合理的做法是 2 个 A78 加 4 个 A55」；制程还是 16nm，比上一代 i.MX 8M Plus 的三星 14nm 还退了一步。

**代价最终落在手机厂头上。** 因为没有集成式移动 SoC，Linux 手机得把 WiFi、蓝牙、基带、GPS、音频 DAC、充电控制、USB-C 控制全部拆成独立芯片：

- Librem 5：**74 颗 IC、4 块板共 1267 个元件**，史上最复杂的手机；用来替代一颗集成 SoC 的那 6 颗芯片占了 **1483.2 mm²，是骁龙 8 的 10 倍**
- PinePhone：已经极简，仍有 **24 颗 IC、627 个元件**；而普通 Android 手机通常只有 300–400 个元件

元件多不只是贵，还更费电——半打大制程芯片的功耗，怎么都比一颗 4nm 以内、专门优化过能效的集成 SoC 高。再加上 Linux 手机很难协调这么多芯片一起进低功耗和睡眠模式，**续航根本不可能追上 Android 手机**。

## 三、RK3588S 改变了游戏规则

2022 年 Rockchip 发布 RK3588 和低功耗版 RK3588S，作者的措辞是「从根本上改变了做一台像样 Linux 手机的前景」：**4×2.4GHz Cortex-A76 + 4×1.8GHz Cortex-A55 + Mali-G610 MP4**，终于有一颗 Linux SoC 的性能够格了。

目前基于它设计的机器：Liberux NEXX、Dawndrums Divine D.；Purism 也刚在论坛宣布下一代手机「正在设计中」，且不会再用 i.MX 平台，因此**很可能就是 RK3588S**。

但作者没有吹。RK3588S 是 8nm，比当今 2nm 的顶级水平落后四代；今天 4nm 的低端骁龙 4 Gen 4 单核还比它强 25%；持续负载超过 30 秒，RK3588S 的性能会掉 10–15%。等基于它的手机上市时，性能会明显不如市面上任何一台 Android 手机。

作者对此的判断很务实：

> At a certain point, more processing power has diminishing utility, and the RK3588S crosses that threshold for most people.

到了一定程度，更强的算力带来的效用是递减的，而 RK3588S 对大多数人来说已经跨过了那条线。只要你不打 3D 游戏、不拍高分辨率视频，性能就不是瓶颈。

**散热是真问题。** PinePhone 因为没好的均热片，SoC 和基带都很烫；Librem 5 用导热硅脂把 SoC 贴到 LCD 背板上，SoC 不烫了，但屏幕和铝框烫手。而均热板要专门设计，小批量手机根本用不起——所以 RK3588S 必须靠节流来迁就手机的功耗与散热包络。

### 开源支持：一半坏消息，一半好消息

坏消息：Rockchip 从没在 `opensource.rock-chips.com` 上公布这颗芯片的文档，还在 2025 年底把那个站关了。2024 年 12 月 21 日，Raspberry Pi 替代方案领域最有影响力的测评者 Jeff Geerling 在 X 上说：

> I was told Rockchip no longer considers RK3588 to be an 'open source' chip. In practice, that means Rockchip no longer contributes RK3588 code to open-source projects and they also decided not to sell RK3588 directly to SBC vendors.

有人告诉他，Rockchip 已不再把 RK3588 当作「开源」芯片。实际影响是：Rockchip 不再向开源项目贡献 RK3588 代码，也决定不再直接向单板机厂商出售 RK3588。

好消息：Rockchip 仍在 GitHub 上更新它的公开内核代码，而且 Collabora 多年来一直在做 mainline 支持，Rockchip 也把 Collabora 列为合作伙伴。四年下来，**现在跑自由/开源驱动已经基本够用**：

- 只剩两个专有件：开机时要执行的 Synopsys DDR 时序训练 blob，以及 GPU 需要的 `mali_csffw.bin` 固件
- 其余 blob 要么已被替换，要么根本不需要
- NPU 有 FOSS 驱动；Collabora 还做出了可替代 `bl31.elf` 的 FOSS 版 Trusted Firmware-A
- 硬件视频解码（VP8/VP9/H.264/H.265）已通，硬件编码在推进中

这一点很关键：**RK3588S 的 CPU/GPU 算力足够用软件完成图像处理和视频编码**，所以它能像正常手机一样拍照录像，只是慢一点、费电一点。而过去的 Linux 手机是「算力不够，根本做不好相机」——PinePhone 拍照慢到痛苦，Librem 5 每拍一张 Millipixels 要卡 3–4 秒。

替代方案不是没有，但都不如它：Nvidia Tegra Orin（blob 更多、更不自由）、Allwinner A733（12nm、性能更弱，且 Allwinner 常年不公开源码、违反 GPL）、NXP i.MX 95（有 mainline 支持，但 16nm + 6 个 A55，性价比差）。

还有一个未来项：Rockchip 承诺 2027 年推出 **RK3668**（4×Cortex-A730 + 6×Cortex-A530，5/6nm），意味着这条升级路线还能走下去。这一点很重要——Purism 当年押注 i.MX 8M Quad，本以为能升到 14nm 版本，结果 NXP 在 i.MX 8M Plus 上砍掉一半 GPU 核心、去掉了 DisplayPort，整条升级路径就断了。

### 可用的 Linux 手机 SoC 对比

以下数据按原文表格重排（Geekbench 6）：

| SoC | 制程 (nm) | 规格 | 单核 | 多核 | 相关机型 |
| --- | --- | --- | --- | --- | --- |
| Allwinner A64 | 40 | 4×1.2GHz A53, Mali-400 MP2 | 109 | 278 | PinePhone |
| NXP i.MX 8M Quad | 28 | 4×1.5GHz A53, GC7000 Lite | 146 | 477 | Librem 5, Liberty |
| NXP i.MX 8M Plus | 14 | 4×1.8GHz A53, GC7000 UltraLite | — | — | Mecha Comet |
| NXP i.MX 95 | 16 | 6×2.0GHz A55, Mali-G310 | 350 | 1300 | Mecha Comet |
| Rockchip RK3399 | 28 | 2×1.8GHz A72 + 4×1.4GHz A53, Mali-T860 | 278 | 708 | PinePhone Pro |
| Rockchip RK3566 | 22 | 4×2.0GHz A55, Mali-G52 MP2 | 140 | 450 | 传闻中的 PinePhone 2 |
| **Rockchip RK3588S** | **8** | **4×2.4GHz A76 + 4×1.8GHz A55, Mali-G610 MP4** | **730** | **2250** | Liberux NEXX, Dawndrums Divine D., 可能是 Librem 5 v2 |
| UNISOC Tiger T606 | 12 | 2×1.6GHz A75 + 6×1.6GHz A55, Mali-G57 MP1 | 375 | 1350 | Jolla C2 |
| MediaTek Helio G81 | 12 | 2×2.0GHz A75 + 6×1.7GHz A55, Mali-G52 MC2 | 432 | 1416 | Commodore Callback 8020 |
| MediaTek Dimensity 900 | 6 | 2×2.4GHz A78 + 6×2.0GHz A55, Mali-G68 MP4 | 1003 | 2423 | Furilabs FLX1/s/s+ |
| MediaTek Dimensity 6300 | 6 | 2×2.4GHz A76 + 6×2.0GHz A55, Mali-G57 MC2 | 780 | 1940 | Brax BraX3 |
| MediaTek Dimensity 7050 | 6 | 2×2.6GHz A78 + 6×2.0GHz A55, Mali-G68 MC4 | 970 | 2330 | Volla Phone Quintus |
| MediaTek Dimensity 7100 | 4 | 4×2.4GHz A78 + 4×2.0GHz A55, Mali-G610 MC2 | 995 | 2900 | Jolla Phone (2026) |
| MediaTek Dimensity 7300 | 4 | 4×2.5GHz A78 + 4×2.0GHz A55, Mali-G615 MC2 | 1040 | 3000 | Volla Phone Plinius |
| Qualcomm QCM4490 | 4 | 2×2.4GHz A78 + 6×2.0GHz A55, Adreno 613 | 900 | 2318 | — |
| **Qualcomm QCM6490** | 6 | 4×2.7GHz A78 + 4×1.95GHz A55, Adreno 643L | 950 | 2850 | MNT Vector, Fairphone 5, SHIFTphone 8 |
| Qualcomm QCM8850 | 4 | 1×3.2GHz Gold-Plus + 4×2.8GHz Gold + 3×2.0GHz Silver, Adreno 740 | 1100 | 3300 | 可能是 MNT Vector |
| Snapdragon 4 Gen 4 | 4 | 2×2.3GHz A78 + 6×2.0GHz A55, Adreno 613 | 920 | 2210 | — |
| Snapdragon 6 Gen 4 | 4 | 1×2.3GHz A720 + 3×2.2GHz A720 + 4×1.8GHz A520, Adreno 810 | 994 | 3082 | — |
| Snapdragon 7 Gen 4 | 4 | 1×2.8GHz A720 + 4×2.4GHz A720 + 3×1.84GHz A520, Adreno 722 | 1150 | 3700 | — |
| Snapdragon 8 Gen 5 Elite | 3 | 2×3.8GHz Oryon Prime + 6×3.32GHz Oryon Performance, Adreno 829/840 | 2400 | 8700 | — |

看这张表就明白作者的判断了：RK3588S 的 730/2250 放在「Linux SoC」里是断层第一，但放到 Android 阵营里只相当于入门机水平——**够用，但不惊艳**。

## 四、新路线：高通 IoT 芯片

过去高通根本不认真做支持 Linux 的强处理器。但 IoT 场景开始需要能跑 AI、能处理多路视频的算力，而 IoT 设备生命周期长，比 Android 更适合 Linux。

转折点是 2023 年 3 月：高通宣布 6nm 的 **QCM6490**（集成基带）同时支持 Android、Linux、Ubuntu、Windows IoT Enterprise 四个系统，并配套 **Product Longevity Program——软件支持到 2036 年 7 月**。

这对 Linux 手机是精准命中：Linux 手机开发周期长、年销量低，恰恰需要超长支持来摊薄投入。Fairphone 5 和 SHIFTphone 8 就是围绕 QCM6490 设计的。

同系列还有：

| 型号 | 支持截止 | 评价 |
| --- | --- | --- |
| QCM4490（4nm） | 2030-04 | 太短，不适合 Linux 手机 |
| **QCM6490（6nm）** | **2036-07** | 作者认为是最佳选择 |
| QCM8850（4nm） | 2033-04 | 可以降频用，但支持短了 |

用 IoT 芯片的最大好处是**设计变简单**：集成度高，电路板复杂度大幅下降；高通给参考设计，改一改就行，迭代次数和测试量都少得多。

甚至可以不自己设计硬件——找 SHIFT 或 Fairphone 代工，再装 Linux，就像 Murena 和 iodé 卖 Fairphone/SHIFT 并刷自家 AOSP 那样。这样既省掉硬件设计的时间和成本，还能打「环保与伦理」的卖点，保修也能一并委托。

MNT Research 的 7 寸 Vector 平板就在走这条路（QCS6490 / QCS8850，SoM 板可换）。他们也测过 RK3588，结论是：

> "gets too hot for a component-dense mobile device, making prolonged use uncomfortable."

对元件密集的移动设备来说太烫了，长时间使用会不舒服。

代价是 **blob**。高通的 Adreno GPU、音频 DSP、NPU/计算、VPU 视频编解码、网络加速（IPA）都要 blob。这些是可选的——可以退回软件实现，只是更热更费电。但 **WiFi、蓝牙、基带这三个 blob 不可省**，除非你额外加独立芯片，那又会推高成本和复杂度。

这里有个作者点出的悖论：愿意为了隐私加硬件断电开关的用户，往往也最在意那三个开机 blob（尤其是跑 hypervisor 和 TrustZone 加密的那个）。RK3566、RK3588、i.MX 95 开机也要 blob，但那只是个 Synopsys 的小文件，只负责 DDR 时序训练；高通的 QCM 系列 blob 规模大得多。

## 五、Android 内核的寿命陷阱

这是全篇最尖锐的一节。

2020–2022 那波之所以让人兴奋，是因为 Librem 5 和 PinePhone **跑的是 Linux 内核**。而其他大多数 Linux 手机是把用户空间跑在 [libhybris](https://github.com/libhybris/libhybris) 之上，加载 Android 库和驱动、把调用翻译成 libc/musl，从而配合 Android 的 Bionic。

用 Android 内核的好处很实在：**能用上骁龙、天玑这种现代集成 SoC**，性能和能效直接对齐 Android 手机。坏处同样实在：**手机寿命被内核锁死**。

Google 历史上只给每个 Android 内核 4 年安全更新，而且往往得升一次 Android 大版本才拿得到（因为 Google 通常只支持每个 Android 版本 3.5 年）。芯片厂给智能手机 SoC 的支持更短——只卖 2–3 年，高端型号一年后需求就枯竭，所以历史上只给 1–3 年系统更新、2–4 年安全更新，而且**提供的驱动和专有 blob 是为某个特定内核写的，根本升不上去**。

对比一下两种承诺：

- Purism 宣传 Librem 5 会有 "lifetime updates that actually extend your phone's life"（真正能延长手机寿命的终身更新）
- PINE64 承诺 PinePhone 及其备件至少卖 "at least 5 years"（5 年）

这不是营销话术——它们用自由/开源驱动和可持续升级的 Linux 内核，不依赖「只兼容某个内核版本」的专有 blob，所以寿命远超任何在售 Android 设备。

### 两个现成的反面教材

**FuriLabs FLX1**（2024-07 发货）用的是 MediaTek Dimensity 900，2021 年 5 月随 Android 11 发布，内核 `android11-5.4`。Google 在 **2026-01-01** 停止支持这个内核，Linux 5.4 也在 **2025-12-03** 停止维护。MediaTek 不提供大版本内核升级，驱动里的 blob 也升不了——于是 FLX1 及后续的 FLX1s / FLX1s+ **卡在一个不再有安全补丁的 Android 11 内核上**。而它们又用 Andromeda（Waydroid 的自定义分支，基于 AOSP 13，2026-03 已停止安全更新）来跑 Android 应用，等于把一扇没锁的门对着整个 Android 恶意软件生态。

**Jolla C2**（€369，2024-09 发货）用 UNISOC Tiger T606（2021-09 发布），内核版本号是 `5.4.233-android12-9-g9c3a5d5b97e3`——大致是 Linux 5.4.233 加上 Google 的 Android 12 改动，和 FLX1 是同一个已停止支持的内核。Jolla 甚至没升到 5.4.302（Linux 5.4 的最后一个维护版）。而且 C2 的内核源码拖到 2025-05-20 才发布，比发货晚了 8 个月。

作者补了一刀：即便升到 5.4.302，那个内核发布时也带着 **1539 个未修复 CVE**；而 Linux 平均每 **2.5 天**就出一个新的严重 CVE。

### 为什么这个问题特别致命

> The problem with the short lifespan of Android kernels is that Linux phones typically take longer to develop and bring to market, and then they are sold for more years than most Android phones.

Android 内核寿命短这个问题之所以要命，是因为 Linux 手机通常开发更久、上市更慢，上市后又要卖更多年。开发周期和销售周期都比 Android 手机长，内核寿命却更短——这个剪刀差是结构性的。

## 六、Android 阵营正在变好：8 年支持

好消息是，这个剪刀差正在被 Google 自己抹平。

逻辑很清楚：苹果承诺至少 5 年、通常给到 6 年以上；Google 的商业模式不靠计划性淘汰（用户越多，广告数据越多），所以延长寿命符合它的利益。

时间线：

| 时间 | 事件 |
| --- | --- |
| 2020-08 | 三星宣布 S10 起 S/Note/Z 系列给 3 年系统 + 安全更新 |
| 2021-10 | Google 宣布 Pixel 6 起 3 年系统 + 5 年安全更新 |
| 2022-02 | 三星反超：4 年系统 + 5 年安全补丁（S21、Z3、Tab8 起） |
| 2023-10 | Google 宣布 Pixel 8 系列 **7 年**更新 |
| 2024-01 | 三星 S24 / S24 Ultra 同样 7 年 |
| 2024-10 | 高通表态高端芯片给 8 年 |
| 2025-02 | 高通正式确认 7 / 8 / 8 Elite 系列 8 年 + **两次内核升级** |
| 2025-05 | MediaTek 跟进：Dimensity 8400 / 9400 也是 8 年 |
| 2025 | 三星全线新机 6 年，含约 $125 的 Galaxy A06 4G |

「两次内核升级」这条最关键——它意味着这些芯片能用上被新版 Android 官方支持的内核，而不是永远钉死在一个版本上。

Google 也在 Android 15 / 16 / 17 里把内核支持从 3 年延到 4 / 5 / 6 年，但作者判断这是过渡措施，最终会回到 **LGRF（Longevity Google Requirements Freeze）** 计划：要求芯片厂每 3 年升级一次内核。

**但中低端芯片没跟上。** 高通对非旗舰只字未提，除了 2020 年 12 月那句「所有骁龙都给 3 年系统 + 4 年安全更新」。所以 Volla、FuriLabs、Jolla、Brax 现有的中端产品线，大概率还是会踩同一个坑。

对新机来说，结论是明确的：**选骁龙 8 或 Dimensity 9000 系列**，能拿到 8 年支持；而且这些芯片支持 DisplayPort Alt Mode，USB-C 能直接输出视频，手机可以当桌面 PC 用——这是 Linux 手机相对 Android 的一个真实卖点，因为 Linux 桌面比 Android 桌面有用得多。

预算紧一点的，骁龙 7 和 Dimensity 8400 也在这 8 年范围内，只是没有视频输出。而如果选骁龙，还有机会在未来拿到部分 mainline Linux 支持，官方支持结束后能「续命」；选 MediaTek 基本没这个指望——作者对此相当不满，因为**太多 Linux 手机厂商选了 MediaTek**。

## 七、软件：Librem 5 的教训与 Phosh 的意外成功

### 大公司是怎么栽的

Purism 在 2017 年 8 月宣布 Librem 5 时，面对的不只是「用一颗还没发布的新 SoC」这个硬件难题，更大的坑是软件。它看过前人怎么栽：

- **Motorola** 做了半打 Linux 变种，但没能统一研发方向，最后转向 Android，把自己商品化了，先后卖给 Google 和联想
- **Palm** 的 webOS 开发太久，钱烧完了，2010 年卖给 HP
- **Nokia** 的 MeeGo 开发太久，2011 年转向微软 Windows Phone，反而加速了自己的崩塌
- **Mozilla** 用 Web 标准做了一整套系统，但资源拼不过 Android，2015 年 12 月放弃手机版 Firefox OS
- **Canonical** 想用 Unity8 统一桌面和移动，成本高、商业兴趣有限，2017 年 4 月放弃 Ubuntu Touch

这段历史教给硬件厂一条铁律：**软件做得越少越好**，只写让硬件跑起来的代码加一点发行版维护。但 2017 年的 Purism 没法走这条路——当时所有可用的移动界面都有硬伤：

- Sailfish 的 Silica 是专有的（和 Purism「100% 自由软件」的目标冲突）
- 三星 Tizen 的 Flora License 只给「Tizen 认证平台」专利许可
- Nemo Mobile 和 Plasma Mobile 都不完整
- LG 把 webOS 改造成了电视/车机系统，剥离专有部分工作量巨大
- Firefox OS 代码已被弃养，UBports 人手撑不起 Ubuntu Touch 的巨大代码库

而且 Purism 还想**和桌面 Linux 统一软件栈**（目标是在 Debian、Ubuntu、Fedora、SUSE、Arch 上都能跑），而这些界面全都基于独立的移动栈。

### 于是自己造一个薄的

Purism 最后决定自研 **Phosh**（phone + shell），定位是 GTK + GNOME 中间件之上的一层薄壳。

这个选择的聪明之处在于：它基于 **Linux + Wayland + wlroots + GTK + GNOME** 这套标准桌面栈，再改约 20 个 GNOME 应用让它们自适应小屏。于是它能白拿 IBM/Red Hat、SUSE、Canonical、Google 对这套栈的企业级支持。Purism 需要向上游提交代码（Linux、wlroots、ModemManager、GTK/GNOME、Matrix），但之后就**可以指望这些项目替它维护**。

2018 年中做 libhandy，2020 年和 GNOME 社区一起做 libadwaita，让 GTK4/GNOME 能在移动和桌面之间自适应。

代价是前期投入高，而 Purism 撞上了 COVID：

- 2020 年 3 月起停止给取消订单的客户退款
- 2020 年 2–5 月，14 个 Librem 5 开发者走了 5 个，留下的人提交量明显下滑
- 2022 年 3 月价格涨到 **$1299**
- 2023 年 8 月，Purism 在给 Louis Rossmann 的信里承认还有 **600 个**取消订单没退款

作者对此的判断很克制：Purism 当时进退两难——公开承认财务问题，订单会全部蒸发；把钱全退了，公司破产，对所有付了 $599–799 的预订者更糟。所以它选择拖，公司活下来了，2020 年 11 月开始交付。但退款至今没还。

### 结果：Phosh 反而赢了

> Of the 469k lines of code in the software projects that Purism initiated for the Librem 5, 98.7% of that code is now controlled by external organizations.

Purism 为 Librem 5 发起的那些项目，总共 46.9 万行代码，其中 **98.7% 现在由外部组织掌控**。

- GNOME 正式收养了 libhandy、Calls、Chat（chatty）
- FreeDesktop.org 收养了 feedbackd
- 2025 年 2 月，德国成立非营利协会 **Phosh.mobi e.V.** 独立主导 Phosh 开发
- 五年间这些项目代码量涨了 **74.9%**，新增部分大多出自已经不在 Purism 的人之手
- Purism 手上只剩 gtherm、haegtesse、wys 三个 D-Bus 守护进程，合计 6173 行，占 **1.3%**

| 项目 | 2021-12 | 2026-09 | 增长 |
| --- | --- | --- | --- |
| libhandy | 47,730 | 48,110 | 0.8% |
| libadwaita | 51,270 | 128,067 | **149.8%** |
| chatty | 49,661 | 49,534 | -0.3% |
| calls | 20,745 | 28,964 | 39.6% |
| libcall-ui | 4,426 | 5,093 | 15.1% |
| phoc | 15,277 | 38,599 | 152.7% |
| phosh | 48,301 | 96,357 | 99.5% |
| phosh-mobile-settings | — | 26,724 | — |
| phosh-tour | — | 4,135 | — |
| squeekboard | 17,993 | 26,773 | 48.8% |
| feedbackd | 5,970 | 9,768 | 63.6% |
| gtherm / haegtesse / wys | 6,281 | 6,173 | — |
| **合计** | **268,257** | **469,237** | **74.9%** |
| 由外部组织接管 | 173,832 (64.8%) | 463,064 (**98.7%**) | 166.4% |

用户也用脚投票：2022 年 1 月 PINE64 对 3079 名 PinePhone 用户的调查里，**39.3% 把 Phosh 选为最喜欢的界面**，Sxmo/Swmo 15.5%、Plasma Mobile 15.0%、Lomiri 6.7%。要知道 Phosh 2018 年 4 月才开始开发，而 Lomiri 和 Plasma Mobile 分别从 2013 年 3 月和 2015 年 7 月就在做了。

有意思的是，Qt/KDE 在移动适配上其实领先很多（Qt Quick 2013 年、Kirigami 2016 年），GTK 直到 2019 年 libhandy 才有对应能力。但 Phosh 靠**复用 GNOME 现成的基础设施和应用**，用更少的人跑得更快。

当然 Phosh 也有明显短板：默认的 Squeekboard 键盘简陋（2025 年才有带纠错和词补全的替代键盘）；桌面模式界面很有限；**没有相机应用**，得靠 PinePhone 的 Megapixels 或 Librem 5 的 Millipixels 分支；也没有 Android 用户习惯的底部三键和手势。

它能赢还有一个现实原因：Purism 在付钱雇人开发，所以更稳；而 Plasma Mobile 依赖 GPU 硬件加速，偏偏 PinePhone 的 A64 和 Librem 5 的 i.MX 8M Quad 驱动都不支持，容易卡死。Phosh 纯软件渲染反而更快。

## 八、Linux 发行版的采纳：从孤岛到遍地开花

Phosh 成功的关键，是它贴着通用桌面栈，所以好打包、好分发：

- 2018-09 被 postmarketOS（现 Nura）采纳，距 Purism 首次亮相才两个月
- 2020-02 进入 Debian，成为 Mobian 的基础
- 随后 Debian、Arch、Manjaro、Fedora、openSUSE、NixOS 首次成为「移动发行版」

Plasma Mobile 后来也照着这条路走，逐步向桌面栈靠拢：2020-12 弃用 Halium、只跑 Linux 内核；2021-12 从 oFono 换成 ModemManager；2026-02 从 Maliit 虚拟键盘换成 Plasma Keyboard。

其他界面也类似：**Sxmo**（Sway + wlroots 上的一组 shell 脚本，2020-02 首发，轻量易改，在 PinePhone 上人气第二）；**Lomiri**（UBports 2020-02 从 Unity8 改名，更快更省内存，但志愿者太少、代码库太大，维护吃力）。

作者的结论是全篇的一个关键判断：

> Because mobile Linux is no longer isolated and locked into silos controlled by large companies, such as Nokia, Samsung, LG, Mozilla and Canonical, it has a much greater chance of succeeding and attracting contributors than it did in the past.

移动 Linux 不再被锁在诺基亚、三星、LG、Mozilla、Canonical 这些大公司控制的孤岛里，所以它成功和吸引贡献者的机会比过去大得多。因为这些界面建立在外部组织维护的现有软件栈上，它们**不太可能像 Firefox OS 那样被抛弃，也不太可能像 Hildon 那样僵化消失**。

## 九、PINE64：把车套在了马前面

PINE64 2015 年 10 月以众筹起家，思路是「只做便宜硬件，软件交给社区」。PinePhone 出货可能超过 **10 万台**，极大地推动了移动 Linux：催生了 Mobian 和 DanctNIX，启发了 Sxmo，促使 Plasma Mobile 决定只跑 Linux 栈、推动 UBports 支持 Linux 内核，也让一堆主流发行版第一次做移动移植。

但它犯了一个根本错误：**把资源押在发行版的打包工作上，而不是先付钱做启动和驱动开发**。Sway 的主要开发者、也是 PinePhone 志愿开发者之一的 Drew DeVault 说得很直接——这是本末倒置。

更糟的是后来的决策。PINE64 创始人 TL Lim 被各发行版之间的争执弄烦了，决定设备只预装一个发行版、一个界面，而他选了 **Manjaro + Plasma Mobile**，并且只给 Manjaro 分钱。问题是：PINE64 自己的调查显示 Phosh 才是最受欢迎的界面（但那是竞争对手 Purism 控制的）；Plasma Mobile 至少还是个需要企业支持的社区界面；而 Manjaro 基本不做开发工作，还因「把已知有问题的开发中软件直接发布」而被广泛批评。

后果是灾难性的。2022 年 8 月，postmarketOS 的 Martijn Braam 公开与 PINE64 决裂。PINE64 的回应没能平息，Drew DeVault 发帖说：

> PINE64 has let its community down.

PINE64 辜负了它的社区。

大部分志愿开发者停止合作。PinePhone Pro（2021-12 发布）的硬件需要大量软件开发才能用，但已经没人做了——几千人买下它，期待它终将变成一台能用的设备，结果直到 2025 年 8 月停售，它仍有重大软件问题。

作者认为正确的做法是：把利润用来付钱给开发者做驱动和内核支持，而不是分给发行版；优先资助那些**对所有用户都有益**的工作，比如 Megapixels 相机应用、EG25-G 基带固件的自由化。因为「愿意把发行版移植到 PinePhone 的志愿者很多，愿意在业余时间啃驱动的人很少」。

## 十、热情是怎么消退的

作者写了一段很坦诚的自我剖白，这段比任何分析都有说服力。

刚拿到 Librem 5 和 PinePhone 时，他觉得这是极客的狂欢：反复刷不同发行版、跑分、追硬件支持的进展、像追球队一样追 Phosh 和 Adwaita 的开发。他甚至把两台手机上每颗元件都查了一遍，记录在项目 wiki 上。

但现实是：**每次刷完新发行版，玩一两天，手机就回到抽屉里。**

- PinePhone 性能差，加载应用慢、界面有可感延迟
- 屏幕因为 I2C 总线流量有明显闪烁，调暗时更难受
- 他一度想动电烙铁改闪存速度，又怕弄坏板子
- PINE64 把屏幕闪烁当作「不是问题」，也没把 eMMC 电压从 3.3V 改到 1.8V（那能把顺序读从 55 MB/s 提到 125 MB/s）
- PINE64 没有和硬件开发者沟通的渠道，他发现原理图错误也没处报

Librem 5 好用一些（CPU 和内存更强，界面更跟手），但他形容自己「像口袋里揣着一个暖炉」——屏幕和铝框发烫，电池掉得快，得不停充电。相机能用之后他也玩了很久，但每张照片处理太慢，真要拍好照片还是掏出刷了 LineageOS 的红米 Note 7。

结论很朴素：**抽屉里已经有一台没在用的 Linux 手机，就很难说服自己再买第二台。** 再加上 2022 年社区开发者集体离开 PINE64、PinePhone Pro 开发停摆、Purism 拒不退款，早期用户的热情就这么耗光了。

## 十一、Jolla 证明需求还在

看起来需求已经死了：Liberux NEXX 众筹一个月只拿到 **120 台**预售，是目标 170 万美元的十分之一，2025 年 11 月后再无音讯；FuriLabs FLX1 口碑不错但几乎没人知道，论坛已经冻结；Dawndrums Divine D.（突尼斯创业公司）还在慢慢推进主板 rev 2 和自研 DawnOS。

但作者指出：这些失败主要是**宣传太差 + 公司没有信誉记录**。Linux 圈被伤过太多次——2013 年 Ubuntu Edge、2015 年 Firefox OS 手机和 Jolla 平板、2019 年 Necunos NC_1——大家对众筹移动设备天然警惕。

真正证明需求还在的是 **Jolla**。

这家芬兰公司 2011 年由前诺基亚 MeeGo 工程师创立，拿 MeeGo 的开源部分加上自家的 Silica 界面（模仿 N9 的滑动 UI），又授权 Myriad 的 Alien Dalvik 来跑 Android 应用（现在叫 AppSupport）。它还开发了 libhybris，并维护了 oFono、Maliit 等一批诺基亚遗留代码。2015 年底取消众筹的 Jolla 平板、只退了一半钱，差点破产；2024 年因为俄罗斯股东问题关掉原公司，以 JollaBoys 名义买回资产重生。

然后是关键数据：

- 2025-12-05 开放 Jolla Phone 预售
- **48 小时内**售完 2000 台众筹目标
- **一周内** 5000 台
- 到 2026 年 8 月累计 **15000 台**

而且人们是在**没看过任何测评、甚至不知道用什么处理器**的情况下下单的。手机 €499 起（现 €679），12GB RAM、256GB 存储、可换电池、物理隐私开关。它的宣传语精准击中了欧洲消费者：

> "The Jolla Phone is not based on Big Tech technology. It is governed by European privacy thinking and a community-led model."

Jolla Phone 不基于大科技公司的技术。它由欧洲的隐私理念和社区主导的模式来治理。

作者的点评很实在：如果 Jolla 肯花钱做广告、走出欧洲、保持现货，本可以卖得更多。**这说明对 Android/iOS 双寡头不满的人群，是一个尚未被开发的市场。**

## 十二、AOSP 这条退路正在关闭

这一节是全文的现实背景，也是 Linux 手机机会的来源。

桌面端 Linux 在增长——很多人受够了微软把 Windows 变成广告平台和 AI 垃圾的载体，加上 Windows 10 停止支持、老机器又过不了 TPM 限制，于是干脆装 Linux。

手机端的不满同样在积累，但**逃离的出口正在被焊死**。过去想夺回一点数字生活控制权的人，可以解 bootloader、刷 /e/OS、CalyxOS、GrapheneOS。现在这条路在收窄：

- 中国品牌已占全球智能手机约 60%，把很多「允许解 bootloader」的老品牌挤出了市场
- LG、BQ、LeEco、WileyFox、Essential、Razer 都没了；索尼和 HTC 销量太小已无足轻重
- 华为 2018 年停止解锁；近两年三星、华硕、真我跟进
- 小米这个「刷机友好」起家的品牌，现在解锁码限制多到没人愿意再为它做第三方 ROM

作者的统计很硬：

> The brands which have good policies for bootloader unlocking has shrunk from 42.5% to about 7% of the global smartphone market over the last couple years.

有良好 bootloader 解锁政策的品牌，全球市场份额在过去几年从 **42.5% 缩到约 7%**。

2025 年这些品牌合计只卖了约 **8700 万台**（联想/摩托 6000 万、Google 1200 万、一加 1160 万、Nothing 200 万……），而全球总销量是 **12.455 亿台**。这还是高估——大部分机型根本没人做第三方 ROM；摩托和 Google 有相当比例走运营商渠道，而 Verizon 这类运营商即使合约到期也不给解锁；MediaTek 天玑和 UNISOC 展锐不像高通那样公开内核源码。

更严峻的是：2025–2026 年，除 2025 年 1 月的 Moto G05（8 个月后就被 G06 取代）之外，**没有任何一款大厂新机拿到 LineageOS 官方支持**。而 LineageOS 官方支持很关键，因为很多第三方 ROM 都基于它、只移植它支持的机型。算下来，**每年真正适合刷机的手机只有约 2000 万台，占 2%**。

而且还在恶化：Oppo 宣布把一加撤出北美和欧洲（一加在印度和中国仍售，中国需出示身份证才能解锁）；Nothing 销量下滑、裁员 100 人（占 12%）；三星给 ONE UI 8 机型全面锁 bootloader；小米开始限制解锁码。全球大品牌里只剩摩托罗拉还开放，但近期机型只有非官方移植。

Google 那边也在提高门槛：从 Android 4.1 起不断把功能从 AOSP 搬进专有库；AOSP 16 起不再在 AOSP 里提供 Pixel 的设备树和驱动二进制，ROM 开发者失去了「能直接在真机上测最新 AOSP」的靶机；还压平了内核提交历史，让 GrapheneOS 这类项目难以从 Google 内核里摘取新特性、修复和安全补丁。

作者由此得出一个尖锐的观察：**手机厂延长支持年限，并不是良心发现，而是换了商业模式**——从「计划性淘汰」转向「监控资本主义」：多收几年数据、做更精准的广告、训练 AI。既然是靠数据回本，就绝不能让用户退出这个系统，于是锁 bootloader、提高 root 门槛。

## 十三、现在可行的三种 Linux 手机

作者把可能性归为三类，这是全文最实用的一节。

### 第一种：纯 Linux 手机

代表：Librem 5、Liberty、PinePhone、PinePhone Pro。跑真正的 Linux 内核。

过去它们缺算力，也常常缺 ISP、音频 DSP、硬件视频编码器、Vulkan 图形、NPU、加密引擎，或缺这些部件的 FOSS 驱动。RK3588S 和未来的 RK3668 第一次给了它们够用的性能。

**优点**：能做真正的硬件断电开关（切断元件的供电，而不是靠 SoC 引脚或软件关掉 WiFi/蓝牙/基带/GPS）；能挑有开源驱动的元件，软件自由度和透明度最高；能公开原理图和 PCB 视图，让硬件和软件一样自由。

**缺点**：风险最高、工程量最大。不能改高通/联发科的参考设计，也不能让 ODM 改现成方案——得找有射频经验的设计公司，从零设计一块元件数是标准手机 2–3 倍的板子，反复迭代，还要写内核代码。上市周期长，用众筹融资容易翻车。

### 第二种：高通 IoT 芯片路线

用 QCM6490 / QCM8850 这类带集成基带的 Dragonwing 处理器。它们不如最新骁龙新，但**多数有 10–15 年支持**，而且不少最终会进 mainline Linux，官方支持结束后还能靠社区续命。

### 第三种：集成移动 SoC + Android 内核

用 libhybris 把标准 Linux 栈跑在 Android 内核上。

过去这不可行，因为 Android SoC 支持期太短，撑不起 Linux 手机的长开发周期和低年销量。现在高通和联发科的旗舰给到 8 年，这条路才成立。

**这是最省钱的方式**：很多手机 ODM 有现成参考机型，愿意按客户要求微调。FuriLabs 证明了连「加隐私开关」这种改动也能谈。代价是要挑 7–8 年支持的 SoC，否则寿命仍然难看。

### 几种设计路线的横向对比

| 路线 | SoC | CPU/GPU | 续航 | 支持 | 硬件开发 | 软件开发 | 价格(1-5) | 备注 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 社区 Linux | RK3566 | 差 | 差 | 永久 | 难 | 无 | 1 | 软件外包给社区，收敛体验差 |
| 昂贵 Linux | RK3588S | 次优 | 差 | 永久 | 很难 | 很难 | 5 | 真硬件开关，可做收敛设备 |
| 中端 blob Linux | QCM6490 | 好 | 次优 | 到 2035 | 易 | 难 | 4 | blob 多，可收敛 |
| 经济 Android 内核 | 骁龙 4/6 Gen 4 | 尚可 | 好 | 4 年 | 易 | 中 | 2 | blob 多，不能收敛 |
| 中端 Android 内核 | 骁龙 7 Gen 4 | 好 | 好 | 8 年 | 易 | 中 | 3 | blob 多，不能收敛 |
| 高端 Android 内核 | 骁龙 8 Gen 5 | 极佳 | 尚可 | 8 年 | 易 | 中 | 5 | blob 多，可收敛 |

但作者提醒：**软件开发成本下降，并不意味着 Linux 手机能变便宜**。QCM4490 和中低端骁龙/天玑的支持期太短，做不出经济型 Linux 手机；骁龙 7 或 Dimensity 8000 系列能做中高端，但不支持 DisplayPort Alt Mode，也就没有「当 PC 用」这个核心卖点。综合下来，**QCM6490 大概是做中高端 Linux 手机的最佳选择**。

至于 Jolla、FuriLabs、Volla、Brax 这类继续做中端的厂商，作者的建议很直接：别再用 MediaTek 了，换能进 mainline 的骁龙，用户至少能在官方支持结束后继续跑 Nura 之类的发行版。

## 十四、真正的障碍是公司

> Now that the available SoC's and software are no longer holding back the making of compelling Linux phones, the real barrier to creating a viable Linux phone market are the companies to make and sell those phones.

既然可用的 SoC 和软件已经不再阻碍做出有竞争力的 Linux 手机，那么建立一个可行 Linux 手机市场的真正障碍，就是那些制造和销售这些手机的公司。

逐家看：

**PINE64**：宣布因 RAM 和 eMMC 涨价暂停大部分设备生产。本质上是承认自己涨不了价——因为软件支持不到位，没人愿意为它多付钱。它既不太可能改商业模式去付钱养开发者，也没修复与出走发行版和志愿者的关系，所以传闻中的 RK3566 版 PinePhone 2 基本无望。作者认为理论上可以再出现一家「定价略高、但有钱付开发者做内核支持」的社区硬件公司，但可能性很低。

**Purism**：明确在做第二代。2026 年 7 月的通讯里说「正处于 Librem 5 v2 和 Liberty 5 v2 的早期规划阶段」，并准备「未来几个月内发起众筹」以「评估客户兴趣和牵引力」。问题是声誉——**还清那 600 个退款花不到 40 万美元**，作者认为这是恢复声誉最划算的一步；不做这一步，很难众筹到它预计需要的 200 万美元以上。而且 Purism 同时还要养 Librem 14 笔记本、Librem 11 平板、Librem Mini，以及一个基于 RISC-V 的 Librem Core-V 芯片项目（已获 CHIPS Act 超 5000 万美元预批）——注意力会被严重分散。

**其他**：Dawndrums 对上市计划守口如瓶；FuriLabs 没有新机消息；BraX3 的 Ubuntu Touch 移植卡了几个月，似乎指望 UBports 社区替它完成；Volla 主打自家的 AOSP 衍生版 Volla OS。

**Jolla**：方向最对——计划转入量产、保证现货、进军北美。但 Linux 社区很多人不会买账：Silica 界面和 AppSupport 都是专有软件；C2 的内核源码拖了 8 个月才发；Jolla Phone 2026 年 7 月 8 日就发货了，内核源码至今未公开；而且用的是 UNISOC 和 MediaTek，基本无缘 mainline，寿命堪忧。

作者特别强调**营销**这个被忽视的变量：Liberux 和 FuriLabs 都栽在不会宣传上，而 Jolla 极其有效地用社交媒体打动了欧洲用户。

潜在的新玩家有两类：卖 Linux PC 的几十家公司（多数没有自研硬件经验，习惯用 Clevo/同方的公版模具，也不做内核工作，更适合拿 ODM 的 Android 方案装 Linux）；以及做 Linux 单板机的公司（更懂和中国台湾厂商合作做定制硬件，但普遍不会经营社区）。

最后是市场基础。多项民调显示隐私焦虑是真实的：Ipsos 调查中 **79%** 全球受访者、**84%** 美国受访者担心在线隐私；Malwarebytes 调查中 **89%** 消费者担心企业与 AI 滥用数据；YouGov 调查中 **62%** 美国人担心第三方掌握了自己多少个人数据。

如果 Linux 手机能提供和 Android/iOS 相当的功能与易用性，这块市场是存在的。但前提是——它必须支持通过 Waydroid 之类跑 Android 应用，并像 Murena、iodé 那样内置拦截第三方追踪器的能力。

## 结语

作者的收尾既不乐观也不悲观，而是把球踢回给了厂商：

> The conditions may be ripe for Linux phones, but it is unclear whether the companies selling Linux phones will take advantage of those conditions to create a viable alternative to the current Android/iOS duopoly. For the sake of software freedom, online privacy and the greater longevity of mobile devices, a concerted push is needed to promote mobile Linux.

条件或许已经成熟，但那些卖 Linux 手机的公司是否会利用这些条件、造出足以替代当前 Android/iOS 双寡头的产品，仍不明朗。为了软件自由、在线隐私和移动设备更长的使用寿命，需要一次协同的推动来推广移动 Linux。

**我的读后感**：这篇文章最有价值的地方，是它把「Linux 手机为什么不行」从一句情绪化的抱怨，拆成了可以逐项验证的工程与商业约束——制程成本、元件数、内核寿命、上游化比例、发行版采纳路径。看完之后你会发现，那些看似「厂商不争气」的结果，背后大多是结构性的账算不过来。而这次之所以不同，是因为**账终于能算平了**：RK3588S 让纯 Linux 路线第一次够用，高通的 15 年支持让 IoT 路线成立，8 年内核支持让 Android 内核路线不再自杀，Phosh 的 98.7% 外部化让软件不再随公司死活。剩下的，确实只是有没有人愿意做。

## 原文出处

- 原文：[Will Linux phones become a viable alternative to the Android/iOS duopoly?](https://amosbbatto.wordpress.com/2026/10/05/linux-phones-alternative/)（Amos Batto，2026-10-05，CC BY 4.0）
- 作者博客：[amosbbatto.wordpress.com](https://amosbbatto.wordpress.com/)
- 原文另提供 [PDF](https://amosbbatto.wordpress.com/wp-content/uploads/2026/10/linuxphonesviablealternative-8.pdf) 与 [ODT](https://amosbbatto.wordpress.com/wp-content/uploads/2026/10/linuxphonesviablealternative-8.odt) 下载
