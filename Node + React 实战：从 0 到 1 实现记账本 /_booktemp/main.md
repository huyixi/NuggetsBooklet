---
title: Node + React 实战：从 0 到 1 实现记账本 
author: Node + React 实战：从 0 到 1 实现记账本 
date: 2025-02-14
lang: zh-CN
---

## 1.开篇词

## 前言

前后端项目目前已经部署到线上环境，大家可以通过以下地址进行访问：

**「掘掘记账本」在线预览：** http://note.chennick.wang

> 测试账号：admin，测试密码：111111。也可以自行注册使用。

**「掘掘记账本」前端代码开源地址：** 

- GitHub：https://github.com/Nick930826/juejue-vite-h5
- GItee：https://gitee.com/cxy19930826/juejue-vite-h5

**「掘掘记账本」后端代码开源地址：** 

- GitHub：https://github.com/Nick930826/jue-diary-server
- Gitee：https://gitee.com/cxy19930826/jue-diary-server

**「项目压缩包下载」**

https://s.yezgea02.com/1667989407474/juejue-vite-h5-master.zip

#### 使用到的软件下载地址

- VSCode：[下载地址](https://code.visualstudio.com/)

- DBeaver：[下载地址](https://github.com/dbeaver/dbeaver/releases)

- Postman：[下载地址](https://www.postman.com/downloads/)

> 笔者尽自己所能，帮助同学们减少一些不必要的时间消耗。

## 前端职业生涯中遇到的这些事儿

已经工作 1-3 年的前端同学，或多会少都会遇到一些问题，比如不知道自己还能学什么，每天像一只无头苍蝇一样，到处学一点。并且我相信，在你的微信公众号里也关注着不少前端相关的公众号，碎片化的知识充斥着你的微信，动则手写 Vue、React、吊打面试官等等。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6b20a2e9f8b4fa3adefbb50ef29aa6b~tplv-k3u1fbpfcp-zoom-1.image)

打一枪换一个地，今天讲 `Vue`，明天讲 `React`，后天讲 `Webpack`，面试文章更是让人心生焦虑，因为你看完之后，发现自己原来还有这么多不会的知识点，补到什么时候是个头。

你若是有很强的总结归纳能力，将所有碎片化的内容规整出来，形成自己的一套知识体系，那么以这样的学习能力，大可自学，不必买教程。

**但是大部分人焦虑的原因**，归根结底还是因为自身的知识体系还不够完善，自身目前所处的高度还不够，导致看待问题的视野还比较模糊。所以，你需要对整个软件工程有一个全链路的学习，这样你的视野将升入新的高度，看待问题将不再局限于某个页面、用某个技术怎么实现。

我不敢保证，去学习 `Node.js` 这门技术，就能让你完全成为一个全栈工程师。但至少遇到问题，你思考问题的解决方案，不再局限于前端范畴，可以结合服务端的知识，去解决前端层面遇到的问题。

我认为，全栈工程师的定义是受到各方面因素影响的。

假如你在一个小厂工作，不限制你使用的技术，无论是用 PHP、Java、Node、Go、Python，只要你能一人或协同多人完成前后端的开发工作，那也是算一名全栈工程师，只不过这样的全栈工程师干的事情是比较杂的，甚至可以叫“全干工程师”。

如果你身在大厂，大厂的工作流程是非常规范及专注的，此时你利用自己的专业知识，去帮助团队在前后端衔接、项目发布持续集成、错误监测工具、脚手架的搭建、公用组件私有化等等方面提高工作效率，那你也可以成为一名全栈工程师。

#### 例子1

我现在有一个想法。我是一个爱看技术文章的勤奋少年，每天早上打开电脑会先去掘金、CSDN、思否等技术平台阅读当天最新的文章，并且将一些好的文章收藏到浏览器的收藏夹里吃灰。但是每天都要打开这些不同的网站，非常麻烦，我想做一个聚合页面，将诸如上述平台的当天最新文章收集到一个网页中，并且要有用户权限，可以收藏文章。

此时就要用到了 `Node` 的爬虫知识，可以利用 `puppeteer` 无头浏览器，获取到相应的网页，并拿到 `dom` 节点，通过 `cheerio` 插件将 `dom` 节点转化为，可通过 `jQuery` 操作的方法。获取到文章标题和详情链接，将数据存入 `MySQL`。利用 Node 抛出接口，浏览器通过 API 接口，获取存储在 `MySQL` 中的数据。

#### 案例2

Web 网站做得多了，想换换技术栈，学习用 `React Native` 做 `App` 应用。于是乎，本小册开发的这套服务端接口，便能派上用场。甚至可以将接口数据，对接到小程序里，实现一套服务端接口多终端使用，不用再用 `Mock` 数据去填充内容。

> 上述例子想告诉大家，有全栈能力的你，可以实现很多，以前你想实现，却不能实现的想法。

## 为什么是 Node

为什么要选择 `Node` 进入全栈开发呢？很简单，作为前端，我们最熟悉的就是 `JS`，而 `Node` 赋予 `JS` 一些系统级的能力，这让我们学习 `Node` 时，不用再重新学习一门新的语言，只要你会 `JS`，结合本小册文档，以及合理的运用搜索引擎，你就能很好的入门 `Node`。

**Node 能做什么有趣的事情**

- 爬虫

- 工具

- 脚本

- 硬件

- 中台

- 通信

**Node 的就业情况**


![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc81b3109f0b4ea1b74b0d365dc7c741~tplv-k3u1fbpfcp-watermark.image)

> 数据来自BOSS直聘。

无论是实习还是社招，`Node` 在行业的需求，以及薪资的水准，都是在普通前端之上的。你可以说我很庸俗，但是社会便是如此，你的付出和你的收获在一定程度上是成正比的。所以，现在就开启你的 `Node` 之旅，这可能会为你后期的职业生涯添上浓墨重彩的一笔。

## 小册设计思路

小册目的很明确，带一部分前端，从纯前端慢慢转变为伪全栈。为什么说是「伪全栈」呢？因为课程的深度不会涉及太多的性能相关的知识，如多集成、高并发、缓存优化、多进程部署之类的问题。这些都是需要你在课后自己去实践学习的内容。

> 如果真的有通过学习一门课程就变成大神，希望知道的同学，把这门课程推荐给我，我也想学。

先带大家拿起板砖🧱 ，敲开全栈的大门。知其然，而后使其然。

我们将会学习掌握下图流程：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b61a509885e41fbba4d955933907797~tplv-k3u1fbpfcp-zoom-1.image)

**需求分析**

项目的逻辑梳理，目的是为了下一步数据库设计做准备，需求分析和数据库设计其实是同步的，需要一边分析，一边设计。

**数据库设计**

本课程采用数据库为 `MySQL`，并且使用更加人性化的可视化工具 [DBeaver](https://dbeaver.io/)，更易于新手上手操作数据库。数据库的作用说简单了，就是为了存储数据，至于用什么技术，不必太过于拘泥，你也可以选择 `MongoDB`。

可视化界面如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3705d4385742472f926205780ed4d5bb~tplv-k3u1fbpfcp-zoom-1.image)

**服务端接口编写**

本课程采用 `Node` 的上层架构 [Egg.js](https://eggjs.org/zh-cn/)，它是由阿里研发维护的，并且是基于 `Koa` 开发，有着高度可扩展的插件机制，很多需求我们可以通过插件的形式来实现，大厂的使用率也很高，文档相对国人友好，学习成本较低。

这里有一份前端早早聊大会公开的各大公司团队的[技术选型](https://www.yuque.com/zaotalk/team/st#6edd)，可以看到 `Node` 这块技术栈，使用 `Egg.js` 的公司占不小的比例。并且大厂都会有自己的前端基建，多数情况下也是采用的 `Egg.js` 作为基础 `Node` 框架。

既然大厂都在使用 `Egg.js`，想要获得更强的竞争力，你需要好好地学习它。

我所在的公司也不例外，包括海报生成、二维码生成、截图服务、静态资源 `CDN` 服务都是基于 `Egg.js` 开发的。


**前端开发**

前端部分采用目前大厂最爱的 `React`，全程使用 `React Hook` 的形式编写。由于咱们做的是记账本，属于金融类项目，所以本小册采用的是 [ZarmUI](https://zarm.gitee.io/#/) 作为组件库。组件库的使用需要根据项目而定，比如你开发的是 `toB` 的管理后台类项目，建议采用 [Ant Design](https://ant-design.gitee.io/docs/react/introduce-cn)。

脚手架采用的是 `Vite2.0`，它在开发模式下的冷启动，让你真正体验到秒更新的快感。我认为 `esm` 的模块化规范会是未来的趋势，趁早学习，占据主动。

后续的章节会对 `Vite` 做一个详细全面的分析。

最终会带大家开发出一个 `toC` 项目，如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bcfa727648c4c73be85524e8b028550~tplv-k3u1fbpfcp-zoom-1.image)

**部署上线**

服务端的部署会教大家如何在服务器环境下安装 `MySQL`，前端和后端的代码，会通过 `pm2` 完成自动化部署，部署线上的前提条件是，需要你有一台云服务器。

## 适宜人群

**1、前端职业生涯前期，遇到学习瓶颈的同学。**

- 局限于前端的知识体系，会让你的思路也同样局限于前端的领域，拓展你的知识面，可以让你对整个技术的认知进入新的高度。

**2、在校学生，希望通过开发实战项目，完成毕设的同学。**

- 本项目带大家从 0 到 1 开发出一个完整的前后端项目，有助于即将毕业的同学很好的理解整个项目的开发过程，在写论文的时候，也能游刃有余。

**3、想通过学习 `Node`，拓展技能树，升职加薪的同学。**

- 多数在小厂做前端开发的同学应该有所体会，一直都是做一些不那么锻炼技术的后台管理系统。这些技能树可能不能很好地支撑你的涨薪诉求，入门 `Node` 后，你可以做一些提高开发效率的工具，帮助你获得更好的升职加薪的机会。

**4、想开启[「远程工作」](https://eleduck.com/)的同学。**

- 远程工作，很多时候需要你既会前端，又得回后端，因为雇佣者开发成本有限，需要开发人员的技能树尽可能的多。

## 我的职责

我并不是大佬，我只是一个处在这个内卷的 IT 大环境下，不得不埋头向前的普通前端。相信和我一样的普通前端是占多数的，没有过人的天分，靠的多是自己的自觉和自律。职业生涯是漫长的，希望我能陪你走过这漫长职业生涯中的一小段。用我喜欢的一句话结尾。

> “以大多数人的努力程度之低，根本轮不到拼天赋。”

## 总结

风里雨里，我在交流群等你。

## 10.前端预备：现代前端框架单页面概念

## 前言

服务端的内容基本上已经结束，从本章节开始，带大家进入前端部分的实战环节。本项目前端部分使用 `React` 作为前端框架，所以先带大家理解什么是单页面，它是怎样实现页面组件之间的切换，路由的原理等知识点。

#### 知识点

- 传统页面 DOM 直出

- 单页面原理

- 前端路由实现

## 单页面

前端自从进入三大框架时代以来，传统的多页面开发已渐渐淡出人们的视线。为了更好的了解现在，我们先要去知道它的过去。

#### 传统页面

这里不纠结叫法，凡是整个项目都是 `DOM` 直出的页面，我们都称它为“传统页面”（SSR 属于首屏直出，这里我不认为是传统页面的范畴）。那么什么是 `DOM` 直出呢？简单说就是在浏览器输入网址后发起请求，返回来的 `HTML` 页面是最终呈现的效果，那就是 `DOM` 直出。并且每次点击页面跳转，都会重新请求 `HTML` 资源。耳听为虚，眼见为实。我们以这个地址为例，验证以下上述说法。

> https://www.cnblogs.com/han-1034683568/p/14126727.html#4773138

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90c234badd9b412399615c1622fb78e2~tplv-k3u1fbpfcp-zoom-1.image)

腚眼一看，就能明白上图在描述什么。没错，博客园就是一个传统页面搭建而成的网站，每次加载页面，都会返回 `HTML` 资源以及里面的 `CSS` 等静态资源，组合成一个新的页面。
还没明白的同学，我再教一个方法，就是在浏览器页面右键，点击“显示网页源代码”，打开后如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c14b94fc22de47be8ae7bf7b1476b24b~tplv-k3u1fbpfcp-zoom-1.image)

网页上能看到什么图片或文字，你能在上述图片中找到相应的 `HTML` 结构，那也属于传统页面，也就是 `DOM` 直出。

#### 单页面

时代在进步，科技在发展，面对日益增长的网页需求，网页开始走向模块化、组件化的道路。随之而来的是代码的难以维护、不可控、迭代艰难等现象。面临这种情况，催生出不少优秀的现代前端框架，首当其冲的便是 `React` 、 `Vue` 、 `Angular` 等著名单页面应用框架。而这些框架有一个共同的特点，便是“通过 `JS` 渲染页面”。
举个例子，以前我们直出 `DOM` ，而现在运用这些单页面框架之后， `HTML` 页面基本上只有一个 `DOM` 入口，大致如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ffef8918b4a4b9cb4401cc7a6dc4eb4~tplv-k3u1fbpfcp-zoom-1.image)

所有的页面组件，都是通过运行上图底部的 `app.js` 脚本，挂载到 `<div id="root"></div>` 这个节点下面。用一个极其简单的 `JS` 展示挂载这一个步骤：

```html
<body>
  <div id="root"></div>
  <script>
    const root = document.getElementById('root') // 获取根节点
    const divNode = document.createElement('div') // 创建 div 节点
    divNode.innerText = '你妈贵姓？' // 插入内容
    root.appendChild(divNode) // 插入根节点
  </script>
</body>
```

所有的节点都通过 `createElement` 方法创建，最终通过 `appendChild` 的形式插入到 `root` 根节点。

那么问题来了，我如果有十几个页面需要这样的操作咋整？

这时候「前端路由」应运而生，它的出现就是为了解决单页面网站多个页面组件切换。通过切换浏览器地址路径，来匹配相对应的页面组件。我们通过一张丑陋的图片来理解这个过程：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ac50c7ba4cd4d85bbbdb3cd491b1e47~tplv-k3u1fbpfcp-zoom-1.image)

「前端路由」会根据浏览器地址栏 `pathname` 的变化，去匹配相应的页面组件。然后将其通过创建 `DOM` 节点的形式，塞入根节点 <div id="root"></div> 。这就达到了无刷新页面切换的效果，从侧面也能说明正因为无刷新，所以 `React` 、 `Vue` 、 `Angular` 等现代框架在创建页面组件的时候，每个组件都有自己的「生命周期」。

#### 路由实现原理

「前端路由」插件比较火的俩框架对应的就是 `Vue-Router` 和 `React-Router` ,但是它们的逻辑，归根结底还是一样的，用殊途同归四个字，再合适不过。

通过分析「哈希模式」和「历史模式」的实现原理，让大家对前端路由的原理有一个更深刻的理解。

**哈希模式(hash)**

`a` 标签锚点大家应该不陌生，而浏览器地址上 `#` 后面的变化，是可以被监听的，浏览器为我们提供了原生监听事件 `hashchange`，它可以监听到如下的变化：

- 点击 `a` 标签，改变了浏览器地址。   

- 浏览器的前进后退行为。

- 通过 `window.location` 方法，改变浏览器地址。

接下来我们利用这些特点，去实现一个 hash 模式的简易路由： [在线运行](https://codepen.io/nick930826/pen/BaLGprx)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Hash 模式</title>
</head>
  <body>
    <div>
      <ul>
        <li><a href="#/page1">page1</a></li>
        <li><a href="#/page2">page2</a></li>
      </ul>
      <!--渲染对应组件的地方-->
      <div id="route-view"></div>
    </div>
  <script type="text/javascript">
    // 第一次加载的时候，不会执行 hashchange 监听事件，默认执行一次
    // DOMContentLoaded 为浏览器 DOM 加载完成时触发
    window.addEventListener('DOMContentLoaded', Load)
    window.addEventListener('hashchange', HashChange)
    // 展示页面组件的节点
    var routeView = null
    function Load() {
      routeView = document.getElementById('route-view')
      HashChange()
    }
    function HashChange() {
      // 每次触发 hashchange 事件，通过 location.hash 拿到当前浏览器地址的 hash 值
      // 根据不同的路径展示不同的内容
      switch(location.hash) {
      case '#/page1':
        routeView.innerHTML = 'page1'
        return
      case '#/page2':
        routeView.innerHTML = 'page2'
        return
      default:
        routeView.innerHTML = 'page1'
        return
      }
    }
  </script>
  </body>
</html>
```

> 当然，这是很简单的实现，真正的 hash 模式，还要考虑到很多复杂的情况，大家有兴趣就去看看源码。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c63aefb5291845bda877ec0a1d1a7fee~tplv-k3u1fbpfcp-zoom-1.image)

**历史模式(history)**

`history` 模式会比 `hash` 模式稍麻烦一些，因为 `history` 模式依赖的是原生事件 `popstate`，下面是来自 MDN 的解释：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e778ae17bb64effb55b03edad66f8df~tplv-k3u1fbpfcp-zoom-1.image)

> 小知识：pushState 和 replaceState 都是 HTML5 的新 API，他们的作用很强大，可以做到改变浏览器地址却不刷新页面。这是实现改变地址栏却不刷新页面的重要方法。

包括 `a` 标签的点击事件也是不会被 `popstate` 监听。我们需要想个办法解决这个问题，才能实现 `history` 模式。

解决思路：我们可以通过遍历页面上的所有 `a` 标签，阻止 `a` 标签的默认事件的同时，加上点击事件的回调函数，在回调函数内获取 `a` 标签的 `href` 属性值，再通过 `pushState` 去改变浏览器的 `location.pathname` 属性值。然后手动执行 `popstate` 事件的回调函数，去匹配相应的路由。逻辑上可能有些饶，我们用代码来解释一下：[在线地址](https://codepen.io/nick930826/pen/BaLGprx)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>History 模式</title>
</head>
<body>
  <div>
    <ul>
      <li><a href="/page1">page1</a></li>
      <li><a href="/page2">page2</a></li>
    </ul>
    <div id="route-view"></div>
  </div>
  <script type="text/javascript">
    window.addEventListener('DOMContentLoaded', Load)
    window.addEventListener('popstate', PopChange)
    var routeView = null
    function Load() {
      routeView = document.getElementById('route-view')
      // 默认执行一次 popstate 的回调函数，匹配一次页面组件
      PopChange()
      // 获取所有带 href 属性的 a 标签节点
      var aList = document.querySelectorAll('a[href]')
      // 遍历 a 标签节点数组，阻止默认事件，添加点击事件回调函数
      aList.forEach(aNode => aNode.addEventListener('click', function(e) {
        e.preventDefault() //阻止a标签的默认事件
        var href = aNode.getAttribute('href')
        //  手动修改浏览器的地址栏
        history.pushState(null, '', href)
        // 通过 history.pushState 手动修改地址栏，
        // popstate 是监听不到地址栏的变化，所以此处需要手动执行回调函数 PopChange
        PopChange()
      }))
    }
    function PopChange() {
      console.log('location', location)
      switch(location.pathname) {
      case '/page1':
        routeView.innerHTML = 'page1'
        return
      case '/page2':
        routeView.innerHTML = 'page2'
        return
      default:
        routeView.innerHTML = 'page1'
        return
      }
    }
  </script>
</body>
</html>
```

> 这里注意，不能在浏览器直接打开静态文件，需要通过 web 服务，启动端口去浏览网址。默认打开的协议是 file 协议，它是不会被 `popstate` 监听的。

## 总结

认真阅读完上述内容，基本上对前端单页面的实现原理有了一个大概的雏形，更深入的学习还是需要再对框架的源码进行分析。

## 11.前端预备：从一个数据请求，入门 React Hooks

## 前言

`React` 早期的写法以 `Class` 类组件为主，附带一些纯用于展示的函数组件，但是函数组件是不能控制自身的状态的。

直到 16.8 版本出来之后，引入了全新的 `Hooks` 写法，这让之前的类写法就显得 比较累赘，函数组件的写法开始流行起来。函数组件引入了多种钩子函数如 `useEffect`、`useState`、`useRef`、`useCallback`、`useMemo`、`useReducer` 等等，通过这些钩子函数来管理函数组件的各自状态。

## 正文

本章节我会通过一个请求，带大家入门整个 `React Hook` 知识体系。首先我们需要创建一个空项目，由于本实验采用的是 `Vite 2.0` 作为脚手架工具，所以我们的 `Node` 版本必须要在 `12.0.0` 以上，目前我的版本是 `12.6.0`。

我们通过指令新建一个联手项目，如下所示：

```bash
# npm 6.x
npm init @vitejs/app hooks-demo --template react

# npm 7+, 需要额外的双横线：
npm init @vitejs/app hooks-demo -- --template react

# yarn
yarn create @vitejs/app hooks-demo --template react
```

根据你的需求，选择上述三个其中一个。新建之后项目目录如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a994cd755bb34164ba5abff2c88af997~tplv-k3u1fbpfcp-zoom-1.image)

```bash
npm install
npm run dev
```

如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b82ef228cba417bb1f6f910c2406abf~tplv-k3u1fbpfcp-zoom-1.image)

看到如上述所示代表项目已经启动成功了。

#### useState

接下来我们清空 `App.jsx`，添加如下代码：

```js
import React, { useState } from 'react'

function App() {
  const [data, setData] = useState([1, 2, 3, 4, 5])
  return (
    <div className="App">
      {
        data.map((item, index) => <div key={index}>{item}</div>)
      }
    </div>
  )
}

export default App
```

函数内声明变量，可以通过 `useState` 方法，它接受一个参数，可以为默认值，也可以为一个函数。上述我们先分析默认值的情况，默认给一个数组 `[1, 2, 3, 4, 5]`，`data` 参数便可以直接在 `JSX` 模板中使用。

#### useEffect

此时，我们通过 `useEffect` 副作用，请求一个接口数据，如下所示：

```js
import React, { useEffect, useState } from 'react'
// 模拟数据接口，3 秒钟返回数据。
const getList = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve([6, 7, 8, 9, 10])
    }, 3000)
  })
}

function App() {
  const [data, setData] = useState([1, 2, 3, 4, 5])

  useEffect(() => {
    (async () => {
      const data = await getList()
      console.log('data', data)
      setData(data)
    })()
  })
  return (
    <div className="App">
      {
        data.map((item, index) => <span key={index}>{item}</span>)
      }
    </div>
  )
}

export default App
```

函数组件默认进来之后，会执行 `useEffect` 中的回调函数，但是当 `setData` 执行之后，`App` 组件再次刷新，刷新之后会再次执行 `useEffect` 的回调函数，这便会形成一个可怕的死循环，回调函数会一直被这样执行下去。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3187ae7425542beb62f3b207e27acb0~tplv-k3u1fbpfcp-zoom-1.image)

所以这里引出 `useEffect` 的第二个参数。它是一个数组，数组内接收回调函数内使用到的状态参数，一旦在组件内改变了状态参数，则会触发副作用 `useEffect` 的回调函数执行。

所以我们如果传一个空数组 `[]`，则该副作用只会在组件渲染的时候，执行一次，如下所示：

```js
useEffect(() => {
  (async () => {
    const data = await getList()
    console.log('data', data)
    setData(data)
  })()
}, [])
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f1c917ab81e41d19dbbf0ea5d31c4ed~tplv-k3u1fbpfcp-zoom-1.image)

执行一次之后，副作用不再被触发。

此时我们需要给请求一个 `query` 参数，如下所示：

```js
import React, { useEffect, useState } from 'react'

const getList = (query) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log('query', query)
      resolve([6, 7, 8, 9, 10])
    }, 3000)
  })
}

function App() {
  const [data, setData] = useState([1, 2, 3, 4, 5])
  const [query, setQuery] = useState('')

  useEffect(() => {
    (async () => {
      const data = await getList(query)
      console.log('data', data)
      setData(data)
    })()
  }, [query])
  return (
    <div className="App">
      {
        data.map((item, index) => <span key={index}>{item}</span>)
      }
      <input onChange={(e) => setQuery(e.target.value)} type="text" placeholder='请输入搜索值' />
    </div>
  )
}

export default App
```

此时我们改变 `query` 的值，副作用函数便会被执行，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef93bf033594ba0b2272f59a99e2447~tplv-k3u1fbpfcp-zoom-1.image)

所以，如果你的接口有查询参数，可以将参数设置在 `useEffect` 的第二个参数的数组值中，这样改变查询变量的时候，副作用便会再次触发执行，相应的函数也会重新带着最新的参数，获取接口数据。

#### 自定义 Hook

我们可以将上述的请求，抽离成一个自定义 `hook`，方便在多个地方调用，新建 `useApi.js` 如下所示：

```js
import React, { useEffect, useState } from 'react'
// 模拟请求
const getList = (query) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      console.log('query', query)
      resolve([6, 7, 8, 9, 10])
    }, 3000)
  })
}
// 自定义 hook
const useApi = () => {
  const [data, setData] = useState([1, 2, 3, 4, 5])
  const [query, setQuery] = useState('')

  useEffect(() => {
    (async () => {
      const data = await getList()
      console.log('data', data)
      setData(data)
    })()
  }, [query])

  return [{ data }, setQuery];
}

export default useApi
```

如上述所示，最终将 `data` 数据，和设置请求参数的方法抛出，在 `App.jsx` 中做如下改动：

```js
import React from 'react'
import useApi from './useApi'

function App() {
  const [{ data }, setQuery] = useApi()
  return (
    <div className="App">
      {
        data.map((item, index) => <span key={index}>{item}</span>)
      }
      <input onChange={(e) => setQuery(e.target.value)} type="text" placeholder='请输入搜索值' />
    </div>
  )
}

export default App
```

我们查看浏览器展示结果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7372c75f23457eb8d114c2bb5d56a5~tplv-k3u1fbpfcp-zoom-1.image)

上述这类自定义 `Hook` 的使用，在开发中也非常常见，比如有一个请求公共数据的接口，在多个页面中被重复使用，你便可通过自定义 `Hook` 的形式，将请求逻辑提取出来公用，这也是之前 `Class` 类组件所不能做到的。

#### useMemo

我们修改 `App.jsx`，在内部新增一个子组件，子组件接收父组件传进来的一个对象，作为子组件的 `useEffect` 的第二个依赖参数。

```js
import React, { useEffect, useState } from 'react'

function Child({ data }) {
  useEffect(() => {
    console.log('查询条件：', data)
  }, [data])

  return <div>子组件</div>
}


function App() {
  const [name, setName] = useState('')
  const [phone, setPhone] = useState('')
  const [kw, setKw] = useState('')

  const data = {
    name,
    phone
  }

  return (
    <div className="App">
      <input onChange={(e) => setName(e.target.value)} type="text" placeholder='请输入姓名' />
      <input onChange={(e) => setPhone(e.target.value)} type="text" placeholder='请输入电话' />
      <input onChange={(e) => setKw(e.target.value)} type="text" placeholder='请输入关键词' />
      <Child data={data} />
    </div>
  )
}

export default App
```

当我们修改姓名和电话的时候，观察子组件是否监听到依赖的变化，执行 `useEffect` 内的回调函数。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97c533fa2d7a44f491734454089b3b84~tplv-k3u1fbpfcp-zoom-1.image)

此时，上述的结果是我们预期的，我们只监听了 `name` 和 `phone` 两个参数，但是我们修改关键词输入框，会得到下面的结果。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d40462facac94aea91209bb5cbc1cedc~tplv-k3u1fbpfcp-zoom-1.image)

子组件并没有监听 `kw` 的变化，但是结果却是子组件也被触发渲染了。原因其实是我们在父组件重新 `setKw` 之后，`data` 值和未作修改 `kw` 前的值已经不一样了。你可能会说，`data` 的值并没有变化，为什么说它已经不一样了呢？详细的分析我们放在后续部分，我们此时可以通过 `useMemo` 将 `data` 包装一下，告诉 `data` 它需要监听的值。

```js
import React, { useEffect, useState, useMemo } from 'react'

function Child({ data }) {
  useEffect(() => {
    console.log('查询条件：', data)
  }, [data])

  return <div>子组件</div>
}


function App() {

  const [name, setName] = useState('')
  const [phone, setPhone] = useState('')
  const [kw, setKw] = useState('')

  const data = useMemo(() => ({
    name,
    phone
  }), [name, phone])

  return (
    <div className="App">
      <input onChange={(e) => setName(e.target.value)} type="text" placeholder='请输入姓名' />
      <input onChange={(e) => setPhone(e.target.value)} type="text" placeholder='请输入电话' />
      <input onChange={(e) => setKw(e.target.value)} type="text" placeholder='请输入关键词' />
      <Child data={data} />
    </div>
  )
}

export default App
```

效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c6a5ab0f6784e8bb1d45a7d2b5eb883~tplv-k3u1fbpfcp-zoom-1.image)

这便是 `useMemo` 的作用，它相当于把父组件需要传递的参数做了一个标记，无论父组件其他状态更新任何值，都不会影响要传递给子组件的对象。

#### useCallback

同理，`useCallback` 也是和 `useMemo` 有类似的功能，比如我们传递一个函数给子组件，如下所示：

```js
import React, { useEffect, useState, useCallback } from 'react'

function Child({ callback }) {
  useEffect(() => {
    callback()
  }, [callback])

  return <div>子组件</div>
}


function App() {

  const [name, setName] = useState('')
  const [phone, setPhone] = useState('')
  const [kw, setKw] = useState('')

  const callback = () => {
    console.log('我是callback')
  }

  return (
    <div className="App">
      <input onChange={(e) => setName(e.target.value)} type="text" placeholder='请输入姓名' />
      <input onChange={(e) => setPhone(e.target.value)} type="text" placeholder='请输入电话' />
      <input onChange={(e) => setKw(e.target.value)} type="text" placeholder='请输入关键词' />
      <Child callback={callback} />
    </div>
  )
}

export default App
```

当我们修改任何状态值，都会触发子组件的回调函数执行，但是 `callback` 没有作任何变化。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5a9b334d4514959aa7cebe0006257a8~tplv-k3u1fbpfcp-zoom-1.image)

此时，我们给要传递的函数，包裹一层 `useCallback`，如下所示：

```js
const callback = useCallback(() => {
  console.log('我是callback')
}, [])
```

无论修改其他任何属性，都不会触发子组件的副作用：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1742b2a340c24cd4b439d17547265e48~tplv-k3u1fbpfcp-zoom-1.image)

> useCallback 的第二个参数同 `useEffect` 和 `useMemo` 的第二个参数，它是用于监听你需要监听的变量，如在数组内添加 `name`、`phone`、`kw` 等参数，当改变其中有个，都会触发子组件副作用的执行。

所以，`useMemo` 和 `useCallback`，都能为「重复渲染」这个问题，提供很好的帮助。

## 重新认识 useEffect

上述很多现象，都是因为你没有很好地去理解 `React Hooks` 函数组件写法的渲染机制。通过一个小例子，我们来重新认识 `useEffect`。

我们将上述 `App.jsx` 作如下修改：

```js
import React, { useEffect, useState } from 'react'

function App() {
  const [count, setCount] = useState(0)
  
  const handleClick = () => {
    setTimeout(() => {
      console.log('点击次数: ' + count);
    }, 3000);
  }

  return (
    <div className="App">
      <button onClick={() => setCount(count + 1)}>点击{count}次</button>
      <button onClick={handleClick}>展示点击次数</button>
    </div>
  )
}

export default App
```

我们作下列几个动作：

1、点击增加按钮两次，将 `count` 增加到 2。

2、点击「展示点击次数」。

3、在 `console.log` 执行之前，也就是 3 秒内，再次点击新增按钮 2 次，将 `count` 增加到 4。

按照正常的思路，浏览器应该打印出 `点击次数: 4`，我们来查看浏览器的展示效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1975c7d4488e4c9a854606cb4dfa1009~tplv-k3u1fbpfcp-zoom-1.image)

点击「展示点击次数」按钮，3 秒后，我们看到的结果是 `点击次数: 2`，这与我们的预期有出入。

函数组件 `App`，在每一次渲染都会被调用，而每一次调用都会形成一个独立的上下文，可以理解成一个快照。每一次渲染形成的快照，都是互相独立的。

默认进来的时候，形成一个快照，此时 `count` 为 0；当我们点击新增按钮第一次，执行 `setCount`，函数组件被刷新一次，此时的快照中，`count` 为 1；再次点击按钮，再次生成快照，此时的 `count` 为 2，此时点击 「展示点击次数」按钮，在这份快照中，我们的 `count` 参数就是 2。所以我们后面无论怎么新增 `count`，最终输出的结果 `count` 就是 2。

我们用一份伪代码来解释，大致如下：

```js
// 默认初始化
function App() {
  const count = 0; // useState 返回默认值
  // ...
  function handleClick() {
    setTimeout(() => {
      console.log('点击次数: ' + count);
    }, 3000);
  }
  // ...
}

// 第一次点击
function App() {
  const count = 1; // useState 返回值
  // ...
  function handleClick() {
    setTimeout(() => {
      console.log('点击次数: ' + count);
    }, 3000);
  }
  // ...
}

// 第二次点击
function App() {
  const count = 2; // useState 返回值
  // ...
  function handleAlertClick() {
    setTimeout(() => {
      console.log('点击次数: ' + count);
    }, 3000);
  }
  // ...
}
```

上述代码中，第二次点击的快照中，`console.log('点击次数: ' + count);` 取的便是 `const count = 2`。

同理，我们可以直到，每次渲染函数组件时，`useEffect` 都是新的，都是不一样的。我们对上面的写法稍作改动。

```js
import React, { useEffect, useState } from 'react'

function App() {
  const [count, setCount] = useState(0)
  
  useEffect(() => {
    setTimeout(() => {
      console.log('点击次数: ' + count);
    }, 3000);
  })

  return (
    <div className="App">
      <button onClick={() => setCount(count + 1)}>点击{count}次</button>
    </div>
  )
}

export default App
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bef605a7a9c45f19f950be4e94a0c31~tplv-k3u1fbpfcp-zoom-1.image)

每一次点击，都会重新执行 `useEffect` 内的回调，并且 `count` 值也是当时的快照的一个常量值。

这和之前的类组件是不同的，我们改成类组件的实现形式如下：

