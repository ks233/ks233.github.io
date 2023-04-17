---
title: 如何用 Hexo + GitHub Pages 部署博客
date: 2023-04-17 20:42:25
tags: [Hexo]
category: Hexo
description: 猴子也能懂的博客部署流程！
cover: cover.png
---

# 如何用 Hexo + GitHub Pages 部署博客

总算把博客部署完了，虽然花了点时间，但是总结起来步骤非常简单，水一篇文章都觉得有点太短了。

## 部署步骤

1. 用 npm 安装 hexo-cli，输入命令 `hexo init <username>.github.io` 初始化一个文件夹

2. 创建文件 `.github/workflows/pages.yml`，内容照着[这里](https://hexo.io/zh-cn/docs/github-pages)写

3. 上传到 GitHub 仓库，名称同样是 `<username>.github.io`，设置为公开。

4. 到 GitHub 仓库的 `Settings > Pages > Build and deployment` 把 Branch 设置为 `gh-pages`。

没了，就这么简单。接下来只要在 `main` 分支里编辑 Markdown 内容就可以了，每次 commit + push 之后 GitHub 都会自动更新仓库的 `gh-pages` 分支，网页也会随之更新。

## 基本使用

- 在 `_config.yml` 里设置站点标题、使用的主题、主页 URL。
- 输入命令 `hexo new "文章标题"` 新建文章。

- 在 `source/_posts` 编辑内容。

- 输入命令 `hexo server` 可以启动本地服务器，先在本地预览效果，效果满意了再发布到仓库，没必要频繁上传。

## 踩坑

### 不要切到 gh-pages 分支

`gh-pages` 这个分支是 GitHub 部署自动生成的，没必要管它。如果你和我一样习惯使用 GitHub Desktop，千万不要手贱把分支切到 `gh-pages`，这个分支没有 ignore node_modules，切过去显示 1000 多个文件变化，电脑会直接卡死。

### 相对路径问题

换成 Butterfly 主题之后，文章页面的头像不能正常显示，查看网页源代码，本来应该是 `\img\avatar.jpg` 的路径变成了 `..\img\avatar.jpg`，路径都错了当然会 404，顶部导航栏的链接也受到了影响。

最诡异的是，hexo server 的链接是正常的，deploy 生成的文件却不正常。翻了好久 issue 终于找到了产生问题的原因：以前折腾的时候把 hexo 配置文件中的 `relative_link` 设置为 `true` 了，改回 `false` 药到病除。

参考：[hexo相对url配置错误导致的资源404和跳转错误 · Issue #552 · jerryc127/hexo-theme-butterfly (github.com)](https://github.com/jerryc127/hexo-theme-butterfly/issues/552)
