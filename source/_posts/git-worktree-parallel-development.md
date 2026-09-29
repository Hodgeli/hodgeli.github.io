---
title: Git worktree：并行开发不再手忙脚乱
date: 2026-09-29 17:10:00
categories: 开发工具
tags:
  - Git
  - 工作流
  - 效率工具
description: 翻译整理自 barrd.dev：用 Git worktree 做到「一个任务、一个分支、一个目录」，同时推进多个功能并随时插入线上热修，让 git stash 变成罕见例外。
---

> **原文**：[Parallel development without the headaches using Git worktree](https://barrd.dev/article/parallel-development-without-the-headaches-using-git-worktree/)
> **作者**：Dave（barrd.dev）
> 本文为中文翻译整理，为便于对照，关键段落保留了英文原文引用。

## 先说结论

`git worktree` 从 **v2.5** 就有了，距今大约十年，但作者一直没用过。真正上手之后，它彻底改变了他的工作流：**一个任务、一个分支、一个目录**，同时推进多个功能、随时插入线上热修，而 `git stash` 从日常操作变成了罕见例外。

要记的命令只有五六个，学习成本很低，换来的却是几乎消失的上下文切换。

## 一、worktree 是什么

作者在折腾一个特别棘手的项目时，发现了 Git 的 `worktree` 功能：**让你同时在多个分支上工作，每个分支有自己的目录，但共享同一份底层仓库历史。**

```
~/Herd/
├── my-project/          # 主 worktree，分支 `main`
│   └── .git/            # 主 git 目录
├── my-project-feature/  # 链接 worktree，分支 `feature/login-form`
└── my-project-hotfix/   # 链接 worktree，分支 `hotfix/payment-bug`
```

上面这些目录共享同一份提交历史，都指向同一个 `.git` 对象数据库，但各自拥有独立的工作区状态。

每个目录用起来和普通 checkout 没区别 —— 改文件、提交、推送照旧，区别在于你**不用再在同一个工作区里反复横跳切分支**。

> Recently whilst tinkering with a particularly tricky project, I came across Git's `worktree` feature. A tool that lets you work on multiple branches simultaneously, each in its own directory, all sharing the same underlying repository history.

> Each directory behaves like a normal checkout, you edit files, commit and push as usual, but you avoid constantly hopping branches in a single working tree.

## 二、branch 和 worktree 的区别

传统做法下，同时处理多个分支意味着大量的 `git checkout` 和 `git stash` —— 不断地保存现场、切换上下文，然后祈祷没弄丢什么重要的东西。很容易迷失方向，尤其是在一个线上 bug 突然打断你思路的时候。

有了 `git worktree`，你可以为任意分支（已存在的或新建的）添加一个新的工作目录，让各条工作流彼此隔离：

```bash
# 把一个已存在的分支作为 worktree 加进来
git worktree add ../my-project-feature feature-branch

# 或者一步到位：新建分支并同时创建 worktree
git worktree add -b new-feature ../my-project-new-feature
```

这会在主项目同级创建新目录，并检出你指定的分支。之后你可以在每个目录里独立地改文件、提交、推送，完全不碰主工作目录。

此时你的目录结构大概是这样：

```
my-project/              # 主 worktree，分支 `main`
my-project-feature/      # `feature-branch` 的 worktree
my-project-new-feature/  # `new-feature` 的 worktree
```

> Traditionally, working on multiple branches meant a lot of `git checkout` and `git stash` constantly saving your place, switching context and hoping you didn't lose anything important. It's easy to get lost, especially when a production bug interrupts your flow.

**一个重要限制**：同一个分支不能同时被检出到多个 worktree —— 每个 worktree 必须检出一个唯一的分支。实际使用中，这条限制反而促成了 *"一个任务、一个分支、一个目录"* 的清爽映射，让你在心理上更容易保持方位感。

> One important limitation is that the same branch cannot be checked out in more than one worktree at the same time. Each worktree must have a unique branch checked out. In practice, that encourages a tidy mapping of *"one task, one branch, one directory"*, which makes it easier to stay oriented mentally.

## 三、实战：一边做新功能，一边救线上故障

一个很真实的场景：你正在开发结账功能，线上突然炸了。

**初始结构：**

```
~/Herd/
└── shop/           # 主 worktree，分支 `main`
    └── .git/
```

**创建功能 worktree：**

```bash
cd ~/Herd/shop
git worktree add -b feature/checkout ../shop-checkout
```

**新结构：**

```
~/Herd/
├── shop/           # 主 worktree，分支 `main`
│   └── .git/
└── shop-checkout/  # 链接 worktree，分支 `feature/checkout`
```

你可以在 `shop-checkout` 里安心开发结账功能，同时让 `shop` 保持在 `main` 上随时应付 code review。

### 线上 bug 来了，创建热修 worktree

```bash
cd ~/Herd/shop
git worktree add -b hotfix/payment-fail ../shop-payment-hotfix
```

**此时的结构：**

```
~/Herd/
├── shop/                 # 主 worktree，分支 `main`
├── shop-checkout/        # 功能 worktree，`feature/checkout`
└── shop-payment-hotfix/  # 热修 worktree，`hotfix/payment-fail`
```

到这个地步，你可以同时做三件事：

- 在 `shop-payment-hotfix` 里修复并测试线上 bug
- 在 `shop-checkout` 里继续迭代 `feature/checkout`
- 让 `shop` 保持在 `main` 上空闲，用于合并和 code review

> Here's a realistic scenario, you're working on a checkout feature when a production bug *appears.*

## 四、如何把 worktree 的分支合并回去

从 worktree 的分支合并改动，和普通的 Git 合并没有任何区别，只是上下文更清晰了 —— 因为每个分支都住在自己的目录里。把功能分支合进 `main` 的典型流程：

1. 在功能 worktree 里完成工作并提交
2. 切到主 worktree 目录：

```bash
cd ../my-project && git checkout main
```

3. 合并功能分支：

```bash
git merge feature-branch
```

4. 解决冲突，然后推送

因为每个 worktree 只服务于一个分支，**误提交到错误分支、或者被热修打断后丢失现场的概率大大降低**……好吧，理论上如此。😉

> Because each worktree is dedicated to a single branch, it's much harder to accidentally commit to the wrong branch or lose your place when a hotfix interrupts your feature work… anyway, that's the theory. 😉

## 五、查看当前所有 worktree

在开始删除或清理之前，先看看 Git 目前知道哪些 worktree 会很有帮助：

```bash
git worktree list
```

**输出示例：**

```
/Users/barrd/Herd/shop                 66c16256 [main]
/Users/barrd/Herd/shop-checkout        0c8ba118 [feature/checkout]
/Users/barrd/Herd/shop-payment-hotfix  a16e4be2 [hotfix/payment-fail]
```

你可以在脑子里把它映射成这样：

```
[main]                → /home/user/Herd/shop
[feature/checkout]    → /home/user/Herd/shop-checkout
[hotfix/payment-fail] → /home/user/Herd/shop-payment-hotfix
```

这样一来，哪些分支被检出、检到了哪里一目了然，也就不会去尝试复用一个已经挂在别的 worktree 上的分支了。

## 六、如何移除 worktree

一个 worktree 用完就该收拾干净。为了安全，先提交或 stash 掉所有改动，然后：

```bash
git worktree remove ../my-project-feature
```

这条命令只对**干净**的 worktree 生效（没有未提交的改动或未跟踪的文件），除非你加上 `--force`。另外，它无法移除主 worktree。

> **Remember**
> Removing a worktree only deletes the working directory, it does not delete the branch itself. Always check with `git status` in that worktree before removing to avoid losing uncommitted work.

**记住**：移除 worktree 只是删掉了工作目录，**并不会删除分支本身**。移除前务必在那个 worktree 里跑一次 `git status`，以免丢失未提交的工作。

## 七、用 prune 清理失效条目

如果你手动删除了某个 worktree 目录，Git 仍然会在主仓库的 `worktrees` 目录下保留它的元数据。这种情况下，`git worktree list` 会把它们标记为 missing。

用这条命令清理这些失效条目：

```bash
git worktree prune
```

如果只想清理**闲置了一段时间**的条目，可以加上过期时间：

```bash
git worktree prune --expire 7.days.ago
```

而 `--expire now` 会立即移除所有失效的 worktree 元数据 —— 在本地开发环境里，如果你经常手动删掉不再需要的旧目录，这个选项相当顺手。

## 八、结语

这个功能从 `v2.5` 就存在了，大约十年前，而作者一直没用过……但现在它已经重塑了他的工作流，尤其是在同时应对多个功能和紧急热修的时候。它把各个要素都分隔开来，减少了上下文切换，也让 stash 变成了罕见的例外。

对于简单的、顺序推进的工作，传统分支方式依然是首选。但如果你曾经希望自己能**同时出现在两个地方**，那就试试 `git worktree` 吧。

> It's been around since `v2.5`, which was ~10 years ago and I'd never used it… But it's now transformed my workflow, especially when juggling parallel features and urgent hotfixes. It keeps all the elements compartmentalised, reduces context switching and means stashing has become a rare exception.

> For simple, sequential work, traditional branching is still the way to go but if you ever find yourself wishing you could be in two places at once, give `git worktree` a try.

> If you've any favourite workflow variations you take advantage of *please get in touch* and let me know.

## 命令速查

| 命令 | 作用 |
| --- | --- |
| `git worktree add <路径> <分支>` | 把已有分支检出到一个新目录 |
| `git worktree add -b <新分支> <路径>` | 新建分支并同时创建 worktree |
| `git worktree list` | 列出所有 worktree 及其对应分支 |
| `git worktree remove <路径>` | 移除 worktree（仅限干净状态，`--force` 可强制） |
| `git worktree prune` | 清理已手动删除目录留下的失效元数据 |
| `git worktree prune --expire 7.days.ago` | 只清理闲置超过指定时间的条目 |

## 关于作者

Dave 是一位住在布里斯托的苏格兰侨民，拥有 20 多年的 Web 开发经验。喜欢弹吉他、读书、看科幻片，以及折腾各种技术。

## 延伸阅读

原文附带的参考资料与同站文章：

- [Git's Database Internals](https://github.blog/open-source/git/gits-database-internals-i-packed-object-store)（github.blog）
- [Git Worktree 官方文档](https://git-scm.com/docs/git-worktree)（git-scm.com）
- [Git switch – a replacement for stash if on wrong branch](https://barrd.dev/article/git-switch-a-replacement-for-stash/)（Article）
- [Remove unused PHP versions from Laravel Herd](https://barrd.dev/article/remove-unused-php-versions-from-laravel-herd/)（Article）
- [Using Laravel Herd whilst keeping Valet and PHP Monitor](https://barrd.dev/article/using-laravel-herd-whilst-keeping-valet-and-php-monitor/)（Article）
- [Starship, blazing fast cross shell prompt](https://barrd.dev/article/starship-blazing-fast-cross-shell-prompt/)（Article）