```js
import React from 'react'

export default class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      count: 0
    }
  }
  componentDidUpdate() {
    setTimeout(() => {
      console.log('点击次数: ' + this.state.count);
    }, 3000);
  }

  render() {
    return <button onClick={() => this.setState({ count: this.state.count + 1 })}>点击{this.state.count}次</button>
  }
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c175d79f67284e59ad4e9794e2ff2355~tplv-k3u1fbpfcp-zoom-1.image)

类组件，声明之后，会在内部生成一个实例 `instance`，所有的数据都会存在类的上下文中，所以 `this.state.count` 会一直指向最新的 `count` 值。

说到这里，大家应该对 `React Hooks` 的函数组件写法有了新的认识。

## 总结

行文至此，希望让同学们能好好地阅读和学习本章节的内容，以及课后对 `React Hooks` 的拓展。更好的理解它，有助于写出可维护、可拓展的代码，技术本身是服务于业务需求的，但是你不能很好的利用技术的特点，那业务也很难达到做满意的效果。


## 12.前端预备：Vite 2.0 下一代前度开发构建工具

## 前言

我还是那句话，工具永远是服务于需求的。纵观整个前端生态的项目构建工具，有服务于 `React` 生态的 `create-react-app`、`umi`、`Next.js` 等。服务于 `Vue` 生态的 `Vue CLI`、`Vite`、`Nuxt.js` 等。它们都是耳熟能详的团队和大佬，为了解决各自需求而研发出来的前端构建工具。而我们要做的其实就是根据项目的需求，进行合理的选择和学习。说白了，在你没有决定权的时候，公司用什么，你就学什么。在你有话语权，能自己抉择的时候，哪个让你开发起来比较舒服，就用哪个。

这些构建工具中，有一个比较特殊，那就是 `Vite`，它是尤雨溪在发布 `Vue 3.0` 时，同步推出的一款前端构建工具。它不光服务于 `Vue`，同时也对其他的框架如 `React`、`Svelte`、`Preact` 都有一定的支持，我们本着学新不学旧的理念，在项目中引进了 `Vite` 作为构建工具。

在开始使用 `Vite` 之前，我们来认识一下它。

#### 知识点

- `Vite` 是什么。

- `Vite` 与 `Webpack` 相比优势在哪里。

- `Vite` 的构建原理。

## Vite 是什么

我们引用官方的一句话来介绍它，“下一代前端开发与构建工具”。

它有以下几个特点：

1、 快速启动，`Vite` 会在本地启动一个开发服务器，来管理开发环境的资源请求。

2、相比 `Webpack` 的开发环境打包构建，它在开发环境下是无需打包的，热更新相比 `Webpack` 会快很多。

3、原生 `ES Module`，要什么就当场给你什么。而 `Webpack` 则是先将资源构建好之后，再根据你的需要，分配给你想要的资源。

尤雨溪在发布 `Vite` 前，发过这么一条微博。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b6344806ae94c96b9060fb0a3b13381~tplv-k3u1fbpfcp-zoom-1.image)

从话语间可以看出，尤雨溪团队对该打包工具也是报以厚望，所以这里大家可以不必担心后续它们会放弃维护这个项目，当然也不能打包票。

## Vite 与 Webpack 相比优势在哪里

接下来我们来聊聊，为什么说它是下一代前端开发与构建工具。是不是当代构建工具出了什么问题？

我们知道当代的前端构建工具有很多，比较受欢迎的有 `Webpack`、`Rollup`、`Parcel`等，绝大多数脚手架工具都是使用 `Webpack` 作为构建工具，如 `Vue-CLI`。

在利用 `Webpack` 作为构建工具时，开发过程中，每次修改代码，都会导致重新编译，随着项目代码量的增多，热更新的速度也随之变慢，甚至要几秒钟才能看到视图的更新。

生产环境下，它将各个模块之间通过编码的方式联系在一起，最终生成一个庞大的 `bundle` 文件。

导致这些问题出现的原因，有以下几点：

1、`HTTP 1.1` 时代，各个浏览器资源请求并发是有上限的（如谷歌浏览器为 6 个，这导致你必须要减少资源请求数）。

2、浏览器并不支持 `CommonJS` 模块化系统（它不能直接运行在浏览器环境下，它是 `Node` 提出的模块化规范，所以需要经过 `Webpack` 的打包，编译成浏览器可识别的 JS 脚本）

3、模块与模块之间的依赖顺序和管理问题（文件依赖层级越多，静态资源也就变得越多，如果一个资源有 100 个依赖关系，可能需要加载 100 个网络请求，这对生产环境可能是灾难，所以在生产环境最终会打包成一个 `bundle` 脚本，会提前进行资源按需加载的配置。）

#### 那么为什么现在又出现了不打包的构建趋势？

1、工程越来越庞大，热更新变得缓慢，十分影响开发体验。推动着我们不断地去创新，不断地尝试着去突破瓶颈。

2、各大浏览器已经开始慢慢的支持原生 `ES Module` (谷歌、火狐、`Safari`、`Edge` 的最新版本，都已支持。这让我们看到了希望)。

3、`HTTP 2.0` 采用的多路复用。不用太担心请求并发量的问题。

4、越来越多的 `npm` 包开始采用了原生 `ESM` 的开发形式。虽然还有很多包不支持，但是我相信这将会是趋势。

我们通过表格的形式，对比一下 `bundle` 和 `bundleless` 的区别。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff916f65816b469989198bdc2ec18fd1~tplv-k3u1fbpfcp-zoom-1.image)

## Vite 构建原理

众所周知，`Vite` 的生产模式和开发模式是不同的概念。我们先聊聊，`Vite` 的开发模式。

首先要明确一点，`Vite` 在开发模式下，有一个 <span style="color: red">依赖预构建</span> 的概念。

#### 什么是依赖预构建

在 `Vite` 启动开发服务器之后，它将第三方依赖的多个静态资源整合为一个，比如 `lodash`、`qs`、`axios` 等这类资源包，存入 ·node_modules/.vite 文件下。

#### 为什么需要依赖预构建

如果直接采用 `ES Module` 的形式开发代码，会产生一大串依赖，就好像俄罗斯套娃一样，一层一层的嵌套，在浏览器资源有限的情况下，同时请求大量的静态资源，会造成浏览器的卡顿，并且资源响应的时间也会变慢。

我们先不通过 `Vite`，而是手动搭建原生 `ES Module` 开发形式，通过引入 `lodash-es` 包，实现一个数组去重的小例子，来详细分析为什么需要依赖预构建。

新建 `test1` 文件夹，通过 `npm init -y` 初始化了一个前端工程：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eabc5b637e734347b8e7965496669fee~tplv-k3u1fbpfcp-zoom-1.image)

手动新建 `index.html`，通过 `script` 标签，引入 `main.js`。这里注意，需要将 `type` 属性设置为 `module`，这样才能支持 `ES Module` 模块化开发。

通过 `npm` 安装 `lodash-es`，这里我们之所以不使用 `lodash`，是因为 `lodash` 不是通过 `ES Module` 形式开发的，直接通过相对路径引入会报错，需要通过 `Webpack` 打包构建。

```bash
npm i lodash-es
```

新建 `main.js` 添加去重逻辑：

```js
import uniq from './node_modules/lodash-es/uniq.js'

const arr = [1, 2, 3, 3, 4]

console.log(uniq(arr))
```

这里我们采用 `VSCode` 的插件，`Live Server`，来启动项目。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30054fefbeaf485a96db8d4a4d8f5aad~tplv-k3u1fbpfcp-zoom-1.image)

安装完之后，在项目中双击 `index.html`，找到右下角的 「Go Live」，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64858bc1bd3e4206a4b996c8ba4f5d74~tplv-k3u1fbpfcp-zoom-1.image)

点击后，自动启动一个 `Web` 服务，浏览器自动打开，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3858ec887f744781b6c45fadad638c2c~tplv-k3u1fbpfcp-zoom-1.image)

结果正确，数组中的 3 被去除了，接下来关键的一个点，我们点击  `Network` 查看，资源引入情况：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b9e60c097184e20a78cb8198968b199~tplv-k3u1fbpfcp-zoom-1.image)

我们只是获取去重方法，却意外引入了 59 资源，这是为什么呢？

我们先查看 `main.js` 内的代码，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f001d806817f4ed5a9ad521c9a91a6d5~tplv-k3u1fbpfcp-zoom-1.image)

代码中只有在首行通过 `import` 引入了 `./node_modules/lodash-es/uniq.js`，所以 `uniq.js` 被作为资源引入进来，我们再看 `uniq.js` 的情况：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b21e238127c47ec8f69b16775b4bb08~tplv-k3u1fbpfcp-zoom-1.image)

`uniq.js` 中，首行通过 `import` 引入了 `_baseUniq.js`，我们继续：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6392953fd6b043ea99355687a5569763~tplv-k3u1fbpfcp-zoom-1.image)

`_baseUniq.js` 中，引入了上图箭头中的一些脚本，不用往下看，我盲猜这种俄罗斯套娃的模式，会一直引用到 `uniq.js` 相关的所有脚本代码。

这只是一个 `uniq` 方法，足足就引入了 59 个资源，这仿佛是在军训浏览器，也就是谷歌能跟它博弈几个回合，引入的包再多几个，我估计也是顶不住的。

所以这时候 `Vite` 便引入了「依赖预构建」的概念。

#### 依赖现预构建浅析

同样的，再通过 `Vite` 构建出一个 `React` 项目，去实现上述逻辑，我们观察 `Vite` 是怎么作的。

首先通过 `Vite` 指令生成项目：

```bash
npm init @vitejs/app test2 --template react
```

并安装 `lodash-es`，修改入口脚本 `main.jsx`：

```js
import uniq from 'lodash-es/uniq.js'

const arr = [1, 2, 3, 3, 4]

console.log(uniq(arr))
```

我们观察浏览器的 `Network`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dce2afc266e84fa79ee8c9a0c0266c85~tplv-k3u1fbpfcp-zoom-1.image)

注意上图，执行 `npm run dev` 后，脚本中引用 `lodash-es/uniq` 的路径是在 `/node_modules/.vite` 文件夹下，并且左下角的请求资源数，也没有我们之前原生 `ES Module` 时的多，少了足足 3/4 还多。

再观察文件目录：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/715c51aaea93420dac55e3ccca003222~tplv-k3u1fbpfcp-zoom-1.image)

`lodash-es/uniq` 已经被 `Vite` 提前预编译到了 `.vite` 文件夹下，这样代码中直接去这个文件夹拿现成的包，就不必再递归地去加载很多静态资源脚本。

## 总结

本章节，通过实例分析，对 `Vite` 有了初步的了解。那么下一章节，我将带大家通过 `Vite` 去搭建一个 `React` 的完整开发环境。



## 13.前端实战：Vite 2.0 + React + ZarmUI 搭建前端 H5 开发环境

## 前言

`React` 技术栈的 `UI` 组件库相比 `Vue`，会少一些。我们耳熟能详的便是 `Antd`，但是它针对的是 `PC` 端的，我们的项目目前是一个 `H5` 的网页（不排除后期做一个 PC 端）。所以我选择了 [Zarm](https:https://zarm.gitee.io/#/)。

这里再次强调，不是 `Zarm` 就比别的移动端组件库好，只是目前我开发的这款记账本项目，`Zarm` 比较适合。

#### 知识点

- 构架工具 `Vite`。

- 前端框架 `React` 和路由 `react-router-dom`。

- `CSS` 预加载器 `Less`。

- `HTTP` 请求库 `axios`。

- 移动端分辨率适配 `flexible`。

- 跨域代理。

## 初始化 Vite + React 项目

`Vite` 官方提供两种初始化项目的方式，一种是如下所示，可以自由选择需要的前端框架。

```bash
npm init @vitejs/app
```

另一种则是直接用官方提供的模板，一键生成项目：

```bash
# npm 6.x
npm init @vitejs/app react-vite-h5 --template react

# npm 7+, 需要额外的双横线：
npm init @vitejs/app react-vite-h5 -- --template react
```

我们使用第二种方式初始化项目，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32661c92fce54016949d56b5a57399ba~tplv-k3u1fbpfcp-zoom-1.image)

安装完 `node_modules` 之后，通过 `npm run dev` 启动项目，如下所示代表成功了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/874d34fcf2394af585b2c42a11cef607~tplv-k3u1fbpfcp-zoom-1.image)

## 引入路由插件 react-router-dom

没有路由的项目，那就不是一个完整项目，而是一个页面而已。真实项目都是存在各种模块之间的切换，各个模块的功能组合在一起才能叫做一个项目。

首选安装 `react-router-dom`，指令如下：

```bash
npm i react-router-dom -S
```

在项目 `src` 目录下新增 `container` 目录用于放置页面组件，再在 `container` 下新增两个目录分别是 `Index` 和 `About` ，添加如下内容：

```js
// Index/index.jsx
import React from 'react'

export default function Index() {
  return <div>
    Index
  </div>
}

// About/index.jsx
import React from 'react'

export default function About() {
  return <div>
    About
  </div>
}
```

再来新建 `src/router/index.js` 配置路由数组，添加如下内容：

```js
// router/index.js
import Index from '../container/Index'
import About from '../container/About'

const routes = [
  {
    path: "/",
    component: Index
  },
  {
    path: "/about",
    component: About
  }
];

export default routes
```

在 `App.jsx` 引入路由配置，实现切换浏览器路径，显示相应的组件：

```js
// App.jsx
import React, { useState } from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom"
import routes from '../src/router'
function App() {
  return <>
     <Routes>
      {routes.map(route => <Route exact key={route.path} path={route.path} element={<route.component />} />)}
     </Routes>
   </>
}

export default App
```

启动项目 `npm run dev`，如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d67090d0f61641539e3fcd9061d27474~tplv-k3u1fbpfcp-zoom-1.image)

## 引入 Zarm UI 组件库

首先通过如下指令安装它：

```bash
npm install zarm -S
```

修改 `App.jsx` 的代码，全局引入样式和中文包：

```js
import React, { useState } from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom"

import { ConfigProvider } from 'zarm'
import zhCN from 'zarm/lib/config-provider/locale/zh_CN'
import 'zarm/dist/zarm.css'

import routes from '../src/router'
function App() {
  return <Router>
    <ConfigProvider primaryColor={'#007fff'} locale={zhCN}>
      <>
       <Routes>
        {routes.map(route => <Route exact key={route.path} path={route.path} element={<route.component />} />)}
       </Routes>
      </>
    </ConfigProvider>
  </Router>
}

export default App
```

此时 `zarm` 的样式，已经全局引入了，我们先查看在 `/container/Index/index.jsx` 添加一个按钮是否生效：

```js
// Index/index.jsx
import React from 'react'
import { Button } from 'zarm'

export default function Index() {
  return <div>
    Index
    <Button theme='primary'>按钮</Button>
  </div>
}
```

重启项目，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5196fda769074ec387a085af87b6bb92~tplv-k3u1fbpfcp-zoom-1.image)

此时恭喜你🎉，你已经成功将组件引入项目中。

#### 小优化

组件虽然引入成功了，但是有一个问题，我不希望所有的组件样式都被一次性的引入，因为这样代码会比较冗余，我只需要引入我使用到的组件样式，实现「按需引入」。

我们先看看，就目前现在这个情况，打完包之后，静态资源有多大。运行指令 `npm run build` ，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba361939748e48499cab35833093c012~tplv-k3u1fbpfcp-zoom-1.image)

腚眼一看，全局引入样式的形式，直接打完包， `css` 静态资源就 `168.22kb` 了，我们尝试配置「按需引入」。

首先我们安装一个插件：

```bash
npm i vite-plugin-style-import -D
```

然后在 `vite.config.js` 配置文件内添加如下内容：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd0314c0446e4654bfcc73e3dee44291~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bcf00b0cb0c4293a2daf92bef93f451~tplv-k3u1fbpfcp-zoom-1.image)

打完包之后，肉眼可见，`css` 提及从 `168.22kb` -> `35.22kb`。这种方式也是前端性能优化的其中一种。

## 配置 CSS 预处理器 Less

项目中采用的 `Less` 作为 `CSS` 预处理器，它能设置变量以及一些嵌套逻辑，便于项目的样式编写。

安装 `less` 插件包，`npm i less -D`，因为上述配置我们使用的是 `less`，并且我们需要配置 `javascriptEnabled 为 true`，支持 `less` 内联 `JS`。

修改 `vite.config.js`，如下：

```js
{
  plugins: [...]
  css: {
    modules: {
      localsConvention: 'dashesOnly'
    },
    preprocessorOptions: {
      less: {
        // 支持内联 JavaScript
        javascriptEnabled: true,
      }
    }
  },
}
```

并且添加了 `css modules` 配置，这样我们就不用担心在项目中，自定义的样式重名的风险，我们尝试在 `/container/Index` 目录下添加样式文件 `style.module.less`，并且在 `/container/Index/index.jsx` 中引入它，如下：

```css
.index {
  span {
    color: red;
  }
}
```

```js
// Index/index.jsx
import React from 'react'
import { Button } from 'zarm'

import s from './style.module.less'

export default function Index() {
  return <div className={s.index}>
    <span>样式</span>
    <Button theme='primary'>按钮</Button>
  </div>
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8866be0be4824492b94297eea2eb4ca3~tplv-k3u1fbpfcp-zoom-1.image)

此时我只能再次恭喜你，`Less` 成功被引入。

## 移动端项目适配 rem

移动端项目，肯定是需要适配各种分辨率屏幕的，就比如你 10px 的宽度，在每个屏幕上的占比都是不一样的，我们这里不对分辨率做深入的探讨，我们目前的首要目的是完成项目移动端的分辨率适配。

首先我们需要安装 `lib-flexible`：

```bash
npm i lib-flexible -S
```

并在 `main.jsx` 中引入它：

```js
import React from 'react'
import ReactDOM from 'react-dom'
import 'lib-flexible/flexible'
import './index.css'
import App from './App'

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
)
```

然后再安装一个 `postcss-pxtorem`，它的作用是在你编写完 `css` 后，将你的单位自动转化为 `rem` 单位。

```bash
npm i postcss-pxtorem
```

在项目根目录新建 `postcss.config.js`：

```js
// postcss.config.js
// 用 vite 创建项目，配置 postcss 需要使用 post.config.js，之前使用的 .postcssrc.js 已经被抛弃
// 具体配置可以去 postcss-pxtorem 仓库看看文档
module.exports = {
  "plugins": [
    require("postcss-pxtorem")({
      rootValue: 37.5,
      propList: ['*'],
      selectorBlackList: ['.norem'] // 过滤掉.norem-开头的class，不进行rem转换
    })
  ]
}
```

修改 `Index/style.module.less`：

```css
.index {
  width: 200px;
  height: 200px;
  background: green;
  span {
    color: red;
  }
}
```

重启项目 `npm run dev`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28c6f12ba2c446ef9f374f878636c1f0~tplv-k3u1fbpfcp-zoom-1.image)

可以看到，`200px` 已经被转化为 `5.3333rem`，我们设置的 `rootValue` 是 `37.5`，你可以换算一下 `5.33333 * 37.5 = 200`。

我们目前把浏览器调整成的是 `iphone 6`，`html` 的 `font-size` 为 `37.5px`，当我们手机变成其他尺寸的时候，这个 `font-size` 的值也会变化，这是 `flexible` 起到的作用，动态的变化 `html` 的 `font-size` 的值，从而让 `1rem` 所对应的  `px` 值一直都是动态适应变化的。

当我切换成 `iphone 6 plus` 时：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b787a8e1e96d4db58622c23d89592954~tplv-k3u1fbpfcp-zoom-1.image)

变成了 `41.4px`，而相应的，我们 `div` 还是 `5.33333rem`，所以此时 `div` 宽度就变大了，但是手机的屏幕宽度也变大了，这就不会影响视觉上的比例误差太大。

## 二次封装 axios

说到这里，那就要涉及到项目的服务端 `API` 接口，我们在前面的章节里，已经完成了服务端的代码编写，但是此时我们的服务端项目是跑在 `http://127.0.0.1/7001` 端口上的。

此时你是可以在后续的请求中，使用 `http://127.0.0.1/7001` 作为项目的 `baseURL`。但是照顾到有些同学没有启动服务端项目，直奔前端项目来的。这里我已经将接口提前部署到了线上环境，供大家使用。接口地址是 `http://api.chennick.wang`。

所以在后续的封装过程中，我会提醒大家两种使用。

首先我们安装 `npm i axios -S`，在 `src` 目录下新建 `utils` 目录，并新建 `axios.js` 脚本：

```js
// src/utils/axios.js
import axios from 'axios'
import { Toast } from 'zarm'

const MODE = import.meta.env.MODE // 环境变量

axios.defaults.baseURL = MODE == 'development' ? '/api' : 'http://api.chennick.wang'
axios.defaults.withCredentials = true
axios.defaults.headers['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.headers['Authorization'] = `${localStorage.getItem('token') || null}`
axios.defaults.headers.post['Content-Type'] = 'application/json'

axios.interceptors.response.use(res => {
  if (typeof res.data !== 'object') {
    Toast.show('服务端异常！')
    return Promise.reject(res)
  }
  if (res.data.code != 200) {
    if (res.data.msg) Toast.show(res.data.msg)
    if (res.data.code == 401) {
      window.location.href = '/login'
    }
    return Promise.reject(res.data)
  }

  return res.data
})

export default axios
```

我逐行为大家分析上述代码的情况情况。

```js
const MODE = import.meta.env.MODE
```

`MODE` 是一个环境变量，通过 `Vite` 构建的项目中，环境变量在项目中，可以通过 `import.meta.env.MODE` 获取，环境变量的作用就是判断当前代码运行在开发环境还是生产环境。

```js
axios.defaults.baseURL = 'development' ? '/api' : 'http://api.chennick.wang'
```

`baseURL` 是 `axios` 的配置项，它的作用就是设置请求的基础路径，后续我们会在项目实战中有所体现。配置基础路径的好处就是，当请求地址修改的时候，可以在此统一配置。

```js
axios.defaults.headers['X-Requested-With'] = 'XMLHttpRequest'
axios.defaults.headers['Authorization'] = `${localStorage.getItem('token') || null}`
axios.defaults.headers.post['Content-Type'] = 'application/json'
```

上述三个配置是用于请求头的设置，`Authorization` 是我们在服务端鉴权的时候用到的，我们在前端设置好 `token`，服务端通过获取请求头中的  `token` 去验证每一次请求是否合法。

最后一行是配置 `post` 请求是，使用的请求体，这里默认设置成 `application/json` 的形式。

```js
axios.interceptors.response.use(res => {
  if (typeof res.data !== 'object') {
    Toast.show('服务端异常！')
    return Promise.reject(res)
  }
  if (res.data.code != 200) {
    if (res.data.msg) Toast.show(res.data.msg)
    if (res.data.code == 401) {
      window.location.href = '/login'
    }
    return Promise.reject(res.data)
  }

  return res.data
})
```

`interceptors` 为拦截器，拦截器的作用是帮你拦截每一次请求，你可以在回调函数中做一些“手脚”，再将数据 `return` 回去。上述代码就是拦截了响应内容，统一判断请求内容，如果非 200，则提示错误信息，`401` 的话，就是没有登录的用户，默认跳到 `/login` 页面。如果是正常的响应，则 `retrun res.data`。

最后我们将这个 `axios` 抛出，供页面组件请求使用。

在 `utils` 下新建一个 `index.js`，内容如下：

```js
import axios from './axios'

export const get = axios.get

export const post = axios.post
```

这样获取的时候，能少写几行代码，能少写点就少写点。

## 代理配置

`baseURL` 为什么在 `development` 环境下，用 `/api` 这样的请求地址。其实它就是为了代理请求而配置的。

这样配置完后，在请求接口的时候，请求地址大概长这样：

```js
/api/userInfo
```

于是我们需要去配置代理，打开 `vite.config.js`，添加如下代码：

```js
server: {
  proxy: {
    '/api': {
      // 当遇到 /api 路径时，将其转换成 target 的值
      target: 'http://api.chennick.wang/api/',
      changeOrigin: true,
      rewrite: path => path.replace(/^\/api/, '') // 将 /api 重写为空
    }
  }
}
```

这样配置完之后，开发环境下，`/api/userInfo` -> `http://api.chennick.wang/api/userInfo`。这样就解决了大家老大难的跨域问题。

但是其实服务端只要设置好白名单，就不会有这样那样的跨域问题。

## resolve.alias 别名设置

这里我们必须得设置好别名，否则在页面中，你会写出很长一串类似这样的代码 `../../../`。

打开 `vite.config.js`，添加配置如下：

```js
...
import path from 'path'

export default defineConfig({
  ...
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // src 路径
      'utils': path.resolve(__dirname, 'src/utils') // src 路径
    }
  },
})
```

此时我们便可以修改之前的代码如下：

**router/index.js**

```js
import Index from '@/container/Index'
import About from '@/container/About'
```

**App.jsx**

```js
import routes from '@/router'
```

## 总结

行文至此，我们的基础开发环境已经搭建完毕，涉及构建工具、前端框架、`UI` 组件库、`HTTP` 请求库、`CSS` 预加载器、跨域代理、移动端分辨率适配，这些知识都是一个合格的前端工程师应该具备的，所以请大家加油，将他们都通通拿下。


## 14.前端实战：底部导航栏

## 前言

上一章节，我们从 0 开始搭建出一套以 `React` 技术栈为基础的前端开发环境，过程中肯定会遇到各种奇奇怪怪的问题，比如 `Node` 版本问题，工具包的版本问题，插件下载完之后，无法得到自己想要的效果等等，为了大家能顺畅地进行开发，请大家尽量将项目中用到的 `node_module` 包版本和我提供给大家的项目中的版本，保持一致。

倘若你学会了这一套搭建流程，我希望你能举一反三，根据项目需求，灵活的切换组件库、PC 版、甚至是主框架。这对提升自己的知识广度很有帮助，因为相比每次都看教程，自己手动实现一遍，印象会更深刻，遇到问题也能通过自己的认知，去解决它。

扯得有点远了，本章节我们将正式进入前端实战环节。

> 本教程已有线上地址[在线地址](http://cost.chennick.wang)，同学们可以在实战部分，对照着线上页面。

#### 知识点

- 编写底部导航栏

- 创建图标公用组件

- 路由控制底部导航栏的显隐

## 编写底部导航栏

我们先观察我们今天要实现的底部导航长啥样，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88b876655d1d4cc98bc64701893070f4~tplv-k3u1fbpfcp-zoom-1.image)

上图红框中的底部导航栏，在很多业务场景下都是需要的，三个导航栏对应着三个不同的三个页面组件，分别是「账单」、「统计」、「我的」。这三个页面组件是需要导航栏的。如果我们点击内页如账单详情页，则底部的导航栏会被隐藏，这就需要我们在导航栏的控制上，下一些功夫。

话不多说，我们在上一章的代码基础上添加导航栏组件，在 `src` 目录下新建 `components` 目录，专门用于放置一些公用组件，我们再在 `components` 目录下新建 `NavBar` 目录，用于编写底部导航栏，代码如下所示：

**Nav/index.jsx**

```js
import React, { useState } from 'react';
import PropTypes from 'prop-types'
import { TabBar } from 'zarm';
import { useNavigate } from 'react-router-dom';
import s from './style.module.less';

const NavBar = ({ showNav }) => {
  const [activeKey, setActiveKey] = useState('/');
  const navigateTo = useNavigate()

  const changeTab = (path) => {
    setActiveKey(path)
    navigateTo(path)
  }

  return (
    <TabBar visible={showNav} className={s.tab} activeKey={activeKey} onChange={changeTab}>
      <TabBar.Item
        itemKey="/"
        title="账单"
      />
      <TabBar.Item
        itemKey="/data"
        title="统计"
      />
      <TabBar.Item
        itemKey="/user"
        title="我的"
      />
    </TabBar>
  );
};

NavBar.propTypes = {
  showNav: PropTypes.bool
}

export default NavBar;
```

代码解析：

首先是声明 `NavBar` 函数组件，它接收一个外部传入的 `showNav` 属性，用于控制导航栏的显示隐藏。

通过 `useNavigate` 钩子方法，拿到路由实例 `navigateTo`，它内部含有很多路由的方法，在上述代码中，我们使用到的是 `navigateTo` 进行路由跳转。

在页面中，引入 `TabBar` 组件，它接受几个属性：

- visible：用于控制导航栏的显示隐藏。

- activeKey：当前被点击的导航栏。

- onChange：点击导航栏之后的回调方法，`path` 参数为 `TabBar.Item` 的 `itemKey` 属性。

> TabBar 官方文档：https://zarm.gitee.io/#/components/tab-bar

所以当你点击导航栏的时候，`changeTab` 方法便会被触发，执行内部的 `setActiveKey` 和 `navigateTo`，他们的作用分别是设置当前点击的高亮和让页面跳转到对应的页面组件。

说到跳转到对应的组件，'/'、'/data'、'/user' 这三个路由对应的三个组件我们还未编写，这里我们在 `container` 目录下新建这三个页面组件，作为占位。

```js
// Home/index.jsx
import React from 'react'

const Home = () => {
  return <div>首页</div>
}

export default Home

// Data/index.jsx
import React from 'react'

const Data = () => {
  return <div>数据</div>
}

export default Data

// User/index.jsx
import React from 'react'

const User = () => {
  return <div>个人中心</div>
}

export default User
```

别忘了，前往 `router/index.js` 添加路由配置，如果不添加这个配置，调用 `navigateTo` 这个方法，就无法匹配到对应的页面组件，代码如下：

```js
// router/index.js
import Home from '@/container/Home'
import Data from '@/container/Data'
import User from '@/container/User'

const routes = [
  {
    path: "/",
    component: Home
  },
  {
    path: "/data",
    component: Data
  },
  {
    path: "/user",
    component: User
  }
];

export default routes
```

这时，我们还缺少一步，将导航栏组件引入 `App.jsx` 入口页面，如下所示：

```js
// App.jsx
...
import NavBar from '@/components/NavBar';
...
function App() {
  return <Router>
    <ConfigProvider primaryColor={'#007fff'}>
      <>
       <Routes>
        {routes.map(route => <Route exact key={route.path} path={route.path} element={<route.component />} />)}
       </Routes>
      <NavBar showNav={showNav} />
     </>
    </ConfigProvider>
    <NavBar showNav={true} />
  </Router>
}
```

通过 `npm run dev` 启动项目，浏览器展示效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39ce0d3387fd41df97db10b054a6ae0a~tplv-k3u1fbpfcp-zoom-1.image)

上图效果所示，注意地址栏的变化，点击相应的 `Tab`，调用的 `navigateTo` 方法，将地址栏的 `pathname` 改变，随之而来的是页面组件的改变。这个就应证了我们第 10 章给大家解释的单页面路由控制的原理。`navigateTo` 做的事情就是改变地址栏，地址栏一旦改变，就会触发地址所对应的组件渲染，如 `/data`，渲染的就是 `Data` 页面组件。

你会问为什么导航栏会一直显示在底部，我们来分析以下代码：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13d46f4c1f214b4bae40240bccff4fbe~tplv-k3u1fbpfcp-zoom-1.image)

红色框是组件展示的区域，每个路径对应着一个组件，这个在 `router/index.js` 文件中也有所体现。

绿色框则代表导航栏的位置，也就是说，无论上面的组件怎么变化，底部的导航栏一直都是存在的。

#### 添加底部导航图标

我们将图标写成公共组件，这样便于后面各个页面方便引入，我们新建 `components/CustomIcon/index.jsx`，添加如下代码：

```js
import { Icon } from 'zarm';

export default Icon.createFromIconfont('//at.alicdn.com/t/font_2236655_w1mpqp7n1ni.js');
```

上述代码，我们引入 `Icon`，执行它的自定义图标方法 `createFromIconfont`，它接收一个参数，为 `iconfont` 生产的静态脚本路径，你可以自己去 [官网](https://www.iconfont.cn/) 配置，也可以直接用我提供的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fe4857973a74a78a2cc2d2110e49c34~tplv-k3u1fbpfcp-zoom-1.image)

这里我已经为大家添加好了各个图标，地址就是上述代码的地址。

接着我们将其引入到代码中使用，打开 `components/NavBar/index.jsx` ，添加如下属性：

```js
import CustomIcon from '../CustomIcon';
...
<TabBar.Item
  itemKey="/"
  title="账单"
  icon={<CustomIcon type="zhangdan" />}
/>
<TabBar.Item
  itemKey="/data"
  title="统计"
  icon={<CustomIcon type="tongji" />}
/>
<TabBar.Item
  itemKey="/user"
  title="我的"
  icon={<CustomIcon type="wode" />}
/>
```

查看浏览器展示效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f7b75bd787a402795887b4893924916~tplv-k3u1fbpfcp-zoom-1.image)

## 底部导航栏的显示隐藏

我们在之前引入 `NavBar` 的代码中，将 `showNav` 属性写死为 `true`。此时，我们需要将其盘活，打开 `App.jsx`，添加如下代码：

```js
import React, { useEffect, useState } from 'react'
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useLocation
} from "react-router-dom"

import NavBar from '@/components/NavBar';

import { ConfigProvider } from 'zarm'

import routes from '@/router'
function App() {
  const location = useLocation() // 拿到 location 实例
  const { pathname } = location // 获取当前路径
  const needNav = ['/', '/data', '/user'] // 需要底部导航栏的路径
  const [showNav, setShowNav] = useState(false) // 是否展示 Nav
  useEffect(() => {
    setShowNav(needNav.includes(pathname))
  }, [pathname]) // [] 内的参数若是变化，便会执行上述回调函数=
  return <Router>
    <ConfigProvider primaryColor={'#007fff'}>
      <Switch>
        {
          routes.map(route => <Route exact key={route.path} path={route.path}>
            <route.component />
          </Route>)
        }
      </Switch>
    </ConfigProvider>
    <NavBar showNav={true} />
  </Router>
}

export default App
```

当你刷新浏览器，控制台应该会报下面的错误：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3a8e99d9b4346ada136f513486912e6~tplv-k3u1fbpfcp-zoom-1.image)

执行 `useLocation` 时，报错 `location of undefined`。这是因为想要在函数组件内执行 `useLocation`，该组件必须被 `Router` 高阶组件包裹，我们做如下改动，将 `App.jsx` 的 `Router` 组件，前移到 `main.jsx` 内，如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b13889ca74b84460bb6205555cbc75fd~tplv-k3u1fbpfcp-zoom-1.image)

逻辑分析：

我们拿到 `pathname`，将其设置为 `useEffect` 钩子函数的第二个参数，监听它的变化，一旦 `pathname` 变化，便会触发回调函数执行 `setShowNav(needNav.includes(pathname))`，结果会传递给 `NavBar` 组件，从而控制组件的显示隐藏。`needNav` 为需要底部导航的路径值。

我们不妨做个测试，在 `container` 目录下新建一个测试页面组件 `Detail`，并且添加路由配置。

别忘记把组件属性修改成动态变量：

```js
<NavBar showNav={showNav} />
```

查看浏览器的展示效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c659b2430bab4985a86c2519eac7d62e~tplv-k3u1fbpfcp-zoom-1.image)

## 总结

导航栏可以用在很多地方，映射到 `PC` 网页就是左侧侧边导航，道理都是相通的。移动端放在下面控制，`PC` 端放在左边或者右边控制罢了。所以再次强调不要学完了一个知识点，就思维定势地认为只能用在某一个需求上，能做到融会贯通，才是判断一个好程序员的标准。



## 15.前端实战：登录注册页面

## 前言

上一章节我们实现了底部导航栏，并且创建了三个主页面，这三个页面是需要展示底部导航栏，而我们本章节要制作的「登录注册页面」便是不需要底部导航栏的单独页面。

> 本教程已有线上地址[在线地址](http://cost.chennick.wang)，同学们可以在实战部分，对照着线上页面进行学习。

#### 知识点

组件：`Cell`、`Input`、`Button`、`CheckBox`。

## 注册页面

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ff7150ab666463faf49a280bded1d9b~tplv-k3u1fbpfcp-zoom-1.image)

我们的系统是面向多用户的，换句话说也就是一个纯正的 C 端项目，任何人都可以通过网站，注册一个新的账号。接下来开始注册页面的编写。

首先新建 `Login` 文件夹，在文件夹内添加两个文件 `index.jsx` 和 `style.module.less`，我们先把注册页面的静态页面切出来，首先给 `index.jsx` 添加如下代码：

```js
import React from 'react'

import s from './style.module.less'

const Login = () => {
  return <div className={s.auth}>
    注册
  </div>
}

export default Login
```

为它添加一个路由配置，打开 `router/index.js` 添加如下：

