---
title: 前端自动化测试精讲
author: 前端自动化测试精讲
date: 2025-02-14
lang: zh-CN
---

## 1.开篇词：如何写前端的自动化测试？

一个需要多人合作、开发周期长的大规模前端项目，因为项目大，排期紧张，很容易出现一些问题，比如：

-   代码风格各不相同，像一个千奇百怪的房子，相同的逻辑可能会有不同的写法或使用不同的依赖；
-   代码过度耦合，阅读和维护极其困难，常常改了一处代码，却影响到了你完全想不到的地方，导致只敢增加代码装饰功能，不敢修改或删除，重构更是完全无法推进；
-   组件职责不够单一，经常会耦合一些业务逻辑，或者加入一些奇怪的代码，如果没写注释，完全 get 不到之前的维护者想干嘛，复用效率低下；
-   新同学上手慢，因为项目大、杂、乱，新手同学本来业务逻辑就不算熟练，上手也畏手畏脚，加上风格各异，导致新同学代码风格慢慢也变成大杂烩，代码屎山越堆越高，最后项目废弃，或者推倒重来；
-   ……

而且，除了业务项目外，我们通常还会做一些基础建设，例如组件库、脚手架、函数库…… 方便不同方向的同学使用。问题是，我们怎么去说服大家去使用我们的库呢？

我们是否能够保证项目的稳定？如果在后续的维护中，一不小心影响到了之前的功能怎么办？类似这种通用库，发布一个有严重 Bug 的版本，可能就会造成成百上千的项目一起崩溃，仅仅通过自测是很没有说服力且没有底气的。

**所以，我们需要自动化测试。**

对核心组件覆盖自动化测试，可以有效地保证组件功能的单一，起到警醒工程师的作用，而不至于让不同的业务代码相互耦合；新同学可以通过单测快速 get 到这个组件打算做什么、有什么能力，不论是后续的维护还是重构都会更有底气。

对于通用的基础建设，相比手工测试，自动化测试的覆盖率更有说服力，并且可以有效规避某次修改引起的历史功能的异常，从而保证整体功能的稳定。

想必大家也知道自动化测试的重要性。其实，对于前端工程师而言，最大的痛点在于，**不知道该怎么去写对应的测试用例。**

## 如何写前端的自动化测试？

相比 Golang 、 Java 等纯后端逻辑的自动化测试，前端的自动化测试大部分需要模拟浏览器环境，进行对应 DOM 和 事件效果的断言，这也是 QA 常称的 UI 自动化测试。相比之下，会更为复杂且难上手，很多同学想接触但是不知从何开始。

为此，我特意向优秀开源项目 Semi 技术团队的同学取经，一起探讨了如何有效地进行代码测试，并且向项目中进行推广。经过长达几个月的业务实践完善，综合未来趋势和单测稳定性等因素（具体会在 [2 | 技术选型：React Testing Library Or Enzyme？](https://juejin.cn/book/7174044519350927395/section/7176612133294063668) 中详细介绍），在 Semi 测试方案选型上做出了更适合同学们学习的改进，技术选型上使用 Jest + React Testing Library + Cypress + Storybook。

Jest 是一个 JavaScript 集大成的测试库，是我们单元测试的基础，而 React Testing Library 则提供了一些 React Component 的 Api ，来协助我们进行 React Dom 和事件相关的单测编写。通过单元测试，我们只能覆盖组件中的除滚动外的大部分场景，对于一些复杂场景覆盖就会比较困难，而 Cypress + Storybook 则可以通过 E2E 端对端的方式帮我们弥补这部分覆盖的缺陷。

我将基于这套技术，从四个维度带大家学习自动化测试：

1.  使用 Jest + React Testing Library 来对浏览器 Dom 和事件进行模拟，掌握如何对组件场景进行前端的单元测试。
1.  使用 Cypress + Storybook 进行用户视角的端对端测试，补全单元测试难以模拟的场景。
1.  对项目进行自动化测试覆盖率的覆盖，并且通过 CICD 进行测试报告的自动生成，将自动化测试融入代码开发中 。
1.  对自动化测试的边界和深度有更深入的思考，因地制宜，结合项目场景去使用自动化测试，避免秀技和 沦为 kpi 的自动化测试工具人。

## 小册介绍

最终设计出如下的小册大纲，希望可以借此帮助同学们写出高质量代码，提高整体编程素质。

小册模块可以分为四个方向，**单元测试** **、端对端测试、持续集成、测试理论。**

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b903e13bccc4d21ac16925b60fb5f24~tplv-k3u1fbpfcp-watermark.image?)

-   单元测试：我们将结合不同的案例来学习 Jest 的基础知识，并基于 React Testing Library 模拟浏览器 dom 和事件，对组件进行更加精准的自动化测试，这将是本小册最重点的学习内容，通过这部分的学习，大家将对大部分场景的自动化测试游刃有余。
-   端对端测试：我们将学习从用户视角进行对应的端对端测试，在这个模块，我们将使用业内主流的端对端测试方案 Cypress 进行用户操作的模拟，完善单测无法覆盖的复杂场景，比如滚动、页面跳转等。
-   持续集成：我们将站在项目视角，来介绍如何将自动化测试覆盖到项目开发中，自动生成测试报告的内容。
-   测试理论：我们将深度思考如何善用自动化测试，不让它成为 kpi 的工具和工程师的负担。工欲善其事，必先利其器，去思考理解自动化测试的意义，结合项目的实际场景，才能真正实现提高整体项目代码质量和风格的初衷。

看过我上一本小册的同学应该大致了解我的写作风格，同样地，为了大家可以更好的理解理论知识，我将**针对具体的场景，从零手写教学代码，** 结合代码讲解对应的知识，每一节课如果涉及代码，将会在课程的最顶部加上对应仓库的链接，大家可以 clone 下来结合学习加深印象。

从下一节课开始，我们开始单元测试模块的学习，前端的单元测试可以分为逻辑和环境模拟两个部分，对于逻辑的部分，我们通常使用 Jest 进行逻辑的断言，这是一套稳定的基于 JS 的测试框架，至于浏览器环境的模拟，有两套主流的辅助库，Enzyme 和 React Testing Library，下一节我们将来一起对比这两套方案，看看哪个更适合我们的业务开发。

## 10.Mock：怎么替代不需要关注的逻辑？

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了 Jest 提供的 FakeTimer，通过它我们可以“快进”定时任务用例，不再需要等待同样的定时时长来获取最终的结果了。在上节课的最后的一则用例中，我们使用了 `jest.fn()`来作为 `asyncSleep`函数的入参。

```
import React from "react";
import { sleep, loopSleep, asyncSleep } from "../components/FakeTimer";

// 9 | FakeTimer：如何"快进"测试定时任务？
describe("examples for fakeTimers", () => {
  beforeAll(() => {
    jest.useFakeTimers();
  });

  // ... other content
  test("a test for a setTimeout with async function", async () => {
    const fn = jest.fn();
    asyncSleep(6000, fn);
    jest.runOnlyPendingTimers();
    await Promise.resolve();
    expect(fn).toBeCalled();
  });
});
```

在上面这则例子中，因为我们并不关心传入 asyncSleep 的回调函数逻辑，我们只希望它可以在指定时间执行回调，所以我们这里使用了 jest 提供的 mock 函数作为它的入参。

因为我们之前的场景并不那么复杂，在实际的业务场景中，我们一个文件中往往穿插着各种引用。其中包含一些测试环境没有的 API 或者全局变量，或者不在我们测试范围内的外部文件，这都是很常见的现象，这些情况我们都需要使用 mock 来模拟它们进行测试。

所以在实际的业务单测中，mock 是很重要的测试手段，这节课我们就来结合场景捋捋，怎么通过 mock 来模拟一些不需要关注的逻辑。

## 全局 mock

在业务场景中，我们可能会导入一些外部依赖进行测试，针对这些外部依赖，我们可能并不关心它的内部逻辑是怎么样的，我们只需要它可以返回预期的结果就好，对于这种场景，我们可以采取全局 mock 的方式，jest 为我们提供了一个 全局 mock 的 API。

```
jest.mock(path, moduleFactory)
```

它接受两个参数，path 和 moduleFactory，其中 path 是需要 mock 的文件路径，moduleFactory 是这个模块的工厂函数，类型与模块保持一致就行，可以进行更自定义的 mock。

这个 mock 的执行会被提升到 import 之前，也就是对于这个文件而言，mock 的内容会替代原有的模块，我们以需求中最常见的场景请求（axios）为例子，看下如何通过全局的方式来测试请求。

首先我们来安装一下 axios 的依赖：

```
npm install axios
```

然后我们加上下面的用例：

```
// ./src/__test__/mock.test.ts
import React from "react";
import axios from "axios";

jest.mock("axios");

// 10 | Mock: 怎么替代不那么重要的逻辑？
describe("examples for mock", () => {
  test("a test for global mock", async () => {
    const res = "this is a test for global mock";
    axios.get.mockResolvedValue(res);
    const data = await axios.get("/");
    expect(data).toBe("this is a test for global mock");
  });
});
```

在上面的例子中，我们用 mock 替代了 axios 的原生模块，其中 axios.get 会返回 jest 的 mockFn，mockResolvedValue 是 mockFn 提供的一个 API，通过它，我们可以模拟 mockFn 的异步返回值，除这个之外，我们还会经常用到以下几种:

| mockFn 提供的 API                        | 能力                        |
| ------------------------------------- | ------------------------- |
| `mockFn.mockReturnValue(value)`       | Mock 返回值，同步               |
| `mockFn.mockReturnValueOnce(value)`   | Mock 返回值，同步，只生效一次         |
| `mockFn.mockResolvedValue(value)`     | Mock resolve 返回值，异步       |
| `mockFn.mockResolvedValueOnce(value)` | Mock resolve 返回值，异步，只生效一次 |
| `mockFn.mockRejectedValue(value)`     | Mock reject 返回值，异步        |
| `mockFn.mockRejectedValueOnce(value)` | Mock reject 返回值，异步, 只生效一次 |

现在我们可以来执行一下这个用例。用例执行的过程中大家可能会遇到下面的报错。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40b91c80b73a4ae9a1c54033cae7e309~tplv-k3u1fbpfcp-zoom-1.image)

这是因为 axios1.x 现在只发出一个 ESM 模块，而不再是一个 CJS 模块，这会导致 Jest 出现解析错误，这是一个已知 [issue](https://github.com/axios/axios/issues/5026)，目前还没得到解决。针对这个问题有两个解决方案。

-   我们可以降级 axios 版本到 0.27.2，这是 0.x 中最新的版本。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/926efd234ce14b89b4083d8626b4f12e~tplv-k3u1fbpfcp-zoom-1.image)

-   仍然选择延用 1.x 的同学可以修改 jest.config.js 的配置，把 axios 移除测试编译范围。以我们当前项目为例子，因为我们使用的是 CRA，不通过 jest.config.js 配置，我们可以直接在 package.json 加上下面的配置，默认 node_modules jest 是不走 babel 编译的，现在我们把 axios 引入编译范围。

```
// ./package.json
{
  // ...
  "jest": {
    "transformIgnorePatterns": [
      "node_modules/(?!axios)"
    ]
  }
}
```

直接使用 jest.config.js 配置的同学可以直接在 jest.config.js 中加上同样的配置：

```
module.exports = {
  // ...
  transformIgnorePatterns: ["node_modules/(?!axios)"],
};
```

这两种方案都可以解决这个问题，大家可以根据自己对 axios 的需求自行选用：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/373a2004e1be4baab3c978564e6669c3~tplv-k3u1fbpfcp-zoom-1.image)

不过因为 mock 是在 import 之前覆写的缘故，类型并没有得到修改，所以我们会有下面的类型报错：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf8e66fcd4f2440b8ababa40bc4edf41~tplv-k3u1fbpfcp-zoom-1.image)

这个问题我们可以通过 jest-mock 提供的 mocked 函数来解决，它会帮我们补充全局 mock 对应的 mockFn 类型，首先我们来安装一下依赖：

```
npm install jest-mock
```

然后我们来调整一下用例：

```
// ./src/__test__/mock.test.ts
import React from "react";
import axios from "axios";
import { mocked } from "jest-mock";

jest.mock("axios");

// 10 | Mock: 怎么替代不那么重要的逻辑？
describe("examples for mock", () => {
  test("a test for global mock", async () => {
    const res = "this is a test for global mock";
    // axios.get.mockResolvedValue(res);
    mocked(axios.get).mockResolvedValue(res);
    const data = await axios.get("/");
    expect(data).toBe("this is a test for global mock");
  });
});
```

可以看到现在就没有类型的报错了~

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7c80fe1e20f44028c1e20037f021b71~tplv-k3u1fbpfcp-zoom-1.image)

## 单次 mock

上面我们提到针对 jest 的 mock API 会提升到 import 之前，也就是 import 的内容不再是原有的模块，除全局的 mock 外，我们还可以进行单次的 mock，jest 对于单次的 mock 提供了一个与 mock 对应的方法 —— doMock

```
jest.doMock(moduleName, factory, options)
```

doMock 的使用与 mock 略有不同，我们可以先来看下下面的例子：

```
// ./src/components/Mock/index.ts
const mock = {
  getMockData: () => {
    return "oldMockData";
  },
};

export default mock;
```

```
// ./src/__test__/mock.test.ts
import React from "react";
import axios from "axios";
import mock from "../components/Mock";

jest.mock("axios");

// 10 | Mock: 怎么替代不那么重要的逻辑？
describe("examples for mock", () => {
  // ...other

  test("a test for single mock", () => {
    jest.doMock("../components/Mock", () => ({
      __esModule: true,
      getMockData: () => {
        return "newMockData";
      },
    }));
    // expect(mock.getMockData()).toBe("newMockData");
    const mock = require("../components/Mock");
    expect(mock.getMockData()).toBe("newMockData");
  });
});
```

在这个例子中，有几个大家需要关注的点。

-   doMock 的第二个入参：也就是我们之前提到的 factory，我们可以通过这个参数来覆写原模块的属性和属性函数，让它们可以返回固定的逻辑或者值。
-   `__esModule: true`：因为我们定义的 mock 模块是通过 esModule 导出的，所以需要加上这个属性帮助 jest 进行 mock。
-   `require("../components/Mock")`: 如果我们直接在全局定义，然后调用可以吗？当然不可以~ 因为 doMock 只会对我们这个 test 生效，而不会提升到 import 之前去覆写原有模块，所以需要采用在用例内 require 的方式导入，直接 import 的模块还会是原来的文件，并不会生效 mock。

## mock 函数

除了 mock 和 doMock 外，jest 还提供了两个常用的 function 帮助我们进行函数的 mock：

```
jest.fn(implementation?)
jest.spyOn(object, methodName)
```

其中 `jest.fn` 用于 mock 一个空函数，它会默认返回 undefined，当然我们也可以传入两个类型来控制它的入参和回参内容，例如`jest.fn<string, string>()`就对应一个入参和回参都为 string 的 mock 函数了~

`jest.spyon`也可以创建一个和`jest.fn`类似的 mock 函数，不同的是它可以追踪目标函数的调用，使得它的入参和回参与需要 mock 的函数是自动匹配的，对于全局 mock 中的那个类型问题，我们就可以使用`jest.spyon`来解决。

```
// ./src/__test__/mock.test.ts
import React from "react";
import axios from "axios";

jest.mock("axios");

// 10 | Mock: 怎么替代不那么重要的逻辑？
describe("examples for mock", () => {
  test("a test for global mock", async () => {
    const res = "this is a test for global mock";
    // axios.get.mockResolvedValue(res);
    jest.spyOn(axios, "get").mockResolvedValue(res);
    const data = await axios.get("/");
    expect(data).toBe("this is a test for global mock");
  });
});
```

这样就不会有类型的问题了，不仅如此，单次 mock 中的例子我们也可以尝试使用它来覆盖：

```
import React from "react";
import axios from "axios";
import mock from "../components/Mock";

jest.mock("axios");

// 10 | Mock: 怎么替代不那么重要的逻辑？
describe("examples for mock", () => {
  // ...other

  test("other ways for single mock", () => {
    jest.spyOn(mock, "getMockData").mockReturnValue("newMockData");
    expect(mock.getMockData()).toBe("newMockData");
  });
});
```

其实，通过 `jest.spyOn` 足够覆盖我们需要的大部分场景，不过它一次只能 mock 一个对应的函数，如果需要对整体模块覆写，那我们还是需要 mock 和 doMock 来协助实现的。

## 小结

这节课我们学习了怎么使用 mock 来替代不需要关注的逻辑，在我们的业务场景中，经常会引用一些外部或者全局逻辑，这些逻辑和我们需要测试的组件内容其实不那么相关，我们可能只需要这些逻辑能有预期的输入输出，通过这种场景我们都会使用 mock来解决。

我们分别介绍了全局 mock，单次 mock 和 mock 函数三种场景，在全局 mock 中我们使用了 jest 的 `mock` API，这个会被提升到文件的 import 之前，使得整个文件引用的对应模块都会采用我们进行的 mock，不过这个可能会有类型的问题，我们可以通过 jest-mock 提供的 `mocked` 函数解决。

紧接着我们还学习了单次 mock，与全局 mock 不同的是，它只会对单次的用例生效，我们需要采用 require 的方式来动态导入我们需要 mock 的模块。

除了这些，我们还学习了 mock 函数中的 `fn` 和 `spyon` API，fn 需要自己定义入参和回参的类型，我们通常用它来定义一些简单、好定义类型的函数，而 spyon 自动追踪需要调用的函数类型进行 mock，通过它我们可以实现我们需要的大部分场景，不过它一次只能 mock 一个函数，针对一个模块，我们还是需要使用 `mock` 和 `doMock` 来完成。

到这里，其实相信大部分的场景同学们都可以完成了，但是在 React 中还有一个很特殊而且使用广泛的模块 —— hook，与常规函数不同，hook 只能在组件中使用，我们并不能像测试函数一样直接去验证它的输入输出，不过也是有解决的办法的。下节课我们就来学习怎么对我们业务中的 hook 覆盖单测。

## 11.RenderHook：怎么测试 React hook？

> 代码仓库：https://github.com/czm1290433700/test_demo

上一节课中，我们学习了怎么使用 Mock 来代替不那么重要的逻辑，分别了解了全局 mock 和 局部 mock 的方式，当我们使用`  mock  `方法的时候，这部分 mock 将被提升到 import 之前，使得整个模块的导入可以由 mock 内容替代。除了全局 mock 外，我们还可以使用 `doMock`、`spyon`等方法来在指定用例下进行模块的模拟。

到目前为止，我们已经学习了单元测试下的大部分场景，相信大家对于业务测试已经有一定的思路了。不过还有一种特殊的情况我们没有提及，那就是 hook 的测试。

Hook 是 React16 提出的新特性，通过它我们慢慢抛弃了 class 的写法，开始可以在不编写 class 的情况下使用 state 以及其他 React 特性，转向函数式编程。

不过与普通函数不同的，hook 只可以在 React 组件的顶部进行调用。在我们的测试用例中，并不能像普通函数那样去测试 hook，那么应该怎么去测试 React hook 呢？

## 从组件维度进行覆盖

最简单直接的方式就是从组件维度展开测试，通过直接测试调用 hook 组件的方式来完成这部分用例，我们来看下面的例子：

```
// ./src/components/RenderHook/useCount.ts
import { useCallback, useState } from "react";

// 11 | RenderHook：怎么测试React hook？
const useCount = () => {
  const [num, setNum] = useState(0);

  const increase = useCallback(() => {
    setNum(num + 1);
  }, []);

  return { num, increase };
};

export default useCount;
```

```
// ./src/components/RenderHook/index.tsx
import { FC } from "react";
import useCount from "./useCount";

interface IProps {}

export const RenderHook: FC<IProps> = ({}) => {
  const { num, increase } = useCount();

  return (
    <div>
      <span role="note">{num}</span>
      <button onClick={increase}>增加</button>
    </div>
  );
};
```

上面我们实现了一个 hook useCount 和组件 RenderHook，在组件 RenderHook 中使用了 useCount 的 hook 来实现数字点击递增的效果，在这个例子中，我们就可以通过测试 RenderHook 组件的能力来推断 useCount 是否符合预期，我们来看下面的用例。

```
import React from "react";
import { render, screen} from "@testing-library/react";
import useCount from "../components/RenderHook/useCount";
import { RenderHook } from "../components/RenderHook";
import userEvent from "@testing-library/user-event";

// 11 | RenderHook：怎么测试React hook？
describe("examples for render hook", () => {
  test("a test for component with useCount", () => {
    render(<RenderHook />);
    const note = screen.getByRole("note");
    expect(note).toHaveTextContent("0");
    userEvent.click(screen.getByRole("button"));
    expect(note).toHaveTextContent("1");
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf696e34475849999b9ddc65171ef788~tplv-k3u1fbpfcp-zoom-1.image)

## RenderHook

但是上面的这个方法只能覆盖这个 hook 本身就是为组件定义的场景，我们不可避免会定义一些公共的 hook ，对于这些 hook 可能会被多个组件调用，我们不可能深入组件内部去测试。同学们可能会说，那我们为这些公共 hook 来定义一个组件专门测试不就好了吗？

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee3cf3300cfb43cf979fc029d7578891~tplv-k3u1fbpfcp-zoom-1.image)

的确是可行的，但是为了测试 hook ，我们不得不创建大量与业务代码无关的测试组件，这个过程在业务中实现显得不那么优雅。为了解决这个问题，testing-library 提供了一个 renderHook 的库来帮我们实现，在它的内部会替我们完成上面我们提到的想法。

如果项目是 React 18 & testing - library 13.1 以上版本的同学，不需要安装任何额外的依赖，可以直接在 `@testing-library/react`中直接调用，依赖本身已经做了相关的集成处理。

如果不满足上述的情况，我们需要自己安装一下依赖，在依赖中引用：

```
npm i @testing-library/react-hooks
```

现在我们来通过 renderHook 再覆盖一下上面 hook 的用例：

```
import React from "react";
import { render, screen, renderHook } from "@testing-library/react";
import useCount from "../components/RenderHook/useCount";
import { RenderHook } from "../components/RenderHook";
import { act } from "react-dom/test-utils";
import userEvent from "@testing-library/user-event";

// 11 | RenderHook：怎么测试React hook？
describe("examples for render hook", () => {
  // ... other
  test("a test for useCount", () => {
    const { result } = renderHook(() => useCount());
    act(() => {
      result.current.increase();
    });
    expect(result.current.num).toBe(1);
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88d09645f34442a2901bc10729583b44~tplv-k3u1fbpfcp-zoom-1.image)

可以看到优雅了很多，我们不再需要基于组件维度去测试我们的用例，只需要把它包裹在 renderHook中，对应的结果会被存放在 result 字段中，我们可以直接解构出来断言。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a82baa0ef21b4bbd8826307e776f2b7a~tplv-k3u1fbpfcp-zoom-1.image)

不过值得一提的是，因为 renderHook 并没有帮我们触发 rerender，所以对于会修改到 state 的方法，我们需要手动将它们用 act 包裹起来触发 rerender。

## 关于 hook 测试的建议

虽然 renderHook 能帮助我们很方便地测试 hook，但是不得不说的是，我仍然建议大家通过组件维度来测试 hook ，而不是滥用 renderHook。

在之前的课程中，我们有反复提到，我们应该尽可能让测试更为强健，也就是从用户视角展开测试，而不是代码结构层面来开展我们的测试。对于用户而言，它并不关心你这里使用的是 hook 还是普通函数，只要能得到它预期的结果就可以，至于内部实现其实并不重要。也就是说，如果对于组件内部的 hook，直接对 hook 展开测试，并不如从组件维度展开测试来的强健。

当然，如果这个 hook 是作为一个公共的 hook，被多个组件来使用，这种场景更适合使用 renderHook 来实现，这个是不矛盾的，因为作为公共组件的 hook，它的直接用户是组件（component），所以我们不应该深入组件内部去测，而是应该直接通过 renderHook 来验证 hook 的功能正常。

## 小结

这节课我们学习了怎么测试 React hook，hook 在 React 中是一个特殊的函数，它只能在 React 组件顶部进行调用，所以我们不能像普通函数一样，在用例中直接调用它来测试。

对于它的测试，我们有两种方法，一种是基于组件维度来进行覆盖，通过测试调用 hook 的组件功能，进而验证 hook 的功能符合预期，另一种则是使用 renderHook 来进行 hook 验证，通过传入 hook 的回调，我们可以直接获取对应 hook 的返回，从而来进行我们的断言。

虽然 renderHook 的测试很方便，但是并不建议大家滥用，因为我们需要从用户视角来展开测试，从而保证用例尽可能强健，当然对于公共逻辑的 hook，因为用户是组件（component) 本身，所以我们还是适合通过 renderHook 的方式来完成用例。

到这里单元测试的部分我们就已经学完了，下节课我们会来学习一种特殊的测试方式，快照测试。通过它，我们可以快速高效地保证组件 UI 的完整。

## 12.快照测试：怎么保障组件 UI 的完整？

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了怎么测试一个 hook 方法，因为 hook 只能在 React 组件顶部调用的特性，所以我们不能像测试普通函数一样测试它，还学习了从组件维度和 renderHook 两种测试的方案和它们适用的场景，我们单元测试的内容就已经学完了，在这节课中，我们会来学习一种不同的测试方案 ---- 快照测试。

在开始这节课的学习前，我想请同学们思考一个问题，对于一个业务组件，我们可以用什么手段来保证组件 UI 的完整呢？有的同学可能就会说了，我们可以用断言呀，查询到对应的元素来判定它不就好了吗 ~ 

这个的确是一个办法，但是断言只能匹配到我们查询到的区域是正常的，一个组件中肯定有一些 DOM 是和功能本身关系不大，但又必须存在的，如果都覆盖断言，一个用例可能就会有几十上百行，那对工程师的心理负担和业务压力增加就太大了（可能真的就要提桶跑路了=。=）

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2a7cf44d55142ea91db398bd597df8e~tplv-k3u1fbpfcp-zoom-1.image)

这边有一个解决办法是使用快照测试，快照测试和它的字面意思一样，通过“快速（简单）拍出的照片”来测试，它是将我们需要判定的元素的内容存储下来，在下一次匹配时，会判断两次的结果能否匹配，从而达到从整体维度保证组件功能完成的能力。

## 组件的快照测试

React Testing library 中提供了快照测试的能力，我们只需要使用它提供给我们的 `toMatchSnapshot` 断言就好，我们可以直接来看看下面的例子：

```
// ./src/components/DomSnap/index.tsx
import { FC } from "react";

interface IProps {}

// 12 | 快照测试：怎么保障组件 UI 的完整？
export const DomSnap: FC<IProps> = ({}) => {
  return (
    <form aria-label="form">
      <input
        type="text"
        name="username"
        disabled
        aria-disabled
        defaultValue="zhenmin"
        aria-label="form_username"
      />
      <input
        type="number"
        name="age"
        defaultValue={23}
        required
        aria-label="form_age"
      />
      <input
        type="radio"
        name="sex"
        value="man"
        defaultChecked
        aria-checked
        aria-label="form_sex"
      />
      <input type="radio" name="sex" value="woman" aria-label="form_sex" />
    </form>
  );
};
```

```
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomSnap } from "../components/DomSnap";

// 12 | 快照测试：怎么保障组件 UI 的完整？
describe("examples for snap", () => {
  test("a test for component snap", () => {
    const { baseElement } = render(<DomSnap />);
    expect(baseElement).toMatchSnapshot();
  });

  test("a test for part component snap", () => {
    render(<DomSnap />);
    expect(
      screen.getByRole("textbox", { name: "form_username" })
    ).toMatchSnapshot();
  });
});
```

在上面的例子中，定义了一个 form，我们需要对它进行快照测试，在用例当中，我示范了全局和部分区域的快照筛选，我们来执行这个用例看看。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dd45f03b9ac495d828dea8128a08d15~tplv-k3u1fbpfcp-zoom-1.image)

除了用例执行成功的说明外，可以发现在 __test__ 目录下生成了一个 __snapshots__ ，这个目录用来存放我们的快照文件：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b48aef2d95400cadb913ac9b787798~tplv-k3u1fbpfcp-zoom-1.image)

我们来看看新生成的快照里面有什么：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1870137521f54ae195cbe8b81eda4413~tplv-k3u1fbpfcp-zoom-1.image)

可以看到针对每一个用例中使用到 toMatchSnapshot 断言的地方，它都会生成一个对应查询区域的快照，后面我们在每次执行这个用例的时候，都会去比对这次的快照能否和上次的匹配起来，我们不妨来改点 dom 试试看。

```
// ./src/components/DomSnap/index.tsx
import { FC } from "react";

interface IProps {}

// 12 | 快照测试：怎么保障组件 UI 的完整？
export const DomSnap: FC<IProps> = ({}) => {
  return (
    <form aria-label="form">
      <input
        type="text"
        name="username"
        disabled
        aria-disabled
        defaultValue="zhenmin"
        aria-label="form_username"
      />
      <input
        type="number"
        name="age"
        // defaultValue={23}
        defaultValue={24}
        required
        aria-label="form_age"
      />
      <input
        type="radio"
        name="sex"
        value="man"
        defaultChecked
        aria-checked
        aria-label="form_sex"
      />
      <input type="radio" name="sex" value="woman" aria-label="form_sex" />
    </form>
  );
};
```

