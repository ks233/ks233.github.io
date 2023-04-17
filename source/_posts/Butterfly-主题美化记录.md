---
title: Butterfly 主题美化记录
typora-root-url: Butterfly 主题美化记录
date: 2023-12-17 18:17:18
category: Hexo
tags: [Hexo, 博客美化]
cover: cover.jpeg
description: >
    <span style="font-size: 3em">“这是什么鸟？”</span>
---

![这是什么鸟？](cover.jpeg)

# Butterfly 主题美化记录

半年前就已经搭好了 Hexo 博客，最近终于有时间维护了，接下来会不定期更新一些学习笔记和折腾经验。

这篇文章记录了我把博客主题从 Fluid 换成 Butterfly 之后做的一系列配置，应该可以帮助后来人快速找到一些常见的基本配置项。

## 整体印象

我希望我的博客页面能在足够个性化（二次元塞爆）的同时保持清爽简洁、风格统一、配色和排版易于阅读。

>  接下来如果没有特别说明，YAML 代码都是在修改 `_config.butterfly.yaml`，CSS 代码都是注入的自定义样式。

### 头图、背景图片

第一步当然是设置背景图片啦，不加入致死量的二次元浓度还做什么 DIY（

```yaml
# The banner image of home page
index_img: /img/82937235_p0_master1200_2x2n.png

# If the banner of page not setting, it will show the top_img
default_top_img: /img/82937235_p0_master1200_2x2n.png

# Website Background (設置網站背景)
# can set it to color or image (可設置圖片 或者 顔色)
# The formal of image: url(http://xxxxxx.com/xxx.jpg)
background: url(/img/kantoku_2x2n.png)
```

`index_img` 是首页的大图，`default_top_img` 是在文章没有封面时默认显示的头图，`background` 是整个页面的背景。

### 卡片透明度、页脚毛玻璃

背景图被挡住那不就白设置了，得让前面的卡片有点透明度。

参考 [Hexo+Butterfly主题设置背景透明度和字体](https://blog.csdn.net/qq_44138925/article/details/128843200)，并且补充了深色模式的设置，注入以下 CSS：

```css
:root {
    --card-bg: rgba(255, 255, 255, 0.9);
}

[data-theme='dark']:root {
    --card-bg: rgba(18, 18, 18, 0.9);
}

/* 页脚模糊 + 变暗 */
#footer {
    background: rgba(0, 0, 0, 0);
    backdrop-filter: brightness(60%) blur(16px);
    font-size: large;
    font-weight: bold;
}
```

目前只改了卡片的透明度，把页脚改成了毛玻璃效果，效果还可以。

注入 CSS 就是新建一个 CSS 文件，然后在 `inject` 里用 HTML 语句引入 CSS 文件， 可以参考上面的链接。

### 默认深色

```yaml
# Default display mode (網站默認的顯示模式)
# light (default) / dark
display_mode: dark
```

这个字段找了我半天，记录一下。

*后来还是改回去了，浅色也挺好看的。*

### 把侧栏放到左边

侧栏默认在右边，感觉放到左边顺眼一点。

```yaml
aside:
  position: left
```

### 首页副标题、打字机效果

```yaml
subtitle:
  enable: true
  # Typewriter Effect (打字效果)
  effect: true
  # Customize typed.js (配置typed.js)
  # https://github.com/mattboldt/typed.js/#customization
  typed_option:
    loop: false
  source: false
  # 如果關閉打字效果，subtitle 只會顯示 sub 的第一行文字
  sub: 
    - 人生就像一盘西洋棋，我不会下西洋棋。
```

`typed_option` 本来是空的，要根据注释中的文档手动添加字段，比如添加 `loop: false` 使打字机不会反复删掉重打。

## 个人信息卡

### 隐藏 Follow Me 按钮

默认按钮是 GitHub 页面，我想把 GitHub 和其它社交媒体图标并列，这个按钮就不需要了。

```yaml
aside:
  card_author:
    button:
      enable: false
```

### 社交媒体图标

设置社交媒体图标和链接，还可以设置描述和颜色，用 `||` 隔开。

```yaml
social:
  fab fa-bilibili: https://space.bilibili.com/4790803 || Bilibili || 'rgb(0,160,216)'
  fab fa-github: https://github.com/ks233 || GitHub
  fab fa-zhihu: https://www.zhihu.com/people/ks233 || 知乎 || 'rgb(23,114,246)'
```

顺便一提，这里的 fa 指的是 [Font Awesome](https://fontawesome.com/)，fab 的 b 是 brand（商标）的缩写，可以到他们官网搜索其它可用的图标与对应的名字。

### 修改悬停动画

头像和社交媒体图标的旋转动画我不太喜欢，感觉比较突兀。

注入以下 CSS 样式：

```css
#aside-content .card-info .card-info-social-icons .social-icon :hover{
    transform: scale(1.5);
}

#aside-content .avatar-img :hover{
    transform: none;
}
```

这样头像的旋转就没了，社交媒体图标的旋转变成了缩放。

参考了 [Discussion #878](https://github.com/jerryc127/hexo-theme-butterfly/discussions/878)。

## 文章相关

### 标题左边的回形针

```yaml
# Beautify (美化頁面顯示)
beautify:
  enable: true
  field: post # site/post
  title-prefix-icon: # '\f0c1'
  title-prefix-icon-color: # '#F47466'
```

**我真的是服了，你命名叫 beautify 鬼找得到啊？？？**效果是修改标题、有序列表、无序列表的样式。

### 显示 Description

首页显示文章时，标题下面默认显示一部分正文，效果通常不太好。

```yaml
# Display the article introduction on homepage
# 1: description
# 2: both (if the description exists, it will show description, or show the auto_excerpt)
# 3: auto_excerpt (default)
# false: do not show the article introduction
index_post_content:
  method: 2
  length: 500 # if you set method to 2 or 3, the length need to config
```

把 `method` 改成 2（both），优先显示 Front-matter 中的 `description`。

### 带颜色的粗体和斜体

使粗体和斜体更加醒目。

```css
strong, em {
    color: #f76d47;
}
```

这个改法多少有点简单粗暴了，但目前为止没出什么毛病，就这样吧（

### 代码块设置

```yaml
highlight_theme: mac
```

感觉比默认好看。

### 目录设置

```yaml
toc:
  post: true
  page: false
  number: false
  expand: true
  style_simple: false # for post
  scroll_percent: false
```

设置 `expand: true` 使目录默认展开，反正我写的东西每篇不会太长。

`scroll_percent` 意义不明，关了。`number` 没什么用，也关掉好了。

`style_simple` 如果开启，侧边栏就会只剩下目录，还是算了。

### 图片描述文字

Markdown 中插入图片格式是 `![图片描述](图片url)`，但默认不显示图片描述，要通过以下设置打开。

```yaml
# figcaption (圖片描述文字)
photofigcaption: true
```

### 关闭不需要的东西

```yaml
post_copyright:
  enable: false
  
sharejs:
  enable: false
```

- `post_copyright`：一个很丑的版权声明框，我寻思我写这么烂应该没人想抄我（
- `sharejs`：一个很鸡肋的分享组件，这年头电脑端分享网页越来越难了，干脆去掉算了。

## 参考资料

[Butterfly - A Simple and Card UI Design theme for Hexo](https://butterfly.js.org/)

[我的Blog美化日记——Hexo+Butterfly | Guo Le's Blog](https://blog.guole.fun/posts/butterfly-custom/?highlight=butterfly)

[Hexo-Butterfly主题博客搭站记录 | 无境 (drflower.top)](https://www.drflower.top/posts/5920b38e/)