```js
import Login from '@/container/Login'
...
{
  path: "/login",
  component: Login
}
```

重启项目，如下所示代表登录注册页面创建成功了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70072a5101314b52a83e7675deb6a205~tplv-k3u1fbpfcp-zoom-1.image)

接下来为 `Login/index.jsx` 添加静态页面代码：

```js
import React from 'react'
import { Cell, Input, Button, Checkbox } from 'zarm'
import CustomIcon from '@/components/CustomIcon'

import s from './style.module.less'

const Login = () => {
  return <div className={s.auth}>
    <div className={s.head} />
    <div className={s.tab}>
      <span>注册</span>
    </div>
    <div className={s.form}>
      <Cell icon={<CustomIcon type="zhanghao" />}>
        <Input
          clearable
          type="text"
          placeholder="请输入账号"
        />
      </Cell>
      <Cell icon={<CustomIcon type="mima" />}>
        <Input
          clearable
          type="password"
          placeholder="请输入密码"
        />
      </Cell>
      <Cell icon={<CustomIcon type="mima" />}>
          <Input
            clearable
            type="text"
            placeholder="请输入验证码"
          />
        </Cell>
    </div>
    <div className={s.operation}>
      <div className={s.agree}>
        <Checkbox />
        <label className="text-light">阅读并同意<a>《掘掘手札条款》</a></label>
      </div>
      <Button block theme="primary">注册</Button>
    </div>
  </div>
}

export default Login
```

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

上述代码中，关键部分是账号输入、密码输入、验证码输入，这三个输入框是需要获取数据作为接口的参数提交上去的。

很多时候，服务端没有开发好接口的时候，我们前端要做的任务就是先还原 `UI` 稿，把该切的页面都切出来，并且预留好需要给接口提交的数据交互，比如上述三个输入框。

样式编写部分，要注意的一点是 `:global` 这个关键词。由于我们采用的是 `CSS Module` 的形式进行开发，也就是你在页面中声明的类名都会根据当前页面，打一个唯一的 `hash` 值，比如我们页面中声明的 `className={s.form}`，最终在浏览器中显示的是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bab558e802d84ccd8c0b4273fe1e6174~tplv-k3u1fbpfcp-zoom-1.image)

`_form_kpur3_30` 是已经被编译过的样式，这样做的目的是避免和别的页面的样式重名，这是目前样式管理的一个诟病，当多人参与项目开发的时候，很难做到不污染全局样式名称，除非很小心的命名样式名称。

所以经过编译之后，想要修改 `.form` 下的 `.za-cell`，如下写法，将无法修改成功：

```css
.form {
  .za-cell {
    color: red;
  }
}
```

原因是，上述写法，`.za-cell` 会被编译加上 `hash`，组件库 `Zarm` 内的 `dom` 类名还是叫 `za-cell`，如上图所示。所以为了不加 `hash`，就需要这样操作：

```css
.form {
  :global {
    .za-cell {
      color: red;
    }
  }
}
```

这样 `.za-cell` 就不会被加上 `hash`，如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/580f03ce2daf4f4488edd73c9a1efae6~tplv-k3u1fbpfcp-zoom-1.image)

完成上述页面布局之后，你会看到这样一个效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2933714025354b66ac111139397aa2d0~tplv-k3u1fbpfcp-zoom-1.image)

少了一个验证码，我们使用插件 `react-captcha-code`，我们通过 `npm` 下载它：

```bash
npm i react-captcha-code -S
```

在代码中引入：

```js
...
import Captcha from "react-captcha-code"
...
<Input
  clearable
  type="text"
  placeholder="请输入验证码"
  onChange={(value) => setVerify(value)}
/>
<Captcha charNum={4} />
```

浏览器展示如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa07ed8b505a421bb3d9120ba8741cac~tplv-k3u1fbpfcp-zoom-1.image)

此时我们已经切完注册页面需要的内容。

我们给页面加上相应的逻辑，首先是账号、密码、验证码：

```js
...
const [username, setUsername] = useState(''); // 账号
const [password, setPassword] = useState(''); // 密码
const [verify, setVerify] = useState(''); // 验证码
...
<Input
  clearable
  type="text"
  placeholder="请输入账号"
  onChange={(value) => setUsername(value)}
/>
...
<Input
  clearable
  type="password"
  placeholder="请输入密码"
  onChange={(value) => setPassword(value)}
/>
...
<Input
  clearable
  type="text"
  placeholder="请输入验证码"
  onChange={(value) => setVerify(value)}
/>
```

当输入框内容修改的时候，`onChange` 会被触发，接受的回调函数参数，便是变化的输入值，此时我们将其保存在声明的变量中。

我们输入的验证码是需要和验证码图片里的验证码匹配的，所以我们还需要拿到图片里的验证码，我们作如下操作：

```js
import React, { useCallback } from 'react'
...
const [captcha, setCaptcha] = useState(''); // 验证码变化后存储值
//  验证码变化，回调方法
const handleChange = useCallback((captcha) => {
  console.log('captcha', captcha)
  setCaptcha(captcha)
}, []);
...
<Captcha charNum={4} onChange={handleChange} />
```

当验证码变化的时候，便能获取到相应的值。修改完上述代码，我们不妨测试一下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68459ab851c941ee92f3fcdaf6f758a6~tplv-k3u1fbpfcp-zoom-1.image)

到此，注册需要的参数都有了，我们开始编写注册方法：

```js
import { Cell, Input, Button, Checkbox, Toast } from 'zarm'
import { post } from '@/utils'
...
const onSubmit = async () => {
  if (!username) {
    Toast.show('请输入账号')
    return
  }
  if (!password) {
    Toast.show('请输入密码')
    return
  }
  if (!verify) {
    Toast.show('请输入验证码')
    return
  };
  if (verify != captcha) {
    Toast.show('验证码错误')
    return
  };
  try {
    const { data } = await post('/api/user/register', {
      username,
      password
    });
    Toast.show('注册成功');
  } catch (error) {
    Toast.show('系统错误');
  }
};
...
<Button onClick={onSubmit} block theme="primary">注册</Button>
```

上述代码中，因为我们使用的是 `async await` 做异步处理，所以需要通过 `try catch` 来捕获异步处理过程中出现的错误，如果使用 `Promise` 的回调函数，则无需使用 `try catch`，改动如下：

```js
post('/api/user/register', {
  username,
  password
}).then(res => {
  // do something
})
```

尝试使用之前注册过的用户名，注册一个账号：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4e36ba2f6724445a821b444dda9643f~tplv-k3u1fbpfcp-zoom-1.image)

服务端给出正确的报错，我们再用一个未注册过的用户名：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eb9d6a0ade945589835a6add7c87e99~tplv-k3u1fbpfcp-zoom-1.image)

此时我们大致将注册功能实现了。这里我不再展开讲样式部分，因为这样会使得文章中出现过多的重复代码，不以阅读，大家尽量根据标签的类名去查找 `css` 样式部分。

## 登录页面

登录页面的逻辑我们直接做到同一个页面中，通过一个 `type` 参数作为判断条件，判断当前状态是登录页面或是注册页面。

话不多说我们添加代码如下：

```js
...
import cx from 'classnames'
...

const Login = () => {
  ...
  const [type, setType] = useState('login'); // 登录注册类型

  return <div className={s.auth}>
    ...
    <div className={s.tab}>
      <span className={cx({ [s.avtive]: type == 'login' })} onClick={() => setType('login')}>登录</span>
      <span className={cx({ [s.avtive]: type == 'register' })} onClick={() => setType('register')}>注册</span>
    </div>
  </div>
  <div className={s.form}>
    ...
    {
      type == 'register' ? <Cell icon={<CustomIcon type="mima" />}>
        <Input
          clearable
          type="text"
          placeholder="请输入验证码"
          onChange={(value) => setVerify(value)}
        />
        <Captcha ref={captchaRef} charNum={4} onChange={handleChange} />
      </Cell> : null
    }
  </div>
  <div className={s.operation}>
    {
      type == 'register' ? <div className={s.agree}>
        <Checkbox />
        <label className="text-light">阅读并同意<a>《掘掘手札条款》</a></label>
      </div> : null
    }
    <Button onClick={onSubmit} block theme="primary">{type == 'login' ? '登录' : '注册'}</Button>
  </div>
}
```

> 注意，如果引入了新的工具包，请自行安装，如上述代码就需要安装 classnames。可以通过 npm i classnames -S 指令

代码分析：

上述代码中，通过 `type` 属性区分注册和登录。

首先是 `tab` 切换，通过 `classname` 来判断是否是当前高亮，用于样式控制。

其次，当 `type == 'register'` 的时候，才把验证码展示出来，因为登录这边咱们就不设置验证码，只在注册的时候显示。

最后是事件的判断，如果 `type == 'login'`，则按钮文案显示为 `登录`，否则为 `注册`。

此时点击触发的 `onSubmit` 事件也很关键，同样需要通过 `type` 判断是登录还是注册，修改代码如下：

```js
const onSubmit = async () => {
  if (!username) {
    Toast.show('请输入账号')
    return
  }
  if (!password) {
    Toast.show('请输入密码')
    return
  }
  try {
    // 判断是否是登录状态
    if (type == 'login') {
      // 执行登录接口，获取 token
      const { data } = await post('/api/user/login', {
        username,
        password
      });
      // 将 token 写入 localStorage
      localStorage.setItem('token', data.token);
    } else {
      if (!verify) {
        Toast.show('请输入验证码')
        return
      };
      if (verify != captcha) {
        Toast.show('验证码错误')
        return
      };
      const { data } = await post('/api/user/register', {
        username,
        password
      });
      Toast.show('注册成功');
      // 注册成功，自动将 tab 切换到 login 状态
      setType('login');
    }
  } catch (error) {
    Toast.show('系统错误');
  }
};
```

由于登录注册的账号和密码是同一参数，我们这边就直接复用了逻辑，并通过 `type` 判断调用哪一个接口。

重启项目，验证登录接口是否成功，如果成功则会返回 `token` 信息，如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79260001863b4fcc9f9d52522a7732fb~tplv-k3u1fbpfcp-zoom-1.image)

此时，我们本地的 `localStorage` 里，已经存下了 `token`，如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cac2dd5459b4fab8ccb7bb476719944~tplv-k3u1fbpfcp-zoom-1.image)

保存 `token` 的形式有很多，你可以引入状态管理插件来对这些数据进行存储，但是这里我们对其进行简单处理，减少项目多余的负担，保证课程的完成度。有时候，成功的将课程完成，也是一种成就感。

## 总结

到此，我们的登录注册页面算是完成了，我们拿到的 `token` 是有时效性的，我在后台设置的是 24 小时的时效，如果过期了，请求其他接口时，就会报错，从而通过逻辑判断重新回到登录页面。下一章节，我会详细分析这块内容。



## 16.前端实战：账单列表页

## 前言

上一章节介绍的登录注册是整个项目的根基，没有拿到 `token`，将无法进行后续的各种操作，如账单的增删改查。所以务必将上一章节好好地阅读与揣摩，为后面的学习做好铺垫。我们直接进入本次前端实战项目的主题，账单的增删改查之列表页。

> 本教程已有线上地址[在线地址](http://cost.chennick.wang)，同学们可以在实战部分，对照着线上页面进行学习。

#### 知识点

- 单项组件抽离

- 列表页无限滚动

- 下拉刷新列表

- 弹窗组件封装

我们先来欣赏一下最终的页面效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fc0196a649c41cb8fe73dafe50233b0~tplv-k3u1fbpfcp-zoom-1.image)

## 列表页编写（静态部分）

按照正常的开发流程，我们先将静态页面切出来，再填入数据使其动态化。在此之前，我们已经新建好了 `Home` 目录，该目录便是用于放置账单列表，所以我们直接在 `Home/index.jsx` 新增代码。

#### 头部统计实现

列表的头部展示的内容为当月的收入和支出汇总，并且有两个列表条件过滤项，分别是类型过滤和时间过滤。

我们新增代码如下：

```js
import React from 'react'
import { Icon } from 'zarm'

import s from './style.module.less'

const Home = () => {
  return <div className={s.home}>
    <div className={s.header}>
      <div className={s.dataWrap}>
        <span className={s.expense}>总支出：<b>¥ 200</b></span>
        <span className={s.income}>总收入：<b>¥ 500</b></span>
      </div>
      <div className={s.typeWrap}>
        <div className={s.left}>
          <span className={s.title}>类型 <Icon className={s.arrow} type="arrow-bottom" /></span>
        </div>
        <div className={s.right}>
          <span className={s.time}>2022-06<Icon className={s.arrow} type="arrow-bottom" /></span>
        </div>
      </div>
    </div>
  </div>
}

export default Home
```

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

代码分析：

`header` 采用 `fixed` 固定定位，将整个汇总信息固定在页面的顶部位置，这样后续列表滚动的时候，你可以方便查看当月的收入汇总，以及筛选当月消费类型和时间段的筛选。每个列表展示的是当月的收入与支出明细，比如 `2021-06` 的收入明细。

本次项目全程采用的是 `Flex` 弹性布局，这种布局形式在当下的开发生产环境已经非常成熟，同学们如果还有不熟悉的，请实现对 `Flex` 布局做一个简单的学习，这边推荐一个学习网站：

> http://flexboxfroggy.com/#zh-cn

笔者当初也是通过这个网站的学习，入门的 `Flex`。

完成上述布局之后，页面如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b4da908ba7d412ea25d6b925006f163~tplv-k3u1fbpfcp-zoom-1.image)

#### 列表页面实现

列表页面会用到 `Zarm` 组件库为我们提供的 [Pull](https://zarm.gitee.io/#/components/pull) 组件，来实现下拉刷新以及无限滚动，我们先来将基础布局实现，如下所示：

```js
// Home/index.jsx
const Home = () => {
  const [list, setList] = useState([
    {
      bills: [
        {
          amount: "25.00",
          date: "1623390740000",
          id: 911,
          pay_type: 1,
          remark: "",
          type_id: 1,
          type_name: "餐饮"
        }
      ],
      date: '2021-06-11'
    }
  ]); // 账单列表
  return <div className={s.home}>
    <div className={s.header}>
      ...
    </div>
    <div className={s.contentWrap}>
      {
        list.map((item, index) => <BillItem />)
      }
    </div>
  </div>
}
```

上述我们添加 `list` 为列表假数据，`BillItem` 组件为账单单项组件，我们将其抽离到 `components` 组件库，如下：

```js
// components/BillItem/index.jsx
import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import dayjs from 'dayjs';
import { Cell } from 'zarm';
import { useNavigate } from 'react-router-dom'
import CustomIcon from '../CustomIcon';
import { typeMap } from '@/utils';

import s from './style.module.less';

const BillItem = ({ bill }) => {
  const [income, setIncome] = useState(0); // 收入
  const [expense, setExpense] = useState(0); // 支出
  const navigateTo = useNavigate(); // 路由实例

  // 当添加账单是，bill.bills 长度变化，触发当日收支总和计算。
  useEffect(() => {
    // 初始化将传入的 bill 内的 bills 数组内数据项，过滤出支出和收入。
    // pay_type：1 为支出；2 为收入
    // 通过 reduce 累加
    const _income = bill.bills.filter(i => i.pay_type == 2).reduce((curr, item) => {
      curr += Number(item.amount);
      return curr;
    }, 0);
    setIncome(_income);
    const _expense = bill.bills.filter(i => i.pay_type == 1).reduce((curr, item) => {
      curr += Number(item.amount);
      return curr;
    }, 0);
    setExpense(_expense);
  }, [bill.bills]);

  // 前往账单详情
  const goToDetail = (item) => {
    navigateTo(`/detail?id=${item.id}`)
  };

  return <div className={s.item}>
    <div className={s.headerDate}>
      <div className={s.date}>{bill.date}</div>
      <div className={s.money}>
        <span>
          <img src="//s.yezgea02.com/1615953405599/zhi%402x.png" alt='支' />
            <span>¥{ expense.toFixed(2) }</span>
        </span>
        <span>
          <img src="//s.yezgea02.com/1615953405599/shou%402x.png" alt="收" />
          <span>¥{ income.toFixed(2) }</span>
        </span>
      </div>
    </div>
    {
      bill && bill.bills.map(item => <Cell
        className={s.bill}
        key={item.id}
        onClick={() => goToDetail(item)}
        title={
          <>
            <CustomIcon
              className={s.itemIcon}
              type={item.type_id ? typeMap[item.type_id].icon : 1}
            />
            <span>{ item.type_name }</span>
          </>
        }
        description={<span style={{ color: item.pay_type == 2 ? 'red' : '#39be77' }}>{`${item.pay_type == 1 ? '-' : '+'}${item.amount}`}</span>}
        help={<div>{dayjs(Number(item.date)).format('HH:mm')} {item.remark ? `| ${item.remark}` : ''}</div>}
      >
      </Cell>)
    }
  </div>
};

BillItem.propTypes = {
  bill: PropTypes.object
};

export default BillItem;
```

通过 `npm i dayjs -S` 添加日期操作工具，移动端建议使用 `dayjs`，因为它相比 `moment`，体积小很多。

上述代码中，`typeMap` 为我们自定义的属性，它是一个简直对，`key` 为消费类型 `icon` 的 `id`，`value` 为消费类型的 `iconfont` 的值，如下所示：

```js
// utils/index.js
...
export const typeMap = {
  1: {
    icon: 'canyin'
  },
  2: {
    icon: 'fushi'
  },
  3: {
    icon: 'jiaotong'
  },
  4: {
    icon: 'riyong'
  },
  5: {
    icon: 'gouwu'
  },
  6: {
    icon: 'xuexi'
  },
  7: {
    icon: 'yiliao'
  },
  8: {
    icon: 'lvxing'
  },
  9: {
    icon: 'renqing'
  },
  10: {
    icon: 'qita'
  },
  11: {
    icon: 'gongzi'
  },
  12: {
    icon: 'jiangjin'
  },
  13: {
    icon: 'zhuanzhang'
  },
  14: {
    icon: 'licai'
  },
  15: {
    icon: 'tuikuang'
  },
  16: {
    icon: 'qita'
  }
}
```

完成上述操作之后，我们重启浏览器，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2eb308feee24749a7ce4cd0d00a9645~tplv-k3u1fbpfcp-zoom-1.image)

样式部分大家可以根据自己的喜好进行微调，不一定要一模一样，仁者见仁。

#### 下拉刷新、上滑无限加载

我们修改 `Home/index.jsx` 如下所示：

```js
import React, { useState, useEffect } from 'react'
import { Icon, Pull } from 'zarm'
import dayjs from 'dayjs'
import BillItem from '@/components/BillItem'
import { get, REFRESH_STATE, LOAD_STATE } from '@/utils' // Pull 组件需要的一些常量

import s from './style.module.less'

const Home = () => {
  const [currentTime, setCurrentTime] = useState(dayjs().format('YYYY-MM')); // 当前筛选时间
  const [page, setPage] = useState(1); // 分页
  const [list, setList] = useState([]); // 账单列表
  const [totalPage, setTotalPage] = useState(0); // 分页总数
  const [refreshing, setRefreshing] = useState(REFRESH_STATE.normal); // 下拉刷新状态
  const [loading, setLoading] = useState(LOAD_STATE.normal); // 上拉加载状态

  useEffect(() => {
    getBillList() // 初始化
  }, [page])

  // 获取账单方法
  const getBillList = async () => {
    const { data } = await get(`/api/bill/list?page=${page}&page_size=5&date=${currentTime}`);
    // 下拉刷新，重制数据
    if (page == 1) {
      setList(data.list);
    } else {
      setList(list.concat(data.list));
    }
    setTotalPage(data.totalPage);
    // 上滑加载状态
    setLoading(LOAD_STATE.success);
    setRefreshing(REFRESH_STATE.success);
  }

  // 请求列表数据
  const refreshData = () => {
    setRefreshing(REFRESH_STATE.loading);
    if (page != 1) {
      setPage(1);
    } else {
      getBillList();
    };
  };

  const loadData = () => {
    if (page < totalPage) {
      setLoading(LOAD_STATE.loading);
      setPage(page + 1);
    }
  }

  return <div className={s.home}>
    <div className={s.header}>
      <div className={s.dataWrap}>
        <span className={s.expense}>总支出：<b>¥ 200</b></span>
        <span className={s.income}>总收入：<b>¥ 500</b></span>
      </div>
      <div className={s.typeWrap}>
        <div className={s.left}>
          <span className={s.title}>类型 <Icon className={s.arrow} type="arrow-bottom" /></span>
        </div>
        <div className={s.right}>
          <span className={s.time}>2022-06<Icon className={s.arrow} type="arrow-bottom" /></span>
        </div>
      </div>
    </div>
    <div className={s.contentWrap}>
      {
        list.length ? <Pull
          animationDuration={200}
          stayTime={400}
          refresh={{
            state: refreshing,
            handler: refreshData
          }}
          load={{
            state: loading,
            distance: 200,
            handler: loadData
          }}
        >
          {
            list.map((item, index) => <BillItem
              bill={item}
              key={index}
            />)
          }
        </Pull> : null
      }
    </div>
  </div>
}

export default Home
}
```

在 `utils/index.js` 中添加一些 `Pull` 组件需要用到的常量，如下：

```js
// utils/index.js
export const REFRESH_STATE = {
  normal: 0, // 普通
  pull: 1, // 下拉刷新（未满足刷新条件）
  drop: 2, // 释放立即刷新（满足刷新条件）
  loading: 3, // 加载中
  success: 4, // 加载成功
  failure: 5, // 加载失败
};

export const LOAD_STATE = {
  normal: 0, // 普通
  abort: 1, // 中止
  loading: 2, // 加载中
  success: 3, // 加载成功
  failure: 4, // 加载失败
  complete: 5, // 加载完成（无新数据）
};
```

代码中，已经为大家整理了详细的注释。无限滚动在移动端的应用随处可见，所以这块内容大家尽量能做到烂熟于心。如果有可能的话，希望你也能将其二次封装，便于多个地方的复用。我们打开浏览器查看效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b1408791dbd457f9a68abd898f6bb74~tplv-k3u1fbpfcp-zoom-1.image)

同学们注意一下上述动图中的细节，滑到底部的时候，有一部分内容被遮挡住了，此时我们需要添加下列样式，进行修复：

```css
.home {
  ...
  .content-wrap {
    height: calc(~"(100% - 50px)");
    overflow: hidden;
    overflow-y: scroll;
    background-color: #f5f5f5;
    padding: 10px;
    :global {
      .za-pull {
        overflow: unset;
      }
    }
  }
}
```

给 `content-wrap` 对应的标签一个高度，并且减去 `50px` 的高度，这样就不会被遮挡住下面一点的部分。

还有一个很关键的步骤，给 `src` 目录下的的 `index.css` 添加初始化高度和样式：

```css
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body, html, p {
  height: 100%;
  margin: 0;
  padding: 0;
}

* {
  box-sizing: border-box;
}

#root {
  height: 100%;
}

.text-deep {
  color: rgba(0, 0, 0, 0.9)
}

.text-light {
  color: rgba(0, 0, 0, 0.6)
}
```

至此，滚动加载基本上就完成了。

#### 添加筛选条件

最后我们需要添加两个筛选条件，类型选择和日期选择。

我们先来实现类型选择弹窗，我们采用的形式如下，底部弹出的弹窗形式，大致如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a334aa0eee1451fbb268f3b2e70a67c~tplv-k3u1fbpfcp-zoom-1.image)

想要实现上述形式，我们需要借助 `Zarm` 组件库为我们提供的 [Popup](https://zarm.gitee.io/#/components/popup) 组件，它的作用就是从不同方向弹出一个脱离文档流的弹出层。同样，我们使用组件的形式将其放置于 `components` 文件夹内实现，这样便于后续其他地方的使用。

新建 `components/PopupType`，在其内部新建 `index.jsx` 和 `style.module.less` 内容如下：

```js
// PopupType/index.jsx
import React, { forwardRef, useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import { Popup, Icon } from 'zarm'
import cx from 'classnames'
import { get } from '@/utils'

import s from './style.module.less'

// forwardRef 用于拿到父组件传入的 ref 属性，这样在父组件便能通过 ref 控制子组件。
const PopupType = forwardRef(({ onSelect }, ref) => {
  const [show, setShow] = useState(false); // 组件的显示和隐藏
  const [active, setActive] = useState('all'); // 激活的 type
  const [expense, setExpense] = useState([]); // 支出类型标签
  const [income, setIncome] = useState([]); // 收入类型标签

  useEffect(async () => {
    // 请求标签接口放在弹窗内，这个弹窗可能会被复用，所以请求如果放在外面，会造成代码冗余。
    const { data: { list } } = await get('/api/type/list')
    setExpense(list.filter(i => i.type == 1))
    setIncome(list.filter(i => i.type == 2))
  }, [])

  if (ref) {
    ref.current = {
      // 外部可以通过 ref.current.show 来控制组件的显示
      show: () => {
        setShow(true)
      },
      // 外部可以通过 ref.current.close 来控制组件的显示
      close: () => {
        setShow(false)
      }
    }
  };

  // 选择类型回调
  const choseType = (item) => {
    setActive(item.id)
    setShow(false)
    // 父组件传入的 onSelect，为了获取类型
    onSelect(item)
  };

  return <Popup
    visible={show}
    direction="bottom"
    onMaskClick={() => setShow(false)}
    destroy={false}
    mountContainer={() => document.body}
  >
    <div className={s.popupType}>
      <div className={s.header}>
        请选择类型
        <Icon type="wrong" className={s.cross} onClick={() => setShow(false)} />
      </div>
      <div className={s.content}>
        <div onClick={() => choseType({ id: 'all' })} className={cx({ [s.all]: true, [s.active]: active == 'all' })}>全部类型</div>
        <div className={s.title}>支出</div>
        <div className={s.expenseWrap}>
          {
            expense.map((item, index) => <p key={index} onClick={() => choseType(item)} className={cx({[s.active]: active == item.id})} >{ item.name }</p>)
          }
        </div>
        <div className={s.title}>收入</div>
        <div className={s.incomeWrap}>
          {
            income.map((item, index) => <p key={index} onClick={() => choseType(item)} className={cx({[s.active]: active == item.id})} >{ item.name }</p>)
          }
        </div>
      </div>
    </div>
  </Popup>
});

PopupType.propTypes = {
  onSelect: PropTypes.func
}

export default PopupType;
```

老规矩，代码逻辑注释我都写在代码中，我坚持不把注释和逻辑分开，是因为我自己在看其他教程的时候，遇到代码中没写逻辑的文章，来回看下边的注释和上边的代码，有点乱，如果同学们有疑问，可以进群截图咨询，我在群里看到的话，随时进行解答。

类型弹窗组件写完之后，我们在 `Home/index.jsx` 内尝试调用它，如下所示：

```js
...
import PopupType from '@/components/PopupType'

const Home = () => {
  const typeRef = useRef(); // 账单类型 ref
  const [currentSelect, setCurrentSelect] = useState({}); // 当前筛选类型
  ...

  useEffect(() => {
    getBillList() // 初始化
  }, [page, currentSelect])

  const getBillList = async () => {
    const { data } = await get(`/api/bill/list?page=${page}&page_size=5&date=${currentTime}&type_id=${currentSelect.id || 'all'}`);
    // 下拉刷新，重制数据
    if (page == 1) {
      setList(data.list);
    } else {
      setList(list.concat(data.list));
    }
    setTotalPage(data.totalPage);
    // 上滑加载状态
    setLoading(LOAD_STATE.success);
    setRefreshing(REFRESH_STATE.success);
  }

  ...

  // 添加账单弹窗
  const toggle = () => {
    typeRef.current && typeRef.current.show()
  };

  // 筛选类型
  const select = (item) => {
    setRefreshing(REFRESH_STATE.loading);
    // 触发刷新列表，将分页重制为 1
    setPage(1);
    setCurrentSelect(item)
  }

  return <div className={s.home}>
    <div className={s.header}>
      <div className={s.dataWrap}>
        <span className={s.expense}>总支出：<b>¥ 200</b></span>
        <span className={s.income}>总收入：<b>¥ 500</b></span>
      </div>
      <div className={s.typeWrap}>
        <div className={s.left} onClick={toggle}>
          <span className={s.title}>{ currentSelect.name || '全部类型' } <Icon className={s.arrow} type="arrow-bottom" /></span>
        </div>
        <div className={s.right}>
          <span className={s.time}>2022-06<Icon className={s.arrow} type="arrow-bottom" /></span>
        </div>
      </div>
    </div>
    <div className={s.contentWrap}>
      {
        list.length ? <Pull
          animationDuration={200}
          stayTime={400}
          refresh={{
            state: refreshing,
            handler: refreshData
          }}
          load={{
            state: loading,
            distance: 200,
            handler: loadData
          }}
        >
          {
            list.map((item, index) => <BillItem
              bill={item}
              key={index}
            />)
          }
        </Pull> : null
      }
    </div>
    <PopupType ref={typeRef} onSelect={select} />
  </div>
}
```

添加类型选择弹窗注意几个点：

1、使用 `useState` 声明好类型字段。
2、通过 `useRef` 声明的 ref 给到 `PopupType` 组件，便于控制内部的方法。
3、传递 `onSelect` 方法，获取到弹窗内部选择的类型。
4、`useEffect` 第二个参数，添加一个 `currentSelect` 以来，便于修改的时候，触发列表的重新渲染。

有一个有趣的知识点，这里和大家分享一下，你尝试去打印 `typeRef` 变量，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c7b0f79094c436d8ee0d089b35acc46~tplv-k3u1fbpfcp-zoom-1.image)

可以看到，在 `PopupType` 组件内挂载的方法，可以在父组件内获取到，那么我们便可以直接把弹窗的显示隐藏参数放在子组件内维护，而不用每次都去在父组件声明 `show` 或 `hide`。

加完类型筛选之后，我们再将时间筛选加上，同样将时间筛选添加至 `components` 目录下，便于后续数据页面的时间筛选。

```js
// PopupDate/index.jsx
import React, { forwardRef, useState } from 'react'
import PropTypes from 'prop-types'
import { Popup, DatePicker  } from 'zarm'
import dayjs from 'dayjs' 

const PopupDate = forwardRef(({ onSelect, mode = 'date' }, ref) => {
  const [show, setShow] = useState(false)
  const [now, setNow] = useState(new Date())

  const choseMonth = (item) => {
    setNow(item)
    setShow(false)
    if (mode == 'month') {
      onSelect(dayjs(item).format('YYYY-MM'))
    } else if (mode == 'date') {
      onSelect(dayjs(item).format('YYYY-MM-DD'))
    }
  }

  if (ref) {
    ref.current = {
      show: () => {
        setShow(true)
      },
      close: () => {
        setShow(false)
      }
    }
  };
  return <Popup
    visible={show}
    direction="bottom"
    onMaskClick={() => setShow(false)}
    destroy={false}
    mountContainer={() => document.body}
  >
    <div>
      <DatePicker
        visible={show}
        value={now}
        mode={mode}
        onOk={choseMonth}
        onCancel={() => setShow(false)}
      />
    </div>
  </Popup>
});

PopupDate.propTypes = {
  mode: PropTypes.string, // 日期模式
  onSelect: PropTypes.func, // 选择后的回调
}

export default PopupDate;
```

底部时间弹窗逻辑和类型选择的逻辑相似，这里不做赘述，直接在 `Home/index.jsx` 中引入时间筛选框：

```js
// Home/index.jsx 
...
import PopupDate from '@/components/PopupDate'

const Home = () => {
  ... 
  const monthRef = useRef(); // 月份筛选 ref

  useEffect(() => {
    getBillList() // 初始化
  }, [page, currentSelect, currentTime])

  ... 

  // 选择月份弹窗
  const monthToggle = () => {
    monthRef.current && monthRef.current.show()
  };

  // 筛选月份
  const selectMonth = (item) => {
    setRefreshing(REFRESH_STATE.loading);
    setPage(1);
    setCurrentTime(item)
  }

  return <div className={s.home}>
    ... 
    <div className={s.right}>
      <span className={s.time} onClick={monthToggle}>{ currentTime }<Icon className={s.arrow} type="arrow-bottom" /></span>
    </div>
    ... 

    <PopupDate ref={monthRef} mode="month" onSelect={selectMonth} />
  </div>
}
```

刷新浏览器如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847ab58538134cdcb8d819d61823a5a7~tplv-k3u1fbpfcp-zoom-1.image)

最后不要忘记计算当前月份的收入和支出汇总数据，放置于头部，修改 `Home/index.jsx` 内的代码如下：

```js
... 
const Home = () => {
  ... 
  const [totalExpense, setTotalExpense] = useState(0); // 总支出
  const [totalIncome, setTotalIncome] = useState(0); // 总收入

  const getBillList = async () => {
    const { data } = await get(`/api/bill/list?page=${page}&page_size=5&date=${currentTime}&type_id=${currentSelect.id || 'all'}`);
    // 下拉刷新，重制数据
    if (page == 1) {
      setList(data.list);
    } else {
      setList(list.concat(data.list));
    }
    setTotalExpense(data.totalExpense.toFixed(2));
    setTotalIncome(data.totalIncome.toFixed(2));
    setTotalPage(data.totalPage);
    // 上滑加载状态
    setLoading(LOAD_STATE.success);
    setRefreshing(REFRESH_STATE.success);
  }

  return <div className={s.home}>
    ... 
    <div className={s.dataWrap}>
      <span className={s.expense}>总支出：<b>¥ { totalExpense }</b></span>
      <span className={s.income}>总收入：<b>¥ { totalIncome }</b></span>
    </div>
    ...
  <div>
}
```

最终展示效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17747f5d0d7b41eabcbe47e8dc633de7~tplv-k3u1fbpfcp-zoom-1.image)

## 总结

本章节的内容，偏向实战，而实战部分代码在文章的重复率不可避免，这里大家把握好本章节两个重要知识点：

1、无限加载、下拉刷新。

2、公用组件提取，如弹窗组件、账单组件。

这两个知识点在实战中，用到的非常多，希望同学们能重视。

## 17.前端实战：新增账单弹窗封装

## 前言

回顾一下上一章节学习的内容。无限滚动列表、弹窗组件的内部控制显隐、工具方法以及常量的提取。若是你开发项目时，在潜意识里，有对这些内容进行封装的思想，那么你已经有模块化、组件化的开发理念了。在大量的工程中得出的实践，将会根深蒂固在你的开发理念里。

之前，我们是对一个小组件，如时间筛选、类型筛选等小组件进行封装。本章节，我们对一个添加模块进行封装，好处就是你在任何地方，都能使用这个添加组件，对账单进行增加操作。

我们先来看看本章节要绘制的页面和逻辑：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/349d2f897ff84498a7016596b2e11882~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示，本章节要实现的需求逻辑，基本上已经绘制在图中。所有的努力，都是为了凑出这几个参数：

- 账单类型

- 账单金额

- 账单日期

- 账单种类

- 备注

然后将这些数据，提交给服务端进行处理，然后存储到数据库，完事。

## 正文

上述需求整理清楚之后，我们开始本章节的制作环节。

#### 弹窗组件实现

先实现点击新增按钮，调出弹窗的功能。首先，在 `Home/index.jsx` 文件中添加 「新增按钮」，如下所示：

```js
import CustomIcon from '@/components/CustomIcon'
... 
const Home = () => {
  ... 
  const addToggle = () => {
    // do something
  }
  ...
  return <div className={s.home}>
    ... 
    <div className={s.add} onClick={addToggle}><CustomIcon type='tianjia' /></div>
  </div>
}
```

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