因为祯民马上 24 了，所以我们这边可以把 age 表单的默认值换成 24，然后我们重新跑一下用例看看会不会匹配出来对应的调整，可以看到和我们预期的一样，对应的区域发生了调整。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf9d7feb3a13466eac1a67964f445bcd~tplv-k3u1fbpfcp-zoom-1.image)

## 序列字符的快照测试

除组件以外呢，快照测试其实也是可以用在函数返回值等非 DOM 的序列字符场景下的，我们来看看下面的例子。

```
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomSnap } from "../components/DomSnap";

// 12 | 快照测试：怎么保障组件 UI 的完整？
describe("examples for snap", () => {
  // ...
  test("a test for string snap", () => {
    expect("a test for string snap").toMatchSnapshot();
  });
});
```

上面的例子里，我们增加一个字符串的快照，这个也是可以用快照测试来验证的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14d4b78619354578865449c2951f4a76~tplv-k3u1fbpfcp-zoom-1.image)

## 快照测试的更新

大家可能会有一个疑问，如果我这次需求迭代完，这个组件的确 DOM 结构就是会变，那我们应该怎么更新之前的快照呢？对于用例中的快照更新有两种方式，第一种我们可以直接在控制台中输入 `u` 来更新快照：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee5810add4f04b168c29bc108a88c40e~tplv-k3u1fbpfcp-zoom-1.image)

但是这样很容易误操作，所以我更建议大家用第二种方式，我们可以额外在 package.json 中加入这样的一条命令，对于不是 CRA 项目的同学，也只需要把前面的`react-scripts`换成`jest`即可：

```
"updateSnap": "react-scripts test --updateSnapshot"
```

包含 updateSnapshot 参数的测试环境会自动更新每一个 diff 不同的快照。

## Where & how to use 快照测试？

虽然快照测试相比断言匹配更加短平快，简单暴力，但并不意味着它可以适用所有的场景，针对每个用例都输出快照是没有意义的。

那么我们应该在什么场景下去使用快照测试呢？其实我们可以把快照测试输出的内容理解为 `screen.debug()`，比对的目的只是需要保证前后两次 debug 的输出是相同的，通过这个特点，我们就可以推断出快照测试**更适合使用在不轻易改变，甚至不会去改变的公共逻辑中**。

快照测试的使用是比较简单的，只需要加上一个断言就可以自动生成，但是对于快照测试的使用，我还是想提几个建议：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c532629a584f4225a1f3d9017b8c9860~tplv-k3u1fbpfcp-zoom-1.image)

-   避免大快照：在我们的业务页面中，组件之间多层嵌套是常有的事情，我们应该避免对一个页面，或者一个大组件直接整体进行快照，因为这样的快照可能会导致后期迭代中需要频繁修改快照。
-   避免小快照：有同学看到这个，就会觉得祯民这不是在自己打自己脸？上面才刚说了要避免大快照，现在又说避免小快照，那还用不用了~其实是这样的，这边的"小”是指粒度过小，比如它可能就一行，像我们上面举例中的`  expect("a test for string snap").toMatchSnapshot() `其实就是一个 bad case，这种粒度我们完全可以使用断言来获得更精准的测试，也更方便。其实快照的粒度怎么选取，还是决定于你认为组件中最大粒度的不会去改变的公共逻辑是到哪里，我们应该尽可能保证粒度大，且快照的内容并不会被修改。
-   避免频繁更新快照：虽然我们有学习怎么去更新快照，但我是不希望大家去频繁更新快照的，使用快照的目的应该就是为了保证这个稳定的公共逻辑能够不变，如果每个开发同学发现快照通过不了就更新，那么快照的意义也就丢失了，就不需要使用快照测试。

## 小结

这节课我们学习怎么使用快照测试来保障组件 UI 的完整，快照测试相比断言成本更小，可以快速匹配这次和历史版本的区别，我们只需要对需要快照的内容使用 `toMatchSnapshot`就可以生成对应的快照了。快照测试本身并不难，反而是如何妥善使用，不滥用快照测试倒显得更为重要。

我们应该尽可能使用快照测试在不容易频繁迭代更改的场景，并且在粒度上，我们要尽可能保证从组件维度上粒度尽可能大，又不容易去迭代更改的程度，这样才能避免对一两行代码快照，或者是快照过大需要频繁更新快照的问题，这两种情况都会丢失快照测试的初衷。

到现在为止，我们需要学习的单元测试内容已经完成了，大家可能会很好奇，Jest 是怎么实现这么一个庞大的单元测试系统的呢？所以下一节课，我们就来深入原理讲一讲，从我们运行命令到用例执行完成究竟发生了什么事情。

## 13.深入原理：Jest 是怎么实现整个单元测试系统的？

> 代码仓库：<https://github.com/czm1290433700/test_demo>

上节课我们学习了怎么通过快照测试来保证 UI 的完整，相比查询元素进行断言，快照测试更加简洁粗暴，可以帮助我们快速检测整个模块是否和上次的快照结果匹配。

在快照的设计中，我们讲究不”大“不“小”，一方面不生成大快照，使得组件频繁变动，带动快照也一起更新；另一方面，不生成小快照，因为过小的快照完全可以通过一两句断言解决，就丧失了快照的意义，尽可能在保证组件不变的前提下，将快照的粒度放大才是更加合适的做法。

到这里相信大家对单元测试如何实现已经了然于心了，不过现在 Jest 做的事情还是比较黑盒的，我们只知道它帮我们开展测试，但是我们并不知道它在这个过程中发生了什么，我们为什么需要配置这个配置那个，所以这一节课，我们就专门来学习一下这其中的原理，一起来看看 Jest 是怎么实现整个单元测试系统的。

## 小彩蛋

在开始这节课的学习前，先同步一个小问题，今天我在执行用例的时候，发现有下面的报错：

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23d2811c965247f8af1049394a0abf2c~tplv-k3u1fbpfcp-zoom-1.image)

这个是因为不能编译依赖中的 css 导致的，解决方法也很简单，只需要加一个 css 的 mock 去替代就好，原先我一直以为 react-scripts 有帮我们完成这一步，遇到这个问题的同学可以参照下面的步骤修复：

```
// ./package.json
"jest": {
    "transformIgnorePatterns": [
      "node_modules/(?!axios)"
    ],
    "moduleNameMapper": {
      "\.(css|scss)$": "<rootDir>/styleMock.js"
    }
  }
```

加上 moduleNameMapper ，如果有更多的样式类型，可以自行补充到前面的正则中，styleMock.js 中的内容就一行，将导入改成空即可，如下：

```
module.exports = {};
```

然后我们再执行所有的用例试试，默认的 test 只会执行最近 commit 相关的用例，我们可以加一则命令用于执行所有的用例，现在可以看到所有的用例都可以通过了。

```
"test:all": "react-scripts test --watchAll",
```

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ab99e8017554b1ab6da0e9498548188~tplv-k3u1fbpfcp-zoom-1.image)

## Jest 系统实现

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20d693f12ac94c92a035a60ccf5abc99~tplv-k3u1fbpfcp-zoom-1.image)

为了方便大家理解，我画了上面的架构图。一起来看看从配置到用例的执行这个过程究竟发生了什么？首先，所有事情的起点是 jest, 准确的说是 jest-cli ，这是我们单测的开始，初始化所有的配置。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f05a96c54735466581d39f3b111de899~tplv-k3u1fbpfcp-zoom-1.image)

紧接着我们来到第二步，也就是我们之前常常配置到的 jest-config，在这里我们可以配置一些全局或者针对目前项目的配置，在获取到这部分配置后，进入到第三步。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/224cd60c9bf4465682d3325d2a16dde4~tplv-k3u1fbpfcp-zoom-1.image)

在第三步中，我们直接交互的部分是 jest-haste-map，这部分是一个虚拟的文件系统，它会在我们第一次执行用例的时候，去遍历一遍项目的文件目录，形成一个 Map ，其中存储着我们文件之间的依赖和上下级关系，在后续的热更新操作中，它将会直接获取之前的 Map 缓存而不再遍历文件系统。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0dc180624a464821b1a6885fd1b42247~tplv-k3u1fbpfcp-zoom-1.image)

再往下就是比较重要的一步了，jest-worker，它的底层基于 watchman 来实现。有一个读者问我 jest 每次热更新会执行全部用例吗？答案当然是不会的，jest-worker 会监听变化的文件，来保证每次热更新重新执行的是最近变更部分的用例，而不是全部。

我们想象一下，如果咱们的用例很多，没有这样一步的话，每次 change 都要等待所有的用例执行完，那真的就是一个很痛苦的事情了。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/053ef856121a47f0845ccd0245b18f38~tplv-k3u1fbpfcp-zoom-1.image)

在上一步完成后，我们已经拿到了我们的配置和文件系统。接下来会通过 searchsource 的集成类来找寻我们需要运行的用例。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbc8340d172a40d188f8d40601e22d44~tplv-k3u1fbpfcp-zoom-1.image)

获取到用例后，我们会经过 test sequencer，这是一个测试排序器，在这一步中我们会来排序用例执行的优先级，优先级会按照过去失败过的用例 > 执行实现长的用例 > 文件 size 大的用例这样一个顺序来执行，来保证用户关注的内容可以被优先做完。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0aeb0a5f9294f77a1cb4f822f70c988~tplv-k3u1fbpfcp-zoom-1.image)

到下一步仍然是调度，我们会经过 test schedule，不过与 test sequencer 不同，这一次不再是分优先级了，而是安排进程，会根据现在 CPU 的情况来把用例分配到合理的线程，也许会单线程，也许会安排多个线程来分开执行。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca60a8414bcb4283b7336c73e5ee2637~tplv-k3u1fbpfcp-zoom-1.image)

调度的部分完成以后，就要开始着手执行我们的用例了，其中比较核心的两个部分是 jest-runner 和 jest-jasmine，其中 jest-runner 负责直接执行，而 jest-jasmine 负责根据架构来拆分我们的用例，这里的架构指的就是我们的 describe 和 test。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ff8af3e8e4a4926847accb3823ea595~tplv-k3u1fbpfcp-zoom-1.image)

在执行的过程中，我们可以分为两个部分，一个是运行环境，另一个就是转译。对于运行环境, 我们可以分为 jsdom 和 node，默认我们是选用 node 的，不过如果我们测试的是 web 应用程序，那就应该选用 jsdom，两者是不同的运行引擎。

对于转译，我们知道 nodejs 是 commonjs 的 "拥护者“，在直接的 node 环境里是不能识别 esm 的写法的，所以我们需要使用一些转译工具，比如 babel，来帮助我们转译成 commonjs，为我们的测试程序保驾护航。

到这里，咱们的 jest 用例就执行完成了，我们再回顾一遍。

首先是前置的工作，我们会拿到 jest 的配置并且会根据文件系统生成一组虚拟的文件映射，来保证后续热更新的效率；接下来会找寻我们文件中需要执行的用例，并且根据优先级和 CPU 的使用情况，将它们分给不同的线程按顺序执行；在执行的过程中，因为环境的原因，需要确定我们的执行引擎和文件转译，然后就会按照我们之前拆分的 decribe 和 test 分批执行我们的用例了。

## 额外的启发

在了解完原理后，其中我们可以得到一点启发，除了 Jest 黑盒的部分，像转译的部分其实是由我们来控制的，在性能上，转译还有优化的空间，除 babel 和 ts-jest 外，业内还提供有 esbuild-jest 和 @swc/jest，以 esbuild-jest 为例，它是基于 esbuild 来实现的 jest 转译工具。

Esbuild 有些同学可能已经比较熟悉了，它是基于 Go 开发的打包工具，不同于 JavaScript，Go 可以直接被编译为本地代码，所以性能上有极大的提升，下面我们以 esbuild-jest 为例介绍一下怎么优化转译，首先来安装一下依赖。

```
npm i esbuild-jest --save-dev
```

然后我们补充一下对应的转译配置，非 CRA 的同学可以把对应的配置加到 jest.config.js 中。

```
// ./package.json
"transform": {
    "^.+\.(t|j)sx?$": "esbuild-jest"
 },
```

我们来执行一下用例，对比之前的 13s 执行时间，我们优化了整整 30%，现在用例数尚且不多，如果更多的用例，这个会更加明显！不过缺陷就是相比 babel 和 ts-jest ，esbuild-jest 和 @swc/jest 的社区相对还比较年轻，所以遇到一些特殊的问题（比如一些老的不合规的依赖，并没有 esm 的写法）可以不能立刻找到解决的办法，不过这并不妨碍我们在新项目中体验~如果遇到不能兼容的问题，我们再换回来就好。

![img](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b44336b29d44353af610fd31656a2b8~tplv-k3u1fbpfcp-zoom-1.image)

## 小结

这一节我们学习了 Jest 系统是如何实现的，简单来说，首先我们会经过一个前置工作的阶段，拿到所有的配置，并且构造出一个虚拟的文件系统用于热更新的 diff，接下来我们会找寻所有需要执行的用例，根据优先级和 CPU 的情况分给不同线程按顺序执行，执行的过程中，我们会经过转译和环境引擎编译的步骤，最后按照我们 describe 的架构和分组完成指定的用例。

除此之外，我们还介绍了一种让单元测试跑得更快的方式，因为 Jest 运行的过程中，虽然大部分是黑盒不可控的，但是其中转译的部分我们还有可以优化的空间，如果我们不使用 babel 而是换用 esbuild 等方案，那么在性能上会有不错的提升。虽然社区还比较年轻，但是尝试一下还是可以的~大不了兼容不了咱再换回去就是haha……

到这里单元测试的部分就已经全部介绍完了，不过在我们的需求中，仍然有一些单元测试难以覆盖的场景，比如滚动、跳转等比较复杂的场景，这些是不好模拟的，这时候就需要借助端对端测试（E2E)的方案来协助我们完成了, 下节课我们就来详细介绍一下什么是端对端测试，我们应该怎么展开对应的测试。

## 14.E2E：怎么覆盖滚动等复杂交互场景的测试？

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了 Jest 是怎么实现整个测试系统的，相信大家对“运行命令到用例执行”这个过程都有了初步的认知。现在我们已经学完了单元测试的全部内容，已经可以对我们的组件的大部分功能进行覆盖了。

不过针对一些复杂的场景，比如滚动，我们没办法通过单元测试的方式来验证，因为它并不支持滚动事件的模拟。针对这种场景，我们可以通过 E2E（端对端）测试的方式来覆盖。

## 什么是端对端测试？

我们之前的测试其实都需要在项目中来编写，针对组件的单一原型来书写用例，这是为了稳固内部系统的质量和功能而展开的测试，也就是单元测试。但是除单元测试外，还有一种自动化测试方案，这种自动化测试方案通常由质量保障团队编写，也就是QA，不需要基于项目展开，从用户角度进行测试。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8024a679c1c044138fee2a69b915395e~tplv-k3u1fbpfcp-zoom-1.image)

端对端测试是可以覆盖滚动和跳转场景的，虽然通常由测试人员编写，但是这并不代表我们不能用~

对于 JS 技术栈的前端开发来说，通常会使用 cypress 作为端对端测试工具，它更加贴近我们的代码习惯，而且支持 npm 包安装，我们就可以把端对端代码维护到我们的项目中进行统一的覆盖率统计。

除 cypress 外，还需要有个服务来单独渲染我们的组件，便于我们进行端对端测试，可以选用 storybook 来帮助快速渲染我们的组件，这样我们就可以通过 cypress 来测试了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9529158da9074c63a2bc93a4856b0181~tplv-k3u1fbpfcp-zoom-1.image)

思路确定了，下面我们来就例子看看应该怎么覆盖滚动场景的用例。

## 滚动场景的覆盖

我们首先来实现一个有滚动场景的组件，比如下面的例子：

```
// ./src/components/ScrollList/index.tsx
import { FC, useMemo, useState } from "react";
import "./styles.css";

interface IProps {
  data: string[];
  height: string | number;
  pageSize?: number;
}

/**
 * 滚动 list, 拉到底部刷新新的一页
 * @param data
 * @param height
 * @returns
 */
export const ScrollList: FC<IProps> = ({ data, height, pageSize = 10 }) => {
  const [page, setPage] = useState(1);

  const currentData = useMemo(
    () => data.slice(0, pageSize * page),
    [pageSize, page]
  );

  return (
    <div
      className="scrollList"
      style={{ height }}
      onScroll={(e) => {
        const { scrollTop, clientHeight, scrollHeight } = e.currentTarget;
        if (
          scrollTop + clientHeight >= scrollHeight &&
          currentData.length < data.length
        ) {
          alert(`当前page为${page}`);
          setPage(page + 1);
        }
      }}
    >
      {currentData.map((item, index) => {
        return (
          <div className="item" key={index}>
            {item}
          </div>
        );
      })}
    </div>
  );
};
```

我们实现了一个组件，这个组件的功能是可以对一个列表进行滚动分页，每次滚到底部，就会渲染出下一页的内容，下面我们就这个组件来展开我们的端对端测试。

首先我们安装一下 cypress：

```
npm install cypress --save-dev
```

安装完成后，会自动打开一个窗口，后续我们打开可以执行 `npm run cypress`：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75d19af8be9d4444a0ab8906760885c5~tplv-k3u1fbpfcp-zoom-1.image)

选择 E2E Testing，然后选择谷歌浏览器预览，最后会得到这样的一个页面：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d32d5570ffda464e831a47de329edded~tplv-k3u1fbpfcp-zoom-1.image)

做完这一步，我们应该可以看到项目中发生了一些变更，可以暂时把 cypress 放一放，我们来继续初始化一下 storybook：

```
npx storybook init
```

执行下面的命令后，会进行 storybook 的初始化，启动的默认端口号是 6006， 我们可以看到会打开这样的一个页面：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e226951531954aa6ab5a4fad06822ba4~tplv-k3u1fbpfcp-zoom-1.image)

因为 cypress 测试，我们也希望测试 storybook 的页面，所以咱们也可以修改 cypress 的 baseurl 为 6006 端口，这样我们在写访问链接的时候就可以省略域名的部分了：

```
// ./cypress.config.ts
import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    baseUrl: "http://localhost:6006/",
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    defaultCommandTimeout: 10000,
  },
});
```

这时候咱们来稍微看一看初始化了哪些内容：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6473057bf80f45e88b9b033d0263d0ec~tplv-k3u1fbpfcp-zoom-1.image)

其中针对 cypress ，它帮我们初始化了一个 cypress 的目录，以及 cypress 的配置文件，其中 cypress 目录中的 e2e 文件夹存放着我们的端对端测试用例，后续如果有新增，保持 xxx.cy.ts 的格式，就可以识别到是测试文件了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488d781d75e44b53a64cc71427de6a4e~tplv-k3u1fbpfcp-zoom-1.image)

这个我不讲解大家应该都可以看懂，因为和单元测试的写法真的真的很像，只是提供了一些额外的 API 而已。Btw，如果有同学打开 e2e 发现其中的 API 会报错也不要着急，因为 tsconfig.json 并没有包括到根目录，我们可以加上：

```
// ./tsconfig.json
{
  "compilerOptions": {
    // ... other
    "types": ["cypress"]
  },
  "include": ["src", "cypress"]
}
```

大概介绍完了 cypress 的目录结构，我们再来看看 storybook。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/959dec3c5a90405bbd79d75d9b9c64dc~tplv-k3u1fbpfcp-zoom-1.image)

这里它帮我们创建了一些例子，我们以 button.stories.tsx 为例看看写了点啥：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b9804aa147147a6ac1f02a8dfcdc9a7~tplv-k3u1fbpfcp-zoom-1.image)

首先是默认暴露的一些属性，这个决定了它的文档根目录，然后底下是调用这个组件以及不同场景下组件的入参，每个都会形成一个子目录，可以用于调试，我们可以看看对应 button 的效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aad6620686264b59931f5339fd00014d~tplv-k3u1fbpfcp-zoom-1.image)

如果大家后续想写一些架构的项目，用 storybook 来书写架构文档真的是很不错的选择，我们来为滚动组件照猫画虎写一个：

```
// ./src/stories/ScrollList.stories.tsx
import React from "react";
import { ComponentStory, ComponentMeta } from "@storybook/react";

import { ScrollList } from "../components/ScrollList";

export default {
  title: "Example/ScrollList",
  component: ScrollList,
  argTypes: {
    backgroundColor: { control: "color" },
  },
} as ComponentMeta<typeof ScrollList>;

const Template: ComponentStory<typeof ScrollList> = (args) => (
  <ScrollList {...args} />
);

export const List = Template.bind({});
List.args = {
  data: [
    "test1",
    "test2",
    "test3",
    "test4",
    "test5",
    "test6",
    "test7",
    "test8",
    "test9",
    "test10",
  ],
  height: 80,
  pageSize: 3,
};
```

咱们来看看效果， 真的很棒！

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/482ca6818bc8426c9caff792ee9d6718~tplv-k3u1fbpfcp-zoom-1.image)

有可访问的页面了，就可以开始写咱们的端对端测试了~

```
// ./cypress/e2e/scrollList.cy.ts
describe("tests for ScrollList", () => {
  it("should render ", () => {
    cy.visit("/iframe.html?id=example-scrolllist--list");
    cy.get(".item").should("have.length", 3);
    cy.get(".scrollList").scrollTo("bottom");
    cy.get(".item").should("have.length", 6);
    cy.get(".scrollList").scrollTo("bottom");
    cy.get(".item").should("have.length", 9);
    cy.get(".scrollList").scrollTo("bottom");
    cy.get(".item").should("have.length", 10);
  });
});

export {};
```

上面的代码相信大家都可以看得懂，查询 - 断言，端对端和单元测试一样，采用类似的链式写法，在这则用例中，我们获取了一开始列表长度，断言初始化为 3， 然后把它滚动到底部，我们希望它可以更新长度为 6，如此循环，最后长度是 10，因为已经没有更多的数据可以用于更新了。

  


不过比较细心的同学可能会发现，你写的访问链接好像和咱们 API 的对不上呀 ~

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38f7f8a9a0f14492a93c134bae8151da~tplv-k3u1fbpfcp-zoom-1.image)

我们直接访问的链接是这个，不过呢 cypress 的测试是不会深入到 iframe 中的，而对于组件右边的部分是通过 iframe 嵌入进来的，我们写的链接就是这个 iframe 的链接，`/iframe.html?id=${你的组件id}`，所以我们直接测试 iframe 就好，同学们也可以直接打开这个链接看看，这个页面中只包含我们的组件。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0af1ab4b0e6144eda4018e916bbddc31~tplv-k3u1fbpfcp-zoom-1.image)

好了，现在来尝试看看跑一下我们的端对端用例，怎么跑呢，进我们刚才打开的 cypress GUI 页面就可以了。

  


很棒，可以看到我们的用例全部都通过啦~我们运行测试的时候，右侧的窗口会同步地模拟我们用例中描述的过程，并与断言进行匹配。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4f91194327948dfa6d84e1478261ca5~tplv-k3u1fbpfcp-zoom-1.image)

不过我们肯定不希望每次都需要我们自己点一遍用例，通过命令自动化执行肯定是需要的，所以我们可以加上下面的这条命令，通过执行这条命令，它就会自动帮我们完成所有的用例了~

```
 // package.json
 "cypress:run": "cypress run",
```

当然 E2E 的功能远不只是协助我们的单元测试覆盖滚动场景这么点，它甚至可以覆盖我们整个项目中的细枝末节，感兴趣的同学也可以自行了解一下，写法上有单元测试的基础，掌握也会很快~只是一些 API 上的不同。

## 小结

这节课我们学习了怎么通过 cypress 和 storybook 覆盖滚动等复杂交互场景，通过端对端测试，我们可以覆盖很多单元测试难以企及的场景，虽然开发并不经常写这个，但是在整个项目质量的维稳上，端对端测试的确起到了不小的作用~

现在我们已经学了不少测试知识了，那么我们应该怎么衡量测试用例覆盖得是否完整呢？那就需要测试覆盖率登场了，下节课我们就来学习怎么对测试代码覆盖自动化测试。

## 15.Coverage：自动化测试覆盖率的统计

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了怎么覆盖滚动等复杂场景，因为单元测试的能力限制，所以我们没办法通过单元测试来覆盖，端对端测试可以帮我们覆盖这部分测试内容。端对端测试通常由质量保障团队进行整个项目维度的用户视角测试，相比单元测试，更容易还原用户的操作行为，而且不需要知道内部代码的实现即可编写。

现在我们已经学习了很多自动化测试的知识，我们可以快速为一个组件来覆盖自动化测试的用例，但是怎么衡量我们的用例写的好不好，覆盖是否完整呢？这个就需要用到覆盖率的统计了。

## 覆盖率指标

什么是测试覆盖率？简单来说，它是我们测试用例覆盖文件的质量指标，可以验证到代码中的每一行是否都被测试用例经过，通常它包含下面的四个指标 ( 不同版本之间名字可能会略微不同，比如复数、缩写等 ）：

| 指标名称      | 指标内容                  |
| --------- | --------------------- |
| statement | 语句覆盖率，是不是每个语句都执行了     |
| branch    | 分支覆盖率，是不是每个 if 判断都执行了 |
| function  | 函数覆盖率，是不是每个函数都执行了     |
| line      | 行覆盖率，是不是每行都执行了        |

## Jest 单元测试覆盖率

现在我们来尝试覆盖 Jest 的那部分单元测试，因为我们是 CRA 项目，所以我们在 package.json 中加入下面的覆盖率相关的配置，如果非 CRA 项目，可以在 jest.config.js 中加入。

```
// ./package.json
"scripts": {
    "test": "react-scripts test",
    "test:all": "react-scripts test --watchAll",
    "test:updateSnap": "react-scripts test --updateSnapshot",
    "test:coverage": "react-scripts test --coverage",
 },
 // other
 "jest": {
    "transform": {
      "^.+\.(t|j)sx?$": "babel-jest"
    },
    "transformIgnorePatterns": [
      "node_modules/(?!axios)"
    ],
    "moduleNameMapper": {
      "\.(css|scss)$": "<rootDir>/styleMock.js"
    },
    // 只统计公共 components 下的非类型文件覆盖率
    "collectCoverageFrom": [
      "<rootDir>/src/components/**/*.{js,jsx,tsx,(!d).ts}"
    ],
    // 覆盖率卡点
    "coverageThreshold": {
      "global": {
        "branches": 90,
        "functions": 90,
        "lines": 90,
        "statements": 90
      }
    }
 },
```

下面我们来解释一下上面的配置，其中 collectCoverageForm 用于配置我们希望覆盖的文件，其中是一个 glob 表达式的数组，我们这里要求覆盖公共 components 下的所有 js/ts(x) 文件，并且从当中筛掉了纯类型文件 (.d.ts) ，coverageThreshold 配置是覆盖率卡点，这里我们要求覆盖率在 90% 以上，不然就会报错。

除了上面的两个配置，还有一个常用的配置，coverageDirectory 这个可以配置覆盖率生成的目录，因为这是 CRA 项目， package.json 中并不支持这个属性，如果我们要加的话，只能执行 `npm run eject`拆开 react-scripts 进而配置，这里并不强要求配置，所以我们这里跳过路径的自定义配置。下面我梳理了一份平时需求中常用的配置，有需求的同学可以参考一下：

```
// 需要走babel转译的依赖，有一些依赖基于esm实现，需要转成commonjs
const ModuleNeedCompile2Cjs = [
  'lodash-es',
].join('|');

module.exports = {
  testEnvironment: 'jsdom', // 运行环境，不需要ui自动化写node
  transform: {
    // 转译使用的工具，可以换esbuild, swj
    '^.+\.(js|ts|tsx|jsx)$': '<rootDir>/node_modules/babel-jest', 
    // svg 的 mock，不用测
    '^.+\.svg$': '<rootDir>/__test__/mocks/svg-transform.js',
  },
  // 初始化的配置，引入 testing-library 的额外 expect 类型
  setupFilesAfterEnv: ['<rootDir>/__test__/setup_test.js'],
  moduleNameMapper: {
    // css 的 mock
    '\.(css|less|sass|scss)$': 'identity-obj-proxy',
    // 如果项目中有加 alias 别名可以这样指向一下，jest不走 webpack
    '^@/(.*)$': '<rootDir>/src/$1',
  },
  // 需要转译成 commonjs 的依赖
  transformIgnorePatterns: [`<rootDir>/node_modules/(?!(${ModuleNeedCompile2Cjs}))`],
  // 需要收集单测覆盖率的文件，glob表达式，业务项目可以控制在公共components和hooks
  collectCoverageFrom: [
    '<rootDir>/src/**/*.{js,jsx,tsx,(!d).ts}',
  ],
  // 覆盖率生成的目录
  coverageDirectory: '<rootDir>/__test__/cov',
  // 覆盖率值的卡点，推荐业务 50% - 70%，架构 70% - 90%，涉及滚动，跳转等较难覆盖逻辑可以适当下调
  coverageThreshold: {
    global: {
      branches: 90,
      functions: 90,
      lines: 90,
      statements: 90,
    },
  },
};
```

好了完成上面的配置后，我们可以尝试执行一下`npm run test:coverage`命令，跑一下我们的覆盖率：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0815a16663804cf199591bf86c2aa82d~tplv-k3u1fbpfcp-zoom-1.image)

可以看到，覆盖得还是很不错的，都覆盖了 100%，不过最后一个组件 ScrollList， 因为我们是通过端对端测试覆盖了，所以这里覆盖率是 0 。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff6b7db161a043d397887304bb1d0b8d~tplv-k3u1fbpfcp-zoom-1.image)

