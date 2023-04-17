---
title: 如何用 Hexo + GitHub Page 部署博客
date: 2023-04-17 20:42:25
tags: [HOW-TO, hexo]
---

# 如何用 Hexo + GitHub Page 部署博客

总算把博客搭起来了（意外地还挺方便），那么作为博客的第一篇文章，就简单总结一下用 Hexo + GitHub Page 部署博客的步骤吧。

## 部署

1. 安装 hexo-cli，输入命令 `hexo init <username>.github.io` 初始化一个文件夹

2. 创建文件 `.github/workflows/pages.yml`，内容照着[这里](https://hexo.io/zh-cn/docs/github-pages)写

3. 上传到 GitHub 仓库

4. 到 GitHub 仓库的 `Settings > Pages > Build and deployment` 把 Branch 改为 `gh-page`

完事了，接下来只要在`source/_posts` 里用 Markdown 写东西就行了，写完上传到 GitHub，等两分钟就更新了。

## 其它注意事项

1. 在 `_config.yml` 里可以设置站点标题、使用的主题、域名。

2. 输入命令 `hexo server` 可以启动本地服务器，先在本地预览效果，效果满意了再发布到仓库，没必要频繁上传。

3. 不要在 GitHub Desktop 里把分支切到 `gh-page`，这个分支没有 ignore node_modules，切过去显示 1000 多个文件变化，巨 TM 卡，切都切不回去。