样式中，注意我给 `border` 设置的是 `1PX`，大写的单位，因为这样写的话，`postcss-pxtorem` 插件就不会将其转化为 `rem` 单位。

重启项目之后，刷新浏览器，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acf8cf59aeed4061b36a5b7359fb42b9~tplv-k3u1fbpfcp-zoom-1.image)

根据之前实现的弹窗组件，我们再实现一套类似的，在弹窗内控制弹窗组件的显示隐藏，在 `components` 下新建 `PopupAddBill` 文件夹，再新建 `index.jsx` 和 `style.module.less`，代码如下：

```js
// PopupAddBill/index.jsx
import React, { forwardRef, useEffect, useRef, useState } from 'react';
import PropTypes from 'prop-types';
import { Popup  } from 'zarm';

const PopupAddBill = forwardRef((props, ref) => {
  const [show, setShow] = useState(false) // 内部控制弹窗显示隐藏。
  // 通过 forwardRef 拿到外部传入的 ref，并添加属性，使得父组件可以通过 ref 控制子组件。
  if (ref) {
    ref.current = {
      show: () => {
        setShow(true);
      },
      close: () => {
        setShow(false);
      }
    }
  };

  return <Popup
    visible={show}
    direction="bottom"
    onMaskClick={() => setShow(false)}
    destroy={false}
    mountContainer={() => document.body}
  >
    <div style={{ height: 200, background: '#fff' }}>弹窗</div>
  </Popup>
})

export default PopupAddBill
```

写完弹窗组件，当然就得去 `Home/index.jsx` 中调用：

```js
// Home/index.jsx
import PopupAddBill from '@/components/PopupAddBill'

const Home = () => {
  ...
  const addRef = useRef(); // 添加账单 ref
  ... 
  // 添加账单弹窗
  const addToggle = () => {
    addRef.current && addRef.current.show()
  }

  return <div className={s.home}>
    ...
    <PopupAddBill ref={addRef} />
  </div>
}
```

重启浏览器，效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7025a89978114333bdf7cbdb20139482~tplv-k3u1fbpfcp-zoom-1.image)

此时我们的“地基”已经打好了，接下来我们要在这个基础上给新增账单弹窗“添砖加瓦”。

#### 账单类型和账单时间

我们先实现弹窗头部左侧的「支出」和「收入」账单类型切换功能，添加代码如下：

```js
// components/PopupAddBill/index.jsx
...
import cx from 'classnames';
import { Popup, Icon  } from 'zarm';

import s from './style.module.less';

const PopupAddBill = forwardRef((props, ref) => {
  ...
  const [payType, setPayType] = useState('expense'); // 支出或收入类型
  ...
  // 切换收入还是支出
  const changeType = (type) => {
    setPayType(type);
  };

  return <Popup
    visible={show}
    direction="bottom"
    onMaskClick={() => setShow(false)}
    destroy={false}
    mountContainer={() => document.body}
  >
    <div className={s.addWrap}>
      {/* 右上角关闭弹窗 */}
      <header className={s.header}>
        <span className={s.close} onClick={() => setShow(false)}><Icon type="wrong" /></span>
      </header>
       {/* 「收入」和「支出」类型切换 */}
      <div className={s.filter}>
        <div className={s.type}>
          <span onClick={() => changeType('expense')} className={cx({ [s.expense]: true, [s.active]: payType == 'expense' })}>支出</span>
          <span onClick={() => changeType('income')} className={cx({ [s.income]: true, [s.active]: payType == 'income' })}>收入</span>
        </div>
      </div>
    </div>
  </Popup>
})

export default PopupAddBill
```

为了减少代码的重复，上述代码只展示了需要添加的部分，尽量不让大家混淆视听。

我们定义 `expense` 为支出，`income` 为收入，代码中通过 `payType` 变量，来控制「收入」和「支出」按钮的切换。上述代码视图效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd1f72d07dff4f69af0848e8d2f0696f~tplv-k3u1fbpfcp-zoom-1.image)

接下来在类型边上添加时间筛选弹窗，此时你将体会到之前提取时间筛选组件是多么的明智。我们继续添加代码：

```js
import React, { forwardRef, useEffect, useRef, useState } from 'react';
...
import dayjs from 'dayjs';
import PopupDate from '../PopupDate'
...

const PopupAddBill = forwardRef((props, ref) => {
  ...
  const dateRef = useRef();
  const [date, setDate] = useState(new Date()); // 日期
  ...
  // 日期选择回调
  const selectDate = (val) => {
    setDate(val);
  }

  return <Popup
    visible={show}
    direction="bottom"
    onMaskClick={() => setShow(false)}
    destroy={false}
    mountContainer={() => document.body}
  >
    <div className={s.addWrap}>
       {/* 「收入」和「支出」类型切换 */}
      <div className={s.filter}>
        ...
        <div
          className={s.time}
          onClick={() => dateRef.current && dateRef.current.show()}
        >{dayjs(date).format('MM-DD')} <Icon className={s.arrow} type="arrow-bottom" /></div>
      </div>
      <PopupDate ref={dateRef} onSelect={selectDate} />
    </div>
  </Popup>
})

export default PopupAddBill
```

我们引入了公共组件 `PopupDate`，传入 `ref` 控制弹窗的显示隐藏，传入 `onSelect` 获取日期组件选择后回调的值，并通过 `setDate` 重制 `date`，触发视图的更新，我们来看浏览器展示效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee3fa326b74f41ddb0d211e886ca5ccb~tplv-k3u1fbpfcp-zoom-1.image)

我们通过上述代码，已经创造出了两个值，分别是「账单类型」和「账单日期」，还差「账单金额」
「账单种类」、「备注」。

#### 账单金额

本章开头大家也应该看到了，金额输入框是模拟的，也就是说当下面模拟数字键盘点击的时候，我们将返回的数据渲染到进入输入框的位置，下面我们先将金额输入框搭建出来，添加代码如下：

```js
<div className={s.money}>
  <span className={s.sufix}>¥</span>
  <span className={cx(s.amount, s.animation)}>10</span>
</div>
```

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15dc48f98c4f42eb9310619510603506~tplv-k3u1fbpfcp-zoom-1.image)

我们将金额动态化，引入 `Zarm` 为我们提供的模拟数字键盘组件 `Keyboard`，代码如下：

```js
...
// 监听输入框改变值
  const handleMoney = (value) => {
    value = String(value)
    // 点击是删除按钮时
    if (value == 'delete') {
      let _amount = amount.slice(0, amount.length - 1)
      setAmount(_amount)
      return
    }

    // 点击确认按钮时
    if (value == 'ok') {
      // 这里后续将处理添加账单逻辑
      return
    }

    // 当输入的值为 '.' 且 已经存在 '.'，则不让其继续字符串相加。
    if (value == '.' && amount.includes('.')) return
    // 小数点后保留两位，当超过两位时，不让其字符串继续相加。
    if (value != '.' && amount.includes('.') && amount && amount.split('.')[1].length >= 2) return
    // amount += value
    setAmount(amount + value)
  }
...

<div className={s.money}>
  <span className={s.sufix}>¥</span>
  <span className={cx(s.amount, s.animation)}>{amount}</span>
</div>
<Keyboard type="price" onKeyClick={(value) => handleMoney(value)} />
```

重启项目，浏览器展示如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fc90561f73d4b2c921864ebefc2cd2c~tplv-k3u1fbpfcp-zoom-1.image)

> 这里一个小提示，我在制作项目的过程中，发现一个 Zarm 2.9.0 版本的 bug，Keyboard 组件在点击删除按钮的时候，onKeyClick 方法会反复被执行，于是我降级为 2.8.2 版本，并且去他们的官网提了 issue。

此时「账单金额」也被安排上了。

#### 账单种类

账单种类的作用是表示该笔账单的大致用途，我们通过接口从数据库回去账单种类列表，以横向滚动的形式，展示在金额的下面，接下来我们看具体的代码实现：

```js
... 
import CustomIcon from '../CustomIcon';
import { get, typeMap } from '@/utils';

...
const [currentType, setCurrentType] = useState({}); // 当前选中账单类型
const [expense, setExpense] = useState([]); // 支出类型数组
const [income, setIncome] = useState([]); // 收入类型数组

useEffect(async () => {
  const { data: { list } } = await get('/api/type/list');
  const _expense = list.filter(i => i.type == 1); // 支出类型
  const _income = list.filter(i => i.type == 2); // 收入类型
  setExpense(_expense);
  setIncome(_income);
  setCurrentType(_expense[0]); // 新建账单，类型默认是支出类型数组的第一项
}, [])


...
<div className={s.typeWarp}>
  <div className={s.typeBody}>
    {/* 通过 payType 判断，是展示收入账单类型，还是支出账单类型 */}
    {
      (payType == 'expense' ? expense : income).map(item => <div onClick={() => setCurrentType(item)} key={item.id} className={s.typeItem}>
        {/* 收入和支出的字体颜色，以及背景颜色通过 payType 区分，并且设置高亮 */}
        <span className={cx({[s.iconfontWrap]: true, [s.expense]: payType == 'expense', [s.income]: payType == 'income', [s.active]: currentType.id == item.id})}>                
          <CustomIcon className={s.iconfont} type={typeMap[item.id].icon} />
        </span>
        <span>{item.name}</span>
      </div>)
    }
  </div>
</div>
```

注意，在 `h5` 界面实现横向滚动，和在网页端相比，多了如下属性：

```css
* {
  touch-action: pan-x;
}
```

> CSS属性 touch-action 用于设置触摸屏用户如何操纵元素的区域(例如，浏览器内置的缩放功能)。

如果不设置它，只是通过 `overflow-x: auto`，无法实现 `h5` 端的横向滚动的，并且你要在一个 `div` 容器内设置全局 `*` 为 `touch-action: pan-x;`，如果后续遇到类似的问题，大家可以参考我上述做法，这是经过实践验证过的方法。

我们来看看浏览器的展示效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9047dbf8d2d44f09ab66fce10dc1ee89~tplv-k3u1fbpfcp-zoom-1.image)

#### 备注弹窗

备注虽然不起眼，但是别小看它，它可以在账单类型不足以概括账单时，加以一定的文字描述。

我们直接将其放置于「账单种类」的下面，代码如下：

```js
...
import {  Input  } from 'zarm';

...
const [remark, setRemark] = useState(''); // 备注
const [showRemark, setShowRemark] = useState(false); // 备注输入框展示控制

... 
<div className={s.remark}>
  {
    showRemark ? <Input
      autoHeight
      showLength
      maxLength={50}
      type="text"
      rows={3}
      value={remark}
      placeholder="请输入备注信息"
      onChange={(val) => setRemark(val)}
      onBlur={() => setShowRemark(false)}
    /> : <span onClick={() => setShowRemark(true)}>{remark || '添加备注'}</span>
  }
</div>
```

**CSS 样式部分**

```css
.remark {
  padding: 0 24px;
  padding-bottom: 12px;
  color: #4b67e2;
  :global {
    .za-input--textarea {
      border: 1px solid #e9e9e9;
      padding:  10px;
    }
  }
}
```

`:global` 的使用之前已经有描述过，这里再提醒大家一句，目前项目使用的是 `css module` 的形式，所以样式名都会被打上 `hash` 值，我们需要修改没有打 `hash` 值的 `zarm` 内部样式，需要通过 `:global` 方法。

浏览器展示效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28bec13e3c9444cb8a4fd3779290193f~tplv-k3u1fbpfcp-zoom-1.image)

#### 调用上传账单接口

此时我们集齐了五大参数：

- 账单类型：payType

- 账单金额：amount

- 账单日期：date

- 账单种类：currentType

- 备注：remark

我们给 `Keyboard` 的「确定」按钮回调添加方法：

```js
import { Toast } from 'zarm';
import { post } from '@/utils';
// 监听输入框改变值
const handleMoney = (value) => {
  value = String(value)
  // 点击是删除按钮时
  if (value == 'delete') {
    let _amount = amount.slice(0, amount.length - 1)
    setAmount(_amount)
    return
  }
  // 点击确认按钮时
  if (value == 'ok') {
    addBill()
    return
  }
  // 当输入的值为 '.' 且 已经存在 '.'，则不让其继续字符串相加。
  if (value == '.' && amount.includes('.')) return
  // 小数点后保留两位，当超过两位时，不让其字符串继续相加。
  if (value != '.' && amount.includes('.') && amount && amount.split('.')[1].length >= 2) return
  // amount += value
  setAmount(amount + value)
}

// 添加账单
const addBill = async () => {
  if (!amount) {
    Toast.show('请输入具体金额')
    return
  }
  const params = {
    amount: Number(amount).toFixed(2), // 账单金额小数点后保留两位
    type_id: currentType.id, // 账单种类id
    type_name: currentType.name, // 账单种类名称
    date: dayjs(date).unix() * 1000, // 日期传时间戳
    pay_type: payType == 'expense' ? 1 : 2, // 账单类型传 1 或 2
    remark: remark || '' // 备注
  }
  const result = await post('/api/bill/add', params);
  // 重制数据
  setAmount('');
  setPayType('expense');
  setCurrentType(expense[0]);
  setDate(new Date());
  setRemark('');
  Toast.show('添加成功');
  setShow(false);
  if (props.onReload) props.onReload();
}
```

`onReload` 方法为首页账单列表传进来的函数，当添加完账单的时候，执行 `onReload` 重新获取首页列表数据。

```js
<PopupAddBill ref={addRef} onReload={refreshData} />
```

浏览器展示如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c3fd021a8f8497d8b14ff0c81a53367~tplv-k3u1fbpfcp-zoom-1.image)

如果如上图所示，恭喜你，你已经成功完成了添加账单的
工作，此时再回头甚至之前写的代码，马上改正一些变量及一些方法的命名，规范化一下代码。

千万别在后面再去完善，因为很大程度上，到后面你会懒得翻前面写的代码，除非实在是逻辑问题导致的 bug。

## 总结

本章节的内容也是非常丰富，我们的所有的努力，就是为了集齐「添加账单」所需要的五大参数。这是很多需求的一个索引，试问前端在调用接口的过程中，不都是做各种努力为了凑齐那几个参数呢？过程很重要，只要流程做得完善，结果自然水到渠成。




## 18.前端实战：账单详情页

## 前言

账单模块还剩最后一个小节，账单详情。账单详情页要做的事情有两个，一个是编辑当前账单操作，另一个是删除当前账单操作，我们先来观察完成后页面结构，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd8a2c4723fb4bbdbde0695d55e6bd92~tplv-k3u1fbpfcp-zoom-1.image)

这里是第一次涉及内页，所以我们需要制作一个公用的头部 `Header`，支持传参接收 `title` 信息。我们在上一章节提取的「添加账单弹窗组件」，在这里派上了用场，新增和编辑是一家，唯一的差别就是编辑的时候，需要传入当前账单的 `id` 给「添加账单组件」，组件内通过账单详情接口，获取账单详情，并将获取的参数用于各个字段初始化值，这就实现了组件的复用。

#### 知识点

- 封装公用头部组件

- 复用添加账单弹窗组件

## 正文开始

#### 公用头部

在 `components` 目录下新建 `Header` 目录，老规矩，添加两个文件 `index.jsx` 和 `style.module.less`。

为 `Header/index.jsx` 添加代码如下：

```js
import React from 'react';
import PropTypes from 'prop-types';
import { useNavigate } from 'react-router-dom'
import { NavBar, Icon } from 'zarm';

import s from './style.module.less'

const Header = ({ title = '' }) => {
  const navigateTo = useNavigate()
  return <div className={s.headerWarp}>
    <div className={s.block}>
      <NavBar
        className={s.header}
        left={<Icon type="arrow-left" theme="primary" onClick={() => navigateTo(-1)} />}
        title={title}
      />
    </div>
  </div>
};

Header.propTypes = {
  title: PropTypes.string, // 标题
};

export default Header;
```

我们采用 `Zarm` 组件库为我们提供的 `NavBar` 组件，实现头部的组件布局。为左边的返回箭头添加一个事件，`navigateTo(-1)` 的作用是路由返回事件，它不会触发浏览器的刷新，而是改变浏览器的地址栏，让组件匹配地址栏对应的地址组件。

还有一点要提醒大家，写公用组件一定要写 `PropTypes`，这是让其他使用该组件的同事知道，你这个组件接受的参数有哪些，以及每个参数的作用是什么，都要注释清楚，这才是一个好的公用组件。我见过很多同事写公用组件都不写 `PropTypes`，这让使用者非常头大。

**CSS 样式代码**

```css
.header-warp {
  border-bottom: 1px solid #e9e9e9;
  .block {
    width: 100%;
    height: 46px;
    :global {
      .za-nav-bar__title {
        font-size: 14px;
        color: rgba(0, 0, 0, 0.9);
      }
      .za-icon--arrow-left {
        font-size: 20px;
      }
    }
  }
  .header {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    .more {
      font-size: 20px;
    }
  }
}
```

完成上述代码之后，我们需要在 `container/Detail/index.jsx` 下引入这个公用头部，代码如下：

```js
import React from 'react';
import Header from '@/components/Header';

import s from './style.module.less';

const Detail = () => {
  return <div className={s.detail}>
    <Header title='账单详情' />
  </div>
}

export default Detail
```

效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4711827eba5141a2822bbde2237032d9~tplv-k3u1fbpfcp-zoom-1.image)

#### 账单明细

接下来，我们通过列表页传入的浏览器查询字符串，通俗的将就是浏览器地址栏上的参数，来获取该笔账单的详情，如下所示：

```js
// container/Detail/index.jsx
import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import qs from 'query-string';
import Header from '@/components/Header';
import { get } from '@/utils';

import s from './style.module.less';

const Detail = () => {
  const location = useLocation(); // 获取 locaton 实例，我们可以通过打印查看内部都有些什么内容。
  const { id } = qs.parse(location.search);

  const [detail, setDetail] = useState({});

  console.log('location', location);

  useEffect(() => {
    getDetail()
  }, []);

  const getDetail = async () => {
    const { data } = await get(`/api/bill/detail?id=${id}`);
    setDetail(data);
  }
  return <div className={s.detail}>
    <Header title='账单详情' />
  </div>
}

export default Detail
```

我们先来看看，浏览器控制台打印出的 `location` 如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ec916d9afd2477680bd98f0ac24a052~tplv-k3u1fbpfcp-zoom-1.image)

可以看到，我们想要的参数在 `search` 属性中，我想把 `?id=917` 转换成 `json` 键值对的形式，如：

```json
{
  id: 917
}
```

所以我通过 `npm install query-string` 引入了查询字符串解析的一个插件，通过如下方式：

```js
qs.parse(location.search)
```

可以将浏览器查询参数变成一个对象形式，所以我们在代码中可以通过 `const` 的解构，将 `id` 取出。最后通过 `get` 方法请求详情接口：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa5910c717994f729e744328c2cf2517~tplv-k3u1fbpfcp-zoom-1.image)

接下来，我们给账单明细部分布局，并且将数据接入，代码如下所示：

```js
import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import qs from 'query-string';
import dayjs from 'dayjs';
import cx from 'classnames';
import Header from '@/components/Header';
import CustomIcon from '@/components/CustomIcon';
import { get, typeMap } from '@/utils';


import s from './style.module.less';

const Detail = () => {
  const location = useLocation(); // 路由 location 实例
  const { id } = qs.parse(location.search); // 查询字符串反序列化

  const [detail, setDetail] = useState({}); // 订单详情数据

  useEffect(() => {
    getDetail()
  }, []);

  const getDetail = async () => {
    const { data } = await get(`/api/bill/detail?id=${id}`);
    setDetail(data);
  }
  return <div className={s.detail}>
    <Header title='账单详情' />
    <div className={s.card}>
      <div className={s.type}>
        {/* 通过 pay_type 属性，判断是收入或指出，给出不同的颜色*/}
        <span className={cx({ [s.expense]: detail.pay_type == 1, [s.income]: detail.pay_type == 2 })}>
          {/* typeMap 是我们事先约定好的 icon 列表 */}
          <CustomIcon className={s.iconfont} type={detail.type_id ? typeMap[detail.type_id].icon : 1} />
        </span>
        <span>{ detail.type_name || '' }</span>
      </div>
      {
        detail.pay_type == 1
          ? <div className={cx(s.amount, s.expense)}>-{ detail.amount }</div>
          : <div className={cx(s.amount, s.incom)}>+{ detail.amount }</div>
      }
      <div className={s.info}>
        <div className={s.time}>
          <span>记录时间</span>
          <span>{dayjs(Number(detail.date)).format('YYYY-MM-DD HH:mm')}</span>
        </div>
        <div className={s.remark}>
          <span>备注</span>
          <span>{ detail.remark || '-' }</span>
        </div>
      </div>
      <div className={s.operation}>
        <span><CustomIcon type='shanchu' />删除</span>
        <span><CustomIcon type='tianjia' />编辑</span>
      </div>
    </div>
  </div>
}

export default Detail
```

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

布局部分我都已经在代码中给了注释，还有不明白的同学可以在群里提问，再次强调一点，`flex` 布局请务必要掌握熟练，在日后的开发过程中，无论是小册还是公司的项目，都会大量的运用到它。甚至 `Flutter` 的布局也借鉴了 `flex` 的原理。

浏览器展示效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ccc8d4d2fb343878c22bb37f3949673~tplv-k3u1fbpfcp-zoom-1.image)

我们还需为底部的两个按钮添加事件。首先，为删除按钮添加删除事件：

```js
import { useLocation, useNavigate } from 'react-router-dom';
import { get, post, typeMap } from '@/utils';
import { Modal, Toast } from 'zarm';
... 

const navigateTo = useNavigate();

// 删除方法
const deleteDetail = () => {
  Modal.confirm({
    title: '删除',
    content: '确认删除账单？',
    onOk: async () => {
      const { data } = await post('/api/bill/delete', { id })
      Toast.show('删除成功')
      navigateTo(-1)
    },
  });
}
```

这里我们利用 `Zarm` 组件提供的 `Modal` 组件，该组件提供了调用方法的形式唤起弹窗，我们利用这个属性
为「删除」加一个二次确认的形式，避免误触按钮。

效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7f1edbbe9d147e39ffd28d9b0a0ab1c~tplv-k3u1fbpfcp-zoom-1.image)

最麻烦的编辑事件处理，我们先来明确一下思路。在点击「编辑」按钮之后，我们会唤起之前写好的「添加账单天窗」，然后将账单 `detail` 参数通过 `props` 传递给弹窗组件，组件在接收到 `detail` 时，将信息初始化给弹窗给的相应参数。

我们来看代码的实现，首先在 `Detail/index.jsx` 内添加代码：

```js
import React, { useEffect, useState, useRef } from 'react';
import PopupAddBill from '@/components/PopupAddBill';
...

const editRef = useRef();
...
<div className={s.operation}>
  <span onClick={deleteDetail}><CustomIcon type='shanchu' />删除</span>
  <span onClick={() => editRef.current && editRef.current.show()}><CustomIcon type='tianjia' />编辑</span>
</div>
...
<PopupAddBill ref={editRef} detail={detail} onReload={getDetail} />
```

尝试点击编辑按钮：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e946a44ae224128ae356abc36d990eb~tplv-k3u1fbpfcp-zoom-1.image)

紧接着，我们修改 `PopupAddBill` 组件，如下所示：

```js
const PopupAddBill = forwardRef(({ detail = {}, onReload }, ref) => {
  ...
  const id = detail && detail.id // 外部传进来的账单详情 id

  useEffect(() => {
    if (detail.id) {
      setPayType(detail.pay_type == 1 ? 'expense' : 'income')
      setCurrentType({
        id: detail.type_id,
        name: detail.type_name
      })
      setRemark(detail.remark)
      setAmount(detail.amount)
      setDate(dayjs(Number(detail.date)).$d)
    }
  }, [detail])

  ... 

  useEffect(async () => {
    const { data: { list } } = await get('/api/type/list');
    const _expense = list.filter(i => i.type == 1); // 支出类型
    const _income = list.filter(i => i.type == 2); // 收入类型
    setExpense(_expense);
    setIncome(_income);
      // 没有 id 的情况下，说明是新建账单。
    if (!id) {
      setCurrentType(_expense[0]);
    };
  }, []);

  ... 
  
  // 添加账单
  const addBill = async () => {
    if (!amount) {
      Toast.show('请输入具体金额')
      return
    }
    const params = {
      amount: Number(amount).toFixed(2),
      type_id: currentType.id,
      type_name: currentType.name,
      date: dayjs(date).unix() * 1000,
      pay_type: payType == 'expense' ? 1 : 2,
      remark: remark || ''
    }
    if (id) {
      params.id = id;
      // 如果有 id 需要调用详情更新接口
      const result = await post('/api/bill/update', params);
      Toast.show('修改成功');
    } else {
      const result = await post('/api/bill/add', params);
      setAmount('');
      setPayType('expense');
      setCurrentType(expense[0]);
      setDate(new Date());
      setRemark('');
      Toast.show('添加成功');
    }
    setShow(false);
    if (onReload) onReload();
  }
})
```

首先，通过 `setXXX` 将 `detail` 的数据依次设置初始值；其次，账单种类需要判断是否是编辑或是新建；最后，修改添加账单按钮，如果是「编辑」操作，给 `params` 参数添加一个 `id`，并且调用的接口变成 `/api/bill/update`。

完成上述操作之后，我们查看浏览器操作情况如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c97d70e0092747cb8c78da25cf17c576~tplv-k3u1fbpfcp-zoom-1.image)

## 总结

本小节我们学习了如何封装内页的头部组件，以及如何将之前的「新增」复用给「编辑」操作，可以以这个为一个思考点，用发散的思维去复制这样的模式，是否其他的新增和编辑操作，也可以这么实现。

#### 本章节源码

[点击下载](https://s.yezgea02.com/1624515959785/react-vite-h5.zip)



## 19.前端实战：账单数据统计页

## 前言

账单的操作部分在之前的章节已经结束了，本章节我们学习如何将账单列表，以可视化数据的新形势展示，本章节我们会通过 `Echart` 插件，对数据进行可视化展示。

页面布局和分析如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af9e832e388940eeade66dcf304a4eeb~tplv-k3u1fbpfcp-zoom-1.image)

#### 知识点

- Echart 引入和使用。

- 进度条组件 `Progress` 的使用。

## 正文

#### 头部筛选和数据实现

当你看到顶部的时间筛选项的时候，你会再一次体会到当初把时间筛选功能封装成公用组件的好处，于是我们打开 `Data/index.jsx`，添加如下代码：

```js
import React, { useEffect, useRef, useState } from 'react';
import { Icon, Progress } from 'zarm';
import cx from 'classnames';
import dayjs from 'dayjs';
import { get, typeMap } from '@/utils'
import CustomIcon from '@/components/CustomIcon'
import PopupDate from '@/components/PopupDate'
import s from './style.module.less';

const Data = () => {
  return <div className={s.data}>
    <div className={s.total}>
      <div className={s.time}>
        <span>2021-06</span>
        <Icon className={s.date} type="date" />
      </div>
      <div className={s.title}>共支出</div>
      <div className={s.expense}>¥1000</div>
      <div className={s.income}>共收入¥200</div>
    </div>
  </div>
}

export default Data
```

头部的一些引入是为后面的代码所用，在这里事先引入，避免后面重复出现。

上述代码为头部统计的页面布局，同样采用的 `flex` 布局，样式部分如下：

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

样式部分有一个小技巧需要注意，日期后面的小竖线，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c98a98ee5aee44af8f5361ce8f144eda~tplv-k3u1fbpfcp-zoom-1.image)

在业务中，类似这样的需求非常多，这里我们可以使用伪类 `::before` 或 `::after` 去实现，减少在页面中再添加一些多余的标签。上述代码实现的逻辑是在日期的 `span` 上加上 `::after`，如下所示：

```css
span:nth-of-type(1)::after {
  content: '';
  position: absolute;
  top: 9px;
  bottom: 8px;
  right: 28px;
  width: 1px;
  background-color: rgba(0, 0, 0, .5);
}
```

给一个空的 `content`，再给上 `1px` 的宽度，颜色和上下距离可以根据需求调整。

苦口婆心的我再次强调，`flex` 布局的重要性，一定要把它吃透，至少在布局的时候，你可以灵活的运用横竖布局。

点击如期按钮，弹出底部弹窗，这里使用到了之前写好的 `PopupDate` 组件，代码如下：

```js
const Data = () => {
  const monthRef = useRef();
  const [currentMonth, setCurrentMonth] = useState(dayjs().format('YYYY-MM'));

  // 月份弹窗开关
  const monthShow = () => {
    monthRef.current && monthRef.current.show();
  };

  const selectMonth = (item) => {
    setCurrentMonth(item);
  };

  return <div className={s.data}>
    <div className={s.total}>
      <div className={s.time} onClick={monthShow}>
        <span>{currentMonth}</span>
        <Icon className={s.date} type="date" />
      </div>
      <div className={s.title}>共支出</div>
      <div className={s.expense}>¥1000</div>
      <div className={s.income}>共收入¥200</div>
    </div>
    <PopupDate ref={monthRef} mode="month" onSelect={selectMonth} />
  </div>
}
```

给日期按钮添加 `monthShow` 点击事件，调出 `PopupDate` 弹窗。并且，通过 `selectMonth` 方法，设置好选择的月份，展示于页面之上。效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34f85185a5934aaba55e13a58d3bdfdd~tplv-k3u1fbpfcp-zoom-1.image)

#### 账单单项排名制作

我们将账单排名部分的结构搭建出来，通过请求数据接口，将数据展示在页面上，代码如下：

```js
const Data = () => {
  ... 
  const [totalType, setTotalType] = useState('expense'); // 收入或支出类型
  const [totalExpense, setTotalExpense] = useState(0); // 总支出
  const [totalIncome, setTotalIncome] = useState(0); // 总收入
  const [expenseData, setExpenseData] = useState([]); // 支出数据
  const [incomeData, setIncomeData] = useState([]); // 收入数据

  useEffect(() => {
    getData()
  }, [currentMonth]);

  // 获取数据详情
  const getData = async () => {
    const { data } = await get(`/api/bill/data?date=${currentMonth}`);

    // 总收支
    setTotalExpense(data.total_expense);
    setTotalIncome(data.total_income);

    // 过滤支出和收入
    const expense_data = data.total_data.filter(item => item.pay_type == 1).sort((a, b) => b.number - a.number); // 过滤出账单类型为支出的项
    const income_data = data.total_data.filter(item => item.pay_type == 2).sort((a, b) => b.number - a.number); // 过滤出账单类型为收入的项
    setExpenseData(expense_data);
    setIncomeData(income_data);
  };

  return <div className={s.data}>
    ...
    <div className={s.structure}>
      <div className={s.head}>
        <span className={s.title}>收支构成</span>
        <div className={s.tab}>
          <span onClick={() => changeTotalType('expense')} className={cx({ [s.expense]: true, [s.active]: totalType == 'expense' })}>支出</span>
          <span onClick={() => changeTotalType('income')} className={cx({ [s.income]: true, [s.active]: totalType == 'income' })}>收入</span>
        </div>
      </div>
      <div className={s.content}>
        {
          (totalType == 'expense' ? expenseData : incomeData).map(item => <div key={item.type_id} className={s.item}>
            <div className={s.left}>
              <div className={s.type}>
                <span className={cx({ [s.expense]: totalType == 'expense', [s.income]: totalType == 'income' })}>
                  <CustomIcon
                    type={item.type_id ? typeMap[item.type_id].icon : 1}
                  />
                </span>
                <span className={s.name}>{ item.type_name }</span>
              </div>
              <div className={s.progress}>¥{ Number(item.number).toFixed(2) || 0 }</div>
            </div>
            <div className={s.right}>
              <div className={s.percent}>
                <Progress
                  shape="line"
                  percent={Number((item.number / Number(totalType == 'expense' ? totalExpense : totalIncome)) * 100).toFixed(2)}
                  theme='primary'
                />
              </div>
            </div>
          </div>)
        }
      </div>
    </div>
    ...
  </div>
}
```

上述是账单排名部分的代码部分，通过 `getData` 方法获取账单数据，接口字段分析：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/139ab1e147bb4fd2a30d543b7e445b82~tplv-k3u1fbpfcp-zoom-1.image)

首先我们需要传递日期参数 `date`，才能正常获取该月份的数据。

- number: 账单金额。

- pay_type：账单类型，1 为支出，2为收入。

- type_id：账单种类 id。

- type_name：账单种类名称，如购物、交通、医疗等。

并将数据进行二次处理，将「收入」和「支出」分成两个数组保存。

通过 `changeTotalType` 方法，切换展示「收入」或「支出」。

通过对 `Progress` 组件的样式二次修改，样式代码如下：

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

将组件展示效果改成如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d660fe020efb419394c6951253775124~tplv-k3u1fbpfcp-zoom-1.image)

#### 饼图制作

接下来我们尝试引入 `Echart`，我们不通过 `npm` 引入它，我们尝试引入它的静态资源，找到根目录下的 `index.html`，添加如下代码：

```js
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" sizes="32x32" href="https://p1-jj.byteimg.com/tos-cn-i-t2oaga2asx/gold-assets/favicons/v2/favicon-32x32.png~tplv-t2oaga2asx-image.image">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>掘掘手札</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="//s.yezgea02.com/1609305532675/echarts.js"></script>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

这种引入方式，不会将 `echart` 打包到最终的入口脚本里。有同学会说可以按需引入，但是就算是按需引入，脚本也会变得很大，本身 `echart` 这类可视化工具库就非常大，因为内部使用了大量绘制图形的代码。

完成上述操作之后，我们尝试在 `/Data/index.jsx` 添加如下代码：

```js
let proportionChart = null; // 用于存放 echart 初始化返回的实例