光凭 Jest 的覆盖率肯定是不符合预期了，不然明明覆盖了的组件却不包括进来，岂不是白干了，下面我们来看看怎么覆盖 cypress 的那部分。

## Cypress 端对端测试覆盖率

Cypress 本身是没有与 storybook 配套生成覆盖率的能力的，我们需要借助一个依赖的能力，babel-plugin-istanbul，这个插件的功能有点像插桩，它会为我们的每一行代码之间插入计时器，从而达到测试覆盖率的目的。我们可以先来安装一下依赖。

```
npm install --save-dev babel-plugin-istanbul
```

因为 cypress 直接测试的其实是 storybook 的终端页面，所以我们为 storybook 配置一下 babel-plugin-istanbul 插件，其中 include 是需要插桩的目录，也就是我们希望统计覆盖率的目录。这样我们的 storybook 中就已经隐藏了覆盖率插桩了。

```
// .storybook/main.js
module.exports = {
  // ...other
  babel: (options) => {
    return {
      ...options,
      plugins: [
        [
          "babel-plugin-istanbul",
          {
            include: "src/components/**/*.{js,jsx,tsx,(!d).ts}",
          },
        ],
      ],
    };
  },
};
```

如果这时候我们打开 storybook，在终端中输入 window.__coverage__ ，就可以看到对应的覆盖率信息了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c0400a7877648618d0b00f8d5883e8c~tplv-k3u1fbpfcp-zoom-1.image)

不过光 storybook 中有还不行，我们要想办法把这个覆盖率生成到我们的项目文件中，需要安装 @cypress/code-coverage ，这是 coverage 提供的覆盖率支持，它本身并不会生成覆盖率，但它可以从测试页面中的终端中读取到对应的覆盖率配置，并生成我们需要的覆盖率文件。我们先来安装一下依赖。

```
npm i --save-dev @cypress/code-coverage
```

然后我们在 cypress 的配置文件中加入下面的配置引入插件。

```
// ./cypress/support/e2e.ts
// ... other
import "@cypress/code-coverage/support";
```

```
// ./cypress.config.ts
import { defineConfig } from "cypress";

export default defineConfig({
  e2e: {
    // ...other
    setupNodeEvents(on, config) {
      require("@cypress/code-coverage/task")(on, config);
      return config;
    },
    // ..other
  },
});
```

完成这些步骤以后，我们可以尝试执行 cypress GUI 页面，并执行用例看看：

```
npm run cypress
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45e138c9d8204059ba1eca892ad810f8~tplv-k3u1fbpfcp-zoom-1.image)

可以看到用例执行的结果中已经有报告生成的记录了，每次生成以后，会把结果同步给 .nyc_output 和 coverage 目录，如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fb6fe8d23094d939b9d361f904f21ae~tplv-k3u1fbpfcp-zoom-1.image)

我们查看一下最终的覆盖率结果，还是挺不错的。如果不使用 cypress 手动触发覆盖率生成，我们使用上节课提到的 cypress:run 命令自动生成也是 ok 的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89f32428732b432b9ca318ddf696b341~tplv-k3u1fbpfcp-zoom-1.image)

## 覆盖率合并

在合并之前，因为我们没自定义目录， cypress 和 jest 都会使用 coverage 目录，这样会有冲突影响后续覆盖率的合并，所以我们需要更改一下 jest 的覆盖率生成目录。

```
npm run eject
```

然后我们在 package.json 中加入下面的配置：

```
// package.json
"coverageDirectory": "<rootDir>/jest/coverage"
```

再重新生成，jest 的目录就会在 jest/coverage 下了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1742aa86c2584eebad35e6706e796cf4~tplv-k3u1fbpfcp-zoom-1.image)

我们再补充一下 .gitignore，覆盖率可以不用提交上去，避免后续 CI 用了之前的覆盖率：

```
// . /.gitignore
# testing
/coverage
/.nyc_output
/jest/coverage/
```

不过需要注意的是，使用 eject 后我们就不再是使用 react-scripts 了，storybook 中对应 react-scripts 的插件也需要去掉：

```
// ./.storybook/main.js
addons: [
    "@storybook/addon-links",
    "@storybook/addon-essentials",
    "@storybook/addon-interactions",
    "@storybook/preset-create-react-app", // 去掉
  ],
```

现在来合并我们的覆盖率，每次分俩报告，这个看起来实在麻烦，不知道大家有没发现，两份报告的 json 在格式上都是相似的，所以我们是可以做到合并的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b3cbf4237144d6086f5245be410d03f~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04dfc3b434374952a7fe699aef9982f2~tplv-k3u1fbpfcp-zoom-1.image)

为了实现合并的效果，我们需要借助 istanbul-combine 依赖，这个可以将多个覆盖率的报告合并为一个，可以在下面的终端中执行这个命令。

```
npx istanbul-combine -d test/merged -p detail -r lcov -r json 
jest/coverage/coverage-final.json coverage/coverage-final.json
```

其中 coverage/coverage-final.json 存放的是 cypress 的覆盖率，jest/coverage/coverage-final.json 存放的是 jest 的覆盖率，我们需要将它俩合并为一个，不过合并的过程中可能会遇到这个问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cadfecebeb704fdaa3d3acb796082b6f~tplv-k3u1fbpfcp-zoom-1.image)

我们按 ctrl 切到依赖中的位置，手动加入下面的代码，这个是 istanbul-combine 的一个已知问题，我看已经有 issue 反馈这个问题了，如果过段时间还没有被修复，我就给他们提个 PR 跟进解决一下。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/809a5287aade4a679580bacc3bae86a7~tplv-k3u1fbpfcp-zoom-1.image)

我们加上这行以后应该就可以正常运行了，可以看到我们的根目录生成了一个 test/merged 的文件，如下：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/477b559ffb5e4a30b50012b394cd55d7~tplv-k3u1fbpfcp-zoom-1.image)

点开里面的覆盖率看看，可以看到已经合并了~现在就舒服多了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/789da12db36c4655af49321927fe523e~tplv-k3u1fbpfcp-zoom-1.image)

因为后面我们还需要集成到 CI 中，所以在服务器手动改依赖是不现实的，这边提供另一个合并的方案，我们先来安装一下依赖：

```
npm i istanbul-merge --save-dev
```

然后我们修改一下 package.json，并且执行一下`npm run coverage:merge`：

```
"coverage:merge": "istanbul-merge --out coverage.json jest/coverage/coverage-final.json coverage/coverage-final.json",
```

不过这个依赖不能生成 html，而且 star 比较少，但是效果的确是可以满足的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23b3897dfeed43529e0a3f043bf107ae~tplv-k3u1fbpfcp-zoom-1.image)

这个合并后的 json 我们同样可以加到 .gitignore 中：

```
// .gitignore
coverage.json
```

## 怎么提高测试覆盖率？

那么我们怎么提高覆盖率呢？可以打开我们最终合并的覆盖率文件，右键用默认浏览器打开就可。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e05b39ff4bd4ba0bb84bc4ad2c3008a~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fdcb6b8ca8447d68e6fd532f2abf79b~tplv-k3u1fbpfcp-zoom-1.image)

通过点击文件，我们进到对应的文件中：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/268ed3caf2904d69b126aaab3e7a88bb~tplv-k3u1fbpfcp-zoom-1.image)

如果有没覆盖到的情况，会标红，这里解释一下为什么 branch 覆盖率是 3/5 , 因为我们的插桩抓到了 5次滚动的执行，但是只有 3 次我们会执行 branch 的逻辑，这个是符合我们预期的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8fe76c3de1894500b22b75b4cb9b5338~tplv-k3u1fbpfcp-zoom-1.image)

对于标红的图，大家可以参考 jest 的覆盖率图。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1051a6efa9f440e29db3310176b56223~tplv-k3u1fbpfcp-zoom-1.image)

这些都是没有走到的逻辑，我们需要做的就是考虑怎么为它们覆盖到，保证用例能走到这些逻辑就好，这样就可以有效地提升覆盖率。

## 小结

这节课我们学习了怎么进行自动化测试覆盖率的统计，因为我们分别使用了 jest 和 cypress 两种方式，所以需要为它们各自覆盖覆盖率，然后再将它们的覆盖率合并起来，通过对覆盖率的统计，我们可以很清晰地知道还有哪些代码没有被测试用例覆盖到，进而帮助我们补充这部分用例，使得我们组件发布的信心更高。

不过现在的测试流程还依赖我们自己执行命令，在多人合作中，我们没办法保证每个合作同学都会按约定去执行覆盖用例，并且保证用例能够正常去执行，所以我们要在 CI 流程中加入对应的测试节点，保证整个流程能够被规范用起来。下节课我们就来学习怎么将自动化测试整合到项目的持续集成当中。

## 16.CI：项目自动化测试的持续集成方案

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了怎么对自动化测试覆盖率的统计，分别统计了 Jest 和 Cypress 的测试覆盖率，Jest 的覆盖率比较简单，可以直接通过它提供的能力进行统计，但是 Cypress 需要我们自己通过 “插桩” 的方式进行统计，最后将两个覆盖率进行了合并，获得了我们项目最终的一个覆盖率。

当然在实际的项目开发中，一个项目大多数情况下并不是一个人来维护，不可能凭借口头上的要求来保证每个开发者在项目提交或是 pull request 时通过用例或是满足覆盖率，这不现实也不保险，所以我们要把这部分验证绑定到 CI，使得每次主分支的 commit 和 pull request 都可以得到限制验证。这节课我们就来学习具体应该怎么实现这个效果。

## 使用 Codecov 存储覆盖率

上节课虽然我们获得了一个覆盖率，但是这个覆盖率终究只是一个文件，它并没有得到一个有效的汇总，也不能提醒什么（除非每次 pull request 我们都自己生成看一看），所以这里我们需要把它存储起来，进行一个汇总提示，借助 Codecov，这是一个开源的代码覆盖率汇总的地方。

首先登录一下 [Codecov](https://app.codecov.io/gh) ，这边使用的是 Github 账号登录，大家也可以选择其他的方式，登录完成后，在 not yet setup 处可以看到我们还未接入 Codecov 的仓库，我们点击我们需要接入的仓库，就可以获得一个密钥 token。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60e438a5733447739acce131c8dcf4ea~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46d4accc9d3e47e79ae415d37f16f0cd~tplv-k3u1fbpfcp-zoom-1.image)

然后我们在项目中合并覆盖率后，执行下面的命令，发现覆盖率就已经上传到 Codecov了。

```
npx codecov --token=xxx(换成你的token) --file=coverage.json
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b66778ddb4a47c8928bf217a25adf58~tplv-k3u1fbpfcp-zoom-1.image)

这个结果还有大用途，可以和我们的 Github 记录结合起来，我们继续往下做。

上面我们已经尝试过手动上传 Codecov 了，不过呢，这个 token 还是暴露出来的，后面接到命令脚本里可不行，这样所有人都可以看到我们仓库的 token，如果随便上传一些东西上去不就有脏数据了？我们需要给它加上一个密钥来进行脱敏。

我们点到 Github 的 settings 中，点击新建仓库密钥。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e49c1cb06c4e4ec684e1c73221c0052e~tplv-k3u1fbpfcp-zoom-1.image)

然后我们把密钥填入。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/744acbc76c23446a8285fc5c57a4cad2~tplv-k3u1fbpfcp-zoom-1.image)

后面就可以利用 secrets.CODECOV_TOKEN 这个 key 在我们的 CI 中运行了。

## 怎么把操作绑定到 CI ？

现在我们应该把测试相关的操作绑定到 CI 上，这就需要借助 git action 了，它可以帮助我们在项目中创建自动化的软件开发流程，从而形成流水线。

大家先按我的步骤继续走下去，后面我们会详细解析应该怎么写一个 action 出来。我们先安装下面的依赖：

```
npm install wait-on --save-dev
```

然后我们在 .github/workflows 目录创建一个 test.yml，这个目录用于指定对应 github 的 action，每个 yml 文件都会对应到一个 action，这些 action 会在指定的情况下触发对应的命令。

```
name: test

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]
  workflow_dispatch:

jobs:
  coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: "16"
      - name: Run install
        run: npm install
      - name: Run Jest coverage
        run: npm run test:coverage &
      - name: Build storybook
        run: npm run build-storybook
      - name: Serve storybook
        run: nohup npx http-server -p 6006 storybook-static &
      - name: Run Cypress coverage
        run: npx wait-on http://127.0.0.1:6006 && npm run cypress:run
      - name: Run Coverage merge
        run: npm run coverage:merge
      - name: Run codecov
        run: npx codecov --token=${{ secrets.CODECOV_TOKEN }} --file=coverage.json
      - name: Run test
        run: npm run test
```

我们来看上面的 action， 简单讲讲为什么这么写。

-   `name` 是这个 action 的名字，会在 Github 的 action 页面对应出来。

-   `on` 对应这个 action 的触发方式，这里我们加上了两个触发方式，当 master 分支 push 和 pull request 的时候，`workflow_dispatch` 这个加上，可以使得这个 action 允许被手动执行。

-   `job` 则对应这个 action 触发的时候需要执行的命令，其中包含着很多流水线的节点：

    -   `coverage` 可以理解成是一个流水线的节点名称，你可以自己定义，当然我们也可以定义多个；

    -   `runs - on` 对应我们运行的环境，我们默认填最近版本的 ubuntu 就可，也就是 ubuntu-latest；

    -   `steps` 中就是这个流水线节点中需要执行的内容了。

        -   `actions/checkout@v3` 和 `actions/setup-node@v3` 就是运行的 node 环境 action 打包，会自动帮我们配置好 node 环境，如果是 14 的版本，这两个可以用 v2。

        -   `name` 和 `run` 分别对应节点步骤名称和要执行的命令 , 这里需要特别解释几个步骤。

            -   `npm run test:coverage &` 中的 & 是为了保证这条命令在后台执行并不阻塞后续节点的展开，因为 `npm run test:coverage` 在完成后并不会退出进程。
            -   `nohup npx http-server -p 6006 storybook-static &`和上面同理，因为服务并不会自动中断进程，我们需要后台执行，保证后续节点不被阻塞。
            -   ` npx wait-on  ``http://127.0.0.1:6006``  && npm run cypress:run `因为 Cypress 需要在 storybook 服务启动后才可以进行端对端测试，所以我们需要 wait-on 等待服务能被响应后再开始端对端测试。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4b2f80f30884651998e7f6363d8d0f1~tplv-k3u1fbpfcp-zoom-1.image)

我们把这则修改提交到 PR 后，可以到 action 看到一则自动运行的 action。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e73a0e099ede41c6b6fcf3e2784b05e6~tplv-k3u1fbpfcp-zoom-1.image)

点进这个 action, 可以看到我们之前设置的节点。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6082313cfbc145d2a5f2c7bb2728a9b6~tplv-k3u1fbpfcp-zoom-1.image)

在这里看到每一步执行的情况，可以看到，每次类似的覆盖率都会被更新到 Codecov中。

## 如何在本地开发 action？

Action 的触发默认是使用 master 主分支的 workflow，那我们在分支中应该怎么开发呢？我们在上面的部分介绍了，如果加上`workflow_dispatch`， 那么我们就可以手动执行这个流水线。

切到 actions，可以看到左边有我们定义的这个 test action，可以按下图点击右侧的 run workflow，选择对应的分支后，手动执行流水线。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c98b103c06834bc98417855e1f472531~tplv-k3u1fbpfcp-zoom-1.image)

## Codecov 机器人

Codecov 除了基础的覆盖率存储功能外，还可以支持我们每次 PR 时在下面进行覆盖率的评论，可以在 [Codecov 团队机器人](https://docs.codecov.com/docs/team-bot) 页面开启 Github 机器人。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/161e1eb25e0f444d91c8374f8bd7d194~tplv-k3u1fbpfcp-zoom-1.image)

然后我们在 PR 的时候执行完 action， codecov 就会在 pr 下评论当前 PR 的覆盖率情况

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e6852e491a84646aac73c3823fe61a2~tplv-k3u1fbpfcp-zoom-1.image)

## 用例的验证

在上面的 action 中，最后还验证了我们的用例能否通过，可以随便改错一个用例，并提交 PR，看看会发生什么。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b469220a72b41c88d708b7a380a0659~tplv-k3u1fbpfcp-zoom-1.image)

可以看到， PR 下的 check 将会报错，我们可以通过这种方式来统一项目中的规范。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d1b34f0dcaf4522b7e8fec9fdc3fb03~tplv-k3u1fbpfcp-zoom-1.image)

对于 action，我们也可以按照它的使用类别创建多个，拆分开来，这样有问题的时候，我们也可以快速定位它是哪个问题。现在我们把这个用例改回来，用例就可以通过了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/507082cfdbd64a72a39d862d327bc5d9~tplv-k3u1fbpfcp-zoom-1.image)

现在就可以进行分支的合并了~如果是多人合作，就可以让同团队的同学帮你 code review，然后 approve 一下了。

## Codecov 覆盖率标记

大家在使用一些开源项目的时候，经常会看到它们的 readme 里会有相关覆盖率的标签，我们以 Semi 为例，可以看到会有覆盖率 89% 的标记。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1f8276231dd4720abd167f40ec3fb82~tplv-k3u1fbpfcp-zoom-1.image)

难道是随便写的标签？当前不是，要是这么搞肯定要被骂死，打开我们项目的 Codecov 的 settings 页，可以看到有个 badge 标签可以复制

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5de818177424919b29833c6a9094aca~tplv-k3u1fbpfcp-zoom-1.image)

copy 下来贴到我们项目的 Readme 中试试。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c56657c028449caaf0abb8c49e9725a~tplv-k3u1fbpfcp-zoom-1.image)

这样我们项目的覆盖率结果也就生成了，用户也可以点击我们的 Codecov 跳转到 Codecov 项目页进行细节的查阅，对于架构项目，可以大大增加用户使用的信心。

## 小结

这节课我们学习了怎么对项目自动化测试进行持续集成，达到在每次 pull request 或是 push 的时候自动进行流水线的效果。通过这种方式，可以有效统一项目开发中团队成员的规范，我们的测试用例也可以真正在项目维度提高整体的质量。

到这里，其实我们前端自动化的内容就已经学习完了，下节课是我们《前端自动化测试精讲》的最后一节，我想和大家分享一下，写这本小册 & 为团队中后台推广单测这段时间我的一些困惑和思考，希望可以给大家一些对代码质量的额外启发。

## 17.最后的思考：用例的边界和深度究竟在哪里？

上一节课中，我们学习了怎么将自动化测试融入项目的 CICD 中，分别配置了 Codecov 和对应的 git actions，对我们的项目 master 分支中的 pull request 和 push 节点进行了流水线的卡点，大家也可以根据自己的需求去配置需要的卡点。

到这里我们前端自动化测试的相关技术知识就已经学习完了，但是很多同学相信还会有不少困惑，对于一个需求，我们应该从哪些方面来展开用例呢？我们又应该怎么向团队推广自动化测试呢？

这些困惑我思考了很久，这节课我们就来一起聊聊，用例的边界和深度究竟在哪里？

## TDD & BDD 的理想国

首先我们来了解两种开发模式，TDD 和 BDD ，这两种都是敏捷软件工程开发下的产物，相信很多同学在阅读这本小册前就已经有所耳闻了。

在之前的章节中，我们编写自动化测试用例的时机都是在组件开发完成之后，对于 TDD 和 BDD 而言，它们都推崇测试驱动开发，与我们平时业务的软件开发模式不同，测试不再仅仅是研发的下游，同时也成为上游的一个角色。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/430f312a5e824e868dd5cf564ab9307b~tplv-k3u1fbpfcp-zoom-1.image)

在这两个开发模式中，期望用例可以在实际开发前确定，并且实现对应的自动化测试后，再进行对应的开发，使得组件可以切合于测试或是用户的维度展开，获得更合理的设计和封装。

TDD 和 BDD 最大的区别在于，TDD 站在测试的维度展开，通常由于研发和测试共同来制定用例，或是研发根据组件维度提供用例测试进行 review。而 BDD 则是站在系统行为层面设计用例，多个团队共同合作提供出最终的设计用例。

这两种开发模式的初衷的确是很好的，但是站在国内的大环境下看，这两种模式可能只能是开发人员心中的理想国，能实现的少之又少，BDD 就不用说了，涉及过多的团队，一起合作整理用例是不现实且低效的。而TDD，我们可以一起来看看它和现状有哪些冲突：

-   研发懂开发，但是对用例的设计不够专业，测试虽然懂设计用例，但是对代码的维护和封装理解上又弱于研发，两者虽然理论上可以进行优势互补，但是在实际的合作中是难以实现的，这就强需求一个对研发和测试用例设计都很专业的人来介入，这样的人选并不多。
-   国内的研发迭代频率是较高的，这种模式会影响整体的开发进度，大环境下，宁可选择手工测试也不会选择 TDD 的模式，因为短期收益比一定是更低的，长期不确定，得看合作情况。
-   这种模式可能会导致研发过度关注用例，而缺失对整体系统的认知。需求开发会被等价于所有的用例通过，长期看，对研发和测试人选的综合能力要求都不小。

之所以称为理想国，代表着虽然它在实际的开发中很难落地，但是仍然是我们最理想的开发模式。那么有没有一些场景，我们可以尽可能去用 TDD 这种模式来开发呢？

是有的，对于一些输入和输出都比较明确的函数，我们是可以先自行定义好自动化测试用例，再对函数内容进行补全的，这个过程可以很好地审视函数是否有功能或者边界情况的遗漏。

但是想要在业务组件需求中应用，我想目前还是很困难的。对项目人员水平和大环境的要求都很高，这个理想国难以推行，至少在国内来看，还需要一个长期努力的过程。

## 测试用例应该从哪些角度展开？

在写这本小册之前，其实我也有和一些同学聊，为什么大家不愿意去写单测呢？其中一个让我比较震惊的理由是，一个需求，他的用例写了快一个月，成本太大了。我很奇怪，真的要写这么久吗？

这个同学是很资深的工程师，对前端各个领域都有自己的见解，技术上是没有问题的，所以我特地 clone 他以前的那个仓库看了一下对应的用例，突然知道为什么会写这么长时间了。用例之间重复交集的内容过多，或是对本不需要测试的内容进行了测试。

总地来说，还是因为缺乏用例设计的思路，而不知道怎么展开对应的测试用例。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf0188d86fc44108a1957482db1b5491~tplv-k3u1fbpfcp-zoom-1.image)

因为大多数前端的确缺乏对用例设计的经验，即使让测试人员来协助我们，测试人员的用例也没办法很好站在组件维度从封装和功能的角度来展开，所以不知道怎么展开对应的组件测试是很正常的现象。

这里我给大家提供我测试一个组件的思路：

-   Props 的覆盖：组件的每一条 props 需要覆盖一条用例，因为组件的每个 props 都是对外暴露的。通常来说，每个 props 都对应这个组件的一个重要能力，所以这个是必须强制覆盖的。
-   组件耦合度的审视：针对组件的 props 覆盖完成后，这个组件的用例覆盖率通常可以达到 70% 以上，如果覆盖率仍然较低，那么需要考虑是不是有核心的功能可以通过 props 暴露出来。这种情况下大概率是耦合了一些业务逻辑，导致用例没办法走到，建议大家把业务逻辑抽出来提高封装复用度。
-   对剩余代码逻辑覆盖用例：props 的用例覆盖可以包括组件的大部分能力，但是可能会有逻辑的遗漏，这是正常的现象，因为并不是所有逻辑都可以通过暴露的 props 来触发，在 [15 | Coverage: 自动化测试覆盖率的统计](https://juejin.cn/book/7174044519350927395/section/7176804672613646376) 我们有介绍过怎么提高覆盖率，可以通过 coverage 的提示来覆盖到未覆盖的逻辑。
-   合理使用快照：对于的确稳定几乎不变的组件，采用小快照的方式进行。
-   只断言核心元素：很多同学写测试用例，恨不得把每个 DOM 都断言一遍，这个是不合理的，我们应该只断言核心的单个元素，每则用例的长度控制在 10 行以内才是正常的。

通常来说，在完成上面五步后，排除跳转滚动等逻辑，单测的覆盖率可以达到 85% - 90%，时间成本也完全可控。

提供一组我在团队内推广单测时获得的数据给大家参考，一个 JSON Schema 动态渲染的组件，简单来说可以通过 JSON schema 动态解析为需要的表单元素，当时我的开发 & 重构周期在 7 天+，单测的行数是 82 行，覆盖率可以达到 100%，对应的开发/单测时间比远低于 10：1。

所以，如果有一个合理的测试用例，测试的时间不应该会占用开发过多的精力和排期，还是可以控制的。

## 怎么在团队中推广自动化测试？

最后我们来一起聊一聊至今我仍然存在困惑的点，怎么在团队中推广自动化测试。

团队内的每个成员都有自己的想法和习惯，怎样才能去说服他们去用起来自动化测试呢（排除 leader 直接推的场景，leader 很赞同就可以跳过这一段了 hahaha）？

任何一个可以在团队内展开的规范，都有以下的几个特点：

-   可以解决普遍的一个痛点；
-   有比较流程化的规范，或者比较容易通过技术手段的方式达成流程化的效果（比如 lint)；
-   学习成本可控，大家可以快速上手；
-   时间收益比较高。

首先我希望大家可以明确一点，自动化测试的核心目标是为未来的迭代保驾护航，所以收益上是很难在短期看出什么效果的，而且衡量的方式也比较模糊（因为你没办法解释，这里本来要出一个 bug ，因为有自动化测试，成功地阻止了这个 bug）。

出于这个原因，给业务项目推广单测是一件极其困难的事情，除非你们的业务项目 bug 很多，很好衡量。

我们目前团队的情况是，要求需求的 bug 估分比低于 0.5，也就是你 2 天的排期只允许你出一个 bug，如果最后 bug 过多就需要复盘，所以大家的项目质量都比较高（至少从 bug 单数量上看，可能是包含了一些 QA 的人情世故的），这个收益就不好衡量，也没办法解决大家的什么痛点。

所以我是怎么慢慢向团队推广自动化测试的呢？

-   首先我在我负责的业务线先自己推广了自动化测试，因为全权负责的关系，所以不会有太多的阻碍，只需要我自己控制业务和测试的平衡就好，在这个基础上试验一段时间后，落地一个最佳实践的方案以及具体的时间比，提供给 ld，来获得最基本的支持。
-   虽然已经有了最佳实践的文档，但是大家可能还是不愿意去做的，因为上面我们也说了，在团队层面推广，大家需要有共同的痛点，这个痛点在业务项目中很难得到体现，所以我先向团队内的架构项目进行了推广，因为架构项目有多个业务线复用，这个痛点相比业务项目会体现得更明显。
-   在有愿意体验的同学后，怎么去解决学习成本的问题？其实最好的学习方式都是基于模仿的，如果项目中有可以运行的用例后，照猫画虎也就不那么困难了。真正难的其实是开始，那么对一开始有意愿去尝试的同学，我就会帮他们的项目接入测试，并且针对典型的代码和组件，我来帮他们覆盖一个最佳实践的用例，通过这种方式慢慢引导同学们开始去写。
-   对架构项目进行流水线卡点，我们可以通过 git actions 的方式给项目的流水线逐一卡点，来促使开发同学不得不写用例来保证功能的完整，当然，我还在思考这个具体怎么实施，力度才不会过。

总而言之，最重要的就是能够**收益明确 & 学习成本不高 & 流程可以规范化**。

目前团队里的自动化测试已经推广了一部分，但是业务项目推广的效果还是不尽人意的。最主要的原因就是业务项目需求的频繁迭代 & 业务压力大，开发同学没时间学习和尝试新的事物。

这个我还在想怎么去解决，可能会通过写一些 lint 或是模版生成测试用例的插件来提效，后面如果有好的解决思路，我也会在掘金上分享给大家，一起讨论。

## 小结

到这里《前端自动化测试精讲》就结束了，自动化测试是我半年来一直思考困惑的事，也算是对自己长期对项目质量思考的答卷吧。

其实我一直觉得，任何项目的终点可能都是重构，随着需求的迭代，人员的流动，项目会越来越不可维护，即使你的初衷再好，迭代过程中都深思熟虑，这个终点可能都无法避免，只是时间的问题。

一个工程师的优秀与否就在于将一个项目引导到这个终点的时间需要多久，优秀的工程师一直在尽力地阻止这一天的到来，或者让这天到来的时候重构不那么困难。而自动化测试就是我们这个工程中最重要的方式，前期可能会有额外的压力，但是长期来看，对项目代码的质量提升都是有巨大帮助的。

很开心大家能看到这里，如果对自动化测试或是项目质量有自己的想法或困惑的同学也可以加读者群，我们一起交流，祝愿大家能早日成为独当一面，重视代码质量的优秀工程师～

## 18.【加餐】Jest Mock 的极致用法 : 如何对 VSCode 插件进行单元测试？

大家好，我是祯民。我们在平常的开发中，面对一些基础轮子或者服务的项目，常常会需要写一些单元测试来保证历史逻辑的稳定。
> 单元测试（Unit Testing）是指对软件系统中的最小可测试单元进行检查和验证，通常是对程序中的一个函数、一个类或一个模块进行测试。其目的是确认这个部分的代码是否能够正常工作，达到预期的结果，并且百分之百地覆盖所有的代码分支和可能的输入情况。


