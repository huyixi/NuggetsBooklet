---
title: 前端工程师进阶 10 日谈
author: 前端工程师进阶 10 日谈
date: 2025-02-14
lang: zh-CN
---

## 1.第一日：遵守各司其责原则

# 第一天

## 第一个故事：切换到夜间模式

在WEB开发中，HTML负责网页的结构，CSS负责网页上各个元素的展示样式，JS则负责网页和用户的交互。想要成为一名优秀的前端工程师，首先要做的就是遵守这三者各司其职的原则，让我们的代码易于维护和扩展。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d6edc4863264ae4984db5099af4ff14~tplv-k3u1fbpfcp-zoom-1.image)

但是，有时候我们常常一不小心就破坏了这个原则。又或者，我们为了实现业务需求，根本不管这个规则。这都会导致我们的代码结构混乱，维护困难。那么下面，我就通过一个例子，来谈谈遵守各司其职这个原则的好处。

现在我们有一个任务，它的具体需求是这样的：给一个网页实现一个深色系和浅色系主题的切换，以使得在夜晚访问这个网页的读者能够使用“夜间模式”。

这个网页的HTML大概是这样的：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>深夜食堂</title>
  <style>
    body, html {
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      overflow: hidden;
    }
    body {
      padding: 10px;
      box-sizing: border-box;
    }
    div.pic img {
      width: 100%;
    }
    #modeBtn {
      font-size: 2rem;
      float: right;
    }
  </style>
</head>
<body>
  <header>
    <button id="modeBtn">🌞</button>
    <h1>深夜食堂</h1>
  </header>
  <main>
    <div class="pic">
      <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
    </div>
    <div class="description">
      <p>
          这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
          眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
      </p>
    </div>
  </main>
</body>
</html>
```

现在的页面，在手机上看起来是这样的效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b0325c25b1bd4ab98363bf46b5d4561e~tplv-k3u1fbpfcp-zoom-1.image)

任务的要求是当用户点击网页右上角的太阳🌞图标时，将网页变为**深夜模式**，即用深色背景、浅色字体来显示网页内容，同时太阳🌞标记变为月亮🌜标记。

这个任务很简单，我们可能非常快的就写下按钮的响应处理：

```js
const btn = document.getElementById('modeBtn');
btn.addEventListener('click', (e) => {
  const body = document.body;
  if(e.target.innerHTML === '🌞') {
    body.style.backgroundColor = 'black';
    body.style.color = 'white';
    e.target.innerHTML = '🌜';
  } else {
    body.style.backgroundColor = 'white';
    body.style.color = 'black';
    e.target.innerHTML = '🌞';
  }
});
```

上面这段代码给按钮注册了click事件，当用户点击按钮的时候，如果当前按钮的文字是🌞，说明是要从日间模式切换成夜间模式，那么将body的背景样式换成深色，文字样式换成浅色，否则将body的背景样式换成浅色，文字样式换成深色。

这是点击按钮后切换的网页呈现效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a623982be3f403b925f2aa329b051ad~tplv-k3u1fbpfcp-zoom-1.image)

看起来，我们完美地实现了产品的需求，可以交差了。但是实际上，上面的代码存在以下三个问题：

1. 对于其他不了解需求的同事，阅读这段代码能够直接理解这个按钮按下的含义吗？
1. 如果产品需求变更，要求用深灰色背景、浅黄色文字来显示夜间模式，JS代码可以避免修改吗？
1. 如果要给切换过程增加动画效果，能方便添加吗？

作为读者的你，知道如何解决这些问题吗？

## 第二个故事：用class属性表示元素的业务状态

第一个故事中，我们直接用JS操作元素，让元素在夜间和白天模式互换：

```js
  body.style.backgroundColor = 'black';
  body.style.color = 'white';
```

这样做的缺点是其他的程序员只知道这两个语句是将`body`的`background`样式改为了黑色，将`color`样式改为了白色，却并不知道这个样式代表的是什么业务需求或者状态。

之所以会这样，是因为我们将**本该由CSS完成的工作交由JS来做了**，本来应该由CSS设置元素的样式，却让JS代替了。所以，我们需要重构一下代码，让它能体现出业务的需求。

我们把夜间模式下元素的样式的设置还给CSS来完成：

```css
body.night {
  background-color: black;
  color: white;
}
```

然后将JS代码重构为如下形式：

```js
const btn = document.getElementById('modeBtn');
btn.addEventListener('click', (e) => {
  const body = document.body;
  if(body.className !== 'night') {
    body.className = 'night';
    e.target.innerHTML = '🌜';
  } else {
    body.className = '';
    e.target.innerHTML = '🌞';
  }
});
```

如上代码所示，当`body`元素的`class`属性不等于`night`时，表示（点击前）当前元素的状态是白天模式，所以现在需要将它的状态修改为夜间模式，于是我们只要将它的`class`属性设置为`night`，页面就会呈现夜间模式的样式。同理，当`body`元素的`class`属性等于`night`时，表示（点击前）body元素是夜间模式，所以需要将这个元素的状态修改为白天模式，也就是默认状态，即`class`属性等于空。

上面的代码，虽然改动十分微小，只是把之前的两行代码：

```js
  body.style.backgroundColor = 'black';
  body.style.color = 'white';
```

替换成一行：

```js
  body.className = 'night';
```

但是，它能解决前面提出的几个问题:

- 首先，className设为night，这个操作本身透露了需求信息，**它描述了这是一个夜间（night）模式的业务状态**。这样就便于后来的维护者快速理解业务需求。

- 其次，如果产品需求变更，把模式对应的颜色换了，我们不需要修改JS代码，只需要修改`body.night`的样式规则即可！

- 第三，如果要增加切换过程的动画效果，可以使用CSS3支持的过渡动画，例如：

```css
body {
  padding: 10px;
  box-sizing: border-box;
  transition: all 1s;
}
body.night {
  background-color: black;
  color: white;
  transition: all 1s;
}
```

给`body`和`body.night`都添加样式规则`transition all 1s`，就可以实现简单的切换动画了。

最后，实际上还有个细节可以改进，那就是`e.target.innerHTML = '🌜';`这样的切换也不是很好，也应该合并到CSS中。这个可以通过伪元素来实现：

```css
#modeBtn::after {
  content: '🌞';
}
body.night #modeBtn::after {
  content: '🌜';
}
```

我们去掉`<button id="modeBtn"></button>`中间的文本内容，然后给它添加伪元素样式，这样我们JS代码简化成：

```js
const btn = document.getElementById('modeBtn');
btn.addEventListener('click', (e) => {
  const body = document.body;
  if(body.className !== 'night') {
    body.className = 'night';
  } else {
    body.className = '';
  }
});
```

这时，JS代码只负责切换元素的状态，而不需要代替CSS改变元素的样式了。

完整的代码如下：

[在线演示](https://junyux.github.io/FE-Advance/day01/index-v2.html)
 
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>深夜食堂</title>
  <style>
    body, html {
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      overflow: hidden;
    }
    body {
      padding: 10px;
      box-sizing: border-box;
      transition: all 1s;
    }
    body.night {
      background-color: black;
      color: white;
      transition: all 1s;
    }
    div.pic img {
      width: 100%;
    }
    #modeBtn {
      font-size: 2rem;
      float: right;
    }
    #modeBtn::after {
      content: '🌞';
    }
    body.night #modeBtn::after {
      content: '🌜';
    }
  </style>
</head>
<body>
  <header>
    <button id="modeBtn"></button>
    <h1>深夜食堂</h1>
  </header>
  <main>
    <div class="pic">
      <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
    </div>
    <div class="description">
      <p>
          这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
          眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
      </p>
    </div>
  </main>
</body>
<script>
  const btn = document.getElementById('modeBtn');
  btn.addEventListener('click', (e) => {
    const body = document.body;
    if(body.className !== 'night') {
      body.className = 'night';
    } else {
      body.className = '';
    }
  });
</scrpit>
</html>
```

从这个故事，我们可以看出，元素的class属性不仅仅只是为了给CSS提供类选择器，还能**表示元素的业务状态**。这样，我们就可以将这些业务状态对应的展示样式交由CSS处理，而JS只需要处理状态的切换即可，从而保证了各司其职的原则，使得我们的代码既能体现业务的需求，也便于将来的维护和扩展。

对于这个例子来说，对于状态的切换，可不可以**完全可以不使用JS，纯用CSS来实现呢**？

## 第三个故事：最好的JS代码是没有JS代码

不使用JS，只使用CSS实现“夜间模式”效果，看起来是一个不小的挑战。不过仔细想想，也不是不可能做到。其实这个问题，最核心的部分是要**使用CSS代替JS来切换并记住与用户交互的状态**。

让我们回忆了一下，在HTML中，能够完成状态切换的元素也是有的，比如表单元素中的选择框（checkbox）元素，那么……

尝试改变一下HTML文档结构：

```html
<body>
  <input id="modeCheckBox" type="checkbox">
  <div class="content">
    <header>
      <button id="modeBtn"></button>
      <h1>深夜食堂</h1>
    </header>
    <main>
      <div class="pic">
        <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
      </div>
      <div class="description">
        <p>
            这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
            眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
        </p>
      </div>
    </main>
  </div>
</body>
```

上面的代码中，我们在body的子元素中添加一个`type="checkbox"`的input元素。当我们点击这个元素时，就有两种状态：普通状态和选中状态。其中，选中状态可以用伪类选择器`#modeCheckBox:checked`来标记。

由于`<input>`元素是body的第一个子元素，它后面的子元素可以通过CSS的兄弟节点选择器来命中。为了便于统一操作，我们给header和main元素外层增加一个`<div class="content">`的容器，这样我们就可以通过CSS选择器改变这个容器的样式：

```css
/* 匹配checkbox选中状态下的.content */
#modeCheckBox:checked + .content {
  background-color: black;
  color: white;
  transition: all 1s;
}
```

上面的这条规则表示当checkbox选中状态下，`.content`元素的样式为黑底白字。

然后，微调一下上一版本的样式，将body中的`padding`移到`.content`容器中，将`body.night`的样式移到`#modeCheckBox:checked + .content`规则中。

```css
body {
  box-sizing: border-box;
}

.content {
  padding: 10px;
  transition: all 1s;
}

#modeCheckBox:checked + .content {
  background-color: black;
  color: white;
  transition: all 1s;
}
```

这样我们就可以通过点击checkbox元素来进行“夜间模式”状态切换了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c376071004074a729cd12159d656eb81~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示，当checkbox被选中时，页面进入夜间模式；当checkbox不被选中时，页面又进入白天模式。

当然，这个效果和需求还有一定差距 —— 不能让用户点击页面顶部的checkbox来替代点击右上角🌞图标，这不符合业务需求。于是，我们打算使用label元素代替checkbox触发用户的点击行为。

通过label元素的for属性指定的id，能够将label元素与对应的表单元素绑定，这样当用户点击label元素的时候，就相当于直接点击对应的表单元素。

<!-- ```html
<label for="modeCheckBox"></label>
``` -->
<!-- 所以，我们只需要将原本的HTMl中的button元素替换成label元素： -->

```html
<body>
  <input id="modeCheckBox" type="checkbox">
  <div class="content">
    <header>
      <label id="modeBtn" for="modeCheckBox"></label>
      <h1>深夜食堂</h1>
    </header>
    <main>
      <div class="pic">
        <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
      </div>
      <div class="description">
        <p>
            这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
            眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
        </p>
      </div>
    </main>
  </div>
</body>
```

如上代码所示，我们将原来的button元素用label元素代替，并将label元素的for属性指向checkbox的id（modeCheckBox）。这样就能够让label元素绑定checkbox元素。

然后，我们再将checkbox框隐藏起来：

```css
#modeCheckBox {
  display: none;
}
```

这样，我们就完美地实现了**只用CSS，不使用JS代码**实现的“夜间模式”切换。

完整代码如下：

[在线演示](https://junyux.github.io/FE-Advance/day01/index-v3.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>深夜食堂</title>
  <style>
    body, html {
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      overflow: hidden;
    }
    body {
      box-sizing: border-box;
    }
    .content {
      padding: 10px;
      transition: all 1s;
    }
    div.pic img {
      width: 100%;
    }
    #modeCheckBox {
      display: none;
    }
    #modeCheckBox:checked + .content {
      background-color: black;
      color: white;
      transition: all 1s;
    }
    #modeBtn {
      font-size: 2rem;
      float: right;
    }
    #modeBtn::after {
      content: '🌞';
    }
    #modeCheckBox:checked + .content #modeBtn::after {
      content: '🌜';
    }
  </style>
</head>
<body>
  <input id="modeCheckBox" type="checkbox">
  <div class="content">
    <header>
      <label id="modeBtn" for="modeCheckBox"></label>
      <h1>深夜食堂</h1>
    </header>
    <main>
      <div class="pic">
        <img src="https://p2.ssl.qhimg.com/t0120cc20854dc91c1e.jpg">
      </div>
      <div class="description">
        <p>
            这是一间营业时间从午夜十二点到早上七点的特殊食堂。这里的老板，不太爱说话，却总叫人吃得热泪盈
            眶。在这里，自卑的舞蹈演员偶遇隐退多年舞界前辈，前辈不惜讲述自己不堪回首的经历不断鼓舞年轻人，最终令其重拾自信；轻言绝交的闺蜜因为吃到共同喜爱的美食，回忆起从前的友谊，重归于好；乐观的绝症患者遇到同命相连的女孩，两人相爱并相互给予力量，陪伴彼此完美地走过了最后一程；一味追求事业成功的白领，在这里结交了真正暖心的朋友，发现真情比成功更有意义。食物、故事、真情，汇聚了整部剧的主题，教会人们坦然面对得失，对生活充满期许和热情。每一个故事背后都饱含深情，情节跌宕起伏，令人流连忘返 [6]  。
        </p>
      </div>
    </main>
  </div>
</body>
</html>
```

现在，我们来比较一下这个版本和第二个故事中有JS的版本，它们各自的的优缺点在哪里：

- JS版本更加简洁，虽然用了JS，但HTML结构更简单。而且JS版本的兼容性要好一些，因为CSS版本使用了兄弟结点选择器，在早期的浏览器上，可能不能被支持。

- CSS版本不用写JS代码，这样就不用维护JS代码，也不可能有JS的bug，所以也是有优势的，尤其是在移动端页面，不用担心浏览器兼容性的前提下，使用这一版更加放心。

虽然这两个版本各有优劣，但是要知道，再简单的代码，也可能会有bug，唯一不会有bug的方式就是不用写代码。**所以，最好的JS代码就是没有JS代码。** 这个项目到这里就结束了，记住你学到的这些，就离高级前端工程师更近了一步。


## 10.第十日：前端工程化

# 第十天

## 第一个故事：搭建环境与代码风格管理

今天的故事是本课程最后的内容，主要来聊聊前端开发的工程化。那么什么是前端工程化呢？它能解决什么问题呢？

我们知道，早期JavaScript代码是写在文本编辑器中的，然后加载到浏览器，直接运行。这种方式对于早期只是开发几个页面来说还是很便利。但是，如今的前端开发演变成复杂的应用开发，一个web项目需要好几个开发人员共同完成。因为一个项目需要多人协作开发，这是就会出现很多问题，比如：

- 模块间变量冲突、覆盖
- 书写风格迥异
- 代码重复和冗余等

前端工程化就是为了解决这些问题而产生的。前端工程化的主要内容包括了**模块化**、**组件化**、**规范化**和**自动化**。在前面的故事中，我们介绍了如何封装模块和创建组件的思路。所以今天的故事，我们重点关注规范化和自动化这两方面。规范化包括了书写规范，版本统一等。自动化包括了自动打包、单元测试，持续集成等等。

早些年，Web开发的规范化一般采用约定的方式，规范程序员的代码书写。比如，让不同的开发人员用不同的名字空间或者不同的前缀来命名各自负责的模块中的变量和函数。但是，这种方式不能保证每个开发人员都能遵守约定，而且在人多的时候，这种方式会把变量和函数的名字变得很复杂，不利于理解和维护。

至于打包，早期的JS语言特性不支持模块化，也没有相应的工具来管理模块，因此开发人员各自写的JS文件都依次添加到HTML页面上。当页面比较复杂的时候，加载的JS文件会比较多，可能造成混乱。再后来，出现了require JS、sea JS等前端模块管理的工具和相应的ADM/CMD规范，前端开始在网页上通过异步加载的方式来管理和组织JS文件，这是最原始的模块管理方式。

但在2009年Node.js诞生后，前端程序员真正有了可以搭建项目工程脚手架和管理代码的环境。用Node.js编写的运行于开发环境代码目录中的工具脚本，可以帮助我们完成诸如代码检查、文件编译、依赖管理、内容打包、单元测试和持续集成等工作，这就让前端项目的代码可维护性大大提升，从而能够轻松维护更大规模的项目。

所以，现在的Web项目一般不再使用“裸写”JavaScript代码的方式，而是会先引入并初始化Node环境。所以第一个故事，我们就来看看Node环境是如何帮助我们实现规范化代码书写的。

下面的内容涉及到[Node.js](https://nodejs.org/)和[NPM](https://www.npmjs.com/)的使用，如果你不了解Node.js和NPM可以查阅它们的官网。

<!-- _这里我们简单介绍一下什么是Node.js和NPM。如果你已经了解了，可以忽略这部分内容。Node.js是基于chrome V8引擎的运行时环境，它可以在命令行下执行JavaScript。而NPM是Node.js的包管理工具，它允许你方便的安装和加载你需要的JS模块。_ -->

首先，在系统里安装好Node.js和NPM后，创建项目目录，在目录下执行初始化NPM配置文件的命令：

```bash
npm init
```

系统将会以询问式的方式创建并初始化NPM配置。这个配置会保存在package.json文件中。通常一个初始的NPM配置如下：

```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "My Web Application",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "MIT"
}
```

这是一份JSON配置文件，`name`字段表示项目名称，如果你要将项目最终发布到NPM，你需要起一个唯一的，没有被人使用过的名字。

`version`字段是项目的版本号，一般来说采用`semver`（语义化版本 Semantic Versioning）规范，根据`semver`规范，版本号格式为：`主版本号.次版本号.修订号`。当项目做了不兼容的API修改时，更新主版本号；做了向下兼容的功能更新时，更新次版本号，只是做了问题修复时，更新修订号。`description`字段是项目描述。

`main`字段是项目的入口JS，如果项目要被其他项目依赖，其他项目的代码中`import`或者`require`时，缺省的入口就是main字段指定的那个JS文件。

`scripts`字段是个很重要的字段，我们的工程化脚本就添加在这里，而且它还有一个很重要的作用，如果我们安装一个带有命令行的Node模块，我们不需要将该模块全局安装，`scripts`中定义的脚本会自动根据`node_modules`找到相应的模块并启动脚本指令。

`keywords`定义模块的关键字，如果我们最终将这个模块发布到NPM上，这里定义的`keywords`有助于其他开发者搜索到模块。

`author`字段设置作者信息。`lincense`设置开源协议。

_关于这份配置文件的说明还有很多，如果你有兴趣可以到官网上查看它的详细说明。这里我们主要介绍这一节需要用到的配置。_

我们初始化好NPM配置之后，就可以安装模块了。

在多人维护的项目中，第一个要做的事情是统一代码风格，包括符号书写风格如缩进、括号、运算符、空格、空行、引号、逗号、分号等等；也包括语法书写风格，如变量命名、逻辑结构、函数签名等等；以及其他一些风格，比如函数参数个数、一行书写的最大字符数、函数长度与逻辑复杂度、单个JS文件长度等等。

这些代码风格检查，我们都可以通过工具`eslint`来完成。所以现在，我们需要给Node环境安装`eslint`包：

```bash
npm install --save-dev eslint
```

上面的命令行中，我们通过`npm install`安装`eslint`，参数`--save-dev`表示将它安装到开发依赖中。安装完成后，`package.json`中增加了`devDependencies`字段，其中内容是当前安装的`eslint`的版本号。如下所示：

```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "My Web Application",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "MIT",
  "devDependencies": {
    "eslint": "^6.8.0"
  }
}
```

安装完成后，我们需要告诉`eslint`检查哪些文件：

```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "My Web Application",
  "main": "index.js",
  "scripts": {
    "lint": "eslint './**/*.js'",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "MIT",
  "devDependencies": {
    "eslint": "^6.8.0"
  }
}
```

如上代码所示，我们给`script`字段添加了`"lint": "eslint './**/*.js'"`这个配置，表示让`eslint`检查项目中所有的JS文件。

但是，`eslint`没有设置默认的检查规则，所以我们必须给它指定检查规则。我们在项目目录下添加一个`.eslintrc.js`文件，内容如下：

```js
module.exports = {
  extends: 'eslint:recommended',
};
```
`eslint:recommended`是`eslint`内置的推荐检查规则，我们暂时就用它来规范开发人员的代码书写。

现在我们在项目中创建一个JS文件`index.js`，内容如下：

```js
var message = "Hello world!";
console.log(message);
```

然后我们在项目目录下运行命令，检查项目下所有JS文件的书写规范：

```bash
npm run lint 
```

这时，我们会看到控制台上输出的检查结果：

```bash
  2:1  error  'console' is not defined  no-undef

✖ 1 problem (1 error, 0 warnings)
```

这条结果说的是`console`变量未定义，但是`console`是在浏览器环境下的内置对象，所以我们可以在`.eslintrc.js`配置里面修改一下：

```js
module.exports = {
  env: {
    browser: true, // 告诉eslint这个项目是浏览器的项目
  },
  extends: 'eslint:recommended',
};
```

因为我们的项目是一个浏览器应用，我们把`env`（环境）配置为`{browser: true}`，这样浏览器下的内置对象就不会报未定义的错误了。

`eslint`还允许我们添加其他规则，比如我们希望不使用`var`，而使用ES6的`const`和`let`声明，那么我们可以添加规则——rules：

```js
module.exports = {
  env: {
    browser: true,
  },
  extends: 'eslint:recommended',
  rules: {
    "no-var": "error",
  },
};
```

我们再次运行`npm run lint`，就可以看到新的错误信息：

```bash
  1:1  error  Unexpected var, use let or const instead  no-var

✖ 1 problem (1 error, 0 warnings)
```

此时我们把`var`改为`const`：

```js
const message = "Hello world!";
console.log(message);
```

再次运行脚本，依然报一个错误：

```bash
  1:1  error  Parsing error: The keyword 'const' is reserved

✖ 1 problem (1 error, 0 warnings)
```

这是因为`eslint`默认的JS版本是ES5，所以不支持`const`语法，需要将默认的JS版本修改为ES6版本：

```js
module.exports = {
  env: {
    browser: true,
  },
  extends: 'eslint:recommended',
  parserOptions: {
    ecmaVersion: 2017,
    sourceType: 'module',
  },
  rules: {
    "no-var": "error",
  },
};
```

上面的代码设置了`parserOptions`属性，将`ecmaVersion`设为`2017`，`sourceType`设为`module`这样它就支持`ES2017`最新的语法和`ES module`模块加载语法的检查了。

其实，ESLint的校验规则很多，有数百条，我们可以在[ESLint官网](https://cn.eslint.org/docs/rules/)上查到所有的规则说明和配置方法，然后根据我们的喜好来配置，但这是一件非常耗时的工作。不过，ESLint提供了交互式初始化校验规则的命令行工具，我们可以使用它来快速配置规则。

### 自动配置 eslint

编辑`package.json`，添加`scripts`字段的内容：

```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint:init": "eslint --init",
    "lint": "eslint './**/*.js'",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "eslint": "^6.8.0"
  }
}
```

我们添加一个`lint:init`命令行脚本，然后运行它：

```bash
npm run lint:init
```

这样ESLint就会启动交互式配置的命令帮助我们配置合适于我们项目的ESLint检查规则。

```bash
> eslint --init

? How would you like to use ESLint? To check syntax, find problems, and enforce 
code style
? What type of modules does your project use? JavaScript modules (import/export)


? Which framework does your project use? None of these
? Does your project use TypeScript? No
? Where does your code run? Browser, Node
? How would you like to define a style for your project? Use a popular style gui
de
? Which style guide do you want to follow? Airbnb: https://github.com/airbnb/jav
ascript
? What format do you want your config file to be in? JavaScript
```

执行`eslint --init`会询问我们几个问题，根据我们的回答初始化配置文件，而且会让我们选择继承常用的代码风格，包括[Airbnb](https://github.com/doasync/eslint-config-airbnb-standard)风格、[Standard](https://github.com/standard/eslint-config-standard)和[Google](https://github.com/google/eslint-config-google)风格，我们可以选择适合我们团队的风格。比如选择Standard风格，最终生成的`.eslintrc.js`配置文件如下：

```js
module.exports = {
  env: {
    browser: true,
    es6: true
  },
  extends: [
    'standard'
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly'
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module'
  },
  rules: {
  }
}
```

这样我们就可以通过ESLint让团队成员维护项目代码时，风格保持一致了。

我们添加了新的Standard风格，再次运行`npm run lint`，发现这次报了比较多的错误：

```bash
  1:5   error  'message' is never reassigned. Use 'const' instead  prefer-const
  1:15  error  Strings must use singlequote                        quotes
  1:29  error  Extra semicolon                                     semi
  2:21  error  Extra semicolon                                     semi
  2:22  error  Newline required at end of file but not found 
```

ESLint报的错误一共5条：

- `message`变量没有被再次赋值，应当使用`const`声明。
- 字符串应该用单引号
- 两条语句多余分号（Standard采用semiless风格，不主动写分号）。
- 文件最后保留一个空行

我们可以根据提示信息一一修复它们，但是我们有一个更简单的方法，在`script`字段中添加如下配置：

```json
  "lint:fix": "eslint './**/*.js' --fix",
```

<!-- ```json
{
  "name": "app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "lint:init": "eslint --init",
    "lint": "eslint './**/*.js'",
    "lint:fix": "eslint './**/*.js' --fix",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "eslint": "^6.8.0",
    "eslint-config-airbnb-base": "^14.0.0",
    "eslint-config-standard": "^14.1.0",
    "eslint-plugin-import": "^2.20.1",
    "eslint-plugin-node": "^11.0.0",
    "eslint-plugin-promise": "^4.2.1",
    "eslint-plugin-standard": "^4.0.1"
  }
}
``` -->

它表示让ESLint自动修复问题。然后，我们只需要在命令后运行`npm run lint:fix`，就能自动修改书写中的错误了。

最后，我们的代码被修复为：

```js
const message = 'Hello world!'
console.log(message)

```

我们也可以根据需要，在`.eslintrc.js`的`rules`字段中修改我们自己喜好的规则，这些规则会覆盖`standard`定义好的默认规则。比如，如果我们希望在语句末尾添加分号，可以在`.eslintrc.js`文件中添加这个规则：

```js
rules: {
  semi: ['error', 'always'],
}
```

<!-- ```js
module.exports = {
  env: {
    browser: true,
    es6: true
  },
  extends: [
    'standard'
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly'
  },
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: 'module'
  },
  rules: {
    semi: ['error', 'always'],
  }
}
``` -->

这样我们再执行`npm run lint`时，又会出现下面这个错误：

```bash
  1:31  error  Missing semicolon  semi
  2:21  error  Missing semicolon  semi

✖ 2 problems (2 errors, 0 warnings)
```

我们可以再次运行`npm run lint:fix`来修复它们。最终代码被修改如下：

```js
const message = 'Hello world!';
console.log(message);

```

除了NPM命令外，ESLint还能被VSCode等常用编辑器支持，这些编辑器能够直接在开发的时候给出语法提示，这样就帮助我们写出符合规范的代码来。

所以，在团队开发的时候，应当养成使用ESLint的习惯，创建项目后，第一个安装和初始化的模块就应当是`eslint`。

这个故事主要让你了解了如何在工具层面规范开发者的代码书写，下一个故事，我们来聊聊规范化的另一个内容：统一开发版本。

## 第二个故事：使用Babel向下兼容

JavaScript大部分的使用场景是在浏览器环境中。因为Web的开放性，用户使用的浏览器版本也很多种。最新的浏览器几乎支持所有最新的JavaScript语言特性，而一些比较旧的浏览器，则可能只支持比较旧版本的JavaScript语言特性。在过去，前端开发者面临两难选择，要么放弃使用新的语言特性书写代码，要么放弃支持一部分使用旧浏览器的用户。但是现在，有了Babel这样的编译工具，情况得到了改变。

Babel是一个JavaScript编译器，它能把新的JavaScript语言版本编译为旧版本，这样我们开发者在进行Web开发的时候，就可以使用最新的语法特性，同时又能兼顾使用老版本浏览器环境的用户了。这样就能保证一个公司内部中的每个项目中使用的JS版本是一样的，降低各项目的维护成本。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8267b59bdb4b4d529c33e837f669a9c1~tplv-k3u1fbpfcp-zoom-1.image)

如上图，左边是编译前的代码，右边是编译后的代码（编译的目标版本是ES5）。

下面，我们就来学习一下如何使用Babel工具。

### 安装Babel

Babel是NPM模块，安装Babel通常需要装好几个库。

我们按照下面的NPM命令来安装：

```bash
npm install --save-dev @babel/core @babel/cli @babel/preset-env
```

`@babel/core`是Babel的核心库，`@babel/cli`是Babel的命令行工具，`@babel/preset-env`是Babel默认的预设环境。

要在运行时兼容老版本的浏览器，我们还要安装一个`core-js v3`模块，这个模块要安装在发布依赖，而不是开发依赖下。

```bash
npm install --save core-js@3
```

💡`npm install`命令的参数`--save-dev`表示在安装模块的同时将模块信息写到`package.json`的`devDependencies`字段，而`--save`参数则表示写到`dependencies`字段。两者的区别是，如果我们将代码发布到NPM，用户通过`npm install <包名>`安装我们的代码时，`devDependencies`字段中的模块并不会被安装，只有用户将我们的代码clone下来，进行改动时，才会安装`devDependencies`中的依赖。

因为`@babel/core`、`@babel/cli`、`@babel/preset-env`只有开发者编译代码时有用，使用模块的人直接使用编译好的代码，所以并不要使用这三个模块。而`core-js`是在运行时为老版本的浏览器提供不支持的API的实现的，所以使用模块的时候要加载它。因此前者用`--save-dev`安装，后者用`--save`安装。同样，前一节我们的`eslint`也是对开发者有用，使用者并不关心，所以也用`--save-dev`安装。

安装好了Babel后，我们在项目目录下创建一个配置文件`.babelrc`，这是一个JSON文件，我们配置如下：

```json
{
  "presets": [
    [
      "@babel/env",
      {
        "targets": "> 0.25%, not dead",
        "useBuiltIns": "usage"
      }
    ]
  ]
}
```
我们先来分析一下这段配置：

`@babel/env`表示预设支持当前版本所能支持的所有JavaScript的正式标准。

` "targets": "> 0.25%, not dead"`表示编译后的目标，这里设置为目前市场占有率高于`0.25%`且依然在维护中（not dead）的浏览器。这个选项包括了较多早期的浏览器，这些浏览器不支持ES6的语法。

`"useBuiltIns": "usage"`表示Babel会根据我们实际用到的API以及编译目标的浏览器兼容性，从`core-js`中按需添加需要的`polyfill`。

`"corejs": 3`表示使用`core-js`的`3.x`版本（默认是使用2.x版本）。

然后，我们在项目中创建一个src目录，修改上一节中的`index.js`文件，并将它移至`src`目录下，内容为：

```js
class Foo {
  bar () {
    return 'bar';
  }
}

const f = new Foo();
console.log(f.bar());

```

然后在package.json文件中的`scripts`字段中添加`compile`命令:

```json
  "scripts": {
    // ..省略其他的设置...
    "compile": "babel src -d lib",
  },
```

`"compile": "babel src -d lib"`表示在compile命令中执行babel，将src目录的所有JS文件编译后，输出到lib目录。

运行compile命令：

```bash
npm run compile
```

这时，我们会发现项目下多了lib目录，其中的index.js文件内容如下：

```js
"use strict";

function _classCallCheck(instance, Constructor) { ... }

function _defineProperties(target, props) { ...}

function _createClass(Constructor, protoProps, staticProps) { ... }

var Foo =
/*#__PURE__*/
function () {
  function Foo() {
    _classCallCheck(this, Foo);
  }

  _createClass(Foo, [{
    key: "bar",
    value: function bar() {
      return 'bar';
    }
  }]);

  return Foo;
}();

var f = new Foo();
console.log(f.bar());
```

上面的这段代码是经过Babel编译后的代码。它将ES6的代码编译成ES5的代码。因为老版浏览器不支持ES6的Class语法，所以Babel将它编译成function，这样就能让ES6的代码运行在老版本的浏览器上了。
<!-- 这个输出的代码，是Babel编译好的，支持老版本浏览器的代码。因为我们在Babel的配置里面指定了预设(presets)字段： -->
<!-- `@babel/env`表示预设支持当前版本所能支持的所有JavaScript的正式标准。

` "targets": "> 0.25%, not dead"`表示编译后的目标，这里设置为目前市场占有率高于`0.25%`且依然在维护中（not dead）的浏览器。

`"useBuiltIns": "usage"`表示Babel会根据我们实际用到的API以及编译目标的浏览器兼容性，从`core-js`中按需添加需要的`polyfill`。

`"corejs": 3`表示使用`core-js`的`3.x`版本（默认是使用2.x版本）。 -->

<!-- 因为`"targets": "> 0.25%, not dead"`这个选项包括了较多早期的浏览器，这些浏览器不支持ES6的class语法，所以这个配置，我们的目标代码就被编译成了ES5的版本。 -->

我们可以修改`targets`，让我们的代码运行在我们需要的浏览器上：

```json
{
  "presets": [
    [
      "@babel/env",
      {
        "targets": {
          "chrome": 49
        },
        "useBuiltIns": "usage",
        "corejs": 3
      }
    ]
  ]
}
```

我们将`targets`设为`"chrome": 49`，那么它会编译成chrome 49所支持的目标代码。再次执行`npm run compile`。

这次得到的 `lib/index.js` 长这样：

```js
"use strict";

class Foo {
  bar() {
    return 'bar';
  }

}

const f = new Foo();
console.log(f.bar());
```

我们看到，除了添加了一行`"use strict"`之外，基本上代码没有任何区别。这是因为`chrome 49`已经支持了class语法。

我们继续修改`src/index.js`：

```js
class Foo {
  bar () {
    return 'bar';
  }
}

const f = new Foo();
console.log(f.bar());

console.log(10 ** 3);

```

我们增加了`console.log(10 ** 3)`这行代码，再次运行`npm run compile`，然后查看`lib/index.js`，我们看到现在的代码是这样的：

```js
"use strict";

class Foo {
  bar() {
    return 'bar';
  }

}

const f = new Foo();
console.log(f.bar());
console.log(Math.pow(10, 3));
```

因为`chrome 49`不支持乘方操作符`**`，所以`10 ** 3`被编译成了`Math.pow(10, 3)`。

除了上面所提到的这些，Babel还有许多配置项和用法，更详细的用法可以参考[Babel官网](https://www.babeljs.cn/)。

总之，有了Babel之后，我们就可以将JavaScript代码编译成任何我们需要的目标版本，这样我们在使用JavaScript写代码的时候就可以放心使用最新的语言特性而不用担心浏览器兼容性问题了。

解决了兼容问题，我们再来思考另一个问题。通常情况下，对于较复杂的Web应用，我们会采用模块化的开发方式，无论是早期Node.js的CommoneJS规范还是ECMAScript最新的ES Module规范都提供了规范的模块加载机制。但是，早期的浏览器却不支持模块的加载，而且现在大部分网站依然是HTTP1.1，除了模块加载外，我们还需要考虑减少HTTP请求的数量。这就要求我们的代码在开发到最终上线的环节还需要解决两个问题：
- 一个是模块加载和管理的问题；
- 另一个是将多个模块文件打包合并成单一文件发布上线的问题。

那么，上述两个问题可以通过什么工具来解决呢？

## 第三个故事：使用Webpack打包和发布

上两个故事中，我们介绍了规范化的工具解决方案，这个故事，我们就来看看自动化打包工具。

在较大规模的Web应用场景中，JavaScript代码会使用比较多，逻辑也比较复杂，而且要多人协作开发，分模块是一个强需求。

最新的浏览器是支持`ES Module`规范的，我们可以用浏览器提供的原生模块机制，实现模块的加载：

```html
<script type="module">
  import {Foo} from '/foo.js';
  const f = new Foo();
  console.log(f.bar());
</script>
```

我们把`script`标签的`type`设为`module`，告诉浏览器这是一段支持`ES Module`的脚本。这样，在这段脚本中，我们才可以使用`import`去加载其他模块。这条语句（`import {Foo} from '/foo.js'`）表示浏览器就会根据网站根目录自动加载对应的`/foo.js`脚本文件。

但是，稍早一些的浏览器不支持`ES Module`，这时候就需要我们的打包工具了。打包工具它解决两个问题： 
1. 根据import关键字，将项目中上所有用到的模块都合并到一个JS文件中。除了JS文件，它还能打包Web项目中的其它的静态资源，比如：html、css、图片等。
1. 减少http请求，提上加载速度

现在比较流行的打包工具有Webpack、Rollup、Gulp等等，一般选择一种就可以，在这里我们选择Webpack。

同样，我们需要在Node环境安装Webpack模块：

```bash
npm install --save-dev webpack webpack-cli webpack-dev-server babel-loader
```

在这里我们安装了四个模块：
- `webpack`：`webpack`核心模块
- `webpack-cli`：命令行
- `webpack-dev-server`：开发服务器
- `babel-loader`：`webpack`集成`babel`编译的加载器。

有了webpack之后，我们要添加webpack的配置文件，它是一个js文件。我们在项目目录下创建一个`webpack.config.js`文件。它的内容如下：

```js
const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'app.js'
  }
};
```

`entry`字段指定了入口文件，这里是`./src/index.js`，`output`字段指定打包后的文件的输出目的地，这里是输出到当前项目的`dist`目录下的`app.js`文件。

我们在`package.json`文件中添加一个命令：

```json
"scripts": {
  // ...省略其他配置...
  "build": "webpack"
},
```

我们添加了build命令，运行它：

```bash
npm run build
```

这样我们得到一个`dist`目录和一个打包后的`app.js`文件。

打包的过程中，控制台上会有一段警告信息：

```bash
ARNING in configuration
The 'mode' option has not been set, webpack will fallback to 'production' for this value. Set 'mode' option to 'development' or 'production' to enable defaults for each environment.
You can also set it to 'none' to disable any default behavior. Learn more: https://webpack.js.org/configuration/mode/
```

这是因为我们没有配置webpack的打包模式。webpack支持`development`、`production`和`none`三种模式。现在我们不指定模式，文件默认会被以`production`模式打包。在production模式下，JS脚本会被压缩成一行以减小体积，你打开`dist/app.js`文件就会看到脚本被压缩成了一行。

### env.mode

为了让Webpack能够以不同的模式进行打包，我们需要在`webpack.config.js`文件中增加`mode`设置：

```js
const path = require('path');

module.exports = function (env = {}) {
  return {
    mode: env.mode,
    entry: './src/index.js',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'app.js'
    }
  };
};
```

然后修改`package.json`中的脚本命令：

```json
"scripts": {
  // ...省略其他配置...
  "build": "webpack --env.mode=none",
  "build:dev": "webpack --env.mode=development",
  "build:prod": "webpack --env.mode=production",
},
```

我们用三个命令`build`、`build:dev`和`build:prod`表示以三种不同的模式打包我们的JS代码。

我们现在再运行一下`npm run build`这时候将以`env.mode=none`的方式进行打包，代码将不再被压缩成一行，我们看到打包后的代码是这样的：

```js
/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
...
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ (function(module, exports) {

class Foo {
  bar () {
    return 'bar';
  }
}

const f = new Foo();
console.log(f.bar());

console.log(10 ** 3);


/***/ })
/******/ ]);
```

前面有一堆被省略掉的代码是Webpack打包的时候添加的，用来正确载入模块的代码。后面一部分是我们原始代码，也就是`src/index.js`中的代码。不过我们看到，这部分代码依然是和我们原来写的一样，如果我们要将它编译成兼容旧版本，同时打包，就需要`Babel`的配合。我们前面安装的`babel-loader`就是用来做这个事情的。

我们修改一下`webpack.config.js`，添加一下loader：

```js
const path = require('path');

module.exports = function (env = {}) {
  return {
    mode: env.mode,
    entry: './src/index.js',
    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: 'app.js'
    },
    module: {
      rules: [
        {
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: 'babel-loader'
          }
        }
      ]
    }
  };
};
```

我们给webpack增加模块（module）配置，规则是匹配所有的 js 文件，但是不包括`node_modules`目录中的文件。因为我们安装的第三方模块通常是编译过的，`use`字段表示要使用的`loader`，这里是`babel-loader`。

为了区分得更明显，我们将`.babelrc`的配置改回以下配置：

```json
{
  "presets": [
    [
      "@babel/env",
      {
        "targets": "> 0.25%, not dead",
        "useBuiltIns": "usage",
        "corejs": 3
      }
    ]
  ]
}
```

这样，再次运行`npm run build`，我们会看到，打包后的代码将变成：

```js
... // 省略前面 Webpack 添加的代码
/***/ (function(module, exports) {

function _classCallCheck(instance, Constructor) { ... }

function _defineProperties(target, props) { ... }

function _createClass(Constructor, protoProps, staticProps) { ... }

var Foo =
/*#__PURE__*/
function () {
  function Foo() {
    _classCallCheck(this, Foo);
  }

  _createClass(Foo, [{
    key: "bar",
    value: function bar() {
      return 'bar';
    }
  }]);

  return Foo;
}();

var f = new Foo();
console.log(f.bar());
console.log(Math.pow(10, 3));

/***/ })
/******/ ]);
```

这样，我们看到`src/index.js`被编译成ES5的代码了。

现在我们修改一下`src`下的文件，把它分成两个文件，新建一个`foo.js`：

```js
export default class Foo {
  bar () {
    return 'bar';
  }
};

```

然后把`index.js`改成：

```js
import Foo from './foo';

const f = new Foo();
console.log(f.bar());

console.log(10 ** 3);

```

我们先运行一下之前的Babel编译命令：`npm run compile`。

我们会看到现在的lib目录下面也是两个文件，一个`foo.js`和一个`index.js`。也就是说，Babel会将src目录下的所有文件一一对应编译到lib下，但是它并不会合并文件。

而我们再运行`npm run build`。

会发现，生成的`dist/app.js`文件内容和之前一个文件时的一样，也就是说，webpack将两个文件打包在了一起。

最后，还有一个问题，我们刚才还安装了一个`webpack-dev-server`，这个脚本又是做什么用的呢？

因为我们现在有了webpack打包工具，所以我们已经可以生成`app.js`这个文件，然后我们可以创建应用来使用`app.js`，或者创建例子来测试它。但是，如果我们在开发中每次一修改原始的src目录中的文件，都要打包一次去更新`app.js`，那样会非常麻烦，开发和测试起来很不方便。`webpack-dev-server`提供了一个可以热更新修改原始文件，立即更新`app.js`的机制，并且它自身是一个web服务器，方便我们开发调试。

我们现在配置一下`webpack-dev-server`，修改`webpack.config.js`文件：

```js
const path = require('path');

module.exports = function (env = {}) {
  return {
    // ...省略其它设置...
    devServer: {
      contentBase: path.join(__dirname, env.server || '.'),
      port: 9090,
      hot: true
    }
  };
};
```

我们添加了一个`devServer`配置，`contentBase`是`http server`运行的目录，我们可以通过`env.server`来指定，`port`是运行端口，我们将它设为9090，`hot`设为`true`，那么一旦src下的内容被修改，`app.js`将自动更新。

接下来我们在项目目录下创建一个example子目录，添加index.html文件：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script src="app.js"></script>
</body>
</html>
```

我们再修改package.json文件，添加一个命令：

```json
"scripts": {
  // ...省略其它配置...
  "dev": "webpack-dev-server --env.server=example",
},
```

我们添加了一个`dev`命令，执行`webpack-dev-server --env.server=example`，现在我们运行它：

```bash
npm run dev
```

这样我们就启动了webpack-dev-server的web服务器，打开浏览器，访问`localhost:9090`就可以看到我们的页面。打开开发者工具，控制台上现在输出的信息是`bar`和`1000`。

回到`src/index.js`文件，我们把`console.log(10 ** 3);`修改为`console.log(20 ** 3);`，再切换回浏览器窗口，我们看到控制台的输出信息变成了`bar`和`2000`。这是因为`webpack`自动更新了`app.js`文件。

至此，webpack打包的简单配置就基本上完成了。这时，我们已经创建了一个完整的开发环境，可以开始我们的项目开发了。

`webpack`还有许多高级的功能，以及不同的loader，不仅仅能够打包JS文件，还可以打包CSS、静态资源和HTML文件，在许多web项目中，我们会配置`webpack`将各种文件打包到一起，最终整体发布，这样线上代码的体积最小，而且HTTP请求数也大大减少。

关于`webpack`的更多功能和示例，可以参考[webpack官网](https://webpack.js.org/)。

### 小结

最后总结一下，在一个通用的项目开发环境中，我们使用ESLint来进行代码提示，从而统一代码风格，提升项目的代码质量；使用Babel来编译代码以兼容旧版本，从而让我们能够使用最新的语言特性来开发项目，以提高开发效率，提升项目的可维护性；使用Webpack来完成代码的打包，解决浏览器不能支持CommonJS和ES Module模块化规范的问题，将我们的项目代码从开发环境转变为可发布到线上的最终代码。

ESLint到Babel到Webpack，这是最基础的工程化工具集，除此以外，还有其他的工具以解决其他问题，比如单元测试的工具、持续集成（CI/CD）的工具等等，这些工具最终的目的都是让我们的开发变得更高效和可靠，项目的代码质量和可维护性得到提升，而这是实际项目开发和团队协作不可或缺的。因此前端工程化方法和相应的工具集，对于优秀的前端工程师，也是必修课，必须要好好掌握。

本课程限于篇幅，我们只是最粗浅地介绍了这些工具的使用，真正发挥不到这些工具能力的十分之一。如果你有兴趣，可以到各自的官网自行学习。

## 11.实例完整代码展示

本课程中有很多实例，这些实例的完整代码都在下面的这个 GitHub 链接里面了

**代码链接：https://github.com/junyux/FE-Advance**

## 2.第二日：让 CSS 做更多的事情

# 第二天

通过第一天的故事，我们了解了元素的class属性可以用来定义元素的某种业务状态或者业务模式，然后通过CSS的类选择器根据业务需求将元素设置成对应的样式，从而避免了将这些本该由CSS完成的任务交由JS完成，保持了HTML、CSS、JS各司其职的原则。

其实，CSS的职责是负责定义元素如何展现，页面上所有元素的样式不管是依赖业务需求还是静态的，都要尽可能的交由CSS来完成。作为初级前端工程师的你可能觉得这有点夸张，但其实CSS还是非常强大的，它可以完成更多的事情。所以，今天的内容将带你了解一下CSS强大的功能，希望它能启发你打开前端开发的新思路。

## 树形结构与三角标

<!-- **用好JS只是前端工程师进阶的第一步，用好CSS才是前端工程师进阶的标志。** -->

同样，我们也是通过一个实际例子来说明。这个任务是实现一个树形展开的列表，大概的界面是如下形式：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1a0ba30ff414e76bee05d08210a9b03~tplv-k3u1fbpfcp-zoom-1.image)

实现这张页面的HTML很简单， 如下代码所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>树UI</title>
</head>
<body>
  <ul class="tree">
    <li>项目1</li>
    <li>项目2</li>
    <li class="expand">项目3
      <ul>
        <li>子项3.1</li>
        <li>子项3.2</li>
        <li>子项3.3</li>
      </ul>
    </li>
    <li>项目4
      <ul>
        <li>子项4.1</li>
        <li>子项4.2</li>
      </ul>
    </li>
    <li>项目5</li>
  </ul>
</body>
</html>
```

页面的HTML结构非常容易，但是我们却遇上了难题。因为浏览器上列表元素默认的样式是小圆点，而不是小三角。那么这个小三角的样式该如何实现呢？

最直接的做法是：给每个`<li>`元素的`list-style`属性设置一张图片：

```css
html, body {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}

ul {
  list-style: url("https://p5.ssl.qhimg.com/t018438001db494c5f3.png");
}

li.expand {
  list-style: url("https://p4.ssl.qhimg.com/t0167b045701562f010.png")
}
.tree li > ul {
  display: none;
}

.tree li.expand > ul {
  display: block;
}
```

如上代码所示：默认情况下，列表元素的`list-style`属性被设置为右三角图标，当`<li>`元素的`class`属性被设置为`expend`的时候，将该`<li>`元素的`list-style`属性设置成下三角图标。这样就达到了设计图的效果。

这样做虽然实现了需求，但是我们发现，这样做有几个缺点：

- 第一，因为`list-style`属性不能设置图片的大小，所以，我们必须根据元素里的文字大小事先设定图标的大小。如果将来文字大小改变了，那么图标的大小也需要跟着调整。

- 第二，因为要下载图片，所以多了一些HTTP请求，HTTP请求多，网页的性能就比较差

所以，通过图片的方式改变列表的样式非常不灵活而且还很消耗性能。那么，还有没有其他的更加高效且灵活方式可以实现同样的效果呢？

## 第二个故事：用CSS实现三角标

如果不使用图片定制列表元素的样式，还有没有其他的方法定制呢？有。我们可以利用伪元素和CSS的border属性来绘制小三角。

我们先来了解一下border属性的特点。看一个简单的例子，我们定义了一个div元素：

```html
  <div id="block"></div>
```

然后，我们给这个`<div>`元素设置了宽，高和上下边框：

```css
#block {
  width: 100px;
  height: 50px;
  border-top: solid 10px;
  border-bottom: solid 10px;
  background-color: #ccc;
}
```

正常情况下，你可能会凭直觉认为，直角border应该是直线，而在只有一边或者平行两边border的情况下确实如此：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a4c989b265f48ecb737cf14bc89d61e~tplv-k3u1fbpfcp-zoom-1.image)

上图中，上下两条黑色边就是block元素的上下边框。

但是，如果我们将上面的上下边框修改为相邻两边（即：上边框和右边框）的情况的呢：

```css
#block {
  width: 100px;
  height: 50px;
  border-top: solid 10px blue;
  border-right: solid 10px;
  background-color: #ccc;
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87af2c94f7884351be11aeb80698a4db~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示，我们看到`border-top`和`border-right`交界的地方是一个斜角。

如果我们再修改一下上面的CSS代码，将它4条边框分别设置为不同的的颜色：

```css
#block {
  width: 100px;
  height: 50px;
  border-top: solid 10px blue;
  border-right: solid 10px green;
  border-bottom: solid 10px red;
  border-left: solid 10px;
  background-color: #ccc;
}
```

它的效果是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/153d3ec2c06f4e6f940f123296f5a4b8~tplv-k3u1fbpfcp-zoom-1.image)

这时，如果我们把这个div元素的宽高都设置为0，会出现怎样的效果呢？

```css
#block {
  width: 0px;
  height: 0px;
  border-top: solid 10px blue;
  border-right: solid 10px green;
  border-bottom: solid 10px red;
  border-left: solid 10px;
  background-color: #ccc;
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75ea54e8dcdd4c3ca5efdf76da0e11d6~tplv-k3u1fbpfcp-zoom-1.image)

这时，你会发现block元素的四个边框缩成了4个小三角形。如果我们将上、右、下的边框都隐藏起来，那么不是我们需要的小三角形的效果吗？

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d341ad921ccc4addbb218d3590e7adeb~tplv-k3u1fbpfcp-zoom-1.image)

如果我们希望得到不同角度的三角形，我们还可以改变相邻的border的宽度，比如我们要得到正三角形，我们可以将上下边框（`border-top`）和左右边框（`border-left`）的比例维持在1比根号3。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6e43d1f72c140fea8c5c8ed22fffc6e~tplv-k3u1fbpfcp-zoom-1.image)

现在，我们来修改`<li>`元素的CSS样式：

```css
.tree li::before {
  color: #999;
  content: '';
  display: inline-block;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 6px 10.4px;
  border-color: transparent;
  border-left-color: currentColor;
  transform: translateX(6px);
}
```

上面的代码，我们使用`li`元素的`::before`伪元素来绘制小三角。我们来分析一下这段CSS规则：

- `border-width: 6px 10.4px`表示将这个伪元素的上下边框设置为6px，左右边框设置为10.4px

- `border-color: transparent`表示将这个伪元素的4个边框的颜色设置为透明色

- `border-left-color: currentColor`表示将这个伪元素的左边框的颜色设置为当前元素的文字颜色

- `transform: translateX(6px)`表示将这个伪元素向右偏移6px, 这样使得这个小三角和列表项的文字中间的间隔不至于太宽

这时的页面效果就是下面这样：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de6891ae64a24204aeb8600dd028adc6~tplv-k3u1fbpfcp-zoom-1.image)

根据需求，当列表中的子列表项被展开的时候，它前面的右三角要变成向下的三角。这个只要通过调整transform属性，对`::before`伪元素进行旋转就能实现：

```css
.tree li.expand::before {
  transform: rotate(90deg) translateX(6px) ;
}
```

所以最终，得到树形UI的完整效果代码：

[在线演示](https://junyux.github.io/FE-Advance/day02/index1-v2.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>树UI</title>
  <style>
  html, body {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
  }

  ul {
    list-style: none;
  }

  .tree li::before {
    color: #999;
    content: '';
    display: inline-block;
    width: 0;
    height: 0;
    border-style: solid;
    border-width: 6px 10.4px;
    border-color: transparent;
    border-left-color: currentColor;
    transform: translateX(6px);
  }

  .tree li.expand::before {
    transform: rotate(90deg) translateX(6px) ;
  }

  .tree li > ul {
    display: none;
  }

  .tree li.expand > ul {
    display: block;
  }
  </style>
</head>
<body>
  <ul class="tree">
    <li>项目1</li>
    <li>项目2</li>
    <li class="expand">项目3
      <ul>
        <li>子项3.1</li>
        <li>子项3.2</li>
        <li>子项3.3</li>
      </ul>
    </li>
    <li>项目4
      <ul>
        <li>子项4.1</li>
        <li>子项4.2</li>
      </ul>
    </li>
    <li>项目5</li>
  </ul>
</body>
</html>
```

使用border来绘制三角形是一种比较简单的效果，但它代表一种使用CSS绘制UI的思路，延续这种思路，我们还可以绘制其他比较复杂的图形，比如：

```html
<div class="icon star"></div>
<div class="icon arrow"></div>
<div class="icon pacman"></div>
```

```css
.icon {
  display: inline-block;
  width: 0;
  font-size: 0;
  position: relative; 
  margin-right: 20px;
}

.star {
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-bottom: 100px solid red;
}

.star::after {
  border-left: 50px solid transparent;
  border-right: 50px solid transparent;
  border-top: 100px solid red;
  position: absolute;
  content: "";
  top: 30px; left: -50px;
}

.arrow {
  width: 40px;
  height: 40px;
  margin: 0 40px;
  background-color: red;
}

.arrow::before {
  position: absolute;
  left: -40px;
  border: solid 20px red;
  border-left-color: transparent;
  content: "";
}

.arrow::after {
  position: absolute;
  right: -40px;
  border: solid 20px transparent;
  border-left-color: red;
  content: "";
}

.pacman {
  width: 0px; height: 0px;
  border-right: 40px solid transparent;
  border-top: 40px solid red;
  border-left: 40px solid red;
  border-bottom: 40px solid red;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
  border-bottom-left-radius: 40px;
  border-bottom-right-radius: 40px;
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f57d56a4c2db4c4caa5058f0c9e2ae61~tplv-k3u1fbpfcp-zoom-1.image)

上面的代码分别实现了六角星、箭头和吃豆人图案。[在线演示](https://junyux.github.io/FE-Advance/day02/index1-ex.html)

CSS的border能够实现的图案还有很多，其思路和三角形并没有什么本质的区别。如果再加上box-shadow等其他属性，能实现的效果就更多了。

<!-- 对于小李来说，在项目中需要学会且熟练运用这样的思路，能够用CSS实现更多的效果，这也是成为高级前端工程师的必经之路。 -->

附：

上面的例子是一个静态的树状列表，如果我们要实现列表项的展开和收起该如何实现呢？

因为展开状态的列表项被定义为`class=expend`。所以，我们可以给状态是expend的`li`元素和普通`li`元素分别设置对应的展示样式：

```css
  .tree li > ul {
    display: none;
  }

  .tree li.expand > ul {
    display: block;
  }
```

如上代码所示，第一条规则表示隐藏普通状态的`li`元素下的子元素。第二表规则表示，显示状态为`expend`的`li`元素下的子元素。

然后，修改我们的JS代码，让`li`元素在展开和隐藏状态间切换：

```js
const tree = document.querySelector('.tree');

tree.addEventListener('click', (evt) => {
  if(evt.target.tagName === 'LI') {
    if(evt.target.className === 'expand') {
      evt.target.className = '';
    } else {
      evt.target.className = 'expand';
    }
  }
});
```

这样就实现了一个动态展开收起的树状列表。[在线演示](https://junyux.github.io/FE-Advance/day02/index1-v3.html)

## 第三个故事：用CSS绘制静态饼图

了解了border属性的特性后，我们将利用这个特性，完成一个更加复杂的任务。这个任务是这样的：要在网页上显示四张图表，这是一个数据统计图表里常见的饼图，大概是如下这个样子：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/746762b99b824602a3bd88510b9f56ae~tplv-k3u1fbpfcp-zoom-1.image)

关于上图的这个效果，我们可以通过比较复杂的HTML结构加上一些JS来完成这个工作。但是如果考虑到代码可维护性，像这样纯UI的工作最好交由CSS完成，让HTML元素尽量保持简洁，比如，保持一个简单的HTML标签：

```html
<div class="pie">25%</div>
```

💡在一个项目里，通常HTML结构保持越简单，项目的JS代码也会相应简洁，代码的可维护性就会大大增强。所以，保持HTML结构简单，尽量不增加冗余标签，是每个前端工程师必须要思考并努力去做到的。

那么，如何使用CSS实现饼图的效果呢？比较直接的思路是采用颜色拼接和旋转来实现。

首先，我们先实现一个单色饼图。这个效果非常容易实现，可以使用CSS的`border-radius`属性将元素的边框四角分别设置为1/4圆弧，如下代码所示：

```html
<div class="pie"></div>
```

```css
.pie {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: #3c7;
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/606da9a1c9d34d5aab17f0338ff368df~tplv-k3u1fbpfcp-zoom-1.image)

在这里，为了方便描述，我们暂时把HTML元素中的文字去掉，因为它的显示有些问题需要解决，后续我们再来讨论它。

有了单色饼图，那么双色饼图该怎么做呢？还记得上一个故事里我们使用border来做三角形和其他有趣图案吗？结合border-radius，我们可以将三角形变成扇形！

```css
.pie {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: #3c7;
  border: solid 10px;
  border-color: red blue orange green;
  box-sizing: border-box;
}
```
上面的代码中，我们先给`.pie`元素的上、右、下、左边框设置不同颜色，以及边框大小10px。它的效果如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63e68b35f3994e7c8860516c7b1bd7dc~tplv-k3u1fbpfcp-zoom-1.image)

然后，我们将元素的width、height属性都修改为0，并将border的大小设置为75px：

```css
.pie {
  display: inline-block;
  width: 0;
  height: 0;
  border-radius: 50%;
  border: solid 75px;
  border-color: red blue orange green;
  box-sizing: border-box;
}
```

这时`.pie`元素的效果就是下面这个样子——四个扇形：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dd2f2b762f14d5ebcde4b0f1eac9ca6~tplv-k3u1fbpfcp-zoom-1.image)

然后，再将上边框和右边框的颜色设置为绿色（#3c7），下边框和左边框的颜色设置为蓝色（#37c），如下代码所示：

```css
.pie {
  display: inline-block;
  width: 0;
  border-radius: 50%;
  border: solid 75px;
  border-color: #3c7 #3c7 #37c #37c;
  box-sizing: border-box;
}
```

这样，`.pie`元素就变成下面的样子：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dd8bbb776e784d2cad89392b9bbf1827~tplv-k3u1fbpfcp-zoom-1.image)

再通过`transform`属性将这个元素旋转45度：

```css
.pie {
  display: inline-block;
  width: 0;
  border-radius: 50%;
  border: solid 75px;
  border-color: #3c7 #3c7 #37c #37c ;
  box-sizing: border-box;
  transform: rotate(45deg);
}
```

这就得到我们要的两色饼图：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23d9311aab174204afbf8e8280c99d3d~tplv-k3u1fbpfcp-zoom-1.image)

<!-- 现在，我们需要思考的是：如何让两种颜色的面积随饼图百分比变化呢？ -->

现在，我们需要思考的是：如何让两种颜色，按照给定的进度数据，显示对应的比例呢？

它的基本思路是这样的： 

1. 在这个元素上叠加一层饼图；
1. 初始状态下，我们将这张饼图的右半边（即，上、右边框）的颜色设置为蓝色；左半边（即，下、左边框）的颜色设置为透明色。这样初始情况下，`.pie`元素右半边绿色的部分，被这一叠加层覆盖为蓝色，从视觉上看`.pie`元素此时的进度是0；
1. 根据需求，以不同角度旋转这个叠加层，这样就实现了不同百分比的饼图。

首先，叠加的饼图可以用**伪元素**来实现：

```css
.pie,
.pie::before {
  display: inline-block;
  width: 0;
  border-radius: 50%;
}

.pie {
  position: relative;
  border: solid 75px;
  border-color: #3c7 #3c7 #37c #37c;
  box-sizing: border-box;
  transform: rotate(45deg);
}

.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%);
}
```

如上代码所示，我们将`.pie::before`伪元素盖在`.pie`元素上，这个伪元素的border一半是透明色，一半是蓝色，恰好是`.pie`元素左边的颜色，那么这样饼图看起来又恰好是一个整圆了。

在`.pie::before`规则中，还需要注意的是这个声明——`transform: translate(-50%, -50%)`。因为元素的定位在元素边框（border-box）的左上角，而相对位置（0,0）则在元素内容区（content-box）的左上角。因为`.pie`元素的`width`和`height`都是0，所以content-box的左上角正好是`.pie`的中心点。因此要给伪元素设置一个向左向上各偏移50%的位置，才能恰好覆盖住`.pie`元素。

这时，这个元素的效果如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac3706b3379e44ea851244b72b0b0df2~tplv-k3u1fbpfcp-zoom-1.image)

然后，我们把伪元素旋转一个角度，比如转过10%，只要在伪元素的tranform属性上增加一个rotate，并让它的值等于`0.1turn`，如下代码所示：

```css
/*省略其他的CSS规则...*/

.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%) rotate(0.1turn);
}
```

在这里，为了看清楚，我把before伪元素的一半`border-color`暂时换成了红色，显示结果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d7a48877a964342aa457b74664281b7~tplv-k3u1fbpfcp-zoom-1.image)

好，我们把颜色换回来，这样就得到我们期望的结果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a36f45e45cd484880f9b8066bd20d92~tplv-k3u1fbpfcp-zoom-1.image)

所以，只要给这个伪元素设置不同的旋转角度，就能得到相应的统计饼图，如下图所示（为了看起来更清晰，我们把蓝色部分的伪元素颜色替换为了半透明的）：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79fca011cfa14b38a9eb9b788c9846b2~tplv-k3u1fbpfcp-zoom-1.image)

<!--
![](https://p3.ssl.qhimg.com/t012f63e6642b6c365a.gif)
-->

问题解决到这里，我们只解决了前半圈，也就是只能展示从`0%`到`50%`的进度表示，而超过`50%`的进度就行不通了。如下代码所示：

```css
.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%) rotate(0.6turn);
}
```

上面的代码中， 我们将伪元素旋转到`0.6trun`（也就是旋转了60%)，这时饼图变成下面这个样子：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54d0005e3a6a44d0ab1a70279294b5a9~tplv-k3u1fbpfcp-zoom-1.image)

这是因为我们的`.pie`元素只有右边一半是绿色，所以旋转超过了`50%`后，左边的蓝色区域就裸露了出来，这显然不是我们期望的结果。

要解决这个问题，我们需要调整伪元素的左右两半圆的颜色配置。初始情况下，我们将这个伪元素的下、左边框设置为透明，上、右边框设置为蓝色，即：左半圆是透明色，右半圆是蓝色。当旋转到`50%`时，伪元素的蓝色右半圆被旋转到`.pie`元素的左边，而透明的左半圆被旋转到`.pie`元素的右边。这时，我们只需要将原来是透明色的下、左边框设置为绿色，将原来是蓝色的上、右边框设置为透明色，就能解决超过上面的问题。

```html
<div class="pie convex"></div>
```

```css
.pie.convex::before {
  border-color: transparent transparent #3c7 #3c7;
}
```

如上代码所示，我们给超过50%进度的饼图元素加一个类选择器`convex`。在这个选择器里，我们将伪元素的上、右边框颜色设置为透明色，将下、左边框的颜色设置为绿色。

这样，超过50%进度的饼图就正常显示了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/284af822b63f4d6aa4018956a4ebcabf~tplv-k3u1fbpfcp-zoom-1.image)

到这里，基本上，我们可以使用CSS实现**静态**的饼图效果。比如，要实现最初的四张饼图，它们的代码如下所示：

[在线演示](https://junyux.github.io/FE-Advance/day02/index2-v1.html)

```html
<div class="pie one"></div>
<div class="pie two"></div>
<div class="pie three"></div>
<div class="pie convex four"></div>
```

```css
.pie,
.pie::before {
  display: inline-block;
  width: 0;
  border-radius: 50%;
}

.pie {
  position: relative;
  border: solid 75px;
  border-color: #3c7 #3c7 #37c #37c;
  box-sizing: border-box;
  transform: rotate(45deg);
}

.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%);
}
.pie.convex::before {
  border-color: transparent transparent #3c7 #3c7;
}
.pie.one::before {
  transform: translate(-50%, -50%) rotate(.1turn);
}

.pie.two::before {
  transform: translate(-50%, -50%) rotate(.25turn);
}

.pie.three::before {
  transform: translate(-50%, -50%) rotate(.5turn);
}

.pie.four::before {
  transform: translate(-50%, -50%) rotate(.8turn);
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0503b53ec6a4442d9d5d6b497f2d1df4~tplv-k3u1fbpfcp-zoom-1.image)

但是，通常情况下，我们的统计数据都是来自服务器，是动态而不是静态的，所以饼图的进度比例是需要动态绑定而不是写死在CSS中的。

这种情况下，按照常规做法，我们需要通过内联CSS的方式动态绑定进度数据，以显示对应比例的饼图。但是**伪元素**是无法通过内联的方式绑定，而且也不容易被JS操作。

💡伪元素不像普通的HTML元素，普通元素我们可以通过DOM拿到元素对象，然后操作它们的样式，伪元素如果非要用JS操作，我们只能操作CSS规则，那样非常繁琐。

那么如何实现动态绑定进度数据的饼图呢？

## 第四个故事： 绘制动态绑定进度的饼图

上一个故事中，我们使用CSS实现了静态的饼图效果。这一个故事，我们将实现动态绑定进度数据的饼图。

要动态绑定数据，我们需要将原本写死在CSS中的进度设置通过HTML的style属性来表示，也就是CSS的内联。因为伪元素是无法通过内联的方式绑定的。所以，我们需要将与进度相关的数据从伪元素的属性设置中移到元素的设置中。

<!-- 如果我们希望在HTML中通过属性来控制显示不同的任意进度的饼图，可以实现吗？ -->
<!-- 
答案是能，我们可以利用控制CSS动画来操作的伪元素的状态。 -->
所以，我们可以把伪元素上的CSS属性通过CSS动画结合它所属元素上的`animation-delay`属性来控制。

首先我们给饼图增加CSS动画：

```css
/*...省略其他的CSS规则...*/

.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%) rotate(.0turn);
  animation: spine 10s linear infinite,
    convex 10s step-end infinite;
}

@keyframes spine {
  to {transform: translate(-50%, -50%) rotate(1turn);}
}

@keyframes convex {
  50% {border-color: transparent transparent #3c7 #3c7;}
}
```

上面的代码中，我们给`.pie::before`伪元素添加了一个动画声明：

```css
animation: spine 10s linear infinite,convex 10s step-end infinite;
```
这条声明表示spine动画执行周期10秒，匀速执行，无限循环；convex动画执行10s，以step-end方式跳跃执行，无限循环。

_`step-end`是每一关键帧在动画进度的末尾改变属性状态；`linear`是每一关键帧在动画执行期间以播放时间均匀插值的方式改变属性状态_

```css
@keyframes spine {
  to {transform: translate(-50%, -50%) rotate(1turn);}
}
```
上面这条规则中，`@keyframes spine`表示声明spine帧动画。`to`是100%的缩写，表示动画完整周期结束时，元素的属性到达的状态。`transform: translate(-50%, -50%) rotate(1turn);`就是动画结束时`.pie::before`元素的状态为转过一圈，位置向左向上偏移50%。

```css
@keyframes convex {
  50% {border-color: transparent transparent #3c7 #3c7;}
}
```
这条规则表示，当动画执行到50%时，将`.pie::before`的状态修改为：`border-color: transparent transparent #3c7 #3c7;`。也就是当动画播放到50%时，将这个伪元素的边框的颜色修改为上、右边框为透明色，下、左边框为绿色。

这样，我们的饼图动画就如下图所示：

<!-- 上面的代码给饼图添加了两个关键帧动画，其中一个是旋转的，另一个是转到一半改变伪元素border颜色的，我们给动画设置了10s的周期，现在饼图动画如下图所示。 -->

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f544064b39624cda8955e425cb784a9f~tplv-k3u1fbpfcp-zoom-1.image)

有了变化的饼图，我们就可以通过`animation-play-state`和`animation-delay`将饼图设置为固定的比例：

<!-- 接着，我们可以通过`animation-play-state: paused`属性将动画暂停，然后通过设置`animation-delay`为负数时间，可以动画状态变更到对应的那一帧： -->

```css
.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%) rotate(.0turn);
  animation: spine 10s linear infinite,
    convex 10s step-end infinite;
  animation-play-state: paused;
  animation-delay: -3s;
}
```

如上代码所示:
- `animation-play-state: paused`表示暂停动画
- `animation-delay: -3s`表示将动画提前3秒执行，也就是说，动画初始的状态就在3s那一帧，即动画处于30%处，刚好对应进度为30%的饼图。

从上面的代码可以看出，我们可以通过控制`animation-delay`属性，设置饼图的比例。但是这个属性依然是设置在伪元素上的，而我们的程序又不能通过伪元素直接修改这个属性。那么我们可不可通过修改`.pie`元素的`animation-delay`属性来间接影响伪元素的状态呢？

答案是可以的。

因为，`animation-delay`属性可以设置为`inherit`值，这样，`animation-delay`属性值就会从父元素继承。而`.pie::before`是伪元素，伪元素总是被浏览器渲染为对应元素的子元素。

也就是说，我们只要将`.pie::before`伪元素的`animation-delay`设为`inherit`，然后将`animation-delay`值作为内联样式直接设置在`.pie`元素上，这样伪元素就能继承`.pie`元素上的`animation-delay`值了。

如下代码所示：

```css
.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%) rotate(.0turn);
  animation: spine 10s linear infinite,
    convex 10s step-end infinite;
  animation-play-state: paused;
  animation-delay: inherit;
}
```

这样，我们要显示刚才那四张饼图，就可以这么写：

```html
<div class="pie" style="animation-delay: -1s;"></div>
<div class="pie" style="animation-delay: -2.5s;"></div>
<div class="pie" style="animation-delay: -5s;"></div>
<div class="pie" style="animation-delay: -8s;"></div>
```

到这里，基本的动态绑定进度的饼图就实现了。

最后，我们需要处理饼图中的文字。因为我们用了0宽高的元素和border来实现饼图，所以我们无法直接将文字直接写在`.pie`元素中。这时，唯一的办法是，我们给文字套一层HTML标签（比如`<span>`），然后将它脱离出文档流：

```html
<div class="pie" style="animation-delay: -1s;"><span>10%</span></div>
<div class="pie" style="animation-delay: -2.5s;"><span>25%</span></div>
<div class="pie" style="animation-delay: -5s;"><span>50%</span></div>
<div class="pie" style="animation-delay: -8s;"><span>80%</span></div>
```
```css
.pie,
.pie::before {
  display: inline-block;
  width: 0;
  border-radius: 50%;
  font-size: 0; /* 纯粹防止空白符，这个例子中可以不添加这个设置*/
}

.pie span {
  font-size: 1rem;
  position: absolute;
  color: #fff;
  transform: translate(-50%, -50%) rotate(-45deg);
}
```

由于`.pie`元素有个45度的旋转，因此，我们要把文字反向旋转回来。

这是最终的效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca2466fdb90e4f67a1b96290dd478a55~tplv-k3u1fbpfcp-zoom-1.image)

完整CSS代码如下所示：

[在线演示](https://junyux.github.io/FE-Advance/day02/index2-v2.html)

```css
.pie,
.pie::before {
  display: inline-block;
  width: 0;
  border-radius: 50%;
  font-size: 0;
}

.pie span {
  font-size: 1rem;
  position: absolute;
  color: #fff;
  transform: translate(-50%, -50%) rotate(-45deg);
}

.pie {
  position: relative;
  border: solid 75px;
  border-color: #3c7 #3c7 #37c #37c;
  box-sizing: border-box;
  transform: rotate(45deg);
}

.pie::before {
  content: '';
  position: absolute;
  border: solid 75px;
  border-color: #37c #37c transparent transparent;
  transform: translate(-50%, -50%) rotate(.0turn);
  animation: spine 10s linear infinite,
    convex 10s step-end infinite;
  animation-play-state: paused;
  animation-delay: inherit;
}

@keyframes spine {
  to {transform: translate(-50%, -50%) rotate(1turn);}
}

@keyframes convex {
  50% {border-color: transparent transparent #3c7 #3c7;}
}
```

到此，动态绘制饼图效果就做出来。唯一有一些遗憾的是，最终我们需要增加一个内嵌span标签，没有遵守我们最初最简的HTML结构的期望。这是一个小遗憾，但这是因为采用border来实现效果带来的限制。

那么这个小遗憾可以解决吗？

## 第五个故事：饼图 2.0

第二个故事中，我们采用了元素的border属性的特性实现了饼图的效果。但是，这种方法让元素的border占满了元素的整个可视区，导致没有文字内容存放的空间，所以最后我们不得不增加一个额外的`<span>`标签来显示文字。这也是这种方法带来的缺点。这一讲，我们将学习另一种方法，实现饼图效果，并且不会增加额外的Html标签。

这种方法是利用CSS的**线性渐变**——`linear-gradient()`函数实现饼图的效果。

下面，让我们看一下使用`linear-gradient()`该怎么做，首先还是从纯色的圆形开始，我们给`background`增加一个线性渐变的效果：

```html
<div class="pie"></div>
```
```css
.pie {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(#37c,#3c7); 
}
```

如上代码所示，`background: linear-gradient(#37c,#3c7)`表示让`.pie`元素表现为一个从上到下颜色从绿色（#37c）均匀过渡到蓝色（#3c7）的背景。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10307ec74c8f4309a8affe9bde9290cb~tplv-k3u1fbpfcp-zoom-1.image)

上图中，绿色到蓝色的变化是均匀的在整个元素内渐变。而`linear-gradient`这个函数还允许设置渐变开始的位置。比如，我们可以把绿色开始渐变的位置设置在元素高度的50%的位置，而把蓝色开始渐变的位置也设置在50%的位置，那么这两个颜色刚好在50%的地方直接切换：

```css
.pie {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(#37c 50%,#3c7 50%);
}
```

如上代码所示：`background: linear-gradient(#37c 50%,#3c7 50%)`表示从起始位置开始到高度50%位置是绿色，然后从50%开始到结束是蓝色，而从50%到50%的地方则是绿色到蓝色的渐变范围。因为50%到50%并没有范围，所以渐变的部分就是一条分割线。它的效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d453402cef149f5aeff046c658d63d4~tplv-k3u1fbpfcp-zoom-1.image)

这样我们就得到一个双色的圆。这时，你可能很直接就想到使用transform属性对元素进行旋转90度。但是这里我们无需这样做，因为`linear-gradient`函数提供了渐变轴的参数。默认情况下，渐变轴是0度，渐变的方向是从下到上，也就是上图中的样子。我们可以通过将渐变轴修改为90度，实现左右渐变的效果：

<!-- 而且我们无需用transform来旋转`.pie`元素，因为我们可以直接给`linear-graident`设置一个角度： -->

```css
.pie {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
}
```
这时，我们将渐变轴顺时针旋转90度，于是我们就得到了与上一个版本相同的双色半圆形。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c69c9ade76dd49e6bc506ca35ae0ccb7~tplv-k3u1fbpfcp-zoom-1.image)

由于这一次我们没有使用border，元素有宽高，所以我们可以在元素上设置文字了：

```html
<div class="pie">10%</div>
```

```css
.pie {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
  color: #fff;
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
}
```

上面代码的效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54bcd43e46854c798a87c4837e7008e0~tplv-k3u1fbpfcp-zoom-1.image)

接下来，我们一样采用与第二个故事相同的思路，用伪元素拼接来实现与进度数据对应的饼图。

```css
.pie,
.pie::before {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  position: relative;
}

.pie {
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
  color: #fff;
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
}

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, transparent 50%,#37c 50%);
}
```

上面的代码中，我们也用`linear-gradient`给伪元素添加背景色渐变，让它的左边是透明色，右边是蓝色。这时，它的效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/908b1d2aa15d472caaa68b48f0f2c2d3~tplv-k3u1fbpfcp-zoom-1.image)

<!-- 但是这里有个问题，我们发现文字被伪元素盖住了一部分： -->
这时，你可能发现了一个问题，文字被盖住了一部分。这是因为伪元素是`.pie`的子元素，它的层级比文字层级高。

如果我们给它设置较小的`z-index`：

```css
/*...省略其他的CSS规则...*/

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, transparent 50%,#37c 50%);
  z-index: -1; /*将伪元素的叠级变小*/
}
```

这时，它又跑到`.pie`元素背景后边去了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0256258d004c4d26b0ee8b0eeb491826~tplv-k3u1fbpfcp-zoom-1.image)

那么这时该怎么办呢？

很简单，我们可以将`.pie`和`.pie::before`的背景对调一下。让伪元素做底层饼图，而让`.pie`元素作为叠加层：

```css
.pie,
.pie::before {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  position: relative;
}

.pie {
  background: linear-gradient(90deg, transparent 50%,#37c 50%);
  color: #fff;
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
}

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
  z-index: -1;
}
```

<!-- 这样让元素背景去遮盖伪元素背景，就得到我们想要的效果了。 -->

这样，写在`.pie`元素里的文字就不会被覆盖，而且也达到了我们的效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b712619635f4588bda70ee81dd1fdc7~tplv-k3u1fbpfcp-zoom-1.image)


现在，我们可以通过旋转上层饼图来实现与进度数据相对应的饼图。但是，这里我们不再需要旋转`.pie`元素，只需要调整`linear-gradient`的渐变轴来实现：
<!-- 那么我们要调整饼图的百分比，和前一个故事类似，不过这次我们换成调整`linear-gradient`的旋转角度： -->

```css
/*...省略其他CSS规则...*/

.pie {
  color: #fff;
  background: linear-gradient(.35turn, transparent 50%,#37c 50%);
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
}

/*...省略其他CSS规则...*/
```

如上代码所示，我们将元素背景色的渐变轴调整成`.35turn`。注意与`rotate`一样，渐变轴旋转可以用`turn`做单位，`90deg`相当于`0.25turn`，再旋转`0.1turn`也就是`0.35turn`，这时候刚好是`10%`的进度了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3de10fe9d3c549b48ac9fbfa2b7636ea~tplv-k3u1fbpfcp-zoom-1.image)

与上一版一样，我们需要在进度超过50%的时候，改变一下`.pie`元素的颜色分配，替换为：

```css
.pie.convex {
  background: linear-gradient(.85turn, #3c7 50%, transparent 50%);
}
```

```html
<div class="pie convex">60%</div>
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/257d048e48ee49498af538e98df14652~tplv-k3u1fbpfcp-zoom-1.image)

这样就可以实现超过50%的情况了。

这个版本通过改变`linear-gradient`的角度来改变饼图的比例，而且改变属性是在`.pie`元素不是在伪元素上，所以我们可以用JS来控制元素。

[在线演示](https://junyux.github.io/FE-Advance/day02/index2-v3.html)

```html
<div class="pie">10%</div>
<div class="pie">25%</div>
<div class="pie">50%</div>
<div class="pie">80%</div>
```

```css
.pie,
.pie::before {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  position: relative;
}

.pie {
  color: #fff;
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
}

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
  z-index: -1;
}
```

```js
function initPieGraph() {
  const graphs = document.querySelectorAll('.pie');
  graphs.forEach((graph) => {
    const percentage = parseFloat(graph.innerHTML) / 100;
    if(percentage <= 0.5) {
      graph.style.background = `linear-gradient(${percentage + .25}turn, transparent 50%,#37c 50%)`;
    } else {
      graph.style.background = `linear-gradient(${percentage + .25}turn, #3c7 50%, transparent 50%)`;
    }
  });
}
initPieGraph();
```

如上代码所示，percentage表示进度。当进度小于50%时，我们将`.pie`元素的背景色设置为左边透明，右边蓝色，且渐变轴是`(percentage+.25)trun`。当进度超过50%时，我们将`.pie`元素的背景色设为左边绿色，右边透明，且渐变轴是`(percentage+.25)trun`。

这样我们得到和上一版一样的结果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4107876fabe449c184eb0eb8189e4929~tplv-k3u1fbpfcp-zoom-1.image)

这一版本的有点在于保持了简单的HTML结构，没有多余的嵌套标签。CSS也更加简单。而它的缺点是需要一段JS来控制不同进度的饼图。所以这个方案和上一个方案相比，只能说是各有利弊，谈不上更完美。

<!-- 好处是我们的HTML结构更简单，不需要嵌套标签，CSS也更简单，代价是我们需要增加一段JS来控制饼图的进度。所以这个方案和上一个方案相比，只能说是各有利弊，谈不上更完美。 -->

那么，能不能既保持HTML简洁、又不依赖JS呢？

你可能想到，我们可以沿用上一个方案里面CSS动画的那个思路呀。是的，这个想法很好，但是，很不幸，CSS动画没办法直接控制`linear-gradient`中的渐变轴的角度，让它线性变化，所以，使用动画来控制渐变轴是行不通的。

那么，作为读者的你，有没有办法让饼图既保持HTML简洁，又不需要JS控制呢？

## 第六个故事：饼图 3.0

为了保持HTML简洁，又使用JS控制，我们可以结合前两个版本的方案，也就是固定渐变轴，然后采用`transform`属性旋转我们的元素，以实现我们的饼图3.0。

但是这个方案有一个问题， 就是我们只能旋转伪元素而不能是`.pie`元素。因为伪元素是子类，如果用`transform`旋转父类，子类会跟着一起旋转。可是，第二个版本中，因为要保证文字显示，我们将伪元素的`z-index`设置为负值，所以它在`.pie`元素的下层。那么到底要怎样旋转伪元素呢？

<!-- 但是这里有个细节需要注意，那就是我们得旋转伪元素而不是`.pie`元素，因为伪元素是子类，如果用`transform`旋转父类，子类会跟着一起旋转。因为要保证文字显示，我们将伪元素的`z-index`设置为负值，所以它在`.pie`元素的下层，而我们切换50%时的状态要改变下层元素。 -->
<!-- ![](https://p1.ssl.qhimg.com/t01af943c9181395383.gif) -->
其实很简单，我们可以把在上层的`.pie`元素的左半圆从原来的透明色设置为绿色，右半圆则初始为透明色：

```html
<div class="pie">0%</div>
```

```css
.pie,
.pie::before {
  display: inline-block;
  width: 150px;
  height: 150px;
  border-radius: 50%;
  position: relative;
}

.pie {
  color: #fff;
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
  background: linear-gradient(.25turn, #3c7 50%,transparent 50%);
}

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
  z-index: -1;
}
```

那么，初始情况下，我们的饼图是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/895ccae0ff4a4f06993e609f0b6633db~tplv-k3u1fbpfcp-zoom-1.image)

然后，我们旋转`.pie::before`这个伪元素：

```css
/* ...省略其他CSS规则... */

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
  z-index: -1;
  transform: rotate(0turn);
  animation: spin 10s linear infinite;
  /* animation-play-state: paused;
  animation-delay: inherit; */
}

@keyframes spin{
  to {transform: rotate(1turn)}
}
```

这时饼图的动画如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40274a40d6d14168bed04512efb8900e~tplv-k3u1fbpfcp-zoom-1.image)

同样，这时我们发现当进度超过50%的时候，进度展示的效果就不正确了。为了清晰，我将`.pie`元素的左半圆设置为半透明：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ed6d6fc8b8c4550be5752d0a3215988~tplv-k3u1fbpfcp-zoom-1.image)

所以这时，我们需要将`.pie`元素的颜色渐变对调一下：
<!-- 我们仍然可以用之前的`spin`动画，不过，另一个`convex`动画，我们不能再加在伪元素上，需要把它加在`.pie`元素上了： -->

```css
.pie {
  color: #fff;
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
  background: linear-gradient(.25turn, #3c7 50%,transparent 50%);
  animation: convex 10s step-end infinite;
  animation-play-state: paused;
  animation-delay: -0s;
}
@keyframes convex{
  50% {background: linear-gradient(90deg, transparent 50%, #37c 50% 0);}
}

/* 省略其他CSS规则*/
```
如上代码所示，我们将`convex`动画设置在`.pie`元素上，而不是原先的伪元素上。当动画执行到50%的时候，我们将`.pie`元素的背景色设置为左边透明色，右边为蓝色。

然后，我们依然通过`animation-delay`属性的内联样式来控制它们：

```html
<div class="pie" style="animation-delay: -1s;">10%</div>
<div class="pie" style="animation-delay: -2.5s;">25%</div>
<div class="pie" style="animation-delay: -5s;">50%</div>
<div class="pie" style="animation-delay: -8s;">80%</div>
```

这个方案到这里就结束了，我们既节省了`<span>`标签，又不用使用JS来控制。它的完整代码如下：

[在线演示](https://junyux.github.io/FE-Advance/day02/index2-v4.html)

```html
<div class="pie" style="animation-delay: -1s;">10%</div>
<div class="pie" style="animation-delay: -2.5s;">25%</div>
<div class="pie" style="animation-delay: -5s;">50%</div>
<div class="pie" style="animation-delay: -8s;">80%</div>
```

```css
.pie {
  color: #fff;
  font-size: 1rem;
  line-height: 150px;
  text-align: center;
  background: linear-gradient(.25turn, #3c7 50%,transparent 50%);
  animation: convex 10s step-end infinite;
  animation-play-state: paused;
  animation-delay: -0s;
}

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, #37c 50%,#3c7 50%);
  z-index: -1;
  transform: rotate(0turn);
  animation: spin 10s linear infinite;
 animation-play-state: paused;
  animation-delay: inherit;
}

@keyframes spin{
  to {transform: rotate(1turn)}
}
@keyframes convex{
  50% {background: linear-gradient(90deg, transparent 50%, #37c 50% 0);}
}
```

### Scss

不过，故事到这里并没有结束，现在这个方案还有一个不足之处。从上面的代码中，我们发现有几处可变值是重复的。比如：`#37c`、`#3c7`两个颜色分别出现了多次，再比如：`width`、`height`、`line-height`也是可变值，可以控制饼图的半径，但是它们的值本身要相同。
<!-- 我们有几处重复的可变值，比如`#37c`、`#3c7`两个颜色分别出现了多次，再比如width、height、line-height也是可变值，可以控制饼图的半径，但是它们的值本身要相同。 -->

我们当然可以就这么放任这些重复值不管，但是这意味着将来需求变更，或者配置需要，我们要改变饼图颜色和大小时，就需要修改多处，只要漏改一处，就会产生bug。

所以，这时候，我们就可以考虑使用像Scss这样的CSS预处理器。比如，我们使用Scss的话，就可以这样定义变量：

```scss
$fg: #3c7;
$bg: #37c;
$radius: 150px;

.pie,
.pie::before {
  display: inline-block;
  width: $radius;
  height: $radius;
  border-radius: 50%;
  position: relative;
}

.pie {
  color: #fff;
  font-size: 1rem;
  line-height: $radius;
  text-align: center;
  background: linear-gradient(.25turn, $fg 50%,transparent 50%);
  animation: convex 10s step-end infinite;
  animation-play-state: paused;
  animation-delay: -0s;
}

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, $bg 50%,#$fg 50%);
  z-index: -1;
  transform: rotate(0turn);
  animation: spin 10s linear infinite;
  animation-play-state: paused;
  animation-delay: inherit;
}

@keyframes spin{
  to {transform: rotate(1turn)}
}
@keyframes convex{
  50% {background: linear-gradient(90deg, transparent 50%, $bg 50% 0);}
}
```

然后通过预处理器将最终生成对应的CSS，这样当我们要修改参数的时候，只需要修改最顶部这三个变量就可以了。

### CSS自定义属性

如果我们的项目只需要运行在较新的浏览器上，那么我们还可以使用**CSS自定义属性**这个强大的特性，动态地定义层叠式变量：

[在线演示](https://junyux.github.io/FE-Advance/day02/index2-v5.html)

```css
.pie,
.pie::before {
  --radius: 150px;
  --fg-color: #3c7;
  --bg-color: #37c;
  display: inline-block;
  width: var(--radius);
  height: var(--radius);
  border-radius: 50%;
  position: relative;
}

.pie {
  color: #fff;
  font-size: 1rem;
  line-height: var(--radius);
  text-align: center;
  background: linear-gradient(.25turn, var(--fg-color) 50%,transparent 50%);
  animation: convex 10s step-end infinite;
  animation-play-state: paused;
  animation-delay: -0s;
}

.pie::before {
  position: absolute;
  left: 0;
  top: 0;
  content: '';
  background: linear-gradient(90deg, var(--bg-color) 50%,var(--fg-color) 50%);
  z-index: -1;
  transform: rotate(0turn);
  animation: spin 10s linear infinite;
  animation-play-state: paused;
  animation-delay: inherit;
}

@keyframes spin{
  to {transform: rotate(1turn)}
}
@keyframes convex{
  50% {background: linear-gradient(90deg, transparent 50%, var(--bg-color) 50% 0);}
}
```

上面的代码，我们定义了三个自定义属性：

```css
{
  --radius: 150px;
  --fg-color: #3c7;
  --bg-color: #37c;
}
```

然后在需要用到的地方使用 `var()` 方式动态地引入这些值，这个方式现在在除了IE之外的浏览器上基本上运行良好。

CSS自定义属性有很多使用场景，它还可以和CSS其他原生新特性比如`cacl()`和`color()`结合使用，能够产生令人惊艳的效果，这部分内容等后续有机会，我们再深入讨论。

饼图的CSS实现到这里基本上就结束了。不过，实现饼图的方案并不只有这些，除了CSS，我们也可以考虑使用SVG或者Canvas，它们也各有利弊，但不在本课程的讨论范畴，有机会，大家可以继续深入学习这些内容。今天的故事主要是告诉你，以全新的视角去看待CSS，它比你想像的要强大的多。掌握这些技巧，可以让你的前端开发更加成熟。

## 3.第三日：代码的封装性、可读性和正确性

<!-- # 第二天：代码的封装性、可读性和正确性 -->
# 第三天：代码的封装性、可读性和正确性

## 第一个故事：函数的封装性

**函数的封装性**是指把函数相关的数据和行为结合在一起，对调用者隐藏内部处理过程。这句话听上去很容易理解，但是实际操作起来却又很容易被忽略。所以，今天的故事，我们将带你看看在实际开发中，函数的封装性是多么容易被破坏的。我们又是如何重构以实现函数的封装性的。

我们的任务是用JavaScript实现一个**异步状态切换的模块**。由于这个模块过于抽象和涉及过多细节，我们在这里将它简化一下，类似于实现一个“交通灯”系统。

先来看看它的页面HTML结构和CSS设置：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>模拟交通灯</title>
  <style>
    html, body {
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      overflow: hidden;

      /*设置html和body元素的布局为弹性布局*/
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
    }
    header {
      line-height: 2rem;
      font-size: 1.2rem;
      margin-bottom: 20px;
    }
    .traffic { /*将class=traffic元素设置为弹性布局，它的子元素按照从上面到下排列*/
      padding: 10px;
      display: flex;
      flex-direction: column;
    }
    .traffic .light {
      width: 100px;
      height: 100px;
      background-color: #999;
      border-radius: 50%;
    }

    /*将class=traffic & class=pass元素下的第一个class=light的元素的背景色设置为绿色*/
    .traffic.pass .light:nth-child(1) {
      background-color: #0a6; /*绿灯*/
    }
    .traffic.wait .light:nth-child(2) {
      background-color: #cc0; /*黄灯*/
    }
    .traffic.stop .light:nth-child(3) {
      background-color: #c00; /*红灯*/
    }
  </style>
</head>
<body>
  <header>模拟交通灯</header>
  <main>
    <div class="traffic pass">
      <div class="light"></div>
      <div class="light"></div>
      <div class="light"></div>
    </div>
  </main>
</body>
</html>
```

上面代码在浏览器上的效果如下图所示：
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cbd1d2a097304c3fba5f32ce7b9aa0ed~tplv-k3u1fbpfcp-zoom-1.image)

这个例子的具体需求是，模拟交通灯信号，分别以5秒、1.5秒、3.5秒来循环切换绿灯（pass状态）、黄灯（wait状态）和红灯（stop状态）。也就是，默认是绿灯，过5秒后显示黄灯，过1.5秒后显示红灯，再过3.5秒后又回到绿灯，然后以这样的方式继续循环下去。

这个需求实现起来很简单，我们的代码如下所示：

[在线演示](https://junyux.github.io/FE-Advance/day03/index1-v1.html)

```js
const traffic = document.querySelector('.traffic');

function loop() {
  traffic.className = 'traffic pass';
  setTimeout(() => {
    traffic.className = 'traffic wait';
    setTimeout(() => {
      traffic.className = 'traffic stop';
      setTimeout(loop, 3500);
    }, 1500);
  }, 5000);
}

loop();
```

首先，我们来分析一下这段代码：

这段代码的一开始就获取了`class=traffic`的元素，然后又声明了一个`loop`函数。这个函数的功能是：默认情况下，将这个`traffic`元素的`class`属性设置为`traffic pass`。 这样设置后，它就命中了下面这个CSS设置，使得第一个div元素的背景变成了绿色：

```css
.traffic.pass .light:nth-child(1) {
  background-color: #0a6; /*绿灯*/
}
```

然后是三个`setTimeout`方法嵌套。第一层的`setTimeout`方法的回调在5000毫秒（也就是5秒）后触发，使得`traffic`元素的`class`属性变成了`tranffic wait`。 这时命中了下面这条CSS规则，让第二个`div`元素变成黄色：

```css
.traffic.wait .light:nth-child(2) {
  background-color: #cc0; /*黄灯*/
}
```

接着是过了1.5秒，变成红灯，然后又过了3.5秒，又回到绿灯。周而复始。

上面的这段代码虽然实现了我们的需求，但是它在设计上有很大的缺陷 —— `loop`函数访问了外部环境`traffic`。这么做有两个问题：

1. 如果我们修改了HTML代码，元素不叫做`traffic`了，这个函数就不work了。
2. 如果我们想把这个函数复用到其他地方，我们还得在那个地方重建这个`traffic`对象。

这两个问题的本质都是因为，在我们的这个设计中，函数的**封装性**完全被破坏，这是新人常常犯的错误。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c0b78f9b030c44848f2e5d73698492aa~tplv-k3u1fbpfcp-zoom-1.image)

所以，我们不能直接将`traffic`这个对象直接写在`loop`函数中。你可能很容易就想到了，让`traffic`对象作为这个函数的参数传入：

[在线演示](https://junyux.github.io/FE-Advance/day03/index1-v2.html)

```js
const traffic = document.querySelector('.traffic');

function loop(subject) {
  subject.className = 'traffic pass';
  setTimeout(() => {
    subject.className = 'traffic wait';
    setTimeout(() => {
      subject.className = 'traffic stop';
      setTimeout(loop.bind(null, subject), 3500);
    }, 1500);
  }, 5000);
}

loop(traffic);
```

这样修改我们解决了第一个问题，就是函数体内部不应该有完全来自外部环境的变量，除非这个函数不打算复用，比如是一个函数内部的函数：

```js
function foo(arg) {
  function bar() {
    // 使用 arg
    arg...
  }
  ...
}
```

上面的代码，bar使用arg是可以的，因为它只在foo内部存在，不会用在其他地方。

不过，我们将traffic作为参数传给loop，只解决了外部变量的封装这一个问题，但是，在这个loop过程中，还有其他的数据我们是写“死”在代码里面的，如果不把它们提取出来，这段代码的可复用性依然很差。

<!-- 但是，这样修改依然有一个问题：如果将来需求变化，需要为其他元素也实现类似的状态切换功能呢？不同的只是状态值和subject。难道我们需要为了这个需求，再复制一段这样的代码吗？ -->

## 第二个故事：实现异步状态切换函数的封装

继续上一个故事的问题，我们如何封装一个函数让它具备适应各种subject的状态切换的功能呢？函数简单来说，是一个处理数据的最小单元。它包含了两个部分：数据和处理过程。要让我们设计的函数具有通用性，那么我们可以抽象数据，也可以抽象过程。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26d92a6fc1974081a874c16ef716504f~tplv-k3u1fbpfcp-zoom-1.image)

通常，抽象数据比较直观，也更常用，我们先来看看如何抽象数据。至于抽象过程，在后续的课程中我们会深入讨论。

### 第一步：数据抽象

**数据抽象就是把数据定义并聚合成能被过程处理的对象，交由特定的过程处理。** 简单来说就是数据的结构化。

<!-- 回到我们这个实例，回顾一下上一个故事中的`loop`函数。这个函数体中包含有哪些可变的数据？哪些数据可以被抽象出来呢？ -->

对于第一个故事中的异步状态切换的任务来说，首先要找到它需要处理的数据，也就是：状态`pass, wait 和 stop`，以及切换的时间`5秒、1.5秒和3.5秒`。

<!--
老大看了小李的代码，首先问小李道：“你知道，程序设计有两种抽象方式吗？”

见小李露出迷惑的表情，老大接着说：“一种方式叫**数据抽象**，一种方式叫**过程抽象**。”

“一般情况下，数据抽象更常见。顾名思义，**数据抽象简单来说就是把数据定义并聚合成能被过程处理的对象，交由特定的过程处理**。对于你的这个任务来说，首先要找到它的数据。”

“我明白了，它的数据包括要操作的对象traffic、切换状态`pass, wait 和 stop`，以及切换的时间`5秒、1.5秒和3.5秒`。”小李说。

“是的，那么你就要把这些数据给抽取出来，围绕这些数据来定义过程。”

“那我了解了。”小李很快重新修改了实现：
-->

我们将数据从`loop`函数剥离出来：

[在线演示](https://junyux.github.io/FE-Advance/day03/index1-v3.html)

```js
const traffic = document.querySelector('.traffic');

function signalLoop(subject, signals = []) {
  const signalCount = signals.length;
  function updateState(i) {
    const {signal, duration} = signals[i % signalCount];
    subject.className = signal;
    setTimeout(updateState.bind(null, i + 1), duration);
  }
  updateState(0);
}

// 数据抽象
const signals = [
  {signal: 'traffic pass', duration: 5000},
  {signal: 'traffic wait', duration: 3500},
  {signal: 'traffic stop', duration: 1500},
];
signalLoop(traffic, signals);
```

我们将状态和时间抽象成一个包含3个对象的数组，并将这个结构化的数据传递到`signalLoop`方法中。利用`updateState`方法的递归调用实现了状态的切换。

<!-- _如果你不明白`updateState`方法中的`bind`用法，可以参考我们的《初级前端工程师JS篇》的函数部分，本课程不做重复介绍。_ -->

经过数据抽象的代码可以适应不同状态和时间的业务需求，我们只需要修改数据抽象即可，而不需要修改`signalLoop`方法。

但是，采用数据抽象重构后，我们的`signalLoop`方法还未达到完全封装。因为`signalLoop`函数中存在一部分改变外部状态的代码。我们把改变外部状态的部分叫做代码的**副作用(side-effect)**。通常情况下，我们可以考虑**把函数体内部有副作用的代码剥离出来**，这往往能提升函数的通用性、稳定性和可测试性。

<!-- 小李的老大对小李的修改十分赞赏，但同时，他也指出`signalLoop`方法的另一个问题——“运行的函数代码作用有两种，一部分代码不改变外部的状态，另一部分代码改变外部的状态。我们把改变外部状态的部分叫做代码的**副作用(side-effect)**。通常情况下，我们可以考虑**把函数体内部有副作用的代码剥离出来**，这往往能提升函数的通用性、稳定性和可测试性。”

“这种改进封装代码的思路叫做**去副作用化**”。 -->

### 第二步：去副作用化

那么，在`signalLoop`方法中，哪个部分的代码改变了外部的状态呢？

```subject.className = `traffic ${signal}`;``` 因为subject是外部变量，这条语句改变了这个变量的className状态。所以，我们需要将这部分也从函数中剥离出去：

<!-- 小李仔细审视了`signalLoop`方法，发现这个方法改变外部状态的是这条语句```subject.className = `traffic ${signal}`;```。因为subject是外部变量，这条语句改变了这个变量的className状态。于是，他又进行了如下修改： -->

[在线演示](https://junyux.github.io/FE-Advance/day03/index1-v4.html)

```js
const traffic = document.querySelector('.traffic');

function signalLoop(subject, signals = [], onSignal) {
  const signalCount = signals.length;
  function updateState(i) {
    const {signal, duration} = signals[i % signalCount];
    onSignal(subject, signal);
    setTimeout(updateState.bind(null, i + 1), duration);
  }
  updateState(0);
}

const signals = [
  {signal: 'pass', duration: 5000},
  {signal: 'wait', duration: 3500},
  {signal: 'stop', duration: 1500},
];
signalLoop(traffic, signals, (subject, signal) => {
  subject.className = `traffic ${signal}`;
});
```

如上代码所示，我们将改变外部变量的操作用回调的方法传给`singalLoop`。这样修改提升了`signalLoop`函数的通用性，使得这个函数也可以用于操作其他的DOM元素的状态切换。

<!-- 上面这段代码，将交通灯信号变化的操作剥离出来，作为`signalLoop`的回调方法（`onSignal`）。这样修改提升了`signalLoop`方法的通用性，使得这个函数也可以用于操作其他的DOM元素。 -->

像上面这样的封装，提高了`signalLoop`函数的‘纯度’。关于什么是函数的“纯度”，我们会在第5日中详细解释。

完成了`signalLoop`函数的封装，我们感觉得无论是采用第一版的3个`setTimeout`方法嵌套，还是使用`updateState`异步递归，虽然都能实现业务需求，但是代码的可读性不是很高。那么如何修改可以提高代码的可读性呢？ 

<!--
“是的，除此之外，这个函数还拥有更好的可测试性和可维护性。”老大说，“因为这样封装使得这个函数的‘纯度’增加了。可能你现在还不能理解什么是函数的‘纯度’，以及它对测试和可维护性带来的影响，但没有关系，我们在以后会有机会讨论它们。”

[TODO] 根据这个具体的例子，解释函数的”纯度“的含义。
[TODO] 封装是解偶的一种方式。

“那么除了数据抽象这个方向，过程抽象又是怎么回事呢？”小李问道。

“过程抽象，是另一个抽象方式，也是封装代码的另一个方向，我们也可以用它来进一步优化代码。但先别着急，在这之前，我们还有一些其他的改进可以继续。”老大说。“接下来，我们先考虑代码的语义，从这个方向增强代码的可读性。”
-->

## 第三个故事：代码的“语义”与可读性

为了提高异步状态切换代码的可读性，我们可以采用ES6异步规范 —— Promise，重构一下我们的代码：
<!-- 小李决定继续改进模拟交通灯的实现代码。这次是考虑内部实现细节。
首先考虑的是最开始那个版本的setTimeout和后来版本的异步递归。如果将它们改成Promise的方式，应该会使得代码的可读性更好。小李这样想，于是动手开始尝试重构。-->

```js
function wait(ms) {
  return new Promise((resolve) => {
    setTimetout(resolve, ms);
  });
}
```

这段代码将`setTimeout`方法封装成`wait`函数。这个函数将`setTimeout`方法用Promise包裹起来，并返回这个Promise对象。

有了这个`wait`函数之后，原本有些晦涩的`setTimeout`嵌套，可以很容易改写成一个`async`函数中的`await`循环：

[在线演示](https://junyux.github.io/FE-Advance/day03/index1-v5.html)

```js
function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

const traffic = document.querySelector('.traffic');

(async function () {
  while(1) {
    await wait(5000);
    traffic.className = 'traffic wait';
    await wait(1500);
    traffic.className = 'traffic stop';
    await wait(3500);
    traffic.className = 'traffic pass';
  }
}());
```

如上代码所示，我们将原来的`loop`方法改为立即调用函数的方式，并将3个`setTimeout`部分修改为`while`死循环。循环体中的部分很容易理解：等待5秒 -> 将`traffic`元素的`className`属性修改为`traffic wait` -> 等1.5秒 -> 将`traffic`元素的`className`属性修改为`traffic stop` -> 等待3.5秒 -> 将`traffic`元素的`className`属性修改为`traffic pass`。

这段代码与之前的代码相比，它的可读性是不是提高了很多？

同样，我们也用Promise修改`signalLoop`的版本，同样也很容易阅读：

[在线演示](https://junyux.github.io/FE-Advance/day03/index1-v6.html)

```js
function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

const traffic = document.querySelector('.traffic');

async function signalLoop(subject, signals = [], onSignal) {
  const signalCount = signals.length;
  for(let i = 0; ;i++) {
    const {signal, duration} = signals[i % signalCount];
    await onSignal(subject, signal);
    await wait(duration);
  }
}

const signals = [
  {signal: 'pass', duration: 5000},
  {signal: 'wait', duration: 3500},
  {signal: 'stop', duration: 1500},
];
signalLoop(traffic, signals, (subject, signal) => {
  subject.className = `traffic ${signal}`;
});
```

与上一次考虑封装性不同，这次的重构主要是在代码的内部，使用`async/await`能够把异步的递归简化为更容易让人阅读和理解的循环，而且，修改后的代码，还允许`onSignal`回调本身也是一个异步过程，这进一步增加了`signalLoop`函数的用途。

在ES6之后，JavaScript比之前的版本有了许多改进，但如果要说最重要的改进，那么Promise规范和`async/await`语法绝对可以列于其中。Promsie和`async/await`创造不仅仅是语法，而是一种新的语义，有了它们，JavaScript这一种异步非阻塞语言，才真正能够将异步的特性发挥到极致。

**代码是人阅读的，只是偶尔让计算机执行一下。**

<!-- 这一个故事与前面两个故事相比比较简短，到这里就结束了。小李将最后这一版代码作为最终的实现版本提交了，产品也顺利发布。但是，有关异步的思考却还没有结束，在后续的故事中还将继续讨论。 -->

## 第四个故事：函数的正确性和效率

代码的封装性和可读性固然重要，但是代码的正确性更为重要。如果你是一个初级工程师，可能你无法写出高封装性的代码，但是你也必须保证你所提交的代码是正确的，否则就会造成业务逻辑失败。可能你会觉的这个话题很滑稽，我怎么可能将错误的代码提交呢？但在实际开发中，我们可能会写出错误的代码而不自知。比如：洗牌算法的陷阱。

考虑这样一个抽奖场景：给定一组生成好的抽奖号码，然后我们需要实现一个模块。这个模块的功能是将这组号码打散（即，洗牌）然后输出一个中奖的号码。

<!-- 周一上班的时候，小李被老大叫到工位前，老大给小李看了一段其他工程师写的代码，这是一段将一组有序的数据随机打散的实现代码，是用在一个提供给用户抽奖的游戏界面上。 -->

那这个打散号码的JS片段如下：

```js
function shuffle(items) {
  return [...items].sort((a, b) => Math.random() > 0.5 ? -1 : 1);
}
```

这段代码被用在一个用户抽奖的页面上，大致是这样的：

<!-- ```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>幸运数字</title>
  <style>
    html, body {
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .lucky {
      position: fixed;
      margin-top: -180px;
    }
    .panel {
      display: grid;
      grid-template-columns: 100px 100px 100px;
      grid-template-rows: 100px 100px 100px;
    }
    .card {
      font-size: 2.5rem;
      line-height: 100px;
      text-align: center;
      color: #999;
      border: solid 1px;
      cursor: pointer;
    }
    .card.bingo {
      color: #a00;
    }
  </style>
</head>
<body>
  <div class="lucky">今日幸运数字：<span id="lucky-number">6</span></div>
  <div class="panel">
    <div class="card" data-idx="0">?</div>
    <div class="card" data-idx="1">?</div>
    <div class="card" data-idx="2">?</div>
    <div class="card" data-idx="3">?</div>
    <div class="card" data-idx="4">?</div>
    <div class="card" data-idx="5">?</div>
    <div class="card" data-idx="6">?</div>
    <div class="card" data-idx="7">?</div>
    <div class="card" data-idx="8">?</div>
  </div>
</body>
</html>
``` -->

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60867fe4d8c347e0b71f05e640e778cf~tplv-k3u1fbpfcp-zoom-1.image)

为了便于描述，此处做了很大的简化，真实项目要比这复杂的得多，且抽奖代码不是运行在客户端，而是在服务端完成的。

这段代码看似可以实现目的，但是实际上却是有很大问题的。因为这个随机方法根本就不够随机。

我们可以写一个程序来测试一下。

```js
function shuffle(items) {
  return items.sort((a, b) => Math.random() > 0.5 ? -1 : 1);
}

const weights = Array(9).fill(0);

for(let i = 0; i < 10000; i++) {
  const testItems = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  shuffle(testItems);
  testItems.forEach((item, idx) => weights[idx] += item);
}

console.log(weights);

// [45071, 45016, 49406, 50455, 50727, 50205, 50981, 52346, 55793]
// 每次结果有变化，但总的来说前面的数字小，后面的数字大
```

我们把1到9数字经过shuffle函数随机10000次，然后把每一位出现的数字相加，得到总和。经过多次检验，发现总和数组前面的数字总是较小，后面的数字较大。

这就意味着，越大的数字出现在数组后面的概率要大一些。

造成这个结果的原因是，数组的`sort`方法内部是一个排序算法，我们不知道它的具体实现，但一般来说，排序算法用某种规则依次选取两个元素比较它们的大小，然后根据比较结果交换位置。

这个算法给排序过程一个随机的比较算子`(a, b) => Math.random() > 0.5 ? -1 : 1`，从而让数组元素的交换过程代码随机性，但是交换过程的随机性，并不能保证数学上让每个元素出现在每个位置都具有相同的几率，因为排序算法对每个位置的元素和其他元素交换的次序、次数都是有区别的。

要实现比较公平的随机算法，其实也并不难。我们只要每次从数组中随机取出一个元素来，将它放到新的队列中，这样直至所有的元素都取完，我们就得到了我们要的随机排列，而且可以严格保证数组元素出现在每个位置的几率都是相同的（这里不考虑JavaScript引擎内置的Math.random函数本身的随机性问题）。

```js
function shuffle(items) {
  items = [...items];
  const ret = [];
  while(items.length) {
    const idx = Math.floor(Math.random() * items.length);
    const item = items.splice(idx, 1)[0];
    ret.push(item);
  }
  return ret;
}

let items = [1, 2, 3, 4, 5, 6, 7, 8, 9];
items = shuffle(items);
console.log(items);
```

上面的代码，每次从数组中随机挑选元素，将这个元素从原数组的副本中删除（为了不影响原素组，我们创建了副本），放入新的数组，这样就可以保证每一个数在每个位置的概率是相同的。

[在线演示](https://junyux.github.io/FE-Advance/day03/index2-v1.html)

这个算法是没有问题的，但是效率上还有提升空间。因为存在splice方法，它的时间复杂度是O(n^2)。

如果要更快一些，我们不必用splice将元素从原数组副本中一一抽取，只要在每次抽取的时候，直接将随机到的位置的元素与数组的第“i”个元素交换即可。

```js
function shuffle(items) {
  items = [...items];
  for(let i = items.length; i > 0; i--) {
    const idx = Math.floor(Math.random() * i);
    [items[idx], items[i - 1]] = [items[i - 1], items[idx]];
  }
  return items;
}

let items = [1, 2, 3, 4, 5, 6, 7, 8, 9];
items = shuffle(items);
console.log(items);
```

如上面代码所示，我们每次从数组的前i个元素（第0~i-1个元素）中随机挑选一个，将它和第i个元素（下标为i-1）进行交换，然后把i的值减1，直到i的值小于1。

这个算法的时间复杂度是O(n)，所以性能上应该更好，如果随机排列的数组很大，我们应该选择这种实现。

[在线演示](https://junyux.github.io/FE-Advance/day03/index2-v2.html)

这个洗牌算法基本没有问题了，但是我们还可以进一步改进它。因为根据需求，用户抽奖的次数是有限制的，而且如果在次数允许的情况下，已经抽到了幸运数字，就不必再抽取下去，所以其实我们不必对整个数组进行完全的随机排列。

这个时候，我们其实可以改用生成器。

```js
function* shuffle(items) {
  items = [...items];
  for(let i = items.length; i > 0; i--) {
    const idx = Math.floor(Math.random() * i);
    [items[idx], items[i - 1]] = [items[i - 1], items[idx]];
    yield items[i - 1];
  }
}

let items = [1, 2, 3, 4, 5, 6, 7, 8, 9];
items = shuffle(items);
console.log(...items);
```

我们只要做一个很小的改动，将函数改成生成器，将`return`改成`yield`，就能够实现部分洗牌，或者用作抽奖：

[在线演示](https://junyux.github.io/FE-Advance/day03/index2-v3.html)

```js
function *shuffle(items) {
  items = [...items];
  for(let i = items.length; i > 0; i--) {
    const idx = Math.floor(Math.random() * i);
    [items[idx], items[i - 1]] = [items[i - 1], items[idx]];
    yield items[i - 1];
  }
}

let items = [...new Array(100).keys()];

let n = 0;
// 100个号随机抽取5个
for(let item of shuffle(items)) {
  console.log(item);
  if(n++ >= 5) break;
}
```

最后，我们总结一下，代码的封装性、可读性和正确性，都是程序开发中必须要关注问题。有时候，一些小细节看似微不足道，但是小问题积累起来，会变成大问题，甚至最终导致一个大系统的崩溃和不可维护。所以，要重视细节，尽量设计好每一个函数，严格保证它们的封装性、可读性和正确性，这是成为一名优秀工程师的前提。

## 4.第四日：过程抽象提升系统的可维护性

# 第四天 过程抽象提升系统的可维护性

<!-- ## 第一个故事：一个简单的函数装饰器 -->
## 第一个故事：只执行一次

上一节我们说过函数是处理数据的最小单元。为了能够让函数具备通用性，我们可以抽象数据或者抽象过程。今天我们就来探讨一下过程是如何抽象的。

在前端开发中，我们经常遇到一些事件处理函数只能执行一次的情况。比如下面的这个例子：

这是一个页面，它处理一个用户事项的清单，大致的代码实现如下：

[在线演示](https://junyux.github.io/FE-Advance/day04/index1-v1.html)

```html
<ul>
  <li><button></button><span>任务一：学习HTML</span></li>
  <li><button></button><span>任务二：学习CSS</span></li>
  <li><button></button><span>任务三：学习JavaScript</span></li>
</ul>
```

```css
ul {
  padding: 0;
  margin: 0;
  list-style: none;
}

li button {
  border: 0;
  background: transparent;
  cursor: pointer;
  outline: 0 none;
}

li.completed {
  transition: opacity 2s;
  opacity: 0;
}

li button:before {
  content: '☑️';
}

li.completed button:before {
  content: '✅';
}
```

```js
const list = document.querySelector('ul');
const buttons = list.querySelectorAll('button');
buttons.forEach((button) => {
  button.addEventListener('click', (evt) => {
    const target = evt.target;
    target.parentNode.className = 'completed';
    setTimeout(() => {
      list.removeChild(target.parentNode);
    }, 2000);
  });
});
```

这是一个非常简单的功能，我们在列表项的按钮上注册click事件，当用户点击到列表项前面的button的时候，显示一个淡出动画，然后将列表项从list中删除。

从下面这个张效果来看，似乎没什么问题：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19937f16c6834276bc1b71176509ab21~tplv-k3u1fbpfcp-zoom-1.image)

但是，测试工程师却发现了一个问题 —— 在列表项消失前，如果快速地点击多次列表元素，在控制台上会出现异常信息：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ef9a7e7f94845e7ba143d5976e20a00~tplv-k3u1fbpfcp-zoom-1.image)

这条信息的出现，是因为当元素还没消失的时候，如果再次被点击，依然会响应事件。所以在事件处理函数中，会启动多个setTimeout定时器。但是当第一次执行`list.removeChild(target.parentNode)`时，target.parentNode就已经从list中移除了，所以当后续定时器回调函数再被执行时，就会抛出异常了。

要解决这个问题其实很简单，就必须让click回调函数只执行一次。而让click回调函数只执行一次的方式有很多种：

### 1. once参数

在新的浏览器里，可以通过`addEventListener`的`once`参数实现：

[在线演示](https://junyux.github.io/FE-Advance/day04/index1-v2.html)

```js
const list = document.querySelector('ul');
const buttons = list.querySelectorAll('button');
buttons.forEach((button) => {
  button.addEventListener('click', (evt) => {
    const target = evt.target;
    target.parentNode.className = 'completed';
    setTimeout(() => {
      list.removeChild(target.parentNode);
    }, 2000);
  }, {once: true});
});
```

但是在部分老的浏览器中，可能不支持once参数。这时候，也可以有别的方法，比如：

### 2. removeEventListener方法

```js
const list = document.querySelector('ul');
const buttons = list.querySelectorAll('button');
buttons.forEach((button) => {
  button.addEventListener('click', function f(evt) {
    const target = evt.target;
    target.parentNode.className = 'completed';
    setTimeout(() => {
      list.removeChild(target.parentNode);
    }, 2000);
    target.removeEventListener('click', f);
  });
});
```

在click事件处理函数中，通过`target.removeEventListener('click', f);`将处理函数本身从事件监听中移除。

### 3. disabled属性

我们也可以使用元素的`disabled`属性来实现目标元素只被点击一次的效果：

[在线演示](https://junyux.github.io/FE-Advance/day04/index1-v3.html)

```js
const list = document.querySelector('ul');
const buttons = list.querySelectorAll('button');
buttons.forEach((button) => {
  button.addEventListener('click', (evt) => {
    const target = evt.target;
    target.parentNode.className = 'completed';
    setTimeout(() => {
      list.removeChild(target.parentNode);
    }, 2000);
    target.disabled = true;
  });
});
```

事件处理方法只执行一次的需求还有很多，比如一个购物车提交数据给服务器，按钮点击一次后，我们也要将按钮置为`disabled`或者移除监听器：

```js
formEl.addEventListener('submit', function submitData(evt) {
  fetch('path/to/url', {
    method: 'POST',
    body: JSON.stringify(formData),
    ...
  });
  formEl.removeEventListener('submit', submitData);
});
```

上述的这些解决方式在不同的需求中都必须不断的重复。那么，有没有通用的办法覆盖所有只需执行一次的需求呢？

## 第二个故事：函数装饰器——once函数

为了能够让第一个故事中的“只执行一次“的需求能覆盖不同的事件处理，我们需要将这个需求从事件处理函数中剥离出来。这个过程我们称为**过程抽象**。下面，我们就来看看过程抽象是如何实现的。
<!-- 那么，我们如何将这个“只执行一次”的过程抽象出来，将具体的处理方法放在这个抽象过程中执行呢？ -->

once函数：

```js
function once(fn) {
  return function (...args) {
    if(fn) {
      const ret = fn.apply(this, args);
      fn = null;
      return ret;
    }
  };
}
```

<!-- 如上代码所示，这个`once`函数的参数`fn`是一个函数。它的返回值也是一个函数，这个函数就是我们抽象出来的，”只执行一次“的过程。我们把这个返回的函数称作是`fn`的**修饰函数**。而把`once`称为**函数的装饰器**。 -->
如上代码所示，这个`once`函数的参数`fn`是一个函数，它就是我们的事件处理函数。`once`的返回值也是一个函数。这个返回函数就是“只执行一次”的过程抽象。所以我们把这个返回函数称作是`fn`的**修饰函数**，而把`once`称为**函数的装饰器**。

我们来分析一下这段代码是如何实现”只执行一次”的需求的：当事件被触发，第一次调用`fn`的修饰函数的时候，`fn`存在，于是执行`fn`，然后将`fn`设置为`null`，并返回`fn`的执行结果。当再次执行这个修饰函数的时候，由于`fn`已经是`null`，就不会再次执行了，这样就实现了只调用一次的过程。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7c8f9f2b92c4435c9bec4474437de50a~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示。注意，蓝色的部分并不是`once`本身，而是`once`调用`fn`函数后返回的那个函数，也就是前面说的修饰函数，或者也可以说是一个代理函数，它根据情况决定是否将输入的参数传给原函数`fn`。

<!-- 这个`once`函数的参数是一个**要修饰的函数fn**，它的返回值是一个函数，修饰了`fn`。具体的逻辑是，当第一次调用返回的函数时，`fn`存在，则返回以当前函数的`this`上下文和参数调用`fn`的结果，同时将`fn`的值设为`null`。这样在下次再调用这个函数时，由于`fn`已经是`null`，就不会再次执行了，这样就实现了只调用一次的逻辑。 -->

现在，我们就可以用它来实现前面的需求：

[在线演示](https://junyux.github.io/FE-Advance/day04/index1-v4.html)

```js
const list = document.querySelector('ul');
const buttons = list.querySelectorAll('button');
buttons.forEach((button) => {
  button.addEventListener('click', once((evt) => {
    const target = evt.target;
    target.parentNode.className = 'completed';
    setTimeout(() => {
      list.removeChild(target.parentNode);
    }, 2000);
  }));
});
```

```js
formEl.addEventListener('submit', once((evt) => {
  fetch('path/to/url', {
    method: 'POST',
    body: JSON.stringify(formData),
    ...
  });
}));
```

如上代码所示，将“只执行一次”的过程抽象出来后，不论是我们的事件处理函数还是表单提交函数都只需要关注业务逻辑，而不需要添加`target.disabled=false`或则`target.removeEventListener`等语句了。我们的代码也不会因为疏忽了这些非业务逻辑的语句而报错。

除了上面这些情况，我们还可以对once方法做一些扩展。比如：我们定义了一个对象的初始化方法，这个方法只允许执行一次，如果用户不小心多次执行，我们想让函数抛出异常。我们修改once方法如下代码所示：

```js
function once(fn, replacer = null) {
  return function (...args) {
    if(fn) {
      const ret = fn.apply(this, args);
      fn = null;
      return ret;
    }
    if(replacer) {
      return replacer.apply(this, args);
    }
  };
}
```

那么我们就可以这样用：

```js
const obj = {
  init: once(() => {
    console.log('Initializer has been called.');
  }, () => {
    throw new Error('This method should be called only once.');
  }),
}

obj.init();
obj.init();
```

这样当我们第二次调用`obj.init()`时，就会抛出异常`new Error('This method should be called only once.');`。

<!-- 👉🏻 `once`是我们接触的第一个函数装饰器，它用来修饰一个函数，所以它的参数是函数，返回值也是函数。我们一般把参数和返回值都是函数的函数，叫做**高阶函数（High Ordered Functions）**。 -->

函数的装饰器是一种新的抽象思路，那么除了`once`外，函数装饰器的这种思路还能应用在哪些场景呢？

## 第三个故事：节流和防抖函数装饰器

<!-- 在前面那个项目中，使用once装饰器解决函数调用只执行一次的问题。 -->
除了`once`装饰器外，这一讲我们来认识另外两种常见的函数装饰器：节流和防抖。

<!-- 还有其他的问题可以用类似的思路来解决。最常见的一类包括函数的**节流**和**防抖**。 -->

### 节流

什么是节流，我们用一个例子来解释一下： 
<!-- 对一些频繁触发的事件，如果注册事件响应函数，实际上这个函数会被执行非常多次。最常见的场景是监听mousemove事件、resize事件和滚动条scroll事件。 -->
<!-- 我们来看一个例子： -->

```html
<div id="panel"></div>
```

```css
html, body {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}
#panel {
  display: inline-block;
  width: 360px;
  height: 360px;
  background: hsl(0, 50%, 50%);
}
```

```js
const panel = document.getElementById('panel');
panel.addEventListener('mousemove', (e) => {
  const {x, y} = e;
  e.target.style.background = `linear-gradient(${y}deg, 
    hsl(0, 50%, 50%),
    hsl(${0.5 * x}, 50%, 50%))`;
});
```

上面的代码是一个从真实的业务中抽象出来的一个简单的例子。我们监听panel元素的`mousemove`方法，然后根据鼠标移动的（`x、y`）位置改变元素的背景色，它的效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97569e50182944dc81c48dbd10b7c827~tplv-k3u1fbpfcp-zoom-1.image)

因为在这个例子中，仅仅只是修改元素的背景色，并没有负责的业务逻辑，所以频繁的响应`mousemove`事件没什么问题。

可是，假设现在我们需要将更改后的颜色发送给服务器保存，那么频繁触发送过多的`mousemove`事件，会导致过多的http请求，给服务器带来比较大的负担。在这种情况下，我们就要设计一个机制，来限制`mousemove`被频繁触发。这个限制的过程就是我们说的**节流**
<!-- 但是如果功能比较复杂的情况，比如我们要将改变后的颜色发送给服务端保存，那么频繁触发的过多的mousemove请求就会带来比较大的负担，这时候，我们就要设计一个机制，来限制mousemove被频繁触发。 -->

```js
panel.addEventListener('mousemove', (e) => {
  // 省略改变颜色的代码...

  //向服务器发送当前颜色
  saveToServer(...data);  // 应避免请求被频繁发起
});
```

那么，我们怎样实现节流呢？ 我们来看看下面的代码：
<!-- 一个比较好的方式是节流，比如限制每隔100毫秒操作一次： -->

[在线演示](https://junyux.github.io/FE-Advance/day04/index2-v1.html)

```js
const panel = document.getElementById('panel');
let throttleTimer = null;
panel.addEventListener('mousemove', (e) => {
  if(!throttleTimer) {
    const {x, y} = e;
    e.target.style.background = `linear-gradient(${y}deg, 
      hsl(0, 50%, 50%),
      hsl(${0.5 * x}, 50%, 50%))`;
    throttleTimer = setTimeout(() => {
      throttleTimer = null;
    }, 100);
  }
});
```

如上代码所示，我们使用定时器作为限制。当`throttleTimer`等于`null`时，执行`mousemove`事件函数。然后，我们启动定时器。当`mousemove`事件在100毫秒内再次触发的时候，因为`throttleTimer`还未被设置为`null`，所以这次的`mousemove`事件被忽略。直到100毫秒之后，`throttleTimer`再次被设置为`null`时，才能触发`mousemove`事件。

上面的代码，虽然我们使用定时器解决了节流的问题，但是并不通用。当下次再遇到需要节流功能的地方时，我们需要复制这个定时器代码。所以，我们需要将这个节流的过程抽象出来，让它成为通用的节流装饰方法。
<!-- 上面这个方法用定时器throttleTimer作为限制，能够简单达到效果，但是当然不具有通用性。 -->

和`once`类似，我们实现一个`throttle`函数装饰器，它限制某个函数在`ms`间隔中只执行一次：

```js
function throttle(fn, ms = 100) {
  let throttleTimer = null;
  return function (...args) {
    if(!throttleTimer) {
      const ret = fn.apply(this, args);
      throttleTimer = setTimeout(() => {
        throttleTimer = null;
      }, ms);
      return ret;
    }
  };
}
```

与`once`一样，`throttle`的第一个参数是个函数，返回值也是一个函数，它返回的函数修饰了参数`fn`。当每次成功调用后，产生一个`ms`毫秒后执行回调的定时器，并赋给`throttleTimer`。在定时器回调函数未执行时，因为t`hrottleTimer`变量有值，函数`fn`就不会被次执行。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dfebdbee2ab94723b065cde52ebe135b~tplv-k3u1fbpfcp-zoom-1.image)

有了这个函数，我们就可以使用它来实现节流了：

[在线演示](https://junyux.github.io/FE-Advance/day04/index2-v2.html)

```js
const panel = document.getElementById('panel');
panel.addEventListener('mousemove', throttle((e) => {
  const {x, y} = e;
  e.target.style.background = `linear-gradient(${y}deg, 
    hsl(0, 50%, 50%),
    hsl(${0.5 * x}, 50%, 50%))`;
}));
```

有趣的是，我们还可以使用这个`throttle`来实现我们上一个故事里的`once`：

```js
function throttle(fn, ms = 100) {
  let throttleTimer = null;
  return function(...args) {
    if(!throttleTimer) {
      const ret = fn.apply(this, args);
      throttleTimer = setTimeout(() => {
        throttleTimer = null;
      }, ms);
      return ret;
    }
  }
}

function once(fn) {
  return throttle(fn, Infinity);
}
```

这时的`once`就相当于一个定时器永不过期的`throttle`，从这一点上来说，`throttle`是比`once`更抽象的函数。

<!-- 同时也说明，**高阶函数之间是可以组合的**，理解这一点很重要，在后续我们会看到更多高阶函数组合的例子。 -->

### 防抖

除了`throttle`，与之类似的有防抖函数`debounce`。那么什么是防抖，我们也通过例子来了解一下：

```html
<div id="panel">
  <canvas></canvas>
</div>
```

```css
html, body {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}
#panel {
  width: 100%;
  height: 0;
  padding-bottom: 100%;
}
```

```js
const panel = document.getElementById('panel');
const canvas = document.querySelector('canvas');
function resize() {
  canvas.width = panel.clientWidth;
  canvas.height = panel.clientHeight;
}
function draw() {
  const context = canvas.getContext('2d');
  const radius = canvas.width / 2;
  context.save();
  context.translate(radius, radius);
  for(let i = radius; i >= 0; i -= 5) {
    context.fillStyle = `hsl(${i % 360}, 50%, 50%)`;
    context.beginPath();
    context.arc(0, 0, i, i, 0, Math.PI * 2);
    context.fill();
  }
  context.restore();
}

resize();
draw();

window.addEventListener('resize', () => {
  resize();
  draw();
});
```

在这例子里，我们在画布Canvas上实现一个不同色彩叠加的圆环，且允许画布的大小随页面宽度弹性改变，它的效果如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/339f86c9ddce40108e677bf4936b23fc~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示，在我们通过拖拽窗口改变窗口大小时，页面有些卡顿。这是因为（同`mousemove`类似）在拖拽窗口时，`resize`事件会反复触发，而每次触发的时候，Canvas都要重新绘制，而且绘制是一个耗时的过程，所以出现了图像卡顿。

那么如何解决这种卡顿的现象呢？我们可以让用户在操作过程中，不绘制Canvas，只在用户最后一次改变窗口大小的操作后才重新绘制Canvas。这一过程就是**防抖**。

<!-- 而实际上，用户可能并不关心窗口大小改变的过程，而只关心改变到新的窗口大小后，最终显示的结果。这时候，防抖函数debounce就派上用场了。 -->

同样，我们先用常规方式改写代码，让它具备防抖功能：

[在线演示](https://junyux.github.io/FE-Advance/day04/index3-v1.html)

```js
// 省略前面的代码...

resize();
draw();

let debounceTimer = null;
window.addEventListener('resize', () => {
  if(debounceTimer) clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    resize();
    draw();
  }, 500);
});
```

与`throttle`类似，我们还是使用一个定时器`debounceTimer`，但是它的逻辑有所变化。在`debounceTimer`定时器存在时，如果`resize`操作被触发，那么我们先清除上一次的`debounceTimer`，创建一个新的`debounceTimer`。这样的话，如果`resize`事件反复被触发，那么`debounceTimer`定时器就会被一直替换成新的，它的回调就不会被执行，只有当`resize`不再被触发超过一定时间（这里是500毫秒）后，它的回调才会被执行。简单来说，就是Canvas的绘制只发生在最后一次操作之后，中间的操作Canvas绘制都不会触发。这样就不会出现抖动现象了。

接下来，我们像之前一样，把`debounce`过程抽象出来：

```js
function debounce(fn, ms) {
  let debounceTimer = null;
  return function (...args) {
    if(debounceTimer) clearTimeout(debounceTimer);

    debounceTimer = setTimeout(() => {
      fn.apply(this, args);
    }, ms);
  };
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a531d96bfb7496d8d47ccdba062e455~tplv-k3u1fbpfcp-zoom-1.image)

然后，我们就可以用`debounce`来实现防抖了：

[在线演示](https://junyux.github.io/FE-Advance/day04/index3-v2.html)

```js
window.addEventListener('resize', debounce(() => {
  resize();
  draw();
}, 500));
```

<!-- 实际上，`debounce`和`throttle`是两个常用的工具函数，很多JS库带有这两个功能，其中最有名的库之一是`lodash`，这是前端工程师完成工作非常有用的工具库，也是小李常用的库。 -->

因为节流和防抖的函数非常相似，可能你会混淆。这里就再次前调一下它们的区别：

- 节流是让事件处理函数隔一个指定毫秒再触发
- 防抖则忽略中间的操作，只响应用户最后一次操作

<!-- 现在我们有了`once`、`debounce`、`throttle`等函数装饰器，或者说是高阶函数。可以理解，它们确实具有通用性，能够给我们的工作带来很大的帮助。但是，为什么说使用这些高阶函数就能够提升系统的可维护性呢，这需要我们进一步深入思考。 -->

回顾第一、二故事，我们了解了三种函数装饰器：`once`、`debounce`、`throttle`。这些函数装饰器有一个共同点：它们的参数是函数，返回值也是函数。我们把这种参数和返回值都是函数的函数，叫做**高阶函数（High Ordered Functions）**。 

高阶函数除了修饰函数外，还有哪些应用和好处呢？

## 第四个故事：函数拦截器

这个故事，我们将带你了解高阶函数的另外一个应用 —— 函数拦截器。

最近我们遇到一个头疼的问题，我们维护的一个工具库面临一次大的升级。这次版本升级中，一部分API将发生变化，旧的用法会被新的用法所取代。但是，由于很多业务中使用了老版本的工具库，不可能一次升级完，因此我们需要做一个平缓过渡：在当前这个版本中，先不取消这些旧的API，而是给它们增加一个提示信息，告诉调用它们的用户，这些API将会在下一次升级中被废弃。

要输出提示信息，可以使用`console.warn`。

```js
function deprecate(oldApi, newApi) {
  const message = `The ${oldApi} is deprecated.
Please use the ${newApi} instead.`;
  console.warn(message);
}
```

我们设计了一个`deprecate`的函数，如上代码所示。如果某个API需要废弃，那么在库中，修改该API的代码，在调用时输出信息，比如：

```js
export function foo() {
  deprecate('foo', 'bar');
  // do sth...
}
```

这样，当用户调用`foo`的时候，控制台上就会输出警告信息：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cc1bc24fa8943fda4cc1f961c4633b0~tplv-k3u1fbpfcp-zoom-1.image)

这么做当然是可以的，但是这么做是有风险的。因为这样做，我们需要找出库中所有要废弃的API，然后一一手动添加`deprecate`方法。这样做增加了手误的风险，导致原有的API出现错误。

所以我们需要思考：如何可以不改动原来库中API，又可以在这些废弃的API调用前显示提示信息呢？
<!-- 小李想到，其实可以不去库中一一寻找这些Api来修改，而是把它们统一导入到一个模块里，用高阶函数的方式进行修改： -->

```js
// deprecation.js
// 引入要废弃的 API
import {foo, bar} from './foo';
...
// 用高阶函数修饰
const _foo = deprecate(foo, 'foo', 'newFoo');
const _bar = deprecate(bar, 'bar', 'newBar');

// 重新导出修饰过的API
export {
  foo: _foo,
  bar: _bar,
  ...
}
```

如上代码所示，我们将库中要废弃的API导入到`deprecation`模块中。然后将这些废弃的方法，和提示信息丢到`deprecate`这个沙箱中处理，返回一个修饰过的函数，并将这些函数以相同的名字导出。这样当其他用户调用这些方法时，就会先经过`deprecate`这个沙箱，显示提示信息，然后再执行`foo`或`bar`方法的内容。

那么，这个`deprecate`函数是如何实现的呢，我们来看一下它的代码：

```js
function deprecate(fn, oldApi, newApi) {
  const message = `The ${oldApi} is deprecated.
Please use the ${newApi} instead.`;
  const notice = once(console.warn);

  return function(...args) {
    notice(message);
    return fn.apply(this, args);
  }
}
```

从上面的代码，我们可以看出，`deprecate`也是一个高阶函数。它输入一个`fn`函数，返回一个函数。`fn`就是要废弃的API。返回的函数是一个包含了打印提示信息，和`fn`调用的函数。这样，当我们执行这个返回的函数的时候，先执行了提示信息的打印，然后才执行原有的API方法。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e4a6e3ae9f46cda51337ca819cf9da~tplv-k3u1fbpfcp-zoom-1.image)

这里我们还添加了一个小细节，定义`notice = once(console.warn)`，用`notice`输出，这样的话，调用相同的函数只会在控制台显示一遍警告，就避免了输出太多重复的信息。

从这个例子，我们可以看到高阶函数另一个经典的使用场景，那就是，**当我们想要修改函数库中的某个API，我们可以选择不修改代码本身，而是对这个API进行修饰，修饰的过程可以抽象为拦截它的输入或输出。** 

这和web开发中的拦截器的思路不谋而合。基于这个思路，我们也可以设计一个简单的通用函数拦截器：

```js
function intercept(fn, {beforeCall = null, afterCall = null}) {
  return function (...args) {
    if(!beforeCall || beforeCall.call(this, args) !== false) {
      // 如果beforeCall返回false，不执行后续函数
      const ret = fn.apply(this, args);
      if(afterCall) return afterCall.call(this, ret);
      return ret;
    }
  };
}
```

`intercept`函数是一个高阶函数，它的第二个参数是一个对象，可以提供`beforeCall`、`afterCall`两个拦截器函数，分别“拦截”`fn`函数的执行前和执行后两个阶段。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3496fac3c2304794aeab3ce1755eb185~tplv-k3u1fbpfcp-zoom-1.image)

在执行前阶段，我们可以通过返回`false`阻止`fn`执行，在执行后阶段，我们可以用`afterCall`返回值替代`fn`函数返回值。

`intercept`有很多用途：

1. 我们可以随时监控一个函数的执行过程，不修改代码的情况下获取函数的执行信息：

[在线演示](https://junyux.github.io/FE-Advance/day04/index4-v1.html)

```js
function sum(...list) {
  return list.reduce((a, b) => a + b);
}

sum = intercept(sum, {
  beforeCall(args) {
    console.log(`The argument is ${args}`);
    console.time('sum'); // 监控性能
  },
  afterCall(ret) {
    console.log(`The resulte is ${ret}`);
    console.timeEnd('sum');
  }
});

sum(1, 2, 3, 4, 5);
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcf1b926bfb341f2878610fd2ea68149~tplv-k3u1fbpfcp-zoom-1.image)

2. 我们可以调整参数顺序：

```js
const mySetTimeout = intercept(setTimeout,  {
  beforeCall(args) {
    [args[0], args[1]] = [args[1], args[0]];
  }
});

mySetTimeout(1000, () => {
  console.log('done');
});
```

上面的代码，重新定义了一个新的定时器函数`mySetTimeout`，它的参数恰好和`setTimeout`相反。

3. 我们可以校验函数的参数类型：

```js
const foo = intercept(foo, {
  beforeCall(args) {
    assert(typeof args[1] === 'string');
  }
});
```

除了上述三点用途外，它可以根据你的业务需求，有很多用途。但最关键的是，这些事情是在不修改原函数代码的基础上做到的！

通过这三个例子，我们了解了高阶函数的一个基础应用，下一讲，我们将谈谈高阶函数在应用中的意义。

<!-- 而这一切，是动态编程语言以及函数式编程的高阶函数思想所赋予我们的能力，掌握这种思想方法和能力，你就能轻松重构代码，让你的代码库变得简洁优雅，有良好的可测试性和可维护性。 -->

## 第五个故事：函数的“纯度”、可测试性和可维护性

<!-- 与大部分前端工程师一样，小李在工作中积累了一些方便好用的工具函数，她将它们添加到自己的工具函数库中。 -->
在前端开发中，我们都会积累一些方便好用的工具函数，且会将它们添加到工具函数库中，以方便在其它项目中复用。

其中有两个工具函数是这样的：

```js
export function setStyle(el, key, value) {
  el.style[key] = value;
}

export function setStyles(els, key, value) {
  els.forEach(el => setStyle(el, key, value));
}
```

这两个函数的功能是给元素设置样式的，其中`setStyle`只给一个元素设置样式，而`setStyles`则给多个元素设置样式。

这两个函数功能单一，看起来非常简单，但是它们有一个共同的缺点——那就是它们都依赖外部的环境（参数`el`元素），同时也改变这个环境。这样定义函数有什么问题呢？

把自己想象成测试人员，如果需要给`setStyle`或者`setStyles`这样的函数进行**黑盒测试**，我们必须给它构建测试的环境。比如，针对上面两个函数，我们需要构建不同的DOM元素结构，然后获取元素或元素列表，然后根据操作后DOM元素的呈现结果判定函数的实现是否正确。这必然导致测试成本的提高。所以，为了降低工具库测试的成本，提高函数的**测试性**，我们需要对工具库进行重构。

要提高函数的可测试性，需要提高函数的**纯度**，也就是需要减少函数对外部环境的依赖，以及减少该函数对外部环境的改变。这样的函数我们成为**纯函数**。

一个严格的纯函数，是具有**确定性**、**无副作用**，**幂等**的特点。也就是说，纯函数不依赖外部环境，也不改变外部环境，不管调用几次，不管什么时候调用，只要参数确定，返回值就确定。这样的函数，就是纯函数。

下面的代码就是我们针对上面两个工具函数的重构：

```js
function batch(fn) {
  return function(subject, ...args) {
    if(Array.isArray(subject)) {
      return subject.map((s) => {
        return fn.call(this, s, ...args);
      });
    }
    return fn.call(this, subject, ...args);
  }
}

export const setStyle = batch((el, key, value) => {
  el.style[key] = value;
});
```

如上代码所示，`batch`是一个高阶函数。在它的返回函数中，第一个参数`subject`**如果是一个数组，则以这个数组的每个元素为第一个参数，依次迭代调用`fn`，将结果作为数组返回**。如果`subject`不是数组，那么直接调用`fn`，并将结果返回。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/300ebcf11df7403b91a3b45453ae571c~tplv-k3u1fbpfcp-zoom-1.image)

所以经过`batch`之后的`setStyle`函数拥有了单个操作或者批量操作元素的能力，相当于原先的`setStyle`和`setStyles`的结合。

我们来看一个完整的例子 —— 将`ul`元素下所有的奇数行的`li`元素的字体颜色修改为红色：

[在线演示](https://junyux.github.io/FE-Advance/day04/index5-v1.html)

```html
<ul>
  <li>1</li>
  <li>2</li>
  <li>3</li>
  <li>4</li>
  <li>5</li>
  <li>6</li>
  <li>7</li>
</ul>
```

```js
function batch(fn) {
  return function (subject, ...args) {
    if(Array.isArray(subject)) {
      return subject.map((s) => {
        return fn.call(this, s, ...args);
      });
    }
    return fn.call(this, subject, ...args);
  };
}

const setStyle = batch((el, key, value) => {
  el.style[key] = value;
});

const items = document.querySelectorAll('li:nth-child(2n+1)');

setStyle([...items], 'color', 'red');
```

上面的代码中，虽然`setStyle`依然不是纯函数，但是`batch`是一个纯函数。也就是说，经过重构的代码，减少了工具库的**非纯函数**，提升了库中纯函数的数量，这样就提升了函数库的可测试性和可维护性。

以`batch`函数为例，我们来看看这时的黑盒测试是多么的简单：
<!-- 我们来看看`batch`函数的黑盒测试，只需要给它传入参数，判断它的返回结果： -->

```js
const list = [1, 2, 3, 4];
const double = batch(num => num * 2);

double(list); // 2, 4, 6, 8
```

如上代码所示，我们只需要给`batch`传入参数，判断它的返回结果是否和预期一致即可，并不需要为它构建HTML环境。

可能这时，你会问，如果只是合并`setStyle`和`setStyles`，也可简单的将这两个方法合并为如下形式：

```js
function setStyle(el, key, value) {
  if(Array.isArray(el)) {
    return el.forEach((e) => {
      setStyle(e, key, value);
    });
  }
  el.style[key] = value;
}
```

这么做，首先它破坏了函数职责单一性的原则。其次，工具库里还有其他类似的函数，比如：

```js
function addState(el, state) {
  removeState(el, state);
  el.className = el.className ? `${el.className} ${state}` : state;
}

function removeState(el, state) {
  el.className = el.className.replace(new RegExp(`(^|\\s)${state}(\\s|$)`, 'g'), '');
}

function addStates(els, state) {
  els.forEach(el => addState(el, state));
}
```

如果要修改，那么还得把这些方法一起修改为下面的样子：

```js
function addState(el, state) {
  if(Array.isArray(el)) {
    return el.forEach((e) => {
      addState(e, state);
    });
  }
  removeState(el, state);
  el.className = el.className ? `${el.className} ${state}` : state;
}

function removeState(el, state) {
  if(Array.isArray(el)) {
    return el.forEach((e) => {
      removeState(e, state);
    });
  }
  el.className = el.className.replace(new RegExp(`(^|\\s)${state}(\\s|$)`, 'g'), '');
}
```

而有了`batch`方法后，因为`const setStyle = batch(...)`是通过函数装饰器的修饰将函数变换为具有批量处理功能，并不违反定义时的职责单一原则，而且测试的时候，只要保证纯函数`batch`的正确性，就完全不用担心被`batch`变换后的函数的正确性。

而且，修改其他的函数也不用那么麻烦了。把所有需要拥有批量处理功能的函数统统用`batch`装饰一下就可以了：

```js
// 统一的批量化处理
addState = batch(addState);
removeState = batch(removeState);
```

这样我们通过设计`batch`高阶函数，让这个库的纯函数增加，非纯函数减少了，这最终大大提升了库的可测试性和可维护性。这就是我们为什么需要使用高阶函数过程抽象来设计和重构函数库的原因。

`batch`只是其中一个高阶函数，就像前面的`once`、`throttle`、`debounce`一样，只是众多函数装饰器中的一个，我们还可以实现其他更多的函数装饰器，用它们来一步一步改造我们的工具函数库。

## 第六个故事：高阶函数的范式

前面的几个故事中，我们得到了几个高阶函数，包括`once`、`throttle`、`debounce`和`batch`，它们的功能各不相同，但是也有共同点，从中我们可以抽取出创建高阶函数的**范式**：

```js
function HOF0(fn) {
  return function(...args) {
    return fn.apply(this, args);
  }
}
```

`HOF0`是高阶函数的**等价范式**，或者说，`HOF0`修饰的函数功能和原函数`fn`的功能完全相同。因为被修饰后的函数就只是采用调用的`this`上下文和参数来调用`fn`，并将结果返回。也就是说，执行它和直接执行`fn`完全没区别。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b382c247224f4ab4bdea99f65a069f42~tplv-k3u1fbpfcp-zoom-1.image)

```js
function foo(...args) {
  // do anything.
}
const bar = HOF0(foo);

console.log(foo('something'), bar('something')); // 调用foo和调用bar完全等价
```

所以`HOF0`是基础范式，其他的函数装饰器就是在它的基础上，要么对**参数进行修改**，如`batch`，要么对**返回结果进行修改**，如`once`、`throttle`、`debounce`和`batch`。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c1b153849884773bfd5f587bb77ff16~tplv-k3u1fbpfcp-zoom-1.image)

那么同样，其他的高阶函数也可以在这基础上设计出来。

比如，我们可以设计出连续执行的函数，用来递归执行，类似于数组的`reduce`方法，但更灵活。

```js
function continous(reducer) {
  return function (...args) {
    return args.reduce((a, b) => reducer(a, b));
  };
}
```

有了`continous`，我们可以创建能够递归处理输入的函数，如：

```js
const add = continous((a, b) => a + b);
const multiply = continous((a, b) => a * b);

console.log(add(1, 2, 3, 4)); // 1 + 2 + 3 + 4 = 10

console.log(multiply(1, 2, 3, 4, 5)); // 1 * 2 * 3 * 4 * 5 = 120
```

与`batch`类似，`continous`也可以用来创建批量操作元素的方法，只不过参数和用法需要调整一下，用起来也没有`batch`那么好用。如下代码所示：

[在线演示](https://junyux.github.io/FE-Advance/day04/index5-v2.html)

```js
const setStyle = continous(([key, value], el) => {
  el.style[key] = value;
  return [key, value];
});

const list = document.querySelectorAll('li:nth-child(2n+1)');
setStyle(['color', 'red'], ...list);
```

注意到因为continous是递归迭代执行，我们要把`list`展开传入`setStyle`。

如果我们想要直接使用`list`作为参数而不是传`...list`，我们可以再实现一个高阶函数来处理它：

```js
function fold(fn) {
  return function (...args) {
    const lastArg = args[args.length - 1];
    if(lastArg.length) {
      return fn.call(this, ...args.slice(0, -1), ...lastArg);
    }
    return fn.call(this, ...args);
  };
}
```

`fold`函数判断最后一个参数是一个数组或类数组（如NodeList），那么将它展开传给原函数`fn`（相对于被修饰的原函数而言是折叠了参数，所以用`fold`命名这个高阶函数）。

所以我们再改一下`setStyle`:

[在线演示](https://junyux.github.io/FE-Advance/day04/index5-v3.html)

```js
const setStyle = fold(continous(([key, value], el) => {
  el.style[key] = value;
  return [key, value];
}));

const list = document.querySelectorAll('li:nth-child(2n+1)');

setStyle(['color', 'red'], list);
```

我们给`setStyle`在`continous`基础上再加一个`fold`的装饰，就可以达到我们的目的，list不用`...`展开。

那么接下来，我们可以调整一下参数顺序，让setStyle更接近batch那一版：

```js
function reverse(fn) {
  return function (...args) {
    return fn.apply(this, args.reverse());
  };
}
```

`reverse`是另一个高阶函数，它将函数的参数调用顺序颠倒：

[在线演示](https://junyux.github.io/FE-Advance/day04/index5-v4.html)

```js
const setStyle = reverse(fold(continous(([key, value], el) => {
  el.style[key] = value;
  return [key, value];
})));

const list = document.querySelectorAll('li:nth-child(2n+1)');

setStyle(list, ['color', 'red']);
```

如上代码所示，setStyle的参数变成了`list`和`['color','red']`。

然后，我们可以把参数`['color', 'red']`展开，所有我们需要实现一个与`fold`相反的`spread`高阶函数：

```js
function spread(fn) {
  return function (first, ...rest) {
    return fn.call(this, first, rest);
  };
}
```

所以最终我们得到了和上一个故事一样的效果的`setStyle`方法：

[在线演示](https://junyux.github.io/FE-Advance/day04/index5-v5.html)

```js
const setStyle = spread(reverse(fold(continous(([key, value], el) => {
  el.style[key] = value;
  return [key, value];
}))));

const list = document.querySelectorAll('li:nth-child(2n+1)');

setStyle(list, 'color', 'red');
```

只不过我们这一次给原始函数套了四个装饰器 `spread(reverse(fold(continous(...))))`。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/072624e682b54a1089b5ad146af37a4c~tplv-k3u1fbpfcp-zoom-1.image)

所以，就这个例子来说，相当于：

```js
function batch(fn) {
  return spread(reverse(fold(continous(fn))));
}
const setStyle = batch(setStyle);
```

当然这里还有个细微差异，就是这一版原始函数的参数顺序不一样，而且要求有返回值:

```js
// 这是原始函数
([key, value], el) => {
  el.style[key] = value;
  return [key, value];
}
```

不过这也已经足够说明**高阶函数可以任意组合**，形成更强大的功能。

另外，像这样`spread(reverse(fold(continous...)))`嵌套的写法，我们也可以用高阶函数改变成更加友好的形式：

```js
function pipe(...fns) {
  return function(input) {
    return fns.reduce((a, b) => {
      return b.call(this, a);
    }, input);
  }
}
```

我们定义一个叫`pipe`的高阶函数，它的参数是一个函数列表，返回一个函数，这个函数以参数input对列表中的函数依次迭代，并将最终结果返回。

例如：

```js
const double = (x) => x * 2;
const half = (x) => x / 2;
const pow2 = (x) => x ** 2;

const cacl = pipe(double, pow2, half);
const result = cacl(10); // (10 * 2) ** 2 / 2 = 200
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/753682188f0c41509b00b9ff523bbea2~tplv-k3u1fbpfcp-zoom-1.image)

👉🏻_pipe_就像一根管道一样，输入的数据顺序经过一系列函子，得到最终输出。实际上这个模型也是**函数式编程**的基本模型，高阶函数是函数式编程的基础，关于函数式编程，后续我们会在其他课程中深入讨论。

有了`pipe`，我们可以运用`pipe`到前面的几个高阶函数，将`batch`用`pipe`来表示为：

```js
const batch = pipe(continous, fold, reverse, spread);
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5231a16869dd4f8c94b98ab980d24d34~tplv-k3u1fbpfcp-zoom-1.image)

更有趣的是，`pipe`本身也可以用高阶函数`continous`重新定义为：

```js
const pipe = continous((prev, next) => {
  return function(input) {
    return next.call(this, prev.call(this, input));
  }
});
```

在这里，我们再一次看到高阶函数组合的威力。如果要类比的话，就像数学中，定义少数几条基本公理就能够推导并建立整个系统一样，我们也可以通过定义几个基本的高阶函数，创造出一整套图灵完备的高阶函数系统，并用它来彻底重构我们的基础库，让基础库中只有高阶纯函数和一些基本的原子操作（就像`(el, key, value）=> {el.style[key] = value;}`这种简单操作）。如果这样做，那么我们的基础库的可维护性就会非常高。


## 5.第五日：用好异步

# 第五天

## 第一个故事：多个异步间的状态同步

第三天中，我们了解了JS中的三种异步方式：定时器、Promise和async/wait。

在不过多考虑代码的复用性和扩展性的时候，其实这三种实现方式差别不大。第一种方式因为有回调嵌套，结构上稍稍不那么美观，而第二、三种方式结构实际差不多，第三种方式之所以好，是因为它更接近于自然语言，以及人思考问题的模式。但本质上，这三种异步表达方式并没有太大的区别。不过，这是因为我们的问题比较简单。

如果我们考虑更复杂的问题，比如一个小游戏中需要几个异步操作，而这几个异步操作又同时需要维护了一个状态，（比如：游戏结束的状态）。这时候，我们需要一种机制来维护异步操作间的状态控制。一个最简单粗暴的做法就是维护一个全局变量，让每个异步操作监控这个变量。只要其中一个异步操作结束时，这个变量就被置为结束状态，然后其他异步操作在监控到这个状态的时候，也中止自身的异步进程。但是使用这样的局部变量不仅增加了代码的复杂度，也使得模块间的耦合更高。所以，我们应该尽量避免使用这样的全局变量。

下面，我们通过一个简单的打字游戏来看看有没有其他方式能够实现各异步过程之间的状态同步。

这个游戏是这样的：界面上会随机出现一段文本，用户如果在规定时间内打完这段文本，那么用户胜出，否则失败。

这个游戏的HTML和CSS结构如下：

```html
<div id="main">
  <div id="panel"></div> <!-- 显示系统生成的文本 -->
  <div id="typed"></div> <!-- 显示用户实际打印的文本 -->
  <div id="starting"></div> <!-- 显示开场倒计动画 -->
  <div id="countdown">00:00</div>
</div>
```

```css
html, body {
  width: 100%;
  height: 100%;
  padding: 6px;
  margin: 0;
  overflow: hidden;
}

#main {
  position: relative;
  display: inline-block;
}

#panel, #typed {
  border: solid 1px #000;
  line-height: 1.5;
  white-space: pre-wrap;
  margin: 0;
  padding: 18px 6px 6px 6px;
  color: #0006;
}

#panel {
  width: 600px;
  min-height: 400px;
}
#panel:empty {
  cursor: pointer;
}
#panel:empty::after {
  content: '鼠标点击后开始';
}

#typed {
  max-width: 600px;
  position: absolute;
  top: 0;
  border-color: transparent;
  color: #008;
  background-color: #eea6;
  background-clip: content-box;
  overflow: hidden;
}
#typed:empty {
  background-color: transparent;
}

#starting {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 3rem;
}

#countdown {
  position: absolute;
  top: 0;
  right: 10px;
  opacity: 0.3;
}
```

游戏界面分为4个部分，`#panel`显示要打的文章，`#typed`显示已经打出的部分，`#starting`是用来显示开始时倒计时的界面，`#countdown`是显示正在打字时的倒计时界面。游戏效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/193a7fafbb0f4d65bdc7b68a9eb60dc8~tplv-k3u1fbpfcp-zoom-1.image)

这个游戏包含3个异步操作：

1. 游戏开场动画
1. 游戏时间倒计
1. 用户输入操作

<!-- 要实现这个游戏的效果呢，用普通的事件响应的方式当然可以做到，但是用Promise和async/await方式实现要简单的多，而且不用在多个控制点之间做状态同步。 -->
<!-- 正常情况下，我们是要同步状态的，比如，如果用户在倒计结束时还没完成打字，我们要将倒计时结束的状态同步给控制打字的组件或函数，告诉它停止接受输入；反之，如果用户在倒计时结束前已经打完全篇文章，我们也要将状态同步给倒计时的组件或函数，告诉它停止倒计时。而使用Promise和async/await，我们可以不做这样的状态同步，而且用更符合自然人思维习惯的方式来描述整个游戏过程。 -->

首先，我们先来实现游戏开动画的异步过程：

```js
const text = `If you already have experience making drawings with computers, you know that in that process you draw a circle, then a rectangle...
...
...Each pipe is also known as a thread.`

// 将一段文本赋值给panel元素
const panel = document.getElementById('panel');
panel.addEventListener('click', main);

function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function starting(el, count = 3) {
  el.innerText = count;
  while(count--) {
    await wait(1000);
    el.innerText = count;
  }
  el.innerText = '';
}

const startingEl = document.getElementById('starting');

// 游戏主体
async function main() {
  panel.innerText = text;
  await starting(startingEl);
}
```

这段代码中，我们定义一个开始前倒计时的异步函数`starting`。它有两个参数，一个参数是要更新状态的元素，另一个参数是倒计时执行的秒数，默认是3秒。我们通过执行定时器异步函数`await wait(1000)`来每隔1秒钟更新一次倒计时。然后，我们在游戏的主体`main`函数中执行，这样游戏的开场动画（3秒倒计时）就完成了。

接着，我们还要实现两个异步过程，一个是打字中的倒计时，另一个是打字时的键盘输入，我们先实现其中简单的，打字中的倒计时：

```js
async function countDown(el, sec) {
  while(sec--) {
    const minute = Math.floor(sec / 60);
    const second = sec % 60;
    const time = `${minute > 10 ? minute: `0${minute}`}:${second > 10 ? second: `0${second}`}`;
    el.innerText = time;
    await wait(1000);
  }
}
```

打字中的倒计时和开始前的倒计时原理差不多，我们仍然是使用`await wait(1000)`这个异步方法来每秒更新一次对应的元素的内容，不过我们要将时间给格式化成`分:秒`的形式。

然后，我们实现打字中的键盘输入：

```js
async function typings(el, text) {
  for(let i = 0; i < text.length; i++) {
    const char = text[i];
    el.innerText = '_';
    const key = await new Promise((resolve) => {
      document.addEventListener('keydown', function f({key}) {
        if(key ===  char) {
          document.removeEventListener('keydown', f);
          resolve(key);
        }
      });
    });
    el.innerText = el.innerText.slice(0, -1) + key + '_';
  }
}
```

如上代码所示，异步函数`typings`等待键盘输入。如果用户输入的键值与文本内容中当前应输入的字符相同，那么我们更新`#typed`元素（这里的el参数）中的`innerText`并等待下一个字符的输入。

最后，我们在`main`函数中组合这三个异步内容：

```js
// ...省略其他代码...

async function main() {
  panel.innerText = text;
  await starting(startingEl); //开场动画
  const countDownPromise = countDown(countdownEl, 10); // 游戏倒计时
  const typingPromise = typings(typedEl, text); // 用户输入操作
  await Promise.race([countDownPromise, typingPromise]);
  console.log('结束');
}
```

在`main`函数中，我们用`Promise.race`来执行倒计时和打字输入两个异步函数。`Promise.race`表示当其中一个异步函数`resove`时，它就会`resolve`，所以，不论是倒计时还是打字输入，哪一个先结束，游戏就会结束。

可能你认为到这里我们的打字游戏就完成了。但是，上述的代码却存在这样一个问题：虽然游戏结束了，但是游戏倒计时和用户输入的这两个异步操作的状态却没有同步。

当用户并未在游戏时间内完成打字任务时，虽然`countDown`的异步已经结束，但是`typingPromise`却还在不断地监听`keydown`事件。所以，即使游戏结束了，用户依然能继续打字。这显然不符合游戏的逻辑。

要解决这个问题，就像前面叙述的，我们可以采取简单粗暴的方式，通过外部状态告诉`typingPromise`不要继续监听输入事件。或者，我们发送游戏结束的消息给`typingPromise`。不过这两种方法无论哪一种，都增加额外的代码复杂度。

一个更加优雅的做法是，通过JavaScript的生成器函数来避免这种状态耦合。

```js
function * typings(text) {
  for(let i = 0; i < text.length; i++) {
    const char = text[i];
    yield new Promise((resolve) => {
      document.addEventListener('keydown', function f({key}) {
        if(key ===  char) {
          document.removeEventListener('keydown', f);
          resolve(key);
        }
      });
    });
  }
}
```

上面的代码中，我们去掉了`typings`直接操作`#typed`元素的代码，并将`async`函数修改为生成器函数，它的`yield`操作每次返回一个`Promise`对象。

然后我们修改`main`函数：

```js
async function main() {
  panel.innerText = text;
  await starting(startingEl);
  const countDownPromise = countDown(countdownEl, 10);
  typedEl.innerText = '_';
  for(const typing of typings(text)) {
    const key = await Promise.race([countDownPromise, typing]);
    if(key) {
      typedEl.innerText = `${typedEl.innerText.slice(0, -1)}${key}_`;
    } else {
      break;
    }
  }
  console.log('结束');
}
```

我们通过`for...of`来迭代生成器，每次循环拿到一次输入的`Promise`，将它和`countDownPromise`做`Promise.race`操作。如果是输入的`Promise`先返回，那么我们可以拿到一个`key`值，用这个`key`值去更新`typedEl`的内容。否则，就是倒计时结束，那么我们用`break`来跳出循环结束游戏。这样就能保证当游戏结束时，不论是倒计时或者用户输入的操作都中止了。

完整的JS代码如下：

[在线演示](https://junyux.github.io/FE-Advance/day05/index1.html)

```js
const text = `If you already have experience making drawings with computers, you know that in that process you draw a circle, then a rectangle, a line, some triangles until you compose the image you want. That process is very similar to writing a letter or a book by hand - it is a set of instructions that do one task after another.

Shaders are also a set of instructions, but the instructions are executed all at once for every single pixel on the screen. That means the code you write has to behave differently depending on the position of the pixel on the screen. Like a type press, your program will work as a function that receives a position and returns a color, and when it's compiled it will run extraordinarily fast. 

Why are shaders fast? To answer this, I present the wonders of parallel processing.

Imagine the CPU of your computer as a big industrial pipe, and every task as something that passes through it - like a factory line. Some tasks are bigger than others, which means they require more time and energy to deal with. We say they require more processing power. Because of the architecture of computers the jobs are forced to run in a series; each job has to be finished one at a time. Modern computers usually have groups of four processors that work like these pipes, completing tasks one after another to keeping things running smoothly. Each pipe is also known as a thread.`;

function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

async function starting(el, count = 3) {
  el.innerText = count;
  while(count--) {
    await wait(1000);
    el.innerText = count;
  }
  el.innerText = '';
}

function* typings(text) {
  for(let i = 0; i < text.length; i++) {
    const char = text[i];
    yield new Promise((resolve) => {
      document.addEventListener('keydown', function f({key}) {
        if(key === char) {
          document.removeEventListener('keydown', f);
          resolve(key);
        }
      });
    });
  }
}

async function countDown(el, sec) {
  while(sec--) {
    const minute = Math.floor(sec / 60);
    const second = sec % 60;
    const time = `${minute > 10 ? minute : `0${minute}`}:${second > 10 ? second : `0${second}`}`;
    el.innerText = time;
    await wait(1000);
  }
}

const typedEl = document.getElementById('typed');
const startingEl = document.getElementById('starting');
const countdownEl = document.getElementById('countdown');

const panel = document.getElementById('panel');
panel.addEventListener('click', start);

async function start() {
  panel.innerText = text;
  await starting(startingEl);
  const countDownPromise = countDown(countdownEl, 10);
  typedEl.innerText = '_';
  for(const typing of typings(text)) {
    const key = await Promise.race([countDownPromise, typing]);
    if(key) {
      typedEl.innerText = `${typedEl.innerText.slice(0, -1)}${key}_`;
    } else {
      break;
    }
  }
  console.log('结束');
}
```

<!-- 我们可以看到，使用异步`Promise`和`async/await`可以以非常简单的方式处理这种需要持续与用户交互的场景，它实现的代码也非常简单易懂，基本上和同步代码从结构和逻辑上区别不大，这样就极大地提升了代码的可读性，从而让代码变得易于维护和易于扩展。 -->
我们可以看到，虽然使用异步`Promise`和`async/await`可以以非常简单的方式处理这种需要持续与用户交互的场景，但是也需要注意多个异步间的状态同步，不要让我们代码存在潜在的逻辑错误或者隐患。

## 第二个故事：异步信号

<!-- 这个故事，我们来聊聊Promise的另一种应用场景：异步信号。通过信号的状态变化来进行组件之间的控制，这样，我们就可以把组件之间需要协同状态的相互耦合简化为控制状态改变这一比较简单的操作。 -->
这个故事，我们想通过一个简单的例子，让你了解Promise的另一个应用场景：异步信号。

这个例子很简单：有若干个用户参与，每个用户从1到10中选择一个数字作为幸运数字，而系统一秒钟随机产生一个1到10的数字，若这个数字和用户的幸运数字相同，则该用户胜出。

这个任务很简单，我们可以不使用Promise，直接将每一秒钟生成的数字与用户的数字逐一比较，选出胜出的用户。但是如果这样做，我们需要在定时器模块维护一个用户列表信息，这增加了代码的耦合。如果使用异步信号，则可以避免这样的耦合。
<!-- 当然，类似的任务其实还可以使用第六日中的“中间人”模式或者状态机来实现，但是如果这一个任务是纯异步的，那么这种模式并不好用。所以，你可以将这个例子看作是了解什么是异步信号的一个媒介。 -->

下面我们就来看看这个异步信号是如何实现的。

<!-- 那么什么是异步信号呢？我们用一个简单的例子来说明什么是异步信号、如何创建异步信号、怎么使用异步信号。 -->
<!-- 假如说，我们要实现一个小游戏，有若干个用户参与，每个用户从1到10中选择一个数字作为幸运数字，而系统一秒钟随机产生一个1到10的数字，若这个数字和用户的幸运数字相同，则该用户胜出。 -->
<!-- 当然这个任务简单到不用异步信号也可以做，不过我们想一下，如果不用异步信号来做，我们需要将每一秒钟生成的数字与用户的数字逐一比较，选出胜出的用户，那也就是说，我们需要有一个地方保存用户的全部信息。但是用异步信号则可以省去这一步。
具体怎么做呢？ -->

我们知道，一般的 Promise 对象，其状态是在作用域内部控制的：

```js
const promise = new Promise((resolve, reject) => {
  // 在这里调用 resolve、 reject 来改变状态
});
```

这么设计能够避免 Promise 状态的泄漏导致滥用。

但是现在，我们需要利用它作用为异步信号，那么我们就必须在外部控制这个 promise 状态。
<!-- 如果我们需要利用它作为异步信号控制多个组件间的状态的话，我们就需要在外部控制这个promise对象的状态： -->

```js
function defer() {
  const deferred = {};
  deferred.promise = new Promise((resolve, reject) => {
    deferred.resolve = resolve;
    deferred.reject = reject;
  });
  return deferred;
}

const deferred = defer();
deferred.resolve(); // 在外部控制 promise 状态
```

如上代码所示，`defer()`函数返回一个`deferred`对象。它包含 `{promise, resolve, reject}` 三个属性。然后，我们可以通过`deferred.resolve()`在外部控制`deferred`中的`promise`的状态了（即`deferred.promise`）。

有了这个`deferred`对象后，我们就可以用它来实现异步信号类 Singal：

```js
function defer() {
  const deferred = {};
  deferred.promise = new Promise((resolve, reject) => {
    deferred.resolve = resolve;
    deferred.reject = reject;
  });
  return deferred;
}

const _state = Symbol('state');
const _checkers = Symbol('checker');

export class Signal {
  constructor(initState) {
    this[_state] = initState;
    this[_checkers] = new Map();
  }

  get state() {
    return this[_state];
  }

  set state(value) {
    // 每次状态变化时，检查未结束的 defer 对象
    [...this[_checkers]].forEach(([promise, {type, deferred, state}]) => {
      if(type === 'while' && value !== state // 当信号状态改变时，while 信号结束
        || type === 'until' && value === state // 当信号状态改变为对应的 state 时，until 信号结束
      ) {
        deferred.resolve(value);
        this[_checkers].delete(promise);
      }
    });
    this[_state] = value;
  }

  while(state) {
    const deferred = defer();
    if(state !== this[_state]) {
      // 如果当前状态不是 while 状态， while 的 deferred 结束
      deferred.resolve(this[_state]);
    } else {
      // 否则将它添加到 checkers 列表中等待后续检查
      this[_checkers].set(deferred.promise, {type: 'while', deferred, state});
    }
    return deferred.promise;
  }

  until(state) {
    const deferred = defer();
    if(state === this[_state]) {
      // 如果当前状态就是 until 状态， until 的 deferred 结束
      deferred.resolve(this[_state]);
    } else {
      // 否则将它添加到 checkers 列表中等待后续检查
      this[_checkers].set(deferred.promise, {type: 'until', deferred, state});
    }
    return deferred.promise;
  }

  delete(promise) {
    this[_checkers].delete(promise);
  }

  deleteAll() {
    this[_checkers].clear();
  }
}
```

这个类很长，我们一步步来分析它。

首先是它的构造函数：

```js
const _state = Symbol('state');
const _checkers = Symbol('checker');

class Signal {
  constructor(initState) {
    this[_state] = initState;
    this[_checkers] = new Map();
  }
  ...
}
```

这个类有两个私有属性——`_state`和`_checkers`。就我们这个例子来说，前者用来存储当前定时器发出的幸运数字。后者用来保存用户给出数字（这个数字信息被保持在`deferred`对象中）。
<!-- 这个类有一个私有属性`_state`来保存状态，有一个私有属性`_checkers`是一个`Map`，用来保存状态切换时待改变的`deferred`对象。 -->

然后，Signal提供了两种信号“原语”：`while`和`until`:

```js
while(state) {
  const deferred = defer();
  if(state !== this[_state]) {
    // 如果当前状态不是 while 状态， while 的 deferred 结束
    deferred.resolve(this[_state]);
  }
  else {
    // 否则将它添加到 checkers 列表中等待后续检查
    this[_checkers].set(deferred.promise, {type: 'while', deferred, state});
  }
  return deferred.promise;
}

until(state) {
  const deferred = defer();
  if(state === this[_state]) {
    // 如果当前状态就是 until 状态， until 的 deferred 结束
    deferred.resolve(this[_state]);
  }
  else {
      // 否则将它添加到 checkers 列表中等待后续检查
    this[_checkers].set(deferred.promise, {type: 'until', deferred, state});
  }
  return deferred.promise;
}
```

这段代码中，`while(state)`表示当信号的状态保持在`state`状态时，将`deferred`对象保存到`_checkers`集合中，并返回`deferred.promise`，否则`resolve`这个`deferred`对象。

`until(state)`表示当信号的状态保持直到`state`状态后，将`deferred`对象`resolve`，否则将`deferred`保存到`_checkers`集合中，并返回`deferred.promise`。

这两个方法主要是提供给外部使用者使用。使用者可以选择采用`while`类型信号或者`util`类型信号来控制自身的状态。

然后，Signal通过`state`的`setter`接收其它模块发来的信号（比如：定时器模块）：

```js
set state(value) {
  // 每次状态变化时，检查未结束的 defer 对象
  [...this[_checkers]].forEach(([promise, {type, deferred, state}]) => {
    if(type === 'while' && value !== state // 当信号状态改变的时，while 信号结束
      || type === 'until' && value === state // 当信号状态改变为对应的 state 时，until 信号结束
    ) {
      deferred.resolve(value); 
      this[_checkers].delete(promise);
    }
  });
  this[_state] = value;
}
```

如上代码所示，当Signal收到信号后，先遍历`_checkers`集合。如果当前是`while`原语，且新状态不等于`while`的状态，那么执行`resolve`将`promise`状态改变，并将这个`deferred`对象从`Map`中移除。同样，如果是`until`原语，且新状态等于`until`状态，也执行`resolve`将`promise`状态改变，并将这个`deferred`对象从`Map`中移除。这样，我们就可以在`Signal`状态改变时，触发对应的`promise`状态改变了。

有了这个Signal类，我们就可以非常简单地实现前面的需求。

首先，创建一个Signal对象，这个对象每隔一秒钟接受一次定时器发出的数字：

```js
const lucky = new Signal();

const timerID = setInterval(() => {
  const num = Math.ceil(Math.random() * 10);
  console.log(num);
  lucky.state = num;
}, 1000);
```

然后我们添加若干个比较数字的“人”：

```js
async function addLuckyBoy(name, num) {
  await lucky.until(num);
  console.log(`${name} is lucky boy!`);
  clearInterval(timerID);
  lucky.deleteAll(); // 删除checkers中的所有promise对象
}

addLuckyBoy('张三', 3);
addLuckyBoy('李四', 5);
addLuckyBoy('王五', 7);
```

这里我们采用了`until`的信号模式：每个用户手持自己的幸运数字，直到其中一个用户的数字和系统给出的数字相符的时候，暂停定时器，并将这个用户的`deferred`对象`resolve`，同时将其他没有中签的用户的`deferred`对象从集合中删除。这样我们的幸运者就被选出了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/350ad51015124742b8820b8e36fcda83~tplv-k3u1fbpfcp-zoom-1.image)

<!-- 当然，这个任务其实还可以使用第六日中的“中间人”模式或者状态机来实现，但是如果这一个任务是纯异步的，那么这种模式并不好用。所以，你可以将这个例子看作是了解什么是异步信号的一个媒介。 -->
从这个例子我们可以看出，利用异步信号，我们的状态发生器模块（比如：定时器函数）只需要单纯地改变信号的状态，不再需要关心具体细节（比如有多少“人”参与这个游戏）。当状态变化时，可以由信号为媒介，通过`deferred`对象异步地通知对应的组件作出反应。

当然多组件之间的状态控制可以通过状态机或者第六日中的“中间人”模式实现。但是如果这种状态控制是纯异步的情况下，异步信号还是比较简单且直观的选择。



## 6.第六日：谈谈组件封装

# 第六天 UI组件封装

## 第一个故事：首页轮播图

组件封装是一个前端工程师进阶的必经之路。组件封装是指Web页面上抽出来一个个包含模版（HTML）、功能（Javascript）和样式（CSS）的单元。所以，今天的内容，我们将带你了解组件封装的开发思路，让你的组件具备**封装性**、**正确性**、**扩展性**和**复用性**。

我们以实现一个首页轮播图的UI组件为例，这个组件的效果如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc61f6b645bc4180b4b64c556b7d149a~tplv-k3u1fbpfcp-zoom-1.image)

上图中的组件实现了3个功能：

1. 四张图片循环播放，每张图片停留若干时间；
1. 当用户点击左右两边的小箭头时，图片分别切换到上一张/下一张；
1. 当用户点击底部的小圆点的时候，则立即跳到小圆点顺序所对应的那张图片。

下面，我们就带你一步步实现这个组件：

### 第一步：确定UI组件的HTML结构。

根据效果图，这个组件包含了4张图片，4张图片就需要有4个HTML元素来封装。你可以采用4个块级元素来安排，比如`div`元素等。我们也可以将这4张图看作是一个图片列表，使用列表元素作为图片的容器：

```html
<div class="slider">
  <ul>
    <li class="slider__item--selected">
      <img src="https://p5.ssl.qhimg.com/t0119c74624763dd070.png"/>
    </li>
    <li class="slider__item">
      <img src="https://p4.ssl.qhimg.com/t01adbe3351db853eb3.jpg"/>
    </li>
    <li class="slider__item">
      <img src="https://p2.ssl.qhimg.com/t01645cd5ba0c3b60cb.jpg"/>
    </li>
    <li class="slider__item">
      <img src="https://p4.ssl.qhimg.com/t01331ac159b58f5478.jpg"/>
    </li>
  </ul>
  <a class="slider__next"></a>
  <a class="slider__previous"></a>
  <div class="slider__control">
    <span class="slider__control-buttons--selected"></span>
    <span class="slider__control-buttons"></span>
    <span class="slider__control-buttons"></span>
    <span class="slider__control-buttons"></span>
  </div>
</div>
```

上面的HTML结构中，首先是一个大的容器，`div.slider`，其中包含一个`ul`列表，列表中是包含四张图片的四个`li`元素。

这里，我们使用两个`<a>`元素分别表示“下一张“和”上一张“的控制
```html
<a class="slider__next"></a> 
<a class="slider__previous"></a>
```

用四个`<span>`元素表示底部的四个小圆点的控制：

```html
<div class="slider__control">
  <span class="slider__control-buttons--selected"></span>
  <span class="slider__control-buttons"></span>
  <span class="slider__control-buttons"></span>
  <span class="slider__control-buttons"></span>
</div>
```

_当然这些控制你也可以使用其他的HTML元素来表示。_

💡注意：这里我们使用的CSS规则名有点特别，如果你是第一次见到可能会觉得有些奇怪。实际上这里的命名是一种CSS书写规范，叫做`BEM`，是英文`Block-Element-Modifier`的简写。

这一规范采用三个部分来描述规则，首先是Block表示组件名，这个任务是写轮播图，我们给这个组件起名字叫`slider`。然后是Element，比如对应的列表项`li`元素，表示item，所以它的class就是`slider__item`，这里Block和Element之间使用双下划线`__`连接。最后是Modifier表示状态，其中一个列表的状态是`selected`，所以最终的class是`slider__item--selected`，这里Element和Modifier之间使用双横杠`--`连接。

在比较复杂的UI组件中，使用`BEM`有几个好处：

1. 让CSS规则保持相对简单，只用一个class就能定位对应的元素，这样优先级也相对扁平，管理起来不容易冲突。

1. 阅读代码的人一眼可以知道一个元素是哪个组件的哪个部分。由于组件复杂的时候，HTML代码比较长，可能元素离组件容器比较远，如果使用普通层级关系，你看到一个`.item`元素，除非找到外层的`.slider`，你才能知道它属于`.slider`组件而不是其他组件的`.item`，那样在HTML代码很复杂的时候找起来就比较费劲。

### 第二步：设置元素的样式

然后根据效果图，我们给这段HTML代码添加CSS样式。

首先，我们给`class=slider`的`div`元素设置了宽度和高度，以及取消`ul`元素默认的列表样式：

```css
.slider {
  position: relative;
  width: 790px;
  height: 340px;
}

.slider ul {
  list-style-type:none;
  position: relative;
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}
```

然后，将`class=slider__item`和`class=slider__item--selected`的`li`元素的position属性设置为绝对定位（absolute），这样就能够将这4张图片重叠显示在同一个位置。如下代码所示：

```css
.slider__item,
.slider__item--selected {
  position: absolute;
  transition: opacity 1s;
  opacity: 0;
  text-align: center;
}

.slider__item--selected {
  transition: opacity 1s;
  opacity: 1;
}
```

其中，`transition: opacity 1s`表示设置图片透明度变化的动画，时间为1秒。状态为`slider__item`时，显示为透明。状态为`slider__item--selected`时显示为不透明。

接着是控制元素的样式：

```css
.slider__next,
.slider__previous{
  display: inline-block;
  position: absolute;
  top: 50%; /*定位在录播图组件的纵向中间的位置*/
  margin-top: -25px;
  width: 30px;
  height:50px;
  text-align: center;
  font-size: 24px;
  line-height: 50px;
  overflow: hidden;
  border: none;
  color: white;
  background: rgba(0,0,0,0.2); /*设置为半透明*/
  cursor: pointer; /*设置鼠标移动到这个元素时显示为手指状*/
  opacity: 0; /*初始状态为透明*/
  transition: opacity .5s; /*设置透明度变化的动画，时间为.5秒*/
}

.slider__previous {
  left: 0; /*定位在slider元素的最左边*/
}

.slider__next {
  right: 0; /*定位在slider元素的最右边*/
}

.slider:hover .slider__previous {
  opacity: 1;
}

.slider:hover .slider__next {
  opacity: 1;
}

.slider__previous:after {
  content: '<';
}

.slider__next:after {
  content: '>';
}
```

上面的规则中，`.slider__next,
.slider__previous`分别表示“向下一张”和“向上一张”的控制。初始状态下，这两个控制元素的背景色为半透明，字体颜色是白色。

`.slider:hover .slider__previous` 和 `.slider:hover .slider__next`这两条规则表示当鼠标悬停在`class=slider`的元素上时，显示左右两侧的控制元素。

最后，定义底部四个小点的样式：

```css
.slider__control{
  position: relative;
  display: table; /* table 布局*/
  background-color: rgba(255, 255, 255, 0.5);
  padding: 5px;
  border-radius: 12px;
  bottom: 30px;
  margin: auto;
}

.slider__control-buttons,
.slider__control-buttons--selected{
  display: inline-block;
  width: 15px;
  height: 15px;
  border-radius: 50%;/*设置为圆形*/
  margin: 0 5px;
  background-color: white;
  cursor: pointer;
}

.slider__control-buttons--selected {
  background-color: red;
}
```

上面的规则中，

- 第一条规则表示给四个小圆点设置一个灰色的背景。其中的`position: relative; display: table;`声明表示将它的子元素（也就是4个小圆点）采用相对定位和table布局，让它们固定显示在图片中部下方。

- 第二条规则设置了小圆点的大小，形状，默认情况下，小圆点的颜色（白色），以及鼠标滑入后的状态（pointer)

- 第三条规则表示，当选择后，小圆点的颜色变成红色。

### 第三步：设计API

页面的主体结构和样式完成之后，我们需要根据组件的功能，为该组件设计API。

我们回顾一下这个组件的需求：

- 四张图片循环播放，每张图片停留若干时间；
- 当用户点击左右两边的小箭头时，图片分别切换到上一张/下一张；
- 当用户点击中下部的小圆点的时候，则立即跳到小圆点顺序所对应的那张图片。

根据上述的需求呢，我们设计了4个组件API:

- slideTo(idx) - 切换显示idx指示位置的图片
- slideNext() - 切换到下一张图
- slidePrevious() - 切换到上一张图
- getSelectedItem() - 获取选中的图片
- getSelectedItemIndex() - 获取选中的图片的位置

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28bdaa91489d4af59988a24f83c9f46c~tplv-k3u1fbpfcp-zoom-1.image)

然后，将这个组件封装为一个类——slider：

```js
class Slider {
  constructor({container}) {
    this.container = container;
    this.items = Array.from(container.querySelectorAll('.slider__item, .slider__item--selected'));
  }

  /*
    通过选择器`.slider__item--selected`获得被选中的元素
  */
  getSelectedItem() {
    const selected = this.container.querySelector('.slider__item--selected');
    return selected;
  }

  /*
    返回选中的元素在items数组中的位置。
  */
  getSelectedItemIndex() {
    return this.items.indexOf(this.getSelectedItem());
  }

  slideTo(idx) {
    const selected = this.getSelectedItem();
    if(selected) { // 将之前选择的图片标记为普通状态
      selected.className = 'slider__item';
    }
    const item = this.items[idx];
    if(item) { // 将当前选中的图片标记为选中状态
      item.className = 'slider__item--selected';
    }
  }

  /*
    将下一张图片标记为选中状态
  */
  slideNext() {
    const currentIdx = this.getSelectedItemIndex();
    const nextIdx = (currentIdx + 1) % this.items.length;
    this.slideTo(nextIdx);
  }

  /*
    将上一张图片标记为选中状态
  */
  slidePrevious() {
    const currentIdx = this.getSelectedItemIndex();
    const previousIdx = (this.items.length + currentIdx - 1) % this.items.length;
    this.slideTo(previousIdx);
  }
}
```
上面的代码中：Slider的构造器中的参数`{container}`表示放置这4张图片的父容器。在构造器中，我们获取了这个父容器下所有的`<li>`元素。

然后，通过`setInterval`方法实现循环播放，间隔为3秒：

```js
const container = document.querySelector('.slider');
const slider = new Slider({container});
setInterval(() => {
  slider.slideNext();
}, 3000);
```

这样，我们的轮播图就以每3秒的切换一次频率动起来了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2bc4605c44a40c983b60f65be31ba47~tplv-k3u1fbpfcp-zoom-1.image)

### 第四步：实现用户控制

实现了组件的API后，我们还需要实现用户控制功能：

- 当用户点击左右两边的小箭头时，图片分别切换到上一张/下一张，并点亮与该图片相对应的小圆点；
- 当用户鼠标移进到底部小圆点时，则立即跳到小圆点顺序所对应的那张图片，停止轮播；
- 当用户鼠标移出底部小圆点后，图片再次恢复轮播。

我们将构造器修改为下面这样：

```js
constructor({container, cycle = 3000} = {}) {
  this.container = container;
  this.items = Array.from(container.querySelectorAll('.slider__item, .slider__item--selected'));
  this.cycle = cycle;

  const controller = this.container.querySelector('.slider__control');
  const buttons = controller.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');

  controller.addEventListener('mouseover', (evt) => {
    const idx = Array.from(buttons).indexOf(evt.target);
    if(idx >= 0) {
      this.slideTo(idx);
      this.stop();
    }
  });

  controller.addEventListener('mouseout', (evt) => {
    this.start();
  });

  /*
    注册slide事件，将选中的图片和小圆点设置为selected状态
  */
  this.container.addEventListener('slide', (evt) => {
    const idx = evt.detail.index;
    const selected = controller.querySelector('.slider__control-buttons--selected');
    if(selected) selected.className = 'slider__control-buttons';
    buttons[idx].className = 'slider__control-buttons--selected';
  });

  const previous = this.container.querySelector('.slider__previous');
  previous.addEventListener('click', (evt) => {
    this.stop();
    this.slidePrevious();
    this.start();
    evt.preventDefault();
  });

  const next = this.container.querySelector('.slider__next');
  next.addEventListener('click', (evt) => {
    this.stop();
    this.slideNext();
    this.start();
    evt.preventDefault();
  });
}
```

如上代码所示，参数`cycle`表示循环播放的时间间隔，默认为3秒。然后是每个控制元素相应的事件处理。下面，我们来依次分析一下它们。

第一个用户事件：当鼠标移入或移出小圆点事件

```js
const controller = this.container.querySelector('.slider__control');

const buttons = controller.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');

controller.addEventListener('mouseover', (evt) =>{
  const idx = Array.from(buttons).indexOf(evt.target);
  if(idx >= 0){
    this.slideTo(idx);
    this.stop(); // 停止自动循环播放
  }
});

controller.addEventListener('mouseout', (evt) => {
  this.start(); // 开始自动循环播放
});
```
上面代码表示：当鼠标移动到小圆点上方的时候（mouseover），判断当前选中的是第几个小圆点，停止自动循环播放功能，然后切换到对应的图片。当鼠标移出controller元素后（mouseout），重启自动循环播放功能。

这里呢，我们先来看看`stop()`和`start()`的实现：

```js
start() {
  this.stop();
  this._timer = setInterval(() => this.slideNext(), this.cycle);
}

stop() {
  clearInterval(this._timer);
}
```

如上代码所示：`start()`方法启动了一个定时器，每隔`cycle`秒执行一次`slideNext()`。`stop()`则是停止这个定时器。


第二个用户事件：点击上一张或下一张事件

```js
const previous = this.container.querySelector('.slider__previous');
previous.addEventListener('click', evt => {
  this.stop();
  this.slidePrevious();
  this.start();
  evt.preventDefault();
});

const next = this.container.querySelector('.slider__next');
next.addEventListener('click', evt => {
  this.stop();
  this.slideNext();
  this.start();
  evt.preventDefault();
});
```
如上代码所示：当用户点击上一张时，程序停止定时器，然后执行`slidePrevious()`方法，让图片向前翻一张，然后重启定时器。类似的，当用户点击下一张时，先停止定时器，然后向后翻一张，再重启定时器。

第三个是处理一个自定义事件 —— slide事件：

```js
this.container.addEventListener('slide', evt => {
  const idx = evt.detail.index
  const selected = controller.querySelector('.slider__control-buttons--selected');
  if(selected) selected.className = 'slider__control-buttons';
  buttons[idx].className = 'slider__control-buttons--selected';
});
```

对应地，修改`slideTo`方法，加入自定义事件触发。

```js
slideTo(idx) {
  const selected = this.getSelectedItem();
  if(selected) {
    selected.className = 'slider__item';
  }
  const item = this.items[idx];
  if(item) {
    item.className = 'slider__item--selected';
  }

  const detail = {index: idx};
  const event = new CustomEvent('slide', {bubbles: true, detail});
  this.container.dispatchEvent(event);
}
```

这个自定义事件（CustomEvent），它的作用是让底部小圆点控件监听`slideTo`方法。当`slideTo`方法执行后，这个方法就会分发一次`slide`事件，然后在这个事件中，更新底部小圆点的状态，让小圆点的状态和各自的图片状态对应起来。

最后将调用过程改成：

```js
const slider = new Slider({container});
slider.start();
```

到此，这个组件的全部功能就完成了。[在线演示](https://junyux.github.io/FE-Advance/day06/index1.html)

通过轮播组件编写过程，我们可以总结一下组件设计的一般性步骤：

1. 设计HTML结构
1. 设计组件的API
1. 设计用户控制流程

从上面的代码中，我们可以看到这个轮播组件实现了**封装性**和**正确性**，但是缺少了**可扩展性**。这个组件只能满足自身的使用，它的实现代码很难扩展到其他的组件，当有功能变化时，也需要修改其自身内部的代码。

比如产品经理因为某种原因，希望将图片下方的小圆点暂时去掉，只保留左右箭头。那么在这个版本中，就需要这么做：

1. 注释掉HTML中`.slider__control`相关的代码
1. 修改Slider组件，注释掉与小圆点控制相关的代码

又或者，将来需要为这个组件添加新的用户控制，都需要对这个组件进行再修改。

那么，如何可以避免这样的修改，让组件具备**可扩展性**呢？

## 第二个故事：组件的插件化

上一个故事中的轮播组件封装，我们实现了**封装性**和**正确性**。但这仅能满足项目当前的基本要求，是对初级工程师的基本要求，而**可扩展性**和**可复用性**，则对于整个项目的未来有很大的帮助，是对高级工程师的要求。在前端UI组件中，提升可扩展性的基本思路，是**插件化**。

那么，对于这个图片轮播组件来说，它的插件化可以是将用户控制组件从Slider组件中剥离出来，做成插件，这样才能提高Slider组件的可扩展性。

在图片轮播组件中，用户的控制组件分为三个部分：图片下部的小圆点以及左右翻页按钮。我们分别用`controller`、`previous`、`next`三个变量来分别处理它们。

现在我们来重构一下上一版的代码：

```js
constructor({container, cycle = 3000} = {}) {
  this.container = container;
  this.items = Array.from(container.querySelectorAll('.slider__item, .slider__item--selected'));
  this.cycle = cycle;
}

registerPlugins(...plugins) {
  plugins.forEach(plugin => plugin(this));
}
```

如上代码所示：在Sliders类的构造器中，我们将注册控制流程的代码移除，增加了一个新的方法叫`registerPlugins`。这个方法接受一组参数`plugins`，每个`plugin`本身是一个初始化函数，可以做任何事情。

然后，我们将之前写在构造器的控制流程代码移到对应的插件中：

```js
/* 小圆点控件 */
function pluginController(slider) {
  const controller = slider.container.querySelector('.slider__control');
  if(controller) {
    const buttons = controller.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');
    controller.addEventListener('mouseover', (evt) => {
      const idx = Array.from(buttons).indexOf(evt.target);
      if(idx >= 0) {
        slider.slideTo(idx);
        slider.stop();
      }
    });

    controller.addEventListener('mouseout', (evt) => {
      slider.start();
    });

    slider.container.addEventListener('slide', (evt) => {
      const idx = evt.detail.index;
      const selected = controller.querySelector('.slider__control-buttons--selected');
      if(selected) selected.className = 'slider__control-buttons';
      buttons[idx].className = 'slider__control-buttons--selected';
    });
  }
}

function pluginPrevious(slider) {
  const previous = slider.container.querySelector('.slider__previous');
  if(previous) {
    previous.addEventListener('click', (evt) => {
      slider.stop();
      slider.slidePrevious();
      slider.start();
      evt.preventDefault();
    });
  }
}

function pluginNext(slider) {
  const next = slider.container.querySelector('.slider__next');
  if(next) {
    next.addEventListener('click', (evt) => {
      slider.stop();
      slider.slideNext();
      slider.start();
      evt.preventDefault();
    });
  }
}
```

如上代码所示，`pluginController`、`pluginPrevious`和`pluginNext`分别表示小圆点控制和左右翻页控制插件。每个插件接受一个Slider的实例。然后，将各自的用户事件注册在对应的插件上。

💡注意：我们在 `Slider.registerPlugins` 对象方法里，给每个 `plugin`（即：插件）传入当前的 slider 对象实例。在插件的初始化函数中，我们就可以拿到这个 slider 对象。这种将依赖对象传入插件初始化函数的方式，叫做**依赖注入**。

**依赖注入**是一种组件/插件解耦合的基本思路，在UI设计中经常被使用，在我们后续的课程中还会见到。

最后再将插件注册到slider对象上：

```js
const container = document.querySelector('.slider');
const slider = new Slider({container});
slider.registerPlugins(pluginController, pluginPrevious, pluginNext);
slider.start();
```

所以，最终，这一版的JS代码是这样的：

[在线演示](https://junyux.github.io/FE-Advance/day06/index2.html)

```js
class Slider {
  constructor({container, cycle = 3000} = {}) {
    this.container = container;
    this.items = Array.from(container.querySelectorAll('.slider__item, .slider__item--selected'));
    this.cycle = cycle;
  }

  registerPlugins(...plugins) {
    plugins.forEach(plugin => plugin(this));
  }

  /*
    通过选择器`.slider__item--selected`获得被选中的元素
  */
  getSelectedItem() {
    const selected = this.container.querySelector('.slider__item--selected');
    return selected;
  }

  /*
    返回选中的元素在items数组中的位置。
  */
  getSelectedItemIndex() {
    return this.items.indexOf(this.getSelectedItem());
  }

  slideTo(idx) {
    const selected = this.getSelectedItem();
    if(selected) {
      selected.className = 'slider__item';
    }
    const item = this.items[idx];
    if(item) {
      item.className = 'slider__item--selected';
    }

    const detail = {index: idx};
    const event = new CustomEvent('slide', {bubbles: true, detail});
    this.container.dispatchEvent(event);
  }

  /*
    将下一张图片标记为选中状态
  */
  slideNext() {
    const currentIdx = this.getSelectedItemIndex();
    const nextIdx = (currentIdx + 1) % this.items.length;
    this.slideTo(nextIdx);
  }

  /*
    将上一张图片标记为选中状态
  */
  slidePrevious() {
    const currentIdx = this.getSelectedItemIndex();
    const previousIdx = (this.items.length + currentIdx - 1) % this.items.length;
    this.slideTo(previousIdx);
  }

  start() {
    this.stop();
    this._timer = setInterval(() => this.slideNext(), this.cycle);
  }

  stop() {
    clearInterval(this._timer);
  }
}

/* 小圆点控件 */
function pluginController(slider) {
  const controller = slider.container.querySelector('.slider__control');
  if(controller) {
    const buttons = controller.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');
    controller.addEventListener('mouseover', (evt) => {
      const idx = Array.from(buttons).indexOf(evt.target);
      if(idx >= 0) {
        slider.slideTo(idx);
        slider.stop();
      }
    });

    controller.addEventListener('mouseout', (evt) => {
      slider.start();
    });

    slider.container.addEventListener('slide', (evt) => {
      const idx = evt.detail.index;
      const selected = controller.querySelector('.slider__control-buttons--selected');
      if(selected) selected.className = 'slider__control-buttons';
      buttons[idx].className = 'slider__control-buttons--selected';
    });
  }
}

function pluginPrevious(slider) {
  const previous = slider.container.querySelector('.slider__previous');
  if(previous) {
    previous.addEventListener('click', (evt) => {
      slider.stop();
      slider.slidePrevious();
      slider.start();
      evt.preventDefault();
    });
  }
}

function pluginNext(slider) {
  const next = slider.container.querySelector('.slider__next');
  if(next) {
    next.addEventListener('click', (evt) => {
      slider.stop();
      slider.slideNext();
      slider.start();
      evt.preventDefault();
    });
  }
}

const container = document.querySelector('.slider');
const slider = new Slider({container});
slider.registerPlugins(pluginController, pluginPrevious, pluginNext);
slider.start();
```

这个版本中，我们将组件核心和插件部分进行了分离，这样就允许我们的组件随时减少或者增加用户控制。比如，上一故事中，当我们的产品经理要求去掉图片下方的小圆点控制时，我们自需要简单将小圆点从插件注册中去掉，完全不需要修改组件代码。

```js
slider.registerPlugins(pluginPrevious, pluginNext);
```

如果，有一天，产品经理又需要对这个组件添加新的用户控制，比如，添加一个按钮叫“试试手气”，点击该按钮，让轮播图随机切换到一张图片上，那么们我们只需要这样做：

在HTML代码中增加“试试手气“这个按钮：

```html
<button class="lucky">试试手气</button>
```

然后创建这个插件：

```js
function  pluginLucky(slider) {
  const luckyBtn = document.querySelector('.lucky');
  if(luckyBtn) {
    luckyBtn.addEventListener('click', evt => {
      slider.stop();
      slider.slideTo(Math.floor(Math.random() * slider.items.length));
      slider.start();
      evt.preventDefault();
    });
  }
}
```

最后将它注册到slider中去即可：

```js
slider.registerPlugins(pluginController, pluginPrevious, pluginNext, pluginLucky);
```

由此可见，插件化之后，组件的可扩展性得到了增强，现在我们可以任意扩展插件，而不用修改Slider本身的核心代码了。

这时，你可能发现了另一个问题 —— 组件的HTML和JS是分开写的，这意味着我们修改组件本身和增加插件的时候，不可避免地需要同时修改HTML和JS代码。

比如，产品经理希望我们将图片数量从四张增加为六张，那么我们需要修改组件和插件的HTML（即：增加`<li>`元素和小圆点控制）。甚至现在连修改一张图片的URL，我们也需要手工修改HTML内容。这也不符合前面课程中学过的数据抽象原则。所以，我们需要去掉组件的HTML代码，让JS来渲染组件需要的HTML。

那么，我们如何让JS渲染组件的HTML呢？

## 第三个故事 组件的模板化

为了让JS渲染组件的HTML，我们需要将组件**模板化**。

为了方便实现模板化，我们需要重构组件的部分API:

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97046646db134e5a96b2e84d893dc578~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示，我们给Slider组件添加了一个`render()`方法。这个方法是用于渲染Slider组件的HTML部分。然后，我们将插件由原先单一的初始化函数重构为一个包含`render()`方法和`initialize()`方法的对象。其中`render()`方法是用来渲染插件的HTML部分，而`initialize()`方法则是用于注册和插件对应的用户事件。

首先，我们来渲染Slider组件的HTML：

```js
class Slider {
  constructor({container, images = [], cycle = 3000} = {}) {
    this.container = container;
    this.data = images;
    this.container.innerHTML = this.render(this.data);
    this.items = Array.from(this.container.querySelectorAll('.slider__item, .slider__item--selected'));
    this.cycle = cycle;
    this.slideTo(0);
  }

  render(images) {
    const content = images.map(image => `
      <li class="slider__item">
        <img src="${image}"/>
      </li>    
    `.trim());

    return `<ul>${content.join('')}</ul>`;
  }
  
  /*此处省略组件其他的API*/
}
```

如上代码所示：我们将数据源（这里就是图片数组）传递给Slider组件。然后Slider的构造器利用这个数据源渲染自己的HTML —— `this.container.innerHTML = this.render(this.data);`，再将这部分HTML添加到container元素中去。

```js
const images = ['https://p5.ssl.qhimg.com/t0119c74624763dd070.png',
  'https://p4.ssl.qhimg.com/t01adbe3351db853eb3.jpg',
  'https://p2.ssl.qhimg.com/t01645cd5ba0c3b60cb.jpg',
  'https://p4.ssl.qhimg.com/t01331ac159b58f5478.jpg'];

const container = document.querySelector('.slider');
const slider = new Slider({container, images});
```

上面这段调用代码渲染的结果如下：

```HTML
<ul>
  <li class="slider__item">
    <img src="https://p5.ssl.qhimg.com/t0119c74624763dd070.png"/>
  </li>
  <li class="slider__item">
    <img src="https://p4.ssl.qhimg.com/t01adbe3351db853eb3.jpg"/>
  </li>
  <li class="slider__item">
    <img src="https://p2.ssl.qhimg.com/t01645cd5ba0c3b60cb.jpg"/>
  </li>
  <li class="slider__item">
    <img src="https://p4.ssl.qhimg.com/t01331ac159b58f5478.jpg"/>
  </li>
</ul>
```

这样，组件的HTML代码部分就简化为下面的形式：

```html
<div class="slider"></div>
```

<!-- 然后，我们修改了`registerPlugin`方法，先将`this.data`数据传给`plugin`的`render()`方法去构造插件的HTML结构，然后再调用`intialize()`完成插件的初始化。 -->

然后，我们为每个插件添加渲染代码：

```js
const pluginController = { // 小圆点插件
  render(images){ //随着图片数量的增加，小圆点元素也需要增加
    return `
      <div class="slider__control">
        ${images.map((image, i) => `
            <span class="slider__control-buttons${i===0?'--selected':''}"></span>
        `).join('')}
      </div>    
    `.trim();
  },

  initialize(slider){
    const controller = slider.container.querySelector('.slider__control');
    
    if(controller){
      const buttons = controller.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');
      controller.addEventListener('mouseover', evt => {
        const idx = Array.from(buttons).indexOf(evt.target);
        if(idx >= 0){
          slider.slideTo(idx);
          slider.stop();
        }
      });

      controller.addEventListener('mouseout', evt => {
        slider.start();
      });

      slider.container.addEventListener('slide', evt => {
        const idx = evt.detail.index
        const selected = controller.querySelector('.slider__control-buttons--selected');
        if(selected) selected.className = 'slider__control-buttons';
        buttons[idx].className = 'slider__control-buttons--selected';
      });
    }    
  }
};

const pluginPrevious = {
  render(){
    return `<a class="slider__previous"></a>`;
  },

  initialize(slider){
    const previous = slider.container.querySelector('.slider__previous');
    if(previous){
      previous.addEventListener('click', evt => {
        slider.stop();
        slider.slidePrevious();
        slider.start();
        evt.preventDefault();
      });
    }  
  }
};

const pluginNext = {
  render(){
    return `<a class="slider__next"></a>`;
  },

  initialize(slider){
    const previous = slider.container.querySelector('.slider__next');
    if(previous){
      previous.addEventListener('click', evt => {
        slider.stop();
        slider.slideNext();
        slider.start();
        evt.preventDefault();
      });
    }  
  }
};
```

如上代码所示：每个插件都被构造成一个对象。每个对象中都有一个`render`方法，负责渲染各自的HTML。`initialize`方法则是负责注册各自的用户事件。

为了将每个插件添加到Slider组件中，我们需要修改Slider的`Slider.registerPlugins()`方法：

```js
registerPlugins(...plugins) {
  plugins.forEach((plugin) => {
    const pluginContainer = document.createElement('div');
    pluginContainer.className = 'slider__plugin';
    pluginContainer.innerHTML = plugin.render(this.data);
    this.container.appendChild(pluginContainer);
    plugin.initialize(this);
  });
}
```
 
如上代码所示：Slider组件为每个plugin创建了一个`class=slider__plugin`的容器，然后将插件的HTML元素添加到这个容器中，再把这个容器添加到Slider组件中去，最后再调用插件的`initialize`方法，以便为每个插件添加各自的用户控制。

这次重构的完整代码如下：

[在线演示](https://junyux.github.io/FE-Advance/day06/index3.html)

```js
class Slider {
  constructor({container, images = [], cycle = 3000} = {}) {
    this.container = container;
    this.data = images;
    this.container.innerHTML = this.render(this.data);
    this.items = Array.from(this.container.querySelectorAll('.slider__item, .slider__item--selected'));
    this.cycle = cycle;
    this.slideTo(0);
  }

  render(images) {
    const content = images.map(image => `
      <li class="slider__item">
        <img src="${image}"/>
      </li>    
    `.trim());

    return `<ul>${content.join('')}</ul>`;
  }

  registerPlugins(...plugins) {
    plugins.forEach((plugin) => {
      const pluginContainer = document.createElement('div');
      pluginContainer.className = 'slider__plugin';
      pluginContainer.innerHTML = plugin.render(this.data);
      this.container.appendChild(pluginContainer);
      plugin.initialize(this);
    });
  }

  /*
    通过选择器`.slider__item--selected`获得被选中的元素
  */
  getSelectedItem() {
    const selected = this.container.querySelector('.slider__item--selected');
    return selected;
  }

  /*
    返回选中的元素在items数组中的位置。
  */
  getSelectedItemIndex() {
    return this.items.indexOf(this.getSelectedItem());
  }

  slideTo(idx) {
    const selected = this.getSelectedItem();
    if(selected) {
      selected.className = 'slider__item';
    }
    const item = this.items[idx];
    if(item) {
      item.className = 'slider__item--selected';
    }

    const detail = {index: idx};
    const event = new CustomEvent('slide', {bubbles: true, detail});
    this.container.dispatchEvent(event);
  }

  /*
    将下一张图片标记为选中状态
  */
  slideNext() {
    const currentIdx = this.getSelectedItemIndex();
    const nextIdx = (currentIdx + 1) % this.items.length;
    this.slideTo(nextIdx);
  }

  /*
    将上一张图片标记为选中状态
  */
  slidePrevious() {
    const currentIdx = this.getSelectedItemIndex();
    const previousIdx = (this.items.length + currentIdx - 1) % this.items.length;
    this.slideTo(previousIdx);
  }

  start() {
    this.stop();
    this._timer = setInterval(() => this.slideNext(), this.cycle);
  }

  stop() {
    clearInterval(this._timer);
  }
}

const pluginController = { // 小圆点插件
  render(images) { // 随着图片数量的增加，小圆点元素也需要增加
    return `
      <div class="slider__control">
        ${images.map((image, i) => `
            <span class="slider__control-buttons${i === 0 ? '--selected' : ''}"></span>
        `).join('')}
      </div>    
    `.trim();
  },

  initialize(slider) {
    const controller = slider.container.querySelector('.slider__control');

    if(controller) {
      const buttons = controller.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');
      controller.addEventListener('mouseover', (evt) => {
        const idx = Array.from(buttons).indexOf(evt.target);
        if(idx >= 0) {
          slider.slideTo(idx);
          slider.stop();
        }
      });

      controller.addEventListener('mouseout', (evt) => {
        slider.start();
      });

      slider.container.addEventListener('slide', (evt) => {
        const idx = evt.detail.index;
        const selected = controller.querySelector('.slider__control-buttons--selected');
        if(selected) selected.className = 'slider__control-buttons';
        buttons[idx].className = 'slider__control-buttons--selected';
      });
    }
  },
};

const pluginPrevious = {
  render() {
    return '<a class="slider__previous"></a>';
  },

  initialize(slider) {
    const previous = slider.container.querySelector('.slider__previous');
    if(previous) {
      previous.addEventListener('click', (evt) => {
        slider.stop();
        slider.slidePrevious();
        slider.start();
        evt.preventDefault();
      });
    }
  },
};

const pluginNext = {
  render() {
    return '<a class="slider__next"></a>';
  },

  initialize(slider) {
    const previous = slider.container.querySelector('.slider__next');
    if(previous) {
      previous.addEventListener('click', (evt) => {
        slider.stop();
        slider.slideNext();
        slider.start();
        evt.preventDefault();
      });
    }
  },
};

const images = ['https://p5.ssl.qhimg.com/t0119c74624763dd070.png',
  'https://p4.ssl.qhimg.com/t01adbe3351db853eb3.jpg',
  'https://p2.ssl.qhimg.com/t01645cd5ba0c3b60cb.jpg',
  'https://p4.ssl.qhimg.com/t01331ac159b58f5478.jpg'];

const container = document.querySelector('.slider');
const slider = new Slider({container, images});
slider.registerPlugins(pluginController, pluginPrevious, pluginNext);
slider.start();
```

模板化之后，代码的可扩展性得到了进一步的提升。现在，如果我们增加或者减少轮播图片数量，只需要修改数据中images数组的元素个数。如果我们需要或者不需要某个插件，我们只需要修改传给`registerPlugins()`方法的参数即可。可以说，这一版代码的可扩展性是达到了发布要求的较高标准的。

这个版本的组件虽然具有较高的可扩展性，但是它缺少**可复用性**。这里的可复用性是指，这套组件（包括Slider的插件）没有统一的规范。如果我们的同事同样需要设置一套组件，其中也有小圆点组件，但是他使用的渲染方法是`draw()`而不是`render()`，组件事件的注册使用的也不是`initialized()`方法， 那么这个同事就需要再重复开发一个小圆点组件。这样代码的可复用性就比较差了。所以，为了提高代码可复用性，我们需要为组件设计一套规范。大家同时遵循这套规范，就能让不同开发者设计的组件被他人复用。

那么，如何实现组件的统一规范呢？

## 第四个故事：设计组件框架

为了提高组件的复用性，我们需要为组件设计一个**统一的规范**。实现这个统一的规范，我们可以通过设计一套通用的**组件机制**，并以这套机制为原则构建一个库。这个**通用机制**实际上提供了代码设计和抽象的一套通用规范，而遵循这套规范的基础库，实际上就是完整的**UI组件框架**。

设计UI组件框架是一件比较复杂的事情，因为要考虑许多细节。但在这里，我们可以简要地设计一个基础简化版。

我们继续修改上一版的设计，提炼出通用的Component类：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0865da3352d447caaaaf96411b26a393~tplv-k3u1fbpfcp-zoom-1.image)

如上图所示，一个组件 Component 包含以下 API:

- static name - 静态属性，表示这个组件的名称
- contructor({container, data, parent}) - 组件构造函数
- registerSubComponents(...Comps) - 给当前组件注册子组件
- render(data) - 渲染HTML模板

```js
class Component {
  static name = 'component';

  constructor({container, data, parent = null} = {}) {
    this.data = data;
    this.container = container;
    this.container.innerHTML = this.render(this.data);
  }

  registerSubComponents(...Comps) {
    const data = this.data;
    const container = this.container;
    this.children = this.children || [];
    Comps.forEach((Comp) => {
      const subContainer = document.createElement('div');
      const sub = new Comp({container: subContainer, data, parent: this});
      container.appendChild(subContainer);
      this.children.push(sub);
    });
  }

  render(data) {
    /* abstract */
    return '';
  }
}
```

然后 Slider 和其他几个插件都作为组件类继承自 Component。

Slider 组件：

```js
class Slider extends Component {
  static name = 'slider';

  constructor({container, images = [], cycle = 3000} = {}) {
    super({container, data: images});
    this.items = Array.from(this.container.querySelectorAll('.slider__item, .slider__item--selected'));
    this.cycle = cycle;
    this.slideTo(0);
  }

  render(images) {
    const content = images.map(image => `
      <li class="slider__item">
        <img src="${image}"/>
      </li>    
    `.trim());

    return `<ul>${content.join('')}</ul>`;
  }

  getSelectedItem() {
    const selected = this.container.querySelector('.slider__item--selected');
    return selected;
  }

  getSelectedItemIndex() {
    return this.items.indexOf(this.getSelectedItem());
  }

  slideTo(idx) {
    const selected = this.getSelectedItem();
    if(selected) {
      selected.className = 'slider__item';
    }
    const item = this.items[idx];
    if(item) {
      item.className = 'slider__item--selected';
    }

    const detail = {index: idx};
    const event = new CustomEvent('slide', {bubbles: true, detail});
    this.container.dispatchEvent(event);
  }

  slideNext() {
    const currentIdx = this.getSelectedItemIndex();
    const nextIdx = (currentIdx + 1) % this.items.length;
    this.slideTo(nextIdx);
  }

  slidePrevious() {
    const currentIdx = this.getSelectedItemIndex();
    const previousIdx = (this.items.length + currentIdx - 1) % this.items.length;
    this.slideTo(previousIdx);
  }

  start() {
    this.stop();
    this._timer = setInterval(() => this.slideNext(), this.cycle);
  }

  stop() {
    clearInterval(this._timer);
  }
}
```

SliderController 组件：

```js
class SliderController extends Component {
  static name = 'slider__control';

  constructor({container, data, parent: slider}) {
    super({container, data});

    const buttons = container.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');
    container.addEventListener('mouseover', (evt) => {
      const idx = Array.from(buttons).indexOf(evt.target);
      if(idx >= 0) {
        slider.slideTo(idx);
        slider.stop();
      }
    });

    container.addEventListener('mouseout', (evt) => {
      slider.start();
    });

    slider.container.addEventListener('slide', (evt) => {
      const idx = evt.detail.index;
      const selected = container.querySelector('.slider__control-buttons--selected');
      if(selected) selected.className = 'slider__control-buttons';
      buttons[idx].className = 'slider__control-buttons--selected';
    });
  }

  render(images) {
    return `
      <div class="slider__control">
        ${images.map((image, i) => `
            <span class="slider__control-buttons${i === 0 ? '--selected' : ''}"></span>
        `).join('')}
      </div>    
    `.trim();
  }
}
```

SliderPrevious 和 SliderNext 组件：

```js
class SliderPrevious extends Component {
  constructor({container, parent: slider}) {
    super({container});
    const previous = container.querySelector('.slider__previous');
    previous.addEventListener('click', (evt) => {
      slider.stop();
      slider.slidePrevious();
      slider.start();
      evt.preventDefault();
    });
  }

  render() {
    return '<a class="slider__previous"></a>';
  }
}

class SliderNext extends Component {
  constructor({container, parent: slider}) {
    super({container});
    const previous = container.querySelector('.slider__next');
    previous.addEventListener('click', (evt) => {
      slider.stop();
      slider.slidePrevious();
      slider.start();
      evt.preventDefault();
    });
  }

  render() {
    return '<a class="slider__next"></a>';
  }
}
```

这样，我们就以组件化的方式实现了这个版本的轮播图，完整的JS代码如下：

[在线演示](https://junyux.github.io/FE-Advance/day06/index4.html)

```js
class Component {
  static name = 'component';

  constructor({container, data, parent = null} = {}) {
    this.data = data;
    this.container = container;
    this.container.innerHTML = this.render(this.data);
  }

  registerSubComponents(...Comps) {
    const data = this.data;
    const container = this.container;
    this.children = this.children || [];
    Comps.forEach((Comp) => {
      const subContainer = document.createElement('div');
      const sub = new Comp({container: subContainer, data, parent: this});
      container.appendChild(subContainer);
      this.children.push(sub);
    });
  }

  render(data) {
    /* abstract */
    return '';
  }
}

class Slider extends Component {
  static name = 'slider';

  constructor({container, images = [], cycle = 3000} = {}) {
    super({container, data: images});
    this.items = Array.from(this.container.querySelectorAll('.slider__item, .slider__item--selected'));
    this.cycle = cycle;
    this.slideTo(0);
  }

  render(images) {
    const content = images.map(image => `
      <li class="slider__item">
        <img src="${image}"/>
      </li>    
    `.trim());

    return `<ul>${content.join('')}</ul>`;
  }

  getSelectedItem() {
    const selected = this.container.querySelector('.slider__item--selected');
    return selected;
  }

  getSelectedItemIndex() {
    return this.items.indexOf(this.getSelectedItem());
  }

  slideTo(idx) {
    const selected = this.getSelectedItem();
    if(selected) {
      selected.className = 'slider__item';
    }
    const item = this.items[idx];
    if(item) {
      item.className = 'slider__item--selected';
    }

    const detail = {index: idx};
    const event = new CustomEvent('slide', {bubbles: true, detail});
    this.container.dispatchEvent(event);
  }

  slideNext() {
    const currentIdx = this.getSelectedItemIndex();
    const nextIdx = (currentIdx + 1) % this.items.length;
    this.slideTo(nextIdx);
  }

  slidePrevious() {
    const currentIdx = this.getSelectedItemIndex();
    const previousIdx = (this.items.length + currentIdx - 1) % this.items.length;
    this.slideTo(previousIdx);
  }

  start() {
    this.stop();
    this._timer = setInterval(() => this.slideNext(), this.cycle);
  }

  stop() {
    clearInterval(this._timer);
  }
}

class SliderController extends Component {
  static name = 'slider__control';

  constructor({container, data, parent: slider}) {
    super({container, data});

    const buttons = container.querySelectorAll('.slider__control-buttons, .slider__control-buttons--selected');
    container.addEventListener('mouseover', (evt) => {
      const idx = Array.from(buttons).indexOf(evt.target);
      if(idx >= 0) {
        slider.slideTo(idx);
        slider.stop();
      }
    });

    container.addEventListener('mouseout', (evt) => {
      slider.start();
    });

    slider.container.addEventListener('slide', (evt) => {
      const idx = evt.detail.index;
      const selected = container.querySelector('.slider__control-buttons--selected');
      if(selected) selected.className = 'slider__control-buttons';
      buttons[idx].className = 'slider__control-buttons--selected';
    });
  }

  render(images) {
    return `
      <div class="slider__control">
        ${images.map((image, i) => `
            <span class="slider__control-buttons${i === 0 ? '--selected' : ''}"></span>
        `).join('')}
      </div>    
    `.trim();
  }
}

class SliderPrevious extends Component {
  constructor({container, parent: slider}) {
    super({container});
    const previous = container.querySelector('.slider__previous');
    previous.addEventListener('click', (evt) => {
      slider.stop();
      slider.slidePrevious();
      slider.start();
      evt.preventDefault();
    });
  }

  render() {
    return '<a class="slider__previous"></a>';
  }
}

class SliderNext extends Component {
  constructor({container, parent: slider}) {
    super({container});
    const previous = container.querySelector('.slider__next');
    previous.addEventListener('click', (evt) => {
      slider.stop();
      slider.slideNext();
      slider.start();
      evt.preventDefault();
    });
  }

  render() {
    return '<a class="slider__next"></a>';
  }
}

const images = ['https://p5.ssl.qhimg.com/t0119c74624763dd070.png',
  'https://p4.ssl.qhimg.com/t01adbe3351db853eb3.jpg',
  'https://p2.ssl.qhimg.com/t01645cd5ba0c3b60cb.jpg',
  'https://p4.ssl.qhimg.com/t01331ac159b58f5478.jpg'];

const container = document.querySelector('.slider');
const slider = new Slider({container, images});
slider.registerSubComponents(SliderController, SliderPrevious, SliderNext);
slider.start();
```

于是我们就得到了一个虽然简单，却自成体系的“组件框架”，这已经不仅仅是考虑Slider这一个组件的问题，依据这一套原则，我们的框架可以逐步添加和实现其他的UI组件，并且可以让这些组件被其他组件复用。

这样复用性的问题就得到了解决。当然，这个小小的组件框架还有许多细节问题未考虑。

比如：

1. 我们抽象了HTML和JS，却没有把CSS包含进来。
1. `registerSubComponents`方法传入的是子组件类，如果我们要创建子组件多个实例，还需要继续完善这套机制才能做到。
1. 我们可以在子组件中拿到parent对象，然后通过parent.container随意操作父组件的HTML结构，这导致不安全和可能的冲突，也需要引入适当的机制来处理这一问题。

上述这些问题和其他一些问题有待继续完善，在一般较成熟的UI框架中，这些问题都有对应的解决方法，不过这超出了我们课程的范畴，我们把这些问题留待其他的课程。

## 7.第七日：常用设计模式

# 第七天 常用设计模式

## 第一个故事：图片预览

如果说组件封装是为了让其他程序员能够复用和扩展我们的UI组件，那么设计模式的意义则在于让其他程序员能够复用我们的**解决方案**。设计模式简单来说就是解决在一个特定上下文中一个问题的一种解决方案。所以，今天的故事，我们就来聊聊前端开发中常用的设计模式。

### 抽象行为（behavior）

我们的任务是这样的，给一个固定列表中的图片元素增加“预览”功能。

对应的HTML页面如下所示：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>图片预览</title>
  <style>
    #list {
      list-style-type: none;
      justify-content: flex-start;
      display: flex;
      flex-wrap: wrap;
    }

    #list li {
      padding: 10px;
      margin: 0;
    }
    #list img {
      height: 200px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <ul id="list">
    <li>
      <img src="https://p4.ssl.qhimg.com/t01713d89cfdb45cdf5.jpg">
    </li>
    <li>
      <img src="https://p4.ssl.qhimg.com/t01e456146c8f8a639a.jpg">
    </li>
    <li>
      <img src="https://p1.ssl.qhimg.com/t015f613e2205b573d8.jpg">
    </li>
    <li>
      <img src="https://p0.ssl.qhimg.com/t01290338a28018d404.jpg">
    </li>
    <li>
      <img src="https://p3.ssl.qhimg.com/t01d9aa5ae469c8862e.jpg">
    </li>
    <li>
      <img src="https://p3.ssl.qhimg.com/t01cb20d35fc4aa3c0d.jpg">
    </li>
    <li>
      <img src="https://p5.ssl.qhimg.com/t0110b30256941b9611.jpg">
    </li>
  </ul>
</body>
</html>
```

显示的UI效果如图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15e3be30345e45ce8b4b74659c3e526e~tplv-k3u1fbpfcp-zoom-1.image)

要实现的功能是，鼠标点击到列表中的图片上，显示对应图片（缩略图）的高清大图并带有“上一张”、“下一张”的切换按钮。

这个任务的解决方案很多：你可以按照常规做法，给每张图片注册一个事件监听器，响应用户的点击，显示该图的预览；你也可以按照组件封装的思路，设计一个预览功能的UI组件。但是，今天我们的主题是设计模式，所以，我们想使用“抽象行为”的设计模式来实现这个任务。这种模式应用了第四日的过程抽象的思想，是比组件化更加轻量的一种解决思路。
<!-- 在第四日，我们已经讨论过了组件封装。像这个问题，我们当然也可以用组件化的思路去解决它。不过除了组件化，我们也还有另一种选择，使用“行为抽象”的设计模式来解决这个问题。这是一种应用第五日过程抽象思想，比组件化更轻量的解决思路。 -->

下面，我们来看一看抽象行为是如何实现这个预览行为的：

```js
const list = document.getElementById('list');
list.addEventListener('click', (evt) => {
  const target = evt.target;
  if(target.tagName === 'IMG') {
    preview(list, target);
  }
});
```
上面的代码是`click`事件处理函数。当点击的`target`是图片时，则执行`preview(list,target)`函数。这个`preview`函数就是我们的预览行为。

下面我们重点看看`preview`行为是如何被抽象出来的：

```js
function useBehavior(context) {
  const {type, getDetail} = context;
  return function (subject, target) {
    const event = new CustomEvent(type, {bubbles: true, detail: getDetail.call(context, subject, target)});
    target.dispatchEvent(event);
  };
}
```

如上代码所示，我们定义了一个很简短的函数`useBehavior(context)`，这个函数是一个高阶函数，它返回的是代表特定行为的方法。当调用这个方法时，传入`subject`和`target`，然后创建一个自定义事件，并通过执行`getDetail`获取到赋给该事件参数的detail内容，然后以`target`为目标派发这个自定义事件。

接下来，我们通过它定义一个叫做“preview”的行为：

```js
const preview = useBehavior({
  type: 'preview',

  /*
    @subject: <ul>元素
    @target: 选中的图片元素
  */
  getDetail(subject, target) {
    const imgs = Array.from(subject.querySelectorAll('img'));
    const selected = imgs.indexOf(target); // 获取选中图片在图片集合中的索引号
    let mask = document.getElementById('mask');

    // 如果mask不存在，创建一个mask元素
    if(!mask) {
      mask = document.createElement('div');
      mask.id = 'mask';
      mask.innerHTML = `
        <a class="previous" href="###">&lt;</a>
        <img src="${imgs[selected].src}">
        <a class="next" href="###">&gt;</a>    
      `;
      // 给 #mask 元素设置样式：
      Object.assign(mask.style, {
        position: 'absolute',
        left: 0,
        top: 0,
        width: '100%',
        height: '100%',
        backgroundColor: 'rgba(0,0,0,0.8)',
        display: 'none',
        alignItems: 'center',
        justifyContent: 'space-between',
      });

      // 给 #mask 元素左右两边的<a>元素设置样式：
      mask.querySelectorAll('a').forEach((a) => {
        Object.assign(a.style, {
          width: '30px',
          textAlign: 'center',
          fontSize: '2rem',
          color: '#fff',
          textDecoration: 'none',
        });
      });
      document.body.appendChild(mask);

      // 给#mask元素添加点击事件处理函数：
      let idx = selected;
      mask.addEventListener('click', (evt) => {
        const target = evt.target;
        if(target === mask) { // 如果点击的对象是mask元素，则隐藏mask元素
          mask.style.display = 'none';
        } else if(target.className === 'previous') { // 显示上一张图片
          update(--idx);
        } else if(target.className === 'next') { // 显示下一张图片
          update(++idx);
        }
      });
    }

    // 设置img元素的src属性指向指定图片
    function update(idx) {
      const [previous, next] = [...mask.querySelectorAll('a')];
      previous.style.visibility = idx ? 'visible' : 'hidden';
      next.style.visibility = idx < imgs.length - 1 ? 'visible' : 'hidden';
      const img = mask.querySelector('img');
      img.src = imgs[idx].src;
    }

    return {
      showMask() { // 显示选中图片的预览
        mask.style.display = 'flex';
        update(selected);
      },
    };
  },
});
```

在`getDetail`方法里，我们先创建一个`id=mask`的`<div>`元素，它的结构如下：

```html
<div id="mask">
  <a class="previous" href="###">&lt;</a>
  <img src="${imgs[selected].src}">
  <a class="next" href="###">&gt;</a>
</div>
```

然后给`#mask`元素设置样式：

```js
Object.assign(mask.style, {
  position: 'absolute',
  left: 0,
  top: 0,
  width: '100%',
  height: '100%',
  backgroundColor: 'rgba(0,0,0,0.8)',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-between',
});
mask.querySelectorAll('a').forEach((a) => {
  Object.assign(a.style, {
    width: '30px',
    textAlign: 'center',
    fontSize: '2rem',
    color: '#fff',
    textDecoration: 'none',
  });
});
document.body.appendChild(mask);
```

接着添加鼠标点击`mask`元素，以及左右两侧箭头（即`a.previous`和`a.next`两个元素）时触发的动作：

```js
mask.addEventListener('click', (evt) => {
  const target = evt.target;
  if(target === mask) {
    mask.style.display = 'none';
  } else if(target.className === 'previous') {
    update(--idx);
  } else if(target.className === 'next') {
    update(++idx);
  }
});
```

`update`方法显示`idx`对应的图片，以及根据图片的位置决定是否显示左右箭头:

```js
function update(idx) {
  const [previous, next] = [...mask.querySelectorAll('a')];
  previous.style.visibility = idx ? 'visible' : 'hidden';
  next.style.visibility = idx < imgs.length - 1 ? 'visible' : 'hidden';
  const img = mask.querySelector('img');
  img.src = imgs[idx].src;
}
```

最后，我们返回一个`showMask()`方法，这个方法的作用是将`id=mask`的`<div>`元素真正显示出来。

```js
return {
  showMask(){
    mask.style.display = 'flex';
    update(selected);
  },
};
```
<!-- 这样，我们就可以在list上触发这个preview行为：

```js
const list = document.getElementById('list');
list.addEventListener('click', (evt) => {
  const target = evt.target;
  if(target.tagName === 'IMG') {
    preview(list, target);
  }
}); 
``` -->

接着我们要通过鼠标click事件触发preview行为：

```js
const list = document.getElementById('list');
list.addEventListener('click', (evt) => {
  const target = evt.target;
  if(target.tagName === 'IMG') {
    preview(list, target);
  }
});
```

然后，我们让`#list`元素监听`preview`事件：

```js
list.addEventListener('preview', ({detail}) => {
  detail.showMask();
});
```

在`preview`事件监听器中我们执行`detail.showMask()`，就能触发图片预览的功能了。[在线演示](https://junyux.github.io/FE-Advance/day07/index1.html)

从上述的解决方案，我们可以看到，通过抽象行为的模式，我们将“预览”这个行为从组件中剥离出来，降低了组件和行为的耦合度。这样做究竟有什么好处呢？

<!-- 看到这里，你可能会对这个降低组件行为耦合度的设计思想有所体会，但同时也会觉得有些疑问，为什么我们要绕一大圈，先设计一个`useBehavior`，再通过`useBehavior`定义`preview`行为，然后在`preview`行为的`getDetail`方法里返回`showMask`，最后再在`preview`事件中调用`showMask()`？

没有关系，你可以先带着这个疑问，随继续我们深入下去，看看这么设计究竟有什么好处。 -->

## 第二个故事：图片选择器

这个故事，我们依然使用和第一个故事相似的HTML结构，实现一个与图片预览类似的功能，叫做图片选择器：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>抽象行为</title>
  <style>
    #list {
      list-style-type: none;
      justify-content: flex-start;
      display: flex;
      flex-wrap: wrap;
    }

    #list li {
      padding: 10px;
      margin: 0;
    }
    #list img {
      height: 200px;
      cursor: pointer;
      box-sizing: border-box;
      padding: 5px;
    }

    #list img.selected {
      border: solid 5px #37c;
      padding: 0;
    }
  </style>
</head>
<body>
  <ul id="list">
    <li>
      <img src="https://p4.ssl.qhimg.com/t01713d89cfdb45cdf5.jpg">
    </li>
    <li>
      <img src="https://p4.ssl.qhimg.com/t01e456146c8f8a639a.jpg">
    </li>
    <li>
      <img src="https://p1.ssl.qhimg.com/t015f613e2205b573d8.jpg">
    </li>
    <li>
      <img src="https://p0.ssl.qhimg.com/t01290338a28018d404.jpg">
    </li>
    <li>
      <img src="https://p3.ssl.qhimg.com/t01d9aa5ae469c8862e.jpg">
    </li>
    <li>
      <img src="https://p3.ssl.qhimg.com/t01cb20d35fc4aa3c0d.jpg">
    </li>
    <li>
      <img src="https://p5.ssl.qhimg.com/t0110b30256941b9611.jpg">
    </li>
  </ul>
</body>
</html>
```

上面的HTML和前面的图片预览基本上一样，只是有些细节的CSS样式修改：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a01d2cee73f848158bdd2c3f9812b0bc~tplv-k3u1fbpfcp-zoom-1.image)

沿用图片预览的思路，我们也可以将图片选择器的“选择”行为抽象出来，它比图片预览更加简单：

```js
function useBehavior(context) {
  const {type, getDetail} = context;
  return function(subject, target) {
    const event = new CustomEvent(type, {bubbles: true, detail: getDetail.call(context, subject, target)});
    target.dispatchEvent(event);
  }
}

const select = useBehavior({
  type: 'select',
  data: {
    picked: new Set(), // 选中的图片集合
  },
  getDetail(subject, target) {
    const picked = this.data.picked;

    if(picked.has(target)) {
      target.className = '';
      picked.delete(target);
    } else {
      target.className = 'selected';
      picked.add(target);
    }

    return {
      changed: target,
      picked,
    };
  },
});
```

在`select`行为里，我们定义一个`picked`集合，用来存放所有选中的图片元素。`getDetail`函数仅仅做一件事情，如果`target`在`picked`集合中，将它移出集合并撤销`img`元素的样式，否则，将它放入集合并添加`img`元素的样式。

_💡注意，在`useBehavior`定义中，我们将`context`作为`getDetail`的`this`上下文传入。这样我们就可以在实际实现`getDetail`方法的时候，通过`this`上下文拿到调用`useBehavior`的对象上的数据，这样我们就可以灵活地给`getDetail`操作提供需要的初始数据了。_

然后，我们给`#list`元素添加`click`和`select`事件处理函数：

```js
const list = document.getElementById('list');
list.addEventListener('click', (evt) => {
  const target = evt.target;
  if(target.tagName === 'IMG') {
    select(list, target);
  }
});

list.addEventListener('select', ({detail}) => {
  // do nothing
  console.log(detail.changed, detail.picked);
});
```

上面的代码中，虽然现在`select`事件处理函数不处理任何事情，但是我们依然可以监听它，以便将来对选择的对象进行下一步动作。它的效果如下所示：
<!-- 这样我们就实现了选择多张图片的功能，我们同样可以监听`select`方法，以便于进一步对选择的对象进行下一步动作。 -->
[在线演示](https://junyux.github.io/FE-Advance/day07/index2.html)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c6277501c6c40389b75d9222d435acf~tplv-k3u1fbpfcp-zoom-1.image)


通过第一个故事和第二个故事，我们可以把“预览”和“选择”这两个行为组合起来。比如，当鼠标点击的同时，我们按下alt建，就表示选择图片；否则就是预览图片：
<!-- 经过我们这么抽象了之后，我们实际上可以把多种行为组合在一起，比如说，我们想要同时支持图片预览和图片选择，可以这么做： -->

[在线演示](https://junyux.github.io/FE-Advance/day07/index3.html)

```js
/* ...省略其他代码... */

const list = document.getElementById('list');
list.addEventListener('click', (evt) => {
  const target = evt.target;
  if(target.tagName === 'IMG') {
    if(evt.altKey) {
      select(list, target);
    } else {
      preview(list, target);
    }
  }
});

list.addEventListener('preview', ({detail}) => {
  const {showMask} = detail;
  showMask();
});
```
如上代码所示，抽象行为的模式允许一个组件可以灵活的**组合或卸载**多个行为，且互不冲突。

<!-- 这个代码里，我们组合了两种不同的行为：`preview`和`select`，在click事件中，我们判断alt键是否被按下，如果被按下，执行的是select，否则执行的是preview，这样的两个行为互不冲突，可以很好地结合在一起使用。 -->

<!-- 在一和二两个故事里，我们实际上抽象了一个”behavior“的设计模式，通过它我们定义UI的行为，并将行为产生的状态变化用自定义事件派发的方式通知出来。这么做的意义在于，我们将每一次行为导致的UI改变独立封装起来，那么我们在做组件的复杂行为的时候，就可以比较自由地随意组合它们。 -->

但是，上面的例子只是非常粗略的抽象方式，而且还有一些争议点，比如我们可以将预览行为中的`showMask`操作直接放在`getDetail`里面完成，为什么要将它暴露给事件处理函数，在处理函数中手工调用？另外，`select`行为中，我们为什么又将`className`的变化放在`getDetail`里面而不是将它交给事件处理函数？

这里是有可权衡的地方，实际上把操作放在哪边，都各有利弊。不过我们一般遵循一个大的原则——如果操作只是处理数据或改变状态，那么将它放在`getDetail`中；但是如果同时改变了DOM结构，比如创建或删除了元素，那么这些操作我们可以交给事件处理函数处理。也就是说，`getDetail`函数只处理数据或者改变元素的`className`（即状态），不对DOM树的结构做修改。因为这样才能保证在组合多个行为下，DOM结构的稳定，否则一个行为操作的DOM元素被另一个行为删除就会导致冲突。

<!-- 因为只有保证这一原则，才能保证DOM结构的稳定，而这是组合各个行为的一个前提，因为只有这样才不会由于一个行为操作的DOM元素被另一个行为删除而导致冲突。 -->

抽象行为（behavior）模式还有很多用途，可以创造非常复杂的行为，我们将会在设计模式的课程中详细介绍。下一个故事，我们来看另一个前端常用的设计模式 —— 中间人模式。

## 第三个故事：滚动的文字

我们接下来的新任务是实现一个同步滚动的编辑与预览区，这是一些在线编辑类Web应用常见的一种交互形式。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f707a4a1f2e48c4ba911753d53a5dbb~tplv-k3u1fbpfcp-zoom-1.image)

_同步滚动的编辑与预览区_

这是页面的HTML结构：

```html
<body>
  <textarea id="editor" oninput="this.editor.update()"
            rows="6" cols="60">
在 2001 到 2003 年间，Judith Miller 在纽约时报上发表了一批文章，宣称伊拉克有能力和野心生产大规模杀伤性武器。这是假新闻。

回顾当年，我们无法确定 Miller 写的这些故事在美国 2013 年做出发动伊拉克战争的决定中扮演了怎样的角色；与 Miller 相同来源的消息与小布什政府的对外政策团队有很大关联。但是，纽约时报仍然起到了为这一政策背书的作用，尤其是对民主党人，本来他们应该会更坚定地反对小布什的政策。毕竟，纽约时报可不是一些无人问津的地方小报，它是整个美国影响力最大的报刊，它一般被认为具有左倾倾向。Miller 的故事某种程度上吻合报纸的政治倾向。

我们可以把 Miller 的错误和最近关于 Facebook 的假新闻问题联系起来看；Facebook 用自己的故事告诫我们“假新闻是坏的”。然而，我持有不同的观点：**新闻假不假没那么重要，由谁来决定什么是新闻才是第一重要的**。

<!--more-->

#### Facebook 的媒体商业化

在[聚集理论](https://stratechery.com/2015/aggregation-theory/)中，我描述了基于分配的经济权利的消亡导致强势中介的崛起，它们掌控客户体验并将它们的供应商商品化。[在 Facebook 的例子里](https://stratechery.com/2016/the-fang-playbook/)，社交网络之所以兴起，是因为之前存在的线下社会网络在往线上网络转变。考虑到人类本质是社会化的，用户开始将时间花在 Facebook 上阅读、发表观点和获取新闻。

...（此处省略）
                     
  </textarea>
  <div id="preview"> </div>
  <div id="hintbar"> 0% </div>
</body>
```

CSS样式：

```css
body{
  display: flex;
}

#editor {
  width: 45%;
  height: 350px;
  margin-right: 10px;
}

#preview {
  width: 45%;
  height: 350px;
  overflow: scroll;
}

#hintbar {
  position: absolute;
  right: 10px;
}
```

要实现这个效果，要控制3个区域的状态，左侧的编辑区，这是一个`textare`元素和其中的文本，中间的预览区，这是一个`id`为`preview`的`div`元素，右侧显示进度百分比信息，是一个`id`为`hintbar`的`div`元素。

最简单的思路是我们同步这三个区域的状态，下面我们来看一下它的实现。

首先，我们使用markdown的JS库提供接口，创建一个`Editor`的对象：

```js
function Editor(input, preview) {
  this.update = function () {
    preview.innerHTML = markdown.toHTML(input.value);
  };
  input.editor = this;
  this.update();
}
new Editor(editor, preview);
```
上面的代码把`editor`中的内容经过markdown解析后赋给`preview`元素。

而markdown库可以通过以下方式加载到我们的页面中：

```html
<script src="https://s3.ssl.qhres.com/!67fc024a/markdown.min.js"></script>
```

然后，我们来实现三部分同步的功能：

```js
//三部分 UI 耦合在一起的 update 方法
function update(src, dest, hint) {
  var scrollRange = src.scrollHeight - src.clientHeight,
      p = src.scrollTop / scrollRange;  
  
  dest.scrollTop = p * (dest.scrollHeight - dest.clientHeight);
  hint.innerHTML = Math.round(100 * p) + '%';
}

update(editor, preview, hintbar);
```
如上代码所示，`update`方法读取滚动元素（`src`）的滚动位置，换算成百分比，然后将被同步的目标元素（`dest`）的`scrollTop`属性设置为和这个百分比值对应的滚动位置。最后，将这个百分比值赋给`hint`元素。

最后，我们分别给`editor`和`preview`元素添加`scroll`事件：

```js
editor.addEventListener('scroll', function(evt) {
  update(editor, preview, hintbar);
});

preview.addEventListener('scroll', function(evt) {  
  update(preview, editor, hintbar);
});
```

这样就可以实现滚动同步了。但是，上面的代码其实存在错误。让我们来看一下现在的效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dcd152d5e6124259bb093f6a97249201~tplv-k3u1fbpfcp-zoom-1.image)

你会看到，一开始的时候，我们滚动左侧，右侧跟着滚动没有问题，但是当我们停止滚动的时候，页面竟然自己会慢慢地往上滚动回去。

为什么会出现这样的错误呢？其实问题出现在`update`方法上：

```js
function update(src, dest, hint) {
  var scrollRange = src.scrollHeight - src.clientHeight,
      p = src.scrollTop / scrollRange;  
  
  dest.scrollTop = p * (dest.scrollHeight - dest.clientHeight);
  hint.innerHTML = Math.round(100 * p) + '%';
}
```

这个方法更新了`dest`的`scrollTop`。调用`update(editor, preview, hintbar)`，就是用`editor`的滚动信息去更新`preview`的`scrollTop`。但是，在浏览器中，如果元素的`scrollTop`改变，就会自动触发`scroll`事件。因此，当我们监听`editor`的`scroll`事件：

```js
editor.addEventListener('scroll', function(evt) {
  update(editor, preview, hintbar);
});
```

在这个`scroll`事件里我们调用`update(editor, preview, hintbar)`，改变了`perview`的`scrollTop`，这时就会触发`preview`的`scroll`事件，但我们又同时监听了`preview`的`scroll`事件：

```js
preview.addEventListener('scroll', function(evt) {
  update(preview, editor, hintbar);
});
```

所以我们又执行了一次`update(preview, editor, hintbar)`，而在这里面，我们又反过来更新了`editor`的`scrollTop`，于是又触发了`editor`的`scroll`事件，这样来回反复触发，根本停不下来……

所以，要解决这个问题，我们需要保证，当`preview`的`scroll`事件被触发时，不应该马上触发`editor`的`scroll`事件。这个问题我们可以中用前面学过的`debounce`函数来解决：

```js
function debounce(fn, ms = 100) {
  let debounceTimer = null;
  return function(...args) {
    if(debounceTimer) clearTimeout(debounceTimer);

    debounceTimer = setTimeout(() => {
      fn.apply(this, args);
    }, ms);
  }
}

let scrollingTarget = null;
editor.addEventListener('scroll', function(evt){
  if(!scrollingTarget) scrollingTarget = editor;
  if(scrollingTarget === editor) update(editor, preview, hintbar);
});

editor.addEventListener('scroll', debounce(function(evt){
  scrollingTarget = null;
}));

preview.addEventListener('scroll', function(evt){  
  if(!scrollingTarget) scrollingTarget = preview;
  if(scrollingTarget === preview) update(preview, editor, hintbar);
});
```

我们定义一个`scrollingTarge`t对象，当它为`null`时，`editor`或`preview`哪一边的scroll先触发，我们就把`scrollingTarget`设为对应的对象。我们设定当scroll事件触发时，`scrollingTarget`与对应的对象相同时才会执行`update`。这样，如果我们先滚动`editor`，那么`scrollingTarget`的值被设为`editor`,这样就只有`editor`的滚动事件中，`update`才会被触发。

直到`editor`滚动结束，我们再将`scrollingTarget`重新设为null：

```js
editor.addEventListener('scroll', debounce(function(evt){
  scrollingTarget = null;
}));

/* 或者
preview.addEventListener('scroll', debounce(function(evt){
  scrollingTarget = null;
}));
*/
```

注意，因为不论哪一边调用`update`，都会触发另一边的scroll事件，所以这里我们只要`editor`或`preivew`任意一边注册了这个`debounce`变换后的函数即可，不需要两边都注册。这样我们就正常实现了滚动文字的功能了。[在线演示](https://junyux.github.io/FE-Advance/day07/index4-v1.html)

但是，上述的实现方式有明显的缺点：将三个UI元素的状态同步耦合在一个`update`函数里处理，导致这个方法不通用。假设我们要增加一个同步状态的对象或者减少一个同步状态的对象，我们都需要修改`update`的代码，而且将来要组合不同的操作改变状态也会非常麻烦。

所以，我们需要引入一种设计模式，降低这种同步状态的耦合度，使得状态同步的功能易于维护。

<!-- 所以，一个更合理的做法是将它们的状态修改分开来，这就需要引入一个设计模式： -->

**中间人（Mediator）**

一个最简单的`Mediator`模式的类定义如下：

```js
class PubSub {
  constructor() {
    this.subscribers = {};
  }

  /*
    @type 消息类型，如scroll
    @receiver 订阅者
    @fn 响应消息的处理函数
  */
  sub(type, receiver, fn) {
    this.subscribers[type] = this.subscribers[type] || [];
    this.subscribers[type].push(fn.bind(receiver));
  }

  /*
    @type 消息类型
    @sender 派发消息者
    @data 数据，比如状态数据
  */
  pub(type, sender, data) {
    const subscribers = this.subscribers[type];
    subscribers.forEach((subscriber) => {
      subscriber({type, sender, data});
    });
  }
}
```

`PubSub`类定义了一个中间人的行为。`sub`方法收集订阅者的关于`type`类型的响应行为。`pub`方法将`type`类型的消息派发给所有注册了该类型消息的订阅者。

然后，我们让`preview`、`editor`、`hintbar`元素分别监听`scroll`类型的消息。

```js
function scrollTo({data:p}){
  this.scrollTop = p * (this.scrollHeight - this.clientHeight);
}

var mediator = new PubSub();
mediator.sub('scroll', preview, scrollTo);
mediator.sub('scroll', editor, scrollTo);
mediator.sub('scroll', hintbar, function({data:p}){
  this.innerHTML = Math.round(p * 100) + '%';
});
```

接着，我们在`editor`和`preview`元素滚动的时候，让中间人派发消息：

```js
function debounce(fn, ms = 100) {
  let debounceTimer = null;
  return function(...args) {
    if(debounceTimer) clearTimeout(debounceTimer);

    debounceTimer = setTimeout(() => {
      fn.apply(this, args);
    }, ms);
  }
}

let scrollingTarget = null;
editor.addEventListener('scroll', debounce(function(evt){
  scrollingTarget = null;
}));

function updateScroll(evt) {
  var target = evt.target;
  if(!scrollingTarget) scrollingTarget = target;
  if(scrollingTarget === target) {
    var scrollRange = target.scrollHeight - target.clientHeight,
      p = target.scrollTop / scrollRange;

    // 中间人派发scroll消息
    mediator.pub('scroll', target, p);
  }
}
editor.addEventListener('scroll', updateScroll);
preview.addEventListener('scroll', updateScroll);
```

注意这里一样要使用debounce。

这样我们就实现了同样的同步滚动，完整的JavaScript代码如下：

[在线演示](https://junyux.github.io/FE-Advance/day07/index4-v2.html)

```js
function Editor(input, preview) {
  this.update = function () {
    preview.innerHTML = markdown.toHTML(input.value);
  };
  input.editor = this;
  this.update();
}
new Editor(editor, preview);

class PubSub {
  constructor() {
    this.subscribers = {};
  }
  pub(type, sender, data){
    var subscribers = this.subscribers[type];
    subscribers.forEach(function(subscriber){
      subscriber({type, sender, data});
    });
  }
  sub(type, receiver, fn){
    this.subscribers[type] = this.subscribers[type] || [];
    this.subscribers[type].push(fn.bind(receiver));
  }
}

function scrollTo({data:p}){
  this.scrollTop = p * (this.scrollHeight - this.clientHeight);
}

var mediator = new PubSub();
mediator.sub('scroll', preview, scrollTo);
mediator.sub('scroll', editor, scrollTo);
mediator.sub('scroll', hintbar, function({data:p}){
  this.innerHTML = Math.round(p * 100) + '%';
});

function debounce(fn, ms = 100) {
  let debounceTimer = null;
  return function(...args) {
    if(debounceTimer) clearTimeout(debounceTimer);

    debounceTimer = setTimeout(() => {
      fn.apply(this, args);
    }, ms);
  }
}

let scrollingTarget = null;
editor.addEventListener('scroll', debounce(function(evt){
  scrollingTarget = null;
}));

function updateScroll(evt) {
  var target = evt.target;
  if(!scrollingTarget) scrollingTarget = target;
  if(scrollingTarget === target) {
    var scrollRange = target.scrollHeight - target.clientHeight,
      p = target.scrollTop / scrollRange;
    mediator.pub('scroll', target, p);
  }
}
editor.addEventListener('scroll', updateScroll);
preview.addEventListener('scroll', updateScroll);
```

这一版代码与前面的代码相比看上去更长了，但是它不再将所有的状态同步耦合在一个`update`函数里，而是分成了发布和订阅两个部分，而且`preview`、`editor`、`hintbar`是分别订阅scroll消息的，这样就保证了UI状态的独立性。假设将来我们要取消`hintbar`的状态同步，我们可以直接注释掉订阅消息的代码：

```js
// mediator.sub('scroll', hintbar, function({data:p}){
//   this.innerHTML = Math.round(p * 100) + '%';
// });
```

这样就不需要修改任何函数的内部实现，从而提高了系统的可维护性。

当我们需要同步多个UI状态时，可以考虑采用中间人模式，用中间人统一管理UI组件的消息，在这个场景下，中间人是一个非常有效的设计模式。

今天的故事主要讲解了前端开发中两个非常常用的设计模式——行为模式和中间人模式。虽然前端开发还有很多其他的设计模式，但是这个超出了这门课的范畴。我们会在将来的设计模式的专门课程中详细讲解，敬请期待。

## 8.第八日：玩转动画

# 第七天

## 第一个故事：匀速圆周运动

动画是网页中常见的效果元素。我们在前面的故事中，也已经见过了一些动画，比如“让CSS做更多的事情”这一故事中，我们使用了CSS关键帧动画。

现代浏览器支持很多种动画方式，比如：CSS过渡动画、CSS关键帧动画、SVG动画、Web Animation API，我们还可以用JS自己实现动画。另外还有许多使用方便和功能强大的第三方动画库可以供我们使用。

今天的故事，我们将讲述两种最常用的动画模式：
- 固定轨迹的动画
- 连续的动画

### 圆周运动

第一个故事，我们先来看看固定轨迹动画的实现思路。这个动画效果是模拟地球围绕太阳做圆周运动：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8901677a7d054b6093975ed21a08d602~tplv-k3u1fbpfcp-zoom-1.image)

实现上图的动画的方式有很多，比较直接的是采用JS来实现，我们先来看一下JS实现的方案。

首先，我们用HTML元素展示动画元素：

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Document</title>
</head>
<body>
  <div class="main">
    <div id="sun">🌞</div>
    <div id="earth">🌏</div>
  </div>
</body>
</html>
```
如上代码所示，我们用两个`div`元素分别代表太阳和地球两个对象。

这是对应的CSS，设置了太阳和地球的初始位置和状态：

```css
.main {
  width: 512px;
  height: 512px;
  position: relative;
}
#sun, #earth {
  position: absolute;
  transform: translate(-50%, -50%);
}
#sun {
  font-size: 5rem;
  left: 50%;
  top: 50%;
}
#earth {
  font-size: 2rem;
}
```

在没有添加动画的时候，显示出来的界面是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e83ff0ce08c4a5c9bd85ef8a9e823d6~tplv-k3u1fbpfcp-zoom-1.image)

太阳位于`div.main`元素正中间，因为我们用了一个经典的绝对定位实现水平垂直居中的方法：

```css
#sun, #earth {
  position: absolute;
  transform: translate(-50%, -50%);
}
#sun {
  font-size: 5rem;
  left: 50%;
  top: 50%;
}
```

我们将`#sun`元素的`position`设为`absolute`，`top`和`left`设为50%，此时它的左上角是位于`div.main`元素的中心点的。然后我们再通过`transform: translate(-50%, -50%)`将它左移、上移自身宽高的一半，这样它的中心点就位于`div.main`元素的中心了。

接下来，我们要实现的效果是让地球的轨迹沿着围绕着太阳的环形运动，那么这个怎么实现呢？

这里我们复习一下高中数学知识：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa60879db6764cf48530d9fd2ef40d82~tplv-k3u1fbpfcp-zoom-1.image)

如图所示，在直角坐标系中，点p围绕半径r，圆心在原点的圆周运动，它任意时刻的坐标`px`，`py`满足：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35ebeda89831457fbf5d253465f884f7~tplv-k3u1fbpfcp-zoom-1.image)

⍺是原点到p点的线段与x轴的夹角。

这是**圆的参数方程**。

所以，我们要做的就是按照参数方程更新地球的位置就可以了。

如果我们的动画让地球围绕太阳旋转一周的周期是T，那么，地球的角速度`⍵ = 2 * Math.PI / T`，所以，⍺角是：

```js
⍺ = ⍵t = 2 * Math.PI * t / T
```

所以，我们就可以通过JS更新地球元素的`left`和`top`属性，让地球运动起来：

[在线演示](https://junyux.github.io/FE-Advance/day08/index1-v1.html)

```js
const earth = document.getElementById('earth');
const x0 = 256;
const y0 = 256;
const radius = 128;
const T = 5000; // 周期

function update(t) {
  const alpha = 2 * Math.PI * t / T;
  const x = x0 + radius * Math.cos(alpha);
  const y = y0 + radius * Math.sin(alpha);
  earth.style.left = `${x}px`;
  earth.style.top = `${y}px`;
  requestAnimationFrame(update);
}
update(0);
```

上面的代码里，x0、y0是圆心，因为太阳不在坐标原点，所以最终的公式是：

```js
const x = x0 + radius * Math.cos(alpha);
const y = y0 + radius * Math.sin(alpha);
```

然后我们通过`requestAnimationFrame`，计算x和y，不断更新`#earth`元素的`top、left`值：

```js
earth.style.left = `${x}px`;
earth.style.top = `${y}px`;
```

`requestAnimationFrame`是浏览器的API，它的参数是一个回调函数。这个API告诉浏览器有一个动画需要执行执行，并且会在浏览器下次重绘之前调用指定的回调函数更新动画。

现在我们来总结一下这种动画实现的思路：

1. 设计轨迹方程，找出动画变量和时间的关系
1. 确定动画周期和与动画变量对应的CSS属性
1. 通过`requestAnimationFrame`API，在浏览器重绘周期中更新动画变量，以实现我们需要的动画效果

使用JS是实现固定轨迹动画的一种方法，我们还可以使用CSS动画来是实现这种类型的动画。这个故事的实例中，我们使用到了圆的参数方程，而CSS动画不太好实现正余弦计算。所以，为了使用CSS实现动画，我们需要调整我们的动画计算方式，那么要如何调整呢？

<!-- 这个版本里，我们使用了JavaScript根据圆的参数方程来修改`#earth`的CSS属性的方式来实现地球绕太阳旋转的效果。这个版本的计算并不复杂，只要理解了圆的参数方程就很容易写出来。 -->
<!-- 不过除了使用圆的参数方程外，还有没有其他解决方法呢？尤其是能否不用JS，只用CSS实现？ -->

## 第二个故事：匀速圆周运动 2.0

使用CSS动画实现圆周运动，我们不能使用圆的参数方程，而需要使用圆的极坐标方程来实现。然后再通过CSS的transform和rotate，就能比较简单的实现圆周运动了。

<!-- s但是，我们不要忘记了，圆除了参数方程之外，还有极坐标方程，而恰好，CSS的transform是支持rotate的，所以我们当然可以有比较简单的用CSS动画实现圆周运动的办法。 -->
首先，我们需要调整一下我们的CSS样式，设置`transform-origin`属性改变元素旋转的参考点：

```css
.main {
  width: 512px;
  height: 512px;
  position: relative;
}
#sun, #earth {
  position: absolute;
}
#sun {
  transform: translate(-50%, -50%);
  font-size: 5rem;
  left: 50%;
  top: 50%;
}
#earth {
  left: 50%;
  top: calc(50% - 128px);
  transform-origin: 50% calc(50% + 128px);
  font-size: 2rem;
}
```
如上代码所示，我们调整了地球元素的初始位置和旋转参考点，使用了两个计算属性值: `top: calc(50% - 128px)` 和 `transform-origin: 50% calc(50% + 128px);`。

👉🏻 CSS中，`calc`可以用来在CSS属性值中执行一些计算，特别有用的是，`calc`计算可以自动转换单位，所以我们可以将百分比单位的数值和px单位的值进行加减计算。

`top: calc(50% - 128px)`表示将`#earth`元素的`top`值设在父容器50%高度，并向上偏移128px的位置。于是地球出现在太阳的正上方，距离太阳中心点的距离是128px。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfe07f24a29c4f5b804659f4ad34baf6~tplv-k3u1fbpfcp-zoom-1.image)

默认情况下，`transform`属性是以元素自身盒子的左上角作为参考点的。而在我们的例子中，我们需要让地球元素以太阳的中心点作为旋转的参考点。所以我们需要使用`transform-origin`属性改变地球元素的参点。如下图所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd65132a95234f93b9fb65ba14b0855d~tplv-k3u1fbpfcp-zoom-1.image)

<!-- 如上图所示，我们将`transform-origin`设为太阳的中心点，要使用的`transform-origin`属性值为`50% calc(50% + 128px)`。 -->
从上图我们可以看出，以太阳中心作为旋转的参考点的位置位于`50% calc(50% + 128px)`。所以，`transform-origin: 50% calc(50% + 128px)`表示将地球的旋转参考点修改到太阳的中心点。这样执行地球的`transform`属性就能让地球围着太阳转了。

然后，我们可以使用CSS关键帧动画，改变`tranform`的值：

```css
@keyframes rotate {
  to {transform: translate(-50%, -50%) rotate(1turn)}
}
```

然后我们给`#earth`元素增加动画：

```css
#earth {
  left: 50%;
  top: calc(50% - 128px);
  transform-origin: 50% calc(50% + 128px);
  font-size: 2rem;

  transform: translate(-50%, -50%) rotate(.0turn);
  animation: rotate 5s linear infinite;
}
```

最后，完整的CSS如下：

[在线演示](https://junyux.github.io/FE-Advance/day08/index1-v2.html)

```css
.main {
  width: 512px;
  height: 512px;
  position: relative;
}
#sun, #earth {
  position: absolute;
}
#sun {
  transform: translate(-50%, -50%);
  font-size: 5rem;
  left: 50%;
  top: 50%;
}
#earth {
  left: 50%;
  top: calc(50% - 128px);
  transform-origin: 50% calc(50% + 128px);
  font-size: 2rem;

  transform: translate(-50%, -50%) rotate(.0turn);
  animation: rotate 5s linear infinite;
}

@keyframes rotate {
  to {transform: translate(-50%, -50%) rotate(1turn)}
}
```

这样我们就实现了纯CSS版本的地球环绕太阳旋转的动画。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1ce90fb58fb46b7976d7210704e7fcf~tplv-k3u1fbpfcp-zoom-1.image)

比较上图和第一个故事中的效果图，你可能会发现它们之间存在细微的差别。第一版是通过参数方程计算地球相对坐标位置，动态修改坐标位置来实现，所以地球本身，除了位置相对太阳旋转，其他的状态都保持不变。而这个版本是通过旋转来实现的，地球的旋转参考点始终是对着太阳的中心点的，所以看起来好像地球自身也在旋转。这就是效果上的细微差异。
<!-- 注意，细节上，这一版和上一版略有不同，因为上一版是通过参数方程计算地球相对坐标位置，动态修改坐标位置来实现，而这一版是通过旋转来实现，所以上一版的地球本身保持不变，只是位置相对太阳旋转，而这一版，地球整体围绕太阳中心点旋转，所以看起来好像地球自身也在旋转，这是效果上的细微差异。 -->

当然，这一版我们同样也可以不用CSS关键帧动画，改用JS来控制，我们只要将CSS动画去掉，添加以下JS代码：

```js
  const earth = document.getElementById('earth');
  const T = 5000; // 5秒

  function update(t) {
    earth.style.transform = `translate(-50%, -50%) rotate(${t / T}turn)`;
    requestAnimationFrame(update);
  }
  update(0);
```

如果你这么做，你会发现在一些浏览器（包括最新的chrome浏览器）上出现奇怪的现象：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e1fad299e1f47d8941480dcab610e2b~tplv-k3u1fbpfcp-zoom-1.image)

如图所示，似乎地球在运动到某些位置的时候会突然抖动一下。不过这个不是我们代码的问题，而是chrome浏览器在处理emoji文字的`transform`属性时产生的bug。要解决这个问题，我们可以将`rotate`换成`rotate3d`:

```js
  const earth = document.getElementById('earth');
  const T = 5000; // 5秒

  function update(t) {
    earth.style.transform = `translate(-50%, -50%) rotate3d(0, 0, 1, ${t / T}turn)`;
    requestAnimationFrame(update);
  }
  update(0);
```

这里我们用`rotate3d`来代替`rotate`。`rotate3d`接受4个参数，前三个参数定义一个三维向量，第四个参数表示围绕该向量旋转，我们是在平面上旋转，要围绕z轴，所以前三个参数是`0,0,1`。

用`rotate3d`替代`rotate`之后，问题就消失了，这样我们依然可以用JS来控制动画。

第一个和第二个故事阐述了固定轨迹动画的实现思路。规定轨迹动画不仅仅是圆周运动，它还包括了渐变动画，椭圆，贝塞尔曲线等等。这些动画既可以使用JS来实现，也可以采用CSS来实现。当然，如果采用CSS动画实现，你设计的动画变量需要被CSS支持，否则是无法实现用CSS来实现的。

用JS或CSS来控制动画，各有各的好处，CSS动画更简单，能够保持WEB开发各司其职的原则，使得代码更加易于维护。而JS动画，在组合复杂的动画过程时，会更加灵活和方便。

接下来，我们就来看看更加复杂的动画应该如何实现——连续动画。

## 第三个故事：自由落体和弹跳小球

在一般情况下，简单的动画使用CSS实现会比较方便，但是一些比较复杂的动画，还是需要使用JS来实现。

比如我们实现一个模拟小球自由落体后弹跳的动画效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/718582019a554b228cac6eb9918c9572~tplv-k3u1fbpfcp-zoom-1.image)

这是相关的HTML与CSS：

```html
<div id="sphere"></div>
<div id="ground"><div>
```

```css
#sphere {
  position: absolute;
  left: 100px;
  top: 100px;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: #0af;
}

#ground {
  position: absolute;
  top: 420px;
  width: 600px;
  height: 10px;
  background: black;
}
```

这是一个连续的动画，连续的动画实际是由几个不同的阶段的轨迹动画组合而成。比如上面的例子，就是由若干个自由落体动画和匀减速动画组合而成。像这样的动画，使用CSS动画几乎没法实现，还是应该考虑使用JS动画。

第一步，我们先实现一个自由落地动画。

我们知道自由落体运动是一个初速度为0的匀加速运动，假设小球离地面高度为S，落地的时间为T，那么根据自由落体运动的公式，我们可以计算出小球的加速度为：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d7b33bb3b5341e59a06bc29ba6940c7~tplv-k3u1fbpfcp-zoom-1.image)

那么经过t时间（t <= T），小球运动的位移为：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c86af43c71144bedb41dc0e3ffecdc32~tplv-k3u1fbpfcp-zoom-1.image)

所以，我们可以这样定义自由落体动画：

```js
const S = 400; // 小球离地的初始高度
const T = 1000; // 落地时间

const target = document.getElementById('sphere')

let startTime = Date.now();

function update() {
  const t = Date.now() - startTime;
  const p = Math.min(t / T, 1);
  const top = S * p ** 2;
  target.style.top = `${top}px`; // 更新动画变量——top属性
  if(p < 1) {
    requestAnimationFrame(update);
  }
}

update();
```

一个自由落体的动画就实现了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5c22c8d779e4278897324ac5ffed06d~tplv-k3u1fbpfcp-zoom-1.image)

以上是动画的第一阶段，现在我们需要执行动画的第二个阶段——弹起。

<!-- 接下来，我们要面对一个问题，那就是我们要在一段动画执行完成之后，执行下一段动画。这是一个异步的过程。 -->
因为弹起动画是在自由落体动画结束之后，所以弹起动画必须等待自由落体动画执行结束后才能开始执行。这就涉及到一个异步的过程。我们需要对动画过程进行一下简单的封装，让它实现一个`asyn/await`的过程。

首先，利用我们之前学过的数据抽象和过程抽象，重构一下上面的代码：

```js
/*
  @target 目标动画元素
  @duration 动画经历的时间
  @progress 动画执行回调函数
*/
function animate(target, duration, progress) {
  const startTime = Date.now();
  return new Promise((resolve) => {
    function update() {
      const t = Date.now() - startTime;
      const p = Math.min(t / duration, 1);
      progress(target, p);
      if(p < 1) {
        requestAnimationFrame(update);
      } else {
        resolve(p);
      }
    }
    update();
  });
}
```

这样，自由落体的动画就可以变成：

```js
const sphere = document.getElementById('sphere');

animate(sphere, 1000, (target, p) => {
  const top = 400 * p ** 2;
  target.style.top = `${top}px`;
});
```

注意，我们在`animate`方法里返回了一个`Promise`对象，这样的话，我们就可以通过异步的`async/await`来连续执行动画。现在，我们就来实现弹起的动画。

与自由落体运动相反，弹起的动画是一个“匀减速”运动，最终将初速度降为0。

在这一阶段，小球的初速度与加速度分别是:

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab6bf89db3a149dcb9ae14aea2c7f227~tplv-k3u1fbpfcp-zoom-1.image)

那么经过t时间（t <= T），小球运动的位移为：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea9e9b987f84408e9b8cb7abfe2a8c1a~tplv-k3u1fbpfcp-zoom-1.image)

所以，弹跳阶段的JS，我们可以这样写：

```js
animate(sphere, 1000, (target, p) => {
  // 起点是400，反向运动，所以要用400减
  const top = 400 - 400 * p * (2 - p);
  target.style.top = `${top}px`;
});
```

然后，我们把两个动画连起来：

```js
(async function () {
  while(1) {
    await animate(sphere, 1000, (target, p) => {
      const top = 400 * p ** 2;
      target.style.top = `${top}px`;
    });
    await animate(sphere, 1000, (target, p) => {
      // 起点是400，反向运动，所以要用400减
      const top = 400 - 400 * p * (2 - p);
      target.style.top = `${top}px`;
    });
  }
}());
```

最终实现的效果如下图：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f7fe94f7664c9787c0dfc78229834f~tplv-k3u1fbpfcp-zoom-1.image)

这个效果不是我们最终想要的，因为小球不停地弹跳而不会停止，所以我们需要给小球增加一个能量损耗。

假设小球每次与地面碰撞后，它的动能损耗30%，那么根据能量守恒，它弹起的高度将变为之前的0.7，而它弹起的时间将变为之前的根号0.7：

所以最后我们将动画修改为：

```js
(async function () {
  let height = 400;
  let duration = 1000;

  while(1) {
    await animate(sphere, duration, (target, p) => {
      const top = (400 - height) + height * p ** 2;
      target.style.top = `${top}px`;
    });

    // 能量损耗后的动画执行高度和时间
    height *= 0.7;
    duration *= Math.sqrt(0.7);

    await animate(sphere, duration, (target, p) => {
      // 起点是400，反向运动，所以要用400减
      const top = 400 - height * p * (2 - p);
      target.style.top = `${top}px`;
    });
  }
}());
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a19a14b467fe45c4acb756e9d66f2400~tplv-k3u1fbpfcp-zoom-1.image)

所以最终就实现了我们所期望的效果。[在线演示](https://junyux.github.io/FE-Advance/day08/index2-v1.html)

现在我们来总结一下连续动画的思路：

1. 将连续的动画分解为若干个固定轨迹的动画
1. 为每个阶段的动画设计轨迹方程，找出动画变量和时间的关系
1. 确定每个阶段的动画周期（duration）和与动画变量对应的CSS属性
1. 利用异步的方式（Promise）连接每个阶段的动画，形成一个连续的动画效果

<!-- 现在我们来总结一下JS动画的要素：

JS动画的关键因素是动画的周期duration、动画便量（在这里是小球的位移）与时间的关系。实际上JS动画就是根据时间和周期来改变元素的某个CSS属性值。无论多复杂的动画，本质上都是属性关于时间的函数。实际上，不仅仅是JS动画，CSS动画也是如此，缓动（easing）函数本身就是对运动的抽象，例如自由落体运动近似等于`ease-in`，弹起的匀减速运动近似等于`ease-out`。

任何元素样式动画都能够用上述基本原理来实现，不过在某些情况下，一些特殊的效果还是需要一定的技巧和借助某些特殊CSS规则来实现。 -->

## 第四个故事：常用动画实现技巧

通过前面的三个故事，我们学习了两种非常常见的动画模式：固定轨迹动画和连续动画。

连续动画实际上是由多段固定轨迹动画组合而成的。在第三个故事里，我们使用Promise来处理连续动画，这是一种最方便的异步处理方式，在第八日的故事中，我们会有更详细的讨论。

而固定轨迹动画可以抽象为一个由**动画周期(T)**、**动画执行时间(t)**，以及**时间与属性值的映射函数(progress)** 共同决定的模型。

### 插值

在固定轨迹动画模型里，知道T、t以及progress，我们就能唯一确定动画元素target在t时刻的属性值。其中比较复杂的是progress，我们可以对它进行规范：

- progress可以由起始值（start）、结束值（end）、以及插值函数（interpolate）确定。

我们用这个规范，重构一下上一个故事中的`animate`函数：

```js
/*
  @target 目标元素
  @prop CSS属性
  @duration 动画周期
  @start 动画开始时，CSS属性的值
  @end 动画结束时，CSS属性值
  @interpolate 插值函数
*/
function animate({target, prop, duration, start, end, interpolate} = {}) {
  const startTime = Date.now();

  return new Promise((resolve) => {
    function update() {
      const t = Date.now() - startTime;
      const p = Math.min(t / duration, 1);
      target.style[prop] = interpolate(start, end, p);
      if(p < 1) {
        requestAnimationFrame(update);
      } else {
        resolve(p);
      }
    }
    update();
  });
}
```

如上代码所示，`interpolate(start, end, p)`这个函数的返回值就是根据`p`对应的比例落在`start`到`end`之间的值，也叫做**插值**。而`p`的值是在[t/duration, 1]之间 （也就是[0,1]之间)，所以这里的插值简单来说，表示根据动画的起始值（start）和动画的结束值（end)，在当前时间下计算出的位于start和end之间的值。

下面，我们来看看这个插值是如何被计算出来的：
<!-- 这样我们就可以用下面的代码来实现上一个故事中小球的自由落体动画了。 -->

```js
animate({
  target: sphere,
  prop: 'top',
  duration: 1000,
  start: 100,
  end: 400,
  interpolate(start, end, p) {
    p **= 2; //匀加速
    return `${start * (1 - p) + end * p}px`;
  }
});
```

上面的代码实现了第三个故事中自由落体的动画。其中，`start * (1 - p) + end * p`是一个最简单的插值公式，它的返回值是一个**线性插值**。如果我们不加`p **= 2`，那么返回的插值是线性的，这样的话小球就是匀速运动。
<!-- 我们来分析一下`interpolate`函数。其中，`start * (1 - p) + end * p`叫做**线性插值**，也是最简单的插值。它表示让返回的值，根据`p`对应的比例落在`start`到`end`之间，如果我们不加`p **= 2`那么用的就是线性插值，这样的话小球就是匀速运动。 -->

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ca5f721599641e0872aad4d446ff33b~tplv-k3u1fbpfcp-zoom-1.image)

如果需要小球做匀加速运动，根据前面的公式：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0dfa27328ad4d0190a193f716bea086~tplv-k3u1fbpfcp-zoom-1.image)

这里`t/T`就是`p`，当`p`等于`p ** 2`即`p`的平方，动画就变成匀加速了。

同样的，如果我们要做弹起的动画，可以：

```js
animate({
  target: sphere,
  prop: 'top',
  duration: 1000,
  start: 400,
  end: 100,
  interpolate(start, end, p) {
    p *= (2 - p); //匀减速
    return `${start * (1 - p) + end * p}px`;
  }
});
```

插值不仅可以改变像`top`、`left`或者`width`、`height`这样的属性值，还可以处理更复杂的属性值，比如颜色：

```js
function lerp(start, end, p) {
  return start * (1 - p) + end * p;
}

animate({
  target: sphere,
  prop: 'background',
  duration: 1000,
  start: [0, 170, 255],
  end: [255, 170, 0],
  interpolate(start, end, p) {
    const color = start.map((s, i) => {
      return lerp(s, end[i], p);
    });
    return `rgb(${color})`
  }
});
```

上面的代码给小球增加一个改变颜色的动画，这样我们会看到小球在弹起的同时，颜色也会发生改变。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6323756059a1454cb1d4512f8a6406ea~tplv-k3u1fbpfcp-zoom-1.image)

### 缓动

我们看到，匀速运动使用线性插值`lerp`函数，匀加速运动在线性插值前将`p`改变为`p`平方，而匀减速运动在线性插值前将`p`改变为`p*(2-p)`，实际上其他的运动形式也可以用这个模型处理，所以我们可以将改变`p`的过程抽象出来，叫做**缓动函数(easing)**。

```js
function animate({target, prop, duration, start, end, easing, interpolate} = {}) {
  const startTime = Date.now();

  return new Promise((resolve) => {
    function update() {
      const t = Date.now() - startTime;
      const p = Math.min(t / duration, 1);

      target.style[prop] = interpolate(start, end, easing ? easing(p) : p);
      if(p < 1) {
        requestAnimationFrame(update);
      } else {
        resolve(p);
      }
    }
    update();
  });
}
```

这样，匀减速的小球弹起就改写为：

```js
animate({
  target: sphere,
  prop: 'top',
  duration: 1000,
  start: 400,
  end: 100,
  easing(p) {
    return p * (2 - p);
  },
  interpolate(start, end, p) {
    return `${start * (1 - p) + end * p}px`;
  }
});
```

除了匀加速、匀减速外，我们还可以实现其他的缓动函数，比如周期运动：

```js
animate({
  target: sphere,
  prop: 'background',
  duration: 100000,
  start: [0, 170, 255],
  end: [255, 170, 0],
  easing(p) {
    return 100 * p % 1;
  },
  interpolate(start, end, p) {
    const color = start.map((s, i) => {
      return lerp(s, end[i], p);
    });
    return `rgb(${color})`
  }
});
```

如上代码所示，这是个执行100秒的动画，但是分为100个周期，每个周期背景色都是从`rgb(0, 170, 255)`线性渐变到`rgb(255, 170, 0)`。

```js
animate({
  target: sphere,
  prop: 'top',
  duration: 100000,
  start: 250,
  end: 100,
  easing(p) {
    return Math.sin(100 * Math.PI * p);
  },
  interpolate(start, end, p) {
    return `${start * (1 - p) + end * p}px`;
  }
});
```

上面的代码是执行100秒的动画，分为50个周期，让小球以250点为起点，做幅度半径为150的简谐振动。

我们可以将上面两个动画合起来，它的效果如下所示：

[在线演示](https://junyux.github.io/FE-Advance/day08/index2-ex.html)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9d1781c3dfe47439bbbde6c718029ef~tplv-k3u1fbpfcp-zoom-1.image)

如果你熟悉CSS动画，你一定知道CSS动画中也是有缓动函数的概念的，而大多数缓动效果可以使用三阶贝塞尔曲线描述。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9690aa520f84094a1776e66065821f1~tplv-k3u1fbpfcp-zoom-1.image)

三阶贝塞尔曲线是由P0、P3两个固定点和P2、P1两个动点表述的连续曲线，满足如下线性方程。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db81c2e8249d4599a21c549b3b30df6b~tplv-k3u1fbpfcp-zoom-1.image)

在CSS动画中内置了贝塞尔曲线的缓动函数，比如我们可以写这样的动画：

```html
<div id="block"></div>
```

```css
#block {
  position: absolute;
  width: 50px;
  height: 50px;
  left: 100px;
  background: red;
  animation: move 3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
}

@keyframes move {
  from {left: 100px}
  to {left: 400px}
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbf37fa72fdd4491bdd9140bd80bcf00~tplv-k3u1fbpfcp-zoom-1.image)

有许多缓动函数都可以通过三阶贝塞尔曲线来实现：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dc981aad0fd4a9fb5732cb2d35a9f64~tplv-k3u1fbpfcp-zoom-1.image)

在JS中，我们也可以构造三阶贝塞尔曲线缓动函数，我们可以直接使用[bezier-easing](https://github.com/gre/bezier-easing)这个开源库。

```html
<script src="https://s5.ssl.qhres.com/!8cf7bfcd/bezier-easing.js"></script>
```

```js
animate({
  target: sphere,
  prop: 'top',
  duration: 2000,
  start: 400,
  end: 100,
  easing: BezierEasing(0.68, -0.55, 0.265, 1.55),
  interpolate(start, end, p) {
    return `${start * (1 - p) + end * p}px`;
  }
});
```

上面的代码产生的小球动画效果如下：[在线演示](https://junyux.github.io/FE-Advance/day08/index2-ex2.html)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d741320b39746e49647f2878567820d~tplv-k3u1fbpfcp-zoom-1.image)

实际上，在较新的浏览器环境中，提供了JavaScript原生的动画API，叫做[Web Animation API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)。这是一个目前还处在草案阶段的新特性，仅被部分较新的浏览器所支持。

Web Animation API 为DOM元素提供了原生的animate方法，它接受keyframes和options两个参数，能够用JS实现和CSS基本上一致的关键帧动画：

```js
sphere.animate([
  {top: '400px'},
  {top: '100px'},
], {
  duration: 2000,
  easing: 'cubic-bezier(0.68, -0.55, 0.265, 1.55)',
  fill: 'forwards',
});
```

上面的代码和前一个例子实现的效果一致，但是不需要依赖我们自己实现的动画方法，直接用原生的`.animate`方法即可。

💡因为现在Web Animation API仍然处于ED(Editor Draft)阶段，所以支持的浏览器有限，而且未来API可能还会有所变化，所以现在不建议直接使用。

好在，通过前面的例子我们也看到，自己实现一个简单的JS动画函数，也不是什么困难的事情，有了通用灵活的动画机制，我们就可以实现各种有趣的动画效果。不过，有些特殊的动画效果，除了使用动画函数外，可能还需要运用一些特殊的CSS属性。

## 第五个故事：特殊的动画效果

前面说了动画的基本思路，基本上所有的动画都可以用前面思路来实现。这个故事，我将带你看一些用特殊的元素属性，实现比较神奇的动画效果。

### 元素渐显

最简单的渐显元素的方式是改变元素的透明度，通过操作CSS的opacity属性就能实现。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78cf1459b6bf4e539b4993e560343789~tplv-k3u1fbpfcp-zoom-1.image)

```html
<div id="content">文字内容</div>
```

```css
#content {
  display: inline-block;
  padding: 5px;
  border: solid 1px;
  font-size: 1.5rem;
  opacity: 0;
  animation: fade-in 5s infinite;
}

@keyframes fade-in {
  to {opacity: 1};
}
```

那么，如果我们要让元素从上往下，或者从左往右渐显出来，要如何实现呢：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ede00655f51242e7ae1176a66161b723~tplv-k3u1fbpfcp-zoom-1.image)

我们可以用伪元素遮盖住元素内容，然后用动画改变伪元素的宽或高：

[在线演示](https://junyux.github.io/FE-Advance/day08/index3-v2.html)

```css
#content {
  position: relative;
  display: inline-block;
  padding: 5px;
  border: solid 1px;
  font-size: 1.5rem;
}

#content::after {
  position: absolute;
  top: -1px;
  right: -1px;
  width: calc(100% + 2px);
  height: calc(100% + 2px);
  content: ' ';
  background: white;
  animation: slide 2s ease-in forwards;
}

@keyframes slide {
  to {width: 0};
}
```

上面的代码需要注意的细节是：

- 如果元素有border，伪元素的宽高要设为100%加上border，对应的`top`和`right`要设置为负的border宽度。
- 因为动画中，文字元素是从左往右显现，所以伪元素的宽度需要从左往右缩小，所以我们需要将伪元素的固定点设置在右上角或者右下角，即：设置`top`/`bottom`和`right`属性；如果动画要从右往左显现，则需要设置`top`/`bottom`和`left`属性；同样，如果从上往下显现，那么就设置`left`/`right`和`bottom`属性。

#### clip-path属性

上面这个方法有点不够完美，主要是我们给`after`伪元素设置了一个白色的背景，如果父元素的背景不是白色，或者改变了，我们就需要修改对应的属性值。实际上，这个问题有个更简单的解决方案，使用CSS的`clip-path`属性：

[在线演示](https://junyux.github.io/FE-Advance/day08/index3-v3.html)

```css
#content {
  position: relative;
  display: inline-block;
  padding: 5px;
  border: solid 1px;
  font-size: 1.5rem;
  clip-path: polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%);
  animation: slide 2s forwards;
}

@keyframes slide {
  to {clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)};
}
```

`clip-path` 属性可以创建一个只有元素的部分区域可以显示的剪切区域。区域内的部分显示，区域外的隐藏。剪切区域是被引用内嵌的URL定义的路径或者外部svg的路径，或者作为一个形状例如`polygon()`。而且，重要的是，`clip-path`支持CSS动画。

上面的代码中，我们采用`polygon`方法剪切可视区域。这个方法接受8个参数，每两个分别表示一个点的坐标。所以，`polygon(0% 0%, 0% 0%, 0% 100%, 0% 100%)`分别表示前2个点在元素的左上角，后两个点在元素的左下角。`polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)}`这个是动画结束的状态，4个点分别位于元素的左上角、右上角、右下角和左下角。所以，这段CSS规则表示的是从左到右的渐显动画。

稍微修改一下`clip-path`的初始值，我们还可以做斜向或者其他形式的渐显动画：

[在线演示](https://junyux.github.io/FE-Advance/day08/index3-v4.html)

```css
#content {
  position: relative;
  display: inline-block;
  padding: 5px;
  border: solid 1px;
  font-size: 1.5rem;
  clip-path: polygon(0% 0%, 0% 0%, 0% 0%, 0% 100%);
  animation: slide 2s forwards;
}

@keyframes slide {
  to {clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)};
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5611a1e96b6424e9ead8e270edc1179~tplv-k3u1fbpfcp-zoom-1.image)

或者：

[在线演示](https://junyux.github.io/FE-Advance/day08/index3-v5.html)

```css
#content {
  position: relative;
  display: inline-block;
  padding: 5px;
  border: solid 1px;
  font-size: 1.5rem;
  clip-path: polygon(50% 50%, 50% 50%, 50% 50%, 50% 50%);
  animation: slide 2s forwards;
}

@keyframes slide {
  to {clip-path: polygon(0% 0%, 100% 0%, 100% 100%, 0% 100%)};
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/39eb4dc4e86a431a91397c848102ae0a~tplv-k3u1fbpfcp-zoom-1.image)


#### mask属性

更复杂的渐显动画可以使用CSS遮罩：`mask`属性，不过这是一个非标准属性，目前需要加-webkit前缀，只有Chorme和Safari等少数浏览器的新版本支持。

`mask`属性可以指定图片作为元素的遮罩，遮罩外的内容隐藏，而且我们可以把遮罩设置为渐变，所以我们就可以使用渐变遮罩来实现更复杂的渐显效果。

```css
#logo {
  display: inline-block;
  width: 150px;
  height: 164px;
  background-image: url(https://p1.ssl.qhimg.com/t01d64366d00102132a.png);
  background-size: 100%;
  -webkit-mask: linear-gradient(to right, #000 0%, transparent 0) 0/20px;
}
```

如上代码所示，`-webkit-mask`可以设置一张图片作为遮罩图片，这个图片可以是SVG图片、PNG图片、线性渐变或者其他渐变，我们这里使用线性渐变。除了设置遮罩图片，还可以设置遮罩位置/宽高，`0/20px`表示遮罩位置为`0,0`，遮罩宽为20px（这里省略了y轴的100%）。

不过因为`linear-gradient`不支持CSS动画，所以我们还需要使用JS：

```js
function animate({target, prop, duration, start, end, easing, interpolate} = {}) {
  const startTime = Date.now();

  return new Promise((resolve) => {
    function update() {
      const t = Date.now() - startTime;
      const p = Math.min(t / duration, 1);

      target.style[prop] = interpolate(start, end, easing ? easing(p) : p);
      if(p < 1) {
        requestAnimationFrame(update);
      } else {
        resolve(p);
      }
    }
    update();
  });
}

animate({
  target: logo,
  prop: 'webkitMask',
  duration: 1000,
  start: 0,
  end: 100,
  interpolate(start, end, p) {
    const v = start * (1 - p) + end * p;
    return `linear-gradient(to right, #000 ${v}%, transparent 0) 0/20px`;
  }
});
```

最终实现的效果如下：[在线演示](https://junyux.github.io/FE-Advance/day08/index3-v6.html)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c4b34052a484926a21f706d654ff776~tplv-k3u1fbpfcp-zoom-1.image)

### 描边动画

描边动画是指演示描绘某个图形的动画，比如实现下面的描绘五角星动画。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90efde1974af45d1959789a6997de91a~tplv-k3u1fbpfcp-zoom-1.image)

这样的描边动画可以通过改变SVG元素的`stroke-dasharray`和`stroke-dashoffset`两个属性来实现。

[在线演示](https://junyux.github.io/FE-Advance/day08/index4.html)

```html
<svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="500" height="500">
  <g fill="none">
    <polygon points="100,10 40,180 190,60 10,60 160,180">
  </g>
</svg>
```

```css
svg polygon {
  stroke: red;
  stroke-dasharray: 1000;
  stroke-dashoffset: 1000;
  stroke-width: 5;
  animation: stroke-path 5s linear infinite;
}

@keyframes stroke-path {
  to {
    stroke-dashoffset: 0;
  }
}
```

`stroke-dasharray`表示将图形以虚线描绘，`stroke-dasharray:1000`表示虚线实线每一个线段长度都是`1000px`，一开始第一条线段是实线，第二条线段是虚线，第三条线段是实线...这样依次交替。

`stroke-dashoffset`表示虚线的偏移，将它也设置为`1000`，那么第一条线就被移出了可见区域，从虚线（即第二条线）开始展示，所以此时的五角星并没有显示出来，然后我们以动画的方式改小虚线的偏移量，这样的话，第一条线（实线）就被慢慢移回可视区域，于是图形的线条就逐步展示出来了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5ff3ccabcbd42a1adb5b2abfa450654~tplv-k3u1fbpfcp-zoom-1.image)

SVG元素除了使用CSS、JS动画，还可以使用SVG支持的SMIL动画，SMIL是Synchronized Multimedia Integration Language的简称。关于SVG的SMIL动画，超过了本课程讨论的范畴，在这里不做进一步讨论，在后续专门讨论SVG的课程中，会有深入的讨论。

## 9.第九日：高级特性与元编程

# 第九天

## 第一个故事：类的私有属性

我们知道，封装性是程序设计很重要的一个概念，我们应当能够将私有数据封装在对象、函数或模块的内部。这些私有数据，模块开发者不希望它们被模块使用者所使用。

在JavaScript中，类的私有属性是Stage3阶段的标准（处于实验性阶段），最新的一些浏览器如Chrome最新版本，支持原生的类私有属性。

在最新的浏览器中，我们可以在变量前加`#`，让变量变成私有属性：

```js
class Foo {
  #foo = 10;
 
  bar() {
    console.log(`Private foo is ${this.#foo}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 10
```

但是在较早的浏览器版本里，不支持使用原生的私有属性，这时，我们只能考虑用其他方式来实现类的私有属性。

### 传统的私有属性约定

在许多代码库或模块，尤其是早期版本的代码库或模块中，私有属性基于约定，以下划线开头：

```js
class Foo {
  constructor() {
    this._foo = 10;
  }

  bar() {
    console.log(`Private foo is ${this._foo}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 10
```

这个并不是真正的“私有属性”，因为使用者其实如果想要访问`_foo`属性，任然能够随意访问。比如：

```js
foo._foo = 20; // 使用者当然可以访问这个 _foo 属性，所以说这只是一个约定
```

### 混淆变量名

如果要比较好地防止使用者使用私有属性，我们可以用混淆变量名的方式来防止使用者随意使用某个我们不想让使用者使用的属性。

```js
const _foo = `_${Math.random().toString(36).slice(2, 10)}`;
class Foo {
  constructor() {
    this[_foo] = 10;
  }

  bar() {
    console.log(`Private foo is ${this[_foo]}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 10
```

如下图所示，Foo方法上包含有一个随机变量名的属性，在内部可以通过`this[_foo]`访问。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1b00b1d220a4df8b5a9cdb23366e4a5~tplv-k3u1fbpfcp-zoom-1.image)

当然，这样使用者仍然可以通过`foo._hodjtxxf`来访问它，但是因为不知道这个名字的含义，而且，每次运行的时候这个名字是随机的，使用者基本上没法使用这个属性了。

不过，使用者即使不知道随机的变量名，依然可以通过`Object.keys`或者`Object.entries`或者`for...in`等方法将这个属性枚举出来，所以仍然有使用这个属性的可能，但是我们可以通过将属性定义成不可枚举属性，来防止用户将它枚举出来：

```js
const _foo = `_${Math.random().toString(36).slice(2, 10)}`;
class Foo {
  constructor() {
    Object.defineProperty(this, _foo, {
      value: 10,
      enumerable: false,
    });
  }

  bar() {
    console.log(`Private foo is ${this[_foo]}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 10
```
如上代码所示，我们使用`Object.defineProperty`方法将变量`_foo`定义成不可枚举的属性。这样，用户除了能在控制台上看到这个属性之外，基本上没法使用它了。

_关于`Object.defineProperty`方法的详细用法，你可以参考《初级前端工程师JS篇》。_

### 使用Map和WeakMap

使用混淆变量名的方式，我们依然能在浏览器控制台中看到这个属性，如果要让它在控制台上也看不到，我们可以使用ES5的Map方法：

```js
const privates = new Map();
class Foo {
  constructor() {
    privates.set(this, {foo: 10, bar: 20});
  }

  bar() {
    const _ = privates.get(this);
    console.log(`Private foo is ${_.foo} and bar is ${_.bar}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 10 and bar is 20
```

使用Map，我们可以将私有属性完全封装在摸快内，在模块外不可能访问到，浏览器控制台上也看不到。

不过使用Map也有缺点，首先这个方法内部使用起来也不太方便，不像之前那样，直接通过`this[_foo]`就能读或写私有属性`_foo`；另外，如果是私有方法，也很麻烦，还要处理this。比如下面这段代码：

```js
const privates = new Map();
class Foo {
  constructor() {
    this.p = 2;
    privates.set(this, {foo: function() {return 10 * this.p}});
  }

  bar() {
    const _ = privates.get(this);
    console.log(`Private foo is ${_.foo.call(this)}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 20
```
注意，上面的代码中，我们不能直接这样调用`_.foo()`，而必须通过`call`或者`apply`方法来调用`_.foo`方法，以保证这个方法中的`this`指向的是`Foo`这个对象。

对比使用混淆变量名的方法：

```js
const _foo = `_${Math.random().toString(36).slice(2, 10)}`;
class Foo {
  constructor() {
    this.p = 2;
  }
  [_foo]() {
    return 10 * this.p;
  }
  bar() {
    console.log(`Private foo is ${this[_foo]()}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 20
```

明显还是混淆变量名的方法更简单。

另外还有一个问题，如果用Map的话，对象引用被取消的时候，因为Map中还有该引用，从而导致对象不能被引擎回收。要解决这个问题，可以将Map用WeakMap替代。

### 使用 Symbol

在ES6之后，JavaScript支持了一种新的原始类型Symbol。Symbol创建唯一的ID，可作为属性或者方法的key，同时，不会被`Object.keys`、`Object.entries`或者`for...in`枚举到。这样我们就能得到比混淆变量名更理想的方式，使用Symbol：

```js
const _foo = Symbol('foo');
class Foo {
  constructor() {
    this.p = 2;
  }
  [_foo]() {
    return 10 * this.p;
  }
  bar() {
    console.log(`Private foo is ${this[_foo]()}`);
  }
}

const foo = new Foo();
foo.bar(); //Private foo is 20
```

使用Symbol的写法和使用混淆变量名的写法基本一样，只是把

```js
const _foo = `_${Math.random().toString(36).slice(2, 10)}`;
```

替换成：

```js
const _foo = Symbol('foo');
```

这样，在模块外部是没法访问到私有属性的，但是控制台上可以在对象的原型上看到一个`Symbol(foo)`属性，如下图所示，但这个属性不会被枚举出来。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80360548a8054c4abf1bed369dd1e8a1~tplv-k3u1fbpfcp-zoom-1.image)

使用Symbol之后，如果使用者确实想要使用这个私有属性，可以使用`Object.getOwnPropertySymbols`方法获取对象上的Symbol（如果是私有方法，则要获取类的原型上的Symbol）。

比如上面的代码，要获取`_foo`私有方法，可以通过：

```js
const _privateFoo = Object.getOwnPropertySymbols(Foo.prototype)[0];

foo[_privateFoo](); // 20
```

来访问私有方法。这种私有访问方式已经非常复杂，基本上可以限制使用者使用这些私有属性和方法了，而留有这一种访问方式，也算是提供一种反射机制，给使用者留下一个后门，以便确实需要的时候进行访问。

所以，在一般的情况下，我们使用`Symbol`来定义对象的私有属性和方法，是目前比较推荐的一种方式，直到原生的私有属性从Stage3成为正式的标准之前，我们还是使用Symbol来定义私有属性和方法吧。

JavaScript中的私有属性可以通过混淆变量、Map/WeakMap，或者Symbol实现。那么我们怎样应用JS私有属性的特性呢？

## 第二个故事：使用访问器属性

一般来说，私有属性配合属性访问器使用，比如我们要想定义一个内部可读写而外部只读的属性，可以这么定义：

```js
const _name = Symbol('bar');

class Foo {
  constructor(name) {
    this[_name] = `foo: ${name}`;
  }

  get name() {
    return this[_name];
  }
}
```

我们将`Foo`的`name`属性定义为一个`get`访问器属性，这样在外部它就是只读属性。它的值由内部的私有属性`this[_name]`决定。

```js
const foo1 = new Foo('a');
const foo2 = new Foo('b');
console.log(foo1.name, foo2.name); // foo: a, foo: b

foo1.name = 'bar';
console.log(foo1.name); // foo: a
```

如上代码所示，我们可以通过`foo1.name`或者`foo2.name`来访问对象的`name`属性。但是我们不能通过`foo1.name = 'bar'`来修改对象的`name`属性值。

### 关联属性

我们在设计对象模型的时候，尽量减少要维护的数据，数据越少，意味着模型越简单，代码的可维护性越强。这时，我们可以通过**关联属性**简化对象模型中的数据。

那么，什么是关联属性呢？我们通过下面这个例子说明一下：

```html
<form>
  <div><label>姓名：</label><input id="name" type="text" value=""></div>
  <div><label>出生年月：</label>
    <select id="birth-year">
      <option>1995年</option>
      <option>1996年</option>
      <option>1997年</option>
      <option>1998年</option>
      <option>1999年</option>
      <option>2000年</option>
      <option>2001年</option>
      <option>2002年</option>
      <option>2003年</option>
      <option>2004年</option>
      <option>2005年</option>
      <option>2006年</option>
      <option>2007年</option>
    </select>
    <select id="birth-month">
      <option>1月</option>
      <option>2月</option>
      <option>3月</option>
      <option>4月</option>
      <option>5月</option>
      <option>6月</option>
      <option>7月</option>
      <option>8月</option>
      <option>9月</option>
      <option>10月</option>
      <option>11月</option>
      <option>12月</option>
    </select>
   </div>
  <div><label>年龄：</label><input id="age" type="text" value="" readonly></div>
  <div><label>用户画像：</label><input id="portrait" type="text" value="" readonly></div>
</form>
```

```css
label {
  display: inline-block;
  width: 80px;
  text-align: right;
  padding-right: 10px;
}
```

上面的代码建立了一个表单，用来显示某个用户的个人信息。它的效果如下所示：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe93f5cc3606404eb7bad669614a1c4f~tplv-k3u1fbpfcp-zoom-1.image)

我们给这个表单的信息创建了一个Person对象，包含有姓名（name）、出生年月（birthday）、年龄（age）和用户画像(protrait)等属性。

但是注意到，其实年龄和用户画像，是可以通过出生年月算出的，所以真正要维护的数据，只有姓名和出生年月。

所以我们可以这样设计Person类：

```js
const _name = Symbol('name');
const _birthYear = Symbol('birth-year');
const _birthMonth = Symbol('birth-month');

class Person {
  constructor({name, birthday}) {
    this[_name] = name;
    const date = new Date(birthday);
    this[_birthYear] = date.getFullYear(); // 出生年份
    this[_birthMonth] = date.getMonth() + 1; // 出生月份
  }
  
  get name() {
    return this[_name];
  }
  
  get birthday() {
    return {
      year: this[_birthYear],
      month: this[_birthMonth],
    };
  }
  
  get age() { // 根据出生年份计算age属性值
    return new Date().getFullYear() - this[_birthYear];
  }
  
  get portrait() { // 根据age属性计算portrait属性值
    if(this.age <= 18) return '少年';
    else return '成年';
  }
}
```

上面的代码中，我们设计三个私有属性`[_name]`、`[_birthYear]`和`[_birthMonth]`，分别存储初始化的姓名、出生年和月的信息。我们用四个访问器属性来提供给使用者`name`、`birthday`、`age`、`portrait`四个对象属性，它们都是只读的。其中，`age`和`portrait`属性就是**关联属性**，它们的值都是根据`birthday`属性值的变化而变化。

然后，我们可以将它们绑定到DOM元素上：

```js
function updatePerson(person) {
  const name = document.getElementById('name');
  name.value = person.name;
  const birthYear = document.getElementById('birth-year');
  const birthMonth = document.getElementById('birth-month');
  const {year, month} = person.birthday;
  birthYear.value = `${year}年`;
  birthMonth.value = `${month}月`;
  const age = document.getElementById('age');
  age.value = `${person.age}岁`;
  const portrait = document.getElementById('portrait');
  portrait.value = person.portrait;
}

const p = new Person({name:'张三', birthday:'1999-12'});
updatePerson(p);
```

这样就实现了UI组件的更新。

不过，上面这个代码仅仅能实现将数据更新给UI组件，如果我们操作UI组件，改变内容，数据并不会主动跟着变化，关联的UI也不会更新。比如，我们操作下拉框，将张三的出身生年月改成2006年，用户画像那一栏里的“成年”，并不会被自动更新成“少年”。这样的UI，所有的操作都需要我们手动去控制，用起来比较繁琐。而且在产品需求比较复杂的时候，如果我们要根据用户的交互，用同一组数据更新多处UI，用JavaScript手动操作DOM元素，会使得页面逻辑变得非常复杂。

### 监听属性改变

现在比较流行的一种设计是，让UI绑定对象的数据，在某个对象的属性发生变化的时候，UI收到属性改变的消息，自动更新。

这种设计强调以数据为中心，开发者只操作数据，让数据改变去自动更新对应的UI。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2d70f9d9283c4d6790dc3da26ab8ab9c~tplv-k3u1fbpfcp-zoom-1.image)

这样的方法叫做**数据驱动UI**或者**响应式数据绑定**。那么具体怎么实现呢？

我们稍稍修改一下前面例子的UI：

```html
<div id="avatar">姓名</div>
<form>
  <div><label>姓名：</label><input id="name" type="text" value=""></div>
  <div><label>出生年月：</label>
    <select id="birth-year">
      <option>1995年</option>
      <option>1996年</option>
      <option>1997年</option>
      <option>1998年</option>
      <option>1999年</option>
      <option>2000年</option>
      <option>2001年</option>
      <option>2002年</option>
      <option>2003年</option>
      <option>2004年</option>
      <option>2005年</option>
      <option>2006年</option>
      <option>2007年</option>
    </select>
    <select id="birth-month">
      <option>1月</option>
      <option>2月</option>
      <option>3月</option>
      <option>4月</option>
      <option>5月</option>
      <option>6月</option>
      <option>7月</option>
      <option>8月</option>
      <option>9月</option>
      <option>10月</option>
      <option>11月</option>
      <option>12月</option>
    </select>
   </div>
  <div><label>年龄：</label><input id="age" type="text" value="" readonly></div>
  <div><label>用户画像：</label><input id="portrait" type="text" value="" readonly></div>
</form>
```

```css
label {
  display: inline-block;
  width: 80px;
  text-align: right;
  padding-right: 10px;
}

#avatar {
  display: inline-block;
  width: 100px;
  height: 120px;
  border: solid 1px;
  margin-left: 10px;
  line-height: 100px;
  text-align: center;
}

form {
  float: left;
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ca8cb84648944cb899621afe7a55d28~tplv-k3u1fbpfcp-zoom-1.image)

然后修改一下JS：

```js
// 中间人
class PubSub {
  constructor() {
    this.subscribers = {};
  }

  /*
    @type 消息类型，如scroll
    @receiver 订阅者
    @fn 响应消息的处理函数
  */
  sub(type, receiver, fn) {
    this.subscribers[type] = this.subscribers[type] || [];
    this.subscribers[type].push(fn.bind(receiver));
  }

  /*
    @type 消息类型
    @sender 派发消息者
    @data 数据，比如状态数据
  */
  pub(type, sender, data) {
    const subscribers = this.subscribers[type];
    subscribers.forEach((subscriber) => {
      subscriber({type, sender, data});
    });
  }
}

const name = document.getElementById('name');
const avatar = document.getElementById('avatar');
const birthYear = document.getElementById('birth-year');
const birthMonth = document.getElementById('birth-month');
const age = document.getElementById('age');
const portrait = document.getElementById('portrait');

// 根据person模型数据更新UI
function updatePerson(person) {
  name.value = person.name;
  const {year, month} = person.birthday;
  birthYear.value = `${year}年`;
  birthMonth.value = `${month}月`;
  age.value = `${person.age}岁`;
  portrait.value = person.portrait;
  avatar.innerHTML = person.name;
}

const p = new Person({name: '张三', birthday: '1999-12'});
// 注册需要监听的change事件
p.watcher.sub('change', null, ({sender}) => {
  updatePerson(sender); // 更新UI
});
updatePerson(p);

name.addEventListener('change', (e) => {
  p.name = e.target.value;
});

birthYear.addEventListener('change', (e) => {
  p.birthday = {year: parseInt(e.target.value, 10)};
});

birthMonth.addEventListener('change', (e) => {
  p.birthday = {month: parseInt(e.target.value, 10)};
});
```

如上代码所示，我们用在第六日中学到过的设计模式——中间人模式，给`Person`对象的`name`和`birthday`属性添加set访问器属性，并添加了一个`watcher`只读属性，用来监听`Person`对象的属性变化。

我们在`name`和`birthday`属性的set访问器中调用`Person`对象的`update`方法，在`update`方法里通过中间人pub一条`change`消息。然后我们通过`p.watcher.sub`监听这条消息，在监听器中调用`updatePerson`方法更新数据到DOM元素。

这样我们在`name`、`birthYear`和`birthMonth`三个UI元素内容改变的时候，回写数据给Person对象，而Person对象数据改变，就会自动通过`watcher`执行`updatePerson`。于是这段代码的效果就是，当用户通过操作表单修改name、birthday时，UI上相关的内容就会自动更新了。[在线演示](https://junyux.github.io/FE-Advance/day09/index1.html)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98830f1af1e24ebab3820e750b51bf9b~tplv-k3u1fbpfcp-zoom-1.image)

所以，如上面例子所示，属性访问器能够实现响应式数据绑定，为我们处理复杂UI问题带来便利。不过，这个例子中的属性访问器也有些不足之处，因为每次添加一个set属性，我们就需要记得调用一下对象的`update`方法，由这个方法负责通知消息监听者对象属性改变。当我们的对象属性很多的时候，有可能因为忘记调用`update`方法产生错误。不过，JavaScript还有一个更强的特性，可以监听对象上任意属性的读写操作，我们在下一个故事中来讨论它。

## 第三个故事：使用代理Proxy

Proxy是ES6之后内置的JavaScript标准对象，它可以代理一个目标对象，以拦截该目标对象的**基本操作**。
<!-- 对被代理对象的**基本操作**进行拦截处理。 -->

我们用一个简单的例子，来看看Proxy对象是如何使用的：

我们知道，JavaScript对象访问一个不存在的属性的时候，该属性返回undefined。假设我们现在希望提供给用户一个对象，当用户访问这个对象时，若属性不存在则抛出异常。

```js
let handler = {
  get: function(target, name){
    if(name in target) {
      return target[name];
    }
    throw new Error('invalid property');
  }
};

const p = new Proxy({}, handler);

p.a = 1;
p.b = 2;

console.log(p.a, p.b); // 1, 2
console.log(p.c); // Error: invalid property
```
以上的代码中，Proxy构造器接受两个参数，第一个参数表示被代理的对象，第二个对象表示拦截对象（也就是`hanlder`)。那么这个`handler`对象拦截什么呢？ `get: function(target, name){...}`表示拦截被拦截对象中所有的get访问器属性，如果`target`（即，被拦截对象）中的`name`属性不存在，那么就抛出错误。

Proxy对象不能被直接继承：

```js
class PObject extends Proxy {
  
}
```

像上面这样继承会报错：

```
VM158:1 Uncaught TypeError: Class extends value does not have valid prototype property undefined
    at <anonymous>:1:23
```

但是，我们可以通过将原型设为代理对象来做到。

所以如果我们想要定义一组类，拥有上面那种拦截特性，我们可以这么做：

```js
let handler = {
  get: function(target, name){
    if(name in target) {
      return target[name];
    }
    throw new Error('invalid property');
  }
};

function Base() {} // 定义一个Base类
Base.prototype = new Proxy({}, handler);

class Foo extends Base {
  constructor() {
    super();
    this.a = 1;
    this.b = 2;
  }
}

const foo = new Foo();
console.log(foo.a, foo.b); // 1, 2
console.log(foo.c); // Error: invalid property
```

如上代码所示，我们首先定义了一个名叫Base的基类。然后将这个Base对象的`prototype`设置为Proxy对象。这样继承了Base类的Foo对象就有了拦截不存在属性的特性。

了解了JS的Proxy对象的特性和使用， 我们可以改造一下上一篇中监听属性变化的代码——用Proxy来拦截属性的变化：

```js
const _name = Symbol('name');
const _birthYear = Symbol('birth-year');
const _birthMonth = Symbol('birth-month');

/*
  这个person类的定义中，去掉了中间人的设置
*/
class Person {
  constructor({name, birthday}) {
    this[_name] = name;
    const date = new Date(birthday);
    this[_birthYear] = date.getFullYear();
    this[_birthMonth] = date.getMonth() + 1;
  }
  
  get name() {
    return this[_name];
  }
  
  set name(value) {
    this[_name] = value;
  }
  
  get birthday() {
    return {
      year: this[_birthYear],
      month: this[_birthMonth],
    };
  }
  
  set birthday({year = this[_birthYear], month = this[_birthMonth]}) {
    this[_birthYear] = year;
    this[_birthMonth] = month;
  }
  
  get age() {
    return new Date().getFullYear() - this[_birthYear];
  }
  
  get portrait() {
    if(this.age <= 18) return '少年';
    return '成年';
  }
}

const name = document.getElementById('name');
const avatar = document.getElementById('avatar');
const birthYear = document.getElementById('birth-year');
const birthMonth = document.getElementById('birth-month');
const age = document.getElementById('age');
const portrait = document.getElementById('portrait');

function updatePerson(person) {
  name.value = person.name;
  const {year, month} = person.birthday;
  birthYear.value = `${year}年`;
  birthMonth.value = `${month}月`;
  age.value = `${person.age}岁`;
  portrait.value = person.portrait;
  avatar.innerHTML = person.name;
}

let p = new Person({name: '张三', birthday: '1999-12'});

function watch(obj, onchange) {
  /*
    这个代理对象表示拦截persion对象的属性赋值操作，在属性赋值操作后，都执行一次onchange方法。这样就无需派发消息的中间人，但又实现了数据驱动UI的效果。
  */
  return new Proxy(obj, {
    set(target, name, value) {
      Reflect.set(target, name, value); // 调用person对象的原始操作(即，属性赋值操作)
      onchange(target, {[name]: value});
      return true; // 表示成功
    },
  });
}

p = watch(p, (subject) => {
  updatePerson(subject);
});
updatePerson(p);

name.addEventListener('change', (e) => {
  p.name = e.target.value;
});

birthYear.addEventListener('change', (e) => {
  p.birthday = {year: parseInt(e.target.value, 10)};
});

birthMonth.addEventListener('change', (e) => {
  p.birthday = {month: parseInt(e.target.value, 10)};
});
```

上面的代码，使用Proxy来拦截属性变化，这样就不用在Person上定义和手工调用`update`方法了。[在线演示](https://junyux.github.io/FE-Advance/day09/index2.html)

Proxy还有很多拦截对象行为的方式，利用这些方式可以改变或扩展JavaScript代码的语义。

通常情况下，我们把改变或扩展编程语言语义的行为，叫做**元编程**(Meta-Programming)。下面我们就通过一些实例来说明Proxy是如何改变语言的语义的。

改变`in`操作符的语义：

```js
const text = `君喻教育。
君子之教，喻也。
http://junyux.com`;

const p = new Proxy(new String(text), {
  has: function(target, name) {
     return target.indexOf(name) >= 0;
  }
});

console.log('君喻' in p);
console.log('君子之教' in p);
console.log('junyux.com' in p);
console.log('foo' in p);
```

在上面的代码里，我们通过Proxy改变了对象的`in`操作符的语义，将它从判断是否是对象上的属性，变为了判断字符串是否在被代理的文本内容中。

注意，这里我们用了一个字符串的装箱操作（即，将原始类型string包装成对象String），因为Proxy的第一个参数必须是一个对象。

我们再来看一个例子——改变对象赋值的语义：

```html
<ul>
  <li>1</li>
  <li>2</li>
  <li>3</li>
  <li>4</li>
  <li>5</li>
  <li>6</li>
</ul>
```

```css
li.selected {
  color: red;
}
```

```js
let view = new Proxy({
  selected: null
},
{
  set: function(target, prop, newval) {
    let oldval = target[prop];

    if (prop === 'selected') {
      if (oldval) {
        oldval.className = '';
      }
      if (newval) {
        newval.className = 'selected';
      }
    }

    Reflect.set(target, prop, newval);

    return true;
  }
});

const list = document.querySelectorAll('ul li');
view.selected = list[1];

setTimeout(() => {
  view.selected = list[2];
}, 1000);

setTimeout(() => {
  view.selected = list[3];
}, 2000);
```
上面的代码中，Proxy对象`view`是`{selected: null}`对象的代理。当我们设置它的`selected`属性的时候，它不仅改变了`selected`属性的值，而且还改变了被选中元素对象的`className`的属性值。这样，我们使用这个`view`，就可以方便地选择元素，而不用每次手工去切换元素的状态。

第三个例子——改变对象get访问器的语义：

有时候，我们要创建一个复杂的多级的配置。因为我们不知道某个配置项是否存在，通常情况下我们可能会这样写：

```js
const config = {...}

// 添加新的内容

config.db = config.db || {};
config.db.mysql = config.db.mysql || {};
config.db.mysql.server = config.db.mysql.server || {};
config.db.mysql.server.connectCount = 2;
```

如果用Proxy，我们可以创建一个这样的对象：

```js
function Configure(config = {}) {
  return new Proxy(config, {
    get(target, key, receiver) {
      if(!Reflect.has(target, key) && key !== 'toJSON') { // 如果key不存在，创建空对象并返回
        const ret = {}
        Reflect.set(target, key, ret)
        return new Configure(ret)
      } else {
        const ret = Reflect.get(target, key)
        if(ret && typeof ret === 'object') {
          // 如果key存在，且key的值是一个对象，那么执行递归
          return new Configure(ret)
        }
        return ret // 如果key存在且不是个对象，直接返回key的值
      }
    }
  })
}

let config = new Configure();
config.db.mysql.server.connectCount = 2;

console.log(JSON.stringify(config)); // {"db":{"mysql":{"server":{"connectCount":2}}}}
```

在上面的代码里，我们使用一个get拦截器，判断当前key是否存在，如果不存在，那么就创建一个空对象{}，并返回这个空对象的代理。如果当前key存在，并且是一个对象，那么将这个对象的代码返回。这样我们就能递归地自动创建多级多级属性，然后赋值，不需要一层一层去判断属性是否存在了。

上面这些例子是关于Proxy的应用。实际上Proxy是属于ES6提供的比较高级的元编程功能，用它能够改变对象的许多默认行为，从而改变或创造新的语义。不过除了Proxy之外，还有一些语言特性也能改变或创造新的语义，我们再继续看下一个故事。

## 第四个故事：属性描述符、Object对象和Symbols

如果你使用过早期版本的JavaScript(ES5之前的版本)，你可能听过“忠告”，说不要往Object.prototype或Array.prototype上添加任何东西。

这是因为，默认定义在对象或对象原型上的属性都是可枚举的，也就是说，这些属性会被`for...in`方法枚举出来。

```js
Array.prototype.foo = function(){
  console.log(foo);
}

const a = [1, 2, 3];

for(let i in a) {
  console.log(i); // 0, 1, 2, foo
}
```

上面的代码在`for...in`的时候会打印出 `0,1,2,foo`。

要避免这个问题，要么在for循环中判断：

```js
for(let i in a) {
  if(a.hasOwnProperty(i)) {
    console.log(i);
  }
}
```

通过对象的`hasOwnProperty`方法将原型上添加的方法排除。

要么，通过`Object.defineProperty`，将`foo`方法设置为不可枚举。

```js
Object.defineProperty(Array.prototype, 'foo', {
  value: function() {
    return 'foo';
  },
  // enumerable: false, 默认值就是false
});
const a = [1, 2, 3];

for(let i in a) {
  console.log(i); // 1, 2, 3
}
```
如上代码所示，`Object.defineProperty`通过属性描述符定义对象的属性，使用这种方式定义的属性，默认情况下是不可枚举的。

`Object.defineProperty`除了改变枚举方式之外，还可以改变读写和删除操作的结果。

在对象上要定义一个只读属性，通过`defineProperty`有两种办法，如果是数据，我们可以将`writable`属性置为`false`（实际上默认值就是`false`）。

试着改写一下上面的代码的`Array.prototype.foo`：

```js
Array.prototype.foo = 'bar';

console.log(Array.prototype.foo); // function()...
```

如上代码所示，我们试图修改`Array.prototype.foo`为数据`bar`， 但是结果依然是function，说明`foo`属性是一个只读属性。

另一种办法是为它设置一个get访问器：

```js
Object.defineProperty(Array.prototype, 'foo', {
  get: function() {
    return 'foo';
  },
});
```

属性访问器只有`get`没有`set`的话，那么这个属性就不可写。

这个属性除了不可写，也是不可改变的，比如无法用`delete`删除。

```js
delete Array.prototype.foo;

console.log(Array.prototype.foo); // function()...
```
这段代码，我们试图用`delete`删除Array原型上的`foo`属性，但是没有成功。这是因为，属性描述符还有一个属性叫`configurable`，定义属性是否可被删除，默认值也是`false`。

我们通过普通的赋值方式设置的属性，它的`enumerable`、`writable`和`configurable`都是`true`。

也就是说，下面这个语句：

```js
obj.foo = 'foo';
```

等价于

```js
Object.defineProperty(obj, 'foo', {
  value: 'foo',
  enumerable: true,
  writable: true,
  configurable: true,
})
```

如果在`class`中定义的方法默认`enumerable`是`false`，而`writable`和`configurable`都是`true`。比如：

```js
class Foo {
  foo() {
    return 'foo';
  }
}
```

相当于：

```js
Object.defineProperty(Foo.prototype, 'foo', {
  value: function() {
    return 'foo';
  },
  writable: true,
  configurable: true,
});
```

除了属性描述符可以在定义属性的时候决定属性是否可枚举、是否可写、是否可删除外，Object上还提供了一些辅助方法来改变一个对象的属性操作方式。

比如我们如果不希望一个对象的属性在运行时发生改变，可以用`Object.freeze`方法将它“冻结”。

```js
const obj = {
  x: 1,
  y: 2,
};

Object.freeze(obj);

obj.x = -1;
obj.y = -2;
obj.z = 3;

console.log(obj); // {x: 1, y: 2}

delete obj.x;

console.log(obj); // {x: 1, y: 2}
```

“冻结”对象相当于将对象上的所有属性都设为不可写（`writable: false`）、不可改变（`configurable: false`），并且不允许再新增属性。不过，如果这个对象上本身有引用类型的属性，这个属性的那个对象依然是可写的。

```js
const obj = {
  x: 1,
  y: 2,
  z: {},
};

Object.freeze(obj);

obj.z.a = 10;

console.log(obj.z.a); // 10
```

对应地，如果我们不想让对象不可写，只是希望对象的属性不能新增或删除，那么可以使用`Object.seal`，相当于将对象上的所有属性都设为不可改变（即，`configurable: false`），并且不允许再新增属性。

通常情况下，如果我们有很大的数据项，而这些数据项一旦加载之后就不可改变，我们可以将它通过`Object.freeze`冻结，这样在一定程度上可以提升性能，JS引擎在这里做了优化。

而`Object.seal`对性能没有影响，但在一些场景下也会有用。比如我们给一个对象设置很多可配置的属性，为了防止用户因为拼写错误给对象添加了错误的属性，我们可以通过`Object.seal`将对象属性锁住。

另外，对象一旦被`Object.freeze`或`Object.seal`，则不能再还原成正常的对象。所以，如果我们不希望使用这两个方法改变原对象，但又希望达到同样的效果，我们可以使用上一节里的`Proxy`来模拟类似的功能。

```js
/*
  Proxy中可以通过defineProperty拦截对象新属性的赋值和defineProperty操作
  通过deleteProperty拦截对象删除属性的操作
 */
const sealHandler = {
  deleteProperty(target, name) {
    return false; // 禁止delete属性
  },
  defineProperty: function (target, name) {
    return target; // 禁止defineProperty
  },
}

const o = new Proxy({
  x: 1, 
  y: 2,
}, sealHandler);

console.log(o.x, o.y); // 1 2
o.z = 3;
console.log(o.z); // undefined
console.log(Object.keys(o)); // ["x", "y"]
delete o.x; // 此操作不成功
console.log(o.x, o.y); // 1 2
Object.defineProperty(o, 'z', {
  value: 3,
});
console.log(o.z); // undefined
```
上面的代码使用Proxy模拟了`Object.freeze`的操作。在不改变原对象（`{x: 1, y: 2}`）的情况下，使用者无法对这个对象进行增加新属性、删除属性以及修改属性操作。

除了用属性描述符和`Object.freeze`、`Object.seal`改变对象行为之外，引擎提供了一些内置的`Symbol`，可以改写对象内部的语义。

比如，我们可以通过给对象的`Symbol.iterator`属性设置方法，来影响目标对象的数组`spread`操作（即，`...`操作符）结果和`for...of`行为。

```js
const _baseUrl = Symbol('baseUrl');
const _paths = Symbol('paths');

class Router {
  constructor(baseUrl = './') {
    this[_baseUrl] = baseUrl;
    this[_paths] = new Set();
  }

  addPath(path) {
    this[_paths].add(path);
  }
  
  *[Symbol.iterator]() {
    const baseUrl = this[_baseUrl];
    for(let path of this[_paths]) {
      yield `${baseUrl}/${path}`;
    }
  }
}

const router = new Router('./src');

router.addPath('a/b');
router.addPath('c/d');

console.log([...router]); // ["./src/a/b", "./src/c/d"]
```

还有设置对象的`Symbol.toStringTag`会影响一个对象被`Object.prototype.toString`调用时返回的值。从而也改变它默认的`toString`行为。

```js
class Foo {
  get [Symbol.toStringTag]() {
    return this.constructor.name;
  }  
}

const foo = new Foo();

console.log(foo + ''); // [object Foo]
```

此外，改写类的静态方法`Symbol.hasInstance`，可以改变`instanceof`操作的结果。因为JavaScript的类继承是单继承，所以在需要多继承的时候，我们只能通过混合的方式来处理：

```js
class A {
  constructor() {
  }

  methodA() {
    console.log('method A');
  }
}

class B extends A {
  constructor() {
    super();
  }
  methodB() {
    console.log('method B');
  }
}

const InterfaceC = {
  // [Symbol.hasInstance](obj) {
  //   return obj instanceof B;
  // },
  methodC() {
    console.log('method C');
  }
};

Object.assign(B.prototype, InterfaceC);

const b = new B();

console.log(b.a, b.b, b.methodA(), b.methodB(), b.methodC()); // a, b, method A, method B, method C

console.log(b instanceof B); // true
console.log(b instanceof A); // true
console.log(b instanceof InterfaceC); // false
```

上面的代码定义了A、B两个类，B继承了A，另外我们定义了一个接口InterfaceC，我们将InterfaceC的属性通过`Object.assign`给赋值到B的原型上，这样B的实例（`b`）就能调用InterfaceC的方法（即，`b.methodC()`）。但是，使用`instanceof` 判断对象`b`是否是InterfaceC的实例时，却返回了false。

为了让`instanceof`方法正常处理多继承，我们需要使用`[Symbol.hasInstance]`方法，并让它返回`obj instanceof B`，这样的话，就能让B实例的行为真正像是InterfaceC的实例了，即`b instanceof InterfaceC`返回true。如下代码所示：

```js
// ...省略其他的代码...
const InterfaceC = {
  [Symbol.hasInstance](obj) {
    return obj instanceof B;
  },
};

console.log(b instanceof InterfaceC); // true
```

除了这些以外，Symbol上还有`Symbol.match`可以设置字符串操作`String.prototype.match`的返回结果，还有`Symbol.split`、`Symbol.search`、`Symbol.replace`等等，也是控制相应的字符串操作的结果，另外还有`Symbol.toPrimitive`能够控制对象转换成原始类型的值，等等，还有许多有用的方法，虽然不太常用，但是确实能改变对象的语义，在这里就不一一列出了，有兴趣的同学可以自行查阅[MDN文档](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol#)。