const Data = () => {
  ... 
  const [pieType, setPieType] = useState('expense'); // 饼图的「收入」和「支出」控制
  
  useEffect(() => {
    getData();
    return () => {
      // 每次组件卸载的时候，需要释放图表实例。clear 只是将其清空不会释放。
      proportionChart.dispose();
    };
  }, [currentMonth]);

  // 绘制饼图方法
  const setPieChart = (data) => {
    if (window.echarts) {
      // 初始化饼图，返回实例。
      proportionChart = echarts.init(document.getElementById('proportion'));
      proportionChart.setOption({
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          // 图例
          legend: {
              data: data.map(item => item.type_name)
          },
          series: [
            {
              name: '支出',
              type: 'pie',
              radius: '55%',
              data: data.map(item => {
                return {
                  value: item.number,
                  name: item.type_name
                }
              }),
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
      })
    };
  };

  // 获取数据详情
  const getData = async () => {
    // ...
    // 绘制饼图
    setPieChart(pieType == 'expense' ? expense_data : income_data);
  };

  // 切换饼图收支类型
  const changePieType = (type) => {
    setPieType(type);
    // 重绘饼图
    setPieChart(type == 'expense' ? expenseData : incomeData);
  }

  return <div className={s.data}>
    ... 
    <div className={s.structure}>
      <div className={s.proportion}>
        <div className={s.head}>
          <span className={s.title}>收支构成</span>
          <div className={s.tab}>
            <span onClick={() => changePieType('expense')} className={cx({ [s.expense]: true, [s.active]: pieType == 'expense'  })}>支出</span>
            <span onClick={() => changePieType('income')} className={cx({ [s.income]: true, [s.active]: pieType == 'income'  })}>收入</span>
          </div>
        </div>
        {/* 这是用于放置饼图的 DOM 节点 */}
        <div id="proportion"></div>
      </div>
    </div>
  </div>
}
```

切换饼图「收入」和「支出」这里，我使用了一个小技巧，每次调用 `setPieChart` 的时候，会将数据重新传入，此时的数据是经过 `changePieType` 接收的参数进行筛选的，如果形参 `type` 的值为 `expense`，那么给 `setPieChart` 传的参数为 `expenseData`，反之则为 `incomeData`。

注意，在页面销毁前，需要将实例清除。在 `useEffect` 内 `return` 一个函数，该函数就是在组件销毁时执行，在函数内部执行 `proportionChart.dispose();` 对实例进行销毁操作。

最后，我们将头部的数据补上，如下所示：

```html
<div className={s.expense}>¥{ totalExpense }</div>
<div className={s.income}>共收入¥{ totalIncome }</div>
```

浏览器展示如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1509f4c80c0429ebcd09d5c91144631~tplv-k3u1fbpfcp-zoom-1.image)

## 总结

可视化的形式还有很多，相关的可视化库有 three.js、d3.js、highchart.js等等，这些内容都值得你去深入，但是在此之前，希望同学们能明确自己希望深入那一方面的知识，进行深度学习。比如张鑫旭大神，对 `CSS` 的研究，入骨三分，我相信业务无人出其右。所以找准方向，往前冲。



## 2.后端预备：Egg.js 基础入门及项目初始化介绍

## Egg.js 简介

纯讲理论知识大家可能会觉得很枯燥乏味，所以我个人习惯采用代码结合理论的形式为大家阐述 `Egg` 的一些关键知识点。

> Egg 的环境要求：Node >= 8.x，npm >= 6.1.0。
我当前的环境：Node 12.6.0，npm 6.9.0。

这里我们使用 `Egg` 为我们提供的脚手架生成指令，几行代码就能初始化一个 `Egg` 项目，如下：

```bash
$ mkdir egg-example && cd egg-example
$ npm init egg --type=simple
$ npm i
```

成功后，用你自己喜欢的编辑器打开项目目录，我个人使用的是 `VSCode`，代码如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2409e151eda34a98ba866bf036b2ee63~tplv-k3u1fbpfcp-zoom-1.image)

#### 目录结构

`Egg` 作为一套解决方案，它内部高度集成了封装好的项目目录结构，现代开发俗称“约定式开发”。正常情况下，你从 0 开始搭建一个 `Node` 服务端代码，需要结合很多工具插件来辅助完成项目的搭建，而 `Egg` 则提前为你提供好了这些繁琐的初始工作，让你能专心与业务层面的开发。

当然，“约定式开发”也有不好的地方，很多配置项都是内部约定好的，在你想要用到某一个功能时，你可能需要去查阅 `Egg` 的官方文档是如何配置的，这就会消耗一点时间，但是相比之下，使用它的利大于弊。

下面我们就先来认识一下，`Egg` 都为我们提供了哪些文件：

**app/router.js**

用于配置 URL 路由规则，比如上述初始化代码中的 `get` 请求，`npm run dev` 启动项目之后，你可以直接在浏览器中访问启动的`端口 + 路径`，默认是 `http://localhost:7001/`，你将会拿到 `app/controller` 文件夹下，`home.js` 脚本中 `index` 方法返回的内容。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46efe79a3b94486f96ca2e6a9fd8d1b0~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea6a54c37da9461ab8a45a1614177c86~tplv-k3u1fbpfcp-zoom-1.image)

这就是路由配置的作用，当然，抛出的形式有多种，如`router.get`、`router.post`、`router.delete`、`router.put` 等，都是支持的，更加具体的内容可阅读 [Router 配置](https://eggjs.org/zh-cn/basics/router.html)。

**app/controller/xx**

用于解析用户的输入，处理后返回相应的结果。上述我们也提到了，通过请求路径将用户的请求基于 `method` 和 `URL` 分发到对应的 `Controller` 上，而 `Controller` 要做的事情就是响应用户的诉求。举个例子，我想拿到 A 用户的个人信息，于是我们要在控制器（Controller）里，通过请求携带的 A 用户的 id 参数，从数据库里获取指定用户的个人信息。我画了一个简易流程图如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a6e2954b379440d87573dbe452e5cc2~tplv-k3u1fbpfcp-zoom-1.image)

上述是一个 `get` 接口，浏览器地址栏直接请求便可，通过 `/user` 路径，找到对应的控制器，这里需要提前定义好 `/user` 对应的控制器。控制器需要做的就是处理数据和响应请求返回数据。更加详细的描述请移步至 [Controller 文档](https://eggjs.org/zh-cn/basics/controller.html)

**app/service/xx**

简单来说，`Service` 就是在复杂业务场景下用于做业务逻辑封装的一个抽象层。上述初始化项目中未声明 `service` 文件夹，它是可选项，但是官方建议我们操作业务逻辑最好做一层封装。我们换一种理解方式，`Service` 层就是用于数据库的查询，我们尽量将粒度细化，这样以便多个 `Controller` 共同调用同一个 `Service`。后续我们链接数据库操作的时候，再进行详细分析。更加详细的描述请移步至 [Service 文档](https://eggjs.org/zh-cn/basics/service.html)。

**app/middleware/xx**

用于编写中间件，中间件的概念就是在路由配置里设置了中间件的路由，每次请求命中后，都要过一层中间件。在我们后续的开发中，也会利用到这个中间件的原理做用户鉴权。当用户未登录的情况下，是不能调用某些接口的。

当然，你可以每次都在 `Controller` 判断，当前请求是否携带有效的用户认证信息。接口一多，到处都是这样的判断，逻辑重复。所以，中间件在某种程度上，也算是优化代码结构的一种方式。更加详细的描述请移步至 [Middleware 文档](https://eggjs.org/zh-cn/basics/middleware.html)。

**app/public/xx**

用于放置静态资源。后续我们将会有一个上传静态资源的接口，包括图片、文本文档、excel、word等，都可以通过服务端读取文件之后，将其写入 `app/public` 文件夹中。在目前没有 `OSS` 服务的情况下，姑且先用这种方式存储静态资源，会消耗一点服务器的内存。

**config/config.{env}.js**

用于编写配置文件。目前本小册项目只配置了 `config/config.default.js` 文件，这个是 `Egg` 框架约定好的，你可以在内部设置一些全局的配置常量，在任何地方都可以通过 `app.config` 获取到 `config.default.js` 文件内的配置项。

**config/plugin.js**

用于配置需要加载的插件。比如 `egg-mysql`、`egg-cors`、`egg-jwt` 等官方提供的插件，你也可以自己编写 `Egg` 插件，社区很多优秀的插件都可以在 `Github` 中搜到，[点击前往](https://github.com/topics/egg-plugin)。

上述目录内容都是我们后续开发会使用到的，同学们做一个基本的了解，做到心中有数便可，后续实战开发部分具体使用到的时候，会结合实践进行分析讲解。

## 编写基础的 GET 和 POST 接口

“冰冻三尺，非一日之寒”，一上手就写稍复杂的项目需求，是不现实的。我们先上手一些简单的知识点，以此来熟悉如何使用 `Egg`，为后续的实战部分作准备。

#### GET 请求参数获取

我们打开之前初始化的 `egg-example` 项目，通过 `npm run dev` 启动项目之后，浏览器添加如下请求地址：

```js
http://localhost:7001/?id=潘嘎之交
```

打开 `app/controller/home.js`，通过如下形式获取到浏览器查询参数。

```js
'use strict';

const Controller = require('egg').Controller;

class HomeController extends Controller {
  async index() {
    const { ctx } = this;
    const { id } = ctx.query;
    ctx.body = id;
  }
}

module.exports = HomeController;
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffa2064f409046f581a6c6c3d8d0c4b9~tplv-k3u1fbpfcp-zoom-1.image)

还有另一种获取申明参数，比如我希望通过这样一个地址获取用户参数 `/user/5`，想获取用户 `id` 为 `5` 的用户信息。我们可以这样操作，首先添加路由，打开 `app/router.js` 添加一个路由：

```js
'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.get('/', controller.home.index);
  router.get('/user/:id', controller.home.user);
};
```

其次在 `app/controller/home.js` 下添加一个 `user` 方法如下：

```js
'use strict';

const Controller = require('egg').Controller;

class HomeController extends Controller {
  async index() {
    const { ctx } = this;
    const { id } = ctx.query;
    ctx.body = id;
  }
  // 获取用户信息
  async user() {
    const { ctx } = this;
    const { id } = ctx.params; // 通过 params 获取申明参数
    ctx.body = id;
  }
}
module.exports = HomeController;
```

我们通过如下请求获取参数，打印在网页上：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46e43a34238741daa295395de9901c05~tplv-k3u1fbpfcp-zoom-1.image)

通过上述操作，大家可以想到，其实用 `GET` 接口，就能把一切都做了，包括 `POST` 能做的，`GET` 也是可以轻松应对，只不过我们为了数据安全以及大小的限制，有些请求还是需要用 `POST` 来完成。所以市面上的面试题有关于 `GET` 和 `POST` 请求的区别，其实都是表象上的区别，而内在都是基于 TCP 协议，从理论上讲，可以说它们没差。

#### POST 请求参数获取

`POST` 接口需要借助 `Postman` 工具进行请求，因为通过浏览器无法手动发起 `POST` 请求，只能通过浏览器地址栏发起 `GET` 请求。所以这里大家可以去搜索引擎自行下载安装。我们来编写一个 `POST` 请求：

```js
// app/router.js
// ...
router.post('/add', controller.home.add);
```

```js
// app/controller/home.js
// post 请求方法
async add() {
  const { ctx } = this;
  const { title } = ctx.request.body;
  // Egg 框架内置了 bodyParser 中间件来对 POST 请求 body 解析成 object 挂载到 ctx.request.body 上
  ctx.body = {
    title
  };
}
```

我们打开 `Postman` 设置如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99c5d09b292e479594a8add539942dd2~tplv-k3u1fbpfcp-zoom-1.image)

点击 「Send」按钮之后，控制台报错如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5da75d9d04be4e3e8bb060a1f070bd1e~tplv-k3u1fbpfcp-zoom-1.image)

注意关键字「安全威胁 csrf 的防范」，简单说就是网络请求的安防策略，比如你 `Egg` 启动的是本地地址 `http://127.0.0.1:7001` ，但是你请求的 `POST` 或 `GET` 接口是非本地计算机（别人的电脑），或者使用 `Postman` 发起请求，都会触发安防策略。

编程的过程就是解决问题的过程，不要怕麻烦，自己踩过坑之后，才能变得更加强大。

前往 `config/config.default.js` 做好白名单配置，这里我直接全部允许请求：

```js
config.security = {
  csrf: {
    enable: false,
    ignoreJSON: true
  },
  domainWhiteList: [ '*' ], // 配置白名单
};
```

重启项目，再次用 `Postman` 发起请求，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8c4d2e4595440e4a17983c8ed55941b~tplv-k3u1fbpfcp-zoom-1.image)

成功拿到服务端返回的参数。

#### 从 Service 内获取数据

目前咱们还没有链接 `MySQL` 数据库，所以这边模拟一下在 `Service` 中获取数据库的数据。

我们在 `app` 目录下新建 `service`，并且创建一个 `home.js`，为其添加如下代码：

```js
// app/service/home.js
'use strict';

const Service = require('egg').Service;

class HomeService extends Service {
  async user() {
    // 假设从数据库获取的用户信息
    return {
      name: '嘎子',
      slogen: '网络的世界太虚拟,你把握不住'
    };
  }
}
module.exports = HomeService;
```

我们可以在 `Controller` 内拿到上述方法，如下所示：

```js
//  app/controller/home.js
// 获取用户信息
async user() {
  const { ctx } = this;
  const { name, slogen } = await ctx.service.home.user();
  ctx.body = {
    name,
    slogen
  }
}
```

打开 `Postman` 请求如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb7312d231974f02a309a0d91392e7ed~tplv-k3u1fbpfcp-zoom-1.image)

`HomeService` 中的 `user` 方法内部，在后续链接数据库之后，可以 `this` 上下文，拿到 `MySQL` 的实力方法，对数据库进行 `CRUD` 操作。

#### Egg.js 中使用前端模板

很多同学可能没有经历过前端刀耕火种的年代，切换路由都是服务器直接出 `HTML` 页面，并且会刷新整个页面。同学们不要小看这种形式，它的渲染速度在多数情况下是比当代的单页面开发形式的网页要快一些的。

我们开发一些简单的网页，想快速部署到云服务器上，就可以使用前端模板的开发形式。下面介绍该种方式如何操作：

首先安装插件 `egg-view-ejs`：

```bash
npm install egg-view-ejs -save
```

然后在 `config/plugin.js` 里面声明需要用到的插件：

```js
module.exports = {
  ejs: {
    enable: true,
    package: 'egg-view-ejs'
  }
};
```

 紧接着我们需要去 `config/config.default.js` 里配置 `ejs` ，这一步我们会将 `.ejs` 的后缀改成 `.html` 的后缀。

```js
config.view = {
  mapping: {'.html': 'ejs'}  //左边写成.html后缀，会自动渲染.html文件
};
```

上述的配置，指的是将 `view` 文件夹下的 `.html` 后缀的文件，识别为 `.ejs`。

接着，在 `app` 目录下创建 `view` 文件夹，并且新建一个 `index.html` 文件，作为前端模板，如下所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title><%-title%></title>
</head>
<body>
    <!-- 使用模板数据 -->
    <h1><%-title%></h1> 
</body>
</html>
```

我们会在 `Controller` 内把变量注入到 `index.html` 文件，模板通过 `<%-xx%>`关键字获取到传入的变量。

下面修改 `controller/home.js` 下的 `index` 方法如下：

```js
async index() {
  const { ctx } = this;
  // ctx.render 默认会去 view 文件夹寻找 index.html，这是 Egg 约定好的。
  await ctx.render('index.html', {
    title: '我是尼克陈', // 将 title 传入 index.html
  });
}
```

我们尝试在浏览器打开 `http://localhost:7001/`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d31534c47314bfe9dc3cc7800a58710~tplv-k3u1fbpfcp-zoom-1.image)

上述代码在服务端就已经构建完毕，输出的是一个纯静态的 `HTML` 文件，我们可以在浏览器右键点击「显示网页源代码」，查看网页源代码，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/566d2f0bbaac499d90399e638d9b4f85~tplv-k3u1fbpfcp-zoom-1.image)

正常情况下，在渲染的网页上看到的内容，如果在上述源代码页面内都能找到响应的部分，那可以理解为是服务端直接输出的 `HTML` 渲染的。

#### 不用框架，模板一把梭

上述开发模式便是前后端不分离的模式，在页面不复杂的情况下，整个项目不采用如 `React` 、`Vue` 这些前端框架，也是可以的。在上述代码 `ctx.render` 之前，我们可以从数据库获取想要的信息，作为参数塞入模板中，模板拿到数据，便可以自由发挥，构建 `HTML`。如果是提交事件，可以通过原生 `ajax` 或者是引入一把梭专家 `jQuery`，提交数据。

## 总结

能跟着教程到这一步的同学，基本上对 `Egg` 有了一个大致的了解。当然，光了解这些基础知识不足以完成整个项目的编写，但是基础还是很重要的嘛。毕竟 `Egg` 是基于 `Koa` 二次封装的，很多内置的设置项需要通过小用例去熟悉，希望同学们不要偷懒，跟完上面的内容，最好是不要做 `CV` 大佬，逐行的去敲，去琢磨，才能真正的变成自己的知识。

下一章我们讲解如何在本地安装 `MySQL`，考虑到不同电脑系统的同学，教程会分 `Windows` 和 `Mac` 两个版本。

#### 本章节源代码

[点击下载](https://s.yezgea02.com/1620397096921/egg-example.zip)


## 20.前端实战：个人中心

## 前言

行文至此，万里长征已经快要走到头了。本章节带同学们来编写最后一个模块 —— 个人中心。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7faa8d9d5851499ba78625108b2ddea1~tplv-k3u1fbpfcp-zoom-1.image)

个人中心模块分几个功能点，首先是头部的用户信息展示，包括头像、用户昵称、个人签名。其次是一些账号相关的操作，如用户信息修改、密码重置等。最后是退出登录，将其放置于页面底部，并且设置二次确认弹窗，避免误触。

#### 知识点

- 图片资源上传格式处理。

- 原生表单插件 `rc-form` 的使用。

- 底部导航栏定位。

## 正文

#### 头部信息展示

修改 `container/User/index.jsx` 代码如下：

```js
import React from 'react';

import s from './style.module.less';

const User = () => {
  return <div className={s.user}>
    <div className={s.head}>
      <div className={s.info}>
        <span>昵称：测试</span>
        <span>
          <img style={{ width: 30, height: 30, verticalAlign: '-10px' }} src="//s.yezgea02.com/1615973630132/geqian.png" alt="" />
          <b>个性签名</b>
        </span>
      </div>
      <img className={s.avatar} style={{ width: 60, height: 60, borderRadius: 8 }} src={'//s.yezgea02.com/1624959897466/avatar.jpeg'} alt="" />
   </div>
  </div>
}

export default User
```

> 文末已为同学们提供下本章节 demo 代码，样式部分不再详细说明。

这里给 `.head` 一个背景图片，介绍一下顶部的布局思路，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7140a83118464d419c020dd84616954f~tplv-k3u1fbpfcp-zoom-1.image)

在 `.head` 内通过 `flex` 实现左右布局，在 `.info` 内通过 `flex` 的 `flex-direction` 设置为 `column` 实现上下布局。

`.head` 底部留出的位置，用于放置后续的操作。

完成布局之后，将数据填上，通过 `/api/user/get_userinfo` 接口，获取用户信息，添加代码如下：

```js
import React, { useState, useEffect } from 'react';
import { get } from '@/utils';

import s from './style.module.less';

const User = () => {
  const [user, setUser] = useState({});
  
  useEffect(() => {
    getUserInfo();
  }, []);

  // 获取用户信息
  const getUserInfo = async () => {
    const { data } = await get('/api/user/get_userinfo');
    setUser(data);
    setAvatar(data.avatar)
  };

  return <div className={s.user}>
    <div className={s.head}>
      <div className={s.info}>
        <span>昵称：{user.username || '--'}</span>
        <span>
          <img style={{ width: 30, height: 30, verticalAlign: '-10px' }} src="//s.yezgea02.com/1615973630132/geqian.png" alt="" />
          <b>{user.signature || '暂无个签'}</b>
        </span>
      </div>
      <img className={s.avatar} style={{ width: 60, height: 60, borderRadius: 8 }} src={user.avatar || ''} alt="" />
   </div>
  </div>
}

export default User
```

`/api/user/get_userinfo` 接口返回字段分析：

- avatar：头像地址，这里要注意，我目前采用的线上接口，如果是本地开发的情况，需要修改你的 `host`。

- signature：个性签名。

- username：用户登录名称。

浏览器展示如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38d7bc9820bb40af9b3c0a587ea44c2d~tplv-k3u1fbpfcp-zoom-1.image)

#### 用户信息相关操作

紧接着，我们需要布局用户相关操作的内容，在上述基础上添加如下代码：

```js
... 
import { useNavigate } from 'react-router-dom';
import { Cell,  } from 'zarm';

const User = () => {
  ...
  const navigateTo = useNavigate();

  return <div className={s.user}>
    ... 
    <div className={s.content}>
      <Cell
        hasArrow
        title="用户信息修改"
        onClick={() => navigateTo('/userinfo')}
        icon={<img style={{ width: 20, verticalAlign: '-7px' }} src="//s.yezgea02.com/1615974766264/gxqm.png" alt="" />}
      />
      <Cell
        hasArrow
        title="重制密码"
        onClick={() => navigateTo('/account')}
        icon={<img style={{ width: 20, verticalAlign: '-7px' }} src="//s.yezgea02.com/1615974766264/zhaq.png" alt="" />}
      />
      <Cell
        hasArrow
        title="关于我们"
        onClick={() => navigateTo('/about')}
        icon={<img style={{ width: 20, verticalAlign: '-7px' }} src="//s.yezgea02.com/1615975178434/lianxi.png" alt="" />}
      />
    </div>
  </div>
};
```

添加样式：

```css
...
.content {
  width: 90%;
  position: absolute;
  top: 120px;
  left: 50%;
  transform: translateX(-50%);
  box-shadow: 3px 2px 20px 10px rgba(0, 0, 0, .1);
  border-radius: 10px;
  overflow: hidden;
}
```

代码部分，直接采用 `Zarm` 组件库提供的 `Cell` 组件，它适用于列表布局，[官方文档](https://zarm.gitee.io/#/components/cell)提供了很多列表布局的例子，可以直接在内部拷贝代码进行二次加工。能不用自己写样式，尽量就不要写。用组件库的目的，就是减少工作量，提高布局的效率。

浏览器展示效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efc9a9ee5b794140b0da572a651b67f3~tplv-k3u1fbpfcp-zoom-1.image)

这里有三个列表跳转项，分别是 `userinfo`、`account`、`about`。我们逐一击破。

首先我们在 `container` 目录下新建一个 `UserInfo` 目录，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/508f67feaa5745689513b1c3a4037bbb~tplv-k3u1fbpfcp-zoom-1.image)

添加 `index.js` 和 `style.module.less`，并且在 `router/index.js` 内添加相对应的路由配置项。

于是我们尝试点击「修改用户信息」，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be3e4fe43b5f48afa0e627a53efcdada~tplv-k3u1fbpfcp-zoom-1.image)

成功之后，我们便可在 `UserInfo` 中编写编辑用户相关信息的操作，在编写正式代码之前，我们先对 `Zarm` 的上传组件进行分析，我们尝试编写如下代码：

```js
import React from 'react';
import { FilePicker, Button } from 'zarm';

import s from './style.module.less';

const UserInfo = () => {

  const handleSelect = (file) => {
    console.log('file', file)
  }
  return <div className={s.userinfo}>
    <FilePicker onChange={handleSelect} accept="image/*">
      <Button theme='primary' size='xs'>点击上传</Button>
    </FilePicker>
  </div>
};

export default UserInfo;
```

点击按钮，上传一张图片，我们查看回调函数 `handleSelect` 的执行结果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5668a3d8c3ac48fc9c793060570ddf8a~tplv-k3u1fbpfcp-zoom-1.image)

此时，我们需要的是上传资源的原始文件，在上述返回对象中，`file` 属性为 `File` 文件类型，它是浏览器返回的原生对象，我们需要通过下列代码，将其改造成一个 `form-data` 对象：

```js
const handleSelect = (file) => {
  console.log('file', file)
  let formData = new FormData()
  formData.append('file', file.file)
}
```

再将 `formData` 通过 `axios` 上传到服务器，服务端通过 `ctx.request.files[0]` 获取到前端上传的
文件原始对象，并将其读取，存入服务器内部。这样就完成了一套前端上传资源，服务端存储并返回路径的一个过程。

接下来进行完整代码的编写，如下所示：

```js
import React, { useEffect, useState } from 'react';
import { Button, FilePicker, Input, Toast } from 'zarm';
import { useNavigate } from 'react-router-dom';
import Header from '@/components/Header'; // 由于是内页，使用到公用头部
import axios from 'axios'; // // 由于采用 form-data 传递参数，所以直接只用 axios 进行请求
import { get, post } from '@/utils';
import { baseUrl } from 'config';  // 由于直接使用 axios 进行请求，统一封装了请求 baseUrl
import s from './style.module.less';

const UserInfo = () => {
  const navigateTo = useNavigate(); // 路由实例
  const [user, setUser] = useState({}); // 用户
  const [avatar, setAvatar] = useState(''); // 头像
  const [signature, setSignature] = useState(''); // 个签
  const token = localStorage.getItem('token'); // 登录令牌

  useEffect(() => {
    getUserInfo(); // 初始化请求
  }, []);

  // 获取用户信息
  const getUserInfo = async () => {
    const { data } = await get('/api/user/get_userinfo');
    setUser(data);
    setAvatar(data.avatar)
    setSignature(data.signature)
  };

  // 获取图片回调 
  const handleSelect = (file) => {
    console.log('file.file', file.file)
    if (file && file.file.size > 200 * 1024) {
      Toast.show('上传头像不得超过 200 KB！！')
      return
    }
    let formData = new FormData()
    // 生成 form-data 数据类型
    formData.append('file', file.file)
    // 通过 axios 设置  'Content-Type': 'multipart/form-data', 进行文件上传
    axios({
      method: 'post',
      url: `${baseUrl}/upload`,
      data: formData,
      headers: {
        'Content-Type': 'multipart/form-data',
        'Authorization': token
      }
    }).then(res => {
      // 返回图片地址
      setAvatar(res.data)
    })
  }

  // 编辑用户信息方法
  const save = async () => {
    const { data } = await post('/api/user/edit_userinfo', {
      signature,
      avatar
    });

    Toast.show('修改成功')
    // 成功后回到个人中心页面
    navigateTo(-1)
  }

  return <>
    <Header title='用户信息' />
    <div className={s.userinfo}>
      <h1>个人资料</h1>
      <div className={s.item}>
        <div className={s.title}>头像</div>
        <div className={s.avatar}>
          <img className={s.avatarUrl} src={avatar} alt=""/>
          <div className={s.desc}>
            <span>支持 jpg、png、jpeg 格式大小 200KB 以内的图片</span>
            <FilePicker className={s.filePicker} onChange={handleSelect} accept="image/*">
              <Button className={s.upload} theme='primary' size='xs'>点击上传</Button>
            </FilePicker>
          </div>
        </div>
      </div>
      <div className={s.item}>
        <div className={s.title}>个性签名</div>
        <div className={s.signature}>
          <Input
            clearable
            type="text"
            value={signature}
            placeholder="请输入个性签名"
            onChange={(value) => setSignature(value)}
          />
        </div>
      </div>
      <Button onClick={save} style={{ marginTop: 50 }} block theme='primary'>保存</Button>
    </div>
  </>
};

export default UserInfo;
```

详细的注释信息，已经在上述代码中表明，需要注意的是，本次请求直接使用了 `axios` 方法，所以我们需要将 `baseUrl` 单独封装到一个配置文件中，便于后续使用，在 `src` 目录下新建 `config/index.js`，添加如下代码：

```js
const MODE = import.meta.env.MODE // 环境变量

export const baseUrl = MODE == 'development' ? '/api' : 'http://api.chennick.wang';
```

`MODE` 作为 `vite` 运行时的环境变量，可以通过它来配置开发环境和生成环境的一些变量差异。

然后需要在 `vite.config.js` 中修改如下：

```js
resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'), // src 路径
      'utils': path.resolve(__dirname, 'src/utils'), // src 路径
      'config': path.resolve(__dirname, 'src/config') // src 路径
    }
  },
```
配置好 `config` ，便可以直接在代码中通过：

```js
import { baseUrl } from 'config';
```

上述形式来获取 `config` 中的变量信息。

重启项目，浏览器展示效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8155a0c93fbe47d1a5c061ffb57d91fd~tplv-k3u1fbpfcp-zoom-1.image)

通过请求，得到的路径是这样的，因为我们在服务端返回的地址就是一个相对路径，所以我们需要给路径加上 `host`，要注意如果你是本地启动的服务端代码，这里的 `host` 就是你的服务端代码启动的 `host`，如 `locahost:7001`，而我目前使用的是在线接口，所以我们在 `utils/index.js` 下新增一个图片地址转换的方法，如下所示：

```js
// utils/index.js
import { baseUrl } from 'config'
const MODE = import.meta.env.MODE // 环境变量
...
export const imgUrlTrans = (url) => {
  if (url && url.startsWith('http')) {
    return url
  } else {
    url = `${MODE == 'development' ? 'http://api.chennick.wang' : baseUrl}${url}`
    return url
  }
}
```

然后在 `UserInfo/index.jsx` 中引入 `imgUrlTrans` 并如下使用：

```js
// 获取用户信息
const getUserInfo = async () => {
  const { data } = await get('/api/user/get_userinfo');
  setUser(data);
  setAvatar(imgUrlTrans(data.avatar))
  setSignature(data.signature)
};

... 

// 返回图片地址
setAvatar(imgUrlTrans(res.data))
```

再次打开浏览器，点击选择图片如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/806c25af2a8c4622a7286a1b68f0bcf9~tplv-k3u1fbpfcp-zoom-1.image)

保存后，数据成功修改，我们如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3260506bed5945fa94fb872358850ad8~tplv-k3u1fbpfcp-zoom-1.image)

#### 重置密码

完成用户信息编辑之后，接下来实现重置密码部分，我们在 `container` 目录下新建 `Account` 目录，在内部分别新建 `index.jsx` 和 `style.module.less`。

首先我们需要安装 `rc-form` 作为本次页面的表单组件，因为 `Zarm` 没有提供表单组件，包括 `Antd Mobile` 这样的组件，也没有提供表单相关的组件，所以这里我们需要使用 `rc-form` 自己编写表单相关验证方法，它也是 `antd` 官方使用的表单组件。

```bash
npm i rc-form -S
```

我们为 `Account/index.jsx` 添加如下代码：

```js
// Account/index.jsx
import React from 'react';
import { Cell, Input, Button, Toast } from 'zarm';
import { createForm  } from 'rc-form';
import Header from '@/components/Header'
import { post } from '@/utils'

import s from './style.module.less'

const Account = (props) => {
  // Account 通过 createForm 高阶组件包裹之后，可以在 props 中获取到 form 属性
  const { getFieldProps, getFieldError } = props.form;

  // 提交修改方法
  const submit = () => {
    // validateFields 获取表单属性元素
    props.form.validateFields(async (error, value) => {
      // error 表单验证全部通过，为 false，否则为 true
      if (!error) {
        console.log(value)
        if (value.newpass != value.newpass2) {
          Toast.show('新密码输入不一致');
          return
        }
        await post('/api/user/modify_pass', {
          old_pass: value.oldpass,
          new_pass: value.newpass,
          new_pass2: value.newpass2
        })
        Toast.show('修改成功')
      }
    });
  }

  return <>
    <Header title="重制密码" />
    <div className={s.account}>
      <div className={s.form}>
        <Cell title="原密码">
          <Input
            clearable
            type="text"
            placeholder="请输入原密码"
            {...getFieldProps('oldpass', { rules: [{ required: true }] })}
          />
        </Cell>
        <Cell title="新密码">
          <Input
            clearable
            type="text"
            placeholder="请输入新密码"
            {...getFieldProps('newpass', { rules: [{ required: true }] })}
          />
        </Cell>
        <Cell title="确认密码">
          <Input
            clearable
            type="text"
            placeholder="请再此输入新密码确认"
            {...getFieldProps('newpass2', { rules: [{ required: true }] })}
          />
        </Cell>
      </div>
      <Button className={s.btn} block theme="primary" onClick={submit}>提交</Button>
    </div>
  </>
};

export default createForm()(Account);
```

样式代码：

```css
.account {
  padding: 0 12px;
  .form {
    :global {
      .za-cell:after {
        left: unset;
        border-top: unset;
        border-bottom: 1PX solid #e9e9e9;
      }
    }
  }
  .btn {
    margin-top: 50px;
  }
}
```

这里要注意，`Account` 在抛出去的时候，需要用 `createForm()` 高阶组件进行包裹，这样在 `Account` 的内部能接收到 `form` 属性，它的内部提供了 `getFieldProps` 方法，对 `Input` 组件进行表单设置，`Input` 的 `onChange` 方法会被代理，最终可以通过 `form.validateFields` 以回到函数的形式拿到 `Input` 内的值，并且可以加以验证。

别忘记在路由配置项中添加相应的路由：

```js
// router/index.js 
... 
import Account from '@/container/Account'

... 
{
  path: "/account",
  component: Account
}
```

页面展示如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/219b6798b5bc4e6ca78b6db0165af6b8~tplv-k3u1fbpfcp-zoom-1.image)

这里为了方便查看效果，输入框就不以密码的形式隐藏输入了，点击「提交」按钮之后，接口调用成功，但是我为 `admin` 账户在服务端设置了不能修改密码的权限，这里方便大家测试页面方便，不能随意修改密码。

> 测试账号：admin，密码：111111

#### 退出登录

退出登录操作，我的处理方式是将本地的 `token` 清除，并且回到登录页面，简单粗暴了一些，但也不失为一个解决方案。

在 `User/index.jsx` 下添加代码如下：

```js
const User = () => {
  // 退出登录
  const logout = async () => {
    localStorage.removeItem('token');
    navigateTo('/login');
  };

  return <div className={s.user}>
    ... 
    <Button className={s.logout} block theme="danger" onClick={logout}>退出登录</Button>
  </div>
}
```

样式如下：

```css
.logout {
  width: 90%;
  position: absolute;
  bottom: 70px;
  left: 50%;
  transform: translateX(-50%);
}
```

通过绝对定位将按钮定位在底部，我们尝试点击它，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/502235db11294dad90861694845e5241~tplv-k3u1fbpfcp-zoom-1.image)

再次点击登录，发现没有自动前往首页，我们这里对登录页面进行修改，打开 `Login/index.jsx`，做如下修改：

```js
const { data } = await post('/api/user/login', {
  username,
  password
});
console.log('data', data)
localStorage.setItem('token', data.token);
window.location.href = '/'
```

这里之所以用 `window.location.href` 的原因是，`utils/axios.js` 内部需要再次被执行，才能通过 `localStorage.getItem` 拿到最新的 `token`。如果只是用 `navigateTo` 跳转页面的话，页面是不会被刷新，那么 `axios.js` 的 `token` 就无法设置。

## 总结

实战部分到此结束，同学们若是在实战中遇到了问题，请前往课程的官方交流群，群里有与你志同道合的同学，以及本人也会在群里为大家排忧解难。




## 21.项目部署上线

## 前言

为了能让用户通过线上地址预览项目，我们需要将本次编写的前后端项目部署到服务器上。本章节为大家带来部署 `Node` 服务端项目和前端项目。

#### 知识点

- CentOS 服务器
- 配置 ssh
- MySQL 服务器端安装
- egg 服务端部署
- pm2 进程守护

代码都已经推到 `Github` 仓库，地址如下所示：

> 记账本服务端代码仓库地址：https://github.com/Nick930826/jue-diary-server

> 记账本前端代码仓库地址：https://github.com/Nick930826/juejue-vite-h5

## 正文

#### 购买服务器

我们先从服务器的购买谈起，如果已经购买服务器的同学，可以省略这一步的。

为什么要购买服务器呢，当你本地开发好项目的时候，你只能跑在你的本机电脑上，所以此时你只能独自欣赏自己的项目。别人无法通过访问你的 IP 地址，去浏览你跑在本地的项目。而服务器的能力，就是可以让你把项目跑在服务器上，让用户通过访问你的服务器抛出的`IP` + `端口号`，去浏览你的网页或者使用你抛出的接口。

服务器的品类也有很多，阿里云、腾讯云、华为云、七牛云等等，都有提供云服务器的功能，这里我选择的是阿里云服务器，同学们可以自行选择。我选择阿里云的原因很简单，它的用户较多，遇到问题的话，网上会有比较多的解决方案，少走弯路。

购买服务器有两种选择，第一种是「包年包月」，有条件的同学可以选择包年，既然接触了全栈开发，或多或少都需要跟服务器打交道；第二种则是「按量收费」，按量收费的特点是可以根据自己的需要，开启或关闭服务器。