**单元测试不同于平时测试同学的功能测试，它更看重以某个模块的角度展开测试，从模块到整体，进而达到为整个系统维稳的目的**，这个是研发同学比较常用的自动化测试手段。

对于前端的单元测试，我们常常使用 jest 作为我们的测试库。当然具体的原因和其中包含了什么功能并不是咱们这篇文章的重点，我们不会过多介绍，还不清楚一些前置信息的同学可以看看这篇[《技术选型：React testing library or Enzyme?》](https://juejin.cn/book/7174044519350927395/section/7176612133294063668)

因为测试过程中很难做到每个环境和 API 是真实存在的，所以**大家在用 Jest 完成单元测试的时候，常常需要使用 mock 来模拟一些特定的环境或者 API 信息来保证整体流程的通畅**，mock 的手段和思路还是有很多值得分享的地方的，所以这一章节我们将来具体学习 Jest mock 的极致用法。

为了方便大家理解，而不是纸上谈兵，这篇文章会以 VSCode 插件为背景展开。因为 VSCode 插件运行时环境包含很多插件 API 以及通常作为一个服务存在的原因，所以它是一个非常典型的适合用于 mock 的业务背景，当然没开发过 VSCode 插件的同学也不需要紧张，这篇文章会包含一些必要的前置知识，其实很简单，并不影响全文的学习。

本文的内容会从以下三个方向展开：
- **VSCode 插件开发前置知识**：在这个模块中，我会给大家简单介绍一下 VSCode 插件开发有什么特殊性，以及我们常用的 API 可能有哪些。
- **VSCode 运行时环境的 mock**：在这个模块中，我们会来学习 VSCode 插件单元测试中必须完成的环境 mock，不仅是 VSCode 插件开发，只要涉及前置环境配置的开发（比如 sql, canvas 等），这都是必不可少的一步。
- **公用模块的 mock**： 对于一些公用模块，我们虽然可以使用它们的真实 API 来调用，但是真实 API 往往存在一些前置环境，或者 catch 兜底，导致我们需要花费额外精力保证这些公用模块在测试环境下可用。可事实上，这些公用模块又并不是我们用例的重点，这时候就可以用 mock 来简化这个调用调试的过程。
- **内部类引用的 mock**：在服务开发中，我们通常会定义大量的类，而且类之间也可能会存在互相的调用，在这个过程中，类的互相调用很容易导致类的用例之间耦合度剧增，从而脱离设计的单一原则。在这种场景下，我们也可以使用 mock 来提高用例的稳健性。

## VSCode 插件开发前置知识
VSCode 插件开发简单来说就是一个 node 服务的开发，只不过在常规 node 服务基础上，它额外提供了一些全局环境下的 API，来触发 VSCode 中的参数配置、弹窗、确认框和插件信息等原生能力。以我前段时间发布的一个插件 demo 为例，它的目录结构是这样的。

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56973219edca4f628189fae26ccee3da~tplv-k3u1fbpfcp-watermark.image?)

对于VSCode 插件开发，微软是有提供一个脚手架来初始化项目的，大家可以参考下面指令试试
```shell
# npm
npm install -g yo generator-code
# or yarn
yarn global add yo generator-code
# 根据提示创建插件工程
yo code
# 使用 VSCode 打开插件工程，假设为 hello-world
code ./hello-world
```
在创建完成以后，大体目录结构和上面的截图应该差不多，大家真正需要关注的主要是两个文件，一个是 extensions.ts，这个是整个插件的入口文件。也许你在初始化的时候选的内容不同，所以你的入口文件也会有差异，具体大家可以以 package.json 中的 main 配置的是啥为准。

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17795f89d00145bc94a91a4217ea29e0~tplv-k3u1fbpfcp-watermark.image?)

这个文件中的内容也很简单，通过 vscode 提供的 registerCommand 方法我们可以注册一个命令，第一个参数是命令的 key，第二个参数是命令触发后的回调函数，完成注册后我们只需要安装插件即可搜索到这个命令。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df639a4278e04424806951b774f39781~tplv-k3u1fbpfcp-watermark.image?)

可以看到 vscode 实际开发是很简单的，没什么特殊的，我们只需要像正常的 node 服务那样编写功能类以后，在命令回调中调用即可。

第二个大家需要关注的文件即 package.json，在 vscode 插件开发中，package.json 中不仅是一个存放项目脚本和依赖的文件，更是整个插件名称、配置参数以及菜单等重要内容的配置文件。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/794106ceed6c4bcdbe12ab901cea43ac~tplv-k3u1fbpfcp-watermark.image?)

具体怎么配置的大家可以自行去官网查阅，这里就不做介绍了。大家只需要知道，在这里配置好的参数会在插件安装后，从 extensions 指定插件目录体现。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3489f9e64b6e48d3a2da1080083ed92a~tplv-k3u1fbpfcp-watermark.image?)

同时我们可以通过调用 vscode 提供的 API 获取到这些参数的配置值，并在我们的实际逻辑中调用。

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7bfa052fa424d24be5e58ab364e3eaf~tplv-k3u1fbpfcp-watermark.image?)

除了 registerCommand 和 getConfiguration 外，vscode 还提供了其他的一些方法来调用它的原生能力，比如 showWarningMessage 触发弹窗警告等，更具体的我这里就不提了，大家可以去官网查阅 API。

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17d4319368824912b8b6284a7bb12d3c~tplv-k3u1fbpfcp-watermark.image?)

我们可以看到 vscode 环境下提供了很多 node 环境下没有的能力和 API 来触发它们的原生事件，但是我们的测试环境是普通的 node 环境，意味着这些 API 是没办法在测试环境中正常使用的，所以 mock 的重要的意义就体现出来了，可以说对于 VSCode 插件的单元测试，如果你不合理使用 mock 是没办法完成的。


![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d56c7f26fc54b33b1a7f54192f40608~tplv-k3u1fbpfcp-watermark.image?)

另外提一个题外话，这里提到的 vscode 插件是我写的一个基于 gpt 模型开发的可以自动生成单元测试的辅助工具，感兴趣的同学可以试试，更详细的信息可以阅读[《（建议收藏深读）GPT 高阶玩法 - 万字 GPT 模型自动化应用指南（ javaScript 示例）》 ](https://juejin.cn/post/7221739494277480504#heading-12)


![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0ea53cef8753453bad4b83981dca7988~tplv-k3u1fbpfcp-watermark.image?)

## VSCode 运行时环境的 mock

上个小标题我们提到，vscode 环境相比 node 环境有很多额外的 API，比如弹窗，进度条等，要为它完成测试，需要mock 插件环境保证 api 的存在，这种针对环境且量不小的 mock 我们通常写在 jest 配置根目录的 `__mocks__` 目录下，这个目录下的文件会作为默认 mocks 加入测试环境，这部分在官方文档中也有额外的补充介绍。

> Manual mocks are defined by writing a module in a `__mocks__/` subdirectory immediately adjacent to the module. For example, to mock a module called `user` in the `models` directory, create a file called `user.js` and put it in the `models/__mocks__` directory.

下面我给出我的 vscode 插件配置给大家参考，这个没有一个标准答案，简单来说，你用到了哪些 API 你都需要为它们兜底一个实现或者值，不仅是 vscode 插件开发，别的场景也是如此。
```javascript
// vscode 环境 mock

const languages = {
  createDiagnosticCollection: jest.fn()
};

const StatusBarAlignment = {};

const window = {
  createStatusBarItem: jest.fn(() => ({
    show: jest.fn()
  })),
  showInformationMessage: jest.fn(),
  showErrorMessage: jest.fn(),
  showWarningMessage: jest.fn(() => ({
    then: jest.fn()
  })),
  createTextEditorDecorationType: jest.fn(),
  withProgress: jest.fn()
};

const workspace = {
  getConfiguration: () => {
    return {
      get: (section) => {
        const configuration = {
          'chatgptUiUnitTest.model': 'azure3.5',
          'chatgptUiUnitTest.ignoreDocument': [
            "**/{__tests__/**,*.{test,spec}}.{js,ts,jsx,tsx}"
          ],
          'chatgptUiUnitTest.supportedFileExtensions': '^(.*\/)?\w+\.(jsx?|tsx?)$',
          'chatgptUiUnitTest.testingLibrary': 'jest',
          'chatgptUiUnitTest.testingLibraryReplenish': '',
          'chatgptUiUnitTest.testDirectory': '__tests__',
          'chatgptUiUnitTest.testFileSuffix': 'test',
          'chatgptUiUnitTest.temperature': 0.8,
          'chatgptUiUnitTest.automaticRetries': 2
        };
        return configuration[section];
      }
    };
  },
  workspaceFolders: [],
  onDidSaveTextDocument: jest.fn()
};

const OverviewRulerLane = {
  Left: null
};

const Uri = {
  file: f => f,
  parse: jest.fn()
};
const Range = jest.fn();
const Diagnostic = jest.fn();
const DiagnosticSeverity = { Error: 0, Warning: 1, Information: 2, Hint: 3 };

const debug = {
  onDidTerminateDebugSession: jest.fn(),
  startDebugging: jest.fn()
};

const commands = {
  executeCommand: jest.fn()
};

class CancellationTokenSource { }

const ProgressLocation = {
  Notification: 1
};

const vscode = {
  languages,
  StatusBarAlignment,
  window,
  workspace,
  OverviewRulerLane,
  Uri,
  Range,
  Diagnostic,
  DiagnosticSeverity,
  debug,
  commands,
  CancellationTokenSource,
  ProgressLocation
};

module.exports = vscode;
```
我用到的 API 相对较多，大家可以根据自己的场景移除掉一些自己没调用的 API，然后我们再重新尝试，会发现用例将可以正常执行。

## 公用模块的 mock

在 node 服务开发中，我们常常会用到 fs 等模块进行一些文件操作，就比如下面的例子。
```javascript
export class B {
  constructor() {
  }

  b1(dirPath) {
    const fileContent = fs.readFileSync(dirPath, 'utf8');
    return fileContent;
  }
}
```
在上面的例子中，我们读了一个文件的内容并将它返回，在实际的测试中，大部分同学会这样设计用例，我们需要先创建一个测试文件，然后将路径传给这个文件，最后测试完成后还需要删除这个文件，比如下面的实现

```javascript
describe('B', () => {

  beforeEach(() => {
    // ... 测试前置环境准备（文件夹创建、文件写入）
  });
  
  afterEach(() => {
     // ... 完成测试后，清除缓存、测试文件等
  })

  it('test for b1', () => {
    b.b1();
    expect(a.a1).toHaveBeenCalled();
    expect(a.a1).toHaveLastReturnedWith('test');
  });
})
```

这个过程是不是太繁琐了？

而且在上面的测试过程中，**与其说我们在测试 b1 , 倒不如说我们在测试 `fs.readFileSync` 的功能**，是不是有点本末倒置的味道？事实上，在用例的测试过程中，我们通常都需要保证用例的单一原则性，通俗地讲，**你的函数干了啥事就测啥，通过别的函数完成的内容与我们无关。**

在上面的 case 中，我们完全可以通过 mock 来简化这个测试过程，比如下面的实现。
```javascript
import * as fs from "fs";

describe('B', () => {

  it('test for b1', () => {
    jest.spyOn(fs, 'readFileSync').mockReturnValueOnce('');
    const res = b.b3('test');
    expect(res).toEqual('');
  });
})
```
`jest.spyOn`可以监听某个公共模块，并通过链式调用的方式（比如这个 case 中的 `mockReturnValueOnce`）来提供一些确切的 mock 方式。我们上面也提到，这个用例中 `fs.readFileSync` 有没有 bug 我们并不关注，所以我们完全不用真实调用它的内部实现，可以通过 mock 拟定一个实现或者返回值，我们继续后续的流程。

这个用法在实际的测试中会有大量的应用，大家可以多思考练习。

## 内部类引用的 mock

因为 node 服务，与 web 开发不同的是，我们会定义更多的类，也会存在类之间的调用，那么如果存在类 A 和 类 B 的互相调用，那么对于它们的测试应该如何展开呢？

诚然，最简单直接也是最符合业务场景的做法就是，mock 一个足够真实的场景，来一步一步验证效果是否是符合预期的，这种效果最理想，但成本也最高，用例的耦合度也最高。

**单元测试与功能测试不同，我们的确需要从用户和产品功能的视角来展开用例的设计，但是代码结构的设计原理也是单元测试用例设计的一个重要因素。** 换言之，牺牲一些产品功能的完整度，来换取更细粒度的用例和更好维护的测试代码是可取的，我们可以追求更加单一原则的用例代码来提高我们测试代码的优雅度。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a6ed5aa5a964adf87529ba5933bd0bb~tplv-k3u1fbpfcp-zoom-1.image)

举个例子，例如 类 A 调用了 类 B，那么我们对类 A 的测试其实并不需要覆盖类 B 的逻辑，也就是说，类 B 功能是不是符合预期的在类 A 的用例中并不重要，我们只需要在类 A 的用例中保证涉及类 B 调用的部分存在且能有正常的值即可（这个保证也许是虚假不确定的）。

至于这其中的过程和类 B 是不是真的可以根据它的流程得到我们预期的值那就不是类 A 关注的了，这应该是类 B 的用例去考虑的，为达到这种目的，我们就可以使用 mock 来为 A 提供一个虚假不确定的 类 B 保证。

**这种用例的设计法则，极致地满足单一原则，虽然牺牲了一些业务完整度（因为做了也许虚假的承诺），但是写出的用例最为优雅可维护，即使类 B 的承诺真的出错了，也可以在它对应的用例中得到体现，而不干扰 A 的用例。** 我们来看下面的例子。

```javascript
import * as fs from 'fs';

export class B {
  constructor() {

  }

 b1() {
    console.log('b1');
  }
}

export class A {
  private b: B;

  constructor(bObj: B) {
    this.b = bObj;
  }

  a1() {
    this.b.b1();
  }
}
```
对于上面的例子，我们可以写出如下的测试用例
```javascript
import { A, B } from '../test';
import * as fs from 'fs';

jest.mock('fs');

describe('A', () => {
  let b: B;
  let a: A;

  beforeEach(() => {
    b = new B();
    b.b1 = jest.fn().mockReturnValue('test');
    a = new A(B);
  });

  it('b1: 是否调用了A的方法a1', () => {
    b.b1();
    expect(a.a1).toHaveBeenCalled();
    expect(a.a1).toHaveLastReturnedWith('test');
  });
});
```
不过需要注意的是，这样设计用例需要满足 b 的引用会在 a 的构造函数中传入，而不是在 a 中直接创建出来，mock 的引用需要保证一致，才能完成 b 方法的 mock 替换。如果是在 a 直接创建出来，a 中使用的 b 引用与测试代码中 mock 的 b 引用就会不同, mock 也便不会生效。

## 小结

到这里，我们这篇文章的内容就讲完了，对于单元测试而言，保证用例的单一原则是一个很重要的用例设计原则，为了达到这个目的，我们常常会使用 mock 来替代掉非该用例中使用的其他的方法。

一方面这样做可以减少对运行环境的模拟准备，也不需要在测试完成后清除之前准备的测试环境，另一方面用例的单一原则也可以达到一个极致的效果，只会包含对应函数中实际需要测试的内容。

我们知道测试用例除了保证历史功能的稳定外，还有一个重要的目的，就是文档用例化，相比 readme ，测试用例无疑是最好的最有时效性的文档，**一个具备单一原则的用例将是最好的组件或是服务文档，不管是交接还是带新同学都会有不错的效果。**

今天的课程我们就到这里，有问题欢迎大家在评论区提问交流。

## 2.技术选型：React Testing Library Or Enzyme？

> 代码仓库(后续学习都在这个仓库，CRA创建）：https://github.com/czm1290433700/test_demo
>
> 配置示例仓库：https://github.com/czm1290433700/test_demo_for_config

  


上一节，我们站在研发的角度大体分析了怎么写前端的自动化测试，不可否认的是，在特定的场景下，合适的自动化测试对项目的维稳和日后的迭代都有深远的意义。

通常，根据自动化测试的维度，可以分为单元测试和端对端测试。单元测试是更细粒度的、从代码组件层次进行的功能测试，而端对端测试是从用户视角，从项目整体展开的测试。从这节课开始，我们先学习单元测试。

针对单元测试，JavaScript 技术栈通常会选用 Jest 作为基础测试框架，它是 Facebook 开发的 JavaScript 测试框架，用于创建、运行和编写测试的 JavaScript 库。但是，**仅通过 Jest** **，** **没办法完成前端的所有单元测试**，因为与常规的接口逻辑测试不同，前端的单元测试涉及到 Dom 和事件的模拟，我们还需要选用一个辅助库来协助我们模拟相关的场景。

有两个主流的辅助库选择，Enzyme 和 React Testing Library，这两个库都是非常优秀的辅助库，它们都提供了测试应用程序所需的所有工具，都能够满足我们的单测需求，但从配置以及测试思路的角度上看，我更推荐大家使用 React Testing Library，下面我们将具体说明。

## 配置

### Jest

> 配置可参考配置示例仓库 test_demo_for_config master 分支。
>
> Node 版本 14 +

Jest 是基础的测试库，是安装 Enzyme 和 React Testing Library 的前置条件，在 create-react-app 脚手架中，会一并自动打包进来，我们这里以非 CRA 场景的例子，来示范一下怎么进行 Jest 的配置。仓库可以使用尤大的 @vitejs/app 来帮助我们初始化一个空白的项目（只是便于创建一个空项目，后续流程与 Vite 无关，Webpack 同样适用）。

```
 npm init vite test_demo
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7460e61b3624ff99c74f1ffe00f21b3~tplv-k3u1fbpfcp-zoom-1.image)

配置上我们选择 React + TS 就可，然后我们打开项目看看，可以看到，一个没有单测能力的项目创建好了, 我们可以打开项目看看。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed8132663b674e65bf0eaf8998bbdd8c~tplv-k3u1fbpfcp-zoom-1.image)

首先我们来安装一下 Jest 相关的依赖。

```
npm install --save-dev jest @types/jest @jest/types
```

安装好了以后，我们初始化一下 Jest 的 配置。

```
npx jest --init
```

可以参照下面进行选择。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93162d834f0f4de3aeb3c89547ca997c~tplv-k3u1fbpfcp-zoom-1.image)

这里简单解释一下我们为什么这么选：

-   前两个配置选项是字面意思，不赘述了。
-   单测环境（jsdom)：因为我们会涉及到 dom 的单测，不仅仅是纯逻辑，如果是纯逻辑的选 node。
-   是否需要覆盖率报告（no)：暂时用不上，后面覆盖率章节会着重介绍。
-   编译代码（babel)： 可以转 ES5，避免一些兼容性问题。
-   每次测试完是否清理 mock、实例等结果（yes): 每次测试完成后会清理 mock 等上次测试的结果，可以避免用例之间的互相影响

到这里我们 Jest 的基本配置就已经完成了，可以看到根目录已经生成了对应的 jest.config.ts 文件，大家也可以根据自己的需要增加额外的自定义配置，具体可以参考[ Configuring](https://jestjs.io/docs/configuration)。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ec402d7879b431bbbd87683a4aa8e23~tplv-k3u1fbpfcp-zoom-1.image)

因为我们选用了 babel 作为单测的编译，所以这边还需要增加一下对应的配置。

```
npm install --save-dev babel-jest @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript
```

这边除 babel 基础的配置集（presets)，我们还安装了 React 和 TypeScript 的配置集，来帮助我们的单测可以支持使用 ts 来书写，安装完成后，我们在根目录创建一个 babel.config.js 文件用于 babel 的配置，其中@babel/preset-react ，我们为它加上 `runtime: "automatic"`的配置，这是为了帮助我们可以自动导入 React，不然后续单测的开发会要求对 React 进行 import。

```
// ./babel.config.js
module.exports = {
  presets: [
    ["@babel/preset-env", { targets: { node: "current" } }],
    ["@babel/preset-react",{ runtime: "automatic" }], // 自动导入react
    "@babel/preset-typescript",
  ],
};
```

这时候我们新增一个单测实验一下，执行一下`npm run test`。

```
// App.test.ts
import React from "react";

test("test", () => {
  expect(1 + 1).toBe(2);
});
```

这时候发现会有 ts-node 需要安装的报错提醒。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/527c1f09c996450091fd6b0ffae7aab5~tplv-k3u1fbpfcp-zoom-1.image)

我们先来看一下 jest-config 的依赖配置，因为配置文件是 ts，所以需要依赖 ts-node 进行编译，如果子依赖中没直接包含的话，的确会有这样的问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/195f53a6171e49e99242502f02b092e0~tplv-k3u1fbpfcp-zoom-1.image)

的确和我们想的一样，那我们自己安装一下 ts-node 就好了。

```
npm install ts-node --save-dev
```

我们再试试看，可能会遇到下面的报错。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef616b5b412049848be57d9a0e32781d~tplv-k3u1fbpfcp-zoom-1.image)

和之前的原因类似，jest-environment-jsdom 也不会作为子依赖自动安装，我们自己安装一下就好。

```
npm install jest-environment-jsdom --save-dev
```

再试试看，发现还有一个问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a9b3825d5844a1e8662c6b76588fda4~tplv-k3u1fbpfcp-zoom-1.image)

这个是因为尤大的 vitejs 脚手架中，在 package.json 中设置了 `type: module`，这将指明这个包是采用何种方式进行导入的，针对`type: module`，babel.config 的后缀类型应该使用 cjs，改成如下图。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7afe7a3c04244117b66964416654eac0~tplv-k3u1fbpfcp-zoom-1.image)

如果没有这项的同学应该是正常的，就可以忽略了，如果大家这时候尝试一下 `npm run test`，会发现应该已经可以了，这些是基于 babel 的配置，[Jest 官网](https://jestjs.io/zh-Hans/docs/getting-started)也提供了 ts-jest 的配置方案，大家可以下来试试看。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28ce132050894d6290d6140bc86054d6~tplv-k3u1fbpfcp-zoom-1.image)

到这里，Jest 的基础配置就已经完成了，但是还有一些特殊情况，我们需要额外进行一些配置。

-   额外的扩展名识别：因为Jest 不使用 Webpack 等打包工具，因此它不知道如何加载除 js/jsx 之外的其他文件扩展名，所以我们需要为它加一个转换器。

```
// jest.config.ts
export default {
  // ... other config
  transform: {
    // ...
    "^.+\.(js|ts|tsx)$": "<rootDir>/node_modules/babel-jest",
  },
};
```

-   Svg mock 转换：我们项目中可能会有用到 svg 等图片，这个对于 Jest 同样也是无法识别的，我们需要对它进行 mock，返回相同的输出结果。

```
// jest.config.ts
export default {
  // ... other config
  transform: {
    // ...
    "^.+\.svg$": "<rootDir>/svg-transform.js",
  },
};
```

```
// ./svg-transform.js
export default {
  process() {
    return { code: "module.exports = {};" };
  },
  getCacheKey() {
    return "svgTransform"; // SVG固定返回这个字符串
  },
};
```

-   CSS 代理：Jest 本身不知道如何处理不同扩展的文件，我们可以通过配置代理的方式，告诉 Jest 将此对象模拟为导入的 CSS 模块。

```
npm install --save-dev identity-obj-proxy
```

```
// jest.config.ts
export default {
  // ... other config
  moduleNameMapper: {
    "\.(css|less)$": "identity-obj-proxy" // 有使用 sass 需求的同学可以把正则换成 ^\.(css|less|sass|scss)$
  }
};
```

大家做到这一步，可以`git init`一下，提交一个 commit 进行保存，下面我们将来配置辅助库。 因为 Jest 的配置都是相同的，后续大家在配置辅助库时，stash 一下之前的配置就可以重新开始了，会方便清晰很多。

### React Testing Library

> 配置可参考配置示例仓库 test_demo_for_config feat/react_testing_library 分支。

接下来我们来配置 React Testing Library，我们先来安装一下依赖，这几个库我们会在后面的课程中着重学习：

-   @testing-library/jest-dom：用于 dom、样式类型等元素的选取。
-   @testing-library/react：提供针对 React 的单测渲染能力。
-   @testing-library/user-event：用于单测场景下事件的模拟。

```
npm install @testing-library/jest-dom @testing-library/react @testing-library/user-event --save-dev
```

针对 @testing-library/jest-dom 我们全局导入一下，使得 expect 可以适配 React testing library 提供的相关断言，我们在根目录创建一个 jest-dom-setup.js (名字可自取)，用于全局导入 @testing-library/jest-dom。

```
//  jest_dom_setup.js
import '@testing-library/jest-dom'
```

然后我们将这个文件配置到 jest.config.ts 的 setupFilesAfterEnv 属性中，这个字段的作用是，将指定的配置文件，在安装测试框架之后，执行测试代码本身之前运行，这样我们就不需要每个单测文件都单独导入一次 @testing-library/jest-dom 了。

```
// jest.config.ts
export default {
  // ... other config
  setupFilesAfterEnv: ["<rootDir>/jest-dom-setup.js"],
};
```

到这里 React Testing Library 的配置就已经完成了，我们可以修改我们的单测来试验一下效果，可以看到已经可以了。

```
// ./src/App.test.tsx
// 这里文件后缀修改为 tsx，因为需要测试 dom
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import App from "./App";

describe("test", () => {
  test("first unit test", () => {
    render(<App />);
    expect(screen.getByText("Vite + React")).toBeInTheDocument();
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25ee1334f28e416aa4a0228bfbb43490~tplv-k3u1fbpfcp-zoom-1.image)

如果大家是使用 create-react-app 创建一个新项目的话，React Testing Library 的配置相比手工配置会方便很多，脚手架帮我们完成了 Jest 到 React Testing Library 所有的配置，我们打开终端执行下面的命令。

```
npm i create-react-app -g 
npx create-react-app test_demo --template typescript
```

执行完成后，会在对应目录下生成如下的项目结构。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7169869b1729424a84b9649eddddf8f4~tplv-k3u1fbpfcp-zoom-1.image)

其中包含`test`即为单测的文件，我们先来看下 package.json。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec2d159b089d48ebafd6f269783ed7fd~tplv-k3u1fbpfcp-zoom-1.image)

可以看到我们上面自己手动配置的依赖都有安装，比较奇怪的是，Jest 去哪里了，我们知道 React Testing Library 只是辅助库，单测基础库还是要使用到 Jest 的，我们到 package.json 中搜一下 `"jest"` 看看。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a78eeaa106f14f1b8b07686d5cf1a16b~tplv-k3u1fbpfcp-zoom-1.image)

可以看到 create-react-app 将 Jest 作为 react-scripts 这个依赖的子依赖单独打包进来了。现在我们来看看脚手架自动生成的单测，这个单测的效果是测试 App 组件下是否包含 learn react 的文案。

```
// ./src/App.test.tsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

我们可以尝试执行 script 中的 test 命令看下效果，可以看到用例通过的信息， create-react-app 其实还是很方便的，不需要我们再配置啥，可以很方便地开始单测地学习，后面的课程我们也会基于这个项目进一步展开。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62a0af0a7ad049048d205f770d6eb6ab~tplv-k3u1fbpfcp-zoom-1.image)

### Enzyme

> 配置可参考配置示例仓库 test_demo_for_config feat/enzyme 分支。

现在我们来配置 Enzyme， 首先我们来安装一下依赖，对于 Enzyme 我们需要安装三个依赖：

-   enzyme：基础库。
-   enzyme-adapter-react：对 React 的适配器，需要安装对应 React 版本的适配器。
-   jest-enzyme：用于 enzyme 对 Jest 的环境适配。

Enzyme 的使用是依赖于适配器（enzyme-adapter-react）的，大家如果到 npm 等[包管理平台](https://www.npmjs.com/search?q=enzyme-adapter-react-17)去搜索，会发现 Enzyme 适配的速度其实是要远慢于 React 的迭代速度的，从 React 17 开始，提供的适配器就已经是开发者自行实现的了，这是 Enzyme目前最大的问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/afb3d9ec1d3c4d5eb6cf99332d81cbc4~tplv-k3u1fbpfcp-zoom-1.image)

**这种稳定性可能没有办法得到有效的保证，对于新项目如果想体验 React 高版本所提供的一些优化（例如流式渲染），可能会遇到一些因没有完全适配而导致的问题**，并且更糟糕的是，目前 Enzyme 只剩一名开发者 [Jordan Harband](https://twitter.com/ljharb)来提供基础的维护，对于一些 issue 的解决可能没办法那么及时。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10af85d861d0481c862791127ef6ec29~tplv-k3u1fbpfcp-zoom-1.image)

因为 vitejs 脚手架初始的项目用的是 React 18，所以我们到包管理里搜一下[ star 最多的项目](https://www.npmjs.com/package/@cfaester/enzyme-adapter-react-18) 进行下载，可以看到 readme 里作者也直接说了这不是官方的，可能会有一些问题 =。=

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3eec6eddde748b882ad905c41ab1e8f~tplv-k3u1fbpfcp-zoom-1.image)

我们现在来安装一下依赖。

```
npm install enzyme @types/enzyme jest-enzyme @cfaester/enzyme-adapter-react-18 --save-dev
```

接下来，我们来创建 Enzyme 的实例，并通过 Jest 的 setupFiles 进行安装时的全局注入。

```
// ./enzyme_setup.ts
import Adapter from "@cfaester/enzyme-adapter-react-18";
import Enzyme from "enzyme";

Enzyme.configure({ adapter: new Adapter() });

export default Enzyme;
```

```
// ./jest.config.ts
export default {
  // ... other config
  setupFiles: ["<rootDir>/enzyme_setup.ts"],
};
```

Jest 环境适配的依赖，我们也需要同样配置到 config 中，把对应的入口文件导入就行。

```
// ./jest.config.ts
export default {
  // ... other config
  setupFilesAfterEnv: ["<rootDir>/node_modules/jest-enzyme/lib/index.js"],
};
```

到这里 Enzyme 的配置就完成了，我们写一条单测来试试。

```
// ./App.test.tsx
import { mount } from "enzyme";
import App from "./App";

describe("test", () => {
  it("first unit test", () => {
    const app = mount(<App />);
    expect(app.find(".read-the-docs").getDOMNode().textContent).toEqual(
      "Click on the Vite and React logos to learn more"
    );
  });
});
```

看错误栈可以看到，这个非官方的 React 18 适配器报错了，看样子是没有导入对应的全局依赖，我们切到对应的错误栈，帮它加一下试试。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f71f69ebbdd4364a79ae4acf6a5ba4b~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d6d80c994694102906829a7c5ee7faf~tplv-k3u1fbpfcp-zoom-1.image)

我们再试试看，看看有没有别的问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0c6f66197ec84934b76660e71cc4675d~tplv-k3u1fbpfcp-zoom-1.image)

这个是因为从 React 15.5.0 开始，PropTypes 已作为单独的依赖项从核心 React 包中删除，依赖包本身并没有去安装这个依赖，我们替它装一下。

```
npm install --save-dev prop-types
```

再试试看，发现已经可以了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d75d688a8d3c4c2ca16c9bf0c353ba07~tplv-k3u1fbpfcp-zoom-1.image)

如果大家要使用 18 版本的话，我建议 fork 这个依赖的仓库，然后按照我们上述进行微调后发包使用，或者给这个仓库提一个 mr 修复一下上述的问题都可。

如果是 React 17 版本应该就不会遇到上面的问题了，换用这个 [@wojtekmaj/enzyme-adapter-react-17](https://www.npmjs.com/package/@wojtekmaj/enzyme-adapter-react-17) 适配器即可，目前还没有发现什么问题，至于到 React16 版本及以前，就都是官方提供的适配器了，稳定性有保障，可以放心使用。

## 测试思路

不得不说我在进行小册技术选型的时候纠结了很久，因为历史原因，包括 Semi 在内的使用的其实都是 Enzyme，不可否认它是一个很优秀的辅助库，对于项目性能的维稳和日后迭代都提供了很大的助力和信心，如果说官方适配器没办法跟上 React 版本，非官方适配器稳定性又没有保障是导火索，那么测试思路就是使我最后决定的那根稻草。

Enzyme 允许访问组件的内部工作原理。我们可以读取和设置状态，并且可以模拟子项，以使测试运行得更快。所以Enzyme 的单元测试是基于 component 的 props 展开的，是从代码逻辑的层面验证组件，例如下面的例子。

```
it('input with custom className & style', () => {
    const wrapper = shallow(<Input className='test' style={{color: 'red'}}/>);
    expect(wrapper.exists('.test')).toEqual(true);
    expect(wrapper.find('div.test')).toHaveStyle('color', 'red');
 });
```

而 React Testing Library 采取完全不同的单测思路，它并不在意组件实现的细节，它的测试将基于组件能力本身，从用户视角去进行测试，例如脚手架生成的单测例子。

```
test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

就我看来，这两种方案其实各有优劣，Enzyme 所推崇的单测思路虽然在编写上会更麻烦，但是可以有效帮助开发审视自己的类名、结构等封装是否合理，尤其如果作为多业务线复用的组件，这个效果会更加明显，因为作为通用组件，类名等设计的是否合理，会决定到这个组件的复用程度（比如复用过程中 global 样式是否容易编写）。

但是从业务项目长久维护上看，Enzyme 的单测其实是一种**脆弱且不可靠的单测**，我们知道在业务代码中，产品需求可能是会频繁变动的，有些需求 pm 当时拍脑袋决定后，可能过段时间发现并不合理，进行调整或者推倒重来，这种情况是很常见的。

针对这种情况，从业务角度上，更需要关注的其实是历史功能是否可以得到完整保留，而不是组件本身的逻辑保持不变，对于业务项目，Enzyme 的单测注定会需要随需求频繁变动，这些时间成本其实都是研发人员难以接受的，我们更需要一个稳定可靠不经常变动的单测来协助我们。所以出于这方面的考虑，这本小册将使用 React Testing Library 来给大家展开单元测试的学习。

## 小结

这节课是我们单元测试章节的启蒙课，在这节课，我们了解到，**单元测试是从组件层面更细粒度展开的测试**，我们通常使用 Jest 作为我们展开单元测试的基础测试库，Jest 的配置相对还是比较繁琐的，大家可以参考下面的思维导图再整理一下思路。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb6a77c318b842d99929c69a69d33d79~tplv-k3u1fbpfcp-zoom-1.image)