购买时，注意一点，一定要选择 `CentOS` 的镜像，版本尽量选择最高版本。因为它是基于 `unix`，对开发比较友好。

这是我购买的配置，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dda1ea5c0f1044068c6dac0432d98505~tplv-k3u1fbpfcp-zoom-1.image)

用于平时部署简单项目，这样的配置基本上是满足的。但是如果你要运行一些比较大型的项目，并且有多个的话，`2G` 的内存是不够的，因为考虑到项目会在服务器端进行打包，会占用不少内存，有可能会因为服务器的内存不足，而导致打包失败，到时候再升级内存的话，就会比较费钱。

#### ssh 配置

购买服务器之后，首先要做的就是登录服务器，市面上不乏可视化的服务器造作软件，但我的建议是指令操作才是一个程序员应该具备的能力。

在此之前，我们先在本地配置好 `ssh`。

**什么是 ssh**

百度百科给出的定义：

> SSH 为 Secure Shell 的缩写，由 IETF 的网络小组（Network Working Group）所制定；SSH 为建立在应用层基础上的安全协议。SSH 是较可靠，专为远程登录会话和其他网络服务提供安全性的协议。利用 SSH 协议可以有效防止远程管理过程中的信息泄露问题。SSH最初是UNIX系统上的一个程序，后来又迅速扩展到其他操作平台。SSH在正确使用时可弥补网络中的漏洞。SSH客户端适用于多种平台。几乎所有UNIX平台—包括HP-UX、Linux、AIX、Solaris、Digital UNIX、Irix，以及其他平台，都可运行SSH。

我用一句话概括它：

> SSH是一种网络协议，用于计算机之间的加密登录。

服务器也是一台计算机，只不过它是远端的计算机，大家买的阿里云、腾讯云等服务器，相当于一台常年开启状态的计算机，可以通过 `dos` 界面进行操作，也可以通过市面上的服务器可视化工具进行管理。

**本地安装 ssh，实现免密登录**

如果已经安装过，忽略这部分的内容，没有安装的请继续往下看。

如果开发机器是 `Windows` 系统，可以先在本地安装好 `git`，然后通过命令行来到项目的 `~` 路径下，运行如下指令生成 ssh key：

```bash
ssh-keygen -t rsa -C "xxxxx@xxxxx.com"
```

上述邮箱地址写邮箱地址，这里不一定要写邮箱，只是为了方便找到生成的 `ssh key` 是谁的。

执行完成后，前往 `~/.ssh` 路径下，查看是否生成好的相应的公钥。笔者的公钥如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dafbcae65da04944a8a749940e318240~tplv-k3u1fbpfcp-zoom-1.image)

`id_rsa.pub` 文件里面的内容，就是需要的公钥内容。

拿到本机的公钥之后，进入阿里云服务器，同样先看看服务器是否有设置好公钥，打开 `~/.ssh` 查看。如果是刚买的服务器，建议先全局安装好 `git`，然后再去查看 `~/.ssh`，正常情况下是如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed0a883481f44b17a539c33e525bc719~tplv-k3u1fbpfcp-zoom-1.image)

> 如果没有内容，建议按照本地配置 ssh key 的方法，在服务器端再做一次配置。

上图所示的 `authorized_keys` 文件，便是设置免密登录的配置文件。只需将你本地电脑的 `id_rsa.pub` 公钥内容，拷贝到 `authorized_keys` 中并保存，那么你便可以在本地远程免密登录服务器，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0335ca539a2e415e81afeff629947de7~tplv-k3u1fbpfcp-zoom-1.image)

如果没有配置好 `authorized_keys`，那么你每次做上述操作的时候，都会提示你输入服务器的登录密码。这样就会阻碍我们后续通过 `pm2` 远程自动化登录服务器。

既然已经配置好了服务器的 `ssh`，我们将服务器的公钥 `id_rsa.pub`，拷贝到我们存放代码仓库的权限配置里，这一步的目的是让服务器可以通过 `ssh` 的方式拉取代码仓库内的最新代码，配置如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1d303bafe1541019e4efade55c0d047~tplv-k3u1fbpfcp-zoom-1.image)

笔者将代码放到了 `Github` 仓库，上图为 `Github` 的 `Setting` 界面，点击 `SSH and GPG keys`，新建一个 `SSH key`，将服务器的公钥粘贴进去，完成之后，你便可以在服务器通过 `ssh` 的方式拉取代码。


以上操作是对本地计算机和云端服务器的一些基础配置，目的是为后面的操作打下基础。

#### MySQL 服务器端安装

第三章笔者讲述了 `MySQL` 在本地的安装，因为那时我们开发也是在本地，所以配置一个本地数据库足矣。而此时，我们需要将服务端的项目上线，`Egg` 开发的项目就不能再连接本地数据库，当然，线上服务代码也连接不上我们本地的数据库。

**第一步**

远程登录服务器之后运行以下命令更新 `yum` 源：

```bash
rpm -Uvh  http://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
```

> 这里我们使用的 `MySQL` 版本是 5.7.28。

安装 `MySQL`，注意这里安装稳定社群版：

```bash
yum install mysql-community-server
```

全部安装完成之后，可以通过以下命令查看是否安装成功：

```bash
[root@iZbp15axph2ymmv3k3i5oxZ ~]# mysql --version
mysql  Ver 14.14 Distrib 5.7.28, for Linux (x86_64) using  EditLine wrapper
```

**第二步**

此时需要配置一下安装好后的 `MySQL`。执行如下命令启动它：

```bash
systemctl start mysqld
```

设置开机自动启动：

```bash
systemctl enable mysqld
```

如果遇到一些问题，需要重启数据库的话，执行以下指令：

```bash
systemctl restart mysqld
```

网上说通过以下命令可以看到初始化密码，因为为了安全考虑，5.7 以后的 `MySQL` 版本，都会有一个默认的初始密码，可以通过下列指令来获取：

```bash
grep 'temporary password' /var/log/mysqld.log
```

如果你通过这条命令行能获取到初始密码，那基本上你就可以进入 `MySQL` 数据库，重制你的密码了。但是我碰到的情况是，`mysqld.log` 文件为空，没有内容。 

于是经过翻阅资料，查到可以设置一些配置，跳过输入密码然后进入 `MySQL` 数据库。操作如下：

1、修改 `MySQL` 的配置文件（默认为/etc/my.cnf）,在`[mysqld]`下添加一行`skip-grant-tables`，如下：

```bash
[mysqld]
skip-grant-tables
```

2、保存配置文件后，重启 `MySQL` 服务 `systemctl restart mysqld`。

3、执行 `mysql -u root -p` 登录 `MySQL`，然后不输入密码直接回车。

4、登录之后，修改密码，操作如下：

```bash
update mysql.user set authentication_string=password('123456') where user='root'
```

5、记得去阿里云服务 `ESC` 实例的安全组里把 `3306` 端口开启，因为 `MySQL` 启动之后，默认是跑在 `3306` 端口上的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b234851298234de0a3c3dfb01494cf62~tplv-k3u1fbpfcp-zoom-1.image)

上述一系列操作的目的，就是将 `MySQL` 在服务器内成功安装，并且启动。这样我们便可以通过 `ip+端口` 的形式，在本地通过 `DBeaver` 远程连接服务器端的数据库，下面是连接操作：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0e7e6a059c44bd78532d67b1e192a92~tplv-k3u1fbpfcp-zoom-1.image)

- 服务器地址：笔者的地址是 `47.99.134.126`，这里可以填写你们自己的地址。

- 端口：默认是 `3306`。

- 用户名：默认是 `root`。

- 密码：这里的密码就是上述我们安装 `MySQL` 时，自己设置的密码。

填写完之后，点击底部的确认按钮，便可连接到服务器的 `MySQL`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78b133e75fcb4609aee663301d564e35~tplv-k3u1fbpfcp-zoom-1.image)

上图所示，笔者已经在服务器端建好了 `jue-cost` 表，`ER图` 如上所示。

这里提供给大家一个 `SQL` 文件，可以直接在数据库导入 `SQL` 文件，直接创建好需要的表结构。

> SQL文件下载：[jue-cost](https://s.yezgea02.com/1625642433217/jue-cost.sql)。

新建好一个数据库之后，右键选择导入上述文件即可。当然，你也可以手动新建一个数据库，并在数据库内创建这三张表，可以参照第五章讲述的内容。

#### 部署服务端代码

接下来我们要做两件事情，第一步先将本地的服务端代码上传到代码仓库，`Github` 和 `Gitee` 都可以，只要是一个线上管理的代码仓库便可。这样做的目的是便于后续的代码更新，可以在服务器及时地拉取到最新的代码。

笔者已经将服务端代码上传到了 `Github`，地址如下：

> https://github.com/Nick930826/jue-diary-server

这里要注意的是，在 `/config/config.default.js` 文件中，你需要修改你自己的数据库名和密码，如下：

```js
exports.mysql = {
  // 单数据库信息配置
  client: {
    // host
    host: 'localhost',
    // 端口号
    port: '',
    // 用户名
    user: 'root',
    // 密码
    password: '你自己的数据库密码',
    // 数据库名
    database: '你自己新建的数据库名称',
  },
  // 是否加载到 app 上，默认开启
  app: true,
  // 是否加载到 agent 上，默认关闭
  agent: false,
};
```

我们前往服务器拉取最新的服务端代码，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0808f86e22f04106a083a95ab08ea395~tplv-k3u1fbpfcp-zoom-1.image)

拉取完成之后，查看文件夹，会多处这么一个项目：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/337ffd64326a474a808d0d08e77bd5dc~tplv-k3u1fbpfcp-zoom-1.image)

进入项目，安装 `node_modules` 包，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2af410c91ac44253a9f825f90363f2d0~tplv-k3u1fbpfcp-zoom-1.image)

安装完成之后，执行 `npm run start`，服务端项目就启动完成了，不用担心它会挂掉，`Egg` 自带进程守护功能。

于是乎，项目就被运行在这样一个地址上：

> http://47.99.134.126:7009

我们不妨测试以下获取用户信息接口是否能连通，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6aca5db70aa041f88918ae42b9d42ab2~tplv-k3u1fbpfcp-zoom-1.image)

目前我们尚未登录，请求时没有携带 `token`，所以此接口返回了 `token` 不存在的错误信息。

这就表明，服务端部署已经成功，你可以通过该接口地址去访问相应的接口，来制作前端页面。

#### 前端 pm2 部署

服务端项目部署完之后，我们继续部署前端项目。先来描述一下前端项目从打包到部署到服务器上的整个过程。

1、首先我们需要运行 `npm run build` 对项目进行打包操作，打完包后，在根目录会出现一个 `dist` 目录，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31733a560b914814a96fc834c2c08e21~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示：

- assets：存放打包后的静态资源，如 js、css、图片等。

- index.html：项目入口页面，就是整个项目需要通过这个页面初始化，内部也看到了引入了 index.xxx.js，这是整个项目的 js 脚本。

现在需要想方设法让 `index.html` 跑在服务器上的某个端口。

这里，为大家推荐一个比较好用的一个插件，通过命令行安装它：

```bash
npm i pushstate-server
```

`pushstate-server `为什么提供了很便捷的启动 `web` 服务的配置，内部的原理是通过 `connect` 服务器，开启一个端口，将 `dist/index.html` 文件作为静态模板输出。

安装好之后，在 `H5` 项目的根目录添加 `juejue-vite-h5-server` 文件，内容如下：

```js
const server = require('pushstate-server')

server.start({
  port: 5021,
  directory: './dist'
})
```

- port：需要启动的端口号。

- directory：`index.html` 所在的目录路径，这里直接写相对路径就好。

配置好上述内容之后，就需要引入 `pm2` 的概念，它是一个进程管理工具，对于前端而言最重要的功能便是进程守护，通过它启动的 `node` 服务，服务挂了会自动拉起项目。

在 `H5` 项目根目录新增 `ecosystem.config.js`，在项目本地执行 `pm2 `的时候，会匹配的项目根目录下的 `ecosystem.config.js` 文件，并且执行它的配置。配置如下：

```js
module.exports = {
  apps: [
    {
      name: 'juejue-vite-h5',
      script: 'juejue-vite-h5-server.js'
    },
  ],
  deploy: {
    production: {
      user: 'root',
      host: '47.99.134.126',
      ref: 'origin/master',
      repo: 'git@git.zhlh6.cn:Nick930826/juejue-vite-h5.git',
      path: '/workspace/juejue-vite-h5',
      'post-deploy': 'git reset --hard && git checkout master && git pull && npm i --production=false && npm run build:release && pm2 startOrReload ecosystem.config.js', // -production=false 下载全量包
      env: {
        NODE_ENV: 'production'
      }
    }
  }
}
```

- apps：`script` 为服务器通过 `pm2` 要执行的脚本，`name` 为脚本在 `pm2` 列表中的名称，这个名称要注意，避免后续其他项目重名，在服务器中你会无法区分是哪个项目。

- deploy：`production` 为部署正式环境的配置，这里我就不配置 `beta` 环境的代码，因为目前就只有一台服务器。

- production.user：默认 root 用户。

- production.host：要部署的服务器 `IP` 地址。

- production.ref：要部署的代码，在代码仓库中的哪个分之，如果是测试环境，那么这里应该就是 `origin/develop`，这里我们默认是正式。

- production.repo：代码存放的地址，这里是我的地址，你可以写你自己的代码仓库地址。

- production.path：在服务器拉取远程仓库地址之后，存放在服务器中的地址，这里我习惯存放在 `workspace` 文件夹内，同学们可以根据自己的习惯进行操作。

- production.post-deploy：需要执行的一些指令，如 `git reset` 重制、`git checkout master` 切换分支、`git pull` 拉取最新代码、`npm i` 安装依赖、`npm run build` 打包构建、`pm2 startOrReload ecosystem.config.js` pm2 执行项目。

> 这里有一点要注意的是，安装依赖的时候，设置 `--production=false` 的目的是将 `devDependencies` 中的包也进行安装，否则我们无法进行 `vite` 打包操作。


首次执行的时候，由于服务器中并没有 `juejue-vite-h5` 这个项目，所以我们需要初始化一下项目，如下所示：

```bash
pm2 deploy ecosystem.config.js production setup
```

执行上述代码之前，服务器并没有 `juejue-vite-h5` 项目：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0025f2fef96a4993b46381a816c62954~tplv-k3u1fbpfcp-zoom-1.image)

我们尝试在前端项目中执行上诉指令：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d84b7f2926447559e1af44fd0013c22~tplv-k3u1fbpfcp-zoom-1.image)

成功之后，查看服务器中是否拉取成功：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34f5d8adf29844e396257cb00b2920be~tplv-k3u1fbpfcp-zoom-1.image)

此时服务器中已经存在 `juejue-vite-h5` 项目，接下来就是自动化执行整个部署流程，执行指令：

```
pm2 deploy production
```

> 注意，代码一定要先提交，因为服务器需要拉取最新的代码，这里必须要保持本地 commit 是没有未提交的。

上述方式如果是服务器的内存是够的情况下，可以正常自动化部署，但是笔者的服务器跑了太多的项目。导致在服务器执行打包操作的时候，内存不足，将部署进程杀死了。

于是我采用本地将项目打包好，连同 `dist` 一起上传到仓库，服务器在拉取代码的时候就不用再执行打包操作，直接执行 `pm2 startOrReload ecosystem.config.js` 操作。所以我们需要修改 `ecosystem.config.js` 如下：

```js
'post-deploy': 'git reset --hard && git checkout master && git pull && npm i --production=false && pm2 startOrReload ecosystem.config.js', // 
```

再次执行 `pm2 deploy production`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/778635c68e204b6d9f92a8976b3e4004~tplv-k3u1fbpfcp-zoom-1.image)

部署成功之后，笔者的前端项目是部署在 `5021` 端口上的，所以直接访问 `http://47.99.134.126:5021`，如下所示表示成功部署：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f39897abf124f198d294b7090fde885~tplv-k3u1fbpfcp-zoom-1.image)

恭喜你，你已经成功将前端项目通过 `pm2` 部署到服务器，并且正常运行了。后续的更新操作，你可以直接将代码在本地打包完，推到代码仓库后，在项目下运行 `pm2 deploy production` 就能自动部署到服务器。

## 总结

部署项目的配置过程可能非常艰辛，但是做程序很多时候就是这样，这种方式部署项目的付出回报率是很可观的，你不必再每次打包之后，将项目压缩拖到服务器，而是通过一条简单的指令，一键部署到服务器，大大提高了工作效率。

如果有条件的同学，使用的是 `GitLab` 作为代码仓库，还可以通过 `CI、CD` 进行持续集成，这里不展开分析。



## 22.问题汇总(持续更新)

## 学习过程中问题汇总

## 数据库相关
#### 问题 1

`ER_NOT_SUPPORTED_AUTH_MODE` 错误解决。

最新的 `mysql` 模块并未完全支持 `MySQL 8` 的“caching_sha2_password” 加密方式，而“caching_sha2_password”在 `MySQL 8` 中是默认的加密方式。因此，下面的方式命令是默认已经使用了“caching_sha2_password”加密方式，该账号、密码无法在mysql模块中使用。

简单说就是目前 `MySQL 8.0` 以上的版本的加密方式，`Node` 还不支持。

解决方法：

```bash
mysql> ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '你的密码';
```

> 上述指令需启动 `mysql` 的情况下执行。

#### 问题 2

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0dce273995f4e6e80c2337b56be5bb9~tplv-k3u1fbpfcp-zoom-1.image)

上述提示多半是端口被占用了，建议修改 `egg` 启动的端口号，在 `config/config.default.js` 中，如下：

```js
config.cluster = {
  listen: {
    path: '',
    port: 7009, // 项目启动的端口号
    hostname: '0.0.0.0'
  }
}
```

#### 问题 3

服务器安装社群版 `mysql` 报错说没有任何匹配？

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/410f8ab3edef4afab11477bb0b71592e~tplv-k3u1fbpfcp-zoom-1.image)

**解决方案**

 安装前要先禁用 `mysql`，先跑一下后面这个指令 `sudo yum module disable mysql`。
 
 ## 网站相关

 #### 问题 1

 网站部署到服务器上之后，通过 `IP` 地址，无法访问到，咋整？

 **解决方案**

 前往服务器实例，安全组，将你所部署的端口加入安全组，具体操作可自行搜索。

 #### 问题 2

 部署上线之后跨域该如何解决？

 **解决方案**

 服务端项目下，通过 `egg-cors` 插件解决，具体配置如下图：

 ![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a611259f2b93452b85d69e3d8d1a1383~tplv-k3u1fbpfcp-zoom-1.image)
 
 #### 问题 3
 
 部署到线上环境后，遇到如下图的报错：
 
 ![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b905189e71cc47e785510846733c2455~tplv-k3u1fbpfcp-zoom-1.image)
 
 请将 `Zarm` 版本降为 2.8.2，因为高版本不兼容 React 的最新版本，这个问题官方没有很好的解决。
 
 > 注意，降版本的时候，服务器内项目的 node_module 包清理一下，会有缓存。

#### 问题 4

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29690202836646ab9594b7bd1166f030~tplv-k3u1fbpfcp-watermark.image?)
报错：styleImport is not a function

解决办法：
vite-plugin-style-import 插件作者，在后期更新的时候，将默认导出的方法变成了一个 `object`，
所以同学们可以尝试这样的写法：

```js
import { default as styleImport } from 'vite-plugin-style-import'
或者
import styleImport from 'vite-plugin-style-import'
const _styleImport = styleImport.default
...
_styleImport({
    .....
})
```
#### 问题 5
如果遇到"Failed to load PostCSS config"，可以尝试将根目录下的 `postcss.config.js` 的后缀改成 `.cjs`结尾。

## 3.后端预备：MySql 本地安装(Win + Mac)

## 前言

对于前端来说，一看到 `MySQL` 可能内心是抵触的，因为它属于后端领域的范畴，前端专注的是浏览器，服务端专注的是数据。但是作为一名有心成为全栈前端工程师的你来说，数据库的学习和使用是避不开的。你可能会问，为什么是 `MySQL`，而不是 `MongoDB`、`Oracle`、`SQL Server` 之类的数据库。

`MySQL` 的使用率相对较高，遇到问题网上的解决方案也很多，所以本教程使用它来作为数据库工具。

你可以这么理解数据库，它就是用于将数据持久化存储的一个容器，并且这个容器处在云端。而不是像浏览器的本地存储（localStorage）一样，数据只是针对于你当前所在的浏览器。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9165440ef0cd4d1896fa4a8011eeb57e~tplv-k3u1fbpfcp-zoom-1.image)

浏览器的存储是一对一的，而线上数据库的存储是一对多，或者是多对多（数据库可能会有多个）。

后端要做的事情，就是将数据库中的表与表之间，建立好一定的联系。根据产品需要的逻辑联系，将数据以 `API` 接口的形式抛出，供前端开发人员调用。

## 本地安装 MySQL

使用它之前，我们需要在本地安装 `MySQL`，很多前端小伙伴在这一步就没坚持下去，选择了放弃。如果这点困难都不能克服，程序员这个职业可能真的不适合你。

考虑到同学们的电脑系统的不同，这里我分 `Windows` 和 `Mac` 两个版本去介绍如何在本地安装数据库。

#### Windows

`Windows` 操作系统中，有两种安装 `MySQL` 的方法：

1、下载 `MSI` 文件，然后点击运行，利用 `Windows` 系统饿的安装程序方法，一步一步往下走。`MSI` 文件就是可视化界面安装文件。

2、下载 `ZIP` 压缩包，解压出来就能立即使用，可能下载的时候会慢一些，本教程我们使用该方式安装 `MySQL`。

**下载**

首先我们打开 [MySQL 官方下载地址](https://dev.mysql.com/downloads/mysql/)。网站会自动匹配适合你当前计算机的安装文件列表，这里我们选择如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1dab5931e824ff2815bc5b72b28b57e~tplv-k3u1fbpfcp-zoom-1.image)

点击「Download」之后，会让你注册登录账号，此时可以选择点击下面这段文字，跳过注册登录。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77d5a83c24554b299bc6cad6c3635bd2~tplv-k3u1fbpfcp-zoom-1.image)

**解压**

下载完成之后，解压到自己想要放置的目录下，比如我就将其解压到我的 `C:\mysql` 目录下，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97ddc907b5854ace9954c6b84a94cb82~tplv-k3u1fbpfcp-zoom-1.image)

> 注意：此时解压后的文件夹中没有 data 目录和 ini 文件。

此时在 `mysql-8.0.24-winx64` 文件夹内新建一个空的 `my.ini`。如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45fbfeb1799743efbba108f4798cd434~tplv-k3u1fbpfcp-zoom-1.image)

**环境变量配置**

打开控制面板，点击「系统和安全」，进入「系统」点击高级系统设置，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55b58583af264cf290b42f69657fe5ee~tplv-k3u1fbpfcp-zoom-1.image)

点击右下角的「环境变量(N)」按钮，在系统变量里新建名为 「MYSQL_HOME」，变量值就是你上一步解压后存放 `MySQL` 文件的安装路径。我的安装路径如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d10088b081e458eb0f51d5e7c7bf893~tplv-k3u1fbpfcp-zoom-1.image)

设置 `Path`，在 `Path` 里面新增 `bin` 目录。双击 `Path`，然后点击新建按钮，添加 `%MYSQL_HOME%\bin` 如下：

![](https:////s.yezgea02.com/1620633149252/2051620633140_.pic_hd.jpg)

此时你再观察全路径，`MYSQL_HOME` 已经被解析成具体的路径，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb960c3827ed4e449b69bf0db21d06b3~tplv-k3u1fbpfcp-zoom-1.image)

这一步的目的，是为了后续能使用 `cmd` 指令去安装 `MySQL`。

**安装**

首先，以管理员身份运行 `cmd`，`Windows 10` 下，直接右键「开始」，找到「命令提示符(管理员)(A)」，点击打开 `cmd`。

1、进入安装 `mysql` 的目录，进入 `bin`:

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7be74f5c595d4070b1d5620128866f01~tplv-k3u1fbpfcp-zoom-1.image)

2、运行安装指令：

```bash
mysqld --install
```

安装成功的话，控制台会提示如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9d3d686167842f6953a366a21346666~tplv-k3u1fbpfcp-zoom-1.image)

3、运行如下指令生成 `data`  目录：

```bash
mysqld --initialize-insecure --user=mysql
```

4、启动 `mysql` 服务：

```bash
net start mysql
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc0fb5c438f14718884bb1bf7f7d91db~tplv-k3u1fbpfcp-zoom-1.image)

此时，不用怀疑，你已经成功在你的本地启动了 `MySQL` 服务。

<span style="color: red">5、（关键步骤）</span>

如果后续用 `egg-mysql` 插件连接数据库的时候会报下面这样的错误：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4141da8bffe455c9d0d6dc272166436~tplv-k3u1fbpfcp-zoom-1.image)

这是因为 8.0 之前的 `mysql` 版本，加密规则是 `mysql_native_password`，而在 8.0 之后，加密规则变为 `caching_sha2_password`。此时你如果用的是 8.0 以前的版本，那么通过 `egg` 启动项目连接数据库是没问题的，我们这里使用的是 8.0 以后的版本，所以就会出现上述错误。

**解决办法：**

以管理员身份运行 `cmd`，上文已经提到过。通过 `mysql -u root -p` 回车进入 `mysql` 如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b399bc6352ee4db695ed48f37a3315bc~tplv-k3u1fbpfcp-zoom-1.image)

我已经设置过密码了，所以上图我是用密码登录的，你若是没有设置，可以直接敲回车登录。

输入下面指令：

```bash
use mysql;
```

```bash
alter user 'root'@'localhost' identified with mysql_native_password by '你的密码';
```

```bash
flush privileges;
```

上述指令的作用是，还原 `MySQL` 的加密规则，还原之后，你再 `egg` 项目中连接 `MySQL` 的时候，就不会报错了。

并且上述指令中的 **「你的密码」**，如果你设置的话，那就会生效，成为以后你登录数据库的密码。

> 注意，指令一定要按照上述输入，包括最后的分号，不然会指令错误。

#### Mac

接下来，我们来安装 `Mac` 环境下的 `MySQL`。同样的，我们打开[下载地址](https://dev.mysql.com/downloads/mysql/)。我们选择下载 `dmg` 文件，如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f95b266390d4fb1851a4eae55608ff3~tplv-k3u1fbpfcp-zoom-1.image)

> 注意，如果安装完之后，出现一些小问题，如无法载入的情况，建议点击 「Archives」选择稍微低一些的版本，如 8.0.20 等。

这里我选择的就是 8.0.20 的版本，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d06d63be602248079641f724c37779d6~tplv-k3u1fbpfcp-zoom-1.image)

下载完成之后，点击安装，按照步骤往下走，直到需要密码的适合，一定要记住自己设置的初始密码。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d39ca1d7110142a195509a53e3562ff9~tplv-k3u1fbpfcp-zoom-1.image)

后续链接数据库，需要这里设置的密码。

点击 「Finish」之后，我们点开「系统偏好」启动服务：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51a475367ad3413c9af285bb686bb14b~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f3335f0ca814b19b0e6303b51bf9aee~tplv-k3u1fbpfcp-zoom-1.image)

此时我们在命令行输入 `mysql -u root -p` 命令，会提示「commod not found」，我们还需要将 `mysql` 加入系统环境变量。

1、进入 `/usr/local/mysql/bin`，查看此目录下是否有 `mysql`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a22ec1a816f4174851d9cb97b2e0839~tplv-k3u1fbpfcp-zoom-1.image)

2、我们在命令行执行指令：

```bash
vim ~/.bash_profile
```

打开之后，点击键盘 「i」键，进入编辑模式，在 `.bash_profile` 中添加 `mysql/bin` 的目录，结束后点击键盘 「esc」退出编辑，输入 「:wq」回车保存。

如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ae7412f25a4494abf8e294a744a30b5~tplv-k3u1fbpfcp-zoom-1.image)

最后在命令行输入：

```bash
source ~/.bash_profile
```

使其配置生效。

再次输入指令尝试登录数据库，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1b563726de846d7af037f5d8f019bb0~tplv-k3u1fbpfcp-zoom-1.image)

上述的密码是安装数据库时，你自己设置好的初始化密码，进入数据库说明已经成功链接上数据库。此时你可以用各种指令去操作该数据库，也可以通过可视化工具，如 `DBevaer` 操作数据库。

此时我们要开启服务，就用如下指令：

```bash
mysql.server start
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c32953d369749a1acdd1c0917624464~tplv-k3u1fbpfcp-zoom-1.image)

## 总结

可以顺利阅读完本章节，并且本地安装好 `MySQL`，说明你还是学习能力是在线的，我一再强调，过程中遇到问题，可以根据错误提示去搜索引擎查找相关的答案，这个能力是一名普通程序员必备的能力。既然 `MySQL` 已经启动了，下一章节为大家带来，数据库可视化操作工具 `DBevaer`，以及 `Egg` 链接本地数据库，做一些简单的数据库 `CRUD` 工作。

## 4.后端预备：可视化数据库工具 DBeaver 的安装和使用

## 前言

说到可视化工具，大家可能会提到 `Navicat`，很遗憾它是付费的，作为教程不能为大家分析它的破解方法，这样会涉及到侵权。但是 `DBevaer` 所展现出的能力，有过之而无不及，并且它还是免费开源的。

大家可以先去 `DBevaer` [官方网站](https://dbeaver.io/download/)下载相应系统环境的安装包，它提供了 `Windows`、`Mac` 和 `Linux` 三个版本，大家可以自行安装。

## 连接本地数据库

我们在上一章节开启了 `MySQL` 的本地服务，但是我们希望用肉眼可见的方式去操作数据库。当然，有的同学喜欢用命令行操作数据库，这也是可行的。只不过考虑到大多数同学还是初学阶段，故采用可视化的形式，比较容易理解。

#### 打开 DBevaer 连接本地数据库

我们打开软件，界面如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/152102d888fb453090a0d316edbb569f~tplv-k3u1fbpfcp-zoom-1.image)

点击左上角的小插头 🔌  新建连接，我们选择 `MySQL` 数据库：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9745e7d414374576b838d8e9f7da38b1~tplv-k3u1fbpfcp-zoom-1.image)

点击「下一步」后，出现如下界面：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67ac9f2144fb4f22a8f879fc081d3aeb~tplv-k3u1fbpfcp-zoom-1.image)

上图中，我没有填写数据库名称，是因为初始化情况下，没有建任何数据库。所以，如果你要是想要连接具体哪一个数据库，这里就可以写上相应的名称。

数据库密码必须是你之前设置好的初始化密码，所以这个密码一定要记住，最好是记在你的记事本上。设置好之后，点击完成。

如果是 `Windows` 系统的同学，通过管理员打开 `cmd`，通过下图指令启动 `MySQL` 之后，无需输入密码，也可以连接到本地的数据库：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44604c9c1fc746178b6d189a553b3e0e~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/568f630eac814087bfa79306fb7fbf69~tplv-k3u1fbpfcp-zoom-1.image)

> 注意，本地服务一定要开启，否则无法连接成功，在第 3 章有详细的讲解。

成功之后如下，我的本地已经新建了一些数据库，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89189ebbc2c5488784ac4a010d6a9dba~tplv-k3u1fbpfcp-zoom-1.image)

正常情况下，你只会有一个默认的 `sys`。

此时我们已经通过 `DBevaer` 成功连通了数据库，我们接下来新建一个测试数据库，让 `Egg` 能成功的连接上，并且做一些简单的 `CRUD`。

## Egg 连接 MySQL

首先我们新建一个数据库，用于后续的测试操作，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f90a3c05a1e4f429ea6e2a7a05859cb~tplv-k3u1fbpfcp-zoom-1.image)

新建一个名为 `test` 的数据库：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a2005719a47481b8bdeb1316b48b246~tplv-k3u1fbpfcp-zoom-1.image)

其次，在 `test` 数据库下新建一张数据表，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05841be7b7fe449292cab8b34439e8b3~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f4f5bba92b44c3d8cf197f2b26f78b3~tplv-k3u1fbpfcp-zoom-1.image)

再在 `list` 表下新建列：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcfe9656ddf84b33a7cb52525cb51d43~tplv-k3u1fbpfcp-zoom-1.image)

数据类型选择 `INT`，非空和自增都勾选上，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abb654d83795422e870a9bd18d2f11b7~tplv-k3u1fbpfcp-zoom-1.image)

每一张表都需要有一个主键，上述 `list` 表，我们就以 `id` 为主键，点击下图「约束」-> 「新建约束」：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b83153e857414746bffe8bfceedf2f7a~tplv-k3u1fbpfcp-zoom-1.image)

我们保存 `list` 表，选择执行：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c10e27bef1dd4a4ea8c06b05e9ded791~tplv-k3u1fbpfcp-zoom-1.image)

完成之后，我们给 `id` 默认一条数据，切换到「数据」。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61f1979eecfb4c19abdbff701caa9828~tplv-k3u1fbpfcp-zoom-1.image)

同样的步骤，我们给 `list` 表再新增 `name` 属性，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ba50c79d60543d488584cb91bc4f7ba~tplv-k3u1fbpfcp-zoom-1.image)

#### 查询接口

保存数据之后，我们打开第 1 章新建好的项目 `egg-example`，安装插件 `egg-mysql` 如下所示：

```bash
npm install egg-mysql
```

打开 `config/plugin.js` 添加插件配置：

```js
'use strict';

/** @type Egg.EggPlugin */
module.exports = {
  ejs: {
    enable: true,
    package: 'egg-view-ejs'
  },
  mysql: {
    enable: true,
    package: 'egg-mysql'
  }
};
```

打开配置文件 `config/config.default.js`，添加 `mysql` 连接配置项：

```js
exports.mysql = {
  // 单数据库信息配置
  client: {
    // host
    host: 'localhost',
    // 端口号
    port: '3306',
    // 用户名
    user: 'root',
    // 密码
    password: '数据库密码', // 初始化密码，没设置的可以不写
    // 数据库名
    database: 'test', // 我们新建的数据库名称
  },
  // 是否加载到 app 上，默认开启
  app: true,
  // 是否加载到 agent 上，默认关闭
  agent: false,
};
```

修改 `service/home.js` 如下所示：

```js
'use strict';

const Service = require('egg').Service;

class HomeService extends Service {
  async user() {
    const { ctx, app } = this;
    const QUERY_STR = 'id, name';
    let sql = `select ${QUERY_STR} from list`; // 获取 id 的 sql 语句
    try {
      const result = await app.mysql.query(sql); // mysql 实例已经挂载到 app 对象下，可以通过 app.mysql 获取到。
      return result;
    } catch (error) {
      console.log(error);
      return null;
    }
  }
}
module.exports = HomeService;
```

修改 `controller/home.js` 的 `user` 方法如下：

```js
async user() {
  const { ctx } = this;
  const result = await ctx.service.home.user();
  ctx.body = result
}
```

修改路由配置 `router.js`：

```js
router.get('/user', controller.home.user);
```

通过 `npm run dev` 启动项目，我们在浏览器直接调用接口，如下所示代表成功。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c51bc14ee1c4a178f8645f1e00f2da3~tplv-k3u1fbpfcp-zoom-1.image)

我们通过 `/user` 接口地址，获取到了 `list` 表的 `id` 和 `name` 属性，以数组的形式返回。

> 如果通过 npm run dev 启动不成功，请前往第 3 章，Windiws 安装部分，第 5 步关键步骤，有提示如何修改 mysq 8.0 + 的加密规则。

#### 新增接口

查询接口成功之后，我们来编写新增接口。在 `service/home.js` 下新建一个函数 `addUser`，如下所示：

```js
// 新增
async addUser(name) {
  const { ctx, app } = this;
  try {
    const result = await app.mysql.insert('list', { name }); // 给 list 表，新增一条数据
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

再为 `controller/home.js` 添加一个 `addUser` 方法，如下所示：

```js
async addUser() {
  const { ctx } = this;
  const { name } = ctx.request.body;
  try {
    const result = await ctx.service.home.addUser(name);
    ctx.body = {
      code: 200,
      msg: '添加成功',
      data: null
    }
  } catch (error) {
    ctx.body = {
      code: 500,
      msg: '添加失败',
      data: null
    }
  }
}
```

完成之后，添加路由，抛出供前端调用，打开 `router.js` 添加如下代码：

```js
router.post('/add_user', controller.home.addUser);
```

打开 `Postman` 发起一个 `post` 请求，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d0df6f943b949c2b2acfcd9e1ed2ca1~tplv-k3u1fbpfcp-zoom-1.image)

此时我们已经成功往数据库里添加了一条新的内容，我们不妨打开 `DBevaer` 查看数据情况：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2c821da4222430c9ad84c2df560bc17~tplv-k3u1fbpfcp-zoom-1.image)

刷新数据库后，我们可以看到 「我是新增的尼克陈」已经被添加到数据库 `list` 表中，并且 `id` 是自动增加的。

此时你再次请求 `/user` 接口，你会拿到两条数据：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72e7883af7c243ad86bbf73742f864bd~tplv-k3u1fbpfcp-zoom-1.image)

#### 编辑接口

编辑接口，就拿我们上述的内容来说，我们通过 `/user` 拿到了列表数据，我们可以通过 `id` 定位某条数据，去修改它的 `name` 属性。

接下来我们来实现编辑接口，同理，我们打开 `/service/home.js`，添加编辑操作：

```js
// 编辑
async editUser(id, name) {
  const { ctx, app } = this;
  try {
    let result = await app.mysql.update('list', { name }, {
      where: {
        id
      }
    });
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

再前往 `/controller/home.js` 添加如下代码：

```js
// 编辑
async editUser() {
  const { ctx } = this;
  const { id, name } = ctx.request.body;
  try {
    const result = await ctx.service.home.editUser(id, name);
    ctx.body = {
      code: 200,
      msg: '添加成功',
      data: null
    }
  } catch (error) {
    ctx.body = {
      code: 500,
      msg: '添加失败',
      data: null
    }
  }
}
```

别忘了添加路由配置，打开 `router.js` 如下所示：

```js
router.post('/edit_user', controller.home.editUser);
```

我们打开 `Postman` 对编辑接口进行调试，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/172fa49354e54718a9658598d4cad18b~tplv-k3u1fbpfcp-zoom-1.image)

观察数据库 `list` 表是否生效：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df13912b897e440084fccb0dd7cf1de5~tplv-k3u1fbpfcp-zoom-1.image)

#### 删除接口

删除内容，一向都是比较容易的，我们继续在 `/service/home.js` 添加删除接口，如下所示：

```js
// 删除
async deleteUser(id) {
  const { ctx, app } = this;
  try {
    let result = await app.mysql.delete('list', { id });
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

再次前往 `/controller/home.js` 添加相应的控制器方法，如下所示：

```js
// 删除
async deleteUser() {
  const { ctx } = this;
  const { id } = ctx.request.body;
  try {
    const result = await ctx.service.home.deleteUser(id);
    ctx.body = {
      code: 200,
      msg: '删除成功',
      data: null
    }
  } catch (error) {
    ctx.body = {
      code: 500,
      msg: '删除失败',
      data: null
    }
  }
}
```

添加相应路由：

```js
// router.js
router.post('/delete_user', controller.home.deleteUser);
```

打开 `Postman` 调试接口，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfd92e906eb54b6c949ad1c57b537185~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e6f95bc587a4445b308be86ff404528~tplv-k3u1fbpfcp-zoom-1.image)

查看数据库，`id` 为 2 的数据已经被清楚了。

## 总结

本章节带大家学习了可视化数据库 `DBevaer` 的安装和使用，并且通过 `Egg` 结合 `Postman` 演示了一边数据库的「增删改查」操作。一个模块数据的「增删改查」，最基础的模式便是如此，而一个项目的落地，需要在此基础上增加各种复杂多变的逻辑与联系。后续我将带大家从 0 到 1，设计「记账本」项目的数据库表结构。

#### 本章节源代码

[点击下载](https://s.yezgea02.com/1620724318684/egg-example.zip)

> 注意，数据库密码我已经清除，大家下载代码后，在 /config/config.default.js 配置项中填写自己的数据库密码。

## 5.后端实战：数据库表的设计

## 前言

数据库设计，在整个软件工程的流程中，是非常重要的一环。前期的铺垫，都是为了后期开发项目时，能够顺畅一些。包括后续的迭代，都需要在数据库表设计中留下可扩展的可能性。

我们整个「记账本」项目有两个核心模块，第一个是「用户模块」，另外一个是「账单模块」。并且配置了三张数据表，表虽然不多，但是基础功能都有涉及到，所以有后续的需求，可以举一反三，进行拓展。

现在我以一个产品经理提出需求的过程，推演整个数据库设计的思路。

## 数据库设计的原则

#### 1、设计数据库的时间要充沛

数据库是用户需求的映射，设计初衷要以用户需求为中心，尽量与用户保持沟通，这里的用户可以指产品经理，亦或是提需求的人。如果遇到需求不明确的地方，设计表时就要事先预留出可变通的字段，这便是所谓的“未雨绸缪”。

#### 2、多考虑一些性能和优化

提前预判哪些数据将会是比较大的，对于这类数据的表结构，设计的时候往往是粗粒度的，以达到用最少的表，最弱的关系去存储大量的数据。

#### 3、添加必要的（冗余）字段

像“创建时间”、“修改时间”、“备注”、“操作用户IP”和一些用于其他需求（如统计）的字段等，在每张表中必须都要有，不是说只有系统中用到的数据才会存到数据库中，一些冗余字段是为了便于日后维护、分析、拓展而添加的，这点是非常重要的，比如黑客攻击，篡改了数据，我们便就可以根据修改时间和操作用户IP来查找定位。

#### 4、设计合理的表关联

表与表之间的关系复杂的情况下，建议采用第三张映射表来维系两张张复杂表之间的关系，达到降低表之间的直接耦合度。

若多张表涉及到大数据量的问题，表结构尽量简单，关联也要尽可能避免。

接下来我们便来设计本次项目所需要用到的数据表。
## 用户表 user

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf742e82cb4a4b3f83941b59f1dc2928~tplv-k3u1fbpfcp-zoom-1.image)

整个记账本项目是一个面向多人注册的 `C` 端项目，所以需要一个「个人中心」模块，用户可以设置自己的头像、个性签名。但是用户名不能修改，因为用户名是用于登录使用，目前系统没有手机验证码的概念，所以这里用户名相当于用户的唯一标示。在编写注册接口的时候，也会先检验数据库中是否存在相同的用户名。这里需要再给一个创建时间，用户后续扩展业务功能，如用户使用系统的年限、根据时间划分登记等等需求。

根据上述需求分析，我们可以设计如下 `user` 表：

- **id**：`id` 字段设置为自增字段，避免认为操作导致数据重复。设置为自增之后，每次往 `user` 表里新增数据，都会默认 `id` 加 1，就算你删除了前面的数据，是不会影响到 `id` 的自增。后续我们通过鉴权，生成用户信息。账单表的存储，都会以用户作为出发点。相当于 `A` 用户，存储自己的账单时，都会将 `A` 用户的 `id` 带上，相当于这份账单标记了用户 `A` 的 `id` 。

- **username**：用于存储用户登录名称。

- **password**：用于存储用户登录密码。

- **signature**：根据上图，我们还需要一个 `signature` 字段作为个性签名。

- **avatar**：用于存储用户头像信息。

- **ctime**：用于存储用户创建时间字段。

#### 新建项目数据库

我们打开 `DBevaer` 选择本地数据库 `localhost`，新建一个 `juejue-cost` 用于本次项目的开发数据库。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd3654e260d64a118e244ae649ecda7f~tplv-k3u1fbpfcp-zoom-1.image)

创建好之后，在 `juejue-cost` 下创建一张 `user` 表，表属性就是我们上述提到的六个字段，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5a40d4d1d4d47d9a88ba5371c5bd3d2~tplv-k3u1fbpfcp-zoom-1.image)

创建的过程不再赘述，可前往第 4 章，查看创建表的相关工作。这里要注意的是，一定要给表设置好主键，我们这里设置 `id` 为主键。设置主键点击「约束」，在面板右键选择「新建约束」，选择要设置的属性。

## 账单表 bill

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0313f4074ed64580b6f1c8dc8bf72083~tplv-k3u1fbpfcp-zoom-1.image)

上图为账单首页，首页顶部有两个信息，代表当月「总支出」和「总收入」。一笔账单记为一项，每一项账单包括几个关键属性，分别是账单的类型（收入或指出）、账单的种类（服饰、交通、奖金等）、账单的金额、账单的日期时间、账单的备注（当种类无法描述清楚时使用）。

根据上述的需求分析，我们可以这样设计 `bill` 表：

- **id**：每张表都需要一个主键，我们照旧，用 `id` 作为「账单表」的属性。

- **pay_type**：账单类型，账单无非就是两种类型，支出和收入，我们用 `pay_type` 作为类型字段，这里约定好 `1` 为支出，`2` 为收入。

- **amount**：账单价格，每个账单都需有一个价格属性，表示该笔账单你消费或收入了多少钱。

- **date**：账单日期，日期可自由选择，以时间戳的形式存储。

- **type_id**：账单标签 id，如餐饮、交通、日用、学习、购物等。

- **type_name**：账单标签名称，如餐饮、交通、日用、学习、购物等。

- **user_id**：账单归属的用户 `id`，本小册制作的是多用户项目，相当于可以有多个用户来注册使用，所以存储账单的时候，需要将用户的 `id` 带上，便于后面查询账单列表之时，过滤出该用户的账单。

- **remark**：账单备注。


#### 新建账单表

我们在上述 `juejue-cost` 的基础上，新建一张 `bill` 表，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f19aed0cbfc4e4fac7381745678b9bd~tplv-k3u1fbpfcp-zoom-1.image)

保存并执行，`bill` 表生效。

## 标签表 type

一开始我是想在前端把标签定死，比如服饰、交通、医疗等等这类账单种类，写成一个静态的对象，供前端项目使用。但是这样做有一个不好的地方，后续如果希望让用户自己添加自定义标签，就不好拓展。所以这里我们在数据库中设置一张 `type` 表，让用户可以灵活的设置属于自己的自定义标签。

我们需要给标签表设置下列属性：

- **id**：唯一标识，设为主键。

- **name**：标签名称，如餐饮、交通、日用、学习、购物等。

- **type**：标签类型，默认 `1` 为收入，`2` 为支出。

- **user_id**：保留字段，设置该标签的用户归属，默认 0 为全部用户可见，某个用户单独设置的标签，`user_id` 就是该用户的用户 `id`，在获取列表的时候，方便过滤。

#### 新建标签表

我们在数据 `juejue-cost` 中新建 `type` 表，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/077451b38bba48f4b38799a915df6bd5~tplv-k3u1fbpfcp-zoom-1.image)

我们的简表工作，基本上完成了。

## 总结

一套系统，最重要的就是用户鉴权，只要用户鉴权实现之后，围绕用户可以展开多个模块的增删改查，目前就是设置一张账单表进行增删改查的演示，后续的拓展可以根据自己的需要来，比如我还可以再加一张表，叫 `note` 表，专门用于日记的记录，此时也就是对 `note` 表的增删改查。我一再强调举一反三的能力，是因为没有人会把所有的东西一五一十的告诉你，多数情况下需要靠自己领悟和拓展，否则你永远只能停留在初级。




## 6.后端实战：egg-jwt 实现用户鉴权（注册、登录）

## 前言

用户鉴权，是一个系统项目中的重中之重。几乎所有的需求，都是围绕用户体系去展开设计的。放眼市面上诸多项目，哪一个不是建立在用户体系基础上的，如博客、电商、工具、管理系统、音乐、游戏等等领域。所以我们将用户鉴权这块内容放在了第一个要实现的接口。

#### 知识点

- egg-jwt 插件的使用

- egg 中间件编写

- token 鉴权

## 用户鉴权是什么

引用百度百科对「用户鉴权」的定义：

> 用户鉴权，一种用于在通信网络中对试图访问来自服务提供商的服务的用户进行鉴权的方法。用于用户登陆到DSMP或使用数据业务时，业务网关或Portal发送此消息到DSMP，对该用户使用数据业务的合法性和有效性（状态是否为激活）进行检查。

我个人觉得上述解释过于官方，我还是喜欢将复杂的东西简单化。我认为鉴权就是用户在浏览网页或 `App` 时，通过约定好的方式，让网页和用户建立起一种相互信赖的机制，继而返回给用户需要的信息。

鉴权的机制，分为四种：

- HTTP Basic Authentication

- session-cookie

- Token 令牌

- OAuth(开放授权)

本小册采用的鉴权模式是 `token` 令牌模式，出于多端考虑，`token` 可以运用在如网页、客户端、小程序、浏览器插件等等领域。如果选用 `cookie` 的形式鉴权，在客户端和小程序就无法使用这套接口，因为它们没有域的概念，而 `cookie` 是需要存在某个域下。

## 注册接口实现

整个注册的流程大致如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14f50febe2c749b486f7cb2fb4491809~tplv-k3u1fbpfcp-zoom-1.image)

我们将第 2 章新建的 `egg-example` 项目改名为 `juejue-server`，这么做的目的是为了避免重复之前章节的内容，并且将里面的相关代码清理，避免后面写代码的时候产生干扰。

注意将 `config.default.js` 的数据库配置项中的数据库名称修改一下，因为我们上一章节新建了一个数据库：

```js
exports.mysql = {
  // 单数据库信息配置
  client: {
    // host
    host: 'localhost',
    // 端口号
    port: '3306',
    // 用户名
    user: 'root',
    // 密码
    password: '你的数据库初始化密码', // Window 用户如果没有密码，可不填写
    // 数据库名
    database: 'juejue-cost',
  },
  // 是否加载到 app 上，默认开启
  app: true,
  // 是否加载到 agent 上，默认关闭
  agent: false,
};
```

众所周知，用户在网页端注册的时候会上报两个参数，「用户名」和「密码」，此时我们便需要在服务端代码中拿到这俩参数。

在 `controller` 目录下新建 `user.js` 用于编写用户相关的代码，代码如下：

```js
// controller/user.js
'use strict';

const Controller = require('egg').Controller;

class UserController extends Controller {
  async register() {
    const { ctx } = this;
    const { username, password } = ctx.request.body; // 获取注册需要的参数
  }
}

module.exports = UserController;
```

此时我们拿到了 `username` 和 `password`，我们需要判断两个参数是否为空。如果是空，则返回错误信息：

```js
// 判空操作
if (!username || !password) {
  ctx.body = {
    code: 500,
    msg: '账号密码不能为空',
    data: null
  }
  return
}
```

此时我们还需要一个判断，根据用户传入的 `username` 去数据库的 `user` 表查询，是否已经被注册。

> 由于没有手机验证短信服务，这里只能让  username 作为唯一标示。

我们需要在 `service` 目录下新建 `user.js`，并且添加 `getUserByName` 方法用于根据 `username` 查找用户信息，内容如下所示：

```js
//  service/user.js
'use strict';

const Service = require('egg').Service;

class UserService extends Service {
  // 通过用户名获取用户信息
  async getUserByName(username) {
    const { app } = this;
      try {
        const result = await app.mysql.get('user', { username });
        return result;
      } catch (error) {
        console.log(error);
        return null;
      }
  }
}
module.exports = UserService;
```

> 使用 async 和 await 时，如果想捕获错误，需要使用 try...catch 来捕获，如果代码运行过程中发生错误，都将会被 catch 捕获。

我们回到 `controller/user.js` 继续添加逻辑，在 「判空操作」逻辑下，判断是否已经被注册的逻辑：

```js
// controller/user.js
async register() {
  ...
  // 验证数据库内是否已经有该账户名
  const userInfo = await ctx.service.user.getUserByName(username) // 获取用户信息

  // 判断是否已经存在
  if (userInfo && userInfo.id) {
    ctx.body = {
      code: 500,
      msg: '账户名已被注册，请重新输入',
      data: null
    }
    return
  }
}
```

经过上述两层判断之后，接下便可将账号和密码写入数据库，我们继续在上述代码后，添加逻辑：

```js
// controller/user.js
// 默认头像，放在 user.js 的最外，部避免重复声明。
const defaultAvatar = 'http://s.yezgea02.com/1615973940679/WeChat77d6d2ac093e247c361f0b8a7aeb6c2a.png'
// 调用 service 方法，将数据存入数据库。
const result = await ctx.service.user.register({
  username,
  password,
  signature: '世界和平。',
  avatar: defaultAvatar
});

if (result) {
  ctx.body = {
    code: 200,
    msg: '注册成功',
    data: null
  }
} else {
  ctx.body = {
    code: 500,
    msg: '注册失败',
    data: null
  }
}
```

我们继续前往 `service/user.js` 添加 `register` 写入数据库的方法：

```js
// service/user.js
...
// 注册
async register(params) {
  const { app } = this;
  try {
    const result = await app.mysql.insert('user', params);
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

此时上述代码的作用，便是将用户注册数据存入到数据库中的 `user` 表。通过在 `router.js` 将接口抛出，如下所示：

```js
// router.js
'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.post('/api/user/register', controller.user.register);
};
```

打开 `Postman`，进行手动测试，观察是否能成功将数据存入数据库。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baa2eef02e414d3593847075ffe11b52~tplv-k3u1fbpfcp-zoom-1.image)

查看数据库是否生效：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e0e2c3534ed49ac958a65ebb618e375~tplv-k3u1fbpfcp-zoom-1.image)

可以看到我们注册的信息已经进入数据库，此时我们验证一下，再次发起相同的请求，查看服务端代码的判断是否生效。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0e2bccf98434c2481b15aaf854be6f7~tplv-k3u1fbpfcp-zoom-1.image)

不出意外，你将会看到“账户名已被注册，请重新输入”。

通常情况下，我们需要将密码通过 `md5` 或者其他的形式加密，避免数据库泄漏之后，导致用户信息被窃取，造成一些不必要的损失。加密这块，是一个比较深的知识点，为了让大家顺利的走完整个项目流程，这里不展开讲解。

## 登录接口实现

注册完成之后，紧接着就是登录流程。我们通过注册的「用户名」和「密码」，调用登录接口，接口会返回给我们一个 `token` 令牌。这个令牌的生成和使用我们通过一张流程图来分析：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/090527aa47c444f0bcf03f1a7cdb7cdd~tplv-k3u1fbpfcp-zoom-1.image)

网页端获取到 `token` 之后，需要将其存在浏览器本地，它是有过期时间的，通常我们会设置 24 小时的过期时间，如果不是一些信息敏感的网站或app，如银行、政务之类，我们可以将过期时间设置的更长一些。

之后每次发起请求，无论是获取数据，还是提交数据，我们都需要将 `token` 带上，以此来标识，此次获取(GET)或提交(POST)是哪一个用户的行为。

你可能会有疑问，服务端是怎么通过 `token` 来判断是哪一个用户在发起请求。既然 `egg-jwt` 有加密的功能，那也会有解密的功能。通过解密 `token` 拿到当初加密  `token` 时的信息，信息的内容大致就是当初注册时候的用户信息。我们通过一张流程图来分析：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/179bd765019a45c6b030a711790913bd~tplv-k3u1fbpfcp-zoom-1.image)

意思就是登录的时候，你使用的是：

```json
{
  username: '张三',
  password: '123'
}
```

那么这个 `token` 内就会含有上述信息，在服务端解析 `token` 的时候，便会解析出上述「用户名」和「密码」。知道是谁发起的请求，那后续就是针对该用户进行数据的获取和存储。

分析完上述鉴权的流程之后，我们开始登录接口的编写。

首先我们需要在项目下安装 `egg-jwt` 插件，执行如下指令：

```bash
npm i egg-jwt -S
```

这是它的[仓库地址](https://github.com/okoala/egg-jwt#readme)，仓库内有一些简易的文档，具体的操作其实很多都没有写在文档里，我也是搜了很多相关的资料，才设计出这样一套鉴权流程。

在 `config/plugin.js` 下添加插件：

```js
...
jwt: {
  enable: true,
  package: 'egg-jwt'
}
...
```

紧接着前往 `config/config.default.js` 下添加自定义加密字符串：

```js
config.jwt = {
  secret: 'Nick',
};
```

`secret` 加密字符串，将在后续用于结合用户信息生成一串 `token`。`secret` 是放在服务端代码中，普通用户是无法通过浏览器发现的，所以千万不能将其泄漏，否则有可能会被不怀好意的人加以利用。

在 `/controller/user.js` 下新建 `login` 方法，逐行添加分析，代码如下：

```js
async login() {
    // app 为全局属性，相当于所有的插件方法都植入到了 app 对象。
    const { ctx, app } = this;
    const { username, password } = ctx.request.body
    // 根据用户名，在数据库查找相对应的id操作
    const userInfo = await ctx.service.user.getUserByName(username)
    // 没找到说明没有该用户
    if (!userInfo || !userInfo.id) {
      ctx.body = {
        code: 500,
        msg: '账号不存在',
        data: null
      }
      return
    }
    // 找到用户，并且判断输入密码与数据库中用户密码。
    if (userInfo && password != userInfo.password) {
      ctx.body = {
        code: 500,
        msg: '账号密码错误',
        data: null
      }
      return
    }
}
```
`app` 是全局上下文中的一个属性，`config/plugin.js` 中挂载的插件，可以通过 `app.xxx` 获取到，如 `app.mysql`、`app.jwt` 等。`config/config.default.js` 中抛出的属性，可以通过 `app.config.xxx` 获取到，如 `app.config.jwt.secret`。

所以我们继续编写后续的登录逻辑，上述的判断都通过之后，后续的代码逻辑如下：

```js
async login () {
  ...
  // 生成 token 加盐
  // app.jwt.sign 方法接受两个参数，第一个为对象，对象内是需要加密的内容；第二个是加密字符串，上文已经提到过。
  const token = app.jwt.sign({
    id: userInfo.id,
    username: userInfo.username,
    exp: Math.floor(Date.now() / 1000) + (24 * 60 * 60) // token 有效期为 24 小时
  }, app.config.jwt.secret);
  
  ctx.body = {
    code: 200,
    message: '登录成功',
    data: {
      token
    },
  };
}
```

我们把获取到的 `userInfo` 中的 `id` 和 `username` 两个属性，通过 `app.jwt.sign` 方法，结合 `app.config.jwt.secret` 加密字符串（之前声明的 `Nick`），生成一个 `token`。这个 `token` 会是一串很长的加密字符串，类似这样 `dkadaklsfnasalkd9a9883kndlas9dfa9238jand` 的一串密文。

完成上述操作之后，我们在路由 `router.js` 脚本中，将登录接口抛出：

```js
'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.post('/api/user/register', controller.user.register);
  router.post('/api/user/login', controller.user.login);
};
```

我们尝试用 `Postman` 去测试一下接口是否可行，运行成功的话，会是如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e452db8ce6a4d8ab7a8fa70d7cd67df~tplv-k3u1fbpfcp-zoom-1.image)

你可以这么理解这个 `token`，它里面藏着 `username` 和 `id` 两个参数，但是我在客户端拿到这个 `token` 并不能破解出它内部的内容。必须要利用加密字符串，结合 `egg-jwt` 的方法，才能解析出 `username` 和 `id`。所以，用户的权限就通过这样的形式建立起来。

包括 `cookie` 其实也是类似的原理，每次请求，请求头 `requert` 都会带上 `cookie`，服务端通过获取请求中带上的 `cookie` 去解析出对应的用户信息，然后操作相应的请求。

那么我希望验证一下，在发起一个带上 `token` 接口请求时，如何在服务端解析出 `token` 内的信息。我们在 `/controller/user.js` 中，新增一个验证方法 `test`，如下所示：

```js
// 验证方法
async test() {
  const { ctx, app } = this;
  // 通过 token 解析，拿到 user_id
  const token = ctx.request.header.authorization; // 请求头获取 authorization 属性，值为 token
  // 通过 app.jwt.verify + 加密字符串 解析出 token 的值 
  const decode = await app.jwt.verify(token, app.config.jwt.secret);
  // 响应接口
  ctx.body = {
    code: 200,
    message: '获取成功',
    data: {
      ...decode
    }
  }
}
```

我们发起请求的时候，通过在请求头 `header` 上，携带认证信息，让服务端可以通过 `ctx.request.header.authorization` 获取到 `token`，并且解析出内容返回到客户端，别忘了去 `router.js` 抛出这个接口：

```js
router.get('/api/user/test', controller.user.test);
```

我们测试一下接口是否可行：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/638cf1177c4d4c75b47072c6e9f1d42e~tplv-k3u1fbpfcp-zoom-1.image)

注意，我们在请求头 `Headers` 上添加 `authorization` 属性，并且值为之前登录接口获取到的 `token` 值。发起请求后，我们得到返回值，`id = 1`、`username = Nick`。实际证明，我们的鉴权，基本上已经完成了。

## 登录验证中间件

中间件我们可以理解成一个过滤器，举个例子，我们有 `A`、`B`、`C`、`D` 四个接口是需要用户权限的，如果我们要判断是否有用户权限的话，就需要在这四个接口的控制层去判断用户是否登录，为代码如下：

```js
A() {
  if(token && isValid(token)) {
    // do something
  }
}

B() {
  if(token && isValid(token)) {
    // do something
  }
}

C() {
  if(token && isValid(token)) {
    // do something
  }
}

D() {
  if(token && isValid(token)) {
    // do something
  }
}
```

上述操作会有两个弊端：

1、每次编写新的接口，都要在方法内部做判断，这很费事。
2、一旦鉴权有所调整，我们需要修改每个用到判断登录的代码。

现在我们引入中间件的概念，在请求接口的时候，过一层中间件，判断该请求是否是登录状态下发起的。此时我们打开项目，在 `app` 目录下新新建一个文件夹 `middleware`，并且在该目录下新增 `jwtErr.js`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f9c9e3a930f4f5ba50581d867250c45~tplv-k3u1fbpfcp-zoom-1.image)

我们为其添加如下代码：

```js
'use strict';

module.exports = (secret) => {
  return async function jwtErr(ctx, next) {
    const token = ctx.request.header.authorization; // 若是没有 token，返回的是 null 字符串
    let decode
    if(token != 'null' && token) {
      try {
        decode = ctx.app.jwt.verify(token, secret); // 验证token
        await next();
      } catch (error) {
        console.log('error', error)
        ctx.status = 200;
        ctx.body = {
          msg: 'token已过期，请重新登录',
          code: 401,
        }
        return;
      }
    } else {
      ctx.status = 200;
      ctx.body = {
        code: 401,
        msg: 'token不存在',
      };
      return;
    }
  }
}
```

首先中间件默认抛出一个函数，该函数返回一个异步方法 `jwtErr`，`jewErr` 方法有两个参数 `ctx` 是上下文，可以在 `ctx` 中拿到全局对象 `app`。

首先，通过 `ctx.request.header.authorization` 获取到请求头中的 `authorization` 属性，它便是我们请求接口是携带的 `token` 值，如果没有携带 `token`，该值为字符串 `null`。我们通过 `if` 语句判断如果有 `token` 的情况下，使用 `ctx.app.jwt.verify` 方法验证该 `token` 是否存在并且有效，如果是存在且有效，则通过验证 `await next()` 继续执行后续的接口逻辑。否则判断是失效还是不存在该 `token`。

编写完上述的中间件之后，我们就要前往 `router.js` 去使用它，如下所示：

```js
'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller, middleware } = app;
  const _jwt = middleware.jwtErr(app.config.jwt.secret); // 传入加密字符串
  router.post('/api/user/register', controller.user.register);
  router.post('/api/user/login', controller.user.login);
  router.get('/api/user/test', _jwt, controller.user.test); // 放入第二个参数，作为中间件过滤项
};
```

我们模拟不带 `authorization` 的请求，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acae4df05f894e34b976e48f891332ae~tplv-k3u1fbpfcp-zoom-1.image)

勾去选项，发起请求，如上图所示，进入中间件，判断 `token` 不存在。我们在随便写一个 `token` 值验证无效的情况。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5dad61c4c634a2aab0ba2f87eae4401~tplv-k3u1fbpfcp-zoom-1.image)

可见，登录验证的中间件逻辑基本上已经实现了，后续我们如果想要新增一些接口是需要用户权限的，便可以在抛出方法的第二个参数，添加 `_jwt` 方法，这样便可在进入接口逻辑之前就进行用户权限的判断。

## 总结

本章节是整个服务端内容的精华所在，无论什么项目，要做用户权限的话，这些逻辑是避不开的。不过想要选择哪种鉴权方式，还是取决于项目以及团队的需要，做完上述鉴权之后，我们的项目就变成了面向多用户的项目。

#### 本章节源代码

[点击下载](https://s.yezgea02.com/1621494507475/juejue-server.zip)

## 7.后端实战：后端实战：用户信息相关接口实现（修改个签、修改密码、上传头像）

## 前言

上一章节带大家实现了登录注册接口，鉴权的相关工作基本完成。本章节带大家实现用户信息的相关接口，如获取用户信息、修改个性签名、重置用户密码、上传用户头像。

文件资源的上传和获取，是本章节的主要目的，无论是什么项目，服务端都需要处理文件资源，如 `Excel`、`Word`、音频、视频、图片、`pdf` 等。我们以最常见的图片资源为例，通过这个例子的分析和学习，同学们可以拓展思维，将其应用到其他的文件资源形式上。

#### 知识点

- 数据库的资源获取

- 数据库的 `update` 更新

- `Egg` 文件资源处理

## 获取用户信息

话不多说，我们直接进入正题。首先我们打开 `/app/controller/user.js`，添加 `getUserInfo` 方法，代码如下所示：

```js
// 获取用户信息
async getUserInfo() {
  const { ctx, app } = this;
  const token = ctx.request.header.authorization;
  // 通过 app.jwt.verify 方法，解析出 token 内的用户信息
  const decode = await app.jwt.verify(token, app.config.jwt.secret);
  // 通过 getUserByName 方法，以用户名 decode.username 为参数，从数据库获取到该用户名下的相关信息
  const userInfo = await ctx.service.user.getUserByName(decode.username)
  // userInfo 中应该有密码信息，所以我们指定下面四项返回给客户端
  ctx.body = {
    code: 200,
    msg: '请求成功',
    data: {
      id: userInfo.id,
      username: userInfo.username,
      signature: userInfo.signature || '',
      avatar: userInfo.avatar || defaultAvatar
    }
  }
}
```

代码中已经添加详细的注释信息，我就不再赘述了。

接着我们将接口抛出，并且添加鉴权中间件，如下所示：

```js
'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller, middleware } = app;
  const _jwt = middleware.jwtErr(app.config.jwt.secret); // 传入加密字符串
  router.post('/api/user/register', controller.user.register);
  router.post('/api/user/login', controller.user.login);
  router.get('/api/user/get_userinfo', _jwt, controller.user.getUserInfo); // 获取用户信息
  router.get('/api/user/test', _jwt, controller.user.test);
};
```

我们直接通过 `Postman` 验证结构是否可行，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e14d09bb8f204456b94615b781eac5c3~tplv-k3u1fbpfcp-zoom-1.image)

> 注意，需要给 `Headers` 添加 `authorization` 属性，值为之前登录接口返回的 `token` 信息。

#### 修改个性签名

为了兼容后续的修改用户头像，我们将接口名称定义的宽一些，我们在 `/controller/user.js` 下，新建 `editUserInfo` 方法，添加如下代码：

```js
// 修改用户信息
async editUserInfo () {
  const { ctx, app } = this;
  // 通过 post 请求，在请求体中获取签名字段 signature
  const { signature = '' } = ctx.request.body

  try {
    let user_id
    const token = ctx.request.header.authorization;
    // 解密 token 中的用户名称
    const decode = await app.jwt.verify(token, app.config.jwt.secret);
    if (!decode) return
    user_id = decode.id
    // 通过 username 查找 userInfo 完整信息
    const userInfo = await ctx.service.user.getUserByName(decode.username)
    // 通过 service 方法 editUserInfo 修改 signature 信息。
    const result = await ctx.service.user.editUserInfo({
      ...userInfo,
      signature
    });

    ctx.body = {
      code: 200,
      msg: '请求成功',
      data: {
        id: user_id,
        signature,
        username: userInfo.username
      }
    }
  } catch (error) {
    
  }
}
```

此时我们还需要打开 `/service/user.js`，新建一个 `editUserInfo` 用于修改数据库中的用户信息，代码如下：

```js
// 修改用户信息
async editUserInfo(params) {
  const { ctx, app } = this;
  try {
    // 通过 app.mysql.update 方法，指定 user 表，
    let result = await app.mysql.update('user', {
        ...params // 要修改的参数体，直接通过 ... 扩展操作符展开
    }, {
        id: params.id // 筛选出 id 等于 params.id 的用户
    });
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

此时，我们在 `router.js` 脚本中，将修改接口抛出：

```js
router.post('/api/user/edit_userinfo', _jwt, controller.user.editUserInfo); // 修改用户个性签名
```

打开 `Postman` 验证接口是否正确：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a48b31b5a5546108cf49eb03b13e503~tplv-k3u1fbpfcp-zoom-1.image)

数据库也相应的修改成功：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc28d3d301c9491e88e510e77a1ae625~tplv-k3u1fbpfcp-zoom-1.image)

## 修改用户头像

说到修改用户头像，正常情况下， 我们在前端是这样操作的。首先，点击用户头像；其次，弹出弹窗或进入手机相册，选择一张自己喜欢的头像，然后上传头像，最后将自己的头像替换成修改后的头像。

上述流程涉及到一个步骤，那就是「上传图片」。所以在编写修改头像信息接口之前，我们需要先实现一个「上传图片」的接口。上传图片的作用是比较宽泛的，不光是头像需要上传图片，其他很多操作也都需要用到，如朋友圈、商品图片等等。所以我们在 `controller` 文件夹下新建一个脚本，名为 `upload.js`，如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3140b5de27045d1b32b8d1498c963ff~tplv-k3u1fbpfcp-zoom-1.image)

接下来，先分析一波图片上传到服务器的逻辑。

1、首先我们需要在前端调用上传接口，并将图片参数带上，具体怎么带，后面代码部分会讲解。

2、在服务端接收前端传进来的图片信息，信息中含有图片路径信息，我们在服务端通过 `fs.readFileSync` 方法，来读取图片内容，并存放在变量中。

3、找个存放图片的公共位置，一般情况下，都会存放至 `app/public/upload`，上传的资源都存在此处。

4、通过 `fs.writeFileSync` 方法，将图片内容写入第 3 步新建的文件夹中。

5、最后返回图片地址，基本上图片地址的结构是 `host + IP + 图片名称 + 后缀`，后续代码中会为大家详细讲解返回的路径。

目前我们没有前端项目可以上传图片，所以这里我们先用`HTML` 简单写一个上传页面，如下所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>图片上传</title>
</head>
<body>
    <input type="file" id='upload' />
    <script>
      // 获取 input 标签的 dom
      var input = document.getElementById('upload')
      // 监听它的变化
      input.addEventListener('change', function(e) {
        // 获取到上传的 file 对象
        var file = input.files[0]
        // 声明 FormData 实例 formData
        let formData = new FormData()
        // 添加实例属性 file
        formData.append('file', file)
        console.log('formData', formData)
        // 调用服务端上传接口。
        fetch('http://localhost:7001/api/upload', {
          method: 'POST',
          body: formData
        }).then(res => {
          if(res.ok) {
            console.log('success')
            return res.json();
          } else {
            console.log('error')
          }
        }).then(res => {
          console.log('res is', res);
        })
      })
    </script>
</body>
</html>
```