因为前端需要模拟浏览器 DOM、事件的原因，所以我们还需要使用一个辅助库来协助我们进行浏览器环境的模拟。主流的库有 Enzyme 和 React Testing Library ，虽然它们都是优秀的单测辅助库，但是它们的思路不尽相同。

Enzyme 提供的能力让我们从组件逻辑细节来展开单测，对于需求频繁变动的场景，这是一种脆弱的单测，可能会需要开发人员频繁修改单元测试。而React Testing Library 并不在意组件实现的细节，是从组件能力本身去展开测试，这样对于代码组件层面的重构和优化，只要最后功能相同，单测将都可以复用，更适合业务场景。

同时考虑到 Enzyme 目前官方适配器更新缓慢，依赖社区非官方适配的原因，所以小册后面的学习，我们将使用 React Testing Library 来进行环境的模拟。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e8279b44fbd45db98158426e57f959b~tplv-k3u1fbpfcp-zoom-1.image)

下一节课，我们将来学习 Jest 的断言，通过它，能够告诉我们的单测程序什么是我们的预期。

## 3.Jest 断言：如何告诉程序什么是你的预期？

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们详细聊了技术选型，选用了 Jest + React Testing Library 来作为单元测试的技术栈，Jest 是一个 JavaScript 集大成的测试库，是我们单元测试的基础，而 React Testing Library 则提供了一些 React Component 的 Api ，来协助我们进行 React Dom 和事件相关的单测编写。

这节课将详细介绍我们是如何通过 Jest 来描述我们的预期的，在开始这节课的学习前，我们来看看上节写的单元测试。

```
// ./src/App.test.tsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

其中 test 用于定义单个的用例， 与此类似的还有 describe 和 it，describe 表示一组分组，其中可以包含多组 test，而 it 是 test 的别名，有相同的作用，例如上节课中 Enzyme 的例子。

```
// ./App.test.tsx
import { mount } from "enzyme";
import App from "./App";

describe("test", () => {
  it("first unit test", () => {
    const app = mount(<App />);
    expect(app.find(".read-the-docs").getDOMNode().textContent).toEqual(
      "Click on the Vite and React logos to learn more"
    );
  });
});
```

我们来看其中的 Callback 逻辑，在这则单测中我们判断了 Learn react 这则文案是否在我们的 DOM 中，`screen.getByText`用于元素的查找，是 React Testing Library 提供给我们的 API，这部分会在 [6 | DOM断言：页面元素的断言](https://juejin.cn/book/7174044519350927395/section/7176804322653503528) 详细举例介绍，我们这边不过多介绍。

```
expect(linkElement).toBeInTheDocument();
```

在选取完元素后，上面这行代码告诉了单测程序，我们希望选取的元素可以存在页面正文中。其实从语义上也很好理解，expect(期望）linkElement(这个元素）toBeInTheDocument（可以在页面正文）。

其中`expect`在我们后面的每次测试中都会频繁用到，其中的参数填入你需要进行判断的对象，`toBeInTheDocument` 这个 Api 是匹配器，也称断言，用来告诉程序你的预期是什么，通过对预期的对象进行断言就是单元测试的基本原理。

在 Jest 中有提供很多基础的断言，来帮助描述我们需求中的常见场景，这节课我们就先来学习 Jest 提供哪些断言的 Api 来帮助我们编写测试预期（`toBeInTheDocument`是React Testing Library 提供的额外断言 Api，我们在[6 | DOM断言：页面元素的断言](https://juejin.cn/book/7174044519350927395/section/7176804322653503528) 一起介绍）。

## Jest 常见断言场景

我根据常用断言的使用场景分成了以下六个方向：

| 场景方向    | 涉及的断言Api                                                                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| 基础类型的比较 | `not`  `toBe(value)`  `toBeTruthy(value)`  `toBeFalsy(value)`  `toBeDefined()`  `toBeUndefined()`  `toBeCloseTo(value)` `toBeNaN()` |
| 引用类型的比较 | `toEqual(value)` |                                                                                                                                 
| 数字符号    | `toBeGreaterThan(value)`  `toBeLessThan(value)`  `toBeGreaterThanOrEqual(value)`  `toBeLessThanOrEqual(value)`                              |
| 正则匹配    | `toMatch(value)`  `toMatchObject(value)`|                                                                                                        
| 表单验证    | `toContain(value)`  `arrayContaining(value)` `toContainEqual(value)`  `toHaveLength(value)`  `toHaveProperty(value)`                      |
| 错误抛出    | `toThrow()`  `toThrowError()` |                                                                                                                  

下面我们就按照上述方向，依次来学习以下对应断言的应用，首先我们在 src 目录下创建一个 __test__ 来存放我们纯逻辑的单测。

```
// ./src/__test__/expect.test.ts
import React from "react";

describe("examples for jest expect", () => {
    // ... 本节课后续的test就放在这里
});
```

### 基础类型的比较

我们知道，JavaScript 中分为基础类型和引用类型，其中基础类型中，大部分比较都可以通过 `toBe` 来完成，而`not`则用来表示非的判断，比如下面的简单例子。

```
// ./src/__test__/expect.test.ts
test("基础类型的比较", () => {
    // tobe
    expect(1 + 1).toBe(2);
    // not
    expect(1 + 1).not.toBe(3);
})
```

不仅是数字，包括 boolean 和 undefined 在内都是可以的。

```
// ./src/__test__/expect.test.ts
test("基础类型的比较", () => {
    // ...
    // boolean
    expect(true).toBe(true);
    // undefined
    expect(undefined).toBe(undefined); 
})
```

虽然这些可以通过 toBe 判断，但是同时 Jest 还提供了 4 个 API 来判断 true、 false、undefined、defined，效果与 toBe 来判断是都相同的。

```
// ./src/__test__/expect.test.ts
test("基础类型的比较", () => {
    // ...
    // boolean
    expect(true).toBe(true);
    expect(true).toBeTruthy();
    expect(false).toBeFalsy();
    // undefined
    expect(undefined).toBe(undefined);
    expect(undefined).not.toBeDefined();
    expect(undefined).toBeUndefined();
})
```

不仅是针对变量，对函数返回值的判断也是可以的，比如：

```
// ./src/__test__/expect.test.ts
test("基础类型的比较", () => {
    // ...
    // undefined
    const test = () => {
      console.log(test);
    };
    expect(test()).toBeUndefined();
})
```

虽然 toBe 的能力很强大，但是针对浮点类型就不行了，比如：

```
// ./src/__test__/expect.test.ts
test("基础类型的比较", () => {
    // ...
    // 浮点数
    expect(0.2 + 0.1).toBe(0.3);
})
```

针对这个用例，我们会得到下面的结果。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f978abe072014a10b50f95a0849291dc~tplv-k3u1fbpfcp-zoom-1.image)

这个倒不是 Jest 的原因，而是由于 JavaScript 本身的特性导致的，我们知道 JavaScript 中数字只有一个 number 类型，与 Java 等语言不同，JavaScript 并没有类似 float 或是 double 的浮点类型，浮点的实现都采用 double(双精度存储）。

大学时候计组课程我们学过，针对双精度存储，包含 8 个字节，也就是 64 位二进制（1 位符号位，11 位阶码（指数位），52 位尾数位），而十进制转二进制可能是除不尽的，52 位尾数位后面的位数就会被抹掉。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3fae277329c45f6975caa765fac5524~tplv-k3u1fbpfcp-zoom-1.image)

所以针对 0.1 + 0.2 的计算其实是这样的过程，首先需要把 0.1 和 0.2 转化成对应的二进制。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cf227e85559421ba728236d150e511c~tplv-k3u1fbpfcp-zoom-1.image)

这样加起来得到的结果就是 0.0100110011001100110011001100110011001100110011001101，因为上面我们说过 JavaScript 是会把 52位尾数后的内容抹掉的，所以这个结果并不是完全精准的，转换为十进制就是 0.30000000000000004，所以没办法全等。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47631ca418a647b9ad044db5d58c0b3e~tplv-k3u1fbpfcp-zoom-1.image)

所以针对浮点数的比较，Jest 有提供一个专门的断言来进行判断，那就是 toBeCloseTo，和它的字面意思相同，这个断言用来判断对象和预期的精度是否足够接近，而不再是全等，例如下面的例子：

```
// ./src/__test__/expect.test.ts
test("基础类型的比较", () => {
    // ...
    // 浮点数
    expect(0.2 + 0.1).toBe(0.3);
    expect(0.2 + 0.1).toBeCloseTo(0.3);
})
```

这样看下来，toBe 是不是和我们平时常用的 === 很像，不过严格意义上说，toBe 的效果并不等同于 全等===， **它是一种更加精确的匹配，应该说等同于 Object.is**，这个是 ES6 提供的新方法，相比 ===， 它修复了 JavaScript 历史的两个问题，NaN 和 +(-)0 。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e19bb9320bfc4d798202b6357b0edb7d~tplv-k3u1fbpfcp-zoom-1.image)

对于 Object.is 这两个不合理的判断都得到了修复。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9d5a0250352438e817f18e99b45931a~tplv-k3u1fbpfcp-zoom-1.image)

针对这两个场景，我们可以写如下的断言，其中`toBeNaN` 也是 Jest 提供的额外基础断言 API，效果上与`toBe(NaN)` 也是相同的。

```
// ./src/__test__/expect.test.ts
test("基础类型的比较", () => {
    // ...
    // NaN
    expect(NaN).toBe(NaN);
    expect(NaN).toBeNaN();
    // +0 -0
    expect(+0).not.toBe(-0);
})
```

### 引用类型的比较

除了基础类型外，我们知道 JavaScript 还有引用类型，与基础类型不同的是，引用类型的全等，是对引用类型的内存指针进行比较，对于深拷贝或是属性完全相同的对象，使用 toBe 的断言是不能满足预期的，所以 Jest 有专门为这类情况提供断言 toEqual(value)，相比 toBe，toEqual 会深度递归对象的每个属性，进行深度比较，只要原始值相同，那就可以通过断言。我们来看下面的例子。

```
// ./src/__test__/expect.test.ts
test("引用类型的比较", () => {
    const a = { obj1: { name: "obj1", obj2: { name: "obj2" } } };
    const b = Object.assign(a);
    const c = JSON.parse(JSON.stringify(a));
    expect(a).toBe(b);
    expect(a).not.toBe(c);
    expect(a).toEqual(b);
    expect(a).toEqual(c);
})
```

其中有 a, b, c 三个对象，b 对象是基于 a 对象的浅拷贝，而 c 对象是基于 a 对象的深拷贝，我们可以看到，a 和 b 是可以通过 toBe 来验证的，因为它们指向同一个内存指针，而 c 是完全开创出来的独立的内存空间，所以不能用全等进行验证，这里我们采用 toEqual 进行验证。

值得一提的是，toEqual 能不能用于验证基础类型呢？也是可以的，我们看下面的例子。

```
// ./src/__test__/expect.test.ts
test("引用类型的比较", () => {
    // ...
    expect(1 + 1).toEqual(2);
})
```

我们上面有提到，toEqual 是采用深度递归的方式进行的原始值比较，虽然基础类型本身并不是对象，但是在对它们的 proto 进行递归比较的时候，会调用它们对应的包装类型创建实例，实例本身是可以作为对象进行比较的，所以 toEqual 同样可以用于基础类型的比较，比较的结果预期将是所有递归属性的值相等。

### 数字符号

我们在书写单测验证一些场景的时候，经常会有数字值比较的需求，比如 > ， < 等，这些也有对应的基础断言可以进行验证，比较简单就不过多讲解了，大家可以看看下面的例子。

```
// ./src/__test__/expect.test.ts
test("数字符号", () => {
    // >
    expect(3).toBeGreaterThan(2);
    // <
    expect(3).toBeLessThan(4);
    // >=
    expect(3).toBeGreaterThanOrEqual(3);
    expect(3).toBeGreaterThanOrEqual(2);
    // <=
    expect(3).toBeLessThanOrEqual(3);
    expect(3).toBeLessThanOrEqual(4);
  });
```

### 正则匹配

正则匹配同样也是我们开发中比较常见的场景，针对这个场景，Jest 断言中有两个常用的匹配器会经常使用，分别是 `toMatch(regexp)` 和 `toMatchObj(value)`，其中 `toMatch(regexp)` 会匹配字符串是否能够满足正则的验证，而`toMatchObj(value)`则用来验证对象能否包含 value 的全部属性，即 value 是否是匹配对象的子集，我们来看下面的例子。

```
// ./src/__test__/expect.test.ts
test("正则匹配", () => {
    expect("This is a regexp validation").toMatch(/regexp/);
    const obj = { prop1: "test", prop2: "regexp validation" };
    const childObj = { prop1: "test" };
    expect(obj).toMatchObject(childObj);
  });
```

其中“This is a regexp validation” 包含 “regexp”字符串，childObj 也作为 obj 的子集，所以这个验证是可以通过的。

### 表单验证

我们在需求中经常会有很多表单，对于表单值的判断也是一个很常遇到的场景，表单验证中我们经常会有值为数组或是对象的判定，所以验证某个字段是否在对象或者数组中是很有必要的。表单验证中也有提供对应能力的断言：

-   `toContain(value)` ：判定某个值是否存在在数组中。
-   `arrayContaining(value)`：匹配接收到的数组，与 toEqual 结合使用可以用于判定某个数组是否是另一个数组的子集。
-   `toContainEqual(value)` ：用于判定某个对象元素是否在数组中。
-   `toHaveLength(value)`：断言数组的长度 。
-   `toHaveProperty(value)`：断言对象中是否包含某个属性，针对多层级的对象可以通过 xx.yy 的方式进行传参断言。

我们来结合下面的例子具体说明：

```
// ./src/__test__/expect.test.ts
test("表单验证", () => {
    // 数组元素验证
    expect([1, 2, 3]).toContain(1);
    expect([1, 2, 3]).toEqual(expect.arrayContaining([1, 2]));
    expect([{ a: 1, b: 2 }]).toContainEqual({ a: 1, b: 2 });
    // 数组长度
    expect([1, 2, 3]).toHaveLength(3);
    // 对象属性验证
    const testObj = {
      prop1: 1,
      prop2: {
        child1: 2,
        child2: "test",
      },
    };
    expect(testObj).toHaveProperty("prop1");
    expect(testObj).toHaveProperty("prop2.child1");
  });
```

在上面的例子中，我们分别对基础元素、数组子集、对象子集的包含关系、数组长度、对象包含的属性进行了断言，对于复合属性断言的场景，我们可以采用类似 `expect(testObj).toHaveProperty("prop2.child1")`的方式进行传参，用 . 来体现对应的层级关系即可。

值得一提的是，`expect([1, 2, 3]).toEqual(expect.arrayContaining([1, 2]));`与之前的断言不同，我们使用`expect.arrayContaining([1, 2])`来替代了文字值，也就是能匹配所有能够涵括它的数组。只要 [1, 2] 是数组 A 的子集，那么数组 A 就可以成为 `arrayContaining` 的匹配对象。

### 错误抛出

最后一个要介绍的场景就是错误抛出，无论是业务或是基础组件代码，错误抛出都是一个常见的场景，对于这些异常情况的断言，也是我们单元测试的一个重要部分。针对这种场景，Jest 提供了 `toThrow` 和 `toThrowError` 两个匹配器，这两个匹配器能力都相同，`toThrowError` 可以理解成是 `toThrow` 的一个别名，我们来看下面的例子。

```
// ./src/__test__/expect.test.ts
test("错误抛出", () => {
    const throwError = () => {
      const err = new Error("console err: this is a test error!");
      throw err;
    };
    expect(throwError).toThrow();
    expect(throwError).toThrowError();

    const catchError = () => {
      try {
        const err = new Error("console err: this is a test error!");
        throw err;
      } catch (err) {
        console.log(err);
      }
    };
    expect(catchError).not.toThrow();
    expect(catchError).not.toThrowError();
  });
```

对于上面的例子，值得一提的是`expect(throwError).toThrow();`中，throwError方法只需要传入即可，不需要执行，即`expect(throwError).toThrow();`，直接执行会抛出未捕获的错误，中断后续的测试进程。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b8835a12dea4f2d86da86df54283ab2~tplv-k3u1fbpfcp-zoom-1.image)

如果我们在方法中，已经有了错误的捕获，那么断言本身是无法生效的，这个大家需要注意一下。

## 自定义断言

上文我们已经针对常见的断言场景，介绍了 Jest 提供的一些常用的匹配器 API，当然官方还提供了一些别的匹配器，不过在日常需求中并不常用，感兴趣的同步可以移步[官网](https://jestjs.io/docs/expect#expectarraycontainingarray)了解更多。

除了基础的已经定义好的断言 API，Jest 也支持我们自定义断言匹配器，来覆盖基础的断言不能覆盖到的特殊业务场景，我们可以使用 Expect.extend 来自定义断言，我们先通过这个 API 的类型，来对它的能力有个初步的了解。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/194ab4b520474c2d9c29d0cb53ff8396~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cec6d70ee244136958845c7f8091d8e~tplv-k3u1fbpfcp-zoom-1.image)

可以看到 `extend` 可以接收一个 key - matcher 的映射 map，不难猜到，key 是自定义匹配器的名称，而 CustomMatcher 则对应匹配器的定义。通过 CustomMatcher 的类型定义我们可以看到，自定义匹配器包含同步（CustomeMatcherResult) 和 异步（Promise<CustomMatcherResult>)两种，它们都接收类型为 ` { pass: boolean; message: () => string }  `的返回值，其中 pass 表示这个断言是否通过，而 message 则作为这个结果的备注信息。

我们首先来尝试定义一个同步的匹配器，想象一个场景，假如我们需要断言一个数字是否在 0 到 10 之间，应该怎么实现这个匹配器呢？我们来看下面的例子。

```
// ./src/__test__/expect.test.ts
test("同步自定义匹配器", () => {
    const toBeBetweenZeroAndTen = (num: number) => {
      if (num >= 0 && num <= 10) {
        return {
          message: () => "",
          pass: true,
        };
      } else {
        return {
          message: () => "expected num to be a number between zero and ten",
          pass: false,
        };
      }
    };
    expect.extend({
      toBeBetweenZeroAndTen,
    });
    expect(8).toBeBetweenZeroAndTen();
    expect(11).not.toBeBetweenZeroAndTen();
  });
```

可以看到同步匹配器的实现很简单，我们只需要在我们预期的判断逻辑中返回对应的结构体，然后将对应的匹配器方法传给 extend 后，就可以通过 expect 来调用对应的匹配器了。现在我们来改造一下这个匹配器，使得它可以支持异步的场景。

```
// ./src/__test__/expect.test.ts
test("异步自定义匹配器", async () => {
    const toBeBetweenZeroAndTen = async (num: number) => {
      const res = await new Promise<{ message: () => string; pass: boolean }>(
        (resolve) => {
          setTimeout(() => {
            if (num >= 0 && num <= 10) {
              resolve({
                message: () => "",
                pass: true,
              });
            } else {
              resolve({
                message: () =>
                  "expected num to be a number between zero and ten",
                pass: false,
              });
            }
          }, 1000);
        }
      );
      return (
        res || {
          message: () => "expected num to be a number between zero and ten",
          pass: false,
        }
      );
    };
    expect.extend({
      toBeBetweenZeroAndTen,
    });
    await expect(8).toBeBetweenZeroAndTen();
    await expect(11).not.toBeBetweenZeroAndTen();
  });
```

可以看到，异步场景只是在同步的基础上加上了 async/await 相关的逻辑，然后在 expect 调用对应匹配器的时候，使用 await 等待结果返回即可。

## 怎么调试单测程序？

上文我们介绍了 Jest 提供的常用断言匹配器，以及如何自定义一个断言匹配器，这里加一个小彩蛋，很多同学可能并不知道怎么调试测试代码，与业务逻辑不同，测试代码运行在 node，所以并不能通过浏览器 console 调试，我们可以采用和调试 node 服务相同的方式来调试我们的单测程序。下面简单举例说明一下。

首先我们在需要断点的位置写入 debugger，或是在左侧点击断点红点都可。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b7c09738b4e4980af773dabb6009bdf~tplv-k3u1fbpfcp-zoom-1.image)

然后通过 vscode JavaScript 调试终端而非普通运行终端，运行对应的单测命令。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c06c29c9e567412186e8c53edc333ef8~tplv-k3u1fbpfcp-zoom-1.image)

可以看到对应断点处就已经停顿下来了，并且可以在左侧视图层看到当前状态下的变量值，顶部也会有步进等调试的按钮，后面我们就像平时调试代码一样正常调试代码就好了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ce534ab89fb4c62a7dd15f1ad60a11c~tplv-k3u1fbpfcp-zoom-1.image)

## 小结

这节课我们学习了怎么告诉测试程序你的预期，我们通过不同的断言来对每个需要验证的对象提出自己的预期，当断言的结果与预期不符的时候，测试程序就会将错误和未通过的用例反馈给你。

针对断言有很多种类，我们基于场景分类，分别学习了基础类型比较，引用类型比较、数字符号、正则匹配等常见的 Jest 断言匹配器。同时我们还尝试自己自定义了断言匹配器，来覆盖基础断言器不足以满意的业务需求。

最后我们还了解了怎么去测试一个单测程序，因为与常规业务代码不同，测试程序执行于 node 环境，所以我们采用开发 node 服务类似的调试方式对测试用例进行调试。

相信经过这节课的学习，同学们已经入门了对纯逻辑的单元测试进行用例的编写，但是这样还远远不够，因为我们的单元测试主要还是覆盖于包含 DOM 的组件场景下，下一节课，我们将来学习 React Testing Library 给我们提供的 DOM 扩展能力，掌握如何对期望 DOM 区域进行选取。

## 4.DOM 查询（上）：页面元素的渲染和行为查询

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了如何告诉程序什么是我们的预期，在单测程序中，每一个预期都通过断言的方式来说明，Jest 提供了很多基础的断言来帮助描述程序中可能存在的不同场景，但是 Jest 的基础断言通常用于纯 JavaScript 逻辑的断言，例如 node 服务的函数。

但是面对业务场景，我们的逻辑中不可避免会涉及 Dom 元素的选取，也就是所谓的 UI 自动化，面对这种场景，我们需要对页面元素进行渲染 、 查询，然后再对结果进行断言，仅通过 Jest 就没办法满足我们的需求了，需要 React Testing Library 的帮助，这节课我们就来学习，如何对 DOM 元素进行渲染、查询。

## 页面元素的渲染

首先还是回到我们最初的例子：

```
test("renders learn react link", () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});
```

@testing-library/react 这个依赖提供了一些处理 React Component 的 API，其中 render 方法用于元素的渲染，并且在 render 执行过后会把值注入到 screen对象中。像上面这个例子中，使用 screen 来选取我们需要的元素，其中 `getByText` 是 React Testing Library 提供的查询 API，我们一会着重介绍。

以上面的例子举例，除了通过 screen 选取元素，还可以直接通过 render 来选取。

```
const linkElementByScreen = screen.getByText(/learn react/i);
const { getByText }  = render(<App />);
const linkElementByRender = getByText(/learn react/i);
```

这两种写法都可以获取到需要的元素，那它们之间有什么区别吗？

> The benefit of using `screen` is you no longer need to keep the `render` call destructure up-to-date as you add/remove the queries you need. You only need to type `screen.` and let your editor's magic autocomplete take care of the rest.

上面是作者对于这个问题的解释，翻译一下是这样的：

> 使用屏幕的好处是，您不再需要在添加/删除所需查询时，保持渲染调用的解构是最新的。您只需要输入屏幕，让您的编辑器神奇地自动完成功能来处理其余的事情。

这样直接看大家可能还不是很理解，我们可以结合[源码](https://github1s.com/testing-library/dom-testing-library/blob/HEAD/src/screen.ts#L5)来一起理解一下这句话。

这是 render 方法的定义：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd6496da906a4f2f8ec162c8155c0646~tplv-k3u1fbpfcp-zoom-1.image)

这是 screen 方法的定义：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b819082906a49c9aebe320b93be9367~tplv-k3u1fbpfcp-zoom-1.image)

它们都有使用`  getQueriesForElement ` 方法，这个方法是为了获取指定元素下的查询，作者有将 role， text 等类别的查询通过这种方式暴露出来。

我们再来具体看这两个方法做了什么，render 方法首先会创建一个元素，并写入到 innerHTML 中，然后再去获取我们传入的组件（html 参数）下的查询对象，并暴露出来，而 screen 方法则是在 document.body 存在的时候，获取 document.body 下的查询进行暴露。

这里的`  document.body ` 和 html 参数其实是同步的，只不过在基础上包了一层 `<body></body>`，这么看来好像只是把查询的字段放在全局进行导出了，这么做的意义是什么呢？综合来讲是两个原因：

-   Render 方法的主要意义其实是渲染，虽然它也会暴露出查询的 API，但这个 API 和 渲染其实是没有关系的，所以把查询作为一个独立的全局对象 screen 暴露出来，可以有效区分渲染和查询的界限，这样从测试项目的结构上来说是更清晰的；

-   另外一个重要的原因是，DOM 相关的查询 API 是比较多的，采用解构的方式很容易就出现下面的写法，我们不得不在每个 test 中重复解构。

```
import {render} from '@testing-library/react'