上述 `HTML` 的功能很简单，就是将上传的资源经过 `FormData` 实例封装之后，传给服务端。接下来，我们前往服务端接收数据，打开 `upload.js`，添加如下代码：

```js
'use strict';

const fs = require('fs')
const moment = require('moment')
const mkdirp = require('mkdirp')
const path = require('path')

const Controller = require('egg').Controller;

class UploadController extends Controller {
  async upload() {
    const { ctx } = this
    // 需要前往 config/config.default.js 设置 config.multipart 的 mode 属性为 file
    let file = ctx.request.files[0]
  
    // 声明存放资源的路径
    let uploadDir = ''
  
    try {
      // ctx.request.files[0] 表示获取第一个文件，若前端上传多个文件则可以遍历这个数组对象
      let f = fs.readFileSync(file.filepath)
      // 1.获取当前日期
      let day = moment(new Date()).format('YYYYMMDD')
      // 2.创建图片保存的路径
      let dir = path.join(this.config.uploadDir, day);
      let date = Date.now(); // 毫秒数
      await mkdirp(dir); // 不存在就创建目录
      // 返回图片保存的路径
      uploadDir = path.join(dir, date + path.extname(file.filename));
      // 写入文件夹
      fs.writeFileSync(uploadDir, f)
    } finally {
      // 清除临时文件
      ctx.cleanupRequestFiles();
    }
  
    ctx.body = {
      code: 200,
      msg: '上传成功',
      data: uploadDir.replace(/app/g, ''),
    }
  }
}

module.exports = UploadController;
```

我们从头到位分析资源上传接口逻辑。首先我们需要安装 `moment` 和 `mkdirp`，分别用于时间戳的转换和新建文件夹。

```bash
npm i moment mkdirp -S
```

其次，`egg` 提供两种文件接收模式，1 是 `file` 直接读取，2 是 `stream` 流的方式。我们采用比较熟悉的 `file` 形式。所以需要前往 `config/config.default.js` 配置好接收形式：

```js
config.multipart = {
  mode: 'file'
};
```

`multipart` 配置项有很多选项，比如 `whitelist` 上传格式的定制，`fileSize` 文件大小的限制，这些都可以在[文档](https://eggjs.github.io/zh/guide/upload.html)中查找到。

配置完成之后，我们才能通过 `ctx.request.files` 的形式，获取到前端上传的文件资源。

通过 `fs.readFileSync(file.filepath)` 读取文件，保存在 `f` 变量中，后续使用。

创建一个图片保存的文件路径：

```js
let dir = path.join(this.config.uploadDir, day);
```

`this.config.uploadDir`  需要全局声明，便于后续通用，在 `config/config.default.js` 中声明如下：

```js
// add your user config here
const userConfig = {
  // myAppName: 'egg',
  uploadDir: 'app/public/upload'
};
```

通过 `await mkdirp(dir)` 创建目录，如果已经存在，这里是不会再重新创建的，`mkdirp` 方法内部已经实现。

构建好文件的路径，如下：

```js
uploadDir = path.join(dir, date + path.extname(file.filename));
```

最后，我们将文件内容写入上述路径，如下：

```js
fs.writeFileSync(uploadDir, f)
```

成功之后返回路径：

```js
ctx.body = {
  code: 200,
  msg: '上传成功',
  data: uploadDir.replace(/app/g, ''),
}
```

这里要注意的是，需要将 `app` 去除，因为我们在前端访问路径的时候，是不需要 `app` 这个路径的，比如我们项目启动的是 7001 端口，最后我们访问的文件路径是这样的 `http://localhost:7001/public/upload/20210521/1621564997310.jpeg`。

完成上述操作之后，我们还需要在做最后一步操作，解决跨域。首先安装 `egg-cors` 插件 `npm i egg-cors`，安装好之后，前往 `config/plugins.js` 下添加属性：

```js
cors: {
  enable: true,
  package: 'egg-cors',
},
```

然后在 `config.default.js` 配置如下：

```js
config.cors = {
  origin: '*', // 允许所有跨域访问
  credentials: true, // 允许 Cookie 跨域跨域
  allowMethods: 'GET,HEAD,PUT,POST,DELETE,PATCH'
};
```

上述逻辑完成之后，我们打开之前写好的前端页面，点击上传图片，如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/108e18468dfb4df1940c1642e790c40d~tplv-k3u1fbpfcp-zoom-1.image)

拿到这样一串路径，我们可以查看服务端项目 `app/public` 文件夹下，是否存入了图片资源：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51368a57cea24f64865b9c0293a75789~tplv-k3u1fbpfcp-zoom-1.image)

在通过浏览器访问图片路径，如下代表图片成功上传至服务器：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a488a87f33a42d0b6ed6e43c883c134~tplv-k3u1fbpfcp-zoom-1.image)

此时我们拿到了服务器返回的图片地址，便可以将其提交至 `editUserInfo` 方法。我们为 `editUserInfo` 方法添加如下参数：

```js
// 修改用户信息
async editUserInfo () {
  const { ctx, app } = this;
  // 通过 post 请求，在请求体中获取签名字段 signature
  const { signature = '', avatar = '' } = ctx.request.body

  try {
    let user_id
    const token = ctx.request.header.authorization;
    const decode = await app.jwt.verify(token, app.config.jwt.secret);
    if (!decode) return
    user_id = decode.id

    const userInfo = await ctx.service.user.getUserByName(decode.username)
    const result = await ctx.service.user.editUserInfo({
      ...userInfo,
      signature,
      avatar
    });

    ctx.body = {
      code: 200,
      msg: '修改成功',
      data: {
        id: user_id,
        signature,
        username: userInfo.username,
        avatar
      }
    }
  } catch (error) {
    
  }
}
```

上述代码，在传参中添加了 `avatar` 参数，并且传入 `ctx.service.user.editUserInfo` 方法保存。

#### 上传资源知识拓展

上述方法是我们没有 `OSS` 服务的情况下使用的，目前市面上更多的方式，是购买 `OSS` 服务，将图片等静态资源上传至 `CDN`，通过内容分发的形式，让使用的用户就近获取在线资源。这属于网站性能优化的一种方式，减少主域名下的资源请求数量，以此来降低网页加载的延迟。

七牛云免费提供了 10GB 的存储空间，如果有域名并且备案过的同学，可以利用它实现一个 `CDN` 的服务，将文件资源存到七牛云内，这样可以降低自己服务器的存储压力。

## 总结

此时我们又完成了三个接口的编写，你会觉得，写服务端比写前端轻松多了。

其实不是这样的，每一个工种都有各自的难点。前端更多的是面向浏览器，而浏览器和用户是一对一的关系，前端更多的是注重视觉和交互方面的体验，让用户以最简单易用的方式去完成自己的诉求。

反观服务端，则是一份服务端代码，为多个终端服务，所以服务端更多是一对多的关系。这就很考验服务端的代码，以及数据库的工作效率。在流量峰值能否很好的响应每个用户发起的请求，极端情况就是天猫双十一这种请求量级，服务端的压力是难以想象的。

所以每个工种，只要做得精，都能发光发热。

#### 本章节源代码

[点击下载](https://s.yezgea02.com/1621577800080/juejue-server.zip)

## 8.后端实战：账单及其相关接口实现

## 前言

账单接口是我们本次实战项目的核心模块，用户可以通过账单模块记录自己日常消费和收入情况。本章节我们需要编写五个接口：

1、账单列表
2、添加账单
3、修改账单
4、删除账单
5、账单详情

这样一套增删改查操作下来，基本上可以用这套模式复制出另一套增删改查，所以业务基本上都是互通的，不同之处在于表与表之间能建立什么样的联系，同时也取决于需求方对业务的要求。

#### 知识点

- 一套 `CRUD`。

- 多层级复杂数据结构的处理。

- `egg-mysql` 的使用。

## 新增账单接口

我们需要先实现新增一个账单，才能比较方便的制作后续的其他接口。我们先来回顾一下前面设计好的账单表 `bill`。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41484300de4b4ced9f93e586ad272788~tplv-k3u1fbpfcp-zoom-1.image)

根据上述表的属性，我们可以轻松的知道新增账单接口需要哪些字段，于是我们打开 `/controller`，在目录下新增 `bill.js` 脚本文件，添加一个 `add` 方法，代码如下:

```js
'use strict';

const moment = require('moment')

const Controller = require('egg').Controller;

class BillController extends Controller {
  async add() {
    const { ctx, app } = this;
    // 获取请求中携带的参数
    const { amount, type_id, type_name, date, pay_type, remark = '' } = ctx.request.body;

    // 判空处理，这里前端也可以做，但是后端也需要做一层判断。
    if (!amount || !type_id || !type_name || !date || !pay_type) {
      ctx.body = {
        code: 400,
        msg: '参数错误',
        data: null
      }
    }

    try {
      let user_id
      const token = ctx.request.header.authorization;
      // 拿到 token 获取用户信息
      const decode = await app.jwt.verify(token, app.config.jwt.secret);
      if (!decode) return
      user_id = decode.id
      // user_id 默认添加到每个账单项，作为后续获取指定用户账单的标示。
      // 可以理解为，我登录 A 账户，那么所做的操作都得加上 A 账户的 id，后续获取的时候，就过滤出 A 账户 id 的账单信息。
      const result = await ctx.service.bill.add({
        amount,
        type_id,
        type_name,
        date,
        pay_type,
        remark,
        user_id
      });
      ctx.body = {
        code: 200,
        msg: '请求成功',
        data: null
      }
    } catch (error) {
      ctx.body = {
        code: 500,
        msg: '系统错误',
        data: null
      }
    }
  }
}

module.exports = BillController;
```

新增账单接口唯一需要注意的是，往数据库里写数据的时候，需要带上用户 `id`，这样便于后续查找、修改、删除，能找到对应用户的账单信息。所以本章节的所有接口，都是需要经过鉴权中间件过滤的。必须要拿到当前用户的 `token`，才能拿到用户的 `id` 信息。

处理逻辑已经写完，我们需要把 `service` 服务也安排上，打开 `service`，在目录下新建 `bill.js`，添加代码如下：

```js
'use strict';

const Service = require('egg').Service;

class BillService extends Service {
  async add(params) {
    const { ctx, app } = this;
    try {
      // 往 bill 表中，插入一条账单数据
      const result = await app.mysql.insert('bill', params);
      return result;
    } catch (error) {
      console.log(error);
      return null;
    }
  }
}

module.exports = BillService;
```

`app.mysql.insert` 是数据库插件 `egg-mysql` 封装好的插入数据库操作。它是一个异步方法，所以我们很多地方都是需要异步操作的。

> 不要忘记将接口抛出，很多时候写完了逻辑，忘记抛出接口，就报 404 错误。

```js
// router.js
router.post('/api/bill/add', _jwt, controller.bill.add); // 添加账单
```

打开我们的调试接口好伙伴 `Postman`，验证它：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6ffe1a01c0e409195242431bf761e67~tplv-k3u1fbpfcp-zoom-1.image)

要注意的是 `Headers` 中要带上 `token` 信息如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6dc5263db3f84c9d843a03b245f5a0db~tplv-k3u1fbpfcp-zoom-1.image)

此时我们查看数据库内是否已经添加了数据，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e0a59cf98a14e9fa83270d504c82498~tplv-k3u1fbpfcp-zoom-1.image)

`id` 是自增属性，所以添加一条数据，默认就是 1 ，再添加一条，`id` 则为 2。

有同学会有疑问，这里的 `type_id` 和 `type_name` 属性从哪里来？

我们在添加账单列表的时候，会选择该笔账单的类型，如餐饮、购物、学习、奖金等等，这个账单类型就是我们我们之前定义的 `type` 表里获取的。于是我们在这里实现手动定义好这张表的初始数据，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31e3925fa6c44c03bf402170f0899af9~tplv-k3u1fbpfcp-zoom-1.image)

每个属性代表的意义我们可以返回第 5 章《数据库表的设计》查看详情。这里的 `user_id` 属性为 0 ，代表的是通用的账单类型，所有用户都可以使用。如果后续有需要添加自定义属性，那么 `user_id` 则需要指定某个用户的 `id`。

## 账单列表获取

账单列表的获取，我们可以先查看前端需要做成怎样的展示形式：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/290bb4dba2f0446ba5aae3580985155d~tplv-k3u1fbpfcp-zoom-1.image)

分析上图，账单是以时间作为维度，比如我在 2021 年 1 月 1 日记录了 2 条账单，在 2021 年 1 月 2 日记录了 1 条账，单我们返回的数据就是这样的：

```js
[
  {
    date: '2020-1-1',
    bills: [
      {
        // bill 数据表中的每一项账单
      },
      {
        // bill 数据表中的每一项账单
      }
    ]
  },
  {
    date: '2020-1-2',
    bills: [
      {
        // bill 数据表中的每一项账单
      },
    ]
  }
]
```

并且我们前端还需要做滚动加载更多，所以服务端是需要给分页的。于是就需要在获取 `bill` 表里的数据之后，进行一系列的操作，将数据整合成上述格式。

当然，获取的时间维度以月为单位，并且可以根据账单类型进行筛选。上图左上角有当月的总支出和总收入情况，我们也在列表数据中给出，因为它和账单数据是强相关的。

于是，我们打开 `/controller/bill.js` 添加一个 `list` 方法，来处理账单数据列表：

```js
async list() {
  const { ctx, app } = this;
  // 获取，日期 date，分页数据，类型 type_id，这些都是我们在前端传给后端的数据
  const { date, page = 1, page_size = 5, type_id = 'all' } = ctx.query

  try {
     let user_id
      // 通过 token 解析，拿到 user_id
      const token = ctx.request.header.authorization;
      const decode = await app.jwt.verify(token, app.config.jwt.secret);
      if (!decode) return
      user_id = decode.id
      // 拿到当前用户的账单列表
      const list = await ctx.service.bill.list(user_id)
      // 过滤出月份和类型所对应的账单列表
      const _list = list.filter(item => {
        if (type_id != 'all') {
          return moment(Number(item.date)).format('YYYY-MM') == date && type_id == item.type_id
        }
        return moment(Number(item.date)).format('YYYY-MM') == date
      })
      // 格式化数据，将其变成我们之前设置好的对象格式
      let listMap = _list.reduce((curr, item) => {
        // curr 默认初始值是一个空数组 []
        // 把第一个账单项的时间格式化为 YYYY-MM-DD
        const date = moment(Number(item.date)).format('YYYY-MM-DD')
        // 如果能在累加的数组中找到当前项日期 date，那么在数组中的加入当前项到 bills 数组。
        if (curr && curr.length && curr.findIndex(item => item.date == date) > -1) {
          const index = curr.findIndex(item => item.date == date)
          curr[index].bills.push(item)
        }
        // 如果在累加的数组中找不到当前项日期的，那么再新建一项。
        if (curr && curr.length && curr.findIndex(item => item.date == date) == -1) {
          curr.push({
            date,
            bills: [item]
          })
        }
        // 如果 curr 为空数组，则默认添加第一个账单项 item ，格式化为下列模式
        if (!curr.length) {
          curr.push({
            date,
            bills: [item]
          })
        }
        return curr
      }, []).sort((a, b) => moment(b.date) - moment(a.date)) // 时间顺序为倒叙，时间约新的，在越上面

      // 分页处理，listMap 为我们格式化后的全部数据，还未分页。
      const filterListMap = listMap.slice((page - 1) * page_size, page * page_size)

      // 计算当月总收入和支出
      // 首先获取当月所有账单列表
      let __list = list.filter(item => moment(Number(item.date)).format('YYYY-MM') == date)
      // 累加计算支出
      let totalExpense = __list.reduce((curr, item) => {
        if (item.pay_type == 1) {
          curr += Number(item.amount)
          return curr
        }
        return curr
      }, 0)
      // 累加计算收入
      let totalIncome = __list.reduce((curr, item) => {
        if (item.pay_type == 2) {
          curr += Number(item.amount)
          return curr
        }
        return curr
      }, 0)

      // 返回数据
      ctx.body = {
        code: 200,
        msg: '请求成功',
        data: {
          totalExpense, // 当月支出
          totalIncome, // 当月收入
          totalPage: Math.ceil(listMap.length / page_size), // 总分页
          list: filterListMap || [] // 格式化后，并且经过分页处理的数据
        }
      }
  } catch {
    ctx.body = {
      code: 500,
      msg: '系统错误',
      data: null
    }
  }
}
```

代码逻辑的分析，全部以注释的形式编写，这样方便同学们边看代码，边分析逻辑，上述代码逻辑较长，希望大家能好好分析，实现逻辑越复杂，越能体现你作为程序员的价值。

上述代码使用到了 `service` 服务 `ctx.service.bill.list`，所以后续我们需要在 `/service/bill.js` 下新建 `list` 方法，如下所示：

```js
// 获取账单列表
  async list(id) {
    const { ctx, app } = this;
    const QUERY_STR = 'id, pay_type, amount, date, type_id, type_name, remark';
    let sql = `select ${QUERY_STR} from bill where user_id = ${id}`;
    try {
      const result = await app.mysql.query(sql);
      return result;
    } catch (error) {
      console.log(error);
      return null;
    }
  }
```

这次我们利用执行 `sql` 语句的形式，从数据库中获取需要的数据，`app.mysql.query` 方法负责执行你的 `sql` 语句，上述 `sql` 语句，解释成中文就是，“从 bill 表中查询 user_id 等于当前用户 id 的账单数据，并且返回的属性是 id, pay_type, amount, date, type_id, type_name, remark”。

将接口抛出：

```js
// router.js
router.get('/api/bill/list', _jwt, controller.bill.list); // 获取账单列表
```

前往 `Postman` 验证一下是否生效：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b3f17aa5b8e4a0387ffa7a614229c4e~tplv-k3u1fbpfcp-zoom-1.image)

## 账单修改接口

我们继续制作账单修改接口，修改接口和新增接口的区别在于，新增是在没有的情况下，编辑好参数，添加进数据库内部。而修改接口则是编辑现有的数据，根据当前账单的 `id`，更新数据。

所以这里我们需要实现两个接口：

1、获取账单详情接口

2、更新数据接口

我们先来完成获取账单详情接口，在 `/controller/bill.js` 添加 `detail` 方法，代码如下所示：

```js
// 获取账单详情
async detail() {
  const { ctx, app } = this;
  // 获取账单 id 参数
  const { id = '' } = ctx.query
  // 获取用户 user_id
  let user_id
  const token = ctx.request.header.authorization;
  // 获取当前用户信息
  const decode = await app.jwt.verify(token, app.config.jwt.secret);
  if (!decode) return
  user_id = decode.id
  // 判断是否传入账单 id
  if (!id) {
    ctx.body = {
      code: 500,
      msg: '订单id不能为空',
      data: null
    }
    return
  }

  try {
    // 从数据库获取账单详情
    const detail = await ctx.service.bill.detail(id, user_id)
    ctx.body = {
      code: 200,
      msg: '请求成功',
      data: detail
    }
  } catch (error) {
    ctx.body = {
      code: 500,
      msg: '系统错误',
      data: null
    }
  }
}
```

编写完上述逻辑之后，我们还需要前往 `/service/bill.js` 添加 `ctx.service.bill.detail` 方法，如下所示：

```js
async detail(id, user_id) {
  const { ctx, app } = this;
  try {
    const result = await app.mysql.get('bill', { id, user_id })
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

抛出接口：

```js
router.get('/api/bill/detail', _jwt, controller.bill.detail); // 获取详情
```

打开 `Postman` 查看是否能根据 `id` 获取到账单：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6c5fa6fb13d4d1985ea3720a38a2bdb~tplv-k3u1fbpfcp-zoom-1.image)

此时我们已经可以通过点击账单列表，前往账单详情页面，进行当前账单的编辑修改工作。

于是乎，就引出了编辑账单接口，我们在 `/controller/bill.js` 添加 `update` 方法，如下所示：

```js
// 编辑账单
async update() {
  const { ctx, app } = this;
  // 账单的相关参数，这里注意要把账单的 id 也传进来
  const { id, amount, type_id, type_name, date, pay_type, remark = '' } = ctx.request.body;
  // 判空处理
  if (!amount || !type_id || !type_name || !date || !pay_type) {
    ctx.body = {
      code: 400,
      msg: '参数错误',
      data: null
    }
  }

  try {
    let user_id
    const token = ctx.request.header.authorization;
    const decode = await app.jwt.verify(token, app.config.jwt.secret);
    if (!decode) return
    user_id = decode.id
    // 根据账单 id 和 user_id，修改账单数据
    const result = await ctx.service.bill.update({
      id, // 账单 id
      amount, // 金额
      type_id, // 消费类型 id
      type_name, // 消费类型名称
      date, // 日期
      pay_type, // 消费类型
      remark, // 备注
      user_id // 用户 id
    });
    ctx.body = {
      code: 200,
      msg: '请求成功',
      data: null
    }
  } catch (error) {
    ctx.body = {
      code: 500,
      msg: '系统错误',
      data: null
    }
  }
}
```

`ctx.service.bill.update` 便是操作数据库修改当前账单 `id` 的方法，我们需要在 `/service/bill.js` 添加相应的方法，如下所示：

```js
async update(params) {
  const { ctx, app } = this;
  try {
    let result = await app.mysql.update('bill', {
        ...params
    }, {
        id: params.id,
        user_id: params.user_id
    });
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

`app.mysql.update` 方法，我们在第 2 章基础入门篇已经有所解释，这边我们再能加深一下印象。

第一个参数为需要操作的数据库表名称 `bill`；第二个参数为需要更新的数据内容，这里直接将参数展开；第三个为查询参数，指定 `id` 和 `user_id`。

完事之后，将接口抛出：

```js
router.post('/api/bill/update', _jwt, controller.bill.update); // 账单更新
```

通过 `Postman` 验证接口是否可行：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c34464264a27489bac2cef23faf66c8c~tplv-k3u1fbpfcp-zoom-1.image)

通过详情接口，请求是否修改成功：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96d145c7901a4a0798dcce492205f19d~tplv-k3u1fbpfcp-zoom-1.image)

不负所望，修改生效了。

## 账单删除接口

删除接口可能是这几个接口中，最容易实现的一个。我们只需要获取到单笔账单的 `id`，通过 `id` 去删除数据库中对应的账单数据。我们打开 `/controller/bill.js` 添加 `delete` 方法，如下所示：

```js
async delete() {
  const { ctx, app } = this;
  const { id } = ctx.request.body;

  if (!id) {
    ctx.body = {
      code: 400,
      msg: '参数错误',
      data: null
    }
  }

  try {
    let user_id
    const token = ctx.request.header.authorization;
    const decode = await app.jwt.verify(token, app.config.jwt.secret);
    if (!decode) return
    user_id = decode.id
    const result = await ctx.service.bill.delete(id, user_id);
    ctx.body = {
      code: 200,
      msg: '请求成功',
      data: null
    }
  } catch (error) {
    ctx.body = {
      code: 500,
      msg: '系统错误',
      data: null
    }
  }
}
```

并且前往 `/service/bill.js` 添加 `delete` 服务，如下所示：

```js
async delete(id, user_id) {
  const { ctx, app } = this;
  try {
    let result = await app.mysql.delete('bill', {
      id: id,
      user_id: user_id
  });
    return result;
  } catch (error) {
    console.log(error);
    return null;
  }
}
```

`app.mysql.delete` 方法接收两个参数，第一个是数据库表名称，第二个是查询条件。这里我们给的查询条件是账单 `id` 和用户 `user_id`。其实我们可以不传用户 `user_id`，因为我们的账单 `id` 都是自增的，不会有重复值出现，不过安全起见，带上 `user_id` 起到双保险的作用。

我们将接口抛出：

```js
// router.js
router.post('/api/bill/delete', _jwt, controller.bill.delete); // 删除账单
```

我们打开老朋友 `Postman`，验证接口是否可行：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66831d00bc754b8985ca8e428a44c6bc~tplv-k3u1fbpfcp-zoom-1.image)

报错信息为 “token 已过期，请重新登录”。这说明我们之前生成 `token` 时，配置的时效生效了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77097cb8726142af935cbaf943153b40~tplv-k3u1fbpfcp-zoom-1.image)

当然，你可以将有效期设置成 1 分钟，这样方便测试有效期是否生效。

我们重新通过登录接口获取新的 `token`，如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97b6a3d3ab9d4e1f8968c9f70b18085f~tplv-k3u1fbpfcp-zoom-1.image)

通过新的 `token` 再次发起删除接口请求：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26f9a2102cf843f99a0447d53b8e0ca2~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea262f1f2e5c45b6b96e0db0b87b7326~tplv-k3u1fbpfcp-zoom-1.image)

请求成功，数据库 `bill` 表里已经空空如也。

## 数据图表模块

完成上述账单模块的一套 `CRUD` 之后，同学们基本上对一张表的 `增上改差` 处理，已经轻车熟路了。学习这件事情，很多时候就是靠不断地练习，甚至同一件事情，你不可能做一次就熟练，熟才能生巧。所以我们接下来再对数据模块进行处理和分析，制作出数据图表接口，我们在实现接口之前，先看看需要实现的需求：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c3527a43de24b5fa805af954b6e19b4~tplv-k3u1fbpfcp-zoom-1.image)

首先是头部的汇总数据，并且接口支持事件筛选，以 `月` 为单位。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/901c4e1ee6af4fa9afbbf3b4430cf0eb~tplv-k3u1fbpfcp-zoom-1.image)

其次是收支的构成图，对每一个类型的支出和收入进行累加，最后通过计算占比以此从大到小排布。如上图所示，当前月份的所有学习支出是 `2553`，这个累加计算，我们在服务端完成。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/418a03f05a9a4d32bb0b6647f1f3f437~tplv-k3u1fbpfcp-zoom-1.image)

最后我们引入 `echarts` ，完成一个饼图的简单排布，其实也就是上图收支比例图的一个变种。

**我们最终要返回的数据机构如下：**

```js
{
  total_data: [
    {
      number: 137.84, // 支出或收入数量
      pay_type: 1, // 支出或消费类型值
      type_id: 1, // 消费类型id
      type_name: "餐饮" // 消费类型名称
    }
  ],
  total_expense: 3123.54, // 总消费
  total_income: 6555.80 // 总收入
}
```

#### 数据接口实现

经过上述分析，想必同学们已是胸有成竹。既然数据是和账单强相关，我们将方法写在 `/controller/bill.js` 中，添加 `data` 方法，首先根据用户信息，获取到账单表的相关数据，如下所示：

```js
async data() {
  const { ctx, app } = this;
  const { date = '' } = ctx.query
  // 获取用户 user_id
  // 。。。
  // 省略鉴权获取用户信息的代码
  try {
    // 获取账单表中的账单数据
    const result = await ctx.service.bill.list(user_id);
    // 根据时间参数，筛选出当月所有的账单数据
    const start = moment(date).startOf('month').unix() * 1000; // 选择月份，月初时间
    const end = moment(date).endOf('month').unix() * 1000; // 选择月份，月末时间
    const _data = result.filter(item => (Number(item.date) > start && Number(item.date) < end))
  } catch {
    
  }
}
```

> 代码源码请看底部为大家提供的本章节源码 demo。

上述 `_data` 便是我们经过筛选过滤出来的当月账单基础数据，每一条数据都是之前用户手动添加的，所以会有很多同类项。接下来，我们的工作就是将这些同类项进行合并。

我们先计算总支出，在上述代码追加如下：

```js
...
// 总支出
const total_expense = _data.reduce((arr, cur) => {
  if (cur.pay_type == 1) {
    arr += Number(cur.amount)
  }
  return arr
}, 0)
```

数组方法 `reduce` 的用处，超出你的想象。在一些累加操作上，它的优势展露无疑。就比如上述需求，我们需要在一串数组中，将每一项的支出 `amount` 值，累加起来最后返回给 `total_expense`。你当然可以通过 `forEach` 方法，在外面声明一个变量，循环的累加它，如下所示：

```js
let total_expense = 0

_data.forEach(item => {
  if (item.pay_type == 1) {
    total_expense += Number(item.amount)
  }
})
```

但是，在外面声明一个变量，这样看起来显得不是那么的美观。很多时候，你不想到处声明变量，此时 `reduce` 便能很好地解决这个问题，因为它第二个参数，可以声明一个值，作为循环的初始值，并在每一次的「回调函数」当作第一个参数 `arr` 被传入。

于是我们继续追加总收入的逻辑，如下所示：

```js
// 总收入
const total_income = _data.reduce((arr, cur) => {
  if (cur.pay_type == 2) {
    arr += Number(cur.amount)
  }
  return arr
}, 0)
```

到这里，我们已经将汇总数据完成。接下来完成收支构成部分：

```js
// 获取收支构成
let total_data = _data.reduce((arr, cur) => {
  const index = arr.findIndex(item => item.type_id == cur.type_id)
  if (index == -1) {
    arr.push({
      type_id: cur.type_id,
      type_name: cur.type_name,
      pay_type: cur.pay_type,
      number: Number(cur.amount)
    })
  }
  if (index > -1) {
    arr[index].number += Number(cur.amount)
  }
  return arr
}, [])

total_data = total_data.map(item => {
  item.number = Number(Number(item.number).toFixed(2))
  return item
})

ctx.body = {
  code: 200,
  msg: '请求成功',
  data: {
    total_expense: Number(total_expense).toFixed(2),
    total_income: Number(total_income).toFixed(2),
    total_data: total_data || [],
  }
}
```

我们分析上述 `reduce` 的回调函数，`arr` 初始值为一个空数组，进入回调函数逻辑，首先我们通过 `findIndex` 方法，查找 `arr` 内，有无和当前项 `cur` 相同类型的账单，比如学习、餐饮、交通等等。

如果 `index` 没有找到，则会返回 -1，此时说明当前 `cur` 的消费类型，在 `arr` 中是没有的，所以我们通过 `arr.push` 新增一个类型的数据，数据结构如上所示。

如果找到相同的消费类型，index 值则为大于 -1 的值，所以我们找到 `arr[index]`，让它的 `number` 属性加上当前项的 `amount`，以此实现相同消费类型的累加。

最后，将所有的 `number` 数据保留两位小数，并且将数据返回。

不要忘记将接口抛出：

```js
router.get('/api/bill/data', _jwt, controller.bill.data); // 获取数据
```

`Postman` 调试结果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f0c88a9021143f99af5185efdd1ad40~tplv-k3u1fbpfcp-zoom-1.image)

## 总结

本章节带同学们学习了一个完整的增删改查套件，这可以作为你的种子套件，后续如果有新的需求思路，要添加新的表和方法，可以按照这样一套作为基础进行临摹。比如我想做一个笔记本需求，那我就可以新建一张 `note` 表，再实现一套类似朋友圈的需求，有文字有图片，可删除可添加。

并且对通过数据图表的接口，对数据库表的数据进行二次处理进行了复习，巩固之前的知识点。

#### 本章节源代码

[点击下载](https://s.yezgea02.com/1626659372012/juejue-server.zip)

## 9.🚩 上半场结束｜服务端总结

## 前言

前后端项目目前已经部署到线上环境，大家可以通过以下地址进行访问：

**「掘掘记账本」在线预览：** http://cost.chennick.wang

> 测试账号：admin，测试密码：111111。也可以自行注册使用。

**「掘掘记账本」前端代码开源地址：** https://github.com/Nick930826/juejue-vite-h5

**「掘掘记账本」后端代码开源地址：** https://github.com/Nick930826/jue-diary-server

个人拙见，服务端的开发并没有你想想中的那么复杂，先抛开那些繁杂的工程化工具，我们把整个项目掰开来分析，无非就是以下两个东西，且听我娓娓道来。

## 服务端语言

服务端语言是什么？它是运行在服务器上，可用于读写数据库、编写服务逻辑的语言。

我并不想把这件事情描述的太复杂，因为归根结底它就是做这两件事。

至于服务端语言的选择，完全是根据业务和自身能力相结合。比如我是一个前端开发，我更倾向于选择 `Node` 作为服务端开发语言，因为 `JavaScript` 是我已经比较熟悉的一门语言。

> 这里强调一下，`Node` 它本身不是一门语言，而是一个开发环境，基于谷歌的 V8 引擎，能让 `JavaScript` 可以运行在服务器的一个环境。赋予 `JavaScript` 更多除了浏览器脚本意外的能力，如 `IO` 操作等。

## 数据库

数据库的作用，是用于数据的持久化存储。

本小册选择 `MySQL` 作为数据库，是因为它作为老牌数据库，网上解决方案比较多，同学们若是在开发过程中遇到问题，可以在搜索引擎上轻松找到自己遇到的问题的解决方案，对于新手而言，项目开发的流畅度是关键，完成一整套项目的开发之后，你可以尝试去选择其他更有意思的数据库，这里不展开描述。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a1a8a8e49454f7e92353f3f387c54ec~tplv-k3u1fbpfcp-zoom-1.image)

本教程采用 `egg-mysql` 插件进行数据库的操作。官方推荐我们使用  `Sequelize` 来应对较为复杂的项目。笔者的初衷是希望大家能快速入门，不希望引入过多的复杂概念，这里如果大家在后续的学习过程中有需要应对更为复杂的项目时，可以考虑引入 `Sequelize` 。

## 项目分析

整个项目是基于 `Egg.js` 作为上层架构，通过 `Egg.js` 为我们提供的一些预定好的开发形式，我们轻松地完成了下列十余个接口的开发：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41c7a8e9d1f74023add7e214b215956c~tplv-k3u1fbpfcp-zoom-1.image)

项目不大，但是本项目包含了几个关键的知识点：

- 多用户鉴权

- 一套增删改查

- 表数据的二次处理（图表）

- 列表分页的制作

- 文件数据上传

用“麻雀虽小、五脏俱全”来形容，一点都不为过。

如果你想要在此基础上拓展一些新的功能，如朋友圈、笔记、博客等，都是可以基于该项目进行二次开发的，因为多用户鉴权的架子已经搭建好，后续要做的就是添加表，以及一些业务逻辑上的处理。

当然，如果你想做更为复杂的项目，比如一个商城。那涉及到的内容可能就更多了，单论商品模块的后台编辑，前台展示，就涉及到 `sku`、购物车、库存的处理、多图上传、详情编辑、类型筛选等等。这就很考验同学们的知识储备和解决问题的能力了。

## Q&A 环节

这里将会展示同学们在评论区提出的有价值和频率比较高的提问，作为一个问答列表，让一些有疑问的同学，在笔者没能及时回复的时候，可以答疑解惑。

**Q1： 前端部分是否有在线接口地址？**

**A1：** 答：[API 文档地址](https://www.yuque.com/docs/share/828e93b5-cc86-47b9-885e-f7c29e5750c7?#（密码：zbxg）)