test('test 1', () => {
  const {queryByLabelText, getByText, getByLabelText} = render(<Thing />)
})

test('test 2', () => {
  const {getByLabelText, queryByLabelText} = render(<Thing />)
})

test('test 3', () => {
  const {getByLabelText, queryByLabelText} = render(<Thing />)
})

test('test 4', () => {
  const {getByLabelText, queryByLabelText} = render(<Thing />)
})
 ```
 这种解构其实是重复的，且与实际测试的逻辑的确半毛钱关系都没有，相比之下 screen 的写法要清晰舒服很多。
 ```
test("test", () => {
  render(<App />);
  screen[...] // 需要啥用啥
}
```
所以我们在写 DOM 相关的单测时，更建议大家采用 screen 来获取 DOM 的 container 来查询，额外值得一提的是，render 函数需要放在每个独立的 test 中，因为在每个 test 执行完以后， React Testing Library 会调用 cleanup 方法来清理环境，例如下面的写法，会导致后面的 test 不能读到元素，**这是一个常见的问题，大家需要注意一下**。
 ```
import React from "react";
import { render, screen } from "@testing-library/react";
import App from "./App";

render(<App />)

describe("tests", () => {
  test("test1", () => {
    // ...
  });

  test("test2", () => {
    screen.debug(); // ... 会读不到元素，仅剩body
  });
});
 ```

## 页面元素的查询

渲染完组件元素后，我们需要对组件进行查询，从而选取到我们需要的区域，React Testing Library 提供的查询 API 很多，但是可以从行为和参照物两个维度进行拆分理解，这节课我们先来学习行为维护的分类。

从行为角度上，查询 API 可以包含三种类别（getBy, queryBy, findBy），它们各自又包含单查和多查，也就是（getBy, queryBy, findBy, getAllBy, queryAllBy, findAllBy)，其中同一种类别的能力类似，区别只在于查询的数量，比如 getBy 和 getAllBy 在 API 的表述上就是近似的，大家可以参照下图来初步理解。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/011bb6c212604a0ead3a6cad0f1ee9c6~tplv-k3u1fbpfcp-zoom-1.image)

其中针对三种类别，它们之间的区别在于：

-   Get：返回查询的匹配节点，如果没元素匹配，则会报错（针对单查如果查到多个也会报错）；
-   Query：返回查询的匹配节点，如果没有元素匹配会返回 null，但是不会报错（同样针对单查，如果查到多个匹配元素也会报错）
-   Find：返回一个 Promise，默认超时时间为 1000 ms， 如果没有元素匹配或者查找超时，Promise 状态切为 reject（同样针对单查，如果查到多个元素，也会返回 reject）。

find 方法我们会在[8 | Async 异步：异步方法如何进行单测？](https://juejin.cn/book/7174044519350927395/section/7176612133516345378) 详细介绍，这节课我们先来学习 get 和 query 的类别。以我们之前使用过的 text 来举例说明，可以创建一个组件作为我们这部分的测试。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      <div>test1</div>
      <div>test2</div>
    </div>
  );
};
```

然后我们加上这样一条单测：

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  test("get & query & find", () => {
    render(<DomQuery />);
    const element = screen.getByText(/test/i);
    screen.debug(element);
  });
});
```

其中 screen.debug 是暴露出来的一个调试 API，可以帮我们将查询出来的元素在控制台中显示出来，我们可以看看效果，发现会抛出找到多个元素的错误，getBy 是没办法直接查询多个的，我们换用 query 或是 find 也会有相同的效果。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae998700185c4fca9eaca53db01e3ca6~tplv-k3u1fbpfcp-zoom-1.image)

在这个基础上，再来丰富一下我们的例子，将用例调整为下面的代码，然后在最后一行加上断点，然后用 debugger 终端执行看看。

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  test("get & query & find", () => {
    render(<DomQuery />);
    const getElement = screen.getByText("test1");
    const getAllElement = screen.getAllByText(/test/i);
    const queryElement = screen.queryByText("test3");
    const queryAllElement = screen.queryAllByText("test3");
    debugger;
  });
});
```

大家可以先根据之前学的理论判断一下预期的结果是什么。query 相比 get 不同的是，它在没匹配到对应元素时，并不会抛出错误，而是返回 null 或是 []，那么这个结果其实应该是`  htmlDivElement, [htmlDivElement, htmlDivElement], null, [] `，我们来看看结果是不是和我们想的一样。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52048a9fa1e34be0b6e2cd9618947b44~tplv-k3u1fbpfcp-zoom-1.image)

相信到这里大家就已经熟悉 get 和 query 以及单查和多查的区别了，那么什么场景下我们应该用 get， 什么场景下我们用 query 呢？

如果说这个元素的存在与否，并不决定这个用例能不能通过，或者说，这个元素不存在，也并不影响这个用例通过的话，我们应该使用 query。如果说这个元素不存在，那么后续的步骤就没有执行的意义，这个用例就是不通过的，我们应该使用 get，因为 get 会抛出错误，直接中断这个用例。

在上面的例子中，我们后缀使用的是 text，这是一种通过标签文本作为参照物的方式，除了这种以外， React Testing Library 还涉及其余 7 种参照物的查询方式，因为文章篇幅的关系，我们将在下一节课继续学习。

## 小结

这节课我们学习了 DOM 查询的上篇 - 页面元素的渲染和行为查询。对于页面元素的渲染，通常采用 render ，这个函数会返回给我们需要的查询，因为考虑到重复解构的原因，React Testing Library 有在全局暴露一个 screen 对象，当我们调用 render 方法后，它会注入 element 到页面的 innerHtml 中，而 screen 则会针对页面 body 区域获取查询，并暴露给我们 body 区域的查询API。

针对查询的部分，我们按照行为和参照物进行了分类，行为上我们分为了 get、 query 和 find 三种类别，其中 get 获取不到元素会抛出错误，而 query 获取不到则是返空，对于 find 则采取异步返回 reject。

在实际场景的应用中，如果元素获取不到，并不意味着这条用例失败，我们可以使用 query 来进行获取，因为 get 抛出的错误也会中断这条用例的执行。我们还学习了单查和多查两种情况的区别，当使用单查 API 查询到多个匹配元素的时候，也会抛出对应的错误来中断用例。

同时我们还接触到了第一个参照物 text， 这是一种通过标签文本作为参照物的方式，除此之外，其实还有其余的 7 种参照物，再考虑到查询行为的三种分类，单查和多查的场景，涉及到的实际 API 有8*3*2 = 48 种之多，那么，应该如何有效排列这些查询方式的优先级，并且在合适的场景使用呢？这些我们都将在下节课详细讨论。

## 5.DOM 查询（下）：页面元素的参照物查询和优先级

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了页面元素的渲染和行为查询，使用了 render 进行我们组件的渲染，并且从 screen 对象中获取到了 document.body 的区域查询。对于查询 API，种类繁多，上节课我们已经就查询 API 的行为，也就是前缀进行了分类，分别学习了单查和多查下的 get、query，但其实查询的 API 类型还远不止此。

我们已经接触到了 text，这就是我们将要介绍的参照物分类。虽然查询的 API 数量很多，但是我们可以根据维度来拆分。

上节课我们根据行为来分类，已经将 API 归为了 get、 find、 query 三类，这个决定了查询 API 命名的前缀。而查询的参照物决定了 API 的后缀是什么，以 getByText 为例，它使用 get 的查询行为，以 Text 为查询的参照物进行单查，可以看到这样分类，几十种 API 也可以快速理解到它们各自的用途。

那么查询的参照物有几种呢？大家可以结合下图初步理解。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e500a62675d44b0a8cfc8339084e8119~tplv-k3u1fbpfcp-zoom-1.image)

## 按照参照物分类

如果用过 Enzyme 的同学应该比较清楚，在 Enzyme 中，我们选取元素是采用 CSS 类或者 id 作为参照物，大家可能很奇怪这些参照物是什么？直接用 CSS 类或者 id 来选取不是更方便精准吗？

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a261a2c328f4d7da40807dc9954e5db~tplv-k3u1fbpfcp-zoom-1.image)

在 [2 | 技术选型：React Testing Library Or Enzyme？](https://juejin.cn/book/7174044519350927395/section/7176612133294063668) 我们就有介绍，React Testing Library 是站在用户视角进行测试，CSS 类名等则是针对代码细节的单测。《Google 软件测试之道》中有提到，测试用例和软件的使用方式越相近，就是越稳健的测试。这也是 React Testing Library 并不建议以代码细节作为参照物的原因，这些从用户视角并不容易感知到，容易导致用例脆弱、不稳定。

言归正传，我们来看下 React Testing Library 提供的查询参照物，首先看下 role（角色），这个是我们最常用的参照物，着重讲解这一块，通过这个可以选取几乎任何我们需要的元素。

那么什么是角色呢？要理解角色的含义，首先我们需要来了解一个 W3C 语义 ---- ARIA。

> ARIA (Accessible Rich Internet Applications) 是一组属性，用于定义使残障人士更容易访问 Web 内容和 Web 应用程序（尤其是使用 JavaScript 开发的应用程序）的方法。

简单来说，我们使用的 div、button 等标签，即使没有加任何属性，也有一个隐性的 ARIA role 属性来表示它的语义，就拿 button 为例，`<button>按钮</button>` 其实可以看作是`  <button role="button">按钮</button> `，这个就是 role 查询。

下面列举一些常用的 div 和它们的隐藏 role ，更详细的隐藏 role 属性大家可以看 [W3C 对应的提案](https://www.w3.org/TR/html-aria/#index-aria-button)。

| 标签                              | 隐性 ARIA role |
| ------------------------------- | ------------ |
| a , href                        | link         |
| a （没有 href 属性）, body, div, span | generic      |
| form                            | form         |
| h1 到 h6                         | heading      |
| html                            | document     |
| img                             | img          |
| p                               | paragraph    |
| table                           | table        |
| ul                              | list         |
| li                              | listitem     |

我们来试验一下，通过默认的 role 能否查询到对应的元素呢？我们给 App.tsx 加一个 button，然后扩展一下之前的测试用例。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <button>按钮</button>
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...

  test("default role", () => {
    render(<App />);
    const button = screen.getByRole("button");
    screen.debug(button);
  });
});
```

运行看一下控制台输出了什么，可以看到，会选取到我们新增的 button 元素。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e725bf72f2eb4d029b8d87b6a964be88~tplv-k3u1fbpfcp-zoom-1.image)

除了默认的 role，我们也可以自己加 role 对标签进行覆盖，比如下面的例子。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <button role="tab">自定义按钮</button>
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
  test("defined role", () => {
    render(<App />);
    const button = screen.getByRole("tab");
    screen.debug(button);
  });
});
```

可以看到，控制台可以输出`自定义按钮`，自定义的 role 可以对默认的 role 属性进行覆盖，不过值得一提的是，**我们不应该为了选取方便就错误或者重复添加 role**，除非是一个自定义的 UI 组件，不然大部分我们需要定位的场景其实都是有默认的 ARIA 语义的。

那么就会存在一个问题了，既然说 role 可以选取到大部分我们需要的场景，那么对于多个相同 role 的元素，我们怎么选取需要的那一个呢，难道只能重复加 role 来新增角色选取么？

事实上除了基础的角色 role 外，W3C 在 ARIA 语义的提案中还包含了 aria 属性，这个语义表明 role 语义的状态和属性，比如 “按压” 的 button， "隐藏" 的 button 等。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/373bff7370624c18998cdc37f27bc907~tplv-k3u1fbpfcp-zoom-1.image)

我们先来看下面的例子，理解一下 aria 属性的作用，以及是怎么和 role 配合使用的。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <button aria-pressed></button>
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
  test("aria", () => {
    render(<App />);
    const button = screen.getByRole("button", { pressed: true });
    screen.debug(button);
  });
});
```

可以看到控制台中将输出具备 `aria-pressed` 属性的 button。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a245aeb53c34cd0a288115faab0603a~tplv-k3u1fbpfcp-zoom-1.image)

aria 属性用来表示对应角色下的额外特殊含义，可以帮助我们在多个相同角色中选中我们需要的那一个，role 查询支持包含`aria-pressed` 在内的 7 种筛选项，它们在 W3C 提案中是这样含义的：

-   `aria-hidden`： 不在 DOM 树上访问的元素；
-   `aria-selected`: 元素是否被选中；
-   `aria-checked`: 元素是否被勾选；
-   `aria-current`: 当前选中的元素；
-   `aria-pressed`: 被按压的元素；
-   `aria-expanded`:元素是否被展开；
-   `aria-level`: 区域的等级，值得一提的是，h1 - h6 会有默认的`aria-level`属性，值对应1-6；
-   `aria-describedby`: 可以通过描述来定位额外的元素。

再次强调一下， aria 属性并不会对显示造成影响，只是语义上的属性。下面我们以 `aria-describedby` 为例，看看 aria 属性是怎么应用的。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <button aria-describedby="description">
          <div id="description">自定义aria按钮</div>
        </button>
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
  test("aria-describedby", () => {
    render(<App />);
    const button = screen.getByRole("button", {
      description: "自定义aria按钮",
    });
    screen.debug(button);
  });
});
```

控制台输出了自定义 aria 按钮的模块，`aria-describedby` 提供了更多的可能性，使得我们可以通过属性外的描述性文案来对应指定的元素。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed433613bf7c4889b1713e60ab0c65b8~tplv-k3u1fbpfcp-zoom-1.image)

除了官方文档中的这 8 种以外，其实还有一个筛选项 name，没有在官网中提及，但是，是一个非常有用的筛选项。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da3d2adb1ff441b3aa7332f09bf958b9~tplv-k3u1fbpfcp-zoom-1.image)

这个筛选项可以查询可访问的名称，比如标签、文本内容，或者是`aria-label` 属性，通常我们业务查询中，当某一个角色数量很多，但是又不好通过别的属性来筛选时，我们就可以通过这个和 `aria-label`配合使用来筛选出我们需要的内容，比如下面的例子：

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <div aria-label="test_note">1234</div>
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
  test("aria-label", () => {
    render(<DomQuery />);
    const note = screen.getByRole("generic", { name: "test_note" });
    screen.debug(note);
  });
});
```

最重要的 role 查询到这里就介绍完了，虽然说 role 的确可以选中所有预期的元素，但是 role 和 aria 的属性比较多，加上国内非障碍网页应用得不多，所以大家可能记不住，React Testing Library 还提供了其他的几种参照物来协助筛选，在一些特定的场景下使用，往往会有奇效。

-   标签文本(labelText)：针对 label 标签的 text 查询，通过这个可以查询到对应 label 的输入节点（比如 input)，我们来看下面的例子。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <label>
        testLabel
        <input />
      </label>
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
   test("labelText", () => {
    render(<DomQuery />);
    const label = screen.getByLabelText("testLabel");
    screen.debug(label);
  });
});
```

控制台输出出来，可以看到，将会输出这个 label 所对应的输入，也就是`<input />`。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d77fa23dabb84ebdaa429896ebe693d9~tplv-k3u1fbpfcp-zoom-1.image)

-   占位符文本（placeholdertext）： 通过 placeholder 来查询，也可以有效查到对应的表单元素，如果你没有使用 label 标签的时候，可以使用这个来作为替代，来看下面的例子。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <input placeholder="a query by placeholder" />
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
   test("placeholder", () => {
    render(<DomQuery />);
    const placeholderInput = screen.getByPlaceholderText(
      "a query by placeholder"
    );
    screen.debug(placeholderInput);
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f841e9a1c1e34900a07cb2848f66bfb3~tplv-k3u1fbpfcp-zoom-1.image)

-   文本（text): 我们之前例子用过很多次的老朋友了，直接通过标签中间的文本来查找，大家可以参考之前 test1 的那个用例，这边就不再举例了。
-   表单value(displayValue): 根据表单元素的值来查询，也就是对应的 value 属性，当然不仅仅是通过value，表单 onchange 进来或者是 defaultValue 也是同样可以生效的，我们来看下面的例子。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <input defaultValue="a query by value" readOnly />
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
   test("value", () => {
    render(<DomQuery />);
    const valueInput = screen.getByDisplayValue("a query by value");
    screen.debug(valueInput);
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9e24d79e19d4213a72b34643cb47289~tplv-k3u1fbpfcp-zoom-1.image)

-   Img alt(altText): 这个则是根据 img 的 alt 来查询，相比之前的一些查询方式，这种从用户视角上就需要满足一定情况才能看见了（图片不能正常加载），我们来看下面的例子。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <img alt="a query by alt" />
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
   test("alt", () => {
    render(<DomQuery />);
    const altImg = screen.getByAltText("a query by alt");
    screen.debug(altImg);
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61e145d7b168454697aaf25a3e8fa846~tplv-k3u1fbpfcp-zoom-1.image)

-   标题（title): title 属性可能大家没怎么用过（说实话，我也几乎没用过它 hahaha），类似 popover 的效果，这个属性也是可以用来查询的，大家看看例子就好。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <span title="a query by title" />
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
   test("title", () => {
    render(<DomQuery />);
    const title = screen.getByTitle("a query by title");
    screen.debug(title);
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2da5311abf68420099b6c286687c5269~tplv-k3u1fbpfcp-zoom-1.image)

-   后门（testid): 最后的这个就特殊点了，这个其实是一个后门的查询方式，通过新增 data-testid 属性来进行查询，这个对整个页面的语义和功能是没有任何影响的，相当于只是我们单独加的一个标识来确定指定的区域，一般只有实在不知道怎么选取需要的区域，才会去使用它，我们来看下面的例子。

```
// ./src/components/DomQuery/index.tsx
import { FC } from "react";

interface IProps {}

// 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 |DOM查询(下)：页面元素的参照物查询和优先级》
export const DomQuery: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <div data-testid="a not so good query"></div>
    </div>
  );
};
```

```
// ./src/__test__/dom_query.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomQuery } from "../components/DomQuery";

describe("tests for 《4 | DOM查询(上)：页面元素的渲染和行为查询》 & 《5 | DOM查询(下)：页面元素的参照物查询和优先级》", () => {
  // ...
   test("testid", () => {
    render(<DomQuery />);
    const testidItem = screen.getByTestId("a not so good query");
    screen.debug(testidItem);
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17d4f4c077884e95b54c653463c580e7~tplv-k3u1fbpfcp-zoom-1.image)

到这里元素的查询方式我们就学完了，不得不说查询的方式真的很多很多，光根据类别来数，行为分类的 6 种，参照物的 8 种，如果再算上不同的 role 和 aria 属性，有几十种查询的方式，让人眼花缭乱，那么，我们应该怎么合理地应用这些查询方式来选取我们希望使用的 DOM 呢？

## 查询的优先级

我们之前有反复提到，React Testing Library 推荐使用近似用户的角度来书写我们的测试用例，我们的单测与用户的角度越贴近，那么它就是越强健可靠的，只要需求逻辑不发生改变，我们的单测就可以不需要调整。

根据这条原则，其实我们很容易区分查询的优先级，我们可以根据查询的参照物是否用户可见来判断它的优先级，比如说：

-   像 `getByRole`、 `getByLabelText`等我们应该主要去使用，因为参照元素对于用户是可见的；
-   对于`getByAltText` 、`getByTitle` 我们可以考虑去用，但不推荐，因为参照物用户只有在特定场景下才可见；
-   至于`getByTestId`我们尽量不要去用，因为用户既没有办法看到，又没有办法听到，只是我们从代码层面加的一个标识，这种做法和 Enzyme 提供的类名的测试思路是没有区别的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24b075959eca44d2b916f347143ac382~tplv-k3u1fbpfcp-zoom-1.image)

## 小结

这节课我们学习了 React Testing Library 参照物层面的分类，如果说行为决定查询 API 的前缀，那么参照物则决定查询 API 的后缀。

从参照物上拆分，我们可以分为 角色 role、标签文本 labelText 等 8种查询方式。其中，角色 role 是我们最常用的方式，通过默认的 aria 角色 role 和属性，我们可以覆盖绝大部分的 DOM 树可见区域，对于自定义的组件，我们也可以去采用自定义 role 的方式来获取，而别的几种查询方式，则提供了一些特定场景下的查询方式，使用上倒是会有奇效。

最后我们还介绍了查询的优先级，与 Enzyme 的测试思路不同的是， React Testing Library 追求的目标是，根据用户的视角来还原测试的场景，这样就可以使得我们的用例与需求功能强绑定，不会因为代码结构的调整和重构影响到测试用例本身。

所以，**我们推荐优先使用用户可见的相关查询方式**，比如 role、labeltext 等，尽可能不要使用 textid 去从代码层面上选取某个元素，避免造成测试用例的脆弱。

现在我们已经学会了怎么去选取页面元素，并且有效合理地使用查询 API，下一步我们就要开始学习断言了。除了 Jest 提供的基础断言外， React Testing Library 提供了一组额外的断言 API 帮助我们更有效优雅地断言我们预期的场景。下节课我们将来学习 React Testing Library 提供了哪些额外的断言 API，并且它们是怎么使用的。

## 6.DOM 断言：页面元素的断言

> 代码仓库：https://github.com/czm1290433700/test_demo

在前两节课，我们学习了 DOM 元素的渲染和查询，我们来简单回忆一下，针对页面元素的渲染，React Testing Library 提供了 render API。render API 会把渲染的元素写入页面的 innerHtml，并会返回指定元素的查询，同时在全局也有暴露一个 screen 全局对象，它将会返回针对 document.body，也就是在当前渲染元素的内容加上 body，并返回标签的查询。

通过获得的查询对象，我们就可以对渲染的元素进行更细粒度的获取，查询的方式可以按照行为和参照物两个维度进行拆分，我们使用最多的是通过角色来查询，这是基于 ARIA 语义提供的查询方式，最贴近功能和需求的语义。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a311a7a1eeba48d281e90e70d1444172~tplv-k3u1fbpfcp-zoom-1.image)

虽然查询 API 数量众多，但是使用上也有对应的优先级，为了书写尽可能稳健的用例，我们需要保证我们的查询贴近用户视角，或是用户可见，所以就有了上面的优先级。

在完成预期对象的查询后，下一步我们需要做的就是对查询出的元素进行预期的断言。除 Jest 提供的断言外，React Testing Library 也提供了一组断言来帮助我们更好地描述自己的预期，这节课我们将结合例子来具体说明怎么对页面元素进行断言。

## 页面元素的断言

页面元素的断言 API 是由 [testing-library](https://github.com/testing-library)/[jest-dom](https://github.com/testing-library/jest-dom) 来提供的，为了方便大家学习理解，我把常用的一些断言根据使用场景分为了页面可见、表单验证和代码层面验证三类，下面我们就按照这三个类别来展开 DOM 断言的学习。

| 断言使用场景 | 断言 API                                                                                                                     |
| ------ | -------------------------------------------------------------------------------------------------------------------------- |
| 页面可见   | `toBeEmptyDOMElement`  `toBeVisible`  `toBeInTheDocument`  `toHaveTextContent`  |                                     
| 表单验证   | `toBeDisabled`  `toBeEnabled`  `toBeRequired`  `toHaveFocus`  `toBeChecked`  `toHaveFormValues` `toHaveValue` |
| 代码层面验证 | `toHaveAttribute`  `toHaveClass`  `toHaveStyle` |

### 页面可见

首先我们来介绍一下`toBeEmptyDOMElement` | `toBeVisible` | `toBeInTheDocument` 这三个断言，它们的含义很接近，都可以用来表示是否可见，但是之间存在一些微小的差异：

-   `toBeEmptyDOMElement`：标签之间是否有可见内容， 即使是空格也会失败；
-   `toBeVisible`：是否可见，从用户直接观察的角度看能否可见；
-   `toBeInTheDocument`：是否存在在文档中，document.body 是否存在这个元素。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fb243edf5b644e095ce9885e7cfb83b~tplv-k3u1fbpfcp-zoom-1.image)

上面的简图就初步描述了它们之间的差异，我们来举例具体说明一下，为了区分上节课的用例，我们单独创建一个新的组件来存放我们这章节的代码：

```
// ./src/components/DomExpect/index.tsx
import { FC } from "react";

interface IProps {}

// 《6 | DOM断言：页面元素的断言》
export const DomExpect: FC<IProps> = ({}) => {
  return (
    <div>
      <div aria-label="empty_note"></div>
      <div role="note" style={{ display: "none" }} aria-hidden>
        1234
      </div>
      <div role="note">1234</div>
    </div>
  );
};
```

```typescript
// ./src/__test__/dom_expect.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  test("visible validation", () => {
    render(<DomExpect />);
    const emptyNote = screen.getByRole("generic", { name: "empty_note" });
    const [hiddenNote] = screen.getAllByRole("note", { hidden: true });
    const normalNote = screen.getByRole("note");
    expect(emptyNote).toBeEmptyDOMElement();
    expect(hiddenNote).not.toBeVisible();
    expect(emptyNote).toBeInTheDocument();
    expect(hiddenNote).toBeInTheDocument();
    expect(normalNote).toBeInTheDocument();
  });
});
```

上面的例子中我们写了几个常见的 DOM，现在我们结合上面三个断言的含义，来解释一下它们分别能命中哪几个 DOM：

-   `toBeInTheDocument`： 这三个 DOM 都是可以满足`toBeInTheDocument`的，因为这几个元素都在文本文档中；
-   `toBeVisible`：只有`<div role="note" style={{ display: "none" }} aria-hidden>1234</div>` 是不能满足的，因为我们对它加上了`display: none`的样式，所以是不可见于 DOM 树的；
-   `toBeEmptyDOMElement`: 只有`<div aria-label="empty_note"></div>` 是匹配 `toBeEmptyDOMElement`的，因为只有它的标签之间没有包含任何内容。

值得一提的是，只有 `aria-hidden` 并不会影响 visible 的判断，这是一个语义的属性，并不作为匹配的一个标准。如果只是加了 `aria-hidden` 而实际可见，仍然会匹配 `toBeVisible`。

除了断言的部分，这个例子中查询的部分我也想和大家具体聊一聊，针对 empty 例子的查询我们为它加上了 label 属性，然后通过了 role 查询的 name 去定位。

```
<div aria-label="empty_note"></div>
```

对于隐藏元素查询的部分，大家可能会有两个疑惑的点：

-   为什么例子中的 normalNote 可以直接用 get 配合角色来定位，文档中不是有两个这样的角色吗？
-   为什么`hidden:true`元素的查询需要用 getAll，它不是只有一个吗？

针对这两个问题，我们来具体解释一下。

-   针对第一个问题，我们的确定义了两个 note 角色，能够直接用单查的方式定位到 hidden: false 元素的原因在于，对于 getByRole，它的默认筛选值中 hidden = false，也就是说，当直接使用 getByRole 的时候，效果等同于 `getByRole(role, {hidden:false})`。
-   当需要查询 hidden:true 元素的时候，大部分场景需要使用 getAll，为什么呢？因为连带 hidden: false 的元素会被一起查询出来，按照 DOM 顺序返回数组，所以这里的 hidden: true 并不是选取 hidden 属性为 true 的元素，而是是否需要查询 hidden 属性为 true 的元素。

到这里，`toBeEmptyDOMElement` 、 `toBeVisible`、 `toBeInTheDocument`这三个断言相信大家就已经有了一个初步的认识了，在页面可见这个方向的断言中，还有一个`toHaveTextContent`没介绍，这个断言和可见其实没有太大的关系，它可以用来匹配对应节点有没有指定的内容，因为也是和页面内容强相关，所以放在了一起，我们来看下面这个例子。

```
// ./src/__test__/dom_expect.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  test("visible validation", () => {
    // ... 
    expect(normalNote).toHaveTextContent(/1/i);
  });
});
```

在上文的用例中，我们额外加入了一条断言，断言`<div role="note">1234</div>`的标签文案中包含 1 ，通过这个断言我们可以快速高效地匹配查询的内容是否符合预期。

### 表单验证

不管是业务需求还是基础组件，我们都会经常接触到表单，可以说表单是前端和服务端 IDL 联系的纽带，不管是多复杂的系统，都是从表单展开对应的功能，所以对表单进行验证和断言是必要且频繁的。针对表单，React Testing Library 提供了下面的断言来协助我们对逻辑进行匹配：

-   `toBeDisabled` ：检查元素是否通过 disable 属性判断，而不是 aria-disabled；
-   `toBeEnabled`: 是否未被禁用，等同于 `.not.toBeDisabled`；
-   `toBeRequired`: 元素是否必填；
-   `toHaveFocus`: 元素是否聚焦；
-   `toBeChecked`: checkbox 或者是 radio 是否被选中；
-   `toHaveFormValues`：验证整体表单的值是否和预期值匹配；
-   `toHaveValue`：与 `toHaveFormValues` 类似，不过不同的是 `toHaveValue` 验证某个单独的表单元素，而不是全部。

我们来看下面的这个例子：

```typescript
// ./src/__test__/dom_expect.test.tsx
import { FC } from "react";

interface IProps {}

// 《6 | DOM断言：页面元素的断言》
export const DomExpect: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <form aria-label="form">
        <input
          type="text"
          name="username"
          disabled
          aria-disabled
          defaultValue="zhenmin"
        />
        <input type="number" name="age" defaultValue={23} required />
        <input
          type="radio"
          name="sex"
          value="man"
          defaultChecked
          aria-checked
        />
        <input type="radio" name="sex" value="woman" />
      </form>
    </div>
  );
};
```

```typescript
// ./src/__test__/dom_expect.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  // ...
  test("form validation without semi", () => {
    render(<DomExpect />);
    const form = screen.getByRole("form");
    const username = screen.getByRole("textbox");
    const age = screen.getByRole("spinbutton");
    const manCheckbox = screen.getByRole("radio", { checked: true });
    const womanCheckbox = screen.getByRole("radio", { checked: false });
    expect(username).toBeDisabled();
    expect(age).toBeEnabled();
    expect(age).toBeRequired();
    age.focus();
    expect(age).toHaveFocus();
    expect(manCheckbox).toBeChecked();
    expect(womanCheckbox).not.toBeChecked();
    expect(form).toHaveFormValues({
      username: "zhenmin",
      age: 23,
      sex: "man",
    });
    expect(age).toHaveValue(23);
  });
});
```

在上面的例子中，我们定义了一个表单，在这个表单中包含四个元素：

-   name 为 username 的文本框，被禁用，拥有一个 "zhenmin" 的默认值；
-   name 为 age 的数字文本框，必填，拥有 23 的默认值；
-   两个 radio ，name 为 sex， 值为 man 的那个被默认选中。

我们通过它们的默认角色进行了查询，对于两个 radio ，我们使用了 checked 的 aria 属性来区分它们。除 checked 外，如果具备同类元素，可以再加上 aria-label 来筛选。要注意的是，这里的 name 不能用 name 筛选，因为它在表单中并不作为语义属性。

值得一提的是，对于 form 元素，虽然它包含 form 角色，但是必须要加上 aria-label 才可以使用 `screen.getByRole("form")`进行筛选，这是一个很特殊的规则，因为 form 元素没有一个可访问的信息，大家可以尝试删掉`<form aria-label="form">` 中的 aria-label 属性，应该会出现下面的报错。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac53d5f046b642dc82d5f35090296a58~tplv-k3u1fbpfcp-zoom-1.image)

相信这个查询的选用会给大家很大的启发，在实际的业务应用中，我们应该也尽可能采用 role 和 aria 属性混用的方式来匹配我们需要的元素，而不要滥用 test-id，因为这样会导致我们堆砌了大量与语义无关的测试标签，这是没有意义且比较糟糕的做法。

选取完元素后，我们使用了上面介绍的断言来匹配我们想验证的内容：

-   name 为 username 的文本框被禁用；
-   name 为 age 的文本框可正常交互，必填的和聚焦的，且值为 23；
-   值为 man 的 checkbox 被选中， woman 没被选中；
-   form 的 value 为 `{ username: "zhenmin", age: 23, sex: "man"}`。

需要特别说明的是 `age.focus`，这里我们使用 fireEvent 来模拟 focus 聚焦的效果，完成我们`toHaveFocus`的验证，不过准确地说，这是一种可以实现但不好的方式，这个并不是严格意义上的从用户视角来模拟，而是从代码角度去直接模拟事件。

与此类似的还有 user-event ，它是一个更贴近用户场景，更准确的方式，它们之间的区别咱们这边不多提及，详细的部分我们会在[7 | User-event: 怎么对 Dom 组件绑定事件进行模拟触发？](https://juejin.cn/editor/book/7174044519350927395/section/7176804373316501556) 具体学习。

### 代码层面验证

除了从用户交互层面的测试，我们有的时候还是需要从代码层面进行验证的，比如某个类、属性或者样式需要在特定场景下包含，这种情况，我们就需要使用到代码层面验证的断言了。

对于代码层面验证的断言，我们常用的有下面三个：

-   `toHaveAttribute`: 匹配元素是否具备某个值的属性；
-   `toHaveClass`: 匹配元素在类属性中是否包含某个类；
-   `toHaveStyle`: 匹配元素是否具有对应样式，需要注意的是，这个是精准非模糊匹配，例如 `display: none` 无法匹配`  display:none;color:#fff; `。

我们来看下面的例子，对于 DOM 的部分，我们复用之前的差不多就够用了，为其中一个元素加一下类：

```
// ./src/__test__/dom_expect.test.tsx
import { FC } from "react";

interface IProps {}

// 《6 | DOM断言：页面元素的断言》
export const DomExpect: FC<IProps> = ({}) => {
  return (
    <div>
      {/* ... other content */}
      <div
        role="note"
        style={{ display: "none" }}
        className="test hidden"
        aria-hidden
      >
        1234
      </div>
      {/* ... other content */}
    </div>
  );
};
```

```
// ./src/__test__/dom_expect.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  // ...
  test("code validation", () => {
    render(<DomExpect />);
    const [hiddenNote] = screen.getAllByRole("note", { hidden: true });
    expect(hiddenNote).toHaveAttribute("aria-hidden");
    expect(hiddenNote).toHaveClass("hidden");
    expect(hiddenNote).toHaveStyle("display: none");
  });
});
```

在上面的例子中，选取了我们之前定义的隐藏区域的 DOM，并对它分别验证了属性、类名和样式，对于属性验证的那个断言`expect(hiddenNote).toHaveAttribute("aria-hidden")`，我们只使用了第一个参数，这个会直接验证这个属性是否存在，同时它也还接收第二个参数，用于验证属性的值，如果需要判断属性的值，大家可以采用类似`toHaveAttribute(attr, value)`的写法。

## 基于组件库的断言

对于业务代码，我们不可避免会使用到组件库，尤其是针对表单的模块，组件库暴露出来的组件未必是基于原生的标签来魔改的，所以在查询和断言上有些许差异，我们以 Semi 组件库的 Select 组件为例，我们知道原生使用下拉框，我们会使用 select 标签，但是那个的定制性会比较差，Semi 提供了一个功能更强大的 Select 组件，如下图。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0355a252f8d41ac9cc926755cd6bce3~tplv-k3u1fbpfcp-zoom-1.image)

不过，它的实现并不是通过 select 标签来实现的，而是自己重构了一套，我们可以打开控制台选一下 select 的区域。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e888df33f2944af89595916b86ee179~tplv-k3u1fbpfcp-zoom-1.image)

这样在查询上，我们就不能用常规选取 select 角色的方式来选取了，所以针对组件库的场景，我们额外补充一份对应的用例来给大家作为对应场景实践的参考，我们首先来安装一下 semi 的依赖：

```
npm i @douyinfe/semi-ui
```

然后我们来看下面的例子，除 semi 表单验证外，我们还修改了一下表单验证的部分，避免一些角色的冲突，相应的普通表单的验证我们也做了一些调整：

```
// ./src/__test__/dom_expect.test.tsx
import { FC } from 'react';
import { Form } from '@douyinfe/semi-ui';

interface IProps {}

// 《6 | DOM断言：页面元素的断言》
export const DomExpect: FC<IProps> = ({}) => (
  <div>
    {/* ...other content */}
    {/* 表单验证 */}
    <form aria-label="form">
      <input type="text" name="username" disabled aria-disabled defaultValue="zhenmin" aria-label="form_username" />
      <input type="number" name="age" defaultValue={23} required aria-label="form_age" />
      <input type="radio" name="sex" value="man" defaultChecked aria-checked aria-label="form_sex" />
      <input type="radio" name="sex" value="woman" aria-label="form_sex" />
    </form>
    {/* semi 表单验证 */}
    <Form initValues={{ username: 'zhenmin', age: 23, sex: 'man', hobby: 'code' }} aria-label="semi-form">
      <Form.Input field="username" disabled name="username" />
      <Form.InputNumber field="age" required name="age" />
      <Form.RadioGroup field="sex" name="sex">
        <Form.Radio value="man" />
        <Form.Radio value="woman" />
      </Form.RadioGroup>
      <Form.Select field="hobby" name="hobby">
        <Form.Select.Option value="code">code</Form.Select.Option>
        <Form.Select.Option value="read">read</Form.Select.Option>
      </Form.Select>
    </Form>
  </div>
);
```

```typescript
// ./src/__test__/dom_expect.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  // ...
  test('form validation without semi', () => {
    render(<DomExpect />);
    const form = screen.getByRole('form', { name: 'form' });
    const username = screen.getByRole('textbox', { name: 'form_username' });
    const age = screen.getByRole('spinbutton', { name: 'form_age' });
    const manCheckbox = screen.getByRole('radio', { checked: true, name: 'form_sex' });
    const womanCheckbox = screen.getByRole('radio', { checked: false, name: 'form_sex' });
    expect(username).toBeDisabled();
    expect(age).toBeEnabled();
    expect(age).toBeRequired();
    age.focus();
    expect(age).toHaveFocus();
    expect(manCheckbox).toBeChecked();
    expect(womanCheckbox).not.toBeChecked();
    expect(form).toHaveFormValues({
      username: 'zhenmin',
      age: 23,
      sex: 'man',
    });
    expect(age).toHaveValue(23);
  });
  // ...
  test('visible validation with semi', () => {
    render(<DomExpect />);
    const form = screen.getByRole('form', { name: 'semi-form' });
    const username = screen.getByLabelText('username');
    const age = screen.getByLabelText('age');
    const sex = screen.getByLabelText('sex');
    const hobby = screen.getByLabelText('hobby');
    expect(username).toBeDisabled();
    expect(age).toBeEnabled();
    expect(age).toBeRequired();
    age.focus();
    expect(age).toHaveFocus();
    // expect(username).toHaveValue('zhenmin');
    // expect(hobby).toHaveValue('code');
    // expect(form).toHaveFormValues({
    //   username: 'zhenmin',
    //   age: 23,
    //   sex: 'man',
    //   hobby: 'code',
    // });
  });
});
```

普通表单验证调整的地方大家自己看一下就好，加了一些 label 来区分，我们来看一下 semi 表单处的用例，首先对于查询，form 处我们需要自己加上 label，原理和之前是一样的，这样 form 才可以作为可访问的信息。对于剩下的表单元素，我们可以直接通过 labeltext 来查询，semi 会将对应的 field 注入到 aria-labelledby 中，例如下图的效果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64224675654f498f9549fe64f5f6efc6~tplv-k3u1fbpfcp-zoom-1.image)

到这里都还挺顺利的，不过到验证值的时候就会出现问题了。我们之前介绍过 react testing library 提供了针对表单元素和整体表单值的断言，表单元素的断言依赖元素上绑定的 value 属性，而整体表单的断言依赖每个元素的 name 来绑定。

对于表单元素，semi 有些会给我们加上 value，比如 input，像上例中的 username。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89be9ba451c74c11833dc5daa558be23~tplv-k3u1fbpfcp-zoom-1.image)

但是有一些不会，比如说像 select，那个是基于 div 自己实现的，像上例中的 hobby。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89c911b8a3b04ed980972ef43a56ebab~tplv-k3u1fbpfcp-zoom-1.image)

对于整体表单，`toHaveFormValues` 断言会完全失效，因为我们使用了 Form 组件，所有的表单元素name 都会被接管到类名上，而不是透传到对应元素上，从源码上我们也可以看到它的选取方式。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa18dd2fd2504f2fa950e45369814135~tplv-k3u1fbpfcp-zoom-1.image)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f00b8214f3324277becb982244f1aad8~tplv-k3u1fbpfcp-zoom-1.image)

这个问题其实是 Semi 最初设计遗留下来的历史包袱，额外增加的 name 字段覆盖了 html 标签提供的 name 属性，加上当时 Semi 使用的单测是基于 enzyme，的确很难暴露出这个问题。因为这个问题从 1.x 就已经开始存在，很多业务方在使用现在考虑到兼容性也没办法去做不兼容修改，后续可能 Semi 会额外加上一个属性用于 html 标签 name 属性的透传，这个 feature 我也会继续跟进 Semi 那边的进度。

在 Semi 还没额外替我们加属性透传前，有什么办法可以解决这个问题呢？对于 Semi 表单值的处理，我这边提供三个方案给大家参考：

-   这是最推荐的方案。使用 Semi Form 组件，但是跳过值处理的断言，直接断言 submit 事件，因为 semi 单测已经帮我们测试过组件内的逻辑，从单测的角度来说，依赖的功能我们不进行测试也是合理的，只需要保证 submit 事件可以被触发即可，至于执行的函数本身，我们可以单独加上用例进行测试。事件的模拟我们会在 [7 | User-event: 怎么对 Dom 组件绑定事件进行模拟触发？](https://juejin.cn/book/7174044519350927395/section/7176804373316501556) 中介绍。
-   换用普通 Semi Input 组件，不用 Semi Form 组件来接管数据，对于普通的 Input 组件是会透传到标签本身的，如下图。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbb7007efdc64177b62e099cacd21205~tplv-k3u1fbpfcp-zoom-1.image)

-   加一个 hidden 区域来存放表单的值，我们直接验证 hidden 区域，这个其实很 hack ，如果大家评估的确需要测试这部分，可以采取这个方案，我们来看下面的例子：

```
// ./src/__test__/dom_expect.test.tsx
import { FC, useState } from 'react';
import { Form } from '@douyinfe/semi-ui';

interface IProps {}

// 《6 | DOM断言：页面元素的断言》
export const DomExpect: FC<IProps> = ({}) => {
  const [semiFormValues, setSemiFormValues] = useState({ username: 'zhenmin', age: 23, sex: 'man', hobby: 'code' });

  return (
    <div>
      {/* ... other content */}
      {/* semi 表单验证 */}
      <Form
        initValues={semiFormValues}
        aria-label="semi-form"
        onChange={(data: any): void => {
          setSemiFormValues(data);
        }}
      >
        <Form.Input field="username" disabled name="username" />
        <Form.InputNumber field="age" required name="age" />
        <Form.RadioGroup field="sex" name="sex">
          <Form.Radio value="man" />
          <Form.Radio value="woman" />
        </Form.RadioGroup>
        <Form.Select field="hobby" name="hobby">
          <Form.Select.Option value="code">code</Form.Select.Option>
          <Form.Select.Option value="read">read</Form.Select.Option>
        </Form.Select>
      </Form>
      <input type="hidden" role="note" value={JSON.stringify(semiFormValues)} />
    </div>
  );
};
```

```
// ./src/__test__/dom_expect.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  // ...
  test('visible validation with semi', () => {
    render(<DomExpect />);
    // ...other content
    const hiddenNotes = screen.getAllByRole('note', { hidden: true });
    expect(hiddenNotes[2]).toHaveAttribute(
      'value',
      JSON.stringify({
        username: 'zhenmin',
        age: 23,
        sex: 'man',
        hobby: 'code',
      })
    );
  });
});
```

## 小结

这一节课我们学习了 React Testing Library 给我们提供的断言，从大方向来说，可以分为页面可见、表单验证和代码层面验证三个维度，其中，表单验证可能在我们的业务场景中有频繁的应用，普通的表单和基于 Semi 的表单表现上是有差异的。

如果有使用 Semi Form 的表单控件，那么验证表单值的时候就不能直接使用`toHaveFormValues`， 因为表单元素的 name 并不会作为属性直接透传。针对这种场景，我最建议大家跳过对值的直接验证，转而直接验证 submit 的结果能否符合预期，如果需要验证值，我们也可以自己加上一个 hidden 表单，进行值的对应。

到这节课为止，我们对于 DOM 的渲染、查询和断言都有了较深入的了解，但是在业务场景中，除了静态的部分，我们难免会遇到各种各样的用户操作事件，对于这些场景的断言，我们需要能够模拟用户的事件来进行预期的判定。在下节课，我们就来学习怎么对 Dom 组件绑定事件进行模拟触发？

## 11.14 更新

之前提到的 html 默认 name 属性 Semi form 组件不能透传的问题，已经联系 Semi 同学进行修复了，后续我们就可以正常使用 toHaveFormValues 进行表单的断言了，详细的 pull request diff 大家可以参考  https://github.com/DouyinFE/semi-design/pull/1266

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/923aa50a26fe48a99a0c0eb01d9a72c0~tplv-k3u1fbpfcp-zoom-1.image)

后续这个 pull request 会随 2.24-beta 版本一同发布，大家升级至更高的 Semi 版本即可~

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/446fd9ab254044f99a20570ee07f76d4~tplv-k3u1fbpfcp-zoom-1.image)

## 7.User-event：怎么对 Dom 组件绑定事件进行模拟触发？

> 代码仓库：https://github.com/czm1290433700/test_demo

经过前三节课的学习，我们现在已经学会了怎么对 DOM 元素进行查询和断言，但是光这样还不足够覆盖我们业务场景的用例需求。在实际的业务场景中，往往会包含各种事件，比如按钮点击，表单提交等，对于这类用例，我们需要模拟对应的事件来触发。

针对这种场景，React Testing Library 提供了两种手段来模拟，fireEvent 和 userEvent，这节课我们就来学习怎么通过它们来模拟事件。

## fireEvent

fireEvent 是 React Testing Library 提供的一组 API，通过它我们可以高效模拟事件的触发。在介绍之前，我们首先回到上节课中的例子。在上节课中，我们测试聚焦的断言时，有使用 fireEvent 来模拟文本框的聚焦。

```
// ./src/__test__/dom_expect.test.tsx
import React from "react";
import { render, screen } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  // ...
  test('form validation without semi', () => {
    // ...
    age.focus();
    // ...
  });
});
```

这是一种特殊的方式，focus 事件有被绑定在元素的对象上，与此类似的 blur（失焦）事件，执行的效果与 fireEvent 中提供的 focus 是相同的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2221bb0e19d14d0aa36913a5663386ef~tplv-k3u1fbpfcp-zoom-1.image)

fireEvent Api 的结构是这样的：

```typescript
fireEvent[eventName](node: HTMLElement, eventProperties: Object)
```

上面的参数 eventName 是指需要模拟的事件，除 focus 外，fireEvent 还可以模拟 click 等事件，其中 eventName 涉及大部分 document event，支持的内容大家可以在源码 [event-map.js](https://github1s.com/testing-library/dom-testing-library/blob/main/src/event-map.js) 中查看。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28180f53a8014571a9cddd8b62191c69~tplv-k3u1fbpfcp-zoom-1.image)

小部分较难模拟的事件不支持，例如滚动，这部分我们可以采用端对端测试的方案来覆盖，具体会在 [14 | E2E:  怎么覆盖滚动等复杂交互场景的测试？](https://juejin.cn/book/7174044519350927395/section/7176804898074427427) 介绍。

除 eventName 外，还有一个 node 和 eventProperties ，node可以接收一个我们查询出来的对象，而 eventProperities 则是描述这个具体事件的属性，以键盘按下事件为例，不同的按键按下会有对应的属性，这个具体的属性可以通过 [下面的页面](https://www.toptal.com/developers/keycode) 查询，比如我们按一下空格键。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/34c0c0e0896b488da248add426a261cb~tplv-k3u1fbpfcp-zoom-1.image)

与之对应的 fireEvent，我们就可以写作：

```
firEvent.keyDown(node, {key: '', code: 'Space', charCode: 32})
```

我们来举个例子具体说明一下：

```
// ./src/components/DomEvent.tsx
import { FC } from "react";

interface IProps {
  onClick: () => void;
}

// 《7 | User-event: 怎么对 Dom 组件绑定事件进行模拟触发？》
export const DomEvent: FC<IProps> = ({ onClick }) => {
  return (
    <div role="note" onClick={onClick}>
      点我试试
    </div>
  );
};
```

```
// ./src/__test__/dom_event.test.tsx
import React from "react";
import { fireEvent, render, screen } from "@testing-library/react";
import { DomEvent } from "../components/DomEvent";

describe("tests for 《7 | User-event: 怎么对 Dom 组件绑定事件进行模拟触发？》", () => {
  test("mock events with fireEvent", () => {
    const clickEvent = jest.fn();
    render(<DomEvent onClick={clickEvent} />);
    fireEvent.click(screen.getByRole("note"));
    expect(clickEvent).toBeCalled();
    expect(clickEvent).toBeCalledTimes(1);
  });
});
```

通常对于事件的用例，我们会使用到 Jest 提供的 mock 事件，以及 `toBeCalled` 和 `toBeCalledTimes` 两个断言，`toBeCalled` 用来判断 mock 事件是否被调用，而 `toBeCalledTimes` 用来判断 mock 事件被调用的次数。

在上面的例子中，我们 mock 了一个函数，并且把它传入我们定义组件的 click 事件中，作为预期，我们断言了这个函数在模拟点击后，将会被执行，且执行次数为1。大家可能会有一个疑问，我们实际传入的方法并不是 mock 方法，那怎么保证这个事件触发后可以按预期执行呢？

其实，这个我们应该单独为函数本身书写用例来测试，因为根据单一原则，我们这边需要保证的是在事件触发后，可以执行对应的回调，至于回调自己的函数做了什么事情，我们应该直接配置入参来测试函数。

## userEvent

上面我们介绍了 fireEvent，虽然它是可以满足我们需求的，但是其实我们应该尽量避免使用 fireEvent，而是使用 userEvent，为什么呢？

在之前的章节我们反复提到，我们书写的用例应该尽可能从用户视角来展开，而不是代码层面，这样对于用例本身来说，才是更强健的，对于 fireEvent 而言，它只是在调度一个 DOM 事件，例如 click 事件，对于 fireEvent 而言，它只是直接触发了这个元素的 click。

然而在实际的场景中，我们点击一个按钮，会有先 hover 再聚焦的过程，这些事件的触发并不会在 fireEvent 中体现出来。 userEvent 则是在模拟完整的事件流程，我们上面提到的 click 事件，它同样也会触发 hover 等事件效果，更为真实地还原了用户的场景，我们可以从源码上来更深刻地认识这个问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2756102062346a7b24713d215e1d8c2~tplv-k3u1fbpfcp-zoom-1.image)

这是 fireEvent 的实现，很简单，除了一些异常的兜底外，就是直接模拟返回的事件。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/392b6c2b71d24599b942c5bae7c8220d~tplv-k3u1fbpfcp-zoom-1.image)

这是 userEvent 的实现，除了模拟传入实例直接需要的 click 外，它还触发了这个元素聚焦和失焦，就不像 fireEvent ，只是简单返回模拟的事件。对于其他事件，userEvent 也是针对事件来一一定制对应的响应函数的，目前支持的有下面的事件， 对于还没实现的事件大家可以用 fireEvent 先替代。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e4225b671e8940398f05454b16071b28~tplv-k3u1fbpfcp-zoom-1.image)

对于之前写的 fireEvent 用例，我们尝试用 userEvent 改写一下：

```
// ./src/__test__/dom_event.test.tsx
import React from "react";
import { fireEvent, render, screen } from "@testing-library/react";
import { DomEvent } from "../components/DomEvent";
import userEvent from "@testing-library/user-event";

describe("tests for 《7 | User-event: 怎么对 Dom 组件绑定事件进行模拟触发？》", () => {
  // ... other content
  test("mock events with userEvent", () => {
    const clickEvent = jest.fn();
    render(<DomEvent onClick={clickEvent} />);
    userEvent.click(screen.getByRole("note"));
    expect(clickEvent).toBeCalled();
    expect(clickEvent).toBeCalledTimes(1);
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/800f2df98fc9412b99a8dbbd967d3e15~tplv-k3u1fbpfcp-zoom-1.image)

## 小结

这节课我们学习了怎么对 DOM 组件的事件进行模拟，React Testing Library 提供了 fireEvent 和 userEvent 两组 API 来帮助我们进行事件模拟，在 API 支持的情况下，我推荐大家优先使用 userEvent。

从实现上来说，fireEvent 采用简单的事件模拟方式，只会触发对应的事件，并不是真实还原用户操作的完整场景，而 userEvent 暴露的每个方法都是根据实际事件场景去定制的还原。从用例的强健性上看，与网页使用方式越相近的测试用例，给予我们的信心就会越大，用例也不容易变更或是遗漏边缘情况。

现在我们已经学习了查询、断言以及事件模拟的相关内容，对于 DOM 事件的用例书写，相信大家已经有了初步的认知，但是到目前为止，我们的用例都还是同步进行的，事实上在实际的业务场景，我们难免会遇到异步执行的逻辑，这个也是我们用例需要覆盖的重要模块，下节课我们就来学习如何测试异步逻辑。

## 8.Async 异步：异步方法如何进行单测？

> 代码仓库：https://github.com/czm1290433700/test_demo

上节课我们学习了怎么模拟 DOM 事件触发来进行逻辑的断言，在 React testing library 中有提供 fireEvent 和 userEvent 两种事件的模拟 API，其中 fireEvent 是简单的事件触发，而 userEvent 相比之下会根据实际场景的角度进行事件的模拟，不仅是事件本身，也包括触发这个事件过程中可能会触发的额外事件，相比之下更符合我们用例的设计原则 -- 贴近用户使用。

之前的课程我们虽然学会了查询，断言和事件的模拟，但一直是同步的逻辑。在实际的业务场景中，异步逻辑的占比也是不小的，那么在测试程序中，我们应该怎么对异步的方法或逻辑进行单测呢？

## 什么是异步？

> 异步指两个或两个以上的对象或事件不同时存在或发生（或多个相关事物的发生无需等待其前一事物的完成）。

对于异步的概念，这个也是我们面试中八股文比较爱问的问题了，虽然很多同学都比较清楚了，但是考虑到读者也有一些是测试的同学，所以这边我们还是一起简单回顾一下什么是异步？

我们知道 JavaScript 不同于 Java 、Golang 等，它是一门单线程编程语言，用通俗易懂的话来说，如果把编程语言比作赛道，JavaScript 是单条赛道，在这条赛道的运动员没有跑完之前，是不能让另一个运动员上去跑的，而别的编程语言有多条赛道，可以实现应用的并行运行，从而提高吞吐率。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a30c1a55179544ada82b7c0756208df4~tplv-k3u1fbpfcp-zoom-1.image)

这样设计的原因是 JavaScript 的使用场景是一门浏览器脚本语言，如果设计为多线程，在操作 DOM 的时候，不同线程之间的互动可能会出现冲突，比如某个线程希望删除这个 DOM 元素，另一个线程要对这个 DOM 元素进行修改。

当然如果参考别的语言中锁的概念进行设计，也是可以解决这个问题的，不过会加大 JavaScript 的设计复杂程度，在早期也很难想象到 JavaScript 会有这么广泛的应用，所以会有这样的一个设计。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f2d8ff40f1e4954b1cbed1613489a0e~tplv-k3u1fbpfcp-zoom-1.image)

但是这就很奇怪了，上面我们介绍到异步是不同时存在或者发生的事情，JavaScript 既然是单线程的，只有一条赛道怎么可能能不阻塞，同时执行呢？

可以很确定的是，JavaScript 还是不能有多个跑道来执行任务的，我们理解中的异步和其他语言中的并行是不同的，在 JavaScript 中异步是基于一个叫 Eventloop 并发模型展开的，注意是 “并发”，不是“并行”，这两者是有很大的区别的。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/903495aba5a143379c03a549514e92d2~tplv-k3u1fbpfcp-zoom-1.image)

JavaScript 的处理其实是在不同的时间之间切换任务，从而实现并发，光 JavaScript 自己是做不到的，因为它自己就一个赛道，不可能跑一半把运动员拉下来，这些都得益于它的运行环境，也就是我们的浏览器。浏览器引擎的实现是多个线程的，大家可以理解成一个是用来跑逻辑的，也就是主线程，另外一个是构图的，也就是 GUI 线程，还有一个是存放异步任务的，也叫任务队列。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf003d58543647d3b306d55e2a701ca6~tplv-k3u1fbpfcp-zoom-1.image)

咱们的逻辑都是在主线程上跑的，主线程没跑完前是不能进行构图的，因为有任务队列的存在，所以主线程是可以不需要等 IO 返回异步任务结果的，可以先挂在任务队列上，先运行后头的任务。

所以对异步最简单的理解就是不挂在主线程，而是放在任务队列中的任务。这些任务通常需要一些时间，或者需要等待拿到结果后才应该执行。只有同步任务走完了，主线程空闲了，任务队列通知主线程这个异步该跑了，才会放到主线程上执行。这个过程会一直重复去执行，也就是 Eventloop 模型。

## Jest 异步

首先我们来介绍一下不涉及 DOM 和事件，也就是 Jest 中的异步。大家应该还记得，我们在 [3 | Jest 断言：如何告诉程序什么是你的预期？](https://juejin.cn/book/7174044519350927395/section/7176802434533048372)这节课中，自定义过一个异步的匹配器，我们来回顾一下这个例子。

```
// ./src/__test__/expect.test.ts
test("异步自定义匹配器", async () => {
    const toBeBetweenZeroAndTen = async (num: number) => {
      const res = await new Promise<{ message: () => string; pass: boolean }>(
        (resolve) => {
          setTimeout(() => {
            if (num >= 0 && num <= 10) {
              resolve({
                message: () => "",
                pass: true,
              });
            } else {
              resolve({
                message: () =>
                  "expected num to be a number between zero and ten",
                pass: false,
              });
            }
          }, 1000);
        }
      );
      return (
        res || {
          message: () => "expected num to be a number between zero and ten",
          pass: false,
        }
      );
    };
    expect.extend({
      toBeBetweenZeroAndTen,
    });
    await expect(8).toBeBetweenZeroAndTen();
    await expect(11).not.toBeBetweenZeroAndTen();
  });
```

在这个例子中，匹配器是异步执行的，需要等待匹配器返回对应的值才能进行断言，所以我们为断言前面加了一个 await 来等待它结果的返回，这个是用例中出现异步的一种情况。

当然除了匹配器异步的情况外，expect 的值是异步的场景会更多，我们来看下面的例子：

```
const fetchData = async () => {
  const res = await new Promise((resolve) =>
    resolve("this is a demo for fetching data")
  );
  return res;
};
```

上面我们定义了一个异步的函数，如果要对这个函数的值进行断言，我们应该怎么做呢？因为断言本身是同步的，按照前几节课的写法，会先执行断言再执行异步函数，这样就拿不到预期的值。我们来看一下下面的用例：

```
// ./src/__test__/async.test.tsx
import React from "react";

describe("examples for async", () => {
  test("for jest", async () => {
    const fetchData = async () => {
      const res = await new Promise((resolve) =>
        resolve("this is a demo for fetching data")
      );
      return res;
    };
    const data = await fetchData();
    expect(data).toBe("this is a demo for fetching data");
  });
});
```

与异步匹配器的使用不同，因为我们需要等待函数的值返回，所以 await 加在函数之前，而不是断言的位置。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8d961141d97407496e438808fe47199~tplv-k3u1fbpfcp-zoom-1.image)

除了这种写法外，我们还可以借助 Jest 提供的 resolves 和 rejects 匹配器来进行异步逻辑的断言，例如下面的例子：

```
// ./src/__test__/async.test.tsx
import React from "react";

// 8 | Async 异步：异步方法如何进行单测？
describe("examples for async", () => {
  test("for jest", async () => {
    const fetchData = async () => {
      const res = await new Promise((resolve) =>
        resolve("this is a demo for fetching data")
      );
      return res;
    };
    const data = await fetchData();
    expect(data).toBe("this is a demo for fetching data");
    await expect(fetchData()).resolves.toBe("this is a demo for fetching data");
    // await expect(fetchData()).rejects.toBe('this is a demo for fetching data');
  });
});
```

对于 `await expect(fetchData()).resolves.toBe("this is a demo for fetching data");` 它会等待前面的断言的 Promise 函数返回 resolve 状态后，再执行后面的断言，rejects 匹配器也同理。

## React Testing library 异步

除了 Jest 中的异步外，React Testing library 也有提供一组的额外的 API 来协助我们进行 DOM 和 state 状态下的断言，其中就包含我们在 [4 | DOM 查询（上）：页面元素的渲染和行为查询](https://juejin.cn/book/7174044519350927395/section/7176803841113849908) 中遗留下来的 findBy 和 findAllBy，我们可以先来看一下下面的这个场景。

```
// ./src/components/DomAsync/index.tsx
import { FC, useEffect, useMemo, useState } from "react";

interface IProps {}

export const DomAsync: FC<IProps> = ({}) => {
  const [text, setText] = useState("");

  const hasDescription = useMemo(() => {
    return text !== "a demo for async test";
  }, [text]);

  useEffect(() => {
    setTimeout(() => {
      setText("a demo for async test");
    }, 500);
  }, []);

  return (
    <div>
      <div>{text}</div>
      {hasDescription && <div>加载中...</div>}
    </div>
  );
};
```

在上面的例子中，我们定义了一个组件，它会在 500ms 后完成加载，显示出 "a demo for async test" 的区域，对于这个场景， "a demo for async test" 并不是在刚加载的时候就存在的，我们使用 get 或者 query 是不能查到它的，那我们应该怎么去完成我们的用例呢？

在 [4 | DOM 查询（上）：页面元素的渲染和行为查询](https://juejin.cn/book/7174044519350927395/section/7176803841113849908)中我们也有提到，findBy 与 getBy 的不同在于，它会重复执行回调去查找对应的元素，直到超过默认的 1000ms 超时时间。对于这个组件，我们就可以通过 findBy 来书写用例，我们来看下面的例子：

```
// ./src/__test__/async.test.tsx
import React from "react";
import {
  render,
  screen
} from "@testing-library/react";
import { DomAsync } from "../components/DomAsync";

// 8 | Async 异步：异步方法如何进行单测？
describe("examples for async", () => {
  // ... other content
  
  test("for react testing library", async () => {
    render(<DomAsync />);
    const testDom = await screen.findByText("a demo for async test");
    expect(testDom).toBeInTheDocument();
  });
});
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/201df612d159440f9a163c6cb5372540~tplv-k3u1fbpfcp-zoom-1.image)

不过`  findBy  `只能固定查元素，而且超时时间固定，如果我们想测一些特殊的逻辑，或者想自定义超时时间应该怎么做呢？React testing library 还提供有一个 `waitfor` 的 API 可以满足我们这个场景，`findBy`其实也是通过 `getBy` 和`waitfor` 来实现的一个常用 API，我们来看看如果使用 waitfor 怎么实现我们上面的场景呢？我们来看下面的例子：

```
// ./src/__test__/async.test.tsx
import React from "react";
import {
  render,
  screen,
  waitFor,
} from "@testing-library/react";
import { DomAsync } from "../components/DomAsync";

// 8 | Async 异步：异步方法如何进行单测？
describe("examples for async", () => {
  // ... other content
  
  test("for react testing library", async () => {
    render(<DomAsync />);
    const testDom = await screen.findByText("a demo for async test");
    expect(testDom).toBeInTheDocument();
    await waitFor(
      () => {
        const waitTestDom = screen.getByText("a demo for async test");
        expect(waitTestDom).toBeInTheDocument();
      },
      {
        timeout: 1000,
        interval: 100,
      }
    );
  });
});
```

`waitfor`接收两个参数，第一个是需要重复执行的回调函数，我们可以在其中查询元素并且断言，`waitfor` 会根据设定（或者默认）的超时时间和执行间隔来重复执行回调。第二个参数是可以配置的数据，比如说超时时间（timeout)、执行间隔（interval），通过这个参数我们就可以自定义我们需要的超时场景。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc064c87f87c434c87c337737adb418a~tplv-k3u1fbpfcp-zoom-1.image)

值得一提的是，在官网的推荐中，建议我们在 `waitfor` 中只加入一个断言，也就是只有一个 expect，这样是为了如果 `waitfor` 失败，可以更快获得某个断言的报错信息，而不用等待超时结束才看到所有的断言报错。

回到上面的场景，现在我们已经断言了 500ms 后 "a demo for async test" 的展示，但是我们组件除了这个功能外，还会在 "a demo for async test"展示的时候隐藏“加载中”的文案，这个是一个常见的场景，我们其实也可以通过 `waitfor` 来自己实现，不过因为常见，所以 React testing library 也有提供对应的包装函数`waitForElementToBeRemoved`来更高效地帮助我们判断。

关于`waitForElementToBeRemoved` 的类型定义是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adc1c30276374275888f4679b9bb3fed~tplv-k3u1fbpfcp-zoom-1.image)

它包含一个泛型 T，这个对应需要判断移除的元素类型，函数本身接收两个参数，一个是 callback，对于这个参数我们可以传入元素本身，或者返回一个返回值为元素的回调函数，至于第二个参数，和`waitfor` 的 options 参数相同，会直接透传给内部逻辑的 `waitfor`，我们可以看下下面的例子：

```
// ./src/__test__/async.test.tsx
import React from "react";
import {
  render,
  screen,
  waitFor,
  waitForElementToBeRemoved,
} from "@testing-library/react";
import { DomAsync } from "../components/DomAsync";

// 8 | Async 异步：异步方法如何进行单测？
describe("examples for async", () => {
  // ... other content
  
  test("for react testing library", async () => {
    render(<DomAsync />);
    waitForElementToBeRemoved(screen.queryByText("加载中...")).then(() => {
      console.log("元素加载完成");
    });
    const testDom = await screen.findByText("a demo for async test");
    expect(testDom).toBeInTheDocument();
    await waitFor(
      () => {
        const waitTestDom = screen.getByText("a demo for async test");
        expect(waitTestDom).toBeInTheDocument();
      },
      {
        timeout: 1000,
        interval: 100,
      }
    );
  });
});
```

在之前的用例基础上，我们补充了一个对加载中的判断，当加载中元素消失的时候，控制台会输出一个元素加载完成的日志。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cb7b6969b3f4bb2a2c1c29de0636cd1~tplv-k3u1fbpfcp-zoom-1.image)

需要特别说明一下的是，对于`waitForElementToBeRemoved`需要判断的 DOM 元素，也就是第一个入参 callback，我们应该使用 `queryBy` 来查询，而不是 `getBy`，在 [4 | DOM 查询（上）：页面元素的渲染和行为查询](https://juejin.cn/book/7174044519350927395/section/7176803841113849908) 中我们有提到过，`queryBy` 和`getBy` 的区别在于 `getBy` 在未查询到指定元素时，会抛出错误。

在我们这个场景下，查询的元素不存在可以说是符合预期的，因为我们本身就是想在它消失的时候做出判断，`getBy` 的错误信息会与`waitForElementToBeRemoved`的错误信息混淆，导致报错并不一致，从而影响到我们对用例结果的判断。

## 一个小彩蛋

细心的同学可能有发现在执行第六节用例的时候，虽然用例通过了，但是我们控制台中有一个这样的报错，因为那时候我们还没有学习异步，虽然这个并不直接属于异步的 API，但是原理其实涉及到异步。所以我没立刻去解决这个问题，考虑了一下这个放在这一节课来介绍大家可能更容易深刻理解，现在我们来看一下这个究竟是什么原因。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27c1f8bec9af44629405258e58d048ac~tplv-k3u1fbpfcp-zoom-1.image)

Act Api 是什么呢？这个其实就已经不是 React testing library 的范畴了，它是 React 测试程序提供的一个触发重新渲染的 API ，我们来从 React 运行机制上解释一下为什么需要这么个 API ？我们可以看一下下面的图解：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58b42d0a37944964ba0bb55fc53c8958~tplv-k3u1fbpfcp-zoom-1.image)

这个图虽然画得可能有点丑，但的确可以很好地说明这个问题，我们知道在 React hook 中有一个 state，这个直接影响到元素本身的渲染内容，当 state 发生改变的时候，将会触发元素的重新 render，但是这个过程后续的断言将会继续执行，也就是说，我们的断言并没有等重渲染完成后，再次获取我们最新的 UI 进行断言，这个也许会导致一些问题。

再来看我们的这个例子，为什么我们聚焦 focus 会影响到重渲染呢？因为我们在 onchange 的时候有改变 state。

```
// ./src/__test__/dom_expect.test.tsx
import { FC, useState } from 'react';
import { Form } from '@douyinfe/semi-ui';

interface IProps {}

// 《6 | DOM断言：页面元素的断言》
export const DomExpect: FC<IProps> = ({}) => {
  const [semiFormValues, setSemiFormValues] = useState({ username: 'zhenmin', age: 23, sex: 'man', hobby: 'code' });

  return (
    <div>
      {/* ... other content */}
      {/* semi 表单验证 */}
      <Form
        initValues={semiFormValues}
        aria-label="semi-form"
        onChange={(data: any): void => {
          setSemiFormValues(data);
        }}
      >
        <Form.Input field="username" disabled name="username" />
        <Form.InputNumber field="age" required name="age" />
        <Form.RadioGroup field="sex" name="sex">
          <Form.Radio value="man" />
          <Form.Radio value="woman" />
        </Form.RadioGroup>
        <Form.Select field="hobby" name="hobby">
          <Form.Select.Option value="code">code</Form.Select.Option>
          <Form.Select.Option value="read">read</Form.Select.Option>
        </Form.Select>
      </Form>
      <input type="hidden" role="note" value={JSON.stringify(semiFormValues)} />
    </div>
  );
};
```

这个问题怎么修呢？我们只需要把可能会干扰到 state 的逻辑放到 act，这样就会刷新所有的效果并且重新渲染。不过其实就我们这个例子而言，不加也没什么关系，因为 focus 这个事件并不会影响到 state，也不会影响到表单的值，也不会重渲染。这个报错的意思更多只是提醒我们，某些逻辑可能修改到了 state， 可能需要考虑到用例出错的场景。

```
import React from "react";
import { render, screen, waitFor } from "@testing-library/react";
import { DomExpect } from "../components/DomExpect/index";
import { act } from "react-dom/test-utils";

describe("tests for 《6 | DOM断言:页面元素的断言》", () => {
  // ... other

  test("form validation without semi", async () => {
    // ... other
    act(() => {
      age.focus();
    })
    // ... other
  });

  // ... other

  test("visible validation with semi", () => {
    // ... other
    act(() => {
      age.focus();
    })
    // ... other
});
```

而且 React testing library 已经把 render 和 事件都包裹到了 act 中，在绝大部分场景下我们是不需要用到它的，但是如果针对 render 和事件之外的场景，我们自己的逻辑有修改到 state，并且出现了这样的报错，我们就需要按照上面说的，把影响到 state 的逻辑包括到 act 中了。

## 小结

这节课我们学习了什么是异步以及怎么测试异步方法，在 JS 中，因为单线程的缘故，异步其实是基于运行引擎的来展开的能力，JS 本身并没办法支持异步，在我们运行 JS 代码的过程中，除了在主线程上跑的逻辑外，还有一部分任务会被放在任务队列中，这些队列需要一定时间，或者拿到结果后才能运行，被称为异步。

这种函数因为不能立刻拿到结果，所以不能够按照常规的方法来测试，在 Jest 中，我们可以通过 await 的方式，等待异步的结果拿到后再断言，如果涉及到 DOM 或者事件需要异步断言，React testing library 也有提供额外的 Api 来协助我们。

我们分别介绍了 `findBy`， `waitfor` 和`waitForElementToBeRemoved`三个 API，其实它们底层都是基于 `waitfor` 来展开的。

除了这些内容外，我们还介绍了一个前几节遗留下来的报错，这个其实是因为我们触发了 state 的修改，react 判断可能会导致 expect 不能取到最新 UI 导致的，我们可以为修改到 state 的逻辑加上 act 函数来触发 DOM 的重渲染。

然而并不是每个定时任务我们都可以通过 waitfor 来搞定，如果这个定时任务需要一天呢？难道咱们的用例也得等一天？这样是很不合理的，其实有一种“假定时器”的做法，可以快进这个过程，下节课我们就来学习 FakeTimer (假定时器）来“快进”测试我们的定时任务。

## 9.FakeTimer：如何"快进"测试定时任务？

> 代码仓库：https://github.com/czm1290433700/test_demo

在上节课中，我们学习了怎么对异步逻辑书写测试用例，针对特殊的异步逻辑，我们通常会使用 waitfor 来重复执行需要验证的回调函数，来完成异步逻辑的测试。在我们的需求当中，难免会遇到像轮询、定时任务的场景，对于这类场景我们会使用 setTimeout、 setInterval 等定时器来实现。

针对这类异步的方法，上节课我们有介绍可以使用 waitfor 来覆盖对应的用例，但是存在一个问题是，如果定时的时长短那可能还行，但是如果定时器多且定时时间不短，我们每则用例都将需要等待那么长的时间，这个其实是不合理的。

针对这种场景，Jest 有提供给我们一组叫 Fake Timer(假定时器）的 API，这节课我们就来学习怎么通过 Fake Timer 来快进我们的任务，以及 Fake Timer 是怎么做到快进效果的。

## 一个小插曲

在开始这节课的学习前，我们插入一个小插曲。在之前的用例执行中，我们发现控制台会输出每次查询的 DOM 结果，这个可以方便我们追溯问题的源头或者快速调试我们的用例，但是当测试用例堆积多了以后，这个 log 栈是比较长的，很难定位到我们需要的位置，也可能很容易丢失。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1ff3acc52504c1c87eb2480c98e0167~tplv-k3u1fbpfcp-zoom-1.image)

对于这个问题，我们其实可以利用 jest 提供给我们的 mock 函数去覆盖全局的 log，那么在哪里加呢？之前在 [2 | 技术选型：React Testing Library Or Enzyme？](https://juejin.cn/book/7174044519350927395/section/7176612133294063668) 介绍 React testing library 的时候，我们提到在配置中，我们会在一个全局的文件中导入 React testing library 所提供的相关断言类型，我们只需要在下面继续补充就好，这样就只会针对测试环境生效，而不会干扰到我们正常的 DOM。

```
// ./src/setupTests.ts
import "@testing-library/jest-dom";

// 移除 jest 的 log 输出
global.console = {
  log: jest.fn(),
  debug: console.debug,
  trace: console.trace,
};
```

针对 debug 和 trace 我们还是注入原来的函数，调试和日志我们还是需要查看的，来试试效果，可以看到就已经没有额外的 log 输出了，看上去清爽多了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ebe96c6032c46888afd382e0fff1345~tplv-k3u1fbpfcp-zoom-1.image)

## 定时快进

现在我们回到正题中来，如果我们的组件涉及到定时的逻辑，定时的时间很长，即使用例本身不超时，执行所需要的时间也是我们不能接受的，所以为了解决这个场景的问题，Jest 提供了一组 Fake Timers API 来跳过定时的等待时长。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9584682f2b04838ba97d6ef4d4782df~tplv-k3u1fbpfcp-zoom-1.image)

我们可以先看下面的例子。

```
// ./src/components/FakeTimer/index.ts
const sleep = async (time: number, result: string): Promise<string> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(result);
    }, time);
  });
};

export { sleep };
```

```
// ./src/__test__/fakeTimer.test.ts
import React from "react";
import { sleep } from "../components/FakeTimer";

// 9 | FakeTimer：如何"快进"测试定时任务？
describe("examples for fakeTimers", () => {
  beforeAll(() => {
    jest.useFakeTimers();
  });

  test("a test for a simple setTimeout", async () => {
    const res = sleep(6000, "this is a simple setTimeout test");
    jest.runAllTimers();
    await expect(res).resolves.toBe("this is a simple setTimeout test");
  });
});
```

在上面的例子中，如果我们定义了一个 sleep 函数，这个函数很简单，它接受两个入参，time 和 result，会在经过 time 时间后将 result 返回，那么如果这个 time 超过了 5000 ms，用例将会执行失败（因为 jest 用例的默认超时时间为 5000ms），所以我们注释掉`jest.runAllTimers()`会得到下面的错误栈信息。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/53b4550e099944dfa89f169b6513ee11~tplv-k3u1fbpfcp-zoom-1.image)

如果我们直接执行上面用例是可以通过的，大家会发现用例可以快速通过，而不需要等待 6 秒以上。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/067b8588517a44e19bf3ddbe53a33684~tplv-k3u1fbpfcp-zoom-1.image)

这个用例与常规用例不同的是，我们在 beforeAll 中加入`jest.useFakeTimers()`，用例本身中启用了`jest.runAllTimers()`，其中`jest.useFakeTimers()`的作用是将定时器替换为假定时器，而`jest.runAllTimers()`的作用是运行所有的定时器，我们可以结合 [源码](https://github1s.com/facebook/jest/blob/HEAD/packages/jest-fake-timers/src/legacyFakeTimers.ts#L264) 看看 jest 是怎么实现这样一个假定时器的，简单但是很精妙。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0ba98db94fa48f1b57dde5684adfe42~tplv-k3u1fbpfcp-zoom-1.image)

大家可以直接关注 `_createMocks`，下面的逻辑只是将 _fakeTimerApis 中的方法覆盖给 global 全局，所以我们调用的 setTimeout 等方法其实是 `_fakeTimerApis` 提供的，在没有执行`  _createMocks ` 前， `_fakeTimerApis` 中的方法其实就是原生对应方法的写入。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec83e22b377649eb845a0c5d0de66b3b~tplv-k3u1fbpfcp-zoom-1.image)

在`  _createMocks `中，它会覆写 `_fakeTimerApis` 中提供的方法，以 setTimeout 的覆写方法为例。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e798abb8e8a4efba6061bb244858d90~tplv-k3u1fbpfcp-zoom-1.image)

_timers 中存放了所有定时器的定时时长，是一个 key - value 的结构，在覆写的方法中，如果没有 delay 的传参，timers 存入的定时器时长就会是 0 ，也就是说我们在执行 `jest.useFakeTimers()`后，执行的 setTimeout 等方法会被 jest 全部覆写，不再是原来的原生方法。

我们再来看看，执行`jest.runAllTimers()`后是怎么立即执行的呢？很多同学已经猜到了，只需要把对应 _timers 下的定时时长删了就可以了，这样找不到对应的定时时长，就可以立即执行了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a6e7ebf418342d497139ea8e8e1eeb0~tplv-k3u1fbpfcp-zoom-1.image)

实际的逻辑中还包含了别的定时方法的清除，这边我们以 setTimeout 为例，对应的方法是 `_runTimerHandle`，可以看到和我们想的一样。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7206ede728a9459982e280e14cd8eb45~tplv-k3u1fbpfcp-zoom-1.image)

除了立即执行所有的定时器外，我们其实还可以控制定时器的执行时间，我们来看下面的例子：

```
// ./src/components/FakeTimer/index.ts
import React from "react";
import { sleep } from "../components/FakeTimer";

// 9 | FakeTimer：如何"快进"测试定时任务？
describe("examples for fakeTimers", () => {
  beforeAll(() => {
    jest.useFakeTimers();
  });

  // ... other content
  test("a test for a controllable setTimeout", async () => {
    const res = sleep(6000, "this is a controllable setTimeout");
    jest.advanceTimersByTime(6000);
    await expect(res).resolves.toBe("this is a controllable setTimeout");
  });
});
```

我们使用 `jest.advanceTimersByTime` 就可以将所有的定时器提前指定时间。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea0a2e35b2454a10977c0f7f4bb5ce8d~tplv-k3u1fbpfcp-zoom-1.image)

## 递归场景的定时快进

当然除了常规的定时外，轮询也是我们业务中常常遇到的一个场景，通过轮询，可以使我们应用获得实时的效果，但是轮询需要使用到递归，如果还是使用 `runAllTimers`，将会遇到栈溢出的问题，我们来看下面例子：

```
// ./src/components/FakeTimer/index.ts
// ... other function
const loopSleep = async (time: number, result: string): Promise<string> => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve(result);
      setTimeout(() => {
        loopSleep(time, result);
      }, time);
    }, time);
  });
};

// ...export 
```

```
// ./src/components/FakeTimer/index.ts
import React from "react";
import { sleep } from "../components/FakeTimer";

// 9 | FakeTimer：如何"快进"测试定时任务？
describe("examples for fakeTimers", () => {
  beforeAll(() => {
    jest.useFakeTimers();
  });

  // ... other content
  test("a test for a recursion setTimeout", async () => {
    const res = loopSleep(6000, "this is a recursion setTimeout test");
    jest.runAllTimers();
    await expect(res).resolves.toBe("this is a recursion setTimeout test");
  });
});
```

如果运行这个用例，我们将得到下面的错误栈：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c363055a66c43589c296f92d66072fd~tplv-k3u1fbpfcp-zoom-1.image)

因为 `jest.runAllTimers()`会运行所有的定时器，不论这个定时器是否在等待中，而因为递归的关系，我们的定时完成后，始终会有一次新的定时，所以会导致我们栈溢出，针对这种场景我们可以使用`runOnlyPendingTimers`，它只会运行目前挂起的定时器，我们修改一下用例：

```
// ./src/components/FakeTimer/index.ts
import React from "react";
import { sleep, loopSleep } from "../components/FakeTimer";

// 9 | FakeTimer：如何"快进"测试定时任务？
describe("examples for fakeTimers", () => {
  beforeAll(() => {
    jest.useFakeTimers();
  });

  // ... other content
  test("a test for a recursion setTimeout", async () => {
    const res = loopSleep(6000, "this is a recursion setTimeout test");
    // jest.runAllTimers();
    jest.runOnlyPendingTimers();
    await expect(res).resolves.toBe("this is a recursion setTimeout test");
  });
});
```

我们运行一下用例，可以看到现在已经可以通过了。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4b33793cfff4591bea6670a7315b42c~tplv-k3u1fbpfcp-zoom-1.image)

到这里我们常用的 FakeTimer 就都介绍过了，除了 `useRealTimers`，这个和 `useFakeTimers`作用相反，可以把 setTimeout 接管回真实的定时器原生方法，比较简单就不额外举例说明了。

## 包含异步函数的定时器快进

除了上面的基础用法外，其实还有一个很容易犯错的场景（我当时也忽略很多次=.=），我们直接看下面的例子。

```
// ./src/components/FakeTimer/index.ts
// ... other function
const asyncSleep = async (time: number, fn: () => void): Promise<void> => {
  setTimeout(() => {
    Promise.resolve().then(() => {
      fn();
    });
  }, time);
};

// ...export 
```

```
import React from "react";
import { sleep, loopSleep, asyncSleep } from "../components/FakeTimer";

// 9 | FakeTimer：如何"快进"测试定时任务？
describe("examples for fakeTimers", () => {
  beforeAll(() => {
    jest.useFakeTimers();
  });

  // ... other content
  test("a test for a setTimeout with async function", async () => {
    const fn = jest.fn();
    asyncSleep(6000, fn);
    jest.runOnlyPendingTimers();
    expect(fn).toBeCalled();
  });
});
```

在上面的例子中，我们写了一个定时函数，当时间到的时候，会异步执行我们传入的回调函数，在用例中，我们使用了 jest 提供的 mock 函数`jest.fn()`，同学们这里不懂不要紧，我们会在 [10 | Mock: 怎么用模拟数据替代较复杂逻辑？](https://juejin.cn/book/7174044519350927395/section/7176804272833724416) 详细介绍，这个 fn 就是我们的一个没有返回值的回调函数，可以理解成一个空函数。

我们定时了 6 秒执行，并通过`jest.runOnlyPendingTimers`快进了这个过程，然后给出了一个断言，我们认为快进完成后，传入的回调函数 fn 应该被调用了，可是用例的结果却差强人意。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4014096f3bf74b3a92d3de6018a6abe1~tplv-k3u1fbpfcp-zoom-1.image)

为什么会出现这样的情况呢？在 [8 | Async 异步：异步方法如何进行单测？](https://juejin.cn/book/7174044519350927395/section/7176612133516345378) 中我们其实有详细介绍异步的原理，JS 本身是没有异步的能力的，在执行引擎的帮助下，我们通过额外的一个线程，任务队列来存放异步的任务，在主线程任务完成后，才会去任务队列中取任务执行，不仅是浏览器引擎，Nodejs 环境下的 V8 引擎也采用类似的策略（蹭一下上节课画的图，同学们可以结合理解）。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b5f6c61cdd142b58b40e1af9b80ae36~tplv-k3u1fbpfcp-zoom-1.image)

我们回到这个例子，我们知道`jest.runOnlyPendingTimers()` 内部实现其实只是把 time 给清空了，立即执行了其中的内容，但是在这个例子中，`setTimeout` 我们存放的是一个异步的任务，上面说过，异步任务是不会被立即执行的，而是存放到任务队列中，所以对于这个例子，我们并不是立即执行函数，而是立即将它放到任务队列，在主线程任务完成后，才能轮到它。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e0ab5db492749dfa99786b4243d67a1~tplv-k3u1fbpfcp-zoom-1.image)

所以当我们断言执行的时候，我们加入的异步逻辑还在任务队列里待着呢，自然我们感知不到它被调用，那应该怎么解决这个问题呢？我们加一个 await 来阻塞断言的执行，期待等待异步逻辑完成后，我们再执行下面的断言，我们来看修改后的例子。

```
import React from "react";
import { sleep, loopSleep, asyncSleep } from "../components/FakeTimer";

// 9 | FakeTimer：如何"快进"测试定时任务？
describe("examples for fakeTimers", () => {
  beforeAll(() => {
    jest.useFakeTimers();
  });

  // ... other content
  test("a test for a setTimeout with async function", async () => {
    const fn = jest.fn();
    asyncSleep(6000, fn);
    jest.runOnlyPendingTimers();
    await Promise.resolve();
    expect(fn).toBeCalled();
  });
});
```

因为`Promise.resolve`是在 fn 之后放入任务队列的，对它执行 await 就可以保证之前放进任务队列的任务可以得到执行，我们现在再来看看结果：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2182bee05934516aeb98cbf62b47308~tplv-k3u1fbpfcp-zoom-1.image)

## 小结

这节课我们学习了怎么“快进”我们的测试定时任务，使用了 Jest 的 FakeTimer API 分别解决了定时快进，递归场景快进和异步函数的定时快进，并且我们还结合了源码解释了 FakeTimer API，究竟是怎么实现“快进”的，现在大家可以说出来其中的细节了吗？

严格意义上来说，这个其实并不是一个快进的行为，而是将我们的定时原生方法进行了拦截，修改了相关的 time，当我们在进行 “快进” 行为时，已经不再是运行原生 global 下的函数了，这种思想大家也可以学习一下，在平时需求中，全局日志或是钩子等地方都有这种思想的影子。

在课程的结尾，我们的例子中还用到了 Jest 的 Mock。 在我们的业务逻辑中，有些逻辑可能我们并不在意它的执行，我们只需要保证它的结果继续进行单测，这种场景下我们常常就会使用 Mock 来替代，是我们单测过程中一个很重要的手段。

下节课我们就来着重学习，怎么使用 Mock 来替代我们不需要关注的逻辑。

