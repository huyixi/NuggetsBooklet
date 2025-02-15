---
title: TypeScript 类型体操通关秘籍
author: TypeScript 类型体操通关秘籍
date: 2025-02-15
lang: zh-CN
---

## 1.如何阅读本小册

在正式开始小册之前，我先来简单介绍下小册的内容，以及大家该怎样阅读小册，才能更好地吸收其中的知识点。

**首先，本小册是围绕 TypeScript 类型体操来讲的，这是 TypeScript 中最难的部分。**

为了帮助大家理解和掌握，我总结出了类型编程六大套路，也就是小册的 5 到 10 节，这是小册中最重点的部分，大家也要重点关注。同时，我也为每个套路提供了大量的实战案例，以及 playground 的链接，建议点进去亲自试一下。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83554d4c736c46c3b8b5648cace22a27~tplv-k3u1fbpfcp-watermark.image?)

当然，每个案例的集合我也都总结在了文章的最后。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a450fddd86db4c609d26e0a2797a5b68~tplv-k3u1fbpfcp-watermark.image?)

六个套路介绍完之后，为了方便记忆，我总结了类型体操顺口溜，并解释了每句的含义，时不时读两遍，配合实战案例，吸收率更好。


说完了最重点的部分，我们再回过头来说说整个小册的构建思路。

在介绍这些套路之前，第 2、3、4 节主要会讲解一些理论知识，包括类型、类型安全、静态类型、动态类型、三种类型系统等等。其中，第 4 节主要讲解 TypeScript 类型系统中的类型和支持的类型运算，这些过一遍就行，在后面的实战中会大量用到，自然而然就记住了。**理论还是很重要的，它提升的是我们的认知，也就是看待技术的视角。**


类型体操顺口溜之后，我们会实现内置的高级类型。其实学完类型体操的套路之后，你会发现内置的类型实现起来太简单了。然后我单独准备了一节实际案例来说明类型体操的意义，以及它在项目中有发挥了什么作用。后面是大量的综合实战，难度会比单独讲每个套路的时候大一些。综合运用各种套路，就能实现各种类型编程逻辑了。

接着，我会讲解 TypeScript 类型检查的实现原理。在这个过程中，我们要自己实现类型检查。只有自己能实现了，才能真正理解 TypeScript 类型检查都做了啥。当然，我也会讲解阅读 TypeScript 源码的方法，带大家探究联合类型的分散特性的实现原理。不过，阅读 TypeScript 源码的必要性不大，它只是一个工具。因此，这一节只是扩展下技术视野。

最后就是小册的总结了，这一节我们会对小册整体的知识点都做个总结。

《Babel 插件通关秘籍》是我写的第一本小册，当时是第一次写，虽然内容很丰富，但表达上还有些不成熟。在写《TypeScript 类型体操通关秘籍》这本小册的时候，我已经有了一些写作经验，知道了该怎么写，所以会写得更清晰些。让小册读起来更清晰、易懂，阅读爽感更强，这也是我一直追求的。

当然，小册的内容难免还会有瑕疵。因此，内容和表达方面有任何问题，大家都可以在评论区、小册交流群和“神光的编程秘籍”公众号找到我，我会积极解答。

希望这本小册能让大家真正“通关”类型体操，成为类型编程高手，让我们一起加油吧！

## 10.套路六：特殊特性要记清

我们会了提取、构造、递归、数组长度的计数、联合类型的分散之后，各种类型体操都能写了 ，只不过有些类型的特性比较特殊，要专门记一下。

这是类型体操的第六个套路：特殊特性要记清。

## 特殊类型的特性

TypeScript 类型系统中有些类型比较特殊，比如 any、never、联合类型，比如 class 有 public、protected、private 的属性，比如索引类型有具体的索引和可索引签名，索引还有可选和非可选。。。

如果给我们一种类型让我们判断是什么类型，应该怎么做呢？

**类型的判断要根据它的特性来，比如判断联合类型就要根据它的 distributive 的特性。**

我们分别看一下这些特性：

## IsAny

如何判断一个类型是 any 类型呢？要根据它的特性来：

**any 类型与任何类型的交叉都是 any，也就是 1 & any 结果是 any。**

所以，可以这样写：

```typescript
type IsAny<T> = 'dong' extends ('guang' & T) ? true : false
```

这里的 'dong' 和 'guang' 可以换成任意两个不同的类型。

当传入 any 时：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abb4cd2ddfca4231b6d00d1838e4d32e~tplv-k3u1fbpfcp-watermark.image?)

当传入其他类型时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80819aa037ad4ad58999c084fc6381e9~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAkgzgQQHYgDwBUB8UC8UDkAJgPZIDm+UEAHsBEoXFABT5kCuAhuZQGRToAlFAD8UYACd20AFxQAZpwA2cCACg1oSLEQoAShDjslwXDuRpuITAG4NW6PAsGjJgExmnKVGy49bGkA)
## IsEqual

之前我们实现 IsEqual 是这样写的：

```typescript
type IsEqual<A, B> = (A extends B ? true : false) & (B extends A ? true : false);
```
问题也出在 any 的判断上：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85ce35a062d14dd0920f8bd02ed6a6a3~tplv-k3u1fbpfcp-watermark.image?)

因为 any 可以是任何类型，任何类型也都是 any，所以当这样写判断不出 any 类型来。

所以，我们会这样写：
```typescript
type IsEqual2<A, B> = (<T>() => T extends A ? 1 : 2) extends (<T>() => T extends B ? 1 : 2)
    ? true : false;
```

这样就能正常判断了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e9cde7dcbc14ac3ab75299dc4006ee2~tplv-k3u1fbpfcp-watermark.image?)

这是因为 TS 对这种形式的类型做了特殊处理，是一种 hack 的写法，它的解释要从 TypeScript 源码找答案了，我放到了[原理篇](https://juejin.cn/book/7047524421182947366/section/7064835788197855272)。感兴趣可以提前看一下。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAkgzgUQI4FcCGAbAPAQQDRQBCAfFALxQAUOUEAHsBAHYAmcRUA-FMAE4rQAXFABmmOBACUUAGRVCtBszZQa3PgKjCxGCZIDcAKEOhIsRKkwAlCOwrxk6bAHI0zgmiYhiRk+GgOlhgATLgEJORUWAAqxJTSZKTRioys7GpQAIxaUMHS9KkqlDFxCUkpyuwK3NnCeYZQjVw8-EKi4hC+pgEWTsE2duaOmKGu7lCe3kZAA)

## IsUnion

还记得怎么判断 union 类型么？要根据它遇到条件类型时会分散成单个传入做计算的特性：

```typescript
type IsUnion<A, B = A> =
    A extends A
        ? [B] extends [A]
            ? false
            : true
        : never
```
这里的 A 是单个类型，B 是整个联合类型，所以根据 [B] extends [A] 是否成立来判断是否是联合类型。（详见上节）

当传入联合类型时：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21efe0828fd34d4697cde01a52baab87~tplv-k3u1fbpfcp-watermark.image?)

当传入单个类型时：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38909d7f1357448d92c66dae83cc4712~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAkgzgVQHYEsD2SA8BBANFAISgF4psA+EgKClrKggA9gIkATOMmungfigDaBALoNmrDoOzDuPOVH4AzAIYAbOBFny6ALijAATgFdN2qHqQQAbhANV7oSLESoMAJQidS8ZOiwBGKAAfKAAmcgBuB3BoH1ckDzhQkmdfDEx-SPsqIA)

## IsNever

never 在条件类型中也比较特殊，如果条件类型左边是类型参数，并且传入的是 never，那么直接返回 never：

```typescript
type TestNever<T> = T extends number ? 1 : 2;
```

当 T 为 never 时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f0cbf1c3e854c6c81d0fedaa2f59623~tplv-k3u1fbpfcp-watermark.image?)

所以，要判断 never 类型，就不能直接 T extends number，可以这样写：

```typescript
type IsNever<T> = [T] extends [never] ? true : false
```

这样就能正常判断 never 类型了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c4da85cd8e04adba5f2686783cb96c4~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAKhDOwByEBuEBOAeGA+KAvLFBAB7AQB2AJvFJQK4C2ARplAPxQCMUAXFABMAbgBQo0JFgJkaTACUEhaYhTpslORlxiJ4aAEl4azDnxEA2jAC6JclVpQLm9ba7AMDaAIBmAQwAbeAhxSUNjLUU6IiMTDS0dcSA)

除此以外，any 在条件类型中也比较特殊，如果类型参数为 any，会直接返回 trueType 和 falseType 的合并：
```typescript
type TestAny<T> = T extends number ? 1 : 2;
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbb5bc38a89546d39f148f35734bddf1~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAKhDOwCCA7EAeGA+KBeWUEAHsBCgCbxQoCuAtgEYQBOUA-FAIxQBcUATAG4AUMNCRYCZGgBKCPJMSoMAQzRYRorcKA)

联合类型、never、any 在作为条件类型的类型参数时的这些特殊情况，也会在后面的原理篇来解释原因。

## IsTuple

元组类型怎么判断呢？它和数组有什么区别呢？

**元组类型的 length 是数字字面量，而数组的 length 是 number。**

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/205d44d023d643c6a9ea699546b00ac2~tplv-k3u1fbpfcp-watermark.image?)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b25014d24e974970920261b675e57faa~tplv-k3u1fbpfcp-watermark.image?)

如图，元组和数组的 length 属性值是有区别的。

那我们就可以根据这两个特性来判断元组类型：

```typescript
type IsTuple<T> = 
    T extends [...params: infer Eles] 
        ? NotEqual<Eles['length'], number> 
        : false
```


类型参数 T 是要判断的类型。

首先判断 T 是否是数组类型，如果不是则返回 false。如果是继续判断 length 属性是否是 number。

如果是数组并且 length 不是 number 类型，那就代表 T 是元组。

NotEqual 的实现是这样的：
```typescript
type NotEqual<A, B> = 
    (<T>() => T extends A ? 1 : 2) extends (<T>() => T extends B ? 1 : 2)
    ? false : true;
```
A 是 B 类型，并且 B 也是 A 类型，那么就是同一个类型，返回 false，否则返回 true。

这样就可以判断出元组类型：

当传入元组时：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12c6d0c40cce4add8433368888184797~tplv-k3u1fbpfcp-watermark.image?)

当传入数组时：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69bf9c23dbfd403f9f90eb34c9a42545~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBANhB2UC8UDaBGANAJkwZgF1UByOeAc2AAtiCBuAKAdElgW2SngFcBbAIwgAnVEVIJKNAkxbQAkgGcAKtzBwAPEoB8nBlH1QlUCAA9gCACYK0AOjtgAhkIe8FALigBLeADNhUAFE4BQIoPQMIgH4oADkAe2AAgEduBxh1IIgFEjJJWkwuPkEhHXCI-Q8fNIUIRmZwaHjElLT1AEECgCEdFDKoAApNLX6ASmQdI1NzeCsoNqho9CgPbDGpy2tB7VHxw2MzDahOhagllZG+6KqYGuWoYCFuWqZ61kUVNQgAJSzuGGBOO9VBoMAVcFBCFo6rIoEDPj8FH9gBwUHCNDwBMJRFCgA)

## UnionToIntersection

类型之间是有父子关系的，更具体的那个是子类型，比如 A 和 B 的交叉类型 A & B 就是联合类型 A | B 的子类型，因为更具体。

如果允许父类型赋值给子类型，就叫做**逆变**。

如果允许子类型赋值给父类型，就叫做**协变**。

（关于逆变、协变等概念的详细解释可以看原理篇）

在 TypeScript 中有函数参数是有逆变的性质的，也就是如果参数可能是多个类型，参数类型会变成它们的交叉类型。

所以联合转交叉可以这样实现 ：

```typescript
type UnionToIntersection<U> = 
    (U extends U ? (x: U) => unknown : never) extends (x: infer R) => unknown
        ? R
        : never
```

类型参数 U 是要转换的联合类型。

U extends U 是为了触发联合类型的 distributive 的性质，让每个类型单独传入做计算，最后合并。

利用 U 做为参数构造个函数，通过模式匹配取参数的类型。

结果就是交叉类型：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07cb622007ca464ba9cd42c4a91e39f3~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAqgOwJYHsEBUUEkEigJwGcoBjEVBAHjgD4YBeGYGFmACjhigA88EATQvBgB+dtwBc8AJQM6AVwQBrBCgDuCGFIRQAbgVk8+g8VKQIAZgRgAlWfQXLVG5qzdibrty216CAbmBQSFhECkwcPCJScjQbKEJ5ABsQBnhkNAjcAmIyCkoAbxgAc3kAQwRiqQBGGABfGAAfGCL+NCqYACZ6mn8gA)

函数参数的逆变性质一般就联合类型转交叉类型会用，记住就行。

## GetOptional

如何提取索引类型中的可选索引呢？

这也要利用可选索引的特性：**可选索引的值为 undefined 和值类型的联合类型**。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21ec2555c40d4830a94f996ca24c5313~tplv-k3u1fbpfcp-watermark.image?)

过滤可选索引，就要构造一个新的索引类型，过程中做过滤：

```typescript
type GetOptional<Obj extends  Record<string, any>> = {
    [
        Key in keyof Obj 
            as {} extends Pick<Obj, Key> ? Key : never
    ] : Obj[Key];
}
```
类型参数 Obj 为待处理的索引类型，类型约束为索引为 string、值为任意类型的索引类型 Record<string, any>。

用映射类型的语法重新构造索引类型，索引是之前的索引也就是 Key in keyof Obj，但要做一些过滤，也就是 as 之后的部分。

过滤的方式就是单独取出该索引之后，判断空对象是否是其子类型。

这里的 Pick 是 ts 提供的内置高级类型，就是取出某个 Key 构造新的索引类型：

```typescript
type Pick<T, K extends keyof T> = { [P in K]: T[P]; }
```

比如单独取出 age 构造的新的索引类型是这样的：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43f684f0a3d744849f3f4129fceb85ba~tplv-k3u1fbpfcp-watermark.image?)

可选的意思是这个索引可能没有，没有的时候，那 Pick<Obj, Key> 就是空的，所以 {} extends Pick<Obj, Key> 就能过滤出可选索引。

值的类型依然是之前的，也就是 Obj[Key]。

这样，就能过滤出所有可选索引，构造成新的索引类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c0cdb56dfe343229a5f9136f52980c6~tplv-k3u1fbpfcp-watermark.image?)

注意，可选不是值可能是 undefined 的意思，比如这样：

```typescript
type Obj = {
    a: 'aaa' | undefined
};
```
这个 a 的索引是可选的么？

明显不是，加上 ? 才是。
```typescript
type Obj = {
    a?: 'aaa' | undefined
};
```

可选的意思是指有没有这个索引，而不是索引值是不是可能 undefined。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwHkzAJYHsB2BDANgHgQCMArKCAD2AgwBMBnKKAJQgGM0AnGvO4DlDAHMANFCwYQAPklQAvFADeAKEaMA2itVaA0hBBQBUANZ60AMyhFSmrbbEMFAXzKVq9KAAUUrIwRKjdKSgAfihAqAAuKAwIADcIDhsoAF1IyxI1QOSAbiVHJQLQSFh4JFRMXBY6AFccYDkSxGR0bHxlRmwAWwgo3n4hXMYsQQhgqIxqzsIE3MdJXKA)

## GetRequired

实现了 GetOptional，那反过来就是 GetRequired，也就是过滤所有非可选的索引构造成新的索引类型：

```typescript
type isRequired<Key extends keyof Obj, Obj> = 
    {} extends Pick<Obj, Key> ? never : Key;

type GetRequired<Obj extends Record<string, any>> = { 
    [Key in keyof Obj as isRequired<Key, Obj>]: Obj[Key] 
}
```
这样就过滤出了非可选类型：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e89490dd2e64506b743bf99911947a2~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAlgzgJQgRwK4wE4QCYB4DSEIUEAHsBAHbZxQDWRA9gGZQDyARgFYA073APigBeKACgokqAG8AviXJUaUAAowAxnVydeUQiCEB+KJQgA3CBigAuPUQDcYsaEhQA4hGBI0mHNu4KFNS0SOqMGHhwwBgwlADmfACGlAZCotLiUlAA2vqwlPRMrDpQibTw3uhYePp8OgIAurY6uUQN4rJOLtAeXihVOEhwqAA2wCLunpW+eNISJokAthC2UTHxjpKJcRCGtpSoixyWjrICjkA)

## RemoveIndexSignature

索引类型可能有索引，也可能有可索引签名。

比如：

```typescript
type Dong = {
  [key: string]: any;
  sleep(): void;
}
```
这里的 sleep 是具体的索引，[key: string]:  any 就是可索引签名，代表可以添加任意个 string 类型的索引。

如果想删除索引类型中的可索引签名呢？

同样根据它的性质，**索引签名不能构造成字符串字面量类型，因为它没有名字，而其他索引可以。**

所以，就可以这样过滤：

```typescript
type RemoveIndexSignature<Obj extends Record<string, any>> = {
  [
      Key in keyof Obj 
          as Key extends `${infer Str}`? Str : never
  ]: Obj[Key]
}
```
类型参数 Obj 是待处理的索引类型，约束为 Record<string, any>。

通过映射类型语法构造新的索引类型，索引是之前的索引 Key in keyof Obj，但要做一些过滤，也就是 as 之后的部分。

如果索引是字符串字面量类型，那么就保留，否则返回 never，代表过滤掉。

值保持不变，也就是 Obj[Key]。

这样就可以过滤掉可索引签名：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8191b63d4d8464fac18a14caa716aae~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAShC2B7AbhAkgOwCYQB4GUBLAcwwENgBXAJwgB4B5AIwCso9gJsBnWCAY0TUsdbsGqEMxADRQyGEAD5FUALxQA3gCgoUANo7dRgNIQQUSVADWZxADMozNoaOu5vU+Y5csvAAYAJBqSdhDUUPjiAL5+APwR4lAAXFAYEKjUhgC6KU56nllaUVpaoJB8SKiYOAQk5FS0cNyUADbAahUo6Nh4RKQUNPTauno2ICliElI5cgoA3IbcLRAQYAAUAJQpyIiEWAtRinNAA)

## ClassPublicProps

如何过滤出 class 的 public 的属性呢？

也同样是根据它的特性：**keyof 只能拿到 class 的 public 索引，private 和 protected 的索引会被忽略**。

比如这样一个 class：

```typescript
class Dong {
  public name: string;
  protected age: number;
  private hobbies: string[];

  constructor() {
    this.name = 'dong';
    this.age = 20;
    this.hobbies = ['sleep', 'eat'];
  }
}
```

keyof 拿到的只有 name：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef7cab845ac047ac99d660c506df00e9~tplv-k3u1fbpfcp-watermark.image?)


所以，我们就可以根据这个特性实现 public 索引的过滤：

```typescript
type ClassPublicProps<Obj extends Record<string, any>> = {
    [Key in keyof Obj]: Obj[Key]    
}
```

类型参数 Obj 为带处理的索引类型，类和对象都是索引类型，约束为 Record<string, any>。

构造新的索引类型，索引是 keyof Obj 过滤出的索引，也就是 public 的索引。

值保持不变，依然是 Obj[Key]。

这样就能过滤出 public 的属性：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8e72f143c894f6cb2c2d3a5b01e56ca~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/MYGwhgzhAEAiD2A7A5tA3gKGtADgVwCMQBLYaRMAWwFMAuaCAFwCdiUBuLXZ+R64PgBNoYZHXJ5KBas07YcrAG5g+0ABbwCBYtQj0mrFAG0Aupy7AkBvAPjMAFAEp0XbIzXEIAOgo1oAXmgAckEkZCC5bGh3Ty9RagDoACYABki3D28NLR0YQKMgiBBqahwggBpg6hUgsy4AXwxGjEYATxwEgGFwKAAFQhJgXp4cCAAlXTwQRkTuyAh+olJh+FGAHgQUAD5zFvaunoWB5ZGINYB5AgAraGoADz5EQRgJy2ZBNYM2ZEqwRFatltEpgotAjABpaitaBsaAAayh8AAZtBLlcTPQ0RCoSZQU0MASgA)


## as const

TypeScript 默认推导出来的类型并不是字面量类型。

比如对象：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ccdec675fc274baca8b9814f232fc4b8~tplv-k3u1fbpfcp-watermark.image?)

数组：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcb1821d51ce4668abb6eb0414a576d8~tplv-k3u1fbpfcp-watermark.image?)

但是类型编程很多时候是需要推导出字面量类型的，这时候就需要用 as const：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1adbd21953043aa859e3dffc9e0dae5~tplv-k3u1fbpfcp-watermark.image?)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a15a03d6c8845279a6c87f71cc6a631~tplv-k3u1fbpfcp-watermark.image?)

但是加上 as const 之后推导出来的类型是带有 readonly 修饰的，所以再通过模式匹配提取类型的时候也要加上 readonly 的修饰才行。

>const 是常量的意思，也就是说这个变量首先是一个字面量值，而且还不可修改，有字面量和 readonly 两重含义。所以加上 as const 会推导出 readonly 的字面量类型。 

比如反转那个三个元素的元组类型，不加上 readonly 再匹配是匹配不出来的：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a785c5929e3d45149fdcf35424ed5df1~tplv-k3u1fbpfcp-watermark.image?)

加上 readonly 之后就可以正常匹配了：


![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58e11d50a4c54327aff47b3987c38dc0~tplv-k3u1fbpfcp-watermark.image?)

这点在类型编程的实际应用中经常遇到，要注意一下。
[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/MYewdgzgLgBCBGArGBeGBvAUDHMCGAXDAIwA02u8RATJgL6aZQCeADgKZxIAqbnaLDiABmXRAG5GoSLDwAnOahgBtMjGqkYAZgC6jQZ3lzeHJQZH4FkzNOhjqSrLnxEyFHFXX18EGLajWTHxiJuwOAnwWCIjU1v6WcuEqahraOj5+4NCBBgmhSeaiRrGMQaYASuwAbuxyEOwAggoAPE1yAHxKbTDsAB5Q7GAAJr5y7HhD4AA2zCoAlmDCtTANmgtLigBCa4vLAMLpAPwqe5rbK+lEYNW1OcGVNXWNCpW+aA+19W3NRvnt4kA)

## 总结

学完前面 5 个套路，我们已经能够实现各种类型编程逻辑了，但一些类型的特性还是要记一下。在判断或者过滤类型的时候会用到：

- any 类型与任何类型的交叉都是 any，也就是 1 & any 结果是 any，可以用这个特性判断 any 类型。
- 联合类型作为类型参数出现在条件类型左侧时，会分散成单个类型传入，最后合并。
- never 作为类型参数出现在条件类型左侧时，会直接返回 never。
- any 作为类型参数出现在条件类型左侧时，会直接返回 trueType 和 falseType 的联合类型。
- 元组类型也是数组类型，但 length 是数字字面量，而数组的 length 是 number。可以用来判断元组类型。
- 函数参数处会发生逆变，可以用来实现联合类型转交叉类型。
- 可选索引的索引可能没有，那 Pick 出来的就可能是 {}，可以用来过滤可选索引，反过来也可以过滤非可选索引。
- 索引类型的索引为字符串字面量类型，而可索引签名不是，可以用这个特性过滤掉可索引签名。
- keyof 只能拿到 class 的 public 的索引，可以用来过滤出 public 的属性。
- 默认推导出来的不是字面量类型，加上 as const 可以推导出字面量类型，但带有 readonly 修饰，这样模式匹配的时候也得加上 readonly 才行。

这些类型的特性要专门记一下，其实过两遍就记住了。

熟悉了这些特殊的特性，配合提取、构造、递归、数组长度计数、联合分散这五种套路，就可以实现各种类型体操。

[本文案例的合并](https://www.typescriptlang.org/play?#code/PTAEEkGcEEDsE8BQAXeAHAphGCA8AVAPlAF5QByAEwHtYBzc0DAD2Q1kslAApy6BXAIb1GAMlD4AlKAD8oZACd+WAFygAZoIA2kDIhTosUOPABKGSPy3JS2E7mHxCAbn2pMdhOcvWATLeM8PiERF30QbABRAEchLQMPKBi43GgAGlAAIWIybmgmVnZOLNlQAEZQNV9pcW5MgrYOLny5CqrJVwSjSGTtbwCe2O1cckFyDMcwrqihrV9UjOzbbgJCbmkSYnwGoubSttBqnaaeVfXSLePi+tbKw8lEUCfSxWU7zR0MTvdu3rn+shJWbzUbjUCTToRKAAVVgAEtaNMYfDaAsSmRoDlHs98ixGsVoNjns85ABtTIAXSuXFJ0ApROJjLkH10DMZzzUrz07KealgGAAbhgFG5DNhYQjYN4rDZAZAJajyNBGAAfCiZchhH7ilFSiwy-xyhWwEbKqYgKAAOUFwqRkGtQoUq1spPwVLxu1ApP5jqpci5720rLtDuF0usA1DTp9wq1YqtNoU4eQhuwUYcCCm2vwFmQ9iItm2HpOsH4AFsAEbC-Z3XzfMU5yB5rwWQu5+wQ8LAKD4fhoLR6bUD2AusppXxpADMFNJ5GHdGQAAtyBT6x5h6nS5XhaSZ3P2Avl-S7b3+xhnWQGUXCidSQA6B9oQQKQRlyBqOGwdTVyIDyBUtkSVAS1qGQP5cF-CxZ3nJcVwyLcqwUYhAN5DQgy+UUPBAsDZjRJZL2JFYiHOTYJGpUAWnKWtpGLYoiLWDZLlorgbio9oUNKFlVHkJQMMw7pTwHZMBkE89STHQ4MmnLN40gUTk1THs+wHXAEJ3ClzWAY18GocBYDYBRdAAY2QSV+NAbTdP04VjNM1FoRyUAGW4aFyNcuRuGYNRoUY0B+FgABrWBqAAdxHPlExom86K80BP2-BRQFMXz-KC0LYA4uRTA4iLHTXLBLL0gzbMlYSyEK6zDIwEzJVwABvUABGEOg1AqABfUA1Qamh6CqUA2s0gBxDBkAAeTQOzYG0aZhrGibJWGUaKwAK3IpLquoBRKFwJsFE-OgJkzRy6oZUkOIAaQweA4pHAKruodRQCW1aOOJQQuDqjrmNAAAFOEjIC3BnoyS6nFKUG7hjEViSpNRntJUHV0QNr9Bmkbxsmvp9QjMhZoxhatHq7EprLDA1F2-bXCeQQ6AwGQ+XLRDXAGyFgFm8xYjhBQMEoaY4UgDn+C5nncAh767vgB6npWjJnschlPvIv6AaBmXQFB4g5Chu5Qfy0B2YwTnue257yPMIzNu2in6EOpxjqc4kEaum7QAlqXTfeuKBcNoXjdFq7ZZWwgKThlanfgACUbR5BBeFygyv1kbY79k6nhJsnQGtugqfBWn6dANSFGZzTzDLaghT0ygWAAZThOgpuQfhuemUvy4wSua7rhum-PU3vvNy2dsUfbbcIY7sTO9kIc-V37se03XvBLgxeirgAAMABI6vi6tq8UNq17kPfEty20nhD6XlvD+ko+1VuK44Tv68ERvuYT+-28f5ha+f1-z1Tr0EtybD3oBfRwOdIADgwGgdYagBTUDhJQYurgQAAGEtDvUgD9fgFYtD-R+goagaBICICMhgyAXAAAitA6CgAAWgHBeCjIF1fBnLOOc0CELYCZHmucM6Fw4XtAUL8sCLmoBWCscILDAL2vQXcnQngW1gLtfgJlNrnAAU8Jc-M7zp1sFQGh5Ac5aMXDommWAyC+AAAzGPkKYyAd4xESKkVwMgs5IEYGgWCcgGAX4rhzijW+Yp0GYOwbg-BhDiEJxCRQsJTCCFEMgLgah9ApjTBiVgxhETEmq1Wv3DaW0h6yIOuCI6thNFemnrdOel8L7w0RsSZGXYl6gCUU2UhtAmygHEatMgFTBCtTSAyCsVQmnTB6fgMUZAfhSx6Z0NpNhnyJTcRJCcoBpzmSWZMjw0zDBSyWfMzpNgempn6YM4ZoyOqewWZ0cZK1tkYFTDMx6JzDnKMWQoBQqZxIZDWdOFpNzUbai2YYJ5ezHpLLrECsU5hHS6GgJ81InzHIIsSt9bmggepaGuqSHeiV0g3QSlkDIeLQCoL9F6VBiwMh0khomW5d9Ezws+QCdacKMCoocJ8h5vgXBAA)







## 11.类型体操顺口溜

TypeScript 类型编程难么？

难。不然怎么会被叫做类型体操呢。

但其实类型体操是有套路的，我把类型体操的各种套路总结成了一个顺口溜：

**类型体操顺口溜**

**模式匹配做提取，重新构造做变换。**

**递归复用做循环，数组长度做计数。**

**联合分散可简化，特殊特性要记清。**

**基础扎实套路熟，类型体操可通关。**

逐句解释下：

## 模式匹配做提取

就像字符串可以通过正则提取子串一样，TypeScript 的类型也可以通过匹配一个模式类型来提取部分类型到 infer 声明的局部变量中返回。

比如提取函数类型的返回值类型：

```typescript
type GetReturnType<Func extends Function> = 
    Func extends (...args: any[]) => infer ReturnType 
        ? ReturnType 
        : never;
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4fe9c7f4a1644248c61771ea0b505a6~tplv-k3u1fbpfcp-watermark.image?)

## 重新构造做变换

TypeScript 类型系统可以通过 type 声明类型变量，通过 infer 声明局部变量，类型参数在类型编程中也相当于局部变量，但是它们都不能做修改，想要对类型做变换只能构造一个新的类型，在构造的过程中做过滤和转换。

在字符串、数组、函数、索引等类型都有很多应用，特别是索引类型。

比如把索引变为大写：

```typescript
type UppercaseKey<Obj extends Record<string, any>> = { 
    [Key in keyof Obj as Uppercase<Key & string>]: Obj[Key]
}
```
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10144e25a6424b7eadbf8f70e317d1c6~tplv-k3u1fbpfcp-watermark.image?)


## 递归复用做循环

在 TypeScript 类型编程中，遇到数量不确定问题时，就要条件反射的想到递归，每次只处理一个类型，剩下的放到下次递归，直到满足结束条件，就处理完了所有的类型。

比如把长度不确定的字符串转为联合类型：

```typescript
type StringToUnion<Str extends string> = 
    Str extends `${infer First}${infer Rest}`
        ? First | StringToUnion<Rest>
        : never;
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e2e1688af304c16b5ed60af0b335e3a~tplv-k3u1fbpfcp-watermark.image?)

## 数组长度做计数

TypeScript 类型系统没有加减乘除运算符，但是可以构造不同的数组再取 length 来得到相应的结果。这样就把数值运算转为了数组类型的构造和提取。

比如实现减法：

```typescript
type BuildArray<
    Length extends number, 
    Ele = unknown, 
    Arr extends unknown[] = []
> = Arr['length'] extends Length 
        ? Arr 
        : BuildArray<Length, Ele, [...Arr, Ele]>;

type Subtract<Num1 extends number, Num2 extends number> = 
    BuildArray<Num1> extends [...arr1: BuildArray<Num2>, ...arr2: infer Rest]
        ? Rest['length']
        : never;
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fc24ba7bf84d4c8e8fcc98a3ea73373c~tplv-k3u1fbpfcp-watermark.image?)

## 联合分散可简化

TypeScript 对联合类型做了特殊处理，当遇到字符串类型或者作为类型参数出现在条件类型左边的时候，会分散成单个的类型传入做计算，最后把计算结果合并为联合类型。

```typescript
type UppercaseA<Item extends string> = 
    Item extends 'a' ?  Uppercase<Item> : Item;
```
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/842143798583491aae9dbec0da327da8~tplv-k3u1fbpfcp-watermark.image?)

这样虽然简化了类型编程，但也带来了一些认知负担。

比如联合类型的判断是这样的：
```typescript
type IsUnion<A, B = A> =
    A extends A
        ? [B] extends [A]
            ? false
            : true
        : never
```

联合类型做为类型参数直接出现在条件类型左边的时候就会触发 distributive 特性，而不是直接出现在左边的时候不会。

所以， A 是单个类型、B 是整个联合类型。通过比较 A 和 B 来判断联合类型。

## 特殊特性要记清

会了提取、构造、递归、数组长度计数、联合类型分散这 5 个套路以后，各种类型体操都能写，但是有一些特殊类型的判断需要根据它的特性来，所以要重点记一下这些特性。

比如 any 和任何类型的交叉都为 any，可以用来判断 any 类型：

```typescript
type IsAny<T> = 'dong' extends ('guang' & T) ? true : false
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abb4cd2ddfca4231b6d00d1838e4d32e~tplv-k3u1fbpfcp-watermark.image?)

比如索引一般是 string，而可索引签名不是，可以根据这个来过滤掉可索引签名：

```typescript
type RemoveIndexSignature<Obj extends Record<string, any>> = {
  [
      Key in keyof Obj 
          as Key extends `${infer Str}`? Str : never
  ]: Obj[Key]
}
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e3a1599b76742b183d6514c883cf5a5~tplv-k3u1fbpfcp-watermark.image?)

## 基础扎实套路熟，类型体操可通关

基础指的是 TypeScript 类型系统中的各种类型，以及可以对它们做的各种类型运算逻辑，这是类型编程的原材料。

但是只是会了基础不懂一些套路也很难做好类型编程，所以要熟悉上面 6 种套路。

基础扎实、套路也熟了之后，各种类型编程问题都可以搞定，也就是“通关”。


## 练练手

在讲 “TypeScript 类型编程为什么被叫做类型体操” 的时候我举了一个 ParseQueryString 的类型例子，用来说明类型编程的复杂度。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb6ea7398df245c1976c514cad68a022~tplv-k3u1fbpfcp-watermark.image?)

学完了所有套路之后，我们来实现下这个类型：

### ParseQueryString

a=1&b=2&c=3&d=4，这样的字符串明显是 query param 个数不确定的，遇到数量不确定的问题，条件反射的就要想到递归：

递归解析出每一个 query params，也就是 & 分隔的每个字符串，每个字符串单独去解析，构造成索引类型，最后把这些所有的单个索引类型合并就行。

也就是这样的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d6b1dea00b0491caee0af438d59757a~tplv-k3u1fbpfcp-watermark.image?)

第一步并不知道有多少个 a=1、b=2 这种 query param，要递归的做模式匹配来提取。

然后每一个 query param 再通过模式匹配取出 key 和 value，构造成索引类型。

然后把每个索引类型合并成一个大的索引类型就可以了。

思路理清了，我们一步步来实现下。

首先，要递归的提取 & 分隔的 query param：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a124009479848e28d6befeb2be79a2b~tplv-k3u1fbpfcp-watermark.image?)

```typescript
type ParseQueryString<Str extends string> = 
    Str extends `${infer Param}&${infer Rest}`
        ? MergeParams<ParseParam<Param>, ParseQueryString<Rest>>
        : ParseParam<Str>;
```

类型参数 Str 为待处理的 query 字符串，通过 extends 约束为 string 类型。

提取 & 分割的字符串到 infer 声明的局部变量 Param 里，后面的字符串放到 Rest 里。

通过 ParseParam 来处理单个的 query param，剩下 query 字符串也是一样的递归处理，然后把这些处理结果合并到一起，也就是 MergeParams。

当提取不出 & 分割的字符串时递归结束，把剩下的字符串也用 ParseParam 来处理。

ParseParam 的实现就是提取和构造：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b484f57f63644ffb7dfeaba67e0ad27~tplv-k3u1fbpfcp-watermark.image?)

```typescript
type ParseParam<Param extends string> = 
    Param extends `${infer Key}=${infer Value}`
        ? {
            [K in Key]: Value 
        } : {};
```

类型参数 Param 类单个的 query param，比如 a=1 这种。

通过模式匹配提取 key 和 value 到 infer 声明的局部变量 Key、Value 里。

通过映射类型语法构造成索引类型返回：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b39ff138898740d6b50f577f26c07224~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBACghgJwM4XguBbAPGzUIAewEAdgCZJRLAICWJA5gHxQC8UAUFN7InocXKUABgBIA3vQBmEBFADSEEAF9WE6bKgA1OABsArhGXCuPMwH4o402dtQA2vKj0FSgLoAubXsOc73ZSgvcWUAbg4OUEheZFQ+DAAlCCR9XWA2GJRcbAByOFYARhymUKA)

每个 query param 处理完了，最后把这一系列构造出的索引类型合并成一个就行了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36e278c4148541409b255fd76f2d941a~tplv-k3u1fbpfcp-watermark.image?)

这也是构造索引类型：

```typescript
type MergeParams<
    OneParam extends Record<string, any>,
    OtherParam extends Record<string, any>
> = {
  [Key in keyof OneParam | keyof OtherParam]: 
    Key extends keyof OneParam
        ? Key extends keyof OtherParam
            ? MergeValues<OneParam[Key], OtherParam[Key]>
            : OneParam[Key]
        : Key extends keyof OtherParam 
            ? OtherParam[Key] 
            : never
}
```

类型参数 OneParam、OtherParam 是要合并的 query param，约束为索引类型（索引为 string，索引值为任意类型。

构造一个新的索引类型返回，索引来自两个的合并，也就是 Key in keyof OneParam | keyof OtherParam。

值也要做合并：

如果两个索引类型中都有，那就合并成一个，也就是 MergeValues<OneParam[Key], OtherParam[Key]>。

否则，如果是 OneParam 中的，就取 OneParam[Key]，如果是 OtherParam 中的，就取 OtherParam[Key]。

MegeValues 的合并逻辑就是如果两个值是同一个就返回一个，否则构造一个数组类型来合并：

```typescript
type MergeValues<One, Other> = 
    One extends Other 
        ? One
        : Other extends unknown[]
            ? [One, ...Other]
            : [One, Other];
```
类型参数 One、Other 是要合并的两个值。

如果两者是同一个类型，也就是 One extends Other，就返回任意一个。

否则，如果是数组就做数组合并，否则构造一个数组把两个类型放进去。

我们单独测试下索引合并：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a03341c9d5ac47c1832542efb5baab10~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAshBOBzCA1AhgGwK4QM4B4B5AOwgBopDgALBAPigF4oAoKdy0qCAD2AmIATXJRoJWHSVAD8nCGynsAXKNrxufAcKhZiAa2IB7AO7EA2gF0FiybLMlyUAHQuqaqzakr7pCm4QWANwsLKCQsAjIAApo8GgAtgTWcjFx8Rr8QiIAShAAxobwgvi4wPAAlsSIFGjEIHRkyf7wqQkZWjn5hcWlFVU1dXQsDMwA3gpmANIQIFCVUHozhgBmKbFtAD4LS6vNrfEWKsnTs7yZ2osgK2tpybZQJ+1Z21e7Yi3r8Xc2snBIqJgcAQHPspjMLH53qCThYhp5JCoQZ8wSAPDYVI8zh0Xtc9p8JPD2LI8WkURYCYSVKQAG4IFgAXxCYWgf2in1wuVwWAwwCYEX++wIoygaBUAEYoPSKMKAEYqABMkrowRCQA)

每个 query param 的解析和构造索引类型，多个索引类型的合并都实现了，合并起来也就实现了 query string 的解析：
```typescript
type ParseQueryString<Str extends string> = 
    Str extends `${infer Param}&${infer Rest}`
        ? MergeParams<ParseParam<Param>, ParseQueryString<Rest>>
        : ParseParam<Str>;
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/160e8f3e55424daaa3b2cb957b6e0d6e~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBACghgJwM4XguBbAPGzUIAewEAdgCZJRLAICWJA5gHxQC8UAUFN7InocXKUABgBIA3vQBmEBFADSEEAF9WE6bKgA1OABsArhGXCuPMwH4o402dtQA2vKj0FSgLoAubXsOc73ZSgvcWUAbg4OUEgoAFlZBggdAwgkLAB5EggAGig04AALWRZ2G1zM-CJSClyCzVKLMoh6ni88wrkBKsp9EgBrEgB7AHcSezdmu0t7DOyoADoFttlx-1svacycpYQ3cMjwaDiEBNwMVNKZ04rBaoAlCABjAYQyLGo6Rhy4EhAmLIvaggrp0hFB7k8Xm8aPQGF8fkwOMUrKZHEpnCQoL0lAMpI0rgAfTHY3HbU6ePw8RQga5dIkgHF4vgYCZQSxUmmgrH0kmA04shpHBJJQypS5M1EgNxbXniqluBGrMytTKnCUrfxedkg6pchmkpkUxWsmrtVVyw2KryZABusg4ygiUWgaBQAEVDAgQABlaGMLA+jqVUHvGFI0oBjnVMSSEgyOSnZQAMnUsc092oxhZlkFqCZqRdufQ2FOf14yAg7tk3t9DCw6eATAVGrLKFO-poTD2+2iBcrnoDMPT+l0wDYLYrHurH1rAHI4KwAIyJ+cAJkTACNWGuHqwAMwzzsRDhAA)

在实现 ParseQueryString 的类型的时候，我们大量用到了`模式匹配做提取`、`重新构造做变换`、`递归复用做循环`这 3 大套路，思路理清之后利用这些套路能够很顺畅的把这个高级类型写出来。

这是最开始被我用来说明类型编程复杂度的例子，是有一定复杂度的，而学到这我们也能实现了。

再回到最开始的问题：

TypeScript 类型编程难么？

其实熟悉一些套路以后，也没那么难。

## 总结

为了方便记忆，我总结了类型体操顺口溜，然后分别解释了每句话的含义，之后又做了一个类型体操来练手。

那个最开始被我用来说明 TypeScript 类型编程复杂度的例子，现在我们也能顺畅的实现了，所用的就是类型体操顺口溜中的套路。

这就像武功秘籍一样，理解了每句话的含义，反复修炼，就能成为类型体操的武林高手：

**模式匹配做提取，重新构造做变换。**

**递归复用做循环，数组长度做计数。**

**联合分散可简化，特殊特性要记清。**

**基础扎实套路熟，类型体操可通关。**


[本文案例的合并](https://www.typescriptlang.org/play?#code/C4TwDgpgBACghgJwM4XguBbAPGzUIAewEAdgCZJRLAICWJA5gHxQC8UAUFN7InocXKUABgBIA3vQBmEBFADSEEAF9WE6bKgA1OABsArhGXCuPMwH4o402dtQA2vKj0FSgLoAubXsOc73ZSgvcWUAbg4OUEheZFQ+DAAlCCR9XWA2GJRcbAByOFYARhymcMjwaABZWQYIHQNkrAB5EggAGihG4AALWRZ2Gw6W-CJSCg7uzQGLQYgpni9OnrkBUcp9EgBrEgB7AHcSezc5u0t7ZraoADprxdkj-1svM5b224Q3UqjK6rj0DCQsANztlhoIxkkAMbbBBkLDUOiMdpwEggJitIETBAglZCKCQ6Gw+H0BhIlFMDh9KymRxKZwkKAbJTbKQzEEAHwZTJZb2ynj8PEUIFBq05IGZrPixyglkFwtxjLF3Mx2Sl0yqCBqdUMAOB8RpIDcr2VesFbnJDzMCxa2X1938XllOLGCvFPPi-It0vGSxtpo9Fq8LQAbrIOMoIl8oOqatkkEkUmkMtHfpgAeIoHAvAUoMp2umAEZeABMOZKEfKmQgAEVDAgQABlGjErCN5YjXFExiUgatuVjMSSEgyOTZZQAMnUQ808eAxillmTsZwiCy8WXfzRlZrsgbTcYWBnTHN9sr2RbNDL5eiaBQ27rreJ8dS6XYN+rtd3CIYWDyhTH+SLMd81YQCIVYABmYpSg4IA)


## 12.TypeScript 内置的高级类型有哪些？

学完了 6 个类型体操的套路之后，各种类型编程逻辑我们都能写出来，但其实一些常见的类型不用自己写， TypeScript 内置了很多，这节我们就来看下 TypeScript 内置了哪些高级类型吧。

## Parameters

Parameters 用于提取函数类型的参数类型。

源码是这样的：
```typescript
type Parameters<T extends (...args: any) => any> 
    = T extends (...args: infer P) => any 
        ? P 
        : never;
```
类型参数 T 为待处理的类型，通过 extends 约束为函数，参数和返回值任意。

通过 extends 匹配一个模式类型，提取参数的类型到 infer 声明的局部变量 P 中返回。

这样就实现了函数参数类型的提取：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99d67cd9a6684cf6ba4c620a671586f4~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FDAuE8AcFMAIAUCGAnRBbaprIM4CVodYBeBFdTbHAHgAoA7CgLlh1GQEt6BzAGlkTdoLegFc0AI2wBKEgD5YAbwC+cgNwggA)

这就是个简单的模式匹配，学完套路一轻轻松松就写出来了。

## ReturnType

ReturnType 用于提取函数类型的返回值类型。

源码是这样的：

```typescript
type ReturnType<T extends (...args: any) => any> 
    = T extends (...args: any) => infer R 
        ? R 
        : any;
```
类型参数 T 为待处理的类型，通过 extends 约束为函数类型，参数和返回值任意。

用 T 匹配一个模式类型，提取返回值的类型到 infer 声明的局部变量 R 里返回。

这样就实现了函数返回值类型的提取：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67daadd0bfb741aeb7449fc5b5a4d528~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAShwFcBOA7AKuCcDOUC8s8y6mAPABQCU+AfFAOQAmA9igOb00DcAUEA)

和提取函数参数类型差不多，也是个简单的模式匹配。

## ConstructorParameters

构造器类型和函数类型的区别就是可以被 new。

Parameters 用于提取函数参数的类型，而 ConstructorParameters 用于提取构造器参数的类型。

源码是这样的：

```typescript
type ConstructorParameters<
    T extends abstract new (...args: any) => any
> = T extends abstract new (...args: infer P) => any 
    ? P 
    : never;
```
类型参数 T 是待处理的类型，通过 extends 约束为构造器类型，加个 abstract 代表不能直接被实例化（其实不加也行）。

用 T 匹配一个模式类型，提取参数的部分到 infer 声明的局部变量 P 里，返回 P。

这样就实现了构造器参数类型的提取：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e6b944be583a44e39fb722fbf5f7c660~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyxyIcAthAFzIZhSgDmA3AQL4EGiSyIrpRsIAMI46UAK4IwWKPiIkQEAO4AKMpRrimAShoChrDgTABPAA4pRIcVJlRUcKBQg8MAJQgZkAXmTXbaVlHZ0o3AB4DHAD6O1kAPlYgA)

构造器参数的提取依然是模式匹配。

## InstanceType

提取了构造器参数的类型，自然也可以提取构造器返回值的类型，就是 InstanceType。

源码是这样的：

```typescript
type InstanceType<
    T extends abstract new (...args: any) => any
> = T extends abstract new (...args: any) => infer R 
    ? R 
    : any;
```
整体和 ConstructorParameters 差不多，只不过提取的不再是参数了，而是返回值。

通过模式匹配提取返回值的类型到 infer 声明的局部变量 R 里返回。

这样就实现了构造器的实例类型的提取：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/141741744a7e4b40977545ed3953f417~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyxyIcAthAFzIZhSgDmA3AQL4EGiSyIrpRsIAMI46UAK4IwWKPiIkQEAO4AKMpRrimAShoChrDgTABPAA4oAkiDpwQSACoWIAJQgZkAXmQ27DiGdLAB4DHFFbeikZKAA+Vk4gA)

## ThisParameterType

函数里可以调用 this，这个 this 的类型也可以约束：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b710dd98e2fa4627a3f6dc53af644507~tplv-k3u1fbpfcp-watermark.image?)

同样，this 的类型也可以提取出来，通过 ThisParameterType 这个内置的高级类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2327b4304c14531bcc09bb189f19bb5~tplv-k3u1fbpfcp-watermark.image?)

它的源码是这样的：

```typescript
type ThisParameterType<T> = 
    T extends (this: infer U, ...args: any[]) => any 
        ? U 
        : unknown;
```

类型参数 T 为待处理的类型。

用 T 匹配一个模式类型，提取 this 的类型到 infer 声明的局部变量 U 里返回。

这样就实现了 this 类型的提取。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAChBOBnA9gOygXigbwFBQKlQEMBbCALigHIBzAV2NVutwF8BuXXAM3tQDGwAJZooACwgAbKcgAUwccMRU4SNAEoc+QgLQopEAHSzaCpYiMlyGrm24B6BxOmyjA4jLnY2t7qEgoABULGGJ4MghgBCDwCAAlCERMYNDwyOj4WMgAHgCIZB4XGWQAPi5cIA)


## OmitThisParameter

提取出 this 的类型之后，自然可以构造一个新的，比如删除 this 的类型可以用 OmitThisParameter。

它的源码是这样的：

```typescript
type OmitThisParameter<T> = 
    unknown extends ThisParameterType<T> 
        ? T 
        : T extends (...args: infer A) => infer R 
            ? (...args: A) => R 
            : T;
```

类型参数 T 为待处理的类型。

用 ThisParameterType 提取 T 的 this 类型，如果提取出来的类型是 unknown 或者 any，那么 unknown extends ThisParameterType<T>  就成立，也就是没有指定 this 的类型，所以直接返回 T。

否则，就通过模式匹配提取参数和返回值的类型到 infer 声明的局部变量 A 和 R 中，用它们构造新的函数类型返回。

这样，就实现了去掉 this 类型的目的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5a810ac624c4cdba0c94f4c8a4c2444~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAChBOBnA9gOygXigbwFBQKlQEMBbCALigHIBzAV2NVutwF8BuXXAM3tQDGwAJZooiYiAAUwABbDEVOEjQAaKMVqUi9UgCMEAShz5CAtCgA2EAHSXktGfMQ2S5Q10JR4EYPXjocgquZNAA1DSREZoQXGzcoJBQAPKkwsAAKs4wxPChwAgAShCImClpmdm5+QgAPIkQyDzikgB8XNxAA)

这个类型除了模式匹配做提取外，也用到了重新构造做变换，稍微复杂一些。

## Partial

索引类型可以通过映射类型的语法做修改，比如把索引变为可选。

```typescript
type Partial<T> = {
    [P in keyof T]?: T[P];
};
```

类型参数 T 为待处理的类型。

通过映射类型的语法构造一个新的索引类型返回，索引 P 是来源于之前的 T 类型的索引，也就是 P in keyof T，索引值的类型也是之前的，也就是 T[P]。

这样就实现了把索引类型的索引变为可选的效果：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaf2aaf69b3a405cb7814c1f0831cb4a~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBACghgJ2ASzgGwEoQM5QLyyIroA8A3gHZwC2EAXFAOQAmA9hQOaMA0UcH9KAEYAHAF8AfAG4AUEA)

## Required

可以把索引变为可选，也同样可以去掉可选，也就是 Required 类型：

```typescript
type Required<T> = {
    [P in keyof T]-?: T[P];
};
```
类型参数 T 为待处理的类型。

通过映射类型的语法构造一个新的索引类型，索引取自之前的索引，也就是 P in keyof T，但是要去掉可选，也就是 -?，值的类型也是之前的，就是 T[P]。

这样就实现了去掉可选修饰的目的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/387abbd0117b4199a349d0fc4e334698~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBASlAjgVwJYCcoBMEGcYC88SamWAPAN4B2AhgLZQD8AXDAORYD21A5uwBoYtXszYBGABwBfAHwBuYEA)

## Readonly

同样的方式，也可以添加 readonly 的修饰：

```typescript
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
};
```
类型参数 T 为待处理的类型。

通过映射类型的语法构造一个新的索引类型返回，索引和值的类型都是之前的，也就是 P in keyof T 和 T[P]，但是要加上 readonly 的修饰。

这样就实现了加上 readonly 的目的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8d17b29b91d4698a6ab371f375052b8~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBASlAhgEwPYDsA2YEGcYC88SaWYAPAN7qIC2UAXDAOSkDmzANDIm4zAEYAHAF8AfAG5g0oA)

## Pick

映射类型的语法用于构造新的索引类型，在构造的过程中可以对索引和值做一些修改或过滤。

比如可以用 Pick 实现过滤：

```typescript
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
};
```
类型参数 T 为待处理的类型，类型参数 K 为要过滤出的索引，通过 extends 约束为只能是 T 的索引的子集。

构造新的索引类型返回，索引取自 K，也就是 P in K，值则是它对应的原来的值，也就是 T[P]。

这样就实现了过滤的目的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c6aab247d894e9cbdd25a65ce85bd93~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBACgSwMYGsBKUDOMC89koA8A3gHYCGAtlAFwwDkAJgPakDm9ANDOW7TAEYAHN0xQAHnQEBfbvQrV6MAD4NeUegD4A3MD16gA)

## Record

Record 用于创建索引类型，传入 key 和值的类型：
```typescript
type Record<K extends keyof any, T> = {
    [P in K]: T;
};
```
这里很巧妙的用到了 keyof any，它的结果是 string | number | symbol：

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90de21446ebc4908907a896ffa364e91~tplv-k3u1fbpfcp-watermark.image?)

但如果你开启了 keyOfStringsOnly 的编译选项，它就只是 stirng 了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33a80dd9f582451c927659da6383dc4a~tplv-k3u1fbpfcp-watermark.image?)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bf798bfab794140b793582073d3bd43~tplv-k3u1fbpfcp-watermark.image?)

用 keyof any 是动态获取的，比直接写死 string | number | symbol 更好。

继续讲 Record 这个类型，它用映射类型的语法创建了新的索引类型，索引来自 K，也就是 P in K，值是传入的 T。

这样就用 K 和 T 构造出了对应的索引类型。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/349f4dfbe514412ea853c5445fc1fcf6~tplv-k3u1fbpfcp-watermark.image?)

当传入的 K 是 string | number | symbol，那么创建的就是有可索引签名的索引类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f1784d6043464d3ab7165e8c810207a1~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?strictFunctionTypes=false&keyofStringsOnly=true#code/C4TwDgpgBAShDGB7ATgEzgZygXlglqAPAOQCGxUAPlMQEbEA0UAdgK4C2tEyAfANwAoAaEh4kaTACYcYgoQzBkAS2YBzJm07d+AoA)

## Exclude

当想从一个联合类型中去掉一部分类型时，可以用 Exclude 类型：

```typescript
type Exclude<T, U> = T extends U ? never : T;
```
联合类型当作为类型参数出现在条件类型左边时，会被分散成单个类型传入，这叫做分布式条件类型。

所以写法上可以简化， T extends U 就是对每个类型的判断。

过滤掉 U 类型，剩下的类型组成联合类型。也就是取差集。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bb8199cf54b43b1b30f92f97378eadf~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?strictFunctionTypes=false&keyofStringsOnly=true#code/FAFwngDgpgBAogDwMYBsCuATKAlKBnGAXnmXSwB4ByAQ0pgB8ZKAjOxypNpjSgGidoMmrAHwBuYMCA)

这里用了分布式条件类型的性质，写法上可以简化。

## Extract

可以过滤掉，自然也可以保留，Exclude 反过来就是 Extract，也就是取交集：
```typescript
type Extract<T, U> = T extends U ? T : never;
```
![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30498193a76b4602ae90564c8e09fa17~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?strictFunctionTypes=false&keyofStringsOnly=true#code/FAFwngDgpgBAogDxAJwIYGMQCUoGcYC88SamAPAOSoUwA+MFARjfReiwwCYUA0D1dBswB8AbmDAgA)

## Omit

我们知道了 Pick 可以取出索引类型的一部分索引构造成新的索引类型，那反过来就是去掉这部分索引构造成新的索引类型。

可以结合 Exclude 来轻松实现：

```typescript
type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;
```
类型参数 T 为待处理的类型，类型参数 K 为索引允许的类型（string | number | symbol 或者 string）。

通过 Pick 取出一部分索引构造成新的索引类型，这里用 Exclude 把 K 对应的索引去掉，把剩下的索引保留。

这样就实现了删除一部分索引的目的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dd6fef61dff436b8c4826ebdf9a5465~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?strictFunctionTypes=false&keyofStringsOnly=true#code/C4TwDgpgBA8gtgS2AJQgZygXlo4AeAbwDsBDOCALgHIBzAVxKJqoBooSbKoAmABgF82VUuSoA+ANxA)

## Awaited

在递归那节我们写过取 Promise 的 ValuType 的高级类型，这个比较常用，ts 也给内置了，就是 Awaited。

它的实现比我们当时写的完善一些：

```typescript
type Awaited<T> =
    T extends null | undefined
        ? T 
        : T extends object & { then(onfulfilled: infer F): any }
            ? F extends ((value: infer V, ...args: any) => any)
                ? Awaited<V>
                : never 
            : T;
```
类型参数 T 是待处理的类型。

如果 T 是 null 或者 undefined，就返回 T。

如果 T 是对象并且有 then 方法，那就提取 then 的参数，也就是 onfulfilled 函数的类型到 infer 声明的局部变量 F。

继续提取 onfullfilled 函数类型的第一个参数的类型，也就是 Promise 返回的值的类型到 infer 声明的局部变量 V。

递归的处理提取出来的 V，直到不再满足上面的条件。

这样就实现了取出嵌套 Promise 的值的类型的目的:

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d42e45b31e14cad9dfe24b5793619c3~tplv-k3u1fbpfcp-watermark.image?)

为什么要提取 then 方法的第一个参数的返回值类型看下 Promise 的结构就明白了：

```typescript
new Promise(() => {
    // xxx
}).then((value) => {
});
```

then 第一个参数是 onfullfilled 的回调，从它的第一个参数就能拿到返回的值的类型。

对比下我们之前的实现：

```typescript
type DeepPromiseValueType2<T> = 
    T extends Promise<infer ValueType> 
        ? DeepPromiseValueType2<ValueType>
        : T;
```

内置的高级类型不再限制必须是 Promise，而是只要对象且有 then 方法就可以，这样更通用了一些。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAgg7gQwJbAgEwEoQM5QLyyIroA8ACgE4D2AtkthOdXQ07fYwHYCuNARhAoA+EUIDcAKClA)

## NonNullable

NonNullable 就是用于判断是否为非空类型，也就是不是 null 或者 undefined 的类型的，实现比较简单：

```typescript
type NonNullable<T> = T extends null | undefined ? never : T;
```

当传入 null 时：
![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1151cae3cac147bdbbfa531b851b96a2~tplv-k3u1fbpfcp-watermark.image?)

当传入非空类型时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2375ad9567704f8b95bc5f3641769d6b~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAcg9gOxgVwDaoIYCNUQEoQDOUAvLIiutrgDwJqoB8A3AFCiTlIPX5EBMpLpUw4INAN4IMAWwgAuKAHIA5sgwIVSgL4tWQA)


## Uppercase、Lowercase、Capitalize、Uncapitalize

这四个类型是分别实现大写、小写、首字母大写、去掉首字母大写的。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea77857ae7bf47c2b51da61f04508e53~tplv-k3u1fbpfcp-watermark.image?)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/569e19b659154cb39251149a3a7f4491~tplv-k3u1fbpfcp-watermark.image?)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b732fe0081f402abc6f33bf60099487~tplv-k3u1fbpfcp-watermark.image?)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8a63df269774d3ea27cd45ec72bd2a9~tplv-k3u1fbpfcp-watermark.image?)

它们的源码时这样的：
```typescript
type Uppercase<S extends string> = intrinsic;

type Lowercase<S extends string> = intrinsic;

type Capitalize<S extends string> = intrinsic;

type Uncapitalize<S extends string> = intrinsic;
```
啥情况，intrinsic 是啥？

这个 intrinsic 是固有的意思，就像 js 里面的有的方法打印会显示 [native code] 一样。这部分类型不是在 ts 里实现的，而是编译过程中由 js 实现的。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d17dbb647124f9a978654774f7dd0cd~tplv-k3u1fbpfcp-watermark.image?)

我们可以在源码里找到对应的处理代码：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/699c89c324654dd4bf176c223cb14dda~tplv-k3u1fbpfcp-watermark.image?)

其实就是 ts 编译器处理到这几个类型时就直接用 js 给算出来了。

为啥要这样做呢？

因为快啊，解析类型是要处理 AST 的，性能比较差，用 js 直接给算出来那多快呀。

这几个类型的原理在原理篇也会带大家 debug 下源码。

[试一下](https://www.typescriptlang.org/play?strictFunctionTypes=false&keyofStringsOnly=true#code/C4TwDgpgBAqmkCcDGBDAzhAShNUC8s8Ey6EAPAOQrUoUB8A3AFBOiRQAyA9gO7GoZsuAtz4kMlAILT6zVuGgBhFGACWwFABtVALyw58UZWo3a9lGrJZtoMAHaoTW3fuGwHK9c-MVJ1K0A)

这基本就是全部的内置高级类型了。

## 总结

虽然我们学完 6 个套路，各种类型编程逻辑都能写了，但是常用的类型 TS 已经内置了。

这些内置的高级类型用我们学的套路很容易可以实现。

比如用模式匹配可以实现：Parameters、ReturnType、ConstructorParameters、InstanceType、ThisParameterType。

用模式匹配 + 重新构造可以实现：OmitThisParameter

用重新构造可以实现：Partial、Required、Readonly、Pick、Record

用模式匹配 + 递归可以实现： Awaited

用联合类型在分布式条件类型的特性可以实现： Exclude

此外还有 NonNullable 和四个编译器内部实现的类型：Uppercase、Lowercase、Capitalize、Uncapitalize。

这些类型也不咋需要记，就算忘记了自己也能很快的实现。重点还是放在 6 个类型编程的套路上。

[本文的案例合并](https://www.typescriptlang.org/play?#code/FAFwngDgpgBACgQwE4ILZRFJBnASlbGAXnmTQy2wB4AKAO3IC4ZsQkBLOgcwBoYEuUZnQCuqAEZYAlMQB8MAN4BfWQG5goSLHwgRSOgBUt+QiR17DW2jKLyA5ABMA9tztqNnTEgBmCAMawcJQuisAw4TAM6MysHNzqSh50Xr4B8MF0AMIusSJ+IE5IoRGRUADu9EwsbJxcUsxBOC4JGuDQMNl0ufmFiCjoXngExB05bHkFSH3kg1SN2C6d3ZPumu0Akl0gCHQBRtAmI5usO3tW84tjSBOFq94iuyDsIQAWUAA27040IC-s2A0MjIFGEIn4ck53lAAHRfLg-P7YaFRKBSFrAAD0GJgb0+TmhfgQnxoyjRrS0MAMiOmAyw+yghxIVP+NIoSHpVDaUCc3hxHy+dwe+WedBYCDACP+gKadD4AiEkTEkiQwNB4XBXUhMLhkqRKLJJSQGAsMF+-2R5BgAGoYHZbdb+IJ0VyYAB5VDsEDM7CsryMt0er3Usi0pCcrQ8sVgVYu92e-1xkBUBQoxh2LgiHZcOxywTMABMAAYlHw7Ci3Oo1oFkE8if6+rX3snU7bnK5cwqAIwADhUlZd+AAjiJ2EaHP6hyOx83yAB+ZiOFzZjvzmA9vvk9r4BBt95gCdQHcuPcz6Ktpc5x1d3urKvwdh+ADW9Yfj9PCsX7avzB7fGwUAADx-EtbXLGAAB9bXlCsNDvfBwSQcdhjMKAEIcKg7AQO1ILscRL1ECQsBjCl4MKJDsHzEZSMQqhYlqPgCOVW8XQAUQAvx3hEBwGWQmA2I4rioAwrCINtPDRLsPxsNbS9MOk3CYLvNi2H8EB-WUlB8mE+TxJwqSJIcWSRJwvDbzvAA5FxzJET4EHEKF-UsuhrNs+yhNET5iPaJyXPeOyHIISiSB8my-Lc98FwzLM7A3WCXQAVQgaAkEJf9-US5LUqEzCEFyxSXQAGScMosCy-0ipKlKEH-DCAEF6vyilMgQCBPSJdgAC8eNMDoWra95Ouy3KsK82B4t2PrtgGrr0om1qpsGuq8rM2DgCAA)




## 13.真实案例说明类型编程的意义

我们学了类型编程的各种套路，写了很多高级类型，也学了 TypeScript 内置的高级类型，对类型编程这一块算是有一定程度的掌握了。

那么类型编程在实际开发中会用到么？它的意义是什么呢？这节我们就通过一些案例来说明类型编程有什么用。

## 类型编程的意义

ts 基础是学习怎么给 js 代码声明各种类型，比如索引类型、函数类型、数组类型等，但是如果需要动态生成一些类型，或者对类型做一些变化呢？

这就是类型编程做的事情了，**类型编程可以动态生成类型，对已有类型做修改。**

类型编程是对类型参数做一系列运算之后产生新的类型。需要动态生成类型的场景必然会用到类型编程，比如返回值的类型和参数的类型有一定的关系，需要经过计算才能得到。

有的情况下不用类型编程也行，比如返回值可以是一个字符串类型 string，但用了类型编程的话，可能能更精确的提示出是什么 string，也就是具体的字符串字面量类型，那类型提示的精准度自然就提高了一个级别，体验也会更好。

这就是类型编程的意义：**需要动态生成类型的场景，必然要用类型编程做一些运算。有的场景下可以不用类型编程，但是用了能够有更精准的类型提示和检查。**

我们还是通过例子来说明：

## ParseQueryString

前面我们实现了一个复杂的高级类型 ParseQueryString，用到了提取、构造、递归的套路。

这么复杂的高级类型能用在哪里呢？有什么意义呢？想必很多同学都有疑问，那么我们就先聊一下这个高级类型的应用场景。

首先，我们写一个 JS 函数，实现对 query string 的 parse，如果有同名的参数就合并，大概实现是这样的：

```javascript
function parseQueryString(queryStr) {
    if (!queryStr || !queryStr.length) {
        return {};
    }
    const queryObj = {};
    const items = queryStr.split('&');
    items.forEach(item => {
        const [key, value] = item.split('=');
        if (queryObj[key]) {
            if(Array.isArray(queryObj[key])) {
                queryObj[key].push(value);
            } else {
                queryObj[key] = [queryObj[key], value]
            }
        } else {
            queryObj[key] = value;
        }
    });
    return queryObj;
}
```
这种逻辑大家写的很多，就不过多解释了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/973f2f48fdfe40e0baf2964034c2446b~tplv-k3u1fbpfcp-watermark.image?)

如果要给这个函数加上类型，大家会怎么加呢？

大部分人会这么加：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/750ad522ae2a4e23be10b30585ba4123~tplv-k3u1fbpfcp-watermark.image?)

参数是 string 类型，返回值是 parse 之后的对象类型 object。

这样是可以的，而且 object 还可以写成 Record<string, any>，因为对象是索引类型（索引类型就是聚合多个元素的类型，比如对象、class、数组都是）。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e29edcec6a2e4c529f9095b1df14d970~tplv-k3u1fbpfcp-watermark.image?)

Record 前面介绍过，是 TS 内置的一个高级类型，会通过映射类型的语法来生成索引类型：

```typescript
type Record<K extends string | number | symbol, T> = { 
    [P in K]: T;
}
```
比如传入 'a' | 'b' 作为 key，1 作为 value，就可以生成这样索引类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2e0e902ab9d48a79e9787fca7598a39~tplv-k3u1fbpfcp-watermark.image?)

所以这里的 Record<string, any> 也就是 key 为 string 类型，value 为任意类型的索引类型，可以代替 object 来用，更加语义化一点：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8908ce097f5341bf90186b5e0fdfae87~tplv-k3u1fbpfcp-watermark.image?)

但是不管是返回值类型为 object 还是 Record<string, any> 都存在一个问题：返回的对象不能提示出有哪些属性：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b60478e37b0d4c689259a02188a439bf~tplv-k3u1fbpfcp-watermark.image?)

对于习惯了 ts 的提示的同学来说，没有提示太不爽了。怎么能让这个函数的返回的类型有提示呢？

这就要用到类型编程了。

我们把函数的类型定义改成这样：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db17d40d01e9452e90fd3939a2b42fbe~tplv-k3u1fbpfcp-watermark.image?)

声明一个类型参数 Str，约束为 string 类型，函数参数的类型指定是这个 Str，返回值的类型通过对 Str 做类型运算得到，也就是 ParseQueryString\<Str>。

这个 ParseQueryString 的类型做的事情就是把传入的 Str 通过各种类型运算产生对应的索引类型。

这样返回的类型就有提示了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6af44e3251ee447e80a01f29334c5785~tplv-k3u1fbpfcp-watermark.image?)

这里最好通过函数重载的方式来声明类型，不然返回值可能和 ParseQueryString<Str> 的返回值类型匹配不上，需要 as any 才行，那样比较麻烦。

这里的 ParseQueryString 就是前面实现的那个高级类型，在这里可以用来实现更精准的类型提示，这就是类型体操的意义。


这个类型的实现思路可以看顺口溜那节，就不赘述了：

```typescript
type ParseParam<Param extends string> = 
    Param extends `${infer Key}=${infer Value}`
        ? {
            [K in Key]: Value 
        } : Record<string, any>;

type MergeValues<One, Other> = 
    One extends Other 
        ? One
        : Other extends unknown[]
            ? [One, ...Other]
            : [One, Other];

type MergeParams<
    OneParam extends Record<string, any>,
    OtherParam extends Record<string, any>
> = {
  readonly [Key in keyof OneParam | keyof OtherParam]: 
    Key extends keyof OneParam
        ? Key extends keyof OtherParam
            ? MergeValues<OneParam[Key], OtherParam[Key]>
            : OneParam[Key]
        : Key extends keyof OtherParam 
            ? OtherParam[Key] 
            : never
}

type ParseQueryString<Str extends string> = 
    Str extends `${infer Param}&${infer Rest}`
        ? MergeParams<ParseParam<Param>, ParseQueryString<Rest>>
        : ParseParam<Str>;

function parseQueryString<Str extends string>(queryStr: Str): ParseQueryString<Str> ;
function parseQueryString(queryStr: string) {
    if (!queryStr || !queryStr.length) {
        return {};
    }
    const queryObj:Record<string, any> = {};
    const items = queryStr.split('&');
    items.forEach(item => {
        const [key, value] = item.split('=');
        if (queryObj[key]) {
            if(Array.isArray(queryObj[key])) {
                queryObj[key].push(value);
            } else {
                queryObj[key] = [queryObj[key], value]
            }
        } else {
            queryObj[key] = value;
        }
    });
    return queryObj;
}


const res = parseQueryString('a=1&b=2&c=3');
```

这里的实现和之前那个还是有一些区别的，主要是这里：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e40d72023ef34185b24b007f809a81c8~tplv-k3u1fbpfcp-watermark.image?)

当提取 a=1 中的 key 和 value，构造成索引类型的时候，如果提取不出来，之前返回的是空对象，现在改成了 Record<string, any>。

因为 ParseQueryString 是针对字符串字面量类型做运算的，如果传入的不是字面量类型，而是 string，那就会走到这里，如果返回空对象，那取它的任何属性都会报错。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5ab82593f2942a99bae3e15f6553c49~tplv-k3u1fbpfcp-watermark.image?)

所以要把不满足条件时返回的类型改为 Record<string, any>：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41750c0b8a2047c09e24318ee33fa263~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBACghgJwM4XguBbAPGzUIAewEAdgCZJRLAICWJA5gHxQC8UAUFN7InocXKUABgBIA3vQBmEBFADSEEAF9WE6bKgA1OABsArhGXCuPMwH4o402dtQA2vKj0FSgLoAubXsOc73ZSgvACUIAGMAewQyLGo6RgAaKDgSECYAbg4OUEgoAFlZBggdAwgkLAB5EggkiuAAC1kWdhsoKugBUgo2hs1Wizbq-p4vOsa5TqEofRIAaxIIgHcSezdhu0t7dqSAOj2x2TX-Wy8t6trehDdM7PBoAoQi3Axy1vbn-CIuylDI6NiaPQGEkUmkEm9Lh9Jt1flEYnEgSDUkwOM0rKYEBA4GQIiRdCAHIoCS5ZkoIlJBqg+BgoAAfKCkkDknrjZ6ePw8ImfQTdRnM97U9ZQSxc6GUPkUg4IZ5CgYPIolQzlAXoDCOdwXVnU9UgNwo45mUbVZ46o7+Lyir5TCUs2QfWU8SxSk1Etwcg1BKDVABusg4yiyOWgaBQAEVDAgQABlQGMLAxiZW7oIxho1oJ7nfKBiSQkGRyZ7KABk6jzmlC1GMQss8qpqvKIbrmBw1KYSUb4dk0djDCwFeATH15t4yCb2ATGSyUhmYWAtFxUDAiDDEe78V7GbFVB7TAAFABHVcJrwJgCUXg7R578ZoLEy05Is-nJEXy4gncjCaBB6vCC8KYYU90TMWgKV3ABCQ8uwzWl6Ug38dl0UgGAaIDrGOTFgH0BAX3EZRMjMAMzEiEhqCgKDIwqAAjAArDxYX+ACkTSNgrHw1oSLI2hiBeViKLXHYkDAXRuN3AByIsxNPAieG4iAXh2KQogAUTgMJ6l3OSaVYFh0P8TjgAcRkkm9HwIDddgtME4TRLE1gpJkuxQKgH8u2omj7EZNw0IdbhQN3ABBBB0BAHZaCQIKQtcyjaM89xTx8j07H49y4t1HYwH0JANNM0ppN8qBAggXQUGApKzBS2KvNY+xKo8ryTLMs0PSI-wipK6A9I9Oq0osqBcsMRzbFagJ8rMTDsJfOrMgDLIDKgTFKHYJdRw-NdvzEuBWAARiLKjWAAJiLMJWAAZgcjggA)

对比下用类型编程和不用类型编程的体验：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/615ead936ac042b3a726b44d932a3b1a~tplv-k3u1fbpfcp-watermark.image?)

vs

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fb4a704a90e4997b741935f0034b1a4~tplv-k3u1fbpfcp-watermark.image?)

这就是类型体操的意义之一：实现更精准的类型提示和检查。

## Promise.all

前面提到过，需要动态生成类型的场景，必然会用到类型编程，我们来看个例子。

Promise 的 all 和 race 方法的类型声明是这样的：

```typescript
interface PromiseConstructor {
    all<T extends readonly unknown[] | []>
        (values: T): Promise<{
            -readonly [P in keyof T]: Awaited<T[P]>
        }>;

    race<T extends readonly unknown[] | []>
        (values: T): Promise<Awaited<T[number]>>;
}
```

因为 Promise.all 是等所有 promise 执行完一起返回，Promise.race 是有一个执行完就返回。返回的类型都需要用到参数 Promise 的 value 类型：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd0d4ff2cf14b61846d9181f4b05774~tplv-k3u1fbpfcp-watermark.image?)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8ba496ddd08425ea6718a9187c2213a~tplv-k3u1fbpfcp-watermark.image?)

所以自然要用类型编程来提取出 Promise 的 value 的类型，构造成新的 Promise 类型。

具体来看下这两个类型定义：

```typescript
interface PromiseConstructor {
    all<T extends readonly unknown[] | []>
        (values: T): Promise<{
            -readonly [P in keyof T]: Awaited<T[P]>
        }>;
}
```
类型参数 T 是待处理的 Promise 数组，约束为 unknown[] 或者空数组 []。

这个类型参数 T 就是传入的函数参数的类型。

返回一个新的数组类型，也可以用映射类型的语法构造个新的索引类型（class、对象、数组等聚合多个元素的类型都是索引类型）。

新的索引类型的索引来自之前的数组 T，也就是 P in keyof T，值的类型是之前的值的类型，但要做下 Promise 的 value 类型提取，用内置的高级类型 Awaited，也就是 Awaited<T[P]>。

同时要把 readonly 的修饰去掉，也就是 -readonly。

这就是 Promise.all 的类型定义。因为返回值的类型和参数的类型是有关联的，所以必然会用到类型编程。

Promise.race 的类型定义也是这样：

```typescript
interface PromiseConstructor {
    race<T extends readonly unknown[] | []>
        (values: T): Promise<Awaited<T[number]>>;
}
```

类型参数 T 是待处理的参数的类型，约束为 unknown[] 或者空数组 []。

返回值的类型可能是传入的任何一个 Promise 的 value 类型，那就先取出所有的 Promise 的 value 类型，也就是 T[number]。

因为数组类型也是索引类型，所以可以用索引类型的各种语法。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35f7b9a071c04f7a98b9577fcab14e22~tplv-k3u1fbpfcp-watermark.image?)

用 Awaited 取出这个联合类型中的每一个类型的 value 类型，也就是 Awaited<T[number]>，这就是 race 方法的返回值的类型。

同样，因为返回值的类型是由参数的类型做一些类型运算得到的，也离不开类型编程。

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/JYOwLgpgTgZghgYwgAgApQPYFtgGcIDCGIuYUArgmBlMgN4BQyzycANmwDwAqyEAHpBAATXMigQ4w4mwCeyciADWIDAHcQAbQC6yAD7IdAPiYszACgBu7chFwAuZNwCUj9NjwROjM75YBaCSkZeU1UZFBkJQhZDBgnbUcAQTU4YEhhHjDtEz9mAF8jAG4GU2YoRC9eASFRcUlpEDkFZVUNHX1DHLLfKxs7Rxc3TBx8ThS0jKyQciwAI2gc4oZ80uEIBDY4CWQEYlJkAAcRz2GPfCISMkpqKBKGPavWDgAlO2QAXiOT-AA6djY5jCPwgvwkuAwbEsEHMAEZnAAaNAgsF2SHQ8wAJkRyPOoPB6JhAGZnNpnPdHgcKkg3mIvsc8WDKkD3KN8WioTD4UjWZ5URDOVicby-gTBSSyfcwLJDihwZ9DCKvLCjAilZxMar1USjNpNDN5osSkA)

这里 T 的类型约束为什么是 unknown[] | [] 也要专门讲一下：

ts 里有个 as const 的语法，加上之后，ts 就会推导出常量字面量类型，否则推导出对应的基础类型：

没有 as const 时：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b60f831767334e1c9b2a04c5a6301da8~tplv-k3u1fbpfcp-watermark.image?)

加上 as const 后：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/70af74c445f04665bd46feb7badab34a~tplv-k3u1fbpfcp-watermark.image?)

没有 as const 时：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbac630c4fcd462ab8898fd5fbe4644d~tplv-k3u1fbpfcp-watermark.image?)

加上 as const 后：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b6e5e6394df43289bd18e907c851916~tplv-k3u1fbpfcp-watermark.image?)

这里类型参数 T 是通过 js 函数的参数传入的，然后取 typeof，也会遇到 as const 的这个问题，约束为 unknown[] | [] 就是 as const 的意思。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4fe63d0ed2f3403184fab83b87113a33~tplv-k3u1fbpfcp-watermark.image?)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4ed74d259194b7cbcbc81985f80b940~tplv-k3u1fbpfcp-watermark.image?)

这个地方确实比较特殊，要记一下。

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/CYUwxgNghgTiAEAzArgOzAFwJYHtXw0IB4AVeEADwxFWAGd44pg8IBPeNAa1RwHdUAbQC6APgAUANygRkIOgC54JAJRKSAbgBQWsHjoZG8+AF4ChcYICMAGngAmOwGZhK7TtCRYCFOmx5zDHtScioaeiNmVg5uXgEReAAfeBEJaVl5dTVldz1UAyM6e1NA+0tbB2dXXP1DHAAjACsSgG8teA74KCUrLQBfHQw2AAcEBsaSEYQzIdGcRHhxmvy6puKzNs6unv6uhjyDd1mxpsnR9YIp+cW15YLYGBLrG0cXQamumBgz6cu5hYed0MDwuz1ewj28AOGCOHwePwux2uII0QA)

## currying

做了一个参数类型和返回值类型有关系的案例，再来看一个更复杂点的：

有这样一个 curring 函数，接受一个函数，返回柯里化后的函数。

也就是当传入的函数为：

```javascript
const func = (a: string, b: number, c: boolean) => {};
```

返回的函数应该为：

```javascript
(a: string) => (b: number) => (c: boolean) => void
```

JS 怎么实现不用关注，我们只关注这个 curring 函数的类型怎么定义：

```typescript
declare function currying(fn: xxx): xxx;
```

明显，这里返回值类型和参数类型是有关系的，所以要用类型编程。

传入的是函数类型，可以用模式匹配提取参数和返回值的类型来，构造成新的函数类型返回。

每有一个参数就返回一层函数，具体层数是不确定的，所以要用递归。

那么，这个类型的定义就是这样的：

```typescript
type CurriedFunc<Params, Return> = 
    Params extends [infer Arg, ...infer Rest]
        ? (arg: Arg) => CurriedFunc<Rest, Return>
        : never;

declare function currying<Func>(fn: Func): 
    Func extends (...args: infer Params) => infer Result ? CurriedFunc<Params, Result> : never;
```
curring 函数有一个类型参数 Func，由函数参数的类型指定。

返回值的类型要对 Func 做一些类型运算，通过模式匹配提取参数和返回值的类型，传入 CurriedFunc 来构造新的函数类型。

构造的函数的层数不确定，所以要用递归，每次提取一个参数到 infer 声明的局部变量 Arg，其余参数到 infer 声明的局部变量 Rest。

用 Arg 作为构造的新的函数函数的参数，返回值的类型继续递归构造。

这样就递归提取出了 Params 中的所有的元素，递归构造出了柯里化后的函数类型。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c8449e6edc84beeb09206104e7b0d26~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBAwgrgJwQSwgEwGJwHYGMA8ACgIYLEC2AzgDRQBKEwi2AfFALxQBQUvUJZKlAgAPYBGxpKUANrJsAMwgIoAQQQBzWgDpd8pSoaVgAXR58LAfigAKUhoBcazQEoObeElSYcBI8FoGJgRWcwteJ2wIADdlAG4uLjQIXAAbUmgFX2BkAHtsKFxEBBB5DXwsPBYbBWwnStwXJzCoBuExCSlbXW17Sid9ZX5SCko3djZBwwhKOFTgKGtPFHQGohGqQJm54DZImPjE3HzjKCy8DltiJ2MUbC0oACNIuHJH5VpcJ0fc3NSIYjYcZsADeAF8ElxjthTkUvKtfJc4SUyjVfC44kA)

这个柯里化的函数类型定义，因为返回值的类型和参数的类型是有关系的，所以离不开类型编程。

## 总结

类型编程是对类型参数做一系列类型运算，产生新的类型。**需要对已有类型做修改，需要动态生成类型的场景，必然会用到类型编程**，比如 Promise.all、Promise.race、柯里化等场景。

有的时候不用类型编程也行，但用了类型编程**能够实现更精准的类型提示和检查**，比如 parseQueryString 这个函数的返回值。

这就是类型编程或者说类型体操的意义。

[本文的案例合并](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/PTAEAUEMCcGcFMCKBXe0CeBlALtAlgHYDmAUCdugA7wQwJTSQC2APA86PAB7bwEAmsULFyEiAPlABeUCVDzajJpx59BoAAYASAN6EAZmlABpeOgC+U3QaMA1SABtU5jXIXuA-KB1v3f0ADaxqCEJmYAugBcoPZONL5+5qDRAErwAMYA9tD8LCL4xAA0oJAE6OIA3GQU1KAAsmhE8LGosCwA8gTwxe3YABZokjIJnTTcvAJCvQPQsv7yXqMJ7tHTRuNqQsgEANYEmQDuBAHhy-NeAaPFAHS3a9Cn837Rl109-WjhVeRUNA3QTXYTDaIy6QJUE3UaSyOTyoiKJTK4kKIw+0HBG0moGh2Vy+TExVK5RIQ28bmg8Eg-EyBAc6ECpnpoR2Zky+lAo3BAB9QCz0GyOWigVE5gpGRDNrzWezOTBmGcFmF6Zj1HyBfcgQq-F5-k0WvA2rKlEEIu8ZkCTehwuItSsOWC5UxLY95tFxSqhGqZULHaKnoqNY7nX7-dEugA3NAkczVX6KBAoNBYeFEFg4WYe4Qp0kJdMSrHaPQEQyzIHmABk1mLRjSIhcWp1jXgQLaDHojrYjuR8aQqAw6bELFr2HENqe0TbzY76cqZH023S2DwNNAlDovaTA+Iadw+fU+OI4gAFABHPvJ6DRdMASgn68T-ZTO+gkiq84Ii+XBFX9-PW6Ip5-rg0QHkQ15ku4eDskeACEZ6bruXI8nBQHQNcDh8EQ-TgT4TwUtgyDQN+OjmFU7gxu4WQECIoDwRg7QAEYAFaRDisKgYSSLSN4pEJFRNF4LwwLcXRF7XLAlAOIJR4AOTljJ15kQognwMC1z6NkACikDpH0R4qcoUiSLh8z8dggR8sU4aOKg4TcQZ4mSdJMlSApSn+FBoCAUmjFMQEfLhDhtrKfoR4AILQIw6DXHgsARVF3n0cx-kRNeQX+vMom+SlVrXJQyCwHp1lxIpwXyEk8AOAgEEZX4WXJQF3EBPVfkBVZNnwC6GUUfMFVVTQJkZS1OV2TIxWoO5iQJOYpXuPhhHfi1VQxmQZmgLwIgAEzcWucAbo+BQATJkBSAAjOWDFSJt5bpFIADMblkE9IAQNAmRMLF8AAMI0vkyCLtkZCELw0D6DpNDgG9H0ID91G4P92DZDV8iOA4LAACp7kIFJUjSdKgNseyHMcdk8icY7zEe40GtE6O3q972fSwg3+gAtDj1K0vSATgCE35eqA6MimFByQCpuTozz1pauYs4JIw6TwBjWOgBzeP0oT+xHCcoBk9LTxUx1sC0-TkOMwgLAi2LvASwEBDIEwDGfKOy1kPwGQODANBrZQUOfROfsw798MA9A3xrajtY7YH8DXKjR48zH1wUrAmQOJGR6ndexRm9Dscp2nGebdnDN58nBqF-AR53degXh8Hqvg1HMi++b+fgwnuefeXqfp1XWc50nBd90exeD23PeV9XtelT8tQbeZMiJ23LCnciXcW5t68xywd3iOEdsO07DzfCQ7vpJ7FKgO+n4rtg9-K5matcwTuxayTx7U8bgv0+j9dw6rA03F77YATqdYom1ih3Trm7D2Xtr4LiXHfe+m1H6qCxM-fGmtiY6z1p-I2Jtab-xoinbaMgQGbTARAqBMCSBrUyMxbiLNIDRFOtGWMtQGFMXRnGchvwBRcOIeZLhZDkYlFYdGEoQgzJPRqDQLhPDqCiLkQI5im0hElEik1cBkDoEcJoDAaAiiaB8OoAKQxGjDGiICDowo0CpGgDMt8ORmijG-GUfw9kVjvgvS+oRDAYh9GgD8ZFPA8B+AADEFydiULAYoaQCJERzO4FsKsAg2FmBFIgNxbgZOxAabAXVtReRgEQaIWTwJGWCf4sJkTonDnifARJBAKb+DDPASMYdYEX3gTfJB350j+PQIOKJH5jz6AINEUZ6R6YJGmSrI8tw44Am-nklslTJB5NrMgBw5kvAhPwOE6ZMTmBxPybAHZI5kigAjGgDRN9uJHhYVmQ6xQGJhiPmgYo6RogMUyGnSkBANk8Q0YM0JRyFzcTBQE4gR4b6KSAA)

## 14.类型编程综合实战一

我们学会了 6 个类型体操的套路，各种高级类型都能写出来，也知道了类型体操的意义（类型之间有关联的时候必须要类型编程，用类型编程能做到更精准的类型提示和检查），但是做的练习还是不够多。

前面的案例更多是用于讲某个套路的，这节开始我们做一些比较综合的案例。

## KebabCaseToCamelCase

常用的变量命名规范有两种，一种是 KebabCase，也就是 aaa-bbb-ccc 这种中划线分割的风格，另一种是 CamelCase， 也就是 aaaBbbCcc 这种除第一个单词外首字母大写的风格。

如果想实现 KebabCase 到 CamelCase 的转换，该怎么做呢？

比如从 guang-and-dong 转换成 guangAndDong。

这种明显是要做字符串字面量类型的提取和构造，并且因为单词数量不确定，要递归地处理。

所以是这样写：

```typescript
type KebabCaseToCamelCase<Str extends string> = 
    Str extends `${infer Item}-${infer Rest}` 
        ? `${Item}${KebabCaseToCamelCase<Capitalize<Rest>>}`
        : Str;
```

类型参数 Str 是待处理的字符串类型，约束为 string。

通过模式匹配提取 Str 中 - 分隔的两部分，前面的部分放到 infer 声明的局部变量 Item 里，后面的放到 infer 声明的局部变量 Rest 里。

提取的第一个单词不大写，后面的字符串首字母大写，然后递归的这样处理，然后也就是 \`\${Item}${KebabCaseToCamelCase<Capitalize<Rest>>`。

如果模式匹配不满足，就返回 Str。

这样就完成了 KebabCase 到 CamelCase 的转换：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa9b283ab5ad407a99627de2ae131a5d~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBA0hBGBDeBhRBnCAVA9mgthADZqYA8AysAE5QQAewEAdgCbpTo0CWzA5gD4oAXigAoKJKhVaDJmw4ADACQBvXgDMItAJJN8AXwC0azdqgAlCFwOLxUh1AD8UFar0RDauElQZseIiEJP5kaGDcwIhE3ABeEGRWXAICthKOkgBc0jQA3GJioJCwCMikAQTE5UkiJb7luJUh5ADkfACuiPxGXaxGrDj8LQL5YkA)

那反过来怎么转换呢？我们再实现下 CamelCase 到 KebabCase 的转换：

## CamelCaseToKebabCase

同样是对字符串字面量类型的提取和构造，也需要递归处理，但是 CamelCase 没有 - 这种分割符，那怎么分割呢？

可以判断字母的大小写，用大写字母分割。

也就是这样：

```typescript
type CamelCaseToKebabCase<Str extends string> = 
    Str extends `${infer First}${infer Rest}`
        ? First extends Lowercase<First> 
            ? `${First}${CamelCaseToKebabCase<Rest>}`
            : `-${Lowercase<First>}${CamelCaseToKebabCase<Rest>}`
        : Str;
```
类型参数 Str 为待处理的字符串类型。

通过模式匹配提取首个字符到 infer 声明的局部变量 First，剩下的放到 Rest。

判断下当前字符是否是小写，如果是的话就不需要转换，递归处理后续字符，也就是 \`\${First}${CamelCaseToKebabCase<Rest>}`。

如果是大写，那就找到了要分割的地方，转为 - 分割的形式，然后把 First 小写，后面的字符串递归的处理，也就是 \`-\${Lowercase<First>}${CamelCaseToKebabCase<Rest>}`。

如果模式匹配不满足，就返回 Str。

这样就完成了 CamelCase 到 KebabCase 的转换：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/40eb2b22902344f09b0b9b98bc3e1bbc~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBAwghgWwgG3gZwgFQPYGkIBGcB6EAPAMrABOUEAHsBAHYAmaUaNAlswOYA+KAF4oAKCiSoVWgyZsOAAwAkAb14AzCLQBi3alwC+azdqgAlCEcUSpdgPxQ9B4HUYt2UADLYA7toBjOAwyZy4hWzsoqEcVVTDgY1V4JFRgrDxCYlIyS3DDG2jogC4oRQBaNR9-aiCQhIEklJRSHHwiEnTcq2BGwqLSmQBuMTFQSFhEFvS2rM6MPJFJ1NbMjpyAcj4AVzh+AEE2ABFsfg2BEaA)

做了两个字符串类型的练习，再来做个数组类型的：

## Chunk

希望实现这样一个类型：

对数组做分组，比如 1、2、3、4、5 的数组，每两个为 1 组，那就可以分为 1、2 和 3、4 以及 5 这三个 Chunk。

这明显是对数组类型的提取和构造，元素数量不确定，需要递归的处理，并且还需要通过构造出的数组的 length 来作为 chunk 拆分的标志。

所以这个类型逻辑这么写：

```typescript
type Chunk<
    Arr extends unknown[], 
    ItemLen extends number, 
    CurItem extends unknown[] = [], 
    Res extends unknown[] = []
> = Arr extends [infer First, ...infer Rest] ? 
          CurItem['length'] extends ItemLen ? 
            Chunk<Rest, ItemLen, [First], [...Res, CurItem]> :
            Chunk<Rest, ItemLen, [...CurItem, First], Res> 
    : [...Res, CurItem]
```

类型参数 Arr 为待处理的数组类型，约束为 unknown。类型参数 ItemLen 是每个分组的长度。

后两个类型参数是用于保存中间结果的：类型参数 CurItem 是当前的分组，默认值 []，类型参数 Res 是结果数组，默认值 []。

通过模式匹配提取 Arr 中的首个元素到 infer 声明的局部变量 First 里，剩下的放到 Rest 里。

通过 CurItem 的 length 判断是否到了每个分组要求的长度 ItemLen：

如果到了，就把 CurItem 加到当前结果 Res 里，也就是 [...Res, CurItem]，然后开启一个新分组，也就是 [First]。

如果没到，那就继续构造当前分组，也就是 [...CurItem, First]，当前结果不变，也就是 Res。

这样递归的处理，直到不满足模式匹配，那就把当前 CurItem 也放到结果里返回，也就是 [...Res, CurItem]。

这样就完成了根据长度对数组分组的功能：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3948d21be8a4fb68bc3776deacee22f~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBAwgFgVwHYGsA8AoK2oEEBO+UEAHsBEgCYDOUyKSA9gO5IDaAugDRRY4CS5ALYAZCsTIUaUJAiEAjCPh59sMBPkEQhE8lVr0mrTlAC8UTipxQAShFqk90wy3YczFjhgB8HgkUcpWjYASyQAMyUoADEQ-GpgHgA6FLDIojsE9wB+Xmt82A0tITYAcgAbCgBzYDhS90D9KGKxJChc1QKceHo0TMTm4VaeNlj44G4LFKTMnnVNYQ5fAC5OrthEVD77AZaKEen54p4xrJ5M307lqZTZwoXtLwxQSA36TI8erbYARi4AJi4AGYuAAWLgAVkm-28AG4MEA)

字符串类型、数组类型都做了一些练习，接下来再做个索引类型的：

## TupleToNestedObject

我们希望实现这样一个功能：

根据数组类型，比如 [‘a’, ‘b’, ‘c’] 的元组类型，再加上值的类型 'xxx'，构造出这样的索引类型：

```javascript
{
    a: {
        b: {
            c: 'xxx'
        }
    }
}
```

这个依然是提取、构造、递归，只不过是对数组类型做提取，构造索引类型，然后递归的这样一层层处理。

也就是这样的：

```typescript
type TupleToNestedObject<Tuple extends unknown[], Value> = 
    Tuple extends [infer First, ...infer Rest]
      ? {
          [Key in First as Key extends keyof any ? Key : never]: 
              Rest extends unknown[]
                  ? TupleToNestedObject<Rest, Value>
                  : Value
      }
      : Value;
```
类型参数 Tuple 为待处理的元组类型，元素类型任意，约束为 unknown[]。类型参数 Value 为值的类型。

通过模式匹配提取首个元素到 infer 声明的局部变量 First，剩下的放到 infer 声明的局部变量 Rest。

用提取出来的 First 作为 Key 构造新的索引类型，也就是 Key in First，值的类型为 Value，如果 Rest 还有元素的话就递归的构造下一层。

为什么后面还有个 as Key extends keyof any ? Key : never 的重映射呢？

因为比如 null、undefined 等类型是不能作为索引类型的 key 的，就需要做下过滤，如果是这些类型，就返回 never，否则返回当前 Key。

这里的 keyof any 在内置的高级类型那节也有讲到，就是取当前支持索引支持哪些类型的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88532b7b2d834b4591306f32cda0b45a~tplv-k3u1fbpfcp-watermark.image?)

如果提取不出元素，那就构造结束了，返回 Value。

这样就实现了根据元组构造索引类型的功能：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24c8dbf5011d4d27952c32ecfb9b337d~tplv-k3u1fbpfcp-watermark.image?)

当传入 number 时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ca07272383c4728a19b48f064381382~tplv-k3u1fbpfcp-watermark.image?)

当传入 undefined 时：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20afc50bcef84df1853a60e9f5e10a34~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/FAFwngDgpgBAKgVwgGynA9gOSgZxFAEwHkAjAKygGMQAeRFWKAD3wDsCcYFWBrV9AO6sA2gF0ANDABqAQ2QIoAPhgBeGMBib4SVDGZsOMYQEtWAMygAnGADFjlvJIB0L0xesAlXCFEatmgH4YAG8-f39hAGkoMBhTW3s8GBlOaNj9KHZOHhj0M2TWWKC0mAAuGFYoADcrUXKw8MavJIysrl5+ITEGxt6YIPpUDGw8QlIKahpmkElZeSUevvDyuYVFgF9FlbkFAG5gA-BobQZh7zHyKhBm1ROhrHPiS8nhAHIAcwQZVnfXyVfvgQ-q8COgfq8JDAAIyKfagSCwQZoB6jJ4Ta64ABMtyRZ1R4yuNDen2+v3+gL+FQQAFsSFZxCCwb9ITC4UdETpkSN8Girs0AMw4zl4nkEl4fL7g8nsSncAhQMymQgM0Hglmww4I5LIZCCQhpOBatQ5MB5ApgfZAA)

我们再来练习下内置的高级类型，我们对这块的练习比较少：

## PartialObjectPropByKeys

我们想实现这样一个功能：

把一个索引类型的某些 Key 转为 可选的，其余的 Key 不变，

比如 
```typescript
interface Dong {
    name: string
    age: number
    address: string
}
```
把 name 和 age 变为可选之后就是这样的：

```
interface Dong2 {
    name?: string
    age?: number
    address: string 
}
```
这样的类型逻辑很容易想到是用映射类型的语法构造一个新的类型。

但是我们这里要求只用内置的高级类型来实现。

那要怎么做呢？

内置的高级类型里有很多处理映射类型的，比如 Pick 可以根据某些 Key 构造一个新的索引类型，Omit 可以删除某些 Key 构造一个新的索引类型，Partial 可以把索引类型的所有 Key 转为可选。

综合运用这些内置的高级类型就能实现我们的需求：

我们先把 name 和 age 这俩 Key 摘出来构造一个新的索引类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bda4effa66cc46338c0bed9ced7c492e~tplv-k3u1fbpfcp-watermark.image?)

然后把剩下的 Key 摘出来构造一个新的索引类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a5d569cce1a4d428dd9e751b19c37c2~tplv-k3u1fbpfcp-watermark.image?)

把第一个索引类型转为 Partial，第二个索引类型不变，然后取交叉类型。

交叉类型会把同类型做合并，不同类型舍弃，所以结果就是我们需要的索引类型。

```typescript
type PartialObjectPropByKeys<
    Obj extends Record<string, any>,
    Key extends keyof any
> = Partial<Pick<Obj,Extract<keyof Obj, Key>>> & Omit<Obj,Key>;
```

类型参数 Obj 为待处理的索引类型，约束为 Record<string, any>。

类型参数 Key 为要转为可选的索引，那么类型自然是 string、number、symbol 中的类型，通过 keyof any 来约束更好一些。默认值是 Obj 的索引。

>keyof any 是动态返回索引支持的类型，如果开启了 keyOfStringsOnly 的编译选项，那么返回的就是 string，否则就是 string | number | symbol 的联合类型，这样动态取的方式比写死更好。

Extract 是用于从 Obj 的所有索引 keyof Obj 里取出 Key 对应的索引的，这样能过滤掉一些 Obj 没有的索引。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3696f8a23c8e44b18b27e05aa0e23cc3~tplv-k3u1fbpfcp-watermark.image?)

从 Obj 中 Pick 出 Key 对应的索引构造成新的索引类型并转为 Partial 的，也就是 Partial<Pick<Obj,Extract<keyof Obj, Key>>>，其余的 Key 构造一个新的索引类型，也就是 Omit<Obj,Key>。然后两者取交叉就是我们需要的索引类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7dff679e1cfe47198f8e2d100fe9167d~tplv-k3u1fbpfcp-watermark.image?)

为啥这里没计算出最终的类型呢？

因为 ts 的类型只有在用到的的时候才会去计算，这里并不会去做计算。我们可以再做一层映射，当构造新的索引类型的时候，就会做计算了：

```typescript
type Copy<Obj extends Record<string, any>> = {
    [Key in keyof Obj]:Obj[Key]
}

type PartialObjectPropByKeys<
    Obj extends Record<string, any>,
    Key extends keyof any = keyof Obj
> = Copy<Partial<Pick<Obj,Extract<keyof Obj, Key>>> & Omit<Obj,Key>>;
```
这里的 Copy 就是通过映射类型的语法构造新的索引类型，key 和 value 都不变。

这样就会计算出最终的索引类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c0b497d248544d6b5b114d4847e0031~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/FASwdgLgpgTgZgQwMZQAQBED2YDmqDewqxqYCAtlAFyoDOEM4ORJCO1pAruQEawvEEAEyEwotWjXqNcwAL4tgEAJ4AHNAGFMq5QB4A8jwBWqKAA9oYIbVQAlKEkwwhu6UwA0qBGGUA+X6gAvAQCqADaANJQyqjgqADW0ZhwqIZGALpUaZHR6fLASmpoAAoIMBAgCAA2aQ4QxTDaAELKUcq0uqFpphZQVjb2js6uDB5ePr7uoW09ltYJSSneMcGJysmpxsABwVo6uqXllVUHIEjxBsbuAKIWMMgQumsbaZ5t-gEAZKnkII+v718AG4Cip1KhDhVqrUkPVGqoWm1aPYbMFIccYXDmq1oh0sLhPAByMiUQmoAA+qEJbCghOBoKKPz+KKCTMe+JwRJJtIpVJpdJBhXBxTO8RZaNFug5XIoPMp1PYAoKQrQtwYD3FqDV91hT0WGGwnKp3LJ8v5vOpCAQAqAA)

当然，这里的 Copy 也可以不加，并不影响功能。

## 总结

我们学完了类型编程的套路，也知道了类型编程的意义（类型有关联的时候必须用类型编程，类型编程可以实现更精准的类型提示和检查），但是做的综合一些的案例还是少，这节就各种类型的类型编程都做了一遍。

包括字符串类型、数组类型、索引类型的构造、提取，都涉及到了递归，也对内置的高级类型做了练习。

这一节的类型练下来，相信你会对类型编程会更加得心应手了。

[本文案例的合并](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/PTAEGkFMCMENoMKwM6QCoHskFtIBslUAoAFwE8AHSCGeQ9LWXAlSAHgGUSAnUSADxKQAdgBNkoZDwCWwgOYA+UAF5QRUBtBdeAoWIkADACQBvWQDNIvAJJDsAXwC0pi1dAAlSFPsG1m-6AA-KDGJraQDqZQcIismDj49GxIFNIksHjSAF7snlIKCj7qARoAXFo8ANxEpJTU0XRxjMz0eSo0MfTxTImsbADkcgCusPKOo6KOohjy-QrVRCCgCSyomA2xxORUyz2rDBtJ2nyCIuKSMvJKqsUax7pnhi7ClrwAYtLc3s+vHl4kRRKGmCHy+JBOenOABkMAB3KwAYz6oPyfiB-mCoRRANMKy6GEOfTyJEKBlu6NA5QMzhMMPh3CRqDY2MKuL2+MJTOJpPJ-nK2gW22oeKanMgbVUIrWBNom3YgxG8gAgmIACIzORzBZLBAACyGwgA1rUdnqDYa2OSldwdKd9KBzcI4cIANoAXQANGiNOFsFCRBDHqBhENsNArF7yQghtxfYH7Y7ne72u7I-42g8E0anbDXW6U26iNdQNbbZCJC7XO9PlIvQA6BtVv5SfPBXkBaOxuwu-p4ERyEi6-r5zPnX3+4RBb0Us1GtjEr3jkRel3Yz2gF0Nut5L2d31upSldslWcWhegJfCFdbvd2L1rr15JTk8qbhs75Yx-c1IXLfVGiU-3NNgXQARg9AAmD0AGYPQAFg9ABWdcIPmGoQDQIYKD7TAADl-kgUQAHloAAK0gBESBNahMOwhh8KkQiSPIyi2Fovt43ORNc1TUAADUMiGSBi3JdjqFHCsm2xetGxeNxiULEpghMY9NBdKAyFAWRQGxUAUBoTSJNAQ1IDIDBzD04RNOCDTKWDSAADcrDdcpVJKYlOIkbi8zcilgjEvCCOIsiKJIed-i9AS8CEhRfPRcooqE9t7HbBLBMgBZqNAAKMAYoRgpYkhAJyvKmJC1ie2GUZNS9foJn6D1+mmWZ11AtCspKoLmNCvIIPaTrGIK0KQIVaqGtAOqxHGkMwwjJqNWHL02sFOpsqwnDcq68qiq8aD+vW+itsKkaqtmWr6q9A1REgcxZEIxrms1Vr2t-DI8DhQiNLQVbVBMsyLNGMhtTAAAFWBuBIaQMm6yiQe4DAKAAITIDTkDyIhZCEbhzFgBFqHVeRQBU-xhB6copG4WQ5HJWA5EgcoZvDbgadEURuC8ZBycuamUo0LKEARsg2GYzy-gRDBuFENgKapr1AYKdpibU2ztL+8zQGYlzmPU0zCxSrKwYhqG8Bhkg4YR5HUctfwRaMzxxcl6XublqyFA9clbKMtWAas9pvY1sii3aAWKCFw3IYyNgQekBELWYj0AFFBG4XGwv9+ODIKJQADINewNJhbIj0NIKFadnD43TfNpGUdMtGvHaCvoe26vLbrtgCbkWrSdwfpQAAHwm2nIC1H9VqI-OdokVQJ4Lzvu56PvB7qunR4NmPDUA6PY47jUF97geh9X9qsqTnhU8As+U9Y-354mnuR8PlfH+X2A361IA)

## 15.类型编程综合实战二

想提升类型编程水平，还是要多做一些有难度的案例，这节我们提高下难度，加大训练强度。

## 函数重载的三种写法

ts 支持函数重载，也就是同名的函数可以有多种类型定义。

重载的写法一共有三种：

```typescript
declare function func(name: string): string;
declare function func(name: number): number;
```
这种大家比较常用，声明两个同名函数，就能达到重载的目的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/baa435154188455fb18f045fcc7fb5bd~tplv-k3u1fbpfcp-watermark.image?)

当然，如果有函数的实现，那就不用带 declare 了：

```typescript
function add(a: number, b: number): number;
function add(a: string, b: string): string;
function add(a: any, b: any) {
    return a + b;
}
```
当传入 number 参数时：
![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cca4da44f3d84685ad33cdba9fe9110f~tplv-k3u1fbpfcp-watermark.image?)

传入 string 参数时：
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ff5def299d9462cbd94824d769309ff~tplv-k3u1fbpfcp-watermark.image?)

函数可以用 interface 的方式声明，同样，也可以用 interface 的方式声明函数重载：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fc6af466fda4757894caa1ae9a85716~tplv-k3u1fbpfcp-watermark.image?)

函数类型可以取交叉类型，也就是多种类型都可以，其实也是函数重载的意思：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db167ed7cbee4bc8a9facc31bae34d08~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/PTAEl-FQHU0WcTF94goAJgUwMYBsCGAnZoBmArgHaoAuAlgPbEEmoAUxmAtsgFygDOZ2FxAcwCUnHn0EBuJGiy46pSjXmNmbTsUIsARsmwjQG7bqnwipBgHJMFoVLOMAjLfgv+ZXfkyo8AMXqgAb3hQENAmVg5uXn5hUWjJYNDwtQNNHT11NONQeABfFxQMHDxUGh5lACZOP1ITewrLa2d6hicTeDIATwAHX3oK0ABeBmTIsRihIYA+KPFhUAAyMNHMoz1p1LXnaSK5UuJy+wBmav66+iPGmzsL1u37RVpMREQGTFX0gBpQLQ-dfUM6RuCmoTxebzic2+v1mE0hMWB5FBoGer3eKOInWhnEwmMmQVCoFwZEI2CeoAA1D8pPl4PtyrguEMUeCHN8Ktt6WQicguANBizXlYLN8LFprvAgA)

声明多个同名函数类型、interface 声明多个函数签名、交叉类型，一共这三种函数重载的方式。

这里讲函数重载是为了下面这个复杂类型做铺垫的：

## UnionToTuple

要求把联合类型转成元组类型，大家有思路没？

也就是 'a' | 'b' | 'c' 转成  ['a', 'b', 'c']。

没思路很正常，因为这里用到了一些特殊的特性。我们先来过一下用到的特性：

我们知道 ReturnType 是 ts 内置的一个高级类型，它可以取到函数返回值的类型。但如果这个函数有多个重载呢？

第一种重载方式：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3155d72396b4d958fd4453e0c6cfef1~tplv-k3u1fbpfcp-watermark.image?)

第二种重载方式：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/670e5640be654068bc841c7351389a12~tplv-k3u1fbpfcp-watermark.image?)

第三种重载方式：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f38331948a74232a82da6339ee7b653~tplv-k3u1fbpfcp-watermark.image?)

**取重载函数的 ReturnType 返回的是最后一个重载的返回值类型。**

但这与联合类型有什么关系呢？

重载函数不是能通过函数交叉的方式写么，而我们又能实现联合转交叉。

所以就能拿到联合类型的最后一个类型：

```typescript
type UnionToIntersection<U> = 
    (U extends U ? (x: U) => unknown : never) extends (x: infer R) => unknown
        ? R
        : never

type UnionToFuncIntersection<T> = UnionToIntersection<T extends any ? () => T : never>;
```

UnionToIntersection 的实现在套路六里讲了，忘了的可以去翻一下。

这里简单讲一下：U extends U 是触发分布式条件类型，构造一个函数类型，通过模式匹配提取参数的类型，利用函数参数的逆变的性质，就能实现联合转交叉。

因为函数参数的类型要能接收多个类型，那肯定要定义成这些类型的交集，所以会发生逆变，转成交叉类型。

然后是 UnionToFuncIntersection 的类型：

我们对联合类型 T 做下处理，用 T extends any 触发分布式条件类型的特性，它会把联合类型的每个类型单独传入做计算，最后把计算结果合并成联合类型。把每个类型构造成一个函数类型传入。

这样，返回的交叉类型也就达到了函数重载的目的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bcb7f4931cef4f109b01f93c92013645~tplv-k3u1fbpfcp-watermark.image?)

然后再通过 ReturnType 取返回值的类型，就取到了联合类型的最后一个类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e451d278ee943548565dc3df49ae2d2~tplv-k3u1fbpfcp-watermark.image?)

取到最后一个类型后，再用 Exclude 从联合类型中把它去掉，然后再同样的方式取最后一个类型，构造成元组类型返回，这样就达到了联合转元组的目的：

```typescript
type UnionToTuple<T> = 
    UnionToIntersection<
        T extends any ? () => T : never
    > extends () => infer ReturnType
        ? [...UnionToTuple<Exclude<T, ReturnType>>, ReturnType]
        : [];
```

类型参数 T 为待处理的联合类型。

T extends any 触发了分布式条件类型，会把每个类型单独传入做计算，把它构造成函数类型，然后转成交叉类型，达到函数重载的效果。

通过模式匹配提取出重载函数的返回值类型，也就是联合类型的最后一个类型，放到数组里。

通过 Exclude 从联合类型中去掉这个类型，然后递归的提取剩下的。

这样就完成了联合转元组的目的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60724bc96e1c4c22a9d8166cec03e221~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBAqgdgSwPZwCpIJJ2BATgZwgGNhk4AeGAPigF4oAoKZqAChiggA8c4ATfLCgB+NlwBcsAJR0aAVzgBrOEgDucKJLgQAbnhndeAsZIRwAZnigAlGbXlKV6pi1ejrL18y268DBqCQsIgo6KhyYAA2EOSoNPSewWToWDgExKQo5ImuqJw8EPyCAIZwICJsdjR5Pnq4iTSGhcasVVBmlrg2EMByuGjgEDksogDaAHST8MlI4VExAKJcRJFyfDGoADTdvf2og1RU29Y9fQOQALrD3lCjFwDc-gGDSaGzEdEngvTTb3PR5AA5MVAVAAD5QQEAI1BEMBREBVHuQA)

回过头来看一下，联合类型的处理之所以麻烦，是因为不能直接 infer 来取其中的某个类型，我们是利用了**取重载函数的返回值类型拿到的是最后一个重载类型的返回值**这个特性，把联合类型转成交叉类型来构造重载函数，然后取返回值类型的方式来取到的最后一个类型。然后加上递归，就实现了所有类型的提取。

## join

不知道大家是否还记得“类型编程的意义”那节的 currying 函数的类型定义，那个还是挺复杂的。我们再来做个类似的练习。

```javascript
const res = join('-')('guang', 'and', 'dong');
```

有这样一个 join 函数，它是一个高阶函数，第一次调用传入分隔符，第二次传入多个字符串，然后返回它们 join 之后的结果。

比如上面的 res 是 guang-and-dong。

如果要给这样一个 join 函数加上类型定义应该怎么加呢？要求精准的提示函数返回值的类型。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c3c69b5b51e04fc79168e40e45dfd170~tplv-k3u1fbpfcp-watermark.image?)

我们可以这样来定义这个类型：

```typescript
declare function join<
    Delimiter extends string
>(delimiter: Delimiter):
    <Items extends string[]>
        (...parts: Items) => JoinType<Items, Delimiter>;
```
类型参数 Delimiter 是第一次调用的参数的类型，约束为 string。

join 的返回值是一个函数，也有类型参数。类型参数 Items 是返回的函数的参数类型。

返回的函数类型的返回值是 JoinType 的计算结果，传入两次函数的参数 Delimiter 和 Items。

这里的 JoinType 的实现就是根据字符串元组构造字符串，用到提取和构造，因为数量不确定，还需要递归。

所以 JoinType 高级类型的实现就是这样的：

```typescript
type JoinType<
    Items extends any[],
    Delimiter extends string,
    Result extends string = ''
> = Items extends [infer Cur, ...infer Rest]
        ? JoinType<Rest, Delimiter, `${Result}${Delimiter}${Cur & string}`>
        : RemoveFirstDelimiter<Result>;
```

类型参数 Items 和 Delimiter 分别是字符串元组和分割符的类型。Result 是用于在递归中保存中间结果的。

通过模式匹配提取 Items 中的第一个元素的类型到 infer 声明的局部变量 Cur，后面的元素的类型到 Rest。

构造字符串就是在之前构造出的 Result 的基础上，加上新的一部分 Delimiter 和 Cur，然后递归的构造。这里提取出的 Cur 是 unknown 类型，要 & string 转成字符串类型。

如果不满足模式匹配，也就是构造完了，那就返回 Result，但是因为多加了一个 Delimiter，要去一下。

```typescript
type RemoveFirstDelimiter<
    Str extends string
> = Str extends `${infer _}${infer Rest}` 
        ? Rest
        : Str;
```

去掉开始的 Delimiter 就是个简单字符串字面量类型的提取，就不多解释了。

这样，就实现了 join 的类型定义：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e590182ed5c4209b393fec881490f41~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/CYUwxgNghgTiAEAzArgOzAFwJYHtXwCsctUAeAKHivgBEQIsBbLDEGeEAD1dWAGd4fDDBIBzcgD4AFKAbNWMAFy16TFmwCUiytVIBJVowFce-QcLEBtALoSd1alIB0LgA6wMfZQZBGN8AF4JeAApYlQAFQBPVxB9Qz4AGhU5dRgJAG5ycgwYhAAlXxwANxAAMSwYITpUhVIAZWEObhBeASERVFFggPhG9hNWswADABIAbxJENngAfQBfCamZwqF54fgAfnhVjGV+rJy80PDo2IoHHyNm0wEoVCibRPsUtQUbofaLLueHVeQIBgPm1zJ1RIF4ABySGSCFXYwtEGWZbsADCyBgyRcThROxAQmsLwc2zCJDOcV2yRqbzYyTG43+gMW42p8jYzPR7AAZKCxOs7A4HMpCowSuVKtVVGyYKRGRhMtlyBAQEC4AJekQSFJIQBaSEabWiZD3USQ5KQ+7AM1Q4B4U0aLJAA)

索引类型是我们处理最多的类型，再来练习个索引类型的：

## DeepCamelize

Camelize 是 guang-and-dong 转 guangAndDong，这个我们上节实现过。现在要求递归的把索引类型的 key 转成 CamelCase 的。

比如这样一个索引类型：

```typescript
type obj = {
    aaa_bbb: string;
    bbb_ccc: [
        {
            ccc_ddd: string;
        },
        {
            ddd_eee: string;
            eee_fff: {
                fff_ggg: string;
            }
        }
    ]
}
```
要求转成这样：

```typescript
type DeepCamelizeRes = {
    aaaBbb: string;
    bbbCcc: [{
        cccDdd: string;
    }, {
        dddEee: string;
        eeeFff: {
            fffGgg: string;
        };
    }];
}
```

这要求在 KebabCase 转 CamelCase 的基础上，加上索引类型的递归处理，比较综合。

我们实现下：

```typescript
type DeepCamelize<Obj extends Record<string, any>> = 
    Obj extends unknown[]
        ? CamelizeArr<Obj>
        : { 
            [Key in keyof Obj 
                as Key extends `${infer First}_${infer Rest}`
                    ? `${First}${Capitalize<Rest>}`
                    : Key
            ] : DeepCamelize<Obj[Key]> 
        };
```
类型参数 Obj 为待处理的索引类型，约束为 Record<string, any>。

判断下是否是数组类型，如果是的话，用 CamelizeArr 处理。

否则就是索引类型，用映射类型的语法来构造新的索引类型，Key 为之前的 Key，也就是 Key in keyof Obj，但要做一些变化，也就是 as 重映射之后的部分。

这里的 KebabCase 转 CamelCase 就是提取 _ 之前的部分到 First，之后的部分到 Rest，然后构造新的字符串字面量类型，对 Rest 部分做首字母大写，也就是 Capitialize<Rest>。

值的类型 Obj[Key] 要递归的处理，也就是 DeepCamelize<Obj[Key]>。

其中的 CamelizeArr 的实现就是递归处理每一个元素：

```typescript
type CamelizeArr<Arr> = Arr extends [infer First, ...infer Rest]
    ? [DeepCamelize<First>, ...CamelizeArr<Rest>]
    : []
```
通过模式匹配提取 Arr 的第一个元素的类型到 First，剩余元素的类型到 Rest。

处理 First 放到数组中，剩余的递归处理。

这样我们就实现了索引类型的递归 Camelize：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0c1284106c549409b0a369c3e661090~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBAwghgWwgGwJYC8IEEBOOA8uOAfFALxRFQQAewEAdgCYDOUA2qgwGYQ5QAxVDhbAANFAB00rr34AlCKIC6AKCgaoAfg4ARCBDDwkaTPiEjgxCdMnGUGbHnyLRxNZqgAuDmtWhIKH1De1MIfAB5ACMAK2o6RlYoRQBjAHscJnxRHC4Acwk4BhBiUgp1TWi42npmNgBXBgBrBjSAdwZ2D09NHVDHIkjY4gqe7ygAbyhRsc12AGkIECguKCaltO4oKunZvag4NkXlmsS2AAMAEgnZPkFhUQBfAH1r24UlYEfzmf3ZnSuEwsT2u8DAqGAcDCLk+xG+vz+PR8xwRY2U42CRkQDjMVQWS2UpFRUEeAG5VP5wNA0rFyJMZnBGc8oiyfDl8uTPCyos8UnyfOxiRNiZ4+SlnkxJWzgLkGHlObNHmIhSLNJKmM8DBBpbL5aqNFrntxjT5hYiesbuM88jadRz9STiY8ZmpnZTApj+phXHTPdjoTSYsRyUA)
    
递归是很常用的套路，比如之前遇到一个这样的需求：

## AllKeyPath
    
需求是拿到一个索引类型的所有 key 的路径。
    
比如这样的索引类型：
    
```typescript
type Obj = {
    a: {
        b: {
            b1: string
            b2: string
        }
        c: {
            c1: string;
            c2: string;
        }
    },
}
```

希望返回 a、a.b、a.b.b1、a.b.b2、a.c、a.c.c1、a.c.c2 这些全部的 path。 

这里需要遍历 Key，用映射类型的语法，然后要递归构造 path，最后取所有 key 的遍历结果。
    
也就是这样写：

```typescript
type AllKeyPath<Obj extends Record<string, any>> = {
  [Key in keyof Obj]: 
    Key extends string
      ? Obj[Key] extends Record<string, any>
        ? Key | `${Key}.${AllKeyPath<Obj[Key]>}`
        : Key
      : never
}[keyof Obj];
```

参数 Obj 是待处理的索引类型，通过 Record<string, any> 约束。
    
用映射类型的语法，遍历 Key，并在 value 部分根据每个 Key 去构造以它为开头的 path。
    
因为推导出来的 Key 默认是 unknown，而其实明显是个 string，所以 Key extends string 判断一下，后面的分支里 Key 就都是 string 了。
    
如果 Obj[Key] 依然是个索引类型的话，就递归构造，否则，返回当前的 Key。
    
我们最终需要的是 value 部分，所以取 [keyof Obj] 的值。keyof Obj 是 key 的联合类型，那么传入之后得到的就是所有 key 对应的 value 的联合类型。
    
这样就完成了所有 path 的递归生成：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2070a6aedaea47b8801eb0420eb51831~tplv-k3u1fbpfcp-watermark.image?)
    
[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBA8gRgKygXigbwFBW1AhgLnSxxLkMxMpzgEZCBnYAJwEsA7Ac2KtICYHm7LjygBfbpQDG5CSMl0ojVpwDcsnpP6LBq9dnElRAGgziMoSFACCAGxsBpCCAAKuYAAsAPPCQQAHsAQbAAm9FAAShCSAPZMwZ5KQkZ4bCAAfGkoRNgA2o4gUOxQANZO0QBmsIgAuoQS+VD+gSFhiZzqAPxVCHlO1Y0BQaERUbHxbRzJuKlpelBdDQA+UAAGACRo+aIAdBu2Dk6uHt6IvSDVaaIrc4T56oRsEABuEEymOaUgFd3Vahjm4Gg+3yR3ckTCqGBhzcXh8aTUQA)
 
最后再练习下内置的高级类型，这些比较常用：

## Defaultize

实现这样一个高级类型，对 A、B 两个索引类型做合并，如果是只有 A 中有的不变，如果是 A、B 都有的就变为可选，只有 B 中有的也变为可选。

比如下面这样：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92b2052f392d475c80d4a42c8a006c7c~tplv-k3u1fbpfcp-watermark.image?)

aaa 是只有 A 有的，所以不变。

bbb 是两者都有的，变为可选。

ccc 是只有 B 有的，变为可选。

怎么实现这样的高级类型呢？

**索引类型处理可以 Pick 出每一部分单独处理，最后取交叉类型来把处理后的索引类型合并到一起。**

上面的类型就可以这样实现：

```typescript
type Defaultize<A, B> = 
    & Pick<A, Exclude<keyof A, keyof B>>
    & Partial<Pick<A, Extract<keyof A, keyof B>>>
    & Partial<Pick<B, Exclude<keyof B, keyof A>>>
```

Pick 出 A、B 中只有 A 有的部分，也就是去 A 中去掉了 B 的 key： Exclude<keyof A, keyof B>。

然后 Pick 出 A、B 都有的部分，也就是 Extract<keyof A, keyof B>。用 Partial 转为可选。

之后 Pick 出只有 B 有的部分，也就是 Exclude<keyof B, keyof A>。用 Partial 转为可选。

最后取交叉类型来把每部分的处理结果合并到一起。

这样就实现了我们的需求：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd40148e85ae4dd293598c9433286215~tplv-k3u1fbpfcp-watermark.image?)

为啥这里没显示最终的类型呢？

因为 ts 只有在类型被用到的时候才会去做类型计算，根据这个特点，我们可以用映射类型的语法构造一个一摸一样的索引类型来触发类型计算。

```typescript
type Copy<Obj extends Record<string, any>> = {
    [Key in keyof Obj]: Obj[Key]
}
```
这就是标准的映射类型的语法，就不多解释了。

这样就能看到最终的类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d70b5fb373664c9fb4bad65932786550~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBAIhBmBDArgG2ASwF4QDwEEAaKAIQD4oBeKAKCnqgDIoAFDAYwGsDiBRAD3apkAEzycIIAPbwoRKBOmzyZOg2YtEAJ0yJUuNlx5QBwLYnbBcimXOI3lZJ2vobtu-Ye4k+g4WOtJWx8FINl8J1UaUEgoAGEpMBBcAHkAIwArKAh+YAgAOxEAZygAJQh2KS0RXCKzDHyAc2JEfJAnKigAbxcoAG0AaUkoBtClKHSMgF0ALgnMwckpmgBfGmjwaHxOnoYoRAO5gEYTwl60i7mAJhvVgG51mOgSHfPLqBurs732X7mAZkBq0em1gCBQ6GwEHKJWoCSSuDgSDQmBwxhUDxoQA)

## 总结

这节我们又做了很多高难度的案例，提高练习的难度才能更好的提升类型编程水平。

首先我们学会了函数重载的三种写法，这个是为后面的联合转元组做铺垫的，联合转元组利用了**提取重载函数的返回值会返回最后一个重载的返回值类型**的特性，通过联合转交叉构造出重载类型来提取的联合类型中的类型，然后递归的处理。

之后我们实现了 join 的类型定义，这个综合用到了元组的提取和字符串字面量类型的构造，再加上递归。

然后我们又实现了 DeepCamelize，递归的处理索引类型，把 Key 转为 CamelCase 的形式，比较综合的案例。
    
之后实现了 AllKeyPath 的类型，通过映射类型遍历 Key，用它来递归构造不同的 Path，最后取 value，就是结果。

最后练习了内置的高级类型 Pick、Exclude、Extract、Partial 等，**处理索引类型的常用套路就是 Pick 出每一部分单独做处理，最后取交叉类型把结果合并到一起**。

能够实现这些高难度的类型，相信你的类型编程水平就已经很不错了。

[本文案例的合并](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/PTAEl-FQHU0WcTF94goAJgUwMYBsCGAnZoBmArgHaoAuAlgPbEEmoAUxmAtsgFygDOZ2FxAcwCUnHn0EBuJGiy46pSjXmNmbTsUIsARsmwjQG7bqnwipBgHJMFoVLOMAjLfgv+ZXfkyo8AMXqgAb3hQENAmVg5uXn5hUWjJYNDwtQNNHT11NONQeABfFxQMHDxUGh5lACZOP1ITewrLa2d6hicTeDIATwAHX3oK0ABeBmTIsRihIYA+KPFhUAAyMNHMoz1p1LXnaSK5UuJy+wBmav66+iPGmzsL1u37RVpMREQGTFX0gBpQLQ-dfUM6RuCmoTxebzic2+v1mE0hMWB5FBoGer3eKOInWhnEwmMmQVCoFwZEI2CeoAA1D8pPl4PtyrguA4hijwQ5vhVtvSyETkFwBoNWa8rBZvhYtNcXCBQABVYiggAqVAVhG66GQLi6vVl8poSoAksR3NguGhHgAeGUzQWJEIMGWgZAAD3cxEQXFloAA-GEnZwZZNBjMSABrYhUADutHUyAAbv9HS7kG6PQw-aB+PhdKAAEqB4PEMOR4i2wne3Olwkx+PYTU9PByxXK1Xq80K605QmNvVUQ3G01ImjmyuhBWJ13ujGdcsMfOgMfV3SlmbOiepueZ7M55AkskK+sjkI+gDaADpz93iEqVWrkOaAKJOjCEFBt77b3dX+tTKbvnekr9egAXUPUBOGPID2i1BtdSvZtb23D1BUva8WzvEVQAAH1AcULCwnDUAsKYTGlAArKh+AKGRimUR5QHI-hh0JAARZB0AoFgKGNcdk0ncZBHgKYGBQdjOONThWNErj-nYUtzX1dwWA9VdeI9fiBAgqZQIYc9T26HAyC4TgFOQJS5wAKQowC7xMpTvkkjjpOwYi621bcWCoeMfAoE0yAcsTdHNABlXgeJTWFBA7ELsDCycAAMABIAk3GKAH1ciSlLcz5Mhcji8tELIThopMaDQEs-h916JjQls5Sk3C3FOggz5S38pzYrU+IBFawlEMIdAeRU8L1JZCwLEElk6s60BjyygBhUlvl0rLCpAstQh9CrrPNQr7LYxzjW+RKAn6waMoCdrjQuxaYqWdS8q0jaQk4dzPOQbzfKuwKzrIFyXHVHlGRZBjiEsABaGxLAEQhcQEUUcNxRAEYsRAaHh7ZpVY5BunmiJ0FQTBTVcvA8bYdiAC9kAAQWwbBzVp5yWUZma5uILMYs+nhlvPVacvWzbZux3H8YoKnzS5v6edPMmDqpxndpyqYBZe2aQI6etQGF2XKbvAB5LRSJm7dSmwRBzXU74mp-FlSwNo3hsnUNwyjCDQJ9HWxZpunzXtp7ns4AJO2ewljwAaWQad+FAENI6ofBQHt4OQ42onQAj6dHY9E6ssl3JUsy9mtxyvLQJTwWTrzpK8e6LjMF1xWeCmUvy-LzgM7L0IgLArXkBxz3xft8PI6AmZQNyEiwGp9B0AzgAFTAyAACw17UqENlkCVCTAd9SrR9-hBJCX3rRUtQc-wNArfy-P1BUpeRBD4EKQQ9yXrnuvlOH9Svuxm6l-W6-1SvgEBgdO4bRAfgVKAgYFPwAeXfIr9SwgVpGVbWosqaIRZOg8mXtzTr1Iv9MqSdBSf3RJ-Y+YDW4-AcE-cBPwqgRQEOPUCqAqGt1QLQph8CU6oEYepHhhJEGhDfnkEmoBp6z0jgvZevsN5Z2yqbc2lspw21IYkYeUdaCx06PHROhsgKcFLBnGa6kRw+iHhnbuCiTZUDNhbbqVtMT+w2j6Ex2EToZ1yKeJKkj56LyXnI0imjR4twDunSOI5Fy1lyMeHRej7aQRcKvPAfjpEBKwYKNJnQZGBIIf9eAWNkCeAGpQKm4jWIlMGng6m3wABCHZSxLDnhQVAIYGbfEfM+V88SE61JjnHBODSXGLFAAvbAlB67mhaW0jpoBHy8C8GQc0vSJHfFWcMkZzSDIUCmTM9pdTOlPnQC+O8Gz1mDIkT+LSKTQDzSoN0ToQTjZoDscoxxqiOyf00RmbRlzEmcEsSPMRtzqab1LDvdEDhoXvxCCfTgFREV5FKprOp4Lj4H1AIiiosLQC304EcQlIK0HFMwKUr2mS7kPKeZUsl1Txb9OGSYIAA)







## 16.新语法 infer extends 是如何简化类型编程的

我们知道，TypeScript 支持 infer 来提取类型的一部分，通过模式匹配的方式。

比如元组类型提取最后一个元素的类型：

```typescript
type Last<Arr extends unknown[]> = 
    Arr extends [...infer rest,infer Ele]
        ? Ele 
        : never;
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb6b26ec804b4bad902108b846b04604~tplv-k3u1fbpfcp-watermark.image?)

比如函数提取返回值类型：

```typescript
type GetReturnType<Func extends Function> = 
    Func extends (...args: any[]) => infer ReturnType 
        ? ReturnType 
        : never;
```

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7093a4345d79478e92cec8ab8306a8b1~tplv-k3u1fbpfcp-watermark.image?)

比如字符串提取一部分，然后替换：

```typescript
type ReplaceStr<
    Str extends string,
    From extends string,
    To extends string
> = Str extends `${infer Prefix}${From}${infer Suffix}` 
        ? `${Prefix}${To}${Suffix}` : Str;
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b38c21a0f2f94024a523da588057c4ff~tplv-k3u1fbpfcp-watermark.image?)

**模式匹配就是通过一个类型匹配一个模式类型，需要提取的部分通过 infer 声明一个局部变量，这样就能从局部变量里拿到提取的类型。**

infer 的模式匹配用法还是挺好理解的。

但是 infer 有一个问题，比如这样：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6022266e758241cdb6727df05dfb7c01~tplv-k3u1fbpfcp-watermark.image?)

从 string 数组中提取的元素，默认会推导为 unknown 类型，这就导致了不能直接把它当 string 用：


![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d73fb694895d4dd9b2ac22951b1af62c~tplv-k3u1fbpfcp-watermark.image?)

那怎么办呢？

之前的处理方式是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b3740978c8b847d2a7be77e2f5f07fd0~tplv-k3u1fbpfcp-watermark.image?)

加一层判断，这样 Last 就推导为 string 类型了。

或者也可以和 string 取交叉类型：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/854eb7496f3c43cdbe4a6e8e60f8b143~tplv-k3u1fbpfcp-watermark.image?)

这样也可以作为 string 来用。

但是我们明明知道这里就是 string，却还需要 & string 或者 xxx extends string 来转换一次，这也太麻烦了。

TS 也知道有这个问题，所以在 4.7 就引入了新语法：infer extends。

现在我们可以这样写：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41ecbe95c16d45c98b12141d8c653d63~tplv-k3u1fbpfcp-watermark.image?)

**infer 的时候加上 extends 来约束推导的类型，这样推导出的就不再是 unknown 了，而是约束的类型。**

[试一下](https://www.typescriptlang.org/play?ts=4.8.0-beta#code/C4TwDgpgBAKhDOwAyBDRAeAggJ21CAHsBAHYAm8Ui2AliQOYDaAugHxQC8UAUFH1DjyFi5SowB0kugDMIeAEoJgAGigy5UVIma9+egPxQABoABzQHAqgADlAVHKB6M0BY-wBIA3luBQAZFWC0GAXyO6enwAXFAkEABucgDc3NygkLBKrgBMWLj4RKQUXj5MbJw8eoKZIjkSUiSyCkqq6niuOkH8hq6l2ZTUdPSBzS3G5tb2zq7+vX1QoeFR2OP8U5ExcQnQcIiuAMzpQlmiud0s7Fy9JcIdUBXi9VCKiHVVGm1ne10MTX2Gppa2ji5owGMJgsZrEgA)

这个语法是 TS 4.7 引入的，在 4.8 又完善了一下。

比如这样一个类型：

```typescript
type NumInfer<Str> = 
    Str extends `${infer Num extends number}`
        ? Num
        : never;
```

在 4.7 的时候推导结果是这样：


![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b1625294f5f4de68a0351dc31e73a08~tplv-k3u1fbpfcp-watermark.image?)

而 4.8 就是这样了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d80ea71fccc24d68a2ed99c7a5b008a9~tplv-k3u1fbpfcp-watermark.image?)

也就是说 4.7 的时候推导出的就是 extends 约束的类型，但是 4.8 的时候，如果是基础类型，会推导出字面量类型。

有了这个语法之后，除了能简化类型编程的逻辑之外，也能实现一些之前实现不了的功能：

比如提取枚举的值的类型：

```typescript
enum Code {
    a = 111,
    b = 222,
    c = "abc"
}
```
我们都是这样写：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db28a55919464599b0f346d71f9cc822~tplv-k3u1fbpfcp-watermark.image?)

但是有的值明明是数字，却被作为了字符串，所以要再处理一下，转换成数字类型，这时候就可以用 infer extends 了：

```typescript
type StrToNum<Str> =
  Str extends `${infer Num extends number}`
    ? Num
    : Str
```
做完 string 到 number 的转换，就拿到了我们想要的结果：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c809ce782cb6461a9eaa21be1e1b79d8~tplv-k3u1fbpfcp-watermark.image?)

这就是 infer extends 的第二个作用。

处理 string 转 number 之外，也可以转 boolean、null 等类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aee1f9d80c1645e48991d5eabba22af8~tplv-k3u1fbpfcp-watermark.image?)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d3518ad7481a47c38137509ae7ffd433~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.8.0-beta#code/KYOwrgtgBAwg9gE2FA3gKCpqBDKBeKARmIBoMsAjfKAJjrKygGNqBybCp1tAXzTQAuATwAOyAMoCATgBU4AOUgAeSVIB8+cqqjAAHgNAIAzlAAGAEhQBLEADNgUqIuh6DIY1HAQKDnqfKYAPxOkAFQAFxQqvzCYlBSwCYEqnLOShYo8Eh+agDcMaIS0nIAQnBwADbA2CAq0hp4WtI6+oYmGTb2jmWVLW4eFOVVNX5hwT0VYZHRgoXxiTTUKXAT1bWs0mDArHkFccuKFRV16pqY2q5tZpadDiFHfVfgR6OMwYeTjNPSe8gJRgBmJbFBRgI5KVjPCo7XJAA)

## 总结

Typescript 支持 infer 类型，可以通过模式匹配的方式，提取一部分类型返回。

但是 infer 提取出的类型是 unknown，后面用的时候需要类似和 string 取交叉类型，或者 xxx extends string 这样的方式来转换成别的类型来用。这样比较麻烦。

所以 TS 4.7 实现了 infer extends 的语法，可以指定推导出的类型，这样简化了类型编程。

而且，infer extends 还可以用来做类型转换，比如 string 转 number、转 boolean 等。

要注意的是，4.7 的时候，推导出的只是 extends 约束的类型，比如 number、boolean，但是 4.8 就能推导出字面量类型了，比如 1、2、true、false 这种。

有了 infer extends，不但能简化类型编程，还能实现一些之前很难实现的类型转换。


## 17.原理篇：逆变、协变、双向协变、不变

深入学习 TypeScript 类型系统的话，逆变、协变、双向协变、不变是绕不过去的概念。

这些概念看起来挺高大上的，其实并不复杂，这节我们就来学习下它们吧。

## 类型安全和型变

TypeScript 给 JavaScript 添加了一套静态类型系统，是为了保证类型安全的，也就是保证变量只能赋同类型的值，对象只能访问它有的属性、方法。

比如 number 类型的值不能赋值给 boolean 类型的变量，Date 类型的对象就不能调用 exec 方法。

这是类型检查做的事情，遇到类型安全问题会在编译时报错。

但是这种类型安全的限制也不能太死板，有的时候需要一些变通，比如子类型是可以赋值给父类型的变量的，可以完全当成父类型来使用，也就是“型变（variant）”（类型改变）。

这种“型变”分为两种，一种是子类型可以赋值给父类型，叫做协变（covariant），一种是父类型可以赋值给子类型，叫做逆变（contravariant）。

先来看下协变：

### 协变（covariant）

其中协变是很好理解的，比如我们有两个 interface：

```typescript
interface Person {
    name: string;
    age: number;
} 

interface Guang {
    name: string;
    age: number;
    hobbies: string[]
}
```

这里 Guang 是 Person 的子类型，更具体，那么 Guang 类型的变量就可以赋值给 Person 类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/235e7b3fdd0f42f8b617a0b6dcb7e913~tplv-k3u1fbpfcp-watermark.image?)

这并不会报错，虽然这俩类型不一样，但是依然是类型安全的。

这种子类型可以赋值给父类型的情况就叫做协变。

[试一下](https://www.typescriptlang.org/play?strictFunctionTypes=false&ts=4.5.0-beta#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyxyIcAthAFzIZhSgDmA3ESXI9aQK7kBG0VgF9kBAqEixEKAOLc4IRvjbEylGnQaLWJZBy4heAqDpIALLHz7AIGDfSYBtALoEhYgDYQwyAA6YcGnQobFwAXmVdNS4AchiAGhU9ThoAJgAGN1YvH0Z5RRo5BSUIwiiKWLzihKT9NPTE3QsrGztkRxjfDzgAT2RGCoTkGIB3BjAmGNchVgJ-EJxkCKrtAiA)

为什么要支持协变很容易理解：类型系统支持了父子类型，那如果子类型还不能赋值给父类型，还叫父子类型么？

所以型变是实现类型父子关系必须的，它在保证类型安全的基础上，增加了类型系统的灵活性。

逆变相对难理解一些：

### 逆变（contravariant）

我们有这样两个函数：

```typescript
let printHobbies: (guang: Guang) => void;

printHobbies = (guang) => {
    console.log(guang.hobbies);
}

let printName: (person: Person) => void;

printName = (person) => {
    console.log(person.name);
}
```

printHobbies 的参数 Guang 是 printName 参数 Person 的子类型。

那么问题来了，printName 能赋值给 printHobbies 么？printHobbies 能赋值给 printName 么？

测试一下发现是这样的：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/874b9002d5f742aaad5c8a086cff2d0b~tplv-k3u1fbpfcp-watermark.image?)

printName 的参数 Person 不是 printHobbies 的参数 Guang 的父类型么，为啥能赋值给子类型？

因为这个函数调用的时候是按照 Guang 来约束的类型，但实际上函数只用到了父类型 Person 的属性和方法，当然不会有问题，依然是类型安全的。

这就是逆变，函数的参数有逆变的性质（而返回值是协变的，也就是子类型可以赋值给父类型）。


那反过来呢，如果 printHoobies 赋值给 printName 会发生什么？

因为函数声明的时候是按照 Person 来约束类型，但是调用的时候是按照 Guang 的类型来访问的属性和方法，那自然类型不安全了，所以就会报错。

但是在 ts2.x 之前支持这种赋值，也就是父类型可以赋值给子类型，子类型可以赋值给父类型，既逆变又协变，叫做“双向协变”。

但是这明显是有问题的，不能保证类型安全，所以之后 ts 加了一个编译选项 strictFunctionTypes，设置为 true 就只支持函数参数的逆变，设置为 false 则是双向协变。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46a74c546c2d41248e6012c10a2ca790~tplv-k3u1fbpfcp-watermark.image?)

我们把 strictFunctionTypes 关掉之后，就会发现两种赋值都可以了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cdd741c42444dfd952b536e1e49147c~tplv-k3u1fbpfcp-watermark.image?)

这样就支持函数参数的双向协变，类型检查不会报错，但不能严格保证类型安全。

开启之后，函数参数就只支持逆变，子类型赋值给父类型就会报错：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca53c326b66245ba9b80eee6ba8691bd~tplv-k3u1fbpfcp-watermark.image?)

[试一下（双向协变的情况）](https://www.typescriptlang.org/play?strictFunctionTypes=false&ts=4.5.0-beta#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyxyIcAthAFzIZhSgDmA3ESXI9aQK7kBG0VgF9kBAqEixEKAOLc4IRvjbEylGnQaLWJZBy4heAqDpIALLHz7AIGDfSYBtALoEhYgDYQwyAA5awAAlLa1saAApGeUUaOQVGAEpkAF4APmQANyxgABNWAn8JYKsbDBTkSOjElPTCXQQcbC8AOg8sRkr45osS2wThT28-AIA5Ci5w30wcGnQobBAktMzsvLFC8DHKcsnpxZrlesasFraOqfmcZrUIfrd1gOLQsuThiS2IfI2wD-Lvp9K+SAA)

[试一下（逆变的情况）](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/JYOwLgpgTgZghgYwgAgArQM4HsTIN4BQyxyIcAthAFzIZhSgDmA3ESXI9aQK7kBG0VgF9kBAqEixEKAOLc4IRvjbEylGnQaLWJZBy4heAqDpIALLHz7AIGDfSYBtALoEhYgDYQwyAA5awAAlLa1saAApGeUUaOQVGAEpkAF4APmQANyxgABNWAn8JYKsbDBTkSOjElPTCXQQcbC8AOg8sRkr45osS2wThT28-AIA5Ci5w30wcGnQobBAktMzsvLFC8DHKcsnpxZrlesasFraOqfmcZrUIfrd1gOLQsuThiS2IfI2wD-Lvp9K+SAA)

再举个逆变的例子，大家觉得下面这样的 ts 代码会报错么：

```typescript
type Func = (a: string) => void;

const func: Func = (a: 'hello') => undefined
```

答案是参数的位置会，返回值的位置不会：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad03ca63263943b09763c058a91793c2~tplv-k3u1fbpfcp-watermark.image?)

参数的位置是逆变的，也就是被赋值的函数参数要是赋值的函数参数的子类型，而 string 不是 'hello' 的子类型，所以报错了。

返回值的位置是协变的，也就是赋值的函数的返回值是被赋值的函数的返回值的子类型，这里 undefined 是 void 的子类型，所以不报错。

在类型编程中这种逆变性质有什么用呢？

还记得之前联合转交叉的实现么？

```typescript
type UnionToIntersection<U> = 
    (U extends U ? (x: U) => unknown : never) extends (x: infer R) => unknown
        ? R
        : never
```

类型参数 U 是要转换的联合类型。

U extends U 是为了触发联合类型的 distributive 的性质，让每个类型单独传入做计算，最后合并。

利用 U 做为参数构造个函数，通过模式匹配取参数的类型。

结果就是交叉类型：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07cb622007ca464ba9cd42c4a91e39f3~tplv-k3u1fbpfcp-watermark.image?)

我们通过构造了多个函数类型，然后模式提取参数类型的方式，来实现了联合转交叉，这里就是因为函数参数是逆变的，会返回联合类型的几个类型的子类型，也就是更具体的交叉类型。

再就是之前提取返回值类型的时候，当时说参数这里只能用 any[] 而不能用 unknown[]

```typescript
type GetReturnType<Func extends Function> = 
    Func extends (...args: any[]) => infer ReturnType 
        ? ReturnType : never;
```
这就是因为函数参数是逆变的，如果是 unknown[]，那当 Func 是这个函数的子类型，它的参数得是 unknown 的父类型，这显然是不可能的，所以这里只能用 any。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e25d2e1ec8074fc6ae58e93a904af89f~tplv-k3u1fbpfcp-watermark.image?)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/809321bf0c374abe807b21ef9d70ac5f~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwCV4FcBOA7AKuCAeAYsugMZQQAewE6AJgM5SEnACWA9ugHxQC8jRpClVoMAFADpJAQ1QBzOgC4oRANbo2Ad3QBtALoBKXtxboAZhFRQkwNFhxQA-FZQZskKEvQQAbhYDcAFABoO7Wtm4QSHTIADYxwLyw8GGuOLii6FIAthBKdMCoJrKGPNwA5DQcsmWcgUA)

当然，如果不开启 strictFunctionTypes 的话，参数是双向协变，那也可以正常推导。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac53a13338b74ef19950564fa51cadc8~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?strictFunctionTypes=false#code/C4TwDgpgBA4hwCV4FcBOA7AKuCAeAYsugMZQQAewE6AJgM5SEnACWA9ugHxQC8jRpClVoMAFADpJAQ1QBzOgC4oRANbo2Ad3QBtALoBKXtxboAZhFRQkwNFhxQA-FZQZskKEvQQAbhYDcAFBBoO7Wtm4QSHTIADYxwLyw8GGuOLii6FIAthBKdMCoJrKGPNwA5DQcsmWcgUA)

逆变和协变都是型变，是针对父子类型而言的，非父子类型自然就不会型变，也就是不变：

### 不变（invariant）

非父子类型之间不会发生型变，只要类型不一样就会报错：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bf4a8be10b5413b96c302a34c6f33c9~tplv-k3u1fbpfcp-watermark.image?)

那类型之间的父子关系是怎么确定的呢，好像也没有看到 extends 的继承？

## 类型父子关系的判断

像 java 里面的类型都是通过 extends 继承的，如果 A extends B，那 A 就是 B 的子类型。这种叫做名义类型系统（nominal type）。

而 ts 里不看这个，只要结构上是一致的，那么就可以确定父子关系，这种叫做结构类型系统（structual type）。

还是拿上面那个例子来说：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22f32f8252c947c7ae1d813367595cc0~tplv-k3u1fbpfcp-watermark.image?)

Guang 和 Person 有 extends 的关系么？

没有呀。

那是怎么确定父子关系的？

通过结构，更具体的那个是子类型。这里的 Guang 有 Person 的所有属性，并且还多了一些属性，所以 Guang 是 Person 的子类型。

注意，这里用的是更具体，而不是更多。

判断联合类型父子关系的时候， 'a' | 'b' 和 'a' | 'b' | 'c' 哪个更具体？

'a' | 'b' 更具体，所以  'a' | 'b' 是 'a' | 'b' | 'c' 的子类型。

测试下：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c2159490e96f4ce6a30db970af82d57f~tplv-k3u1fbpfcp-watermark.image?)

## 总结

ts 通过给 js 添加了静态类型系统来保证了类型安全，大多数情况下不同类型之间是不能赋值的，但是为了增加类型系统灵活性，设计了父子类型的概念。父子类型之间自然应该能赋值，也就是会发生型变（variant）。

型变分为逆变（contravariant）和协变（covariant）。协变很容易理解，就是子类型赋值给父类型。逆变主要是函数赋值的时候函数参数的性质，参数的父类型可以赋值给子类型，这是因为按照子类型来声明的参数，访问父类型的属性和方法自然没问题，依然是类型安全的。但反过来就不一定了。

不过 ts 2.x 之前反过来依然是可以赋值的，也就是既逆变又协变，叫做双向协变。

为了更严格的保证类型安全，ts 添加了 strictFunctionTypes 的编译选项，开启以后函数参数就只支持逆变，否则支持双向协变。

型变都是针对父子类型来说的，非父子类型自然就不会型变也就是不变（invariant）。

ts 中父子类型的判定是按照结构来看的，更具体的那个是子类型。

理解了如何判断父子类型（结构类型系统），父子类型的型变（逆变、协变、双向协变），很多类型兼容问题就能得到解释了。


## 18.原理篇：编译 ts 代码用 tsc 还是 babel？

编译 TypeScript 代码用什么编译器？

那还用说，肯定是 ts 自带的 compiler 呀。

但其实 babel 也能编译 ts 代码，那用 babel 和 tsc 编译 ts 代码有什么区别呢？

我们分别来看一下：

## tsc 的编译流程

typescript compiler 的编译流程是这样的：


![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85851ebe6f2d41a28ca3885d91beb969~tplv-k3u1fbpfcp-watermark.image?)

源码要先用 Scanner 进行词法分析，拆分成一个个不能细分的单词，叫做 token。

然后用 Parser 进行语法分析，组装成抽象语法树（Abstract Syntax Tree）AST。

之后做语义分析，包括用 Binder 进行作用域分析，和有 Checker 做类型检查。如果有类型的错误，就是在 Checker 这个阶段报的。

如果有 Transformer 插件（tsc 支持 custom transform），会在 Checker 之后调用，可以对 AST 做各种增删改。

类型检查通过后就会用 Emmiter 把 AST 打印成目标代码，生成类型声明文件 d.ts，还有 sourcemap。

> sourcemap 的作用是映射源码和目标代码的代码位置，这样调试的时候打断点可以定位到相应的源码，线上报错的时候也能根据 sourcemap 定位到源码报错的位置。

tsc 生成的 AST 可以用 [astexplorer.net](https://astexplorer.net/) 可视化的查看：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ff97c94315b4c3fadcb1e8f16218f02~tplv-k3u1fbpfcp-watermark.image?)

生成的目标代码和 d.ts 和报错信息也可以用 [ts playground](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/DYUwLgBA9gRgVgLggJRAYygJwCYB4DOYmAlgHYDmANBAIakCeAfANwBQrscEAvBAN6sIQiKRoBbEEgDk5AK51yU1gF8gA) 来直接查看：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7a0904a087a419a9229a7cb82045a4d~tplv-k3u1fbpfcp-watermark.image?)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63d3150e4d0b4195abf37c5a79394769~tplv-k3u1fbpfcp-watermark.image?)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bff067eb9e342d1bf1a112a34c1db89~tplv-k3u1fbpfcp-watermark.image?)

大概了解了 tsc 的编译流程，我们再来看下 babel 的：

## babel 的编译流程

babel 的编译流程是这样的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b515ccf55fe4706a128ad38b50b1c24~tplv-k3u1fbpfcp-watermark.image?)

源码经过 Parser 做词法分析和语法分析，生成 token 和 AST。

AST 会做语义分析生成作用域信息，然后会调用 Transformer 进行 AST 的转换。

最后会用 Generator 把 AST 打印成目标代码并生成 sourcemap。

babel 的 AST 和 token 也可以用 [astexplorer.net](https://astexplorer.net/) 可视化的查看：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd0269a40767438d83200b7b88f51163~tplv-k3u1fbpfcp-watermark.image?)

如果想看到 tokens，需要点开设置，开启 tokens：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a9b86936db44ee39b4037073ca9b504~tplv-k3u1fbpfcp-watermark.image?)

而且 babel 也有 [playground](https://www.babeljs.cn/repl)（babel 的叫 repl） 可以直接看编译之后生成的代码：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ead3c55a7798411892d5a35de927e997~tplv-k3u1fbpfcp-watermark.image?)

其实对比下 tsc 的编译流程，区别并不大：

Parser 对应 tsc 的 Scanner 和 Parser，都是做词法分析和语法分析，只不过 babel 没有细分。

Transform 阶段做语义分析和代码转换，对应 tsc 的 Binder 和 Transformer。**只不过 babel 不会做类型检查，没有 Checker。**

Generator 做目标代码和 sourcemap 的生成，对应 tsc 的 Emitter。**只不过因为没有类型信息，不会生成 d.ts。**

对比两者的编译流程，会发现 babel 除了不会做类型检查和生成类型声明文件外，tsc 能做的事情，babel 都能做。

看起来好像是这样的，但是 babel 和 tsc 实现这些功能是有区别的：

## babel 和 tsc 的区别

抛开类型检查和生成 d.ts 这俩 babel 不支持的功能不谈，我们看下其他功能的对比：

分别对比下语法支持和代码生成两方面：

### 语法支持

tsc 默认支持最新的 es 规范的语法和一些还在草案阶段的语法（比如 decorators），想支持新语法就要升级 tsc 的版本。

babel 是通过 @babel/preset-env 按照目标环境 targets 的配置自动引入需要用到的插件来支持标准语法，对于还在草案阶段的语法需要单独引入  @babel/proposal-xx 的插件来支持。

所以如果你只用标准语法，那用 tsc 或者 babel 都行，但是如果你想用一些草案阶段的语法，tsc 可能很多都不支持，而 babel 却可以引入 @babel/poposal-xx 的插件来支持。

从支持的语法特性上来说，babel 更多一些。

### 代码生成

tsc 生成的代码没有做 polyfill 的处理，想做兼容处理就需要在入口引入下 core-js（polyfill 的实现）。

```typescript
import "core-js";

Promise.resolve;
```

babel 的 @babel/preset-env 可以根据 targets 的配置来自动引入需要的插件，引入需要用到的 core-js 模块，


![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0fc4bee497346d0aaf6b568f03f6012~tplv-k3u1fbpfcp-watermark.image?)

引入方式可以通过 useBuiltIns 来配置：

entry 是在入口引入根据 targets 过滤出的所有需要用的 core-js。

usage 则是每个模块按照使用到了哪些来按需引入。

```javascript
module.exports = {
    presets: [
        [
            '@babel/preset-typescript',
            '@babel/preset-env',
            {
                targets: '目标环境',
                useBuiltIns: 'entry' // ‘usage’
            }
        ]
    ]
}
```

此外，babel 会注入一些  helper 代码，可以通过 @babel/plugin-transform-runtime 插件抽离出来，从 @babel/runtime 包引入。

使用 transform-runtime 之前：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59a09d4e83964506bf43471ff8240634~tplv-k3u1fbpfcp-watermark.image?)

使用 transform-runtime 之后：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2846306a47b648fda5564d2cd071fb79~tplv-k3u1fbpfcp-watermark.image?)

（transform runtime 顾名思义就是 transform to runtime，转换成从 runtime 包引入 helper 代码的方式）

所以一般babel 都会这么配：
```javascript
module.exports = {
    presets: [
        [
            '@babel/preset-typescript'
        ],
        [
            '@babel/preset-env',
            {
                targets: '目标环境',
                useBuiltIns: 'usage' // ‘entry’
            }
        ]
    ],
    plugins: [ '@babel/plugin-transform-runtime']
}
```
当然，这里不是讲 babel 怎么配置，我们绕回主题，babel 和 tsc 生成代码的区别：

**tsc 生成的代码没有做 polyfill 的处理，需要全量引入 core-js，而 babel 则可以用 @babel/preset-env 根据 targets 的配置来按需引入 core-js 的部分模块，所以生成的代码体积更小。**

看起来用 babel 编译 ts 代码全是优点？

也不全是，babel 有一些 ts 语法并不支持：

## babel 不支持的 ts 语法

babel 是每个文件单独编译的，而 tsc 不是，tsc 是整个项目一起编译，会处理类型声明文件，会做跨文件的类型声明合并，比如 namespace 和 interface 就可以跨文件合并。

所以 babel 编译 ts 代码有一些特性是没法支持的：

### const enum 不支持

enum 编译之后是[这样的](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/KYOwrgtgBACsBOBnA9iA3gKCtqARVA5lALxQDkAJoWQDRY4DiYAhiEaWQS22RgL4YMAY1QoANsAB0Y5AQAUcJKkn42ASgDcQA)：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b6d559ff59945c69d0e6809caf7f9ef~tplv-k3u1fbpfcp-watermark.image?)
而 const enum 编译之后是直接替换用到 enum 的地方为对应的值，是[这样的](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/MYewdgzgLgBApmArgWxgBTgJwuA3gKBiJgBFwBzGAXhgHIATC2gGkOIHFEBDMSm28t1618AX3z5QkEABs4AOhkhyACgzZw8srwCUAbiA)：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef04cae64f284a55ade58a868084d85e~tplv-k3u1fbpfcp-watermark.image?)

const enum 是在编译期间把 enum 的引用替换成具体的值，需要解析类型信息，而 babel 并不会解析，所以它会把 const enum 转成 enum 来处理：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04cbe159a3f445cf8ba30c695eaa5585~tplv-k3u1fbpfcp-watermark.image?)

后记：babel 7.15 以后开始支持了，在 @babel/preset-typescript 里加了个 [optimizeCosntEnums 选项](https://babeljs.io/docs/babel-preset-typescript#optimizeconstenums)，原理应该是通过 AST 做了 enum 引用的解析，然后编译时替换引用的值。

### namespace 部分支持：不支持 namespace 的合并，不支持导出非 const 的值

比如这样一段 ts 代码：

```typescript
namespace Guang {
    export const name = 'guang';
}

namespace Guang {
    export const name2 = name;
}

console.log(Guang.name2);
```

按理说 Guang.name2 是 'dong'，因为 ts 会自动合并同名 namespace。

ts 编译之后的代码是[这样的](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/HYQwtgpgzgDiDGEAEBxAriYBzJBvAUAJAQAeMA9gE4AuS85wUtokSAvEgORYbacDc+AL758LaHESpeOAsTJVa9Rs3AQATOyTjBI-MqjkANhAB0R8lgAU6TFlPj1ASkFA)：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a529953f5274e8ba651153145796eab~tplv-k3u1fbpfcp-watermark.image?)

都挂到了 Guang 这个对象上，所以 name2 就能取到 name 的值。

而 babel 对每个 namespace 都是单独处理，所以是[这样的](https://babeljs.io/repl#?browsers=defaults%2C%20not%20ie%2011%2C%20not%20ie_mob%2011&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=HYQwtgpgzgDiDGEAEBxAriYBzJBvAUAJAQAeMA9gE4AuS85wUtokSAvEgORYbacDc-AL758LaHESpeOAsTJVa9Rs3AQATOyTjBI_MqjkANhAB0R8lgAU6TFlPj1ASkFA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Ctypescript&prettier=false&targets=&version=7.17.9&externalPlugins=%40babel%2Fplugin-proposal-private-property-in-object%407.16.7&assumptions=%7B%7D)：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d21775a4e75245a0b1afb314ec79fccf~tplv-k3u1fbpfcp-watermark.image?)

因为不会做 namespace 的合并，所以 name 为 undefined。

还有 namespace 不支持导出非 const 的值。

ts 的 namespace 是可以导出非 const 的值的，后面可以修改：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1662c9dd5a7c4498bb72f3550091c65a~tplv-k3u1fbpfcp-watermark.image?)

但是 babel 并[不支持](https://babeljs.io/repl#?browsers=defaults%2C%20not%20ie%2011%2C%20not%20ie_mob%2011&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=HYQwtgpgzgDiDGEAEBxAriYBzJBvAUAJAQAeMA9gE4AuSANhLaJEgLxIDkWG2HA3PgC--IA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Ctypescript&prettier=false&targets=&version=7.17.9&externalPlugins=%40babel%2Fplugin-proposal-private-property-in-object%407.16.7&assumptions=%7B%7D)：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24d86271f4fd49458647911ff7b8bb67~tplv-k3u1fbpfcp-watermark.image?)

原因也是因为不会做 namespace 的解析，而 namespace 是全局的，如果在另一个文件改了 namespace 导出的值，babel 并不能处理。所以不支持对 namespace 导出的值做修改。

除此以外，还有一些语法也不支持：

### 部分语法不支持

像 export = import = 这种过时的模块语法并[不支持](https://babeljs.io/repl#?browsers=defaults%2C%20not%20ie%2011%2C%20not%20ie_mob%2011&build=&builtIns=false&corejs=3.21&spec=false&loose=false&code_lz=JYWwDg9gTgLgBAcQK4EMB2BzOBeOUCmAjksAQBQBEAdAPQaqYUCUA3AFBtA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&timeTravel=false&sourceType=module&lineWrap=true&presets=env%2Ctypescript&prettier=false&targets=&version=7.17.9&externalPlugins=%40babel%2Fplugin-proposal-private-property-in-object%407.16.7&assumptions=%7B%7D)：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb8884b205d945aba5ac85083acceacf~tplv-k3u1fbpfcp-watermark.image?)

开启了 jsx 编译之后，不能用 \<type> 的方式做类型断言：

我们知道，ts 是可以做类型断言来修改某个类型到某个类型的，[用 as xx 或者 \<xx> 的方式](https://www.typescriptlang.org/play?jsx=0&ts=4.5.0-beta#code/DYUwLgBAHjBcEFcB2BrJB7A7kg3AKD1EgHMEBDJY+AZzACcBLS-PUi4iAXgmhgjOoRajZgTaUuEADzCmxAHy8oOIA)。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ff887c5452d463c811942a36bb00fa2~tplv-k3u1fbpfcp-watermark.image?)

但是如果开启了 jsx 编译之后，\<xx> 的形式会和 jsx 的语法冲突，所以就[不支持 \<xx> 做类型断言了](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/DYUwLgBAHjBcEFcB2BrJB7A7kg3AKD1EgHMEBDJY+AZzACcBLS-PUi4iAXgmhgjOoRajZgTaUuEADzCmxAHy8oOIA)：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b588b3512e8e4fcbbb3844f6522bb3ab~tplv-k3u1fbpfcp-watermark.image?)

tsc 都不支持，babel 当然也是一样：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ddafd3bc5df4a1aa4939f183891bb5e~tplv-k3u1fbpfcp-watermark.image?)

babel 不支持 ts 这些特性，那是否可以用 babel 编译 ts 呢？

## babel 还是 tsc？

babel 不支持 const enum（会作为 enum 处理），不支持 namespace 的跨文件合并，导出非 const 的值，不支持过时的 export = import = 的模块语法。

这些其实影响并不大，只要代码里没用到这些语法，完全可以用 babel 来编译 ts。

babel 编译 ts 代码的优点是可以通过插件支持更多的语言特性，而且生成的代码是按照 targets 的配置按需引入 core-js 的，而 tsc 没做这方面的处理，只能全量引入。

而且 tsc 因为要做类型检查所以是比较慢的，而 babel 不做类型检查，编译会快很多。

那用 babel 编译，就不做类型检查了么？

可以用 tsc --noEmit 来做类型检查，加上 noEmit选项就不会生成代码了。

如果你要生成 d.ts，也要单独跑下 tsc 编译。

## 总结

babel 和 tsc 的编译流程大同小异，都有把源码转换成 AST 的 Parser，都会做语义分析（作用域分析）和 AST 的 transform，最后都会用 Generator（或者 Emitter）把 AST 打印成目标代码并生成 sourcemap。但是 babel 不做类型检查，也不会生成 d.ts 文件。

tsc 支持最新的 es 标准特性和部分草案的特性（比如 decorator），而 babel 通过 @babel/preset-env 支持所有标准特性，也可以通过 @babel/proposal-xx 来支持各种非标准特性，支持的语言特性上 babel 更强一些。

tsc 没有做 polyfill 的处理，需要全量引入 core-js，而 babel 的 @babel/preset-env 会根据 targets 的配置按需引入 core-js，引入方式受 useBuiltIns 影响 (entry 是在入口引入 targets 需要的，usage 是每个模块引入用到的)。

但是 babel 因为是每个文件单独编译的（tsc 是整个项目一起编译），而且也不解析类型，所以 const enum（后来支持了），namespace 合并，namespace 导出非 const 值并不支持。而且过时的 export =  的模块语法也不支持。

但这些影响不大，完全可以用 babel 编译 ts 代码来生成体积更小的代码，不做类型检查编译速度也更快。如果想做类型检查可以单独执行 tsc --noEmit。

当然，文中只是讨论了 tsc 和 babel 编译 ts 代码的区别，并没有说最好用什么，具体用什么编译 ts，大家可以根据场景自己选择。


## 19.原理篇：实现简易 TypeScript 类型检查 

不自己实现 ts 类型检查，怎么能叫“通关”呢？

这一节我们基于 babel 来实现类型检查，也就是 Checker 的功能。
当然，只是简易版本，帮助大家理清类型检查的实现原理。

这节是从 [babel 插件小册](https://juejin.cn/book/6946117847848321055)拿过来的，因为这本不是讲 babel 插件的，所以大家不用看细节，理清下思路就行。

代码在 [github](https://github.com/QuarkGluonPlasma/babel-plugin-exercize)，可以下下来跑一下类型检查部分。

## 如何检查类型

我们知道，babel 能够解析 typescript 语法，那么能不能基于 babel 实现类型检查呢？

我们经常用 tsc 来做类型检查，有没有想过，类型检查具体做了什么？

源码是字符串，是没法直接处理的，我们会先把代码 parse 成 AST，这是计算机能理解的格式。之后的**类型检查就是对 AST 结构的检查**。

比如一个变量声明为了 number，那么给它赋值的是一个 string 就是有类型错误。

再复杂一点，如果类型有泛型，也就是有类型参数，那么需要传入具体的参数来确定类型，确定了类型之后再去和实际的 AST 对比。

typescript 还支持高级类型，也就是类型可以做各种运算，这种就需要传入类型参数求出具体的类型再去和 AST 对比。

我们来写代码实现一下：

## 代码实现

### 实现简单类型的类型检查

#### 赋值语句的类型检查

比如这样一段代码，声明的值是一个 string，但是赋值为了 number，明显是有类型错误的，我们怎么检查出它的错误的。

```javascript
let name: string;

name = 111;
```

首先我们使用 babel 把这段代码 parse 成 AST：

```javascript
const  parser = require('@babel/parser');

const sourceCode = `
    let name: string;

    name = 111;
`;

const ast = parser.parse(sourceCode, {
    plugins: ['typescript']
});
```
使用 babel parser 来 parse，启用 typescript 语法插件。

可以使用 [astexplerer.net](https://astexplorer.net/#/gist/fbe3aa6468083e790076830c48a4725c/9573eca6e0bc15dfdaf341eda5a2afc2906875e6) 来查看它的 AST：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7a3f0df639438cb2aa5a6314bfb701~tplv-k3u1fbpfcp-watermark.image)

##### 实现类型检查

我们需要检查的是这个赋值语句 AssignmentExpression，左右两边的类型是否匹配。

右边是一个数字字面量 NumericLiteral，很容易拿到类型，而左边则是一个引用，要从作用域中拿到它声明的类型，之后才能做类型对比。

babel 提供了 scope 的 api 可以用于查找作用域中的类型声明（binding），并且还可以通过 path.getTypeAnnotation 获得声明时的类型。

```javascript
 AssignmentExpression(path, state) {
    const leftBinding = path.scope.getBinding(path.get('left'));
    const leftType = leftBinding.path.get('id').getTypeAnnotation();// 左边的值声明的类型
}
```

这个返回的类型是 TSTypeAnnotation 的一个对象，我们需要做下处理，转为类型字符串，也就是 string、number 这种。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adaad85b1de341e58d719810894bfc5c~tplv-k3u1fbpfcp-watermark.image)

封装一个方法，传入类型对象，返回 number、string 等类型字符串
```javascript
function resolveType(targetType) {
    const tsTypeAnnotationMap = {
        'TSStringKeyword': 'string'
    }
    switch (targetType.type) {
        case 'TSTypeAnnotation':
            return tsTypeAnnotationMap[targetType.typeAnnotation.type];
        case 'NumberTypeAnnotation': 
            return 'number';
    }
}
```

这样我们拿到了左右两边的类型，接下来就简单了，对比下就知道了类型是否匹配：
```javascript
AssignmentExpression(path, state) {
    const rightType = resolveType(path.get('right').getTypeAnnotation());
    const leftBinding = path.scope.getBinding(path.get('left'));
    const leftType = resolveType(leftBinding.path.get('id').getTypeAnnotation());
    if (leftType !== rightType ) {
        // error: 类型不匹配
    }
}
```
##### 错误打印优化

报错信息怎么打印呢？可以使用 @babel/code-frame，它支持打印某一片段的高亮代码。

```javascript
path.get('right').buildCodeFrameError(`${rightType} can not assign to ${leftType}`, Error)
```
效果如下：

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b7f4107058d4a67ae40b7d1f23aa3ea~tplv-k3u1fbpfcp-watermark.image)

这个错误堆栈也太丑了，我们把它去掉，设置 Error.stackTraceLimit 为 0 就行了

```javascript
Error.stackTraceLimit = 0;
path.get('right').buildCodeFrameError(`${rightType} can not assign to ${leftType}`, Error));
```
但是这里改了之后还要改回来，也就是:

```javascript
const tmp = Error.stackTraceLimit;
Error.stackTraceLimit = 0;
console.log(path.get('right').buildCodeFrameError(`${rightType} can not assign to ${leftType}`, Error));
Error.stackTraceLimit = tmp;
```
再来跑一下：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e3e18ea42dd4f3aae0e13d65756430f~tplv-k3u1fbpfcp-watermark.image)

好看多了！

##### 错误收集

还有一个问题，现在是遇到类型错误就报错，但我们希望是在遇到类型错误时收集起来，最后统一报错。

怎么实现呢？错误放在哪？

babel 插件中可以拿到 file 对象，有 set 和 get 方法用来存取一些全局的信息。可以在插件调用前后，也就是 pre 和 post 阶段拿到 file 对象。

所以我们可以这样做：
```javascript
pre(file) {
    file.set('errors', []);
},
visitor: {
    AssignmentExpression(path, state) {
        const errors = state.file.get('errors');

        const rightType = resolveType(path.get('right').getTypeAnnotation());
        const leftBinding = path.scope.getBinding(path.get('left'));
        const leftType = resolveType(leftBinding.path.get('id').getTypeAnnotation());
        if (leftType !== rightType ) {
            const tmp = Error.stackTraceLimit;
            Error.stackTraceLimit = 0;
            errors.push(path.get('right').buildCodeFrameError(`${rightType} can not assign to ${leftType}`, Error));
            Error.stackTraceLimit = tmp;
        } 
    }
},
post(file) {
    console.log(file.get('errors'));
}
```

这样就可以做到过程中收集错误，最后统一打印：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/917ee6d6f4da4c739d4b7a0ffe742b26~tplv-k3u1fbpfcp-watermark.image)

这样，我们就实现了简单的赋值语句的类型检查！

#### 函数调用的类型检查

赋值语句的检查比较简单，我们来进阶一下，实现函数调用参数的类型检查

```javascript
function add(a: number, b: number): number{
    return a + b;
}
add(1, '2');
```
这里我们要检查的就是函数调用语句 CallExpression 的参数和它声明的是否一致。


![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38286e5076cf4609b0cb66bfa34b66ef~tplv-k3u1fbpfcp-watermark.image)

CallExpression 有 callee 和 arguments 两部分，我们需要根据 callee 从作用域中查找函数声明，然后再把 arguments 的类型和函数声明语句的 params 的类型进行逐一对比，这样就实现了函数调用参数的类型检查。

```javascript
pre(file) {
    file.set('errors', []);
},
visitor: {
    CallExpression(path, state) {
        const errors = state.file.get('errors');
        // 调用参数的类型
        const argumentsTypes = path.get('arguments').map(item => {
            return resolveType(item.getTypeAnnotation());
        });
        const calleeName = path.get('callee').toString();
        // 根据 callee 查找函数声明
        const functionDeclarePath = path.scope.getBinding(calleeName).path;
        // 拿到声明时参数的类型
        const declareParamsTypes = functionDeclarePath.get('params').map(item => {
            return resolveType(item.getTypeAnnotation());
        })

        argumentsTypes.forEach((item, index) => {
            if (item !== declareParamsTypes[index]) {
                // 类型不一致，报错
            }
        });
    }
},
post(file) {
    console.log(file.get('errors'));
}
```
运行一下，效果如下：


![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be28b2a2b76f4587ade7f6caf5d6144c~tplv-k3u1fbpfcp-watermark.image)

我们实现了函数调用参数的类型检查！实际上思路还是挺清晰的，检查别的 AST 也是类似的思路。

### 实现带泛型的类型检查

泛型是什么，其实就是类型参数，使得类型可以根据传入的参数动态确定，类型定义更加灵活。

比如这样一段代码：
```javascript
function add<T>(a: T, b: T) {
    return a + b;
}
add<number>(1, '2');
```
怎么做类型检查呢？

这还是函数调用语句的类型检查，我们上面实现过了，区别不过是多了个参数，那么我们取出类型参数来传过去就行了。

```javascript
CallExpression(path, state) {
    // 先拿到类型参数的值，也就是真实类型
    const realTypes = path.node.typeParameters.params.map(item => {
        return resolveType(item);
    });
    //实参的类型
    const argumentsTypes = path.get('arguments').map(item => {
        return resolveType(item.getTypeAnnotation());
    });
    const calleeName = path.get('callee').toString();
    // 根据函数名查找函数声明
    const functionDeclarePath = path.scope.getBinding(calleeName).path;
    const realTypeMap = {};

  // 把类型参数的值赋值给函数声明语句的泛型参数
   functionDeclarePath.node.typeParameters.params.map((item, index) => {
        realTypeMap[item.name] = realTypes[index];
    });
    const declareParamsTypes = functionDeclarePath.get('params').map(item => {
        return resolveType(item.getTypeAnnotation(), realTypeMap);
    })
    // 做类型检查的时候取具体的类型来对比
    argumentsTypes.forEach((item, index) => { 
        if (item !== declareParamsTypes[index]) {
            // 报错，类型不一致
        }
    });
}
```

多了一步确定泛型参数的具体类型的过程。

执行看下效果：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4126833b7eed45eca7b461179aa4ecfb~tplv-k3u1fbpfcp-watermark.image)

我们成功支持了带泛型的函数调用语句的类型检查！

### 实现带高级类型的函数调用语句的类型检查

typescript 支持高级类型，也就是支持对类型参数做各种运算然后返回最终类型

```javascript
type Res<Param> = Param extends 1 ? number : string;
function add<T>(a: T, b: T) {
    return a + b;
}
add<Res<1>>(1, '2');
```
比如这段代码中，Res 就是一个高级类型，对传入的类型参数 Param 进行处理之后返回新类型。

这个函数调用语句的类型检查，比泛型参数传具体的类型又复杂了一些，需要先求出具体的类型，然后再传入参数，之后再去对比参数的类型。

那么这个 Res 的高级类型怎么求值呢？

我们来看一下这个 Res 类型的 AST：

![image.png](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d715c4b197474eea9847eae1720a6965~tplv-k3u1fbpfcp-watermark.image)

它有类型参数部分（typeParameters），和具体的类型计算逻辑部分（typeAnnotation），右边的 `Param extends 1 ? number : string;` 是一个 condition 语句，有 Params 和 1 分别对应 checkType、extendsType，number 和 string 则分别对应 trueType、falseType。

我们只需要对传入的 Param 判断下是否是 1，就可以求出具体的类型是 trueType 还是 falseType。

具体类型传参的逻辑和上面一样，就不赘述了，我们看一下根据类型参数求值的逻辑：
```javascript
function typeEval(node, params) {
    let checkType;
    // 如果参数是泛型，则从传入的参数取值
    if(node.checkType.type === 'TSTypeReference') {
        checkType = params[node.checkType.typeName.name];
    } else {// 否则直接取字面量参数
        checkType = resolveType(node.checkType); 
    }
    const extendsType = resolveType(node.extendsType);
    if (checkType === extendsType || checkType instanceof extendsType) { // 如果 extends 逻辑成立
        return resolveType(node.trueType);
    } else {
        return resolveType(node.falseType);
    }
}
```
这样，我们就可以求出这个 Res 的高级类型当传入 Params 为 1 时求出的最终类型。

有了最终类型之后，就和直接传入具体类型的函数调用的类型检查一样了。（上面我们实现过）

执行一下，效果如下：

![image.png](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e79c469f2147d7bf9ce40733ec08ba~tplv-k3u1fbpfcp-watermark.image)

完整代码如下（有些长，可以先跳过往后看）：
```javascript
const { declare } = require('@babel/helper-plugin-utils');

// 解析高级类型的值，传入泛型参数的值
function typeEval(node, params) {
    let checkType;
    if(node.checkType.type === 'TSTypeReference') {
        checkType = params[node.checkType.typeName.name];
    } else {
        checkType = resolveType(node.checkType);
    }
    const extendsType = resolveType(node.extendsType);
    // 如果 condition 表达式 的 check 部分为 true，则返回 trueType，否则返回 falseType
    if (checkType === extendsType || checkType instanceof extendsType) {
        return resolveType(node.trueType);
    } else {
        return resolveType(node.falseType);
    }
}

function resolveType(targetType, referenceTypesMap = {}, scope) {
    const tsTypeAnnotationMap = {
        TSStringKeyword: 'string',
        TSNumberKeyword: 'number'
    }
    switch (targetType.type) {
        case 'TSTypeAnnotation':
            if (targetType.typeAnnotation.type === 'TSTypeReference') {
                return referenceTypesMap[targetType.typeAnnotation.typeName.name]
            }
            return tsTypeAnnotationMap[targetType.typeAnnotation.type];
        case 'NumberTypeAnnotation': 
            return 'number';
        case 'StringTypeAnnotation':
            return 'string';
        case 'TSNumberKeyword':
            return 'number';
        case 'TSTypeReference':
            const typeAlias = scope.getData(targetType.typeName.name);
            const paramTypes = targetType.typeParameters.params.map(item => {
                return resolveType(item);
            });
            const params = typeAlias.paramNames.reduce((obj, name, index) => {
                obj[name] = paramTypes[index]; 
                return obj;
            },{});
            return typeEval(typeAlias.body, params);
        case 'TSLiteralType':
            return targetType.literal.value;
    }
}

function noStackTraceWrapper(cb) {
    const tmp = Error.stackTraceLimit;
    Error.stackTraceLimit = 0;
    cb && cb(Error);
    Error.stackTraceLimit = tmp;
}

const noFuncAssignLint = declare((api, options, dirname) => {
    api.assertVersion(7);

    return {
        pre(file) {
            file.set('errors', []);
        },
        visitor: {
            TSTypeAliasDeclaration(path) {
                path.scope.setData(path.get('id').toString(), {
                    paramNames: path.node.typeParameters.params.map(item => {
                        return item.name;
                    }),
                    body: path.getTypeAnnotation()
                });
                path.scope.setData(path.get('params'))
            },
            CallExpression(path, state) {
                const errors = state.file.get('errors');
                // 泛型参数
                const realTypes = path.node.typeParameters.params.map(item => {
                    return resolveType(item, {}, path.scope);
                });
                // 实参类型
                const argumentsTypes = path.get('arguments').map(item => {
                    return resolveType(item.getTypeAnnotation());
                });
                const calleeName = path.get('callee').toString();
                // 根据函数名查找到函数声明
                const functionDeclarePath = path.scope.getBinding(calleeName).path;
                const realTypeMap = {};
                functionDeclarePath.node.typeParameters.params.map((item, index) => {
                    realTypeMap[item.name] = realTypes[index];
                });
                // 把泛型参数传递给具体的泛型
                const declareParamsTypes = functionDeclarePath.get('params').map(item => {
                    return resolveType(item.getTypeAnnotation(), realTypeMap);
                })

                // 声明类型和具体的类型的对比（类型检查）
                argumentsTypes.forEach((item, index) => {
                    if (item !== declareParamsTypes[index]) {
                        noStackTraceWrapper(Error => {
                            errors.push(path.get('arguments.' + index ).buildCodeFrameError(`${item} can not assign to ${declareParamsTypes[index]}`,Error));
                        });
                    }
                });
            }
        },
        post(file) {
            console.log(file.get('errors'));
        }
    }
});

module.exports = noFuncAssignLint;

```
就这样，我们实现了 typescript 高级类型！

## 总结

类型代表了变量的内容和能对它进行的操作，静态类型让检查可以在编译期间做，随着前端项目越来越重，越来越需要  typescript 这类静态类型语言。

类型检查就是做 AST 的对比，判断声明的和实际的是否一致：
- 简单类型就直接对比，相当于 if else
- 带泛型的要先把类型参数传递过去才能确定类型，之后对比，相当于函数调用包裹 if else
- 带高级类型的泛型的类型检查，多了一个对类型求值的过程，相当于多级函数调用之后再判断 if else

实现一个完整的 typescript type cheker 还是很复杂的，不然 typescript checker 部分的代码也不至于好几万行了。但是思路其实没有那么难，按照我们文中的思路来，是可以实现一个完整的 type checker 的。

这一节主要是用到了 path.getTypeAnnotation 的 api 来获取声明的类型，然后进行 AST 的检查，希望能够帮助你理解 type checker 的实现原理。

（当然，文中只是实现了独立的一个个类型的检查，tsc 会递归地做多个文件的全文的类型检查，但是具体的每一部分都是类似的思路。）

（代码在[这里](https://github.com/QuarkGluonPlasma/babel-plugin-exercize)，建议 git clone 下来通过 node 跑一下）



## 2.为什么说 TypeScript 的火爆是必然？

TypeScript 这些年越来越火，可以说是前端工程师的必备技能了，各大框架都基于它实现。

那么，TypeScript 的出现和爆火是偶然发生的吗？其实不是，类似 TypeScript 这种静态类型语言成为主流是必然会发生的。为什么这么说呢？

**让我们先思考一个问题：类型是什么？**

类型具体点来说就是指 number、boolean、string 等基础类型和 Object、Function 等复合类型，它们是编程语言提供的对不同内容的抽象：

- **不同类型变量占据的内存大小不同**：boolean 类型的变量会分配 4 个字节的内存，而 number 类型的变量则会分配 8 个字节的内存，给变量声明了不同的类型就代表了会占据不同的内存空间。

- **不同类型变量可做的操作不同**：number 类型可以做加减乘除等运算，boolean 就不可以，复合类型中不同类型的对象可用的方法不同，比如 Date 和 RegExp，变量的类型不同代表可以对该变量做的操作就不同。

我们知道了什么是类型，那自然可以想到类型和所做的操作要匹配才行，这就是为什么要做类型检查。

**如果能保证对某种类型只做该类型允许的操作，这就叫做`类型安全`**。比如你对 boolean 做加减乘除，这就是类型不安全，你对 Date 对象调用 exec 方法，这就是类型不安全。反之，就是类型安全。

所以，**类型检查是为了保证类型安全的**。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b88c88dad8414ce0aad3f1319299911d~tplv-k3u1fbpfcp-watermark.image?)

类型检查可以在运行时做，也可以运行之前的编译期做。这是两种不同的类型，前者叫做动态类型检查，后者叫做静态类型检查。

两种类型检查各有优缺点。`动态类型检查` 在源码中不保留类型信息，对某个变量赋什么值、做什么操作都是允许的，写代码很灵活。但这也埋下了类型不安全的隐患，比如对 string 做了乘除，对 Date 对象调用了 exec 方法，这些都是运行时才能检查出来的错误。

其中，最常见的错误应该是 “null is not an object”、“undefined is not a function” 之类的了，写代码时没发现类型不匹配，到了运行的时候才发现，就会有很多这种报错。

所以，动态类型虽然代码写起来简单，但代码中很容易藏着一些类型不匹配的隐患。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e18ae92db4f14345b55c9708ee7af373~tplv-k3u1fbpfcp-watermark.image?)

`静态类型检查`则是在源码中保留类型信息，声明变量要指定类型，对变量做的操作要和类型匹配，会有专门的编译器在编译期间做检查。

静态类型给写代码增加了一些难度，因为你除了要考虑代码要表达的逻辑之外，还要考虑类型逻辑：变量是什么类型的、是不是匹配、要不要做类型转换等。

不过，静态类型也消除了类型不安全的隐患，因为在编译期间就做了类型检查，就不会出现对 string 做了乘除，调用了 Date 的 exec 方法这类问题。

所以，静态类型虽然代码写起来要考虑的问题多一些，会复杂一些，但是却消除了代码中潜藏类型不安全问题的可能。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e1e06cf88324aeeadf03a865c7bd973~tplv-k3u1fbpfcp-watermark.image?)

知道了动态类型检查和静态类型检查的区别，我们自然可以得出这样的结论：

**动态类型只适合简单的场景，对于大项目却不太合适，因为代码中可能藏着的隐患太多了，万一线上报一个类型不匹配的错误，那可能就是大问题。**

**而静态类型虽然会增加写代码的成本，但是却能更好的保证代码的健壮性，减少 Bug 率。**

所以，**大型项目注定会用静态类型语言开发。**

JavaScript 本来是为了浏览器的表单验证而设计的，所以就设计成了动态类型的，写代码比较简单。

但 JavaScript 也没想到它后来会被用来开发各种项目，比如 PC 和移动端的网页、React Native 跨端 App、小程序、Electron 桌面端、Node.js 服务端、Node.js 工具链等。

开发各种大型项目的时候，JavaScript 的动态类型语言的缺点就暴露出来了，bug 率太高了，健壮性很难保证。那自然就有了对静态类型的强烈需求，于是 TypeScript 应运而生。

TypeScript 给 JavaScript 添加了一套静态类型系统，从动态类型语言变成了静态类型语言，可以在编译期间做类型检查，提前发现一些类型安全问题。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33b13f9fef884cdc9f598930f40a42f9~tplv-k3u1fbpfcp-watermark.image?)

而且，因为代码中添加了静态类型，也就可以配合编辑器来实现更好的提示、重构等，这是额外的好处。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b306ef3bd374bc285a5189edf9c502b~tplv-k3u1fbpfcp-watermark.image?)

所以，TypeScript 的火爆是一个偶然么？不，我觉得是必然，因为大型项目注定会用静态类型语言来开发。

## 总结

类型决定了变量的内存大小和可以对它进行的操作，保证对什么类型只做什么操作就叫做类型安全，而保证类型安全的方式就是类型检查。

类型检查可以在运行时做，叫做动态类型检查，也可以在编译时做，叫做静态类型检查。

动态类型可能藏在代码里的隐患太多了，bug 率比较高，所以大型项目注定会用静态类型语言来开发。

JavaScript 本身是一门动态类型语言，因为被越来越多的用来开发各种大型项目，所以就有了对静态类型的需求。TypeScript 就满足了这个需求。而且还有额外的更好的提示、更易于重构的好处。

所以，TypeScript 的出现和现在的火爆是必然会发生的。


## 20.原理篇：如何阅读 TypeScript 源码

讲类型编程的时候，分布式条件类型是比较麻烦的一个点：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd0f02d6ea26472c992295c4694d587d~tplv-k3u1fbpfcp-watermark.image?)
![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57e5ca4a9d474a65b49f1f0e5b456d49~tplv-k3u1fbpfcp-watermark.image?)

Test\<T> 这个高级类型，有一个泛型参数 T，当 T 传入的类型为联合类型的时候，有两种情况：

- 如果 checkType（extends 左边的类型） 是 T，则把联合类型拆开后解析类型，最后合并成一个联合类型返回。

- 如果 checkType 不是 T，把联合类型整体作为 T 来解析，返回解析后的类型。

这个语法叫 Distributive Condition Type，分布式条件类型。设计的目的就是为了简化 `Test<number> | Test<boolean>` 的情况。

我们通过这个语法的实现作为抓手，来探究一下 ts 源码应该怎么读。

## 类型的表示法：类型对象

ts 会把源码进行 parse，生成 AST，然后从 AST 中解析出类型信息。

ts 的类型信息是通过类型对象来存储的，我们来看几个例子。（可视化的查看 AST 可以使用 [astexplorer.net](https://astexplorer.net/#/gist/bd6031c7ab25e3d33e8899b3914e9357/f36b635cedba9a6939953631e66868ab322f65d2) 这个网站。）

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f07aa135b0d549b68b7f68267c8f6619~tplv-k3u1fbpfcp-watermark.image?)

上面定义了四个类型：

a 类型是 `LiteralType`，字面量类型，literal 属性保存具体的字面量，这里是 NumericLiteral，数字字面量。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96e5e0c2bf7044f0927d097960d11446~tplv-k3u1fbpfcp-watermark.image?)

b 类型是 `UnionType`，联合类型，types 属性保存了它所包含的类型，这里是两个 LiteralType

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7eb375a7fd694cd190913743693c32bb~tplv-k3u1fbpfcp-watermark.image?)

T extends boolean 这部分是一个 `ConditionType`，有 checkType、extendsType、trueType、falseType 四个属性分别代表不同的部分。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a4884d8e24ed405d95229fce11734b94~tplv-k3u1fbpfcp-watermark.image?)


![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6df3905714d4d119dcd6d8365a01698~tplv-k3u1fbpfcp-watermark.image?)

可以看到，T 是一个 `TypeReference` 类型，也就是它只是一个变量引用，具体的值还是泛型参数传入的类型。

Test<number | boolean> 也是一个 `TypeReference`，类型引用。有 typeName 和 typeArguments 两个属性，typeName 就是它引用的类型 Test，typeArguments 就是泛型参数的值，这里是 UnionType。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30af93f294ba4c689ec4859021d8e7bd~tplv-k3u1fbpfcp-watermark.image?)

所以说，类型在 ts 里面都是通过类型对象来表示的。

比较特别的是 `TypeReference` 类型，它只是一个引用，具体的类型还得把类型参数传入所引用的类型，然后求出最终类型。比如这里的 Test<number | boolean> 的类型，最终的类型是把参数 number | boolean 传入定义的那个 ConditionType 来求出的。这就是 ts 的`高级类型`。

理解了类型是怎么表示的，高级类型和泛型参数都是什么，接下来我们就可以正式通过调试 ts 源码来看下 ConditionType 的解析过程了。

## VSCode 调试 Typescript 源码

首先，我们要把 ts 源码下载下来：

```shell
git clone git@github.com:microsoft/TypeScript.git
```
reset 到我当时看的 commit：
```
git reset --hard df673f74f5cf4fa1948ad2f8c25e6a0290d212ea
```
然后可以看到 lib 目录下有 tsc.js 和 typescript.js，这两个分别是 ts 的命令行和 api 的入口。

但是，这些是编译以后的 js 代码，源码在 src 下，是用 ts 写的。

怎么把编译后的 js 代码和 ts 源码关联起来呢？ sourcemap！

编译源码：

```
yarn 
yarn run build:compiler
```
然后就可以看到多了一个 built 目录，下面有 tsc.js、typescript.js 这两个入口文件，而且也有了 sourcemap：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3ad11e877b3140c79d0fe88f55385370~tplv-k3u1fbpfcp-watermark.image?)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feb4f018d4d842f7b520d3a9fd5df910~tplv-k3u1fbpfcp-watermark.image?)

接下来就可以直接调试 ts 源码，而不是编译后的 js 代码了。

我们来试试：

### vscode 直接调试 ts

vscode 在项目根目录下的 .vscode/launch.json 下保存调试配置：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85719ad045f84fc5a68044de36e9e511~tplv-k3u1fbpfcp-watermark.image?)

我们添加一个调试配置：

```javascript
{
    "name": "调试 ts 源码",
    "program": "${workspaceFolder}/built/local/tsc.js",
    "request": "launch",
    "skipFiles": [
        "<node_internals>/**"
    ],
    "args": [
        "./input.ts"
    ],
    "stopOnEntry": true,
    "type": "node"
}
```
含义如下：
- name： 调试配置的名字
- program：调试的目标程序的地址
- request：有 launch 和 attch 两个取值，代表启动新的还是连上已有的
- skipFiles：调试的时候跳过一些文件，这里配置的是跳过 node 内部的那些文件，调用栈会更简洁
- args：命令行参数
- stopOnEntry：是否在首行加个断点
- type：调试的类型，这里是用 node 来跑

保存之后就可以在调试面板看到该调试选项：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8a495a542db44d8789864267222bac59~tplv-k3u1fbpfcp-watermark.image?)

这里我们设计的 input.ts 是这样的：

```typescript
type Test<T> = T extends boolean ? "Y" : "N";

type res = Test<number | boolean>;
```
在 ts 的 checker.ts 部分打个断点，然后点击启动调试。

然后，看，这断住的地方，就是 ts 源码啊，不是编译后的 js 文件。这就是 sourcemap 的作用。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60806f0242b149bf8ff5a2f70a70e5ab~tplv-k3u1fbpfcp-watermark.image?)

还可以在左边文件树看到源码的目录结构，这比调试编译后的 js 代码爽多了。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6eac2d0c9f6848e49195eccb8b48285e~tplv-k3u1fbpfcp-watermark.image?)

会了通过 sourcemap 调试源码之后，我们该进入主题了： 通过源码探究分布式条件类型的实现原理。

其实我们上面使用的是 tsc.js 的命令行入口来调试的，这样其实代码比较多，很难理清要看哪部分代码。怎么办呢？

接下来就是我的秘密武器了，用 typescript compiler api。

## typescript compiler api

ts 除了命令行工具的入口外，也提供了 api 的形式，只是我们很少用。但它对于探究 ts 源码实现有很大的帮助。

我们定义个 test.js 文件，引入 typescript 的包：

```javascript
const ts = require("./built/local/typescript");
```
然后用 ts 的 api 传入编译配置，并 parse 源码成 ast：
```javascript
const filename = "./input.ts";
const program = ts.createProgram([filename], {
    allowJs: false
});
const sourceFile = program.getSourceFile(filename);
```
这里的 createProgram 第二个参数是编译配置，就是 compilerOptions。

program.getSourceFile 返回的就是 ts 的 AST。

并且还可以拿到 typeChecker：

```javascript
const typeChecker = program.getTypeChecker();
```
然后呢？typeChecker 是类型检查的 api，我们可以遍历 AST 找到检查的 node，然后调用 checker 的 api 进行检查：

```javascript 
function visitNode(node) {
    if (node.kind === ts.SyntaxKind.TypeReference)  {
        const type = typeChecker.getTypeFromTypeNode(node);

        debugger;
    }

    node.forEachChild(child =>
        visitNode(child)
    );
}

visitNode(sourceFile);
```
我们判断了如果 AST 是 TypeReference 类型，则用 typeChecker.getTypeFromTypeNode 来解析类型。

接下来就可以精准的调试该类型解析的逻辑了，相比命令行的方式来说，更方便理清逻辑。

完整代码如下：

```javascript
const ts = require("./built/local/typescript");

const filename = "./input.ts";
const program = ts.createProgram([filename], {
    allowJs: false
});
const sourceFile = program.getSourceFile(filename);
const typeChecker = program.getTypeChecker();

function visitNode(node) {
    if (node.kind === ts.SyntaxKind.TypeReference)  {
        const type = typeChecker.getTypeFromTypeNode(node);

        debugger;
    }

    node.forEachChild(child =>
        visitNode(child)
    );
}

visitNode(sourceFile);
```
我们改下调试配置，然后开始调试：
```javascript
{
    "name": "调试 ts 源码",
    "program": "${workspaceFolder}/test.js",
    "request": "launch",
    "skipFiles": [
        "<node_internals>/**"
    ],
    "args": [
    ],
    "type": "node"
}
```
在 typeChecker.getTypeFromTypeNode 这行打个断点，我们去看下具体的类型解析过程。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8898458264204abfa7b88b33e5fcfb50~tplv-k3u1fbpfcp-watermark.image?)

然后，XDM，打起精神，本文的高潮部分来了：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71c6bb71ee3b4c09b71fc04c2b7b75c4~tplv-k3u1fbpfcp-watermark.image?)

我们进入了 getTypeFromTypeNode 方法，这个方法就是根据 AST 的类型来做不同的解析，返回类型对象的。各种类型解析的逻辑都是从这里进入的，这是一个重要的交通枢纽。

然后我们进入了 TypeReference 的分支，因为 Test<number | boolean> 就是一个类型引用嘛。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd9cac9771d34c018e4ae0ea48b21106~tplv-k3u1fbpfcp-watermark.image?)

TypeReference 的类型就是它引用的类型，它引用了 ConditionType，所以会再解析 T extends boolean 这个 ConditionType 的类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aacf7094ed43474ba2254c6156fa94d7~tplv-k3u1fbpfcp-watermark.image?)

所有的类型都是按照 ast node 的 id 存入一个 nodeLinks 的 map 中来缓存，只有第一次需要解析，之后直接拿结果。比如上图的 resolvedType 就存入了 nodeLinks 来缓存。

然后，XDM，看到闪闪发光的那行代码了么？

解析 ConditionType 的类型的时候会根据 checkType 部分是否是类型参数（TypeParameter，也就是泛型）来设置 isDistributive 属性。

之后解析 TypeReference 类型的时候，会传入具体的类型来实例化：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06be75bbc57f4bd894c7b224ae86fcea~tplv-k3u1fbpfcp-watermark.image?)

这里就判断了 conditionType 的 isDistributive 属性，如果是，则把 unionType 的每个类型分别传入来解析，最后合并返回。

如图，我们走到了 isDistributive 为 true 的这个分支。

那么解析出的类型就是 'Y' | 'N' 的联合类型。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0eece6f1ebdc4a2cb9b7c58961c9a561~tplv-k3u1fbpfcp-watermark.image?)

那我们把 input.ts 代码改一下呢：

```typescript
type Test<T> = [T] extends [boolean] ? "Y" : "N";

type res = Test<number | boolean>;
```
checkType 不直接写类型参数 T 了。

再跑一次：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f894f99ef634c82aa5c7a4eaea6e06a~tplv-k3u1fbpfcp-watermark.image?)

这次没进去了。

难道说？

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea6b3ae5fd344522aeefbedeecc88778~tplv-k3u1fbpfcp-watermark.image?)

确实，这样的结果就是 N。

说明了什么？说明了 `ConditionType 是根据 checkType 是否是类型参数来设置了 isDistributive 属性，之后解析 TypeReference 的时候根据 isDistributive 的值分别做了不同的解析。`

那么只要 checkType 不是 T 就行了。

所以这样也行：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea43120ae9e744009d1da6d9fac7e84a~tplv-k3u1fbpfcp-watermark.image?)

这样也行：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cd6cb1f989d4d2a997f1325ae8e33b7~tplv-k3u1fbpfcp-watermark.image?)

我们经常用 [T] 来避免 distributive 只不过这样比较简洁，看完源码我们知道了，其实别的方式也行。

就这样，我们通过源码理清了这个语法的实现原理。

## 总结

我们以探究 distributive condition type 的实现原理为目的来阅读了 typescript 源码。

首先把 typescript 源码下载下来，执行编译，生成带有 sourcemap 的代码，之后在 vscode 里调试，这样可以直接调试编译前的源码，信息更多。

typescript 有 cli 和 api 两种入口，用 cli 的方式无关代码太多，比较难理清，所以我们用 api 的方式来写了一段测试代码，之后打断点来调试。

ts 的类型信息保存在类型对象中，这个可以用 [astexplorer.net](https://astexplorer.net/#/gist/bd6031c7ab25e3d33e8899b3914e9357/f36b635cedba9a6939953631e66868ab322f65d2) 来可视化的查看。

用 typeChecker.getTypeFromTypeNode 可以拿到某个类型的具体值，我们就是通过这个作为入口来探究各种类型的解析逻辑。

源码中比较重要的有这么几点：
- getTypeFromTypeNode 方法是通过 node 获取类型的入口方法，所有 AST 的类型对象都是通过这个方法拿到
- nodeLinks 保存了解析后的类型，key 为 node id，这样解析一遍就好了，下次拿缓存。

之后我们看了 ConditionType 的解析逻辑会根据 checkType 是否为类型参数来设置 isDistributive 属性，然后 TypeReference 实例化该类型的时候会根据 isDistributive 的值进入不同的处理逻辑，这就是它的实现原理。

理解了原理之后，我们再使用 distributive condition type 就心里有底了，还可以创造很多变形使用，不局限于 [T]。

本文以调试一个类型解析逻辑的原理为抓手探究了 ts 源码阅读方式，调试 ts 别的部分的代码，或者调试其他的库也是类似的。

大家想探究某个类型语法实现原理的时候，可以通过源码层面来彻底搞清楚。


## 21.原理篇：一些特殊情况的说明

学完了各种套路，做了大量练习之后，各种类型编程逻辑我们都能写了。但是依然会遇到一些难以解释的、令人困惑的点。

这一节就来集中讲一下这些令人困惑的地方的原理。

## isEqual 为什么要这样写

前面讲过 isEqual 要这样写：

```typescript
type IsEqual<A, B> = (<T>() => T extends A ? 1 : 2) extends (<T>() => T extends B ? 1 : 2)
    ? true : false;
```
这样才能正确的判断 any：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a4de6faf4d44804a9c36db38cc1a361~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBAkgzgUQI4FcCGAbAPAQQDRQBCAfFALxQAUWAKsZQJTmk1QQAewEAdgCZxQcUAPxQAjFABcUAExMOXPgOp1GzKKwU9+REeKmyGAKCim9wAE4po0gGaY4EANxHXoSLESpMAJQgCKeGR0bEtrAjRuEGInIA)

这是为什么呢？

其实就是源码里的特殊处理。

xx extends yy 这里的判断逻辑在 checkTypeRelatedTo 这个函数里，里面定义了各种类型之间如何判断相关性。

其中就有两个都是条件类型的情况的处理：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3ac283416624fb494f74da5f3f42487~tplv-k3u1fbpfcp-watermark.image?)


如图，source 和 target 都是条件类型（Conditional Type）的时候会走到这里，然后有这样一段注释：

如果是两个条件类型 `T1 extends U1 ? X1 : Y1` 和 `T2 extends U2 ? X2 : Y2` 相关的话，那 T1 和 T2 相关、X1 和 X2 相关、Y1 和 Y2 相关，而 U1 和 U2 相等。

注意，这里 U1 和 U2 是相等的，不是相关。

如果是判断相关性的话，任意类型 extends any 都是 true，但通过构造两个条件类型判断相关性，就可以利用 extends 右边部分相等的性质来判断两个类型是否 equal。

比如 any 和 1，判断相关性的话，肯定是 true，但是判断相等的话，就是 false 了。不过 TS 没有暴露判断相等的方式，只有 extends 这个来判断类型相关性的语法。

这就是为什么我们要这样判断两个类型相等，就是利用了**两个条件类型判断相关性的时候会判断右边部分是否相等**的这个性质，算是一种 hack 的写法。答案要从源码找。

## 为什么我调整了下 extends 左右类型的位置，就报错了

前面我们实现过加法，是这样写的：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a8491e6360541f688b1f72e97bd94bd~tplv-k3u1fbpfcp-watermark.image?)

通过递归构造长度为 Num1 和 Num2 的元组，然后合并成一个新的元组再取长度的方式来实现的。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgrgSwDYBMCCAnDBDEAeAKCmKgBkIA7Ac2AAsoIAPYSlAZygrgFsAjCDABooREgFEk0ALxQ4FANYUA9gHcKw0cUwYGzVhzmLVFANoBdKDPMEAfJajaTAcknU6Ti0xYV2ZSjXpNEmIAfgcsEWDggC5YRFRtXDxyN1phCQhhEwA6XO10yTMbAG4CAlBIBxQUPAA5HgBGXW9fLj4BYXruACZm-U4efgw7GSCc3PhkdCwkroabQVzsyYSZ-C7umzNnVwCPUrKK6DRqgCUINjgkYHsTmoBmbuFugFYSoA)

有的同学发现把 Length 和 Arr['length'] 对调之后就报错了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/06c9b782f0f14dbbbd0483a4df37290c~tplv-k3u1fbpfcp-watermark.image?)

报的错误是无限递归了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5d8a671f50046ff8d572081b9ddd5f2~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgrgSwDYBMCCAnDBDEAeAKCmKgBkIA7Ac2AAsoIAPYSlAZygrgFsAjCDABooREgFEk0ALxQ4FANYUA9gHcKw0cUwYGzVhzmLVFANoBdKDPMEAfJbKUa9Jiwrso2kwHJJ1Ol7NNEmIAfg8sEWDggC5YRFRtXDxyP1phCQhhEwA6XO10yTMbAG4CAlBIDxQUPAA5HgBGXVd3Lj4BYXruACZm-U4efgw7GSCc3PhkdCwkroabQVzsyYSZ-C7umzNvXycA0rKK6DRqgCUINjgkYHsTmoBmbuFugFYSoA)

这是为什么呢，逻辑看起来没啥错误呀？

大家可以先看下这个案例：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98ae749a74f44af8a5252fffd3836a7c~tplv-k3u1fbpfcp-watermark.image?)

声明一个泛型函数，取它的参数类型，结果是 unknown。

有的同学说，这很正常啊，高级类型就像函数调用一样，现在还没调用，没传入参数呢，当然是 unknown。

对，**类型编程中如果需要取类型参数做一些计算的时候，默认推导出的是约束的类型，如果没有类型约束，那就是 unknown**。

上面那个类型把 T 约束为 number，推导出的就是 number：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e96d5f5a49134c159f07deaf94ae3d0d~tplv-k3u1fbpfcp-watermark.image?)

Add 那个类型把约束写死为具体的数字的时候，就会发现不报错了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33fac3e44c984d91a6e076fb20143bae~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgrgSwDYBMCCAnDBDEAeAKCmKgBkIA7Ac2AAsoIAPYSlAZygrgFsAjCDABooREgFEk0ALxQ4FANYUA9gHcKw0cUwYGzVhzmLVFANoBdKDPMEAfJbKUa9Jiwrso2kwHJJ1Ol7NNEmIAfg8sEWDggC5YRFRtXDxyP1phCQhhEwA6XO10yTMbAG4CAlBIDxQUPAA5HgBGXVd3AGYAJmF67nbm-Sh2gFY7GSCc3PhkdCwk7oabQVzsyYSZ-G72mzNvXycA0vLwaDRqgCUINjgkYHsTmo7hIZKCIA)

所以上面 Add 那个类型里取 Num1 和 Num2 传入 BuildArray 做计算的话，其实传入的是 number：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad1b2aad410745c3891f2270aba8fc77~tplv-k3u1fbpfcp-watermark.image?)

number extends 某个具体的数字自然永远不成立，永远是 false，所以就无限递归了。反过来写就不会有这个问题。

## 几个条件类型的特殊情况

有这样几个条件类型，大家先试着猜下 res 都是啥：

第一个：

传入的类型参数为联合类型 1 | 'a'，问 res 是啥

```typescript
type Test<T> = T extends number ? 1 : 2;

type res = Test<1 | 'a'>;
```

第二个：

传入的类型参数为 boolean，问 res 是啥
```typescript
type Test<T> = T extends true ? 1 : 2;

type res = Test<boolean>;
```

第三个：

传入的类型参数为 any，问 res 是啥
```typescript
type Test<T> = T extends true ? 1 : 2;

type res = Test<any>;
```

第四个：

传入的类型参数为 never，问 res 是啥
```typescript
type Test<T> = T extends true ? 1 : 2;

type res = Test<never>;
```

先记一下自己的答案，接下来我公布正确答案，大家看下猜对了几个。

### 答案

第一个类型 res 是 1 | 2 

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2144e41fe7924ac29ead869af0bd54b6~tplv-k3u1fbpfcp-watermark.image?)

再来看第二个类型，res 也是 1 | 2

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2596de989f8446b78769c01afcdc353a~tplv-k3u1fbpfcp-watermark.image?)

接下来是第三个类型，res 也是 1 | 2

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0e6f1afe81ce4b9aa080c37d5cb81ffc~tplv-k3u1fbpfcp-watermark.image?)

最后是第四个类型，res 是 never

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb2a04830f214d53ba32fc10fa1227f1~tplv-k3u1fbpfcp-watermark.image?)

不管答对了几个都没关系，关键是要知道它的原因，接下来我解释下：

### 原因

第一个就是分布式条件类型的特性，联合类型作为类型参数出现在条件类型左边的时候，会把每个类型单独传入做计算，把结果合并成联合类型。这个我们上节还看过源码。

第二个是因为 boolean 也是联合类型，是 true | false，所以也会触发分布式条件类型。这个可以从源码的注释中找到说明，感兴趣也可以调试下源码，判断下 flags。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/335d038cd3ad4d26bdd9cb2a5e97aa7f~tplv-k3u1fbpfcp-watermark.image?)

第三个是条件类型中 any 的特殊处理，如果左边是 any，则会返回 trueType 和 falseType 的联合类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/355bb8793a824d7d8cc318cf2f7f1af2~tplv-k3u1fbpfcp-watermark.image?)

第四个其实严格来说也是分布式条件类型的一种情况，ts 处理分布式条件类型的时候对 Union 和 Never 都做了特殊处理：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18abc14766794756a9071087ef9f4ffc~tplv-k3u1fbpfcp-watermark.image?)

但是后面走的分支不一样：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54e58d8f289d4a0c9c04e5d6ee7db605~tplv-k3u1fbpfcp-watermark.image?)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3806548354f04da3a499dfb5fc7e9d49~tplv-k3u1fbpfcp-watermark.image?)

可以看到，如果是 never，那就直接返回了。

所以当条件类型左边是 never 的时候，就会直接返回 never。

严格来说分布式条件类型是包含 Union 和 Never 两种情况的，只不过 never 的情况比较特殊，可以单独摘出来讲，平时我们谈到分布式条件类型（distributive conditional type）就是指联合类型 Union 的情况。

## 总结

这一节我们集中讲了一些 ts 里令人困惑的点：

- 判断相等是根据“两个条件类型如果相关，那么 extendsType 部分是相等的”这个特性。

- 类型参数默认推导出的是类型约束的类型。

- 条件类型中，联合类型、any、never、boolean 都比较特殊：
    - 联合类型有分布式条件类型的特性，会分发传入
    - boolean 也是联合类型
    - any 会直接返回 trueType 和 falseType 的联合类型
    - never 会直接返回 never，严格来说这个也是分布式条件类型的一种情况
    
这节从源码角度理清了一些情况的原理，如果大家还有一些困惑的点的话可以告诉我，我再补充进来。





## 22.小册总结

TypeScript 是 JavaScript 的超集，它给 JS 添加了一套静态类型系统。

TS 的入门就是学怎么给 JS 添加类型，比如函数、class、构造器、对象等怎么加类型，这些其实文档写的很清楚了，网上也有很多相关资料。

TS 的进阶部分就是类型编程，也就是如何动态生成一些类型，这部分是 TS 最强大也是最复杂的部分，被戏称为“类型体操”，但是网上没有专门系统讲这部分的。所以我才写了这本小册，希望能把类型编程讲清楚，同时也讲下 TS 类型检查的实现原理以及怎么阅读 TS 源码。

首先我们明确了什么是类型安全，TypeScript 添加的静态类型系统就是为了保证类型安全的，把一些类型不兼容的错误提前到编译期间检查出来，提高代码的健壮性，这就是为什么大型项目必然会用静态类型的语言来写。

大家可能有写过 java 代码，会发现它的那套类型系统好像没有 TS 的这么复杂，所以我们又理了下类型系统的三个层次，支持泛型并且支持类型编程的类型系统是最复杂的，TS 的类型系统就是这样。

之后我们过了遍 TS 类型系统中的类型和支持的类型计算，其实大部分类型是和 JS 中的保持一致的，只不过扩展了 interface、enum、元组等复合类型，和 never、any、void 等特殊类型。

这些基础是告诉我们怎么声明类型的，而类型编程则是动态生成类型，对类型做增删改，比直接声明类型更高一层。

后面我们分别讲学了**模式匹配**（各种类型通过 infer 提取某部分类型）、**重新构造**（类型是不可变的，想修改只能重新构造一个新的。最主要的是通过映射类型来生成新的索引类型）、**递归**（类型编程里涉及到数量不确定的问题，要条件反射的想到用递归来解决）、**数组长度计数**（严格来说是元组长度，通过构造不同元素个数的元组再取长度的方式实现计数）、**联合类型的分发特性**（分布式条件类型，当联合类型作为类型参数出现在条件类型左边的时候触发），以及**一些特殊的类型逻辑**的讲解。

学完这些套路之后，各种类型编程逻辑我们都能写。

而且，TS 也内置了不少高级类型，我们也都过了一遍。

并且我们还通过几个例子感受了下类型编程的意义：**可以对已有类型做修改，可以动态生成一些类型，可以做更精准的类型检查和提示**。

之后进行了一些综合的实战，综合运用上面的套路和内置的高级类型来实现了一些复杂的类型编程逻辑。

原理篇我们学习了 TS 里比较难理解的逆变、协变、双向协变、不变等概念，型变给类型系统增加了一些灵活性，这些理论知识还是要知道的。

然后我们对比了下 babel 和 tsc 编译 ts 代码的区别：babel 不会做类型检查，但是在代码产物上更有优势，可以根据 targets 指定的环境来按需编译并且引入 polyfill。而 tsc 只能指定语言版本的 target，不会做 polyfill，代码产物会更大一些，但是类型检查必须依赖它。

两者结合的方式就是用 babel（或者 swc、esbuild 等同类编译器）来编译 ts 代码，然后用 tsc --noEmit 执行类型检查。

之后我们基于 babel 插件实现了简易的 ts 类型检查，大家不用写出来，但是可以跑下代码感受下类型检查的实现原理。

之后我们通过分布式条件类型为切入点读了 TypeScript 源码，当大家对某个类型的实现有困惑的时候，可以试着从源码找找答案。

然后对于 isEqual 等类型编程中一些比较令人困惑的点集中做了说明。

类型编程的案例还是有很多的，但是都逃不开小册里的那几个套路，这就像你会了 JS 的 if else、function、for、while 就能写各种逻辑一样，把这些基础的套路掌握好了，各种类型编程逻辑都是能写的，万变不离其宗。

希望这本小册能帮助大家掌握类型编程，成为类型体操高手。



## 23.加餐：3 种类型来源和 3 种模块语法

TypeScript 给 JavaScript 添加了一套类型语法，我们声明变量的时候可以给变量加上类型信息，这样编译阶段就可以检查出变量使用的对不对，也就是类型检查。

给变量添加类型，很自然可以想到时在声明的时候指定：

比如对象：

```typescript
interface Person {
    name: string;
    age?: number;
}

const guang: Person = {
    name: 'guang'
}
```

比如函数：

```typescript
function add(num1: number, num2: number): number {
    return num1 + num2;
}
```

这样当使用它们的时候，比如变量赋值、函数调用，就可以通过类型信息检查出使用的对不对：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18c1067053754da1b23abbde5b8e8110~tplv-k3u1fbpfcp-watermark.image?)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d203439ac79c4c0d83c3ea1d9b3c675f~tplv-k3u1fbpfcp-watermark.image?)

TypeScript 这样设计类型语法没啥问题，但是只是这样还不够。

我们自己写的代码可以这样声明类型，但不是我们写的呢？

比如 JS 引擎提供的 Number、String、Date、RegExp，浏览器环境的 HTMLElement、Event 等 api。

这些 api 是执行引擎内置的实现，但我们代码里会用到它们，也同样需要检查使用的对不对，也就是类型检查。怎么给这些 api 加上类型呢？

## TypeScript 类型声明的三种来源

TypeScript 设计了 declare 的语法，可以单独声明变量的类型：

比如对象：
```typescript
interface Person {
    name: string;
    age?: number;
}

declare const guang: Person;
```
比如函数：
```typescript
declare function add(num1: number, num2: number): number;
```

这样单独声明了类型，使用这些 api 的时候也就能做类型检查。

像 JS 引擎那些 api，还有浏览器提供的 api，这些基本是必用的，而且都有标准的。所以 TypeScript 给内置了它们的类型声明。

TypeScript 包下有个 lib 目录，里面有一堆 lib.xx.d.ts 的类型声明文件，这就是 TS 内置的一些类型声明。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c67a7818d32249269ac8ebdd96787a76~tplv-k3u1fbpfcp-watermark.image?)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/452c218beebe495f9e23e37efb89dd94~tplv-k3u1fbpfcp-watermark.image?)

因为这些只是声明类型，而没有具体的 JS 实现，TS 就给单独设计了一种文件类型，也就是 d.ts， d 是 declare 的意思。

比如 lib.dom.d.ts 里的类型声明：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35ddc8f8c22b4074992857e99789c903~tplv-k3u1fbpfcp-watermark.image?)

因为是 ts 内置的，所以配置一下就可以用了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2a586d8004049e194a110cd23982a6f~tplv-k3u1fbpfcp-watermark.image?)

tsconfig.json 里配置下 compilerOptions.lib，就可以引入对应的 d.ts 的类型声明文件。

有的同学可能会说，可是内置的类型声明也不多呀，只有 dom 和 es 的。

确实，因为 JS 的 api 还有浏览器的 api 都是有标准的，那自然可以按照标准来定义类型。其余的环境的 api 可能没有标准，经常变，那自然就没法内置了，比如 node。所以 lib 里只有 dom 和 es 的类型声明。

那 node 环境，还有其他环境里的内置 api 怎么配置类型声明呢？

node 等环境的 api 因为没有标准而没有被 TS 内置，但 TS 同样也支持了这些环境的类型声明的配置。

方式是通过 @types/xxx 的包：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9778d228e72843b1b6567e49fb9accd6~tplv-k3u1fbpfcp-watermark.image?)

TS 会先加载内置的 lib 的类型声明，然后再去查找 @types 包下的类型声明。

这样，其他环境的类型声明就可以通过这种方式来扩展。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/74b45cde7be94785948429a71e1ebb77~tplv-k3u1fbpfcp-watermark.image?)

@types 包是在 [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped/blob/master/README.zh.md) 这个项目下统一管理的，想创建一个 @types 包的话要去看一下他们的文档。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aab5ef6002c54213bce055f463720b68~tplv-k3u1fbpfcp-watermark.image?)

一般来说，很快就可以发到 npm 的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cc4766a3ffc43d5a4ea465edec456db~tplv-k3u1fbpfcp-watermark.image?)

我们知道，TS 内置的那些 lib 是可以配置的，扩展的这些 @types/xx 的包自然也可以配置：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89863c6e73fb4c9c9fa532239f0062de~tplv-k3u1fbpfcp-watermark.image?)

可以指定加载 @types 目录下的哪些包，还可以修改查找 @types 包的目录（默认是 node_modules/@types)：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97cd492ca69249c8b886cbcc39c22390~tplv-k3u1fbpfcp-watermark.image?)

除了给 node 等环境的 api 加上类型声明外，@types 包还有一种用途，就是给一些 JS 的包加上类型声明：

如果代码本身是用 ts 写的，那编译的时候就可以开启 compilerOptions.declaration，来生成 d.ts 文件：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8712a57078514d8cb97cd0cccc235fc2~tplv-k3u1fbpfcp-watermark.image?)

然后在 package.json 里配置 types 来指定 dts 的位置：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c4f190636de46359b3440b3be7fc1f9~tplv-k3u1fbpfcp-watermark.image?)

这样就不需要单独的 @types 包了。

但如果代码不是用 ts 写的，那可能既需要单独写一个 @types/xxx 的包来声明 ts 类型，然后在 tsconfig.json 里配置下，加载进来。

比如常用的 vue3 就不需要 @types/vue 包，因为本身是用 ts 写的，npm 包里也包含了 dts 文件。

但是 react 不是 ts 写的，是用的 facebook 自己的 flow，自然就需要 @types/react 的包来加上 ts 类型声明。

至此，ts 内置的 dom 和 es 的类型声明，其他环境还有一些包的类型声明我们都知道怎么加载了。

那自己写的 ts 代码呢？

这些其实我们经常配置，就是配置下编译的入口文件，通过 includes 指定一堆，然后通过 excludes 去掉一部分。还可以通过 files 再单独包含一些：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f280facf1dcc4ec08b4f739b4b9c0ba4~tplv-k3u1fbpfcp-watermark.image?)

tsc 在编译的时候，会分别加载 lib 的，@types 下的，还有 include 和 files 的文件，进行类型检查。

这就是 ts 类型声明的三种来源。

现在还有一个问题，有的 api 是全局的，有的 api 是某个模块的，ts 是怎么声明全局 api 的类型，怎么声明模块内的 api 的类型呢？

## 全局类型声明 vs 模块类型声明

我们写的 JS 代码就是有的 api 是全局的，有的 api 是模块内的，所以 TS 需要支持这个也很正常。

但 JS 的模块规范不是一开始就有的，最开始是通过在全局挂一个对象，然后这个对象上再挂一些 api 的方式，也就是命名空间 namespace。

所以 TS 最早支持的模块化方案自然也就是 namespace：

```typescript
namespace Guang {
    export interface Person {
        name: string;
        age?: number;
    }

    const name = 'guang';
    const age = 20;

    export const guang: Person = {
        name,
        age
    }
    export function add(a: number, b: number):number {
        return a + b;
    }
}
```

理解 namespace 的话可以看一下编译后的代码：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c094481781546508551a06dfd9bc80b~tplv-k3u1fbpfcp-watermark.image?)

就是全局上放一个对象，然后对象上再挂几个暴露出去的属性。

看了编译后的代码，是不是 namespace 瞬间就学会了～

后来，出现了 CommonJS 的规范，那种不能叫 namespace 了，所以 TS 支持了 module，

很容易想到，@types/node 的 api 定义就是一堆的 module：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dbb6767321e64d25985384af5568cd65~tplv-k3u1fbpfcp-watermark.image?)

这个 module 和 namespace 有什么区别呢？

其实真没什么区别，只不过 module 后一般接一个路径，而 namespace 后一般是一个命名空间名字。其他的语法都一样的。

而且这个结论是有依据的：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dec4bdeacf6a4a17a1f7adfbe16a9ac9~tplv-k3u1fbpfcp-watermark.image?)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c77268d47ca41e2a042734bcab2b424~tplv-k3u1fbpfcp-watermark.image?)

用 [astexplorer.net](https://astexplorer.net) 看一下 parse 后的 AST，两者的 AST类型都是一样的。也就是说编译器后续的处理都一样，那不是一种东西是什么。

再后来的故事大家都知道了，JS 有了 es module 规范，所以现在推荐直接用 import export 的方式来声明模块和导入导出了。

额外多了的，只不过有一个 import type 的语法，可以单独引入类型：

```typescript
import type {xxx} from 'yyy';
```

所以现在声明模块不咋推荐用 namespace 和 module，还是尽量用 es module 吧。

那全局的类型声明呢？

有了 es module 之后，TS 有了一个单独的设计：

**dts 中，如果没有 import、export 语法，那所有的类型声明都是全局的，否则是模块内的。**

我们试验一下：

include 配置 src 下的 ts 文件，然后再用 files 引入 global.d.ts 文件：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14f5c8b9fb9b41239a23e97b5d4dd295~tplv-k3u1fbpfcp-watermark.image?)

在 global.d.ts 里声明一个 func 函数：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6adbf7d853043c99e9742135e50d2b3~tplv-k3u1fbpfcp-watermark.image?)

在 src/index.ts 里是有提示的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2442225f75b14fc3bcf46ff3e0863926~tplv-k3u1fbpfcp-watermark.image?)

编译也不报错：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66aefdb9f62a46d6b1e10dc94723c970~tplv-k3u1fbpfcp-watermark.image?)

加上一个 import 语句：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fbc08a3c490f4f03846d7777b9e417bb~tplv-k3u1fbpfcp-watermark.image?)

编译就报错了，说是找不到 func：
![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16f35249ce194944bc4c1e6cb37845b2~tplv-k3u1fbpfcp-watermark.image?)

这说明 func 就不再是全局的类型了。

这时候可以手动 declare global：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2d36f271f364478a430e83866f0fb32~tplv-k3u1fbpfcp-watermark.image?)

再试一下，编译就通过了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92dc60483aec429abc80f167ac2928fc~tplv-k3u1fbpfcp-watermark.image?)

而且不止是 es module 的模块里可以用 global 声明全局类型，module 的方式声明的 CommonJS 模块也是可以的：

比如 @types/node 里就有不少这种全局类型声明：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21dd101b6d414b5180594083372d91b2~tplv-k3u1fbpfcp-watermark.image?)

这就是 3 种 typescript 声明模块的语法，以及声明全局类型的方式。

那么如果就是需要引入模块，但是也需要全局声明类型，有什么更好的方式呢？

有，通过编译器指令 reference。这样既可以引入类型声明，又不会导致所有类型声明都变为模块内的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/608e41bb549f4e7caf4f873761c6be9e~tplv-k3u1fbpfcp-watermark.image?)

可以看到很多 dts 都这样引入别的 dts 的，就是为了保证引入的类型声明依然是全局的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e331aef1d8412a828776db010e49e5~tplv-k3u1fbpfcp-watermark.image?)

## 总结

TypeScript 给 JavaScript 添加了类型信息，在编译时做类型检查。

除了在变量声明时定义类型外，TS 也支持通过 declare 单独声明类型。只存放类型声明的文件后缀是 d.ts。

TypeScript 有三种存放类型声明的地方：

- lib： 内置的类型声明，包含 dom 和 es 的，因为这俩都是有标准的。
- @types/xx： 其他环境的 api 类型声明，比如 node，还有 npm 包的类型声明
- 开发者写的代码：通过 include + exclude 还有 files 指定

其中，npm 包也可以同时存放 ts 类型，通过 packages.json 的 types 字段指定路径即可。

常见的是 vue 的类型是存放在 npm 包下的，而 react 的类型是在 @types/react 里的。因为源码一个是 ts 写的，一个不是。

巧合的是，TS 声明模块的方式也是三种：

- namespace：最早的实现模块的方式，编译为声明对象和设置对象的属性的 JS 代码，很容易理解
- module：和 namespace 的 AST 没有任何区别，只不过一般用来声明 CommonJS 的模块，在 @types/node 下有很多
- es module：es 标准的模块语法，ts 额外扩展了 import type

dts 的类型声明默认是全局的，除非有 es module 的 import、export 的声明，这时候就要手动 declare global 了。为了避免这种情况，可以用 reference 的编译器指令。

**学习类型定义是怎么给 JS 加上类型，学习类型编程是怎么动态生成类型和对类型做修改，这些类型可能会通过模块或全局的方式来组织，所以还需要学习模块语法，而且可能会放在 lib、@types/xxx、用户目录等位置，还要学习不同来源的类型的查找机制。**

深入掌握 TypeScript 的话，除了学习类型定义以及类型编程，这三种类型声明的来源（lib、@types、用户目录），以及三种模块声明的方式（namespace、module、es module），还有全局类型的声明（global、reference），也都是要掌握的。




## 24.加餐：用 Project Reference 优化 tsc 编译性能

TypeScript 给 JavaScript 添加了一套类型系统，可以在编译期间检查出类型错误，这增加了代码的健壮性，但也多了一个编译的过程。

ts 编译速度与项目规模有关，如果项目比较大，代码很多，那就需要编译很长一段时间。

有没有什么办法可以提升 tsc 编译的性能呢？

还真有，TypeScript 3.0 的时候实现了 Project Reference 的特性，就是用于优化编译和类型检查的性能的。

那 Project Reference 是干什么的呢？

## Project Reference

想象这样一个场景。项目目录下有两个相对独立的模块 aaa 和 bbb

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a90d06fb5a641d7a2a0481f975cc83d~tplv-k3u1fbpfcp-watermark.image?)

它们是用同一个 tsconfig.json 来配置编译方式的：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be04f9b11a4a4a52bbc7c89004edeeb0~tplv-k3u1fbpfcp-watermark.image?)

执行 tsc 就会编译所有 include 的文件到 dist 目录下：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ce9456a73ba4f7cac98fcebbf70e8f3~tplv-k3u1fbpfcp-watermark.image?)

假设 aaa 和 bbb 都很大，编译要很久，但是两者的关联还不是特别大。

aaa 模块下的变动基本和 bbb 模块下的没啥关系，但是 aaa 变了，bbb 也要重新编译一遍，bbb 变了 aaa 也要重新编译一遍，这就很没必要。

有的同学说，那在 aaa 和 bbb 下分别放一个 tsconfig.json，各自编译各自的不就行了？

这样是可以，但是这样就是多次编译了，比较麻烦。

能不能还是一次编译，但是对一些相对独立的模块做下缓存，不要跟随别的模块一起编译呢？

可以的，这就是 Project Reference 做的事情了。

在 aaa 和 bbb 下各自创建一个 tsconfig.json，放各自的编译配置。注意这里要加一个 composite: true，这是 Project Reference 需要的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a83c2a0a008f48ef9b2e6022064dda39~tplv-k3u1fbpfcp-watermark.image?)

然后在根目录的 tsconfig.json 里加上一个 references 的配置，引入 aaa 和 bbb：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7017701481304362b5f8584eafa2e1cf~tplv-k3u1fbpfcp-watermark.image?)

这样再执行 tsc --build 进行编译，你会发现编译结果多了 .d.ts 的声明，还多了 tsconfig.tsbuildinfo 的文件：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79f23865950346f7aa54ef55f120766c~tplv-k3u1fbpfcp-watermark.image?)

打开 tsconfig.tsbuildinfo 看一下，会发现它记录了编译了哪些文件，还记录了这些文件的 hash 值：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/98aa0f60eeb847aeba3936582cbf0779~tplv-k3u1fbpfcp-watermark.image?)

看到这里，你是不是就知道为啥它能实现缓存了？

没错，就是对比文件的 hash，当编译到这个 project 的时候，会对比下 hash 有没有变化，变了才去编译。没变的就直接跳过了。

而且，别的地方可能用到这个 project 的类型，所以需要生成 d.ts 声明文件，这就是为啥我们没有指定 declaration: true 的配置，但是编译产物里还是有 d.ts。其实这是 composite 选项做的，它设置了 Project Reference 需要的一些编译选项：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f71cfb8cff845e0becd0b04b644ef64~tplv-k3u1fbpfcp-watermark.image?)

现在当你修改了 aaa 下某个模块的代码，重新编译的时候就不会编译 bbb 了，只会编译 aaa 下的那个模块。

这就是 Project Reference 的作用。

当然，这种编译模式和常规的编译模式不同，所以不是直接用 tsc 来编译，而是用 tsc --build 或者 tsc -b。

此外，Project Reference 还支持通过 prepend 指定编译顺序，比如给 bbb 添加 prepend: true，那么就会先编译 bbb，再编译当前项目，然后编译 aaa：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e5e4dfe33104500a184ff80998446cd~tplv-k3u1fbpfcp-watermark.image?)

其实很容易想到，monorepo 里就可以用 Project Reference 来提升 tsc 的编译性能。因为 monorepo 下的多个 project 相互之间都比较独立，一个模块的改动一般不会影响另一个模块，所以编译的时候也应该各自做缓存。

举个真实项目的例子吧：

nest 之前是 gulp + tsc 的方式来编译的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe5d8ef2cde943ae8f02c4ca373c3342~tplv-k3u1fbpfcp-watermark.image?)

之后为了优化编译性能，换成 tsc 的 project reference 的方式了：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/daf2a849455b451aa849264be0c61d66~tplv-k3u1fbpfcp-watermark.image?)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a268b0c2589462488897ec6923a5f47~tplv-k3u1fbpfcp-watermark.image?)

## 总结

TypeScript 3.0 时实现了 Project Reference 来优化性能。

如果项目下有一些相对独立的模块，别的模块的变动不影响它，但是它却要跟着重新编译一次，这时就可以用 Project Reference 来优化了。

在独立的模块下添加 tsconfig.json，加上 composite 的编译选项，在入口的 tsconfig.json 里配置 references 引用这些独立的模块。然后执行 tsc --build 或者 tsc -b 来编译。

这时候就实现了编译和类型检查的性能优化。

原理是编译时会生成 tsconfig.tsbuildinfo 的文件，记录着编译的文件和它们的 hash，当再次编译的时候，如果文件 hash 没变，那就直接跳过，从而提升了编译速度。

这是 TypeScript 提供的编译性能优化机制，当项目比较大，tsc 执行的速度比较慢的时候，不妨尝试一下。

## 25.加餐：一道 3 层的 ts 面试题

最近遇见一道不错的 TS 面试题，分享一下。

这道题有 3 个层次，我们一层层来看。

第一层的要求是这样的：

**实现一个 zip 函数，对两个数组的元素按顺序两两合并，比如输入 [1,2,3], [4,5,6] 时，返回 [[1,4], [2,5],[3,6]]**

这层就是每次各从两个数组取一个元素，合并之后放到数组里，然后继续处理下一个，递归进行这个流程，直到数组为空即可。

```javascript
function zip(target, source) {
  if (!target.length || !source.length) return [];

  const [one, ...rest1] = target;
  const [other, ...rest2] = source;

  return [[one, other], ...zip(rest1, rest2)];
}
```

结果是对的：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9fe22402c8b74f4c92526bf6096746c3~tplv-k3u1fbpfcp-watermark.image?)

第一层还是比较简单的，然后我们来看第二层要求：

**给这个 zip 函数定义 ts 类型（两种写法）**

函数的定义有两种形式：

直接通过 function 声明函数：
```javascript
function func() {}
```

和声明匿名函数然后赋值给变量：

```javascript
const func = () => {}
```

而参数和返回值的类型都是数组，只是具体类型不知道，可以写 unknown[]。

所以两种函数类型的定义就是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8af513936c74470adf20945b2608bff~tplv-k3u1fbpfcp-watermark.image?)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7c7ac25f0ec4f0c969c70db558f2eed~tplv-k3u1fbpfcp-watermark.image?)

也是直接 function 声明函数类型和 interface 声明函数类型然后加到变量类型上两种。

因为具体元素类型不知道，所以用 unknown。

这里可能会问 any 和 unknown 的区别：

any 和 unknown 都可以接收任何类型：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42ee8313565841f4a1f1a44f3e87724d~tplv-k3u1fbpfcp-watermark.image?)

但是 any 也可以赋值给任何类型，但 unknown 不行。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33ec41d7068a42559ce4f3746f1f1420~tplv-k3u1fbpfcp-watermark.image?)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88d86a61c4de4c10b633dfff9d4b9d8e~tplv-k3u1fbpfcp-watermark.image?)

这里只是用来接收其他类型， 所以 unknown 比any 更合适一些，更安全。

这一层也是比较基础的 ts 语法，第三层就上了难度了：

**用类型编程实现精确的类型提示，比如参数传入 [1,2,3], [4,5,6]，那返回值的类型要提示出 [[1,4], [2,5],[3,6]]**

这里要求返回值类型是精确的，我们就要根据参数的类型来动态生成返回值类型。

也就是这样：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca16308fffd24d2ab93d201807594a6a~tplv-k3u1fbpfcp-watermark.image?)

声明两个类型参数 Target、Source，约束为 unknown[]，也就是元素类型任意的数组类型。

这俩类型参数分别是传入的两个参数的类型。

返回值通过 Zip 计算得出。

然后要实现 Zip 的高级类型：

传入的类型参数分别是两个数组类型，我们同样要从中提取出每个元素合并到一起。

提取元素可以用模式匹配的方式：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e924383bcb5f4d1bb5d8aadb40ca6925~tplv-k3u1fbpfcp-watermark.image?)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bc144970bb24465afa100bb62897b42~tplv-k3u1fbpfcp-watermark.image?)

所以这个类型就可以这样定义：

```typescript
type Zip<One extends unknown[], Other extends unknown[]> =
    One extends [infer OneFirst,...infer Rest1]
      ? Other extends [infer OtherFirst, ...infer Rest2]
        ? [[OneFirst, OtherFirst], ...Zip<Rest1, Rest2>]
        : []
      : [];
```
分别提取两个数组的第一个元素，构造成新数组。然后对剩下的数组递归进行这样的处理，直到数组为空。

这样就实现了我们想要的高级类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02042c7cf3c94d0cbdf7a00616687231~tplv-k3u1fbpfcp-watermark.image?)

但你把它作为返回值加到函数上会报错：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf4d7ba9f6c143db95f5a3fa324022e8~tplv-k3u1fbpfcp-watermark.image?)

因为声明函数的时候都不知道参数是啥，自然计算不出 Zip<Target, Source> 的值，所以这里会类型不匹配：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa43eefc8e264a818ad995678ddf0495~tplv-k3u1fbpfcp-watermark.image?)

那怎么办呢？

可以用函数重载解决：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8d58160fc26d498d9e209a312dd55e52~tplv-k3u1fbpfcp-watermark.image?)

ts 支持函数重载，可以写多个同名函数的类型的类型定义，最后写函数的实现，这样用到这个函数的时候会根据参数的类型来匹配函数类型。

我们用了类型编程的那个函数通过这种方式写就不会报错了。

我们使用下看看：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e59c589b6d51472aad9212df40bf06fd~tplv-k3u1fbpfcp-watermark.image?)

咋返回值的类型不对呢？

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4266a93fd9af4be5b6330fa7f95296a7~tplv-k3u1fbpfcp-watermark.image?)

其实这时候匹配的函数类型是对的，只不过推导出的不是字面量类型。

这时候可以加个 as const。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f8588cdcde64c1b97b4304210cfbd9b~tplv-k3u1fbpfcp-watermark.image?)

但是加上 as const 会推导出 readonly [1,2,3]

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd50614058c448f380cd8f3758ae5740~tplv-k3u1fbpfcp-watermark.image?)

这样类型就不匹配了，所以要在类型参数的声明上也加上 readonly:

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14d63087a00a43c5bf62937718c657c6~tplv-k3u1fbpfcp-watermark.image?)

但这样 Zip 函数的类型又不匹配了。

难道要把所有用到这个类型的地方都加上 readonly 么？

不用，我们 readonly 的修饰去掉不就行了？

Typescript 有内置的高级类型 readonly：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5817c2792b54fbca35f3e30ddc1dcb9~tplv-k3u1fbpfcp-watermark.image?)

可以把索引类型的每个索引都加上 readonly 修饰：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e15ea9a8e3f47559df54d123ea05d8a~tplv-k3u1fbpfcp-watermark.image?)

但没有提供去掉 readonly 修饰的高级类型，我们可以自己实现一下：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f2c283be97f404eac13fa7874fc41fb~tplv-k3u1fbpfcp-watermark.image?)

用映射类型的语法构造个新索引类型，加上个 -readonly 就是去掉 readonly 修饰的意思。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c31e9a53ec944b38a0d47bb44c779eb~tplv-k3u1fbpfcp-watermark.image?)

有的同学可能问了，数组类型也是索引类型么？

是，索引类型是聚合多个元素的类型，所以对象、数组、class 都是。

所以我们把它用在数组上自然也是可以的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cfe98ddda7a648919df64cd4b5f52a3e~tplv-k3u1fbpfcp-watermark.image?)

（准确来说叫元组，元组是元素个数固定的数组）

那我们只要在传入 Zip 之前，用 Mutable 去掉 readonly 就可以了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7d8e720ba61432d9235532593d79a11~tplv-k3u1fbpfcp-watermark.image?)

再来试一下：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ed1ca13d54f4b019c287d96a0666ef1~tplv-k3u1fbpfcp-watermark.image?)

大功告成！现在返回值的类型就对了。

但还有个问题，如果不是直接传入字面量，是推导不出字面量类型的，这时候貌似就不对了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61f55554d25c45bbb6f93f2f3bf933f6~tplv-k3u1fbpfcp-watermark.image?)

可我们不都声明重载类型了么？

如果推导不出字面量类型，应该匹配这个呀：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0fcef5c14ecf4ae2bb9b2357d99f687c~tplv-k3u1fbpfcp-watermark.image?)

但实际上它匹配的还是第一个：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/418948649bfe49e9ad6f939d8bf8b77a~tplv-k3u1fbpfcp-watermark.image?)

这时候其实只要调换下两个函数类型的顺序就可以了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c87b45ed6fc2477d96536a28ca33256c~tplv-k3u1fbpfcp-watermark.image?)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa8a0940591c4141aa348454e5986339~tplv-k3u1fbpfcp-watermark.image?)

这时字面量参数的情况依然也是对的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e88600ec9514d229775e5b5b9ce90f8~tplv-k3u1fbpfcp-watermark.image?)

为什么呢？

因为**重载函数的类型是从上到下依次匹配，只要匹配到一个就应用。**

非字面量的情况，类型是 number[]，能匹配 unknown[] 的那个类型，所以那个函数类型生效了。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c0ae501565b46f3a44568f56bc2e105~tplv-k3u1fbpfcp-watermark.image?)

而字面量的情况，推导出的是 readonly [1,2,3]，带有 readonly 所以不匹配 unknown[]，继续往下匹配，就匹配到了带有类型参数的那个函数类型。

这样两种情况就都应用了合适的函数类型。

全部代码是这样的：

```typescript
type Zip<One extends unknown[], Other extends unknown[]> = One extends [
  infer OneFirst,
  ...infer Rest1
]
  ? Other extends [infer OtherFirst, ...infer Rest2]
    ? [[OneFirst, OtherFirst], ...Zip<Rest1, Rest2>]
    : []
  : [];

type Mutable<Obj> = {
  -readonly [Key in keyof Obj]: Obj[Key];
};

function zip(target: unknown[], source: unknown[]): unknown[];

function zip<Target extends readonly unknown[], Source extends readonly unknown[]>(
  target: Target,
  source: Source
): Zip<Mutable<Target>, Mutable<Source>>;

function zip(target: unknown[], source: unknown[]) {
  if (!target.length || !source.length) return [];

  const [one, ...rest1] = target;
  const [other, ...rest2] = source;

  return [[one, other], ...zip(rest1, rest2)];
}

const result = zip([1, 2, 3] as const, [4, 5, 6] as const);

const arr1 = [1, 2, 3];
const arr2 = [4, '5', 6];

const result2 = zip(arr1, arr2);

```
[ts playground 地址](https://www.typescriptlang.org/play?#code/C4TwDgpgBAWglmAPAeQHbQgD2BVATAZygFdUBrVAewHdUBtAXQBoplgALCAJyix3yKkKNegwB8UALxQAUFFbpe2XISh04qAGbcFEAGJwuBYCwB05jdp4AlCMYCMDOfKgB+Vhx18VRdVp1snFwGRiZQ5qaWOrbGAExOLi7udHRo+obGLIHcIcbM4ebwSDHA9iwlsWIJiVAAXGrV8vWMANwyMqCQUACyxMAAhgBGADYQKIMAVhLSAN7OALRcEP14lKjDIGoA0hCbGlBku5SarJMM9ciTdDsgDG0Avm0ymqQAxsBwa1AAXggAFAMuABzCDAepCKi0RgsAiUYhcV4QcHkSGiACUyOEULu7ReqHen1QPwQiAAKv1gaClPxVEsVmsNiQUSJoVAAMpwhEYZQCKB01brTYQlniP7OQEgsFQcmUkzOWHwxH1DmKiAyDGwEm9AYjMYyyViFjaoajRAqrliMRPPEEr6-MAAimSzGo1kKrkukVoqBzeRwE5-ACEEtBplGqCBHCgAB9o1BA+7EWHcJH2N6lsB4UTWu15K81sY1GsIGZzEsHAwpFAQ8A2nmC8Ai54uKXTOXgPEq4mIE95Bms2o6MWWJRm-kIva-u2yny7B20Tj7u186hC+XiMNG9JJ3QZ7EWABmSv9IgrzJqAAsLAArCwAGzH08NtFPM+NilcexV3csfdQI9tG+UAfrE35XlAADk14QfeOIyEB66bqB27-B+M4gS+QA)

## 总结

今天我们做了一道综合的 ts 面试题，一共有三层：

第一层实现 js 的逻辑，用递归或者循环都能实现。

第二层给函数加上类型，用 function 声明类型和 interface 声明函数类型两种方式，参数和返回值都是 unknown[]。

第三层是用类型编程实现精准的类型提示，这一层需要拿到参数的类型，通过提取元素的类型并构造出新的数组类型返回。还要通过函数重载的方式来声明类型，并且要注意重载类型的声明顺序。

as const 能够让字面量推导出字面量类型，但会带有 readonly 修饰，可以自己写映射类型来去掉这个修饰。

其实这也是我们学习 ts 的顺序，我们先要能把 js 逻辑写出来，然后知道怎么给函数、class 等加 ts 类型，之后学习类型编程，知道怎么动态生成类型。

其中类型编程是 ts 最难的部分，也是最强大的部分。攻克了这一层，ts 就可以说学的差不多了。


## 26.加餐：项目中 2 个真实的类型编程案例

最近有两个同学问了我项目中遇到的 ts 问题，这俩问题都是典型的可以用类型编程来解决的。

这俩都是项目中真实遇到的 TS 类型问题，我们一起看一下吧：

第一个问题是这样的，项目中定义了接口返回的数据的类型，比如这样：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3e068564f03b4dc285a079783cbde186~tplv-k3u1fbpfcp-watermark.image?)

那么填充数据的时候就要根据类型的定义来写：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11ec2964b4374f3eb37d2b75cd100b91~tplv-k3u1fbpfcp-watermark.image?)

但是呢，如果你想扩展一些属性就报错了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/258248091d9140a4b5086f49702020b1~tplv-k3u1fbpfcp-watermark.image?)

但现在想每层都能灵活扩展一些属性，怎么做呢？

简化一下就是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acb4ef8bd47e46e281e7e65f76789e42~tplv-k3u1fbpfcp-watermark.image?)

如何能让这个索引类型可以灵活添加一些额外的索引呢？

可以这样，添加一个可索引签名

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d389c152b2243aa832259463e8f6b29~tplv-k3u1fbpfcp-watermark.image?)

能满足这个索引签名的额外索引都可以添加。

也可以这样写：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ef20dc51ec64060b17a0095882aea73~tplv-k3u1fbpfcp-watermark.image?)

和 Record<string, any> 取交叉类型。

这个 Record 是一个内置的高级类型，作用是根据传入的 key 和 value 的类型生成索引类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eda9f2842c1b43fab2843a778c0f7257~tplv-k3u1fbpfcp-watermark.image?)

这种生成索引类型的语法叫做映射类型。

所以，Record<string, any> 就是这样的，也是一个有可索引签名的索引类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d2a3ec1f0e5a494fb3cc0db61d005199~tplv-k3u1fbpfcp-watermark.image?)

普通的对象我们知道怎么处理了，那多层的呢？

这样任意层数的索引类型，怎么给每一层都加上 Record<string, any> 呢？

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/412296c71e4743648d2611b694024a26~tplv-k3u1fbpfcp-watermark.image?)

这时候就要用到递归了，可以这样写：

```typescript
type DeepRecord<Obj extends Record<string, any>> = {
    [Key in keyof Obj]: 
        Obj[Key] extends Record<string, any>
            ? DeepRecord<Obj[Key]> & Record<string, any>
            : Obj[Key]
} & Record<string, any>;
```

定义一个 DeepRecord 的高级类型，传入的类型参数 Obj 为一个索引类型，通过 Record<string, any> 约束。

然后通过映射类型的语法构造一个新的索引类型。

Key 来自之前的索引类型的 Key，也就是 Key in keyof Obj。

Value 要判断是不是索引类型，如果依然是 Record<string, any>，那就递归处理它的值 Obj[Key]，否则直接返回 Obj[Key]。

每一层都要和 Record<string, any> 取交叉类型。

这样就完成了递归让 Obj 的每一层都变得可扩展的目的。

我们测试一下：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57af468b9fb644269160ff584a588ece~tplv-k3u1fbpfcp-watermark.image?)

可以看到，处理过后的类型确实是每一层都加上了 Record<string, any>。

也确实每一层都可以扩展了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c87c0a4bccf4749bf1f84440e66d4b8~tplv-k3u1fbpfcp-watermark.image?)

并且有类型定义的索引也会做类型检查：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36e541a84c96419cbfc010f55b4ab68f~tplv-k3u1fbpfcp-watermark.image?)

小结一下：**可索引签名可以让索引类型扩展任意数量的符合签名的索引，如果想给任意层级的索引每层都加上可索引签名就要递归处理了。**

那如果不用类型编程呢？

那你就要原封不动的写一个新的索引类型，然后手动给每一层都加上可索引签名，那就麻烦太多了，而且也不通用。

这就是类型编程的意义之一，可以根据需要修改类型。

[案例一的 ts playground 地址](https://www.typescriptlang.org/play?#code/C4TwDgpgBAIghsOUC8UDeAoK2pzwLigDsBXAWwCMIAnAbixwqcMxzagGMvDTKb72OACYjCAZ2DUAlkQDmAnAF8ANA2wQNLNewBme8ZJnztbEUJ7kqdbYoy3QkWBrAAlCBwD21IQB4A8hQAVlAQAB7AEERCYlBunt4+EtJyyrhEIAB8GSjo2gDaANIQIFAyUADWxR46UAGBALqEJjh1hcX1IeGR0bHuXr5JRqlw6RnNggD8ThCufQmtRSD12QBkvfEDhilpmePshAvtdlBrcf2JW7LDo-QYDtDUEDGoMM5nCfCIGbeeRBJQQgQcEInyQqFYODwwKgAEZVGwmBQtIJsFwOIQ4XszIQAORQnE2eE4DQQZEovQ6XGInFEwTYqAAJhsdiAA)

再来看第二个问题：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d45527a9e92c4ce3ad4347bc9b5b54e8~tplv-k3u1fbpfcp-watermark.image?)

也就是当一个索引为 'desc' | 'asc' 的时候，其他索引都是 false。

这种类型怎么写呢？

有的同学说，这个就是枚举所有的情况呀，比如这样：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f23645078fc44085b7a36980aa74767d~tplv-k3u1fbpfcp-watermark.image?)

这确实能解决问题：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6956aaeb7b9f447b9e807056a6d94060~tplv-k3u1fbpfcp-watermark.image?)

可以看到类型检查是符合我们的需求的。

但如果我再加几个属性呢？

是不是可能的类型又多了几种？

手动维护也太麻烦了！

这时候就可以用类型编程动态生成了。

比如我定义这样一个高级类型：

```typescript
type GenerateType<Keys extends string> = {
    [Key in Keys]: {
        [Key2 in Key]: 'desc' | 'asc'
    }
}
```
它生成的类型是这样的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36e31de8fd3c463abddb8870a73e9d8f~tplv-k3u1fbpfcp-watermark.image?)

这个还是很容易理解的，映射类型就是用来生成索引类型的。

我们可以取它的值：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/059cdeae9ad14b53a8ea2d99dd2f454a~tplv-k3u1fbpfcp-watermark.image?)

结果就是这样的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cff5d073d12f40c2a2581ce85aa2a2df~tplv-k3u1fbpfcp-watermark.image?)

现在就只差那些为 false 的索引了。

Keys 是一个联合类型，从中去掉 Key 的类型，可以用 Exclude，也就是 Exclude<Keys, Key>。

那么这个类型就可以这么写：
```typescript
type GenerateType<Keys extends string> = {
    [Key in Keys]: {
        [Key2 in Key]: 'desc' | 'asc'
    } & {
        [Key3 in Exclude<Keys, Key>]: false
    }
}[Keys]
```
结果就是我们要的类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e1ffdd8c34642b29af4385190bc7874~tplv-k3u1fbpfcp-watermark.image?)

任意多个索引都可以动态生成复合需求的联合类型。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/23be1dc23a424a3bb3cc98c412247ce3~tplv-k3u1fbpfcp-watermark.image?)

上面这个高级类型还可以做一些优化，把 key 的约束换成 keyof any：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/601565b08a98493b9efc30dd4c169c75~tplv-k3u1fbpfcp-watermark.image?)

keyof any 的结果就是索引的类型：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9be688247f3d46f0b114b6a4a9febe20~tplv-k3u1fbpfcp-watermark.image?)

但有个配置项叫做 keyofStringsOnly

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32f78c5970a846288b1927785f82798f~tplv-k3u1fbpfcp-watermark.image?)

开启之后就只能是 string 作为 key 了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/050762aefc9e4e6bb86d2b79eecba53f~tplv-k3u1fbpfcp-watermark.image?)

keyof any 就可以动态获取 key 的可能类型，比写死更好。

这个高级类型最终就是这样的：

```typescript
type GenerateType<Keys extends keyof any> = {
    [Key in Keys]: {
        [Key2 in Key]: 'desc' | 'asc'
    } & {
        [Key3 in Exclude<Keys, Key>]: false
    }
}[Keys]
```

小结一下：**当需要枚举很多种类型的可能性的时候，可以用类型编程动态生成。**

那如果不用类型编程呢？

那你就得手动维护所有的可能类型了。

这就是类型编程的第二个意义，可以动态生成类型。

[案例二的 ts playground 地址](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hB2EBOBDYEAq4IB4DSEIAzlBAB7rwAmJA1oQPYBmUK8IAfFALxQDeAKCjCoAbQIgoAS3hQJRALoAufkJHrxhAEzTZE5VADkVCEQDGhqAB8jKc4bXCAvlABkq9RokBmXVACiZGYANgCuJviERAA0coQcBkwowUQQjlBOAk6axAoA3AICoJBQSKY8sAjIaJjYOIYojZY2hgBG7c1GZt2GHAUCZgzwRMCsSmUkvILqjSgqDfbR6e2tKkkpEEvq3WZryalZhYPDo6ul5VPps3sbWyIr8yaL6Ts3B5kDQyNQu+eTHiJrrZnuoHkYnhY7sJXlB1u8BEA)

通过这两个真实的案例，不知道你是否体会到类型编程解决了什么问题呢？

**当你需要修改已有的类型，或者动态生成类型，都可以用类型编程。**

第一个案例，我们递归给每一层加上了可索引签名，不需要手动一层层改。

第二个案例，我们动态生成了所有的可能类型，不需要手动枚举。

类型编程的意义，你感受到了么？


## 27.加餐：TypeScript 新语法 satisfies：用声明 or 用推导？

用了 TypeScript 之后，我们就可以声明类型，然后给 js 变量加上这个类型。

比如这样：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/839d85fdabfd417da58b26a83766a23d~tplv-k3u1fbpfcp-watermark.image?)

就有类型提示了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a09cbb9ed5784dd5a279635edd65c9e2~tplv-k3u1fbpfcp-watermark.image?)

也会做类型检查：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c7de116c10e49479139a36962208e6b~tplv-k3u1fbpfcp-watermark.image?)

但也不是所有的变量都要手动声明类型，因为 ts 会做自动类型推导：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72f234a1afcd484cbd7b229a77715e16~tplv-k3u1fbpfcp-watermark.image?)

同样是有类型提示和检查的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/209405eef42f4c96b4a9fd76c0cd549b~tplv-k3u1fbpfcp-watermark.image?)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/331cbcf780e14b9b8d72d332621627b3~tplv-k3u1fbpfcp-watermark.image?)

而且推导的时候还可以加上 as const，这样推导出的是字面量类型（不过会有 readonly 的修饰）：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13c6def9f769427692481c4b5c6eeae4~tplv-k3u1fbpfcp-watermark.image?)

那问题来了，什么时候手动声明类型，什么时候用自动推导呢？

比如上面这个 obj，b 属性推导出的是 string，但其实也可能是一个 number。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/260549661e1a4cd19c9cbd01264fa056~tplv-k3u1fbpfcp-watermark.image?)

但给它赋值 number 会报错：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b2c99dddfe54f5285f5151a1dbb72c1~tplv-k3u1fbpfcp-watermark.image?)

这种就得手动声明类型了：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/af795c82c84040e6b826d6ba92f89841~tplv-k3u1fbpfcp-watermark.image?)

还有，函数的参数，只有调用的时候才能知道参数具体的类型，这时候怎么自动推导？

没办法推导。

所以也得手动声明类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef027010480445fd9adc78246434a3d0~tplv-k3u1fbpfcp-watermark.image?)

总之，**ts 代码包括自动推导出的类型、手动声明的类型两种。**

自动类型推导省去了很多写类型的麻烦，但很多情况下还是要手动声明类型的。

但手动声明的类型是有局限性的，比如这样的类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dc4c8f0d8bb84190a594d15614b1a99f~tplv-k3u1fbpfcp-watermark.image?)

key:string 那部分是索引签名，也就是任意的 key 为 string，value 为任意类型的索引都可以加。

它是可以检查出类型错误，也支持扩展任意索引。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/183373e7c4fe4c15a69c69c3a56d298f~tplv-k3u1fbpfcp-watermark.image?)

但它只会提示声明的索引，动态添加的那些是不会提示的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b95c3811d994beaa0d29705c2fb0e11~tplv-k3u1fbpfcp-watermark.image?)

这样其实有的时候并不方便。

而如果自动推导呢？

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/914931b66bc045238ef1ed66db534d65~tplv-k3u1fbpfcp-watermark.image?)

这样就可以提示所有的索引了。

但是呢其中 b 的类型又不对，还是需要声明类型来约束。

是不是就很头疼？

用声明的方式少了具体赋值的变量类型的信息，用自动推导的方式又不能保证类型是对的。

有没有两全其美的办法呢？

4.9 之前还真没有。

不过 4.9 加入了一个 satisfies 的新语法。

这样用：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d8c0eb910b346c5bda15fb7557982e7~tplv-k3u1fbpfcp-watermark.image?)

不需要给变量声明这个类型了，用自动推导出来的类型，这样提示就是根据具体的值来的。

而且，还有了声明的方式的类型检查。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dad0bbbe7b0c40d4bd883975000eaf54~tplv-k3u1fbpfcp-watermark.image?)

是不是两全其美！

这就是为什么 ts 要增加 satisfies 这个语法。

它的作用就是**让你用自动推导出的类型，而不是声明的类型，增加灵活性，同时还可以对这个推导出的类型做类型检查，保证安全。**

但是，satisfies 的方式也有它的问题，比如这里用了推导出的类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c3ffcc06f644d6c87807e5999086aa7~tplv-k3u1fbpfcp-watermark.image?)

那就不能动态扩展索引了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19da355e509448869c32b201a1135050~tplv-k3u1fbpfcp-watermark.image?)

而如果是声明的那种索引签名，是支持扩展的：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/48529f4d86d44178af2c6fc158158007~tplv-k3u1fbpfcp-watermark.image?)

所以，具体什么时候用声明的类型，什么时候用推导出的类型 + satisfies，还是要看情况的。

这个新语法还是很有用的，估计以后在代码里会经常看到。

不过现在还没咋见，因为他还是在 beta 的版本。

需要下载 ts 指定 beta 才行：

```
npm install typescript@beta
```

这里的 @beta 是指定标签的意思。

我猜大家都用过 xxx@latest 的方式下载过 npm 包。

这个 latest 也同样是标签。

你可以通过 npm dist-tag ls 的方式看到 npm 包的所有 tag：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd9fb726c49b4a02b84c6978c31e9952~tplv-k3u1fbpfcp-watermark.image?)

所以说 npm install typescript 是下载不了 beta 版本的包的，它下载的是 latest 的 tag 对应的版本。只有手动指定 typescript@beta 才可以。

说点题外话，这个 tag 是怎么打上的呢？

发包的时候会用 npm publish，这种会自动打上 latest 的 tag。

也可以手动 npm publish --tags beta，这样打的就是 beta 的 tag了。

除了发包的时候可以指定 tag，平时也可以通过 npm dist-tag 命令来给某个版本的包打上 tag：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0656476f5be646a8b1ec3cc00bb320b9~tplv-k3u1fbpfcp-watermark.image?)

## 总结

TypeScript 中变量的类型有两种，一种是手动声明的，一种是自动推导的。

大多数情况下，不用手动声明类型，用自动推导的就行，比较方便。

但像函数参数、需要约束的变量类型等情况下就得手动声明了。

有的时候还是自动推导出的类型更合适一些，但是还需要通过声明的方式对其中的类型做约束。

不能两全其美。

所以 ts 加入了 satisfies 的语法，这样就可以用自动推导出的类型了，它也可以加上类型的约束。

算是融合了自动推导的类型和手动声明的类型的优点。

现在这个语法还在 4.9-beta 的包里，需要 npm install 的时候手动指定 dist-tag。

估计等它到正式版之后，你再写 ts 代码会有新的纠结了：

我是用手动声明的类型，还是自动推导的类型 + satiesfies 呢？这是个问题。


## 28.加餐：JSDoc 真能取代 TypeScript？

这几个月，想必大家都听到过一个新闻：

Svelte 弃用 TypeScript，改用 JSDoc 了。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/453d4156361c437cb4e6d5227dc123ca~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1192&h=538&s=263884&e=png&b=fdfdfd)

TypeScript 我们知道，是用来给 JS 加上类型的，可以实现类型提示和编译时的类型检查。

那 JSDoc 能够完成一样的功能么？Svelte 是出于什么原因弃用 TS 的呢？

先不着急回答这个问题。

我们总得先了解下 JSDoc：

可能大家认为的 JSDoc 是这个东西：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/852d125264ea43148e185571fe34a240~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1104&h=794&s=126697&e=png&b=f2f2f2)

在代码的注释上加上类型的标识，然后通过 jsdoc 命令行工具，就可以直接生成文档。

比如这样的文档：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f969a381d21d491d8527d388f0861579~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1500&h=487&s=101050&e=png&b=ffffff)

确实，这个是 JSDoc 最初的含义。

但我们说的 JSDoc 并不是这个，而是 TS 基于 JSDoc 语法实现的，在注释里给代码添加类型的语法。

文档在[这里](https://www.typescriptlang.org/docs/handbook/jsdoc-supported-types.html#type)：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9379fa6e2c4451aa9b8f3cf9971f2b1~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1714&h=1440&s=307515&e=png&b=faf9f9)

ts 支持在 js 文件的注释里，通过 JSDoc 的语法给它加上类型。

至于有什么意义，那可就太多了。

比如一个 JS 的配置文件，你想在写配置的时候能有提示，就可以用 JSDoc：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86a657befac44c8fb0ca1054838ee4d8~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=686&h=326&s=44805&e=png&b=212121)

这里注释里的 @type 就是 JSDoc 声明类型的语法。

在 vite 文档里，你可以看到对 JSDoc 的支持：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a2b99b95f6b4da39da48ddd8383c6be~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1458&h=488&s=79230&e=png&b=2a2c31)

我们自己试一下：

```
mkdir jsdoc-test
cd jsdoc-test
npm init -y
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87d2d9cb47b34d0da5090cbda1b56fd2~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=830&h=672&s=126834&e=png&b=000000)

创建项目和 package.json。

然后安装 typescript：

```
npm install --save-dev typescript
```
创建 tsconfig.json 文件：

```
npx tsc --init
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f631093ec7b44e2e897ac206cef59c40~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=702&h=378&s=44346&e=png&b=181818)

生成的 tscconfig.json 太多注释了，我们删一下：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec5082c2fadf4d98bd59302c8dee51d4~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=810&h=432&s=59270&e=png&b=1f1f1f)

然后创建 src/index.ts

```javascript
function add(a: number, b: number) {
    return a + b;
}
```

这样在用到这个 add 的时候，就会做类型检查：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fb1a2c2d775345679427cb122b9ec3c4~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=814&h=240&s=42321&e=png&b=212121)

在 tsconfig.json 里 include 一下：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ef3f6df19f643f39e900632eea5c728~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=680&h=478&s=67544&e=png&b=1f1f1f)

之后执行编译：

```
npx tsc
```
生成的代码是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b27b326454d4e9bb2fbf26d60518791~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=894&h=258&s=41000&e=png&b=1e1e1e)

这个是 ts 的编译流程，大家都很熟悉。

现在问题来了，我有一个 src/index2.js，怎么实现一样的类型检查呢？

这样写：
```javascript
/**
 * @param {number} a  参数aaa
 * @param {number} b  参数bbb
 */
function add2(a, b) {
    return a + b;
}
```
注释里的就是 JSDoc 的语法。

但现在并没有报类型错误：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4be5846f0904425aaa786a8d7fe8bd98~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=672&h=418&s=50357&e=png&b=1f1f1f)

需要在 tsconfig 里开启：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e156088b1f6b43fbb08d7682157dfaee~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=788&h=660&s=87910&e=png&b=1f1f1f)

allowJS 是允许编译 JS，checkJS 是在编译 JS 的时候也做类型检查。

开启后你就会发现，js 文件里也会做类型检查了：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2b101d7b3f434857b1458f3c3c9688bb~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=668&h=396&s=59515&e=png&b=202020)

hover 上去的时候，会提示类型信息：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1b5560c773b4070af53b660ab9c1863~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=776&h=388&s=60103&e=png&b=1f1f1f)

注意，这可不是用 ts 语法声明的类型，而是用 JSDoc 写的。

然后我们开启 dts：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff8cee813b78493b9510d33e58cc25cf~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=706&h=684&s=90457&e=png&b=1f1f1f)

再编译：

```
npx tsc
```
可以看到同样能产出 d.ts 类型声明文件：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6486c3bc88204e47b66bb1b78176223e~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1296&h=382&s=75735&e=png&b=1e1e1e)

而这时候产物的 JS 代码和源码差别不大：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e434d5d38b64e068a2d20dced2268c2~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=966&h=402&s=81724&e=png&b=1e1e1e)

因为本来 JSDoc 就是在注释里的，类型检查也好、生成 dts 也好，都不用改动源码。

这就是 JSDoc 最大的好处：**无侵入的给 JS 加上类型，拥有和 ts 一样的类型检查、类型提示、生成 dts 等功能，但却不需要编译，因为 JS 代码可以直接跑。**

有同学可能会说，就声明个函数类型就和 ts 一样了？

那肯定不止这么点语法，我们再看几个：

比如可以用 @type 给变量声明类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84857be5391847b39c313ff54c87142d~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=530&h=382&s=37946&e=png&b=212121)

这里可以是各种类型，比如函数类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/428e4537b0d54f20aaefbcf09c28c30f~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=776&h=202&s=32970&e=png&b=202020)

如果类型被多处用到，可以用 @typedef 抽出来，单独命名：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52b3aa0dd9dd45bb9523b433b713ea35~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=880&h=456&s=55699&e=png&b=1f1f1f)

你还可以把这个类型放到 dts 文件里，在这里 import 进来用：

比如我把它放到 guang.d.ts 里：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9f578a9075445e8a3e802fb5a080b01~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=668&h=194&s=28447&e=png&b=1f1f1f)

然后这样引入用：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/262de5ce6363454cab7ff5cb4ca9a4c8~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=766&h=214&s=35372&e=png&b=202020)

这样就避免了在 @typedef 里写大段类型定义了，不然代码写多了就不好维护了。

这样就可以在 dts 里定义类型，然后在 js 里通过 JSDoc 引入来用。

**dts + JSDoc 是绝佳搭配。**

然后我们继续看 JSDoc 的函数类型定义：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/446e3efbaf504ed987129524e3b76b1b~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=962&h=612&s=112804&e=png&b=1f1f1f)

这分别是可选参数、参数默认值、返回值类型的语法。

还有同学说，那 ts 的泛型呢？这个 JSDoc 不支持的吧？

当然也是支持的，这样写：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb98c9474a354f3992ef9c5c421ffdc8~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=652&h=484&s=70992&e=png&b=1f1f1f)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/677e676760de4e0985ba4aad9f6af872~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=544&h=210&s=25269&e=png&b=202020)

通过 @template 声明类型参数，然后下面就可以用了。

泛型都可以用，那基于泛型的类型编程，也就是类型体操当然也可以玩：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ea0061aaeff47acb46fb208a2a2f2ad~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=930&h=466&s=66372&e=png&b=1f1f1f)

一般这种复杂类型还是抽离到 dts 里，然后 @type {import('xxx').xxx} 引入比较好。

再就是 class 了，这个自然也是支持的。

比如声明一个泛型类：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6e52fadbdcd4c03b1d6485a380129c9~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=628&h=956&s=101258&e=png&b=1f1f1f)

这段类型大家能看懂么？

就是声明了一个泛型类，有一个类型参数 T。它通过 @extends 继承了 Set\<T\> 类型。

它有个 name 属性的类型为 T，并且还声明了构造器和 sleep 方法的类型。

用一下试试：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/191e42d236894ef8b6079c5b991aacb7~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=982&h=228&s=32429&e=png&b=222222)
      
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8e766409ac14c8d8b24b4df7531601a~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=532&h=184&s=22979&e=png&b=202020)
    
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/393f551b559e46c4bdd89d470af67a75~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=492&h=400&s=39546&e=png&b=212121)
    
name 和 sleep 的类型，继承的 Set 的类型，都没问题。
    
这就是 JSDoc 定义 class 类型的方式。

综上，用 JSDoc 可以定义变量、函数、class、泛型等，可以从别的 dts 文件引入类型。
    
基本上 ts 能做的，JSDoc 也都可以。
    
但是，JSDoc 语法毕竟是在注释里的，多了一大坨东西，而且写起来也不如 ts 语法直观。
    
所以，一般没必要这样写，除非你是给 JS 加类型。
    
那 svelte 是出于什么原因选择了 JSDoc 的方式呢？
    
看下那个 pr 就知道了：
  
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54598871ef0b467897c59cb7aab84801~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1540&h=824&s=194131&e=png&b=ffffff)

直接看官方回复：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/817603100ac84d2098d9148af37d3d4f~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1792&h=442&s=103441&e=png&b=ffffff)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f1d05aa22f1499195239f017ef749e0~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1818&h=806&s=250490&e=png&b=ffffff)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16f319f3930046a7b4b8cf2250afac90~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1792&h=838&s=271122&e=png&b=ffffff)

也就是说，用 ts 的语法，需要编译后才能调试，这样需要再 sourcemap 一次才能对应到源码。

但是用 JSDoc 的方式，不用编译就可以直接调试。

估计是遇到了啥 VSCode 调试上的问题。

然后下面还有个 VSCode 调试器的维护者评论说，有任何调试相关的问题可以找我：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/490470f547f14519b60344ced87f374c~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1820&h=1082&s=409403&e=png&b=ffffff)

总之，svelte 选择从 ts 转成 JSDoc + dts 并不是因为 ts 有啥问题，主要是为了调试方便。

那我们再看下它怎么用的吧：

可以看到，是 js 文件里用 JSDoc 来声明类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60ac39aad8e64cc4bea8ff20e354d31d~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1128&h=900&s=199396&e=png&b=1f1f1f)


然后复杂类型在 dts 里定义，然后这里引入：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8cec68a2cc8a41a7b9fe3077549708c9~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1084&h=512&s=135286&e=png&b=1f1f1f)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4219875e487749c4a818d2f19740b824~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1000&h=788&s=135774&e=png&b=1f1f1f)

就和我们刚才测试的一样。

## 总结

这几个月经常听到知名开源项目抛弃 ts 拥抱 JSDoc 的新闻，我们一起探究了一下。

JSDoc 是在 js 的注释里通过 @type、@typedef、@template、@param 等来定义类型，然后开启 checkJS 和 allowJS 的配置之后，tsc 就可以对 js 做类型检查。

ts 里可以定义的类型，在 JSDoc 里都可以定义，比如变量、函数、class、泛型，甚至类型编程等。复杂的类型还可以抽离到 dts 里，在 @type 里引入。

也就是说 JSDoc 确实可以替代 ts。

然后我们看了 svelte 选择 JSDoc 的原因，只是为了调试方便。这样不用编译就可以直接跑 js 代码，可以直接定位到源码。而且这样也能利用 ts 的类型提示和检查的能力。

所以很多人就说 svelte 抛弃了 ts。

这叫抛弃么？

并不是，JSDoc 只是另一种使用 ts 的方式而已。


## 29.加餐：一道字节面试真题

前天，小册群友问了我一个 TS 体操问题，说是面字节时遇到的。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ac06972003d74c30a831827d379a042c~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=792&h=376&s=142698&e=png&b=f9f9f9)

今天又催了一下：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/838cef3458bb4853a26713c7cd8fe890~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1066&h=494&s=125473&e=png&b=f3f2f2)

面试题是这样的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d42300aca9402cb7af99261b552e44~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1362&h=392&s=80451&e=jpg&b=fefcfc)

让实现这个 FormatDate 的类型，用来限制字符串只能是指定的日期格式。

看起来好像没多大难度，就是提取出 YY、MM、DD 和分隔符，然后构造对应的字符串类型就好了。

但上手试了一下，还真没那么简单。

首先，我们用模式匹配的方式，也就是 extends + infer 来提取出 YY、MM、DD 这三部分：

```javascript
type Seperator = '-' | '.' | '/';

type FormatDate<Pattern extends string> = 
  Pattern extends `${infer Aaa}${Seperator}${infer Bbb}${Seperator}${infer Ccc}`
    ? [Aaa,Bbb,Ccc]
    : never;
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd3845eadcfb479e8d367847600019f6~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=526&h=110&s=17286&e=png&b=fbfbfa)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/270cc21e76864a3ab642f9db0a5dc64a~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=522&h=106&s=18515&e=png&b=f9f9f8)

同样，也可以提取出分隔符部分：

```javascript
type FormatDate<Pattern extends string> = 
  Pattern extends `${infer Aaa}${Seperator}${infer Bbb}${Seperator}${infer Ccc}`
    ? Pattern extends `${Aaa}${infer Sep}${Bbb}${infer _}${Ccc}`
      ? [Aaa, Bbb, Ccc, Sep]
      : never
    : never;
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20e6bad93ad746b1a6034909e4417471~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=574&h=112&s=17671&e=png&b=fafaf9)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ef4b9f2d059b448d832df7a1e78d4818~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=586&h=110&s=19264&e=png&b=f9f9f8)

然后根据 YY、MM、DD 分别构造 4 位和 2 位的字符串，最后组合起来不就行了？

但问题就在这里。

组合字符串字面量类型是这样写：

```javascript
type Num = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

type YY = `${Num}${Num}${Num}${Num}`;

type MM = `${Num}${Num}`;

type DD = `${Num}${Num}`;

type GenStr<Type extends string> = 
  Type extends 'YY'
    ? YY
    : Type extends 'MM'
      ? MM
      : DD;

type res3 = `${GenStr<'YY'>}-${GenStr<'MM'>}-${GenStr<'DD'>}`;
```

就是根据 YY、MM 还是 DD 生成不同的字符串字面量，然后组合到一块。

这时候会提示你 union 数量太多：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e80e325feab94b1ab0ca22c42c2e53db~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1024&h=146&s=40207&e=png&b=f4f3f3)

因为组合起来的情况太多了。

这时候需要减少 union 数量才行。

所以我们可以改成这样：

```javascript
type Num = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

type Num2 = Num | 0

type YY = `19${Num2}${Num2}` | `20${Num2}${Num2}`;

type MM = `0${Num}` | `1${0 | 1 | 2}`;

type DD = `${0}${Num}` | `${1 | 2}${Num2}` | `3${0 | 1}`;

type GenStr<Type extends string> = 
  Type extends 'YY'
    ? YY
    : Type extends 'MM'
      ? MM
      : DD;

type res3 = `${GenStr<'YY'>}-${GenStr<'MM'>}-${GenStr<'DD'>}`;
```
也就是年份只能是 19 和 20 开头，月份只能是 1-12 的数字，日期是 01-31 的数字。

这样，组合就少了很多。

再试下：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcfd10b12c814b6ea4cec7725602e87e~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=924&h=144&s=39715&e=png&b=f9f9f8)

现在就能正常计算出类型了。

然后用之前提取出的 Aaa、Bbb、Ccc 和 Sep 来生成字符串字面量类型：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ffea0be3132445af978f7224a87ab420~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=1044&h=218&s=62961&e=png&b=fffffe)

这样，就完成了需求：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57c4971029884ee99c3ab7513093f6dd~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=688&h=152&s=28287&e=png&b=f9f9f8)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a31f07990527418d8f772372a09b0701~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=726&h=146&s=29465&e=png&b=f9f9f8)

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/372ac30da6f44f019ed6747f43a90321~tplv-k3u1fbpfcp-jj-mark:0:0:0:0:q75.image#?w=736&h=286&s=54857&e=png&b=f5f5f5)

回过头来看一下，这个类型难么？

思路并不难，就是通过模式匹配（extends + infer）提取出各部分，然后构造对应的字符串字面量类型，组合起来就好了。

它难在如果直接组合，union 数量会过多，从而报错。

所以需要根据年月日的特点，对生成的字符串字面量类型做更精准的控制。

这样，就能生成满足需求的日期字符串类型。

全部代码如下，大家可以试试：

```javascript
type Seperator = '-' | '.' | '/';

type Num = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

type Num2 = Num | 0

type YY = `19${Num2}${Num2}` | `20${Num2}${Num2}`;

type MM = `0${Num}` | `1${0 | 1 | 2}`;

type DD = `${0}${Num}` | `${1 | 2}${Num2}` | `3${0 | 1}`;

type GenStr<Type extends string> = 
  Type extends 'YY'
    ? YY
    : Type extends 'MM'
      ? MM
      : DD;

type FormatDate<Pattern extends string> = 
  Pattern extends `${infer Aaa}${Seperator}${infer Bbb}${Seperator}${infer Ccc}`
    ? Pattern extends `${Aaa}${infer Sep}${Bbb}${infer _}${Ccc}`
      ? `${GenStr<Aaa>}${Sep}${GenStr<Bbb>}${Sep}${GenStr<Ccc>}`
      : never
    : never;

const a: FormatDate<'YY-MM-DD'> = '2023-01-02';

const b: FormatDate<'DD/MM/YY'> = '01/02/2024';

const c: FormatDate<'DD/MM/YY'> = '2024-01-02';
```

[playground 地址](https://www.typescriptlang.org/play?ssl=44&ssc=1&pln=13&pc=1#code/FAegVGwARlgZGYO7dBY-4PO1ANzoADlBUcgFwJ4AOApoN4+g0eqAw-4BSugcXKBlfoPrmgnk6BR1oG+mgL6mA8FoPD6gIW6B1bUBk3oCY5aLEDR8oAVtJOKjyAYgHsATgFsAhjgAiWogB4ARNu0BaALLnTATWuGAfHPmBBRUAd0YNGAuOVkx5UAMZKAHYAzjhQACZ6AFxQyupaujgGxmaWNnb2UAC8UIYAjABMpkWmhQAMhQAshlAAPnmllWWVNQDcTlCAsHJuHiLenYGh4VHJsfGaOnpGJhZWtg45jaWlFdW1DQXF+autG43bh3v1UAB053KcvID0poCAxoBYmoCznoBgSoApaUJIhqb7hqc-IIZxCBgMB8MQoABlIjEFRaVRLADkpgRJwRpxRDQRIARHVBhCIUAAcgBXNRLfInQonADMJyqJwArCcAGwnADsJwAHCcAJy4sEEklqKm5IUncoggVQWxLAAG+R5ABIAN5CwoAXxVavVspOsoqWtJGsNwp1-PxUEscvKJp1evyKvKJwpDQ1svN4JMcsdmtVpLtDVlKpdUGNftNusD1MdzrNkotAHEiEEITgVPoACoWogAD2SQQiISgYRUAEsggBzLK5aBQLPg3P5wtQBG2BG1+QAfml1g7UFi9YJjeTzYRlnbfj83csffksRMHoJE0S0wAClpkioglBhwWiyXy1WlrX1zhN9vd82g8rywAzIgqKAAQQ0Gl9UJhcJUvrvD6gACEACNAPfaEHy-H8gnvR8AGF-H8HU+27U9zx3PMRyLa8XzfFVf0fD9fSAkDcKgv8AH1fTghDZVnKBu2vJMUzTfRsPsUCCF9RjU3TIi2JVAiVS45iqLYmjJznKAgiIAA3B8+1iKTZJUXEhjCKANHGVRJiSAxW2sOZTBMBFqxbNZqVMcp8gswocRBVTwkAzSEimZJ9AREwQEsEA2xMhFLJASoQDWKpbOAeyAic7Tpnc7RPPMbzrGMxFgosqzKlCoA)

## 总结

今天我们做了一道字节的 ts 体操真题。

核心思路就是模式匹配（extends + infer）提取出各部分内容，然后构造日期字符串。

答出这个，应该就有大部分的分了。

但是如果直接构造，会因为 union 数量太多导致失败。

这时候要根据日期的特点想办法减少 union 的数量，直到可以顺利生成。

再答出这个，这道面试题就稳了。

这道题整体来说还是比较难的，既考察了模式匹配+ 构造的 ts 类型编程基础，又考察了对 union 太多的情况的处理，算是一道比较高阶的面试题。


## 3.TypeScript 类型编程为什么被叫做类型体操？

类型系统不止 TypeScript 有，别的语言 Java、C++ 等都有，为什么 TypeScript 的类型编程被叫做类型体操，而其他语言没有呢？这节我们来分析下原因。

TypeScript 给 JavaScript 增加了一套静态类型系统，通过 TS Compiler 编译为 JS，编译的过程做类型检查。

它并没有改变 JavaScript 的语法，只是在 JS 的基础上添加了类型语法，所以被叫做 JavaScript 的超集。

JavaScript 的标准在不断的发展，TypeScript 的类型系统也在不断完善，因为“超集”的设计理念，这两者可以很好的融合在一起，是不会有冲突的。

静态类型编程语言都有自己的类型系统，从简单到复杂可以分为 3 类：

### 简单类型系统

变量、函数、类等都可以声明类型，编译器会基于声明的类型做类型检查，类型不匹配时会报错。

这是最基础的类型系统，能保证类型安全，但有些死板。

比如一个 add 函数既可以做整数加法、又可以做浮点数加法，却需要声明两个函数：

```c++
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}
```

这个问题的解决思路很容易想到：如果类型能传参数就好了，传入 int 就是整数加法，传入 double 就是浮点数加法。

所以，就有了第二种类型系统。

### 支持泛型的类型系统

泛型的英文是 Generic Type，通用的类型，它可以代表任何一种类型，也叫做`类型参数`。

它给类型系统增加了一些灵活性，在整体比较固定，部分变量的类型有变化的情况下，可以减少很多重复代码。

比如上面的 add 函数，有了泛型之后就可以这样写：

```c++
T add<T>(T a, T b) {
    return a + b;
}

add(1,2);
add(1.111, 2.2222);
```

**声明时把会变化的类型声明成泛型（也就是类型参数），在调用的时候再确定类型。**

Java 就是这种类型系统。如果你看过 Java 代码，你会发现泛型用的特别多，这确实是一个很好的增加类型系统灵活性的特性。

但是，这种类型系统的灵活性对于 JavaScript 来说还不够，因为 JavaScript 太过灵活了。

比如，在 Java 里，对象都是由类 new 出来的，你不能凭空创建对象，但是 JavaScript 却可以，它支持对象字面量。

那如果是一个返回对象某个属性值的函数，类型该怎么写呢？

```typescript
function getPropValue<T>(obj: T, key): key对应的属性值类型 {
    return obj[key];
}
```

好像拿到了 T，也不能拿到它的属性和属性值，如果能对类型参数 T 做一些逻辑处理就好了。

所以，就有了第三种类型系统。

### 支持类型编程的类型系统

在 Java 里面，拿到了对象的类型就能找到它的类，进一步拿到各种信息，所以类型系统支持泛型就足够了。

但是在 JavaScript 里面，对象可以字面量的方式创建，还可以灵活的增删属性，拿到对象并不能确定什么，所以要支持对传入的类型参数做进一步的处理。

**对传入的类型参数（泛型）做各种逻辑运算，产生新的类型，这就是类型编程。**

比如上面那个 getProps 的函数，类型可以这样写：

```typescript
function getPropValue<
    T extends object,
    Key extends keyof T
>(obj: T, key: Key): T[Key] {
    return obj[key];
}
```

这里的 keyof T、T[Key] 就是对类型参数 T 的类型运算。

TypeScript 的类型系统就是第三种，支持对类型参数做各种逻辑处理，可以写很复杂的类型逻辑。

**类型逻辑可以多复杂？**

类型逻辑是对类型参数的各种处理，可以实现很多强大的功能：

比如这个 ParseQueryString 的类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/411e1505474d475a8e612bd4b473623e~tplv-k3u1fbpfcp-zoom-1.image)

它可以对传入的字符串的类型参数做解析，返回解析以后的结果。

如果是 Java 的只支持泛型的类型系统可以做到么？明显不能。但是 TypeScript 的类型系统就可以，因为它可以对泛型（类型参数）做各种逻辑处理。

只不过，这个类型的类型逻辑的代码比较多（下面的 ts 类型暂时看不懂没关系，在顺口溜那节会有详解，这里只是用来直观感受下类型编程的复杂度的，等学完以后大家也能实现这样的复杂高级类型的）：

```typescript
type ParseParam<Param extends string> = 
    Param extends `${infer Key}=${infer Value}`
        ? {
            [K in Key]: Value 
        } : {};

type MergeValues<One, Other> = 
    One extends Other 
        ? One
        : Other extends unknown[]
            ? [One, ...Other]
            : [One, Other];

type MergeParams<
    OneParam extends Record<string, any>,
    OtherParam extends Record<string, any>
> = {
  [Key in keyof OneParam | keyof OtherParam]: 
    Key extends keyof OneParam
        ? Key extends keyof OtherParam
            ? MergeValues<OneParam[Key], OtherParam[Key]>
            : OneParam[Key]
        : Key extends keyof OtherParam 
            ? OtherParam[Key] 
            : never
}
type ParseQueryString<Str extends string> = 
    Str extends `${infer Param}&${infer Rest}`
        ? MergeParams<ParseParam<Param>, ParseQueryString<Rest>>
        : ParseParam<Str>;
```

**TypeScript 的类型系统是`图灵完备`的，也就是能描述各种可计算逻辑。简单点来理解就是循环、条件等各种 JS 里面有的语法它都有，JS 能写的逻辑它都能写。**

对类型参数的编程是 TypeScript 类型系统最强大的部分，可以实现各种复杂的类型计算逻辑，是它的优点。但同时也被认为是它的缺点，因为除了业务逻辑外还要写很多类型逻辑。

不过，我倒是觉得这种复杂度是不可避免的，因为 JS 本身足够灵活，要准确定义类型那类型系统必然也要设计的足够灵活。

是不是感觉 TypeScript 类型系统挺复杂的？确实，不然大家也不会把 TS 的类型编程戏称为`类型体操`了。

但不用担心，这本小册就是专门讲这个的，后面会讲各种 TS 类型编程的套路，学完那些之后，再回来看这个问题就没那么难了。

## 总结

TypeScript 给 JavaScript 增加了一套类型系统，但并没有改变 JS 的语法，只是做了扩展，是 JavaScript 的超集。

这套类型系统支持泛型，也就是类型参数，有了一些灵活性。而且又进一步支持了对类型参数的各种处理，也就是类型编程，灵活性进一步增强。

现在 TS 的类型系统是图灵完备的，JS 可以写的逻辑，用 TS 类型都可以写。

但是很多类型编程的逻辑写起来比较复杂，因此被戏称为类型体操。

## 4.TypeScript 类型系统支持哪些类型和类型运算？

学完前几节我们知道 TypeScript 给 JavaScript 加了一套静态类型系统，还支持了泛型和各种类型运算逻辑。

那么这个类型系统里都有哪些类型？支持哪些类型运算逻辑？

## TypeScript 类型系统中的类型

静态类型系统的目的是把类型检查从运行时提前到编译时，那 TS 类型系统中肯定要把 JS 的运行时类型拿过来，也就是 number、boolean、string、object、bigint、symbol、undefined、null 这些类型，还有就是它们的包装类型 Number、Boolean、String、Object、Symbol。

这些很容易理解，给 JS 添加静态类型，总没有必要重新造一套基础类型吧，直接复用 JS 的基础类型就行。

复合类型方面，JS 有 class、Array，这些 TypeScript 类型系统也都支持，但是又多加了三种类型：元组（Tuple）、接口（Interface）、枚举（Enum）。

### 元组

`元组（Tuple）`就是元素个数和类型固定的数组类型：

```typescript
type Tuple = [number, string];
```
### 接口
`接口（Interface）`可以描述函数、对象、构造器的结构：

对象：

```typescript
interface IPerson {
    name: string;
    age: number;
}

class Person implements IPerson {
    name: string;
    age: number;
}

const obj: IPerson = {
    name: 'guang',
    age: 18
}
```
函数：

```typescript
interface SayHello {
    (name: string): string;
}

const func: SayHello = (name: string) => {
    return 'hello,' + name
}
```
构造器：
```typescript
interface PersonConstructor {
    new (name: string, age: number): IPerson;
}

function createPerson(ctor: PersonConstructor):IPerson {
    return new ctor('guang', 18);
}
```
对象类型、class 类型在 TypeScript 里也叫做索引类型，也就是索引了多个元素的类型的意思。对象可以动态添加属性，如果不知道会有什么属性，可以用可索引签名：

```typescript
interface IPerson {
    [prop: string]: string | number;
}
const obj:IPerson = {};
obj.name = 'guang';
obj.age = 18;
```
总之，**接口可以用来描述函数、构造器、索引类型（对象、class、数组）等复合类型**。

### 枚举

`枚举（Enum）`是一系列值的复合：

```typescript
enum Transpiler {
    Babel = 'babel',
    Postcss = 'postcss',
    Terser = 'terser',
    Prettier = 'prettier',
    TypeScriptCompiler = 'tsc'
}

const transpiler = Transpiler.TypeScriptCompiler;
```

此外，TypeScript 还支持`字面量类型`，也就是类似 1111、'aaaa'、{ a: 1} 这种值也可以做为类型。

其中，字符串的字面量类型有两种，一种是普通的字符串字面量，比如 'aaa'，另一种是模版字面量，比如 `aaa${string}`，它的意思是以 aaa 开头，后面是任意 string 的字符串字面量类型。

所以想要约束以某个字符串开头的字符串字面量类型时可以这样写：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64066e8ca57d4f09897071f2ea91aad3~tplv-k3u1fbpfcp-watermark.image?)

还有四种特殊的类型：void、never、any、unknown：

- **never** 代表不可达，比如函数抛异常的时候，返回值就是 never。
- **void** 代表空，可以是 undefined 或 never。
- **any** 是任意类型，任何类型都可以赋值给它，它也可以赋值给任何类型（除了 never）。
- **unknown** 是未知类型，任何类型都可以赋值给它，但是它不可以赋值给别的类型。

这些就是 TypeScript 类型系统中的全部类型了，大部分是从 JS 中迁移过来的，比如基础类型、Array、class 等，也添加了一些类型，比如 枚举（enum）、接口（interface）、元组等，还支持了字面量类型和 void、never、any、unknown 的特殊类型。

###  类型的装饰

除了描述类型的结构外，TypeScript 的类型系统还支持描述类型的属性，比如是否可选，是否只读等：

```typescript
interface IPerson {
    readonly name: string;
    age?: number;
}

type tuple = [string, number?];
```

## TypeScript 类型系统中的类型运算

我们知道了 TypeScript 类型系统里有哪些类型，那么可以对这些类型做什么类型运算呢？

### 条件：extends ? : 

TypeScript 里的条件判断是 `extends ? :`，叫做条件类型（Conditional Type）比如：

```typescript
type res = 1 extends 2 ? true : false;
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ad094fa410940fcbb54e74f029ad265~tplv-k3u1fbpfcp-watermark.image?)

这就是 TypeScript 类型系统里的 if else。

但是，上面这样的逻辑没啥意义，静态的值自己就能算出结果来，为什么要用代码去判断呢？

所以，类型运算逻辑都是用来做一些动态的类型的运算的，也就是对类型参数的运算。

```typescript
type isTwo<T> = T extends 2 ? true: false;

type res = isTwo<1>;
type res2 = isTwo<2>;
```


![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b54d5af2ec7a4ebb9679817ccc84c23c~tplv-k3u1fbpfcp-watermark.image?)

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/688987f1b7354de1b8780add86861efd~tplv-k3u1fbpfcp-watermark.image?)

这种类型也叫做`高级类型`。

**高级类型的特点是传入类型参数，经过一系列类型运算逻辑后，返回新的类型。**

### 推导：infer 

如何提取类型的一部分呢？答案是 infer。

比如提取元组类型的第一个元素：

```typescript
type First<Tuple extends unknown[]> = Tuple extends [infer T,...infer R] ? T : never;

type res = First<[1,2,3]>;
```
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22b916e9f07b4dd58a4098b70eecf77f~tplv-k3u1fbpfcp-watermark.image?)

注意，第一个 extends 不是条件，条件类型是 `extends ? :`，这里的 extends 是约束的意思，也就是约束类型参数只能是数组类型。

因为不知道数组元素的具体类型，所以用 unknown。

infer 在后面的章节会大量用到，这里先简单了解即可。

### 联合：｜ 

联合类型（Union）类似 js 里的或运算符 |，但是作用于类型，代表类型可以是几个类型之一。

```typescript
type Union = 1 | 2 | 3;
```

### 交叉：&

交叉类型（Intersection）类似 js 中的与运算符 &，但是作用于类型，代表对类型做合并。

```typescript
type ObjType = {a: number } & {c: boolean};
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44b56ec911e94618acff65eb7e42fb0f~tplv-k3u1fbpfcp-watermark.image?)

注意，同一类型可以合并，不同的类型没法合并，会被舍弃：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61934612b9ce46049d25e9293c53b2e3~tplv-k3u1fbpfcp-watermark.image?)

### 映射类型

对象、class 在 TypeScript 对应的类型是索引类型（Index Type），那么如何对索引类型作修改呢？

答案是`映射类型`。

```typescript
type MapType<T> = {
  [Key in keyof T]?: T[Key]
}
```

keyof T 是查询索引类型中所有的索引，叫做`索引查询`。

T[Key] 是取索引类型某个索引的值，叫做`索引访问`。

in 是用于遍历联合类型的运算符。

比如我们把一个索引类型的值变成 3 个元素的数组：

```typescript
type MapType<T> = {
    [Key in keyof T]: [T[Key], T[Key], T[Key]]
}

type res = MapType<{a: 1, b: 2}>;
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8c462c6120348d0bdd00afbaa58727c~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAsghmAKuCAeRA+KBeKBvAKCmKgG0BpCEKASwDsoBrKgewDMpEBdALjMQpUuAGk6CQIsZQlcCAXwIFQkKACcIAZxywEySKjxw+ARlEAjPgCY5GANxA)

**映射类型就相当于把一个集合映射到另一个集合，这是它名字的由来**。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d31910d7bb6f4e379bf91a638e9c4f36~tplv-k3u1fbpfcp-watermark.image?)


除了值可以变化，索引也可以做变化，用 as 运算符，叫做`重映射`。

```typescript
type MapType<T> = {
    [
        Key in keyof T 
            as `${Key & string}${Key & string}${Key & string}`
    ]: [T[Key], T[Key], T[Key]]
}
```
我们用 as 把索引也做了修改，改成了 3 个 key 重复：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1240af0a478640cdbc7fa364045eefaf~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAsghmAKuCAeRA+KBeKBvAKCmKgG0iTKBpCEKASwDsoBrWgewDMpEoLKBUOAGcoAAwAkeGnQBkUYcABOTAOYBfKTKjzFKxhq20dC5WvVj+UALoAuMolIzrAGh5Par98+sF1BAlBIKCUIUVx4JBRUPDh7AEY3ACN7ACZ1DABuIA)

这里的 & string 可能大家会迷惑，解释一下：

因为索引类型（对象、class 等）可以用 string、number 和 symbol 作为 key，这里 keyof T 取出的索引就是 string | number | symbol 的联合类型，和 string 取交叉部分就只剩下 string 了。就像前面所说，交叉类型会把同一类型做合并，不同类型舍弃。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7a37f14570743898285a59f5e797662~tplv-k3u1fbpfcp-watermark.image?)

因为 js 处理对象比较多，所以索引类型的映射比较重要。

## 总结

给 JavaScript 添加静态类型系统，那肯定是能复用的就复用，所以在 TypeScript 里，基础类型和 class、Array 等复合类型都是和 JavaScript 一样的，只是又额外加了接口（interface）、枚举（enum）、元组这三种复合类型（对象类型、class 类型在 TypeScript 里叫做索引类型），还有 void、never、any、unkown 四种特殊类型，以及支持字面量做为类型。此外，TypeScript 类型系统也支持通过 readonly、？等修饰符对属性的特性做进一步的描述。

此外，TypeScript 支持对类型做运算，这是它的类型系统的强大之处，也是复杂之处。

TypeScript 支持条件、推导、联合、交叉等运算逻辑，还有对联合类型做映射。

这些逻辑是针对类型参数，也就是泛型（类型参数）来说的，**传入类型参数，经过一系列类型运算逻辑后，返回新的类型的类型就叫做高级类型**，如果是静态的值，直接算出结果即可，没必要写类型逻辑。

这些语法看起来没有多复杂，但是他们却可以实现很多复杂逻辑，就像 JS 的语法也不复杂，却可以实现很多复杂逻辑一样。

后面我们会大量用到这些类型编程语法来实现各种复杂的类型逻辑。


## 5.套路一：模式匹配做提取

TypeScript 类型编程的代码看起来比较复杂，但其实这些逻辑用 JS 大家都会写，之所以到了类型体操就不会了，那是因为还不熟悉一些套路。

所以，这节开始我们就来学习一些类型体操的套路，熟悉这些套路之后，各种类型体操逻辑就能够很顺畅的写出来。

首先，我们来学习类型体操的第一个套路：模式匹配做提取。

## 模式匹配

我们知道，字符串可以和正则做模式匹配，找到匹配的部分，提取子组，之后可以用 $1,$2 等引用匹配的子组。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b6e9f15d14c452f8b5f4a59a3d3add8~tplv-k3u1fbpfcp-watermark.image?)

Typescript 的类型也同样可以做模式匹配。

比如这样一个 Promise 类型：

```typescript
type p = Promise<'guang'>;
```

我们想提取 value 的类型，可以这样做：

```typescript
type GetValueType<P> = P extends Promise<infer Value> ? Value : never;
```

通过 extends 对传入的类型参数 P 做模式匹配，其中值的类型是需要提取的，通过 infer 声明一个局部变量 Value 来保存，如果匹配，就返回匹配到的 Value，否则就返回 never 代表没匹配到。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7fea3a531fab498e8ca7a1daace8038b~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwDUCGAbArhAKuCAeACgHxQC8U+UEAHsBAHYAmAzuQE4D2AtgJZN7d0AZhFZRk6CMQD8Y1BigAuKHQgA3EQG4AUDtCRY8cRgBKEJmhTBSBxHKw4CHHn1wByAOZokdd68KENIA)

这就是 Typescript 类型的模式匹配：

**Typescript 类型的模式匹配是通过 extends 对类型参数做匹配，结果保存到通过 infer 声明的局部类型变量里，如果匹配就能从该局部变量里拿到提取出的类型。**

这个模式匹配的套路有多有用呢？我们来看下在数组、字符串、函数、构造器等类型里的应用。

## 数组类型

### First

数组类型想提取第一个元素的类型怎么做呢？
```typescript
type arr = [1,2,3]
```
用它来匹配一个模式类型，提取第一个元素的类型到通过 infer 声明的局部变量里返回。

```typescript
type GetFirst<Arr extends unknown[]> = 
    Arr extends [infer First, ...unknown[]] ? First : never;
```
 
类型参数 Arr 通过 extends 约束为只能是数组类型，数组元素是 unkown 也就是可以是任何值。

> **any 和 unknown 的区别**：
>any 和 unknown 都代表任意类型，但是 unknown 只能接收任意类型的值，而 any 除了可以接收任意类型的值，也可以赋值给任意类型（除了 never）。类型体操中经常用 unknown 接受和匹配任何类型，而很少把任何类型赋值给某个类型变量。

对 Arr 做模式匹配，把我们要提取的第一个元素的类型放到通过 infer 声明的 First 局部变量里，后面的元素可以是任何类型，用 unknown 接收，然后把局部变量 First 返回。

当类型参数 Arr 为 [1,2,3] 时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/189a8a20ed5c4f60905bc88ca9ba61bb~tplv-k3u1fbpfcp-watermark.image?)

当类型参数 Arr 为 [] 时：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff00e79903474f01b522fc95b4189096~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwDECWAnAzsAPAQRSqEAHsBAHYAmaUArqQNakD2A7qQNoC6AfFALxS58REhSpskpAGYR8ydMAA0UAHSraDFuw4coAfihyMUAFxRSEAG4yA3ACh7oSLHiHgAJQhpqAG2B9niKgYmGwAjAoATAoAzNx2to7QcIHyHl6+Ef7JriFxtkA)

### Last

可以提取第一个元素，当然也可以提取最后一个元素，修改下模式类型就行：

```typescript
type GetLast<Arr extends unknown[]> = 
    Arr extends [...unknown[], infer Last] ? Last : never;
```
当类型参数 Arr 为 [1,2,3]时：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/959e27b8dbfd420182d8bcac575c6d5b~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwBkCGBnYAeAggJ21CAHsBAHYAmKUAriQNYkD2A7iQNoC6AfFALxQ55CxcpVYA6CTXrM27ADRQAliQBmEPMjTsoAfiibgUAFxQSEAG7qA3ACg7oSLHgGAShBRUANob5xEqDFYARjkAJjkAZi5bGwdoP1d3L2BQ3id-NHQOTisgA)

### PopArr

我们分别取了首尾元素，当然也可以取剩余的数组，比如取去掉了最后一个元素的数组：

```typescript
type PopArr<Arr extends unknown[]> = 
    Arr extends [] ? [] 
        : Arr extends [...infer Rest, unknown] ? Rest : never;
```

如果是空数组，就直接返回，否则匹配剩余的元素，放到 infer 声明的局部变量 Rest 里，返回 Rest。

当类型参数 Arr 为 [1,2,3] 时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd533ba9b9a2431287b1c8d12f02e6df~tplv-k3u1fbpfcp-watermark.image?)

当类型参数 Arr 为 [] 时：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22a64419e01a47f49ca4dc0d60bc8510~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBACg9mAggJ2QHhcqEAewIB2AJgM5QCuBA1gXAO4EDaAugHxQC8Um2ehpUFlAD8g5lABc3VL3zEyjAHTKAlgQBmELACUIJYABoK1Wg3Gjd+yVAIQAbloDcAKFehIsBJfIAbYJ08kVDRGAEYDACYDAGY2FzdwaHgwbz8IgOTMELigA)

### ShiftArr

同理可得 ShiftArr 的实现：

```typescript
type ShiftArr<Arr extends unknown[]> = 
    Arr extends [] ? [] 
        : Arr extends [unknown, ...infer Rest] ? Rest : never;
```

当类型参数 Arr 为 [1,2,3]时：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a1c5bb5c645a472ba143b4c4787e972a~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAygCwJYDMQEEBOmA8XMxQAeIUAdgCYDOMArmQNZkD2A7mQNoC6AfDALwx8hEuWoxuMAPwSuMAFxDsI0pRod6TNmQA0MAHSGkZFFAIAlKFRByZl6wphkoANzMBuYF-DR4yNPa0ADYgAn6oGNg4HACMOgBMOgDMvJ6gkLCIEYEh8WFZaPjRqUA)

## 字符串类型

字符串类型也同样可以做模式匹配，匹配一个模式字符串，把需要提取的部分放到 infer 声明的局部变量里。

### StartsWith

判断字符串是否以某个前缀开头，也是通过模式匹配：

```typescript
type StartsWith<Str extends string, Prefix extends string> = 
    Str extends `${Prefix}${string}` ? true : false;
```
需要声明字符串 Str、匹配的前缀 Prefix 两个类型参数，它们都是 string。

用 Str 去匹配一个模式类型，模式类型的前缀是 Prefix，后面是任意的 string，如果匹配返回 true，否则返回 false。

当匹配时：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/891a3c57dc8b4a9581883b05d58ced38~tplv-k3u1fbpfcp-watermark.image?)

不匹配时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e3eaa47b924f9ca4e837042a12650c~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAysCGAnYBnA6gS2ACwDx0SggA9gIA7AExShWEQ3IHMAaKABUQgDMNijSFarXqMmAPigBeWPQFkqNAAYASAN6cefAL7q6DZtqVQA-FHoBXaAC4o3eABsUEANwAoD6EiykqTDgAlCBQLB2BpH2R0LDwAciYLeGYoJMooSgB7Zli2eMTs8XcPNy9oOF9owODQ4AAmCPKo-ziEpKYUqnSsphyoWMyClyA)

### Replace

字符串可以匹配一个模式类型，提取想要的部分，自然也可以用这些再构成一个新的类型。

比如实现字符串替换：

```typescript
type ReplaceStr<
    Str extends string,
    From extends string,
    To extends string
> = Str extends `${infer Prefix}${From}${infer Suffix}` 
        ? `${Prefix}${To}${Suffix}` : Str;
```

声明要替换的字符串 Str、待替换的字符串 From、替换成的字符串 3 个类型参数，通过 extends 约束为都是 string 类型。

用 Str 去匹配模式串，模式串由 From 和之前之后的字符串构成，把之前之后的字符串放到通过 infer 声明的局部变量 Prefix、Suffix 里。

用 Prefix、Suffix 加上替换到的字符串 To 构造成新的字符串类型返回。

当匹配时：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cd97d2e01ec4749bd80ab520d1733ff~tplv-k3u1fbpfcp-watermark.image?)

不匹配时：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/41c48e63dc6240dfa481dd256c89a9e0~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAShYBsCGBjCBlYAnAPJrUEAHsBAHYAmAzlFdgJZkDmANFAGJYD2AtoSeWq0GzNgBUu-UpRp0sjJgD4oAXihR8UwTQAGAEgDejAGYQCABSwRj9IgF9DnXg6NlTBdAFdjN+zqgA-FD6BpbWti4SLl4+Ef4AXBrYANwAUOmgkLDwyGhwVJ4IwKrZiKgY2DgARADinkjMTPXMAOQ0AEYQdFDG8oJQ9DQBVWxVw6MAIlzMFNNMVYppGeDQcGV5XYXAAEwla7kVuFVI7SgjUGPnVVMzcwvJQA)

### Trim

能够匹配和替换字符串，那也就能实现去掉空白字符的 Trim：

不过因为我们不知道有多少个空白字符，所以只能一个个匹配和去掉，需要递归。

先实现 TrimRight:
```typescript
type TrimStrRight<Str extends string> = 
    Str extends `${infer Rest}${' ' | '\n' | '\t'}` 
        ? TrimStrRight<Rest> : Str;
```

类型参数 Str 是要 Trim 的字符串。

如果 Str 匹配字符串 + 空白字符 (空格、换行、制表符)，那就把字符串放到 infer 声明的局部变量 Rest 里。

把 Rest 作为类型参数递归 TrimRight，直到不匹配，这时的类型参数 Str 就是处理结果。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df89e8af4ccb4d868cae790b82d10fbc~tplv-k3u1fbpfcp-watermark.image?)

同理可得 TrimLeft：

```typescript
type TrimStrLeft<Str extends string> = 
    Str extends `${' ' | '\n' | '\t'}${infer Rest}` 
        ? TrimStrLeft<Rest> : Str;
```

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c44ef0a46e514a3588b220e23752da8d~tplv-k3u1fbpfcp-watermark.image?)

TrimRight 和 TrimLeft 结合就是 Trim：

```typescript
type TrimStr<Str extends string> =TrimStrRight<TrimStrLeft<Str>>;
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/332a738fff064ba58b073d1e03539275~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAKgTgSwLYGVhwEoIOYAtgA8acUEAHsBAHYAmAzlHegldgHxQC8UxpF19KAAMAJAG8WAMwgkMEJgF9xAciiqAPmoA6VDduDKFQqAH5YiVOix5CcphwBcPdAG4AUG9CRzya-jsArgA2wFw+lpg4+ATK2AEAhqxQySnJymzunuDQ8MjEADIQkoS85JS0DEyIrBzcpfwVwipqUJrKOnrtBkoSVNKy8sBGpuEFRbaDjs5wmV45FoXFgSFhuRGLhKqpUDQA9qzps9mj6ETofOWCVSzsXGvEfoT36BtncGwZHlnea8uh3M84DFtjt9tgUoc3EA)

## 函数

函数同样也可以做类型匹配，比如提取参数、返回值的类型。

### GetParameters

函数类型可以通过模式匹配来提取参数的类型：

```typescript
type GetParameters<Func extends Function> = 
    Func extends (...args: infer Args) => unknown ? Args : never;
```
类型参数 Func 是要匹配的函数类型，通过 extends 约束为 Function。

Func 和模式类型做匹配，参数类型放到用 infer 声明的局部变量 Args 里，返回值可以是任何类型，用 unknown。

返回提取到的参数类型 Args。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1dd929580e34c77afc6265886ee43f4~tplv-k3u1fbpfcp-watermark.image?)

[试一试](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwAUCGAnJBbeEUGcA8AYgK4B2AxlBAB7AQkAmOUx5wAlgPYkB8UAvM1IVqtBkwAUAOmmoA5jgBcUNiQBm2KAEEU8gJT9epANYkOAdxJQA-Fp1MlJCADdsAbgBQn0JCjI0mWlwAJQgcIgAbYH5YeD8MLFw8cRJ4pRxgFBVZABooJFkIByJ0ACNsfT5edMySWW4Pd29oOIDsHBCwyIAmaLhEVHjA-HEKqoys+qA)

## GetReturnType

能提取参数类型，同样也可以提取返回值类型：

```typescript
type GetReturnType<Func extends Function> = 
    Func extends (...args: any[]) => infer ReturnType 
        ? ReturnType : never;
```

Func 和模式类型做匹配，提取返回值到通过 infer 声明的局部变量 ReturnType 里返回。

参数类型可以是任意类型，也就是 any[]（注意，这里不能用 unknown，这里的解释涉及到参数的逆变性质，具体原因逆变那一节会解释）。


![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4539c7a0a01c43a7837908c6397bcbfc~tplv-k3u1fbpfcp-watermark.image?)

[试一试](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwCV4FcBOA7AKuCAeAYsugMZQQAewE6AJgM5SEnACWA9ugHxQC8jRpClVoMAFADpJAQ1QBzOgC4oU9CADaAXQCUvbi3QAzCKihJgaLDigB+UygzZIUJeggA3YwG4AUN9BOzC0cIJDpkABtw4F5YeECHHFxRdCkAWwglOmBUfVkdHm4AchoOWULOTyA)

### GetThisParameterType

方法里可以调用 this，比如这样：

```javascript
class Dong {
    name: string;

    constructor() {
        this.name = "dong";
    }

    hello() {
        return 'hello, I\'m ' + this.name;
    }
}

const dong = new Dong();
dong.hello();
```
用`对象.方法名`的方式调用的时候，this 就指向那个对象。

但是方法也可以用 call 或者 apply 调用：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75229ba1521c42d1940c441e6e0ee0d5~tplv-k3u1fbpfcp-watermark.image?)

call 调用的时候，this 就变了，但这里却没有被检查出来 this 指向的错误。

如何让编译器能够检查出 this 指向的错误呢？

可以在方法声明时指定 this 的类型：

```javascript
class Dong {
    name: string;

    constructor() {
        this.name = "dong";
    }

    hello(this: Dong) {
        return 'hello, I\'m ' + this.name;
    }
}
```
这样，当 call/apply 调用的时候，就能检查出 this 指向的对象是否是对的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a0fef176aec24e27ad2513b9a04afaa7~tplv-k3u1fbpfcp-watermark.image?)

如果没有报错，说明没开启 strictBindCallApply 的编译选项，这个是控制是否按照原函数的类型来检查 bind、call、apply

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73676681ef8f450f9ba281584d44d131~tplv-k3u1fbpfcp-watermark.image?)

这里的 this 类型同样也可以通过模式匹配提取出来：

```typescript
type GetThisParameterType<T> 
    = T extends (this: infer ThisType, ...args: any[]) => any 
        ? ThisType 
        : unknown;
```

类型参数 T 是待处理的类型。

用 T 匹配一个模式类型，提取 this 的类型到 infer 声明的局部变量 ThisType 中，其余的参数是任意类型，也就是 any，返回值也是任意类型。

返回提取到的 ThisType。

这样就能提取出 this 的类型：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c8247dad58d4a0cbf2d1b2701908a45~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/MYGwhgzhAEAiD2A7A5tA3gKGt6iwFsBTALmggBcAnASxQG4MsdgkLKBXYc+SgCgEp0THDnIALahAB0eItAC80AEQATJMiUMRAX0YixhECHi9xk0ghSDMIkZULl2lRNADkBo-AA00AJIAdV3w3aABqaDNpWUItHF1dDBZECmg1FAVcQgB3OHUBBjTkKQ9jfMZC4sNjKWAwI140AA9m4gBGbX4GDHIATwAHQmgAcQcAFQkIAAUwSgIHQkpR-sIAHlGAPgzR6EJG8kJEFRhTCdJaADMF6HHJJYGfKUeZ5AhSMEQegG0AXUF5TfePWgAH5rhM7oNSOxEABrRDwLKILq9AbDMYTaazIj7RbLABKhBgihG5BuUxmcxxEJWKMI8HOqXUlU86y6GCAA)

## 构造器

构造器和函数的区别是，构造器是用于创建对象的，所以可以被 new。

同样，我们也可以通过模式匹配提取构造器的参数和返回值的类型：

### GetInstanceType

构造器类型可以用 interface 声明，使用 new(): xx 的语法。

比如：

```typescript
interface Person {
    name: string;
}

interface PersonConstructor {
    new(name: string): Person;
}
```
这里的 PersonConstructor 返回的是 Person 类型的实例对象，这个也可以通过模式匹配取出来。

```typescript
type GetInstanceType<
    ConstructorType extends new (...args: any) => any
> = ConstructorType extends new (...args: any) => infer InstanceType 
        ? InstanceType 
        : any;
```
类型参数 ConstructorType 是待处理的类型，通过 extends 约束为构造器类型。

用 ConstructorType 匹配一个模式类型，提取返回的实例类型到 infer 声明的局部变量 InstanceType 里，返回 InstanceType。

这样就能取出构造器对应的实例类型：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3bde943e699415fab2be6e6aeeeb454~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwEkB2BnYBDJBjCAVcEAPAMID2qwATgK5bCmX6RQQAewESAJilEhAHcoACgB049JQDmKAFxRMIAJRQAvAD4FSEJoBQUA2qhkKNOgybQ2Hbr35CxE6XK3K1mgJZIAZhEpRkNEwcSyh9QwiAfgCKYLwCMIiI+UUAbl1dLw5Kb3QcKAAFPxRyKABvcIMkdABbCHk0Si8pdIBfDKy-XPyiyhKkE0baen8KiPtharqGqmaleV7+tozQZjhEWOx4yAAlCF5VWHhAjC3LQkXyQaphhnV0oA)

### GetConstructorParameters

GetInstanceType 是提取构造器返回值类型，那同样也可以提取构造器的参数类型：

```typescript
type GetConstructorParameters<
    ConstructorType extends new (...args: any) => any
> = ConstructorType extends new (...args: infer ParametersType) => any
    ? ParametersType
    : never;
```
类型参数 ConstructorType 为待处理的类型，通过 extends 约束为构造器类型。

用 ConstructorType 匹配一个模式类型，提取参数的部分到 infer 声明的局部变量 ParametersType 里，返回 ParametersType。

这样就能提取出构造器对应的参数类型：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0db834880b4c4ca6a6e22c894eaa4209~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBA4hwGED2A7AzsATgVwMbCUwAUBDTEgW3gkzQB4AoKZqZdLPAzAFXGggAewCCgAmaKCggB3KAAoAdErIBzNAC4oJFCACUUALwA+LToYmDrVBhz5CvSFEHCxEqbMXLMazQEsUAGY0UKTkVMK0DhD6xqYgTCwA-CFklNSRfAnMmlIAbjQA3AwM-hEBJLjQRDRoqFAA3lmSaZo2-ipFAL7FpTTllSE1qGw2nIQNTe5yKC1QbSgquprVtKhdxaCOcIjWHHbEqeE1AEoQEpbbI3tcoWkR9Cu1KFe2XEZFQA)

## 索引类型

索引类型也同样可以用模式匹配提取某个索引的值的类型，这个用的也挺多的，比如 React 的 index.d.ts 里的 PropsWithRef 的高级类型，就是通过模式匹配提取了 ref 的值的类型：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/33c5fa6ffe7a4fda85230e5b363e0d5c~tplv-k3u1fbpfcp-watermark.image?)

我们简化一下那个高级类型，提取 Props 里 ref 的类型：

### GetRefProps

我们同样通过模式匹配的方式提取 ref 的值的类型：

```typescript
type GetRefProps<Props> = 
    'ref' extends keyof Props
        ? Props extends { ref?: infer Value | undefined}
            ? Value
            : never
        : never;
```
类型参数 Props 为待处理的类型。

通过 keyof Props 取出 Props 的所有索引构成的联合类型，判断下 ref 是否在其中，也就是 'ref' extends keyof Props。

为什么要做这个判断，上面注释里写了：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/580bf3bf266f42c69b268d96a3fb09be~tplv-k3u1fbpfcp-watermark.image?)

在 ts3.0 里面如果没有对应的索引，Obj[Key] 返回的是 {} 而不是 never，所以这样做下兼容处理。

如果有 ref 这个索引的话，就通过 infer 提取 Value 的类型返回，否则返回 never。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71790e667fba43759068d72d2f44f234~tplv-k3u1fbpfcp-watermark.image?)

当 ref 为 undefined 时：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/08aa267ecaaf461a959bcb83230352fe~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?ts=4.5.0-beta#code/C4TwDgpgBA4hwCUIDMAKAnA9mAzgHg2xwD4oBeKAKChqgHJ0U6oIAPYCAOwBMcoBrCCEzIohXNVpSA-GKy4W7LrygBvKI2TSAXFACWnZBHRQAagEMANgFdoAHyjWeKAxG4BfSVO9RZFmxBePrS6nBAAbsZBUqERxgDclJSgkLDwSGjyOEh8FHCIKOL46po6UACMADRQnOYAthC6dNyYnADmdO7Eicng0PkZRTkATORpBZlEeCUoZU7cLmHc1bUNTS3tnd2UQA)

## 总结

就像字符串可以匹配一个模式串提取子组一样，TypeScript 类型也可以匹配一个模式类型提取某个部分的类型。

**TypeScript 类型的模式匹配是通过类型 extends 一个模式类型，把需要提取的部分放到通过 infer 声明的局部变量里，后面可以从这个局部变量拿到类型做各种后续处理。**

模式匹配的套路在数组、字符串、函数、构造器、索引类型、Promise 等类型中都有大量的应用，掌握好这个套路能提升很大一截类型体操水平。

[本文案例的合并](https://www.typescriptlang.org/play?#code/PTAEm8fRo9UZXlFmTR1TUPexgAOUFj-pCEVoeH1CcyoWUTAtBUAXjQNeUAoMkUABQCcB7AWwEsBnAUwC4yAXATwAO7UAHF2PAGoBDADYBXdgBVB7ADzUAfKAC8NUOwAePdgDsAJqxoMWHVcxMAzdrVDT57LQH5XshaE6gJuwAbs4A3BT8QqLibgoASuyscjI8OjGSvkoq6tZsagDkAOZyUiZFBRoaERRUgA6mgCN+qLVgYjwAYsy0rDy8Khmd3TyqAIK0LobG5pZyJgDWJvQA7iYA2gC6WrpjE0amFqCr9k4ugz0ANKAAdDezC8tr6+ug3mdpAUGhtDVRwm1viWSqXS-y6PVUqwAjOcAEznADMmwivwGYJ4gJSPBhIPEbwhSJaGQAMlIen1om0SeCdvo9tNQHdFisNltQDTJvtLKsbldGQ8Npdjs5QFSeM9vKL-IEQuFIv1KaT0UlMTieKKIdC4YjquS-uJRRjUtjdArwSyalRqPQBDtdTRrTtRuNaVMDnzmZt0uy6QcNi9Ds8At7XVyeUKXICeJd3SZxaBI1LPrK7VaBIa0rpU46obCEQSUan08b7TbxvidYSAMoAC2YDh4tpRNbrDbLwc5DPmTMerPb9L93j9QedHP7McuYccwsjcYTHxl3zl0Wb9fT6RXrdoGtz2uR-Q3RfXtfr2YJlDAgHVtQBk3oAmOWa59AlZ4UloPFYAHVmDxq9wm8-Xx+X7VqoT67CGoA9LQ9hFJcdDsA4zAGC6HaQdBrKgch9IAAYACQAN5wQhBgAL74ah5TEVh-o8LQfgBA4sgcD8+7-m+n7fmuuhPi+bFAaoxSlOUoBlGYoBmPQ5QFJcAllBUOp-jxgEccqRrrqxSnATJQkiWJEkVNJ4mSRWD6JAIMhSAAxlwdqmeZVmgSBNGYQc5EwaA7TWM5liuZcij0F5EE0Wh6SPk5o4HLheHhlY8GIaReEeUw8XRZWcgOERlH+pFhFxfhfnxal6VxVRASgcx0S2ZZ7CcfG7BmVVDkAEQiIJRQlLJBSWAARkkaQOFB+ygGwLyNZcjWeKNoCNQAInphlFI18n9JVVmHroK3sE1UhdRZk3jXts3lPNi01A+ihQYwv79OdzCMKB8TMEU1bDBh4XeUF5ToWFPqWJF0WRvFBSgEDAA+wMADomKDEM8AUmXeDdd00Q9T3DJGWilTR5XCIjKPPTViP3Y9z38e1QmgBTlPAxWKKEzRRLwS933ga5X1gR2kVA9DBSQ9z4Ow8lU4Rr18OgHTtAM-Wqjo1KZVLjjF2S0qQIZmLF2gUr-FUxT82VNjau3Q5r0-YFUGfTo4t48M4ua6BVT67jKmq+LWva-NlN6xQD6AL+KdT3lQbTUC+UiMOIzisHagfB6HxjdKo7SzBZAUJyYFk8MwEmsinSdvaAAAUPIvkUrABNFYzFwAlDoWgxv65eWPOXz60HtAh2H3Q1VHrcx+Hqh5yYbcBD5wlFFwgRyIwPW0FX2haKze7RC3bex6wa0ZEvPdx3nM9zx9RQVgH4iJDwci0CYyhCJHR-iKf585NnyeJ+nmfpA-ucFzcRcl8JJh8BsO9DSFrVE+Z8L7CG8MfW+YDEwLn1pA0BKhDTAhNNfEBd8hB9wHqHIee8AEFF1gfVo4hFC1lYBvduYCyAWXMqwSwh0iigDwmQKmWCx6uRqFTCyElIJyDTvQWg29GHMO1hTb8bArisPSI1Y6EQqbEQoFTas7AZAyHoHnMR396FVyYSIimtAb5n2BkolR9BLgAElwYFEYMDUAABqUAGiJFt1kZTeR8iqHcLSO7XQQQligHodvCI80rjGNUYEigwTQn0CuBZWQMg854QMEkzgkJiIV31m0EhbByGxzAaoRQrJFABXUaQ0uQCsmsDAROT+tBi4BDKH-dYACGn+gqdAgIMYMnENITk5wYDASqgqb02geTfj0AcLpcoITlGqMIaAQAIeaAAIEwAFmr+yITwMxJgehlCspQlEbRNnbNTtkDBABhTxtE+EjP6LnXx+dC61O-g05pv8tDCIproc5WyaK8J4Pw6Btz2B+I-lcL+9Tf4AOioc58xzoHvO1t4aFOyTnCHhVTcFfAaj2FjgxKyNBw4SSESwweptoIRHcdi5wuLhDUAJSYL5PCrlEspr4-uJLXIVwCLS7oElyXywyEi2FiCkiqkFbsnI3LWASQZT8q5cy2gysuX82gwyI77PEIq35-DVWqHhZqq5AKTZ3JBWCn+fAXl8DIKyfVyrDXgWNQ8upgCTg0Gju3SpKgLXwu8Kqyh6LpRN35Qqi5WqVVupXgMlBPAbXavDb3SV0qQ1yotGAQARL6AFR9KAzRD5KgcHQa0Jcr65vzQIVguQC2snhQUfRDgga5zmOwPg4yrAFrRZTH1DBS0BTwqAGtngykuriMIMGswzCxSCGYeRuiEU+HcG2kRjdnDzpgYGotiQ82dtXiKqN66S1lp7X2gI0JAgkvwXpOGNN5TXw3QWwExY2i7s3aoA98F+2djHQhCdlxWEBDPZJYiFYgA)


## 6.套路二：重新构造做变换

类型编程主要的目的就是对类型做各种转换，那么如何对类型做修改呢？

TypeScript 类型系统支持 3 种可以声明任意类型的变量： type、infer、类型参数。

type 叫做类型别名，其实就是声明一个变量存储某个类型：

```typescript
type ttt = Promise<number>;
```
infer 用于类型的提取，然后存到一个变量里，相当于局部变量：
```typescript
type GetValueType<P> = P extends Promise<infer Value> ? Value : never;
```
类型参数用于接受具体的类型，在类型运算中也相当于局部变量：

```typescript
type isTwo<T> = T extends 2 ? true: false;
```

但是，严格来说这三种也都不叫变量，因为它们不能被重新赋值。

TypeScript 设计可以做类型编程的类型系统的目的就是为了产生各种复杂的类型，那不能修改怎么产生新类型呢？

答案是重新构造。

这就涉及到了第二个类型体操套路：重新构造做变换。

## 重新构造

**TypeScript 的 type、infer、类型参数声明的变量都不能修改，想对类型做各种变换产生新的类型就需要重新构造。**

数组、字符串、函数等类型的重新构造比较简单。

索引类型，也就是多个元素的聚合类型的重新构造复杂一些，涉及到了映射类型的语法。

我们先从简单的开始：

## 数组类型的重新构造

### Push

有这样一个元组类型：

```typescript
type tuple = [1,2,3];
```
我想给这个元组类型再添加一些类型，怎么做呢？

TypeScript 类型变量不支持修改，我们可以构造一个新的元组类型：

```typescript
type Push<Arr extends  unknown[], Ele> = [...Arr, Ele];
```

类型参数 Arr 是要修改的数组/元组类型，元素的类型任意，也就是 unknown。

类型参数 Ele 是添加的元素的类型。

返回的是用 Arr 已有的元素加上 Ele 构造的新的元组类型。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01b0b85547194b85957fc49719f90af2~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBACgrgZwBYB4CCAnDUIA9gQB2AJglFHIQNaED2A7oQNoC6ANFAKIA2EAfFAC8UJgDpxmDBx4QWAbgBQS0JFiIkAJQgI43YELXIUTAIwcATBwDM7KABY+ioA)

这就是数组/元组的重新构造。

>**数组和元组的区别**：数组类型是指任意多个同一类型的元素构成的，比如 number[]、Array\<number>，而元组则是数量固定，类型可以不同的元素构成的，比如 [1, true, 'guang']。


### Unshift

可以在后面添加，同样也可以在前面添加：

```typescript
type Unshift<Arr extends  unknown[], Ele> = [Ele, ...Arr];
```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b5251a521ce34c7f93d4a7aa7896c94f~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAqgdgZwBYEsBmwA8BBATrqCAD2AjgBMEooBXOAazgHsB3OAbQF0AaKAUQA2EAHxQAvFHaCIvAHTy8uTgG4AUKtCRYiVBgBKEBDQHBx25OizsAjLwBMvAMw8oABmHKgA)

这两个案例比较简单，我们来做一个复杂的：

### Zip

有这样两个元组：

```typescript
type tuple1 = [1,2];
type tuple2 = ['guang', 'dong'];
```
我们想把它们合并成这样的元组：
```typescript
type tuple = [[1, 'guang'], [2, 'dong']];
```

思路很容易想到，提取元组中的两个元素，构造成新的元组：

```typescript
type Zip<One extends [unknown, unknown], Other extends [unknown, unknown]> = 
    One extends [infer OneFirst, infer OneSecond]
        ? Other extends [infer OtherFirst, infer OtherSecond]
            ? [[OneFirst, OtherFirst], [OneSecond, OtherSecond]] :[] 
                : [];
```

两个类型参数 One、Other 是两个元组，类型是 [unknown, unknown]，代表 2 个任意类型的元素构成的元组。

通过 infer 分别提取 One 和 Other 的元素到 infer 声明的局部变量 OneFirst、OneSecond、OtherFirst、OtherSecond 里。

用提取的元素构造成新的元组返回即可：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37dbf1cdf86d49358595274c9d167f07~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAWglmAPAeQHbQgD2BVATAZygG0BXVAa1QHsB3VAGinKrtQF0nlgALCAJyhYc+ImUo16TFpI4A+KAF4oAKCjqoaDNlyEScVADMBm9ADE4-AsCYHjgrQGUIAY2r52ajd4D8m3ibCumJ2Jtx8-BZWNlChDgH8zm4eXt5pUH7ExFpR1lwJucCcJE6u7nj5EUnl7OxQAFzEdanprfUk7ADcKi2taSqgkLAIAEoQBKQANsBKw0jEAIwMAEzFxADkAOakAIaom+tM63juB+xynUA)

但是这样只能合并两个元素的元组，如果是任意个呢？

那就得用递归了：

```typescript
type Zip2<One extends unknown[], Other extends unknown[]> = 
    One extends [infer OneFirst, ...infer OneRest]
        ? Other extends [infer OtherFirst, ...infer OtherRest]
            ? [[OneFirst, OtherFirst], ...Zip2<OneRest, OtherRest>]: []
                : [];
```
类型参数 One、Other 声明为 unknown[]，也就是元素个数任意，类型任意的数组。

每次提取 One 和 Other 的第一个元素 OneFirst、OtherFirst，剩余的放到 OneRest、OtherRest 里。

用 OneFirst、OtherFirst 构造成新的元组的一个元素，剩余元素继续递归处理 OneRest、OtherRest。

这样，就能处理任意个数元组的合并：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e79ddcf08184e618430b5885592260c~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAWglmATAHgPIDtoQB7AugEwGcoBXdAa3QHsB3dAbQF0AaKVYACwgCcoc8hEuSp1GTAHxQAvFABQURe0z9c+YlAZx0AM17KIAMTg8iwNgDor2vXwwQAShDNMFS9wH52XfQPUktXX0Obh5jU3MoKwsbYJ8eJxc3dxSoLwYGe3CzNhDebOBWKKt4JDRMRMi8hOdgCSYALk1XVNalJuYAbjkeuVBIWARERNIAG2AZQbKGAEYWRBYAZhYAFhYAViKGAHIAc1IAQ3Rd7bZtgmpj06htuCJr7YAjWoedHjh1bclOoA)

了解了数组类型的重新构造，我们再来看下字符串类型的：

## 字符串类型的重新构造

### CapitalizeStr

我们想把一个字符串字面量类型的 'guang' 转为首字母大写的 'Guang'。

需要用到字符串类型的提取和重新构造：

```typescript
type CapitalizeStr<Str extends string> = 
    Str extends `${infer First}${infer Rest}` 
        ? `${Uppercase<First>}${Rest}` : Str;
```
我们声明了类型参数 Str 是要处理的字符串类型，通过 extends 约束为 string。

通过 infer 提取出首个字符到局部变量 First，提取后面的字符到局部变量 Rest。

然后使用 TypeScript 提供的内置高级类型 Uppercase 把首字母转为大写，加上 Rest，构造成新的字符串类型返回。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ca8ff4fdc3f4aadb0fed9d49df3ec71~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAwghmAlsOAbRAvCBlYAnAHlzyggA9gIA7AEwGco79EqBzAPigF4pjSLq9KAAMAJAG8WAMwgkAYojxMAvhOmyoAJQgrhUAPwiJAVTCQ8AYzh0IBBUuDtV47bqgAuXvgDcAKH+gkLAIyGiYEK4ArqjA3MFIKOhYxAQA5KyRcGyp7N5AA)

这就是字符串类型的重新构造：**从已有的字符串类型中提取出一些部分字符串，经过一系列变换，构造成新的字符串类型。**

### CamelCase

我们再来实现 dong_dong_dong 到 dongDongDong 的变换。

同样是提取和重新构造：

```typescript
type CamelCase<Str extends string> = 
    Str extends `${infer Left}_${infer Right}${infer Rest}`
        ? `${Left}${Uppercase<Right>}${CamelCase<Rest>}`
        : Str;
```

类型参数 Str 是待处理的字符串类型，约束为 string。

提取 _ 之前和之后的两个字符到 infer 声明的局部变量 Left 和 Right，剩下的字符放到 Rest 里。

然后把右边的字符 Right 大写，和 Left 构造成新的字符串，剩余的字符 Rest 要继续递归的处理。

这样就完成了从下划线到驼峰形式的转换：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/50e1ecae11064007a152f626e1006cb4~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAwghgWwgG3gZwgHgMrAE5QQAewEAdgCZpRr4CWZA5gHxQC8UAUFD1LgcVKVqAAwAkAbwYAzCAQAyEacAC+AfUky5UAEp1GAC1Waysgjoi0VI7rzsB+KOImLlKyQFUwkPAGM4GJh6hsDM7hLwSKgBWBa0YTZ2dgBcfPgA3JycoJCwiCjoEHEArsjA7HlRhZgA5BQA9kxqDU0tjDXM6UA)

### DropSubStr

可以修改自然也可以删除，我们再来做一个删除一段字符串的案例：删除字符串中的某个子串

```typescript
type DropSubStr<Str extends string, SubStr extends string> = 
    Str extends `${infer Prefix}${SubStr}${infer Suffix}` 
        ? DropSubStr<`${Prefix}${Suffix}`, SubStr> : Str;
```
类型参数 Str 是待处理的字符串， SubStr 是要删除的字符串，都通过 extends 约束为 string 类型。

通过模式匹配提取 SubStr 之前和之后的字符串到 infer 声明的局部变量 Prefix、Suffix 中。

如果不匹配就直接返回 Str。

如果匹配，那就用 Prefix、Suffix 构造成新的字符串，然后继续递归删除 SubStr。直到不再匹配，也就是没有 SubStr 了。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8751c7cef5fa4c0b81e91c82346beb54~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAIgTgezAZQK4CNnDgHi3KCAD2AgDsATAZyiuwEsyBzAGijU20JPOtoeYA+KAF4oAKChT2XYqUo0ABgBIA3owBmEAgAU4EDfSIBfNR3yn1ZLQTQbDJxROkuoAfliIUGfDhWq9AyNLOwdjRTZzbGEALhk4AG5xcVBITyQAJQgqVAAbYFF0705cAHIKBGYAPxrStlKq0sEEoA)

字符串类型的重新构造之后，我们再来看下函数类型的重新构造：

## 函数类型的重新构造：

### AppendArgument

之前我们分别实现了参数和返回值的提取，那么重新构造就是用这些提取出的类型做下修改，构造一个新的类型即可。

比如在已有的函数类型上添加一个参数：

```typescript
type AppendArgument<Func extends Function, Arg> = 
    Func extends (...args: infer Args) => infer ReturnType 
        ? (...args: [...Args, Arg]) => ReturnType : never;
```

类型参数 Func 是待处理的函数类型，通过 extends 约束为 Function，Arg 是要添加的参数类型。

通过模式匹配提取参数到 infer 声明的局部变量 Args 中，提取返回值到局部变量 ReturnType 中。

用 Args 数组添加 Arg 构造成新的参数类型，结合 ReturnType 构造成新的函数类型返回。

这样就完成了函数类型的修改：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57e69e3602754410bec28e13e829fdac~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAgmkDsAmMBOBzArgWwg4APAGKYIDGUEAHsHkgM5QnnACWA9ggDSwYB8UALxQAUFHFNSFarWSMAFADplAQwz0AXFFYIAZhFS909AJRCBO-YYBKEYJlQIAKuGhiJHgPxQlq9VoBtZUU0Yx5QgF0zQQFbe0cXSCgtBAgANwMAbhERUCS4RBQMHDxgW3pMABtgcWECulCS-AJ5BBVcLXpgVB10aIEAI3Z2SogVbigEHAGDPmygA)

最后，我们再来看下索引类型的重新构造

## 索引类型的重新构造

索引类型是聚合多个元素的类型，class、对象等都是索引类型，比如这就是一个索引类型：

```typescript
type obj = {
  name: string;
  age: number;
  gender: boolean;
}
```
索引类型可以添加修饰符 readonly（只读）、?（可选）:

```typescript
type obj = {
  readonly name: string;
  age?: number;
  gender: boolean;
}
```

对它的修改和构造新类型涉及到了映射类型的语法：

```typescript
type Mapping<Obj extends object> = { 
    [Key in keyof Obj]: Obj[Key]
}
```

### Mapping

映射的过程中可以对 value 做下修改，比如：

```typescript
type Mapping<Obj extends object> = { 
    [Key in keyof Obj]: [Obj[Key], Obj[Key], Obj[Key]]
}
```

类型参数 Obj 是待处理的索引类型，通过 extends 约束为 object。

用 keyof 取出 Obj 的索引，作为新的索引类型的索引，也就是 Key in keyof Obj。

值的类型可以做变换，这里我们用之前索引类型的值 Obj[Key] 构造成了三个元素的元组类型 [Obj[Key], Obj[Key], Obj[Key]]：


![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c48fadee010f48bd9ef83979711ae2f3~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAsgQwhAlgOwOYB4DyAjAKxigA8Qo0ATAZxgHtCoBjEAPhgF4YBvGYGATADaAaShgY6GAGtxdAGYx8BALoAuYctHiVAGiWFtYPQYJGVK4AF9goSLABOUWl0TJ02Xgg0BGfXg0AJitWAG4gA)

索引类型的映射画下图很容易理解：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20f29fe720ee40d19c35e2fc4f3467db~tplv-k3u1fbpfcp-watermark.image?)

### UppercaseKey

除了可以对 Value 做修改，也可以对 Key 做修改，使用 as，这叫做`重映射`：

比如把索引类型的 Key 变为大写。

```typescript
type UppercaseKey<Obj extends object> = { 
    [Key in keyof Obj as Uppercase<Key & string>]: Obj[Key]
}
```

类型参数 Obj 是待处理的索引类型，通过 extends 约束为 object。

新的索引类型的索引为 Obj 中的索引，也就是 Key in keyof Obj，但要做一些变换，也就是 as 之后的。

通过 Uppercase 把索引 Key 转为大写，因为索引可能为 string、number、symbol 类型，而这里只能接受 string 类型，所以要 & string，也就是取索引中 string 的部分。

value 保持不变，也就是之前的索引 Key 对应的值的类型 Obj[Key]。

这样构造出的新的索引类型，就把原来索引类型的索引转为了大写：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10144e25a6424b7eadbf8f70e317d1c6~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAqmkCcDGBDAzhA0hEAeA8gEYBWUEAHsBAHYAmaUA9iREsAHxQC8UA3lACgowqAG1sIKAEtqUANY5GAMyhFS6WPAjJ0EXBKgAyKGmAIZAc3YBdAFyqS4nNYEBfAQNCRNiVBgkAShBoAK4ANsDcPtp+WDi4-BYhKNQW9gCMADRQtIyp9gBMruwA3EA)

#### Record

TypeScript 提供了内置的高级类型 Record 来创建索引类型：

```typescript
type Record<K extends string | number | symbol, T> = { [P in K]: T; }
```
指定索引和值的类型分别为 K 和 T，就可以创建一个对应的索引类型。

上面的索引类型的约束我们用的 object，其实更语义化一点我推荐用 Record<string, any>：

```typescript
type UppercaseKey<Obj extends Record<string, any>> = { 
    [Key in keyof Obj as Uppercase<Key & string>]: Obj[Key]
}
```

也就是约束类型参数 Obj 为 key 为 string，值为任意类型的索引类型。

### ToReadonly

索引类型的索引可以添加 readonly 的修饰符，代表只读。

那我们就可以实现给索引类型添加 readonly 修饰的高级类型：

```typescript
type ToReadonly<T> =  {
    readonly [Key in keyof T]: T[Key];
}
```
通过映射类型构造了新的索引类型，给索引加上了 readonly 的修饰，其余的保持不变，索引依然为原来的索引 Key in keyof T，值依然为原来的值 T[Key]。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cdf1b5b8ff140a9b1cb1327036a51d1~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAKgewEpQIYBMEDsA2YA8cAfDALwwwDewFFATmprmDANoDSULAlljANZcEAM3gBdAFzwOXMQG5gAX2Arw0GCgzY8KAM4BXHCDLxkjbQWq0YWVAFsoU3SDq8A5guuo3jm-rsARlB0CopEckA)

### ToPartial

同理，索引类型还可以添加可选修饰符：

```typescript
type ToPartial<T> = {
    [Key in keyof T]?: T[Key]
}
```

给索引类型 T 的索引添加了 ? 可选修饰符，其余保持不变。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82e280f3d8c74428a30e4041f85a082f~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAKg9gBQIYCdgEskBsA8MB8UAvFAN4BQUVUA2gNIQhToB2UA1o3AGawC6AfgBcseoz7kAvuXKhIUZGkxYAShADOAVyzBisRKgzYcFalBZIAthBHrgKVgHMA3JWpJHN85ssAjCCiukvjOQA)

### ToMutable

可以添加 readonly 修饰，当然也可以去掉：

```typescript
type ToMutable<T> = {
    -readonly [Key in keyof T]: T[Key]
}
```
给索引类型 T 的每个索引去掉 readonly 的修饰，其余保持不变。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b557f60b928b4016a3478704870d29a7~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAKg9gWQK7AIYCMA2EA8MB8UAvFAN4BQUVUAtAE4SoAmcAdpiFANoDSEnAS1ZQA1vzgAzWAF0AXLF79p5AL7lyoSFGRosEAEoQAzkkzBiVeDozYcFalAbM2HKK1QBbCPKPA6QgHMAbkpqVADvNyQPdAg6EJV8EKA)

### ToRequired

同理，也可以去掉可选修饰符：

```typescript
type ToRequired<T> = {
    [Key in keyof T]-?: T[Key]
}
```
给索引类型 T 的索引去掉 ? 的修饰 ，其余保持不变。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7beee4ca5e524b44a1e9c088eaae4721~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAKg9gJQgRwK4EsBOEAmAeGAPigF4oBvAKChqgG0BpCEKdAOygGtm4AzWALoBaAPwAuWI2YDKAX0qVQkKEjRZcSAM6oANjuClYiFBmz4qtKGwCGAWwjiom4JnYBzANzVa1txAlsqLYARhCYXrKEXkA)

### FilterByValueType

可以在构造新索引类型的时候根据值的类型做下过滤：

```typescript
type FilterByValueType<
    Obj extends Record<string, any>, 
    ValueType
> = {
    [Key in keyof Obj 
        as Obj[Key] extends ValueType ? Key : never]
        : Obj[Key]
}
```
类型参数 Obj 为要处理的索引类型，通过 extends 约束为索引为 string，值为任意类型的索引类型 Record<string, any>。

类型参数 ValueType 为要过滤出的值的类型。

构造新的索引类型，索引为 Obj 的索引，也就是 Key in keyof Obj，但要做一些变换，也就是 as 之后的部分。

如果原来索引的值 Obj[Key] 是 ValueType 类型，索引依然为之前的索引 Key，否则索引设置为 never，never 的索引会在生成新的索引类型时被去掉。

值保持不变，依然为原来索引的值，也就是 Obj[Key]。

这样就达到了过滤索引类型的索引，产生新的索引类型的目的：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c10b0e0b073d4ce19ab89bda1224a331~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAYglgG2BATgIRANQIYIK4QAq4EAPAPIBGAVlBAB7IB2AJgM5QBKEAxgPYoWpNsBRwmAcwA0UbExAA+GTnxESCqAF4oAbwBQUQ1ADaAaQggo4qAGsLfAGZQqtA0ffYOLsxYC6dRghWDhUCYkgoAH4oc0sALigmCAA3VF83d0ME71j0gF89PXFkFAdsHmgABVQ2PiZdDMTsAFsIBJExSQBuRuwJNsS8ZspUHvcACz5KShB20XEJY18egsLQCPgkVG42PCQtWEQSjFC1SFJqlFqmGQ6FqAAfQeHUBS6gA)

## 总结

TypeScript 支持 type、infer、类型参数来保存任意类型，相当于变量的作用。

但其实也不能叫变量，因为它们是不可变的。**想要变化就需要重新构造新的类型，并且可以在构造新类型的过程中对原类型做一些过滤和变换。**

数组、字符串、函数、索引类型等都可以用这种方式对原类型做变换产生新的类型。其中索引类型有专门的语法叫做映射类型，对索引做修改的 as 叫做重映射。

提取和构造这俩是相辅相成的，学完了`模式匹配做提取`，`重新构造做变换` 这两个套路之后，很多类型体操就有思路了。

[本文案例的合并](https://www.typescriptlang.org/play?#code/PTAEgdTQRv0LH+ChZKACgVwM4AtYBcCeAHAU2XQwB4BBAJytEIA9tCA7AEzVFBWYGtmB7AO7MA2gF0ANKACiAG0IA+UAF5QIgHSbqVKXMJiA3PDxESmAEqE0KWdhVnyIgIxSATFIDMk0ABYFRhDAAVWZMAEsAM2wcAmIQ8KjKGjpGFnZObj4hUW89JVURPSlNdW1DY1jQeIxI7EtrW3tq2rJnN09vAAZ-eEQALTD8GNMB-DIAeWZiBiY2DhFMgWEpRezvcewMQloZtPnV5a5eJeYxfNBYTk5J6dS5tTDmCO3QG4AxMKo0bClH59obgBlQgAY34bDElyu0IA-K9Ni9dvcRH8XhstlQPl8fqBUQCEVRgWCIVDoWTQHCRCJ3p9vlJ0dssd9vNSpkTwax6QT2RCxKAAFziC7kkVXflqcqk0Vk4bEUb1Gx2VSjVouVwsgDkAHMUABDZhajVSDWscGGs4BfqDVyy0CjVwTKYpWbpA45LkY517I5ZYTic5Sm5e5F415TJk4kqhm71bCQ0Vwhk7O7pFFPNEEiPFTTRgmx+PSziU1mELPwjER7wle2Owixj3bWMKMTi8RSwucVuSkxy60KxrK62qiTuDwSHwSACsmp1+sNxtNBqNoA1YTQy41ACMrNgNxEqGE0hqLb0wIB1bUAZN6AJjk4IFQABhXX4MLYXWyMIAL0IgOwVFtj+fV93y-H8qDIUDg3Sb4DwNc4IKRdIAAMABIAG9QwjABfNDQ1jTDEIpUAUNQoJ8CIKgQV1NBCDICMFGw1C8II8VQICHsHyfF830-OsrEVewAK44Dv1-MhtT1JcejvR8AFtCFkR9qP-XU5IUqiaPglMOGgx4tQDaFNJdDhiNDAAZQgokwgB9HD01ocwwi1DBsAY3Cd3w9srjhYjzMstDSPIyjqLIBynOwei0Nk+TFJopsPNFFjfzYyoorU6j+yVDjVJisTFy1Ky8oKs0NSkxAABEqH4fBARQTdQNtCqqpqurRMM70dINKRmra+4Or0+wpR6pDbP+ZAqAssJ6AY7rf1cuzQBqiIIkm-DhRFOFGuq2rQLIYikHG5aprQxbDvwrrtt-JREqoZLTE2jL7E2mawJNM0AD8Po3N6SstMBAF-FcBT1ACgyLSagdTk5honYkGiDYcGUEh7BaO4EFII4N5UewMJwSkcH9KuTHmDRhCOAAChKXUqC1NBxVDcG0AAShUJQ3OwFAqGYAAVSpPKLUAKc0KmadbEoGbx6mxGZ5QlEsdnOZ50xxSmAA3bZbuIWGwepxGWDqPjGnsLX4Z1pGyDJ5gVMIcU+ulpRN34fh5H1KRmER7cqFKsBACJfQBUfUAbx9AGj1IGAFkn2fA1bTDsjdImTcACt0dAfgE9BcL7FQtbOBEABpQhcFxZhQB4fP+AiV4E5bNRxgT3P8-WWu89wBv47r5vIUwipTHGjhVGjiOtTITPdXFFxQE3cVXEwr2qlBij1Kb20Au2ILCCbuPE9J5PU5BdPVEzqU28L4vS-LmvE6o2fAvUsgm9AAAyUA+ubcVz7bjuu7iOfV6bh7VGX+e1F16Z1nAaUeUg8qT2nr9UAXN+CWF1IuWQuBbRwIQUg3AZAubnFAKhKU41EHgmQWoO+jwT64DLrAquXN35GE7radBRDcB-1gfAwghDmDIKHlKS2ckba-l0kYaEuotTW1AG7GSHs6EzzgUgKm2M3yoP4HIqgCjZBYPOHg6ER8yElwoeXLmYgYTihoU3D+toVFqJYbI+RYQ3zcOhLwsRfUhFXBEWIiRUjYDQKBnAkOKBXybnkEo-xgT5AaIzlKAAtAQjBJD87Hz0ZQwxJj37eM-qAUJuogm8QaJlVhWSckOKuLEph4irb8JglqVxnB3HK3durbxMi2EAEcUCfEIKwJRlg2kdNYBE-eh9SFFySQYsQUTjGwLSfQ9iPT2njVYP2AcrC5l9OKZwJxkyXFSjqeIhpN0mkwI+LYbYAAhXAAA1N8KBCCK0ILaY5TAqDnKubIG5dyN5J0sGCKg-S+pSH1LgBQUhXnvNiJooZCTdGnwronPmoBL5vzMUnUFtzKhwjvsrQgasqAFnJK-Ru9d0mwEeE8iIuoQTECQNsNA4JcE8IqU-ARBoakItEfUyRjToQYBTpuXAlTdLiDoRkx5jYDaZVFc8y51y0VEDINSr4uMmVVNAAAHz2Zyz2BggA)






## 7.套路三：递归复用做循环

会做类型的提取和构造之后，我们已经能写出很多类型编程逻辑了，但是有时候提取或构造的数组元素个数不确定、字符串长度不确定、对象层数不确定。这时候怎么办呢？

其实前面的案例我们已经涉及到了一些，就是递归。

这就是第三个类型体操套路：递归复用做循环。

## 递归复用

**递归是把问题分解为一系列相似的小问题，通过函数不断调用自身来解决这一个个小问题，直到满足结束条件，就完成了问题的求解。**

TypeScript 的高级类型支持类型参数，可以做各种类型运算逻辑，返回新的类型，和函数调用是对应的，自然也支持递归。

**TypeScript 类型系统不支持循环，但支持递归。当处理数量（个数、长度、层数）不固定的类型的时候，可以只处理一个类型，然后递归的调用自身处理下一个类型，直到结束条件也就是所有的类型都处理完了，就完成了不确定数量的类型编程，达到循环的效果。**

既然提到了数组、字符串、对象等类型，那么我们就来看一下这些类型的递归案例吧。

## Promise 的递归复用

### DeepPromiseValueType

先用 Promise 热热身，实现一个提取不确定层数的 Promise 中的 value 类型的高级类型。

```typescript
type ttt = Promise<Promise<Promise<Record<string, any>>>>;
```

这里是 3 层 Promise，value 类型是索引类型。

数量不确定，一涉及到这个就要想到用递归来做，每次只处理一层的提取，然后剩下的到下次递归做，直到结束条件。

所以高级类型是这样的：
```typescript
type DeepPromiseValueType<P extends Promise<unknown>> =
    P extends Promise<infer ValueType> 
        ? ValueType extends Promise<unknown>
            ? DeepPromiseValueType<ValueType>
            : ValueType
        : never;
```

类型参数 P 是待处理的 Promise，通过 extends 约束为 Promise 类型，value 类型不确定，设为 unknown。

每次只处理一个类型的提取，也就是通过模式匹配提取出 value 的类型到 infer 声明的局部变量 ValueType 中。

然后判断如果 ValueType 依然是 Promise类型，就递归处理。

结束条件就是 ValueType 不为 Promise 类型，那就处理完了所有的层数，返回这时的 ValueType。

这样，我们就提取到了最里层的 Promise 的 value 类型，也就是索引类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/518c10e2128b444f88711904e725aab5~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAIhFgAoCcD2BbAlgZwgNQEMAbAVwgBVwIAeRKCAD2AgDsATbKFDHGklgNYtUAdxYA+cVAC8AKCgKu9Jqw5c0WXNUwsAZhGRRCpClSnzFlgPxHiZSpGXN2nbpr6DhY8Rct+oNnAIbrzG9lTUYaaQPv7+AFy2Jg4Qvn6JLBAAbgYA3LKyoI5BSBq8AEoQ2CREwDKw8KU8uFEptGVaIVqVAMaoyGzU2MDIOgDmADRQBCwgkpK5QA)

其实这个类型的实现可以进一步的简化：

```typescript
type DeepPromiseValueType2<T> = 
    T extends Promise<infer ValueType> 
        ? DeepPromiseValueType2<ValueType>
        : T;
```
不再约束类型参数必须是 Promise，这样就可以少一层判断。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e24a07fc579647ff9d974943af1626fc~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAIhFgAoCcD2BbAlgZwgNQEMAbAVwgBVwIAeRKCAD2AgDsATbKFDHGklgNYtUAdxYA+cVAC8AKCgKu9Jqw5c0WXNUwsAZhGRRCpClSnzFlgPxHiZSpGXN2nbpr6DhY8Rct+oNnAIbrzG9lTUYaaQPv7+AFy2Jg4Qvn6JLBAAbgYA3LKyoI5BSBq8AEoQ2CREwDKw8KU8uFEptGVaIVqVAMaoyGzU2MDIOgDmADRQBCwgkpL5hVQNwR34dtEQAEzU5FLSUGnkTqqua9p6BknhMYdxAStN7q1UOy8xaZaJ5ItF0CVddbJV6VTgHAFrd7bdrNGiAmHuagsEjoABGBnm4nyQA)

接下来再看下数组类型的递归复用：

## 数组类型的递归

### ReverseArr
有这样一个元组类型：

```typescript
type arr = [1,2,3,4,5];
```

我们把它反过来，也就是变成：
```typescript
type arr = [5,4,3,2,1];
```
这个学完了提取和构造很容易写出来：

```typescript
type ReverseArr<Arr extends unknown[]> = 
    Arr extends [infer One, infer Two, infer Three, infer Four, infer Five]
        ? [Five, Four, Three, Two, One]
        : never;
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d67c9c3c77f04234919e17730a1c8d67~tplv-k3u1fbpfcp-watermark.image?)

但如果数组长度不确定呢？

数量不确定，条件反射的就要想到递归。

我们每次只处理一个类型，剩下的递归做，直到满足结束条件。

```typescript
type ReverseArr<Arr extends unknown[]> = 
    Arr extends [infer First, ...infer Rest] 
        ? [...ReverseArr<Rest>, First] 
        : Arr;
```

类型参数 Arr 为待处理的数组类型，元素类型不确定，也就是 unknown。

每次只处理一个元素的提取，放到 infer 声明的局部变量 First 里，剩下的放到 Rest 里。

用 First 作为最后一个元素构造新数组，其余元素递归的取。

结束条件就是取完所有的元素，也就是不再满足模式匹配的条件，这时候就返回 Arr。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1caebf3f4c9e41198dfaac48f35bcd56~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAShBuEBOBnCBBJSA8mlQgA9gIA7AExSgFdSBrUgewHdSBtAXQD4oBeKAFBRhUPAWJlKUNgEtSAM2RQAYjNTAANFAB0uuYvxwUwDoJHmoAfmm7tcRKgxZsR4Fy2r1poReEAuUSwAbgEBUEhYBGQ0PCNqABtgPkiHGOc2AEYNACYNAGYNABYNAFZuIKA)

### Includes

既然递归可以做循环用，那么像查找元素这种自然也就可以实现。

比如查找 [1, 2, 3, 4, 5] 中是否存在 4，是就返回 true，否则返回 false。

从长度不固定的数组中查找某个元素，数量不确定，这时候就应该想到递归。

```typescript
type Includes<Arr extends unknown[], FindItem> = 
    Arr extends [infer First, ...infer Rest]
        ? IsEqual<First, FindItem> extends true
            ? true
            : Includes<Rest, FindItem>
        : false;

type IsEqual<A, B> = (A extends B ? true : false) & (B extends A ? true : false);
```

类型参数 Arr 是待查找的数组类型，元素类型任意，也就是 unknown。FindItem 待查找的元素类型。

每次提取一个元素到 infer 声明的局部变量 First 中，剩余的放到局部变量 Rest。

判断 First 是否是要查找的元素，也就是和 FindItem 相等，是的话就返回 true，否则继续递归判断下一个元素。

直到结束条件也就是提取不出下一个元素，这时返回 false。

相等的判断就是 A 是 B 的子类型并且 B 也是 A 的子类型，。

这样就完成了不确定长度的数组中的元素查找，用递归实现了循环。

当包含时：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d3068162fb34b41840be24c55f94dbd~tplv-k3u1fbpfcp-watermark.image?)

当不包含时：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd8609a747bd462db18c2b3aa35294e4~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAkgOwMYBsCuATKBnAPAQQCdCYoAPEKBDbGNBAawQHsB3BAbQF0AaGAMQCW1OJQC2APhgBeGMBgKYREuUrVaHYQDMoJIYWwg+AOlPbdMAEo4QXeYocB+eNgCiARzQBDFLn2G+IRFxKVUqGhgQQjQoewd4mGcomLiExQAueGR0LDxrAIFhDFEoSVSHTK0fbCgAbmBQSFg4N08fAj4AISlZAAp8Ugpw2k7EyOjYSuqoAEoYADIYXtGw9SUx5MmYKpQamfrG6CzUTBx8tBQQGWOcnFwOAEY+ACY+AGY+ABY+AFZeGE+EgO4COiBOuXOl2e1zBtzwjxe7y+v3+ADYgUA)

### RemoveItem

可以查找自然就可以删除，只需要改下返回结果，构造一个新的数组返回。

```typescript
type RemoveItem<
    Arr extends unknown[], 
    Item, 
    Result extends unknown[] = []
> = Arr extends [infer First, ...infer Rest]
        ? IsEqual<First, Item> extends true
            ? RemoveItem<Rest, Item, Result>
            : RemoveItem<Rest, Item, [...Result, First]>
        : Result;
        
type IsEqual<A, B> = (A extends B ? true : false) & (B extends A ? true : false);
```

类型参数 Arr 是待处理的数组，元素类型任意，也就是 unknown[]。类型参数 Item 为待查找的元素类型。类型参数 Result 是构造出的新数组，默认值是 []。

通过模式匹配提取数组中的一个元素的类型，如果是 Item 类型的话就删除，也就是不放入构造的新数组，直接返回之前的 Result。

否则放入构造的新数组，也就是再构造一个新的数组 [...Result, First]。

直到模式匹配不再满足，也就是处理完了所有的元素，返回这时候的 Result。

这样我们就完成了不确定元素个数的数组的某个元素的删除：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eef06834cb424514b8783823b5b02642~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAShC2B7AbhAksBAeAggJzyggA9MA7AEwGcoBXMgazMQHcyBtAXQBooMFecKrQA2wIqQiUa9Jqw6coAXihcAfMqgAoKLqj5CJctVUBLMgDMIhAGKm8VYLwB0r81cJDgnHXr8B+PioAUQBHWgBDESw7Byc+THgNIykTYDxaCF8-HKhAuCRUfngsL15iwQhhMTVs3L0ALlgEFHRE0qr4itVXZyFReNjHTlr6qCb+sQBuLS1QSCCwyOicXgAhDRUAChwJYxo1vKh0zPGoCyiqCABKKAAyKC3DlOl9I5PoJouRK+uZufA0AKrWKk3EKmBRXa7AAjNwAEwI7gAZh4UHhaimQA)

### BuildArray

我们学过数组类型的构造，如果构造的数组类型元素个数不确定，也需要递归。

比如传入 5 和元素类型，构造一个长度为 5 的该元素类型构成的数组。

```typescript
type BuildArray<
    Length extends number, 
    Ele = unknown, 
    Arr extends unknown[] = []
> = Arr['length'] extends Length 
        ? Arr 
        : BuildArray<Length, Ele, [...Arr, Ele]>;
```

类型参数 Length 为数组长度，约束为 number。类型参数 Ele 为元素类型，默认值为 unknown。类型参数 Arr 为构造出的数组，默认值是 []。

每次判断下 Arr 的长度是否到了 Length，是的话就返回 Arr，否则在 Arr 上加一个元素，然后递归构造。

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00049e632bbf4707b879cbd062fe0762~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAQgVwJYBsAmBBATlghmAHgBkoA7AcxAAsYoAPEMtAZxlIQFsAjKLAGhjAYwmAFEUsALwwEpANakA9gHdSAoSOxZaDJq1kKVpANoBdGNLMA+CxuFbjAcgkVqj8-UakWMEq5p2IsIA-DBagkFBAFzwyOha+MRklFQC4lACxgB0OVppEqZWANzAoJCwiKiYOABKUMwIKCAWsVUJhACsxUA)

学完了数组类型的递归，我们再来看下字符串类型。

## 字符串类型的递归

### ReplaceAll

学模式匹配的时候，我们实现过一个 Replace 的高级类型：

```typescript
type ReplaceStr<
    Str extends string,
    From extends string,
    To extends string
> = Str extends `${infer Prefix}${From}${infer Suffix}` 
    ? `${Prefix}${To}${Suffix}` : Str;
```

它能把一个字符串中的某个字符替换成另一个：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5e1e3328db5470b9d759eb194b66b9c~tplv-k3u1fbpfcp-watermark.image?)

但是如果有多个这样的字符就处理不了了。

如果不确定有多少个 From 字符，怎么处理呢？

**在类型体操里，遇到数量不确定的问题，就要条件反射的想到递归。**

每次递归只处理一个类型，这部分我们已经实现了，那么加上递归的调用就可以。

```typescript
type ReplaceAll<
    Str extends string, 
    From extends string, 
    To extends string
> = Str extends `${infer Left}${From}${infer Right}`
        ? `${Left}${To}${ReplaceAll<Right, From, To>}`
        : Str;
```
类型参数 Str 是待处理的字符串类型，From 是待替换的字符，To 是替换到的字符。

通过模式匹配提取 From 左右的字符串到 infer 声明的局部变量 Left 和 Right 里。

用 Left 和 To 构造新的字符串，剩余的 Right 部分继续递归的替换。

结束条件是不再满足模式匹配，也就是没有要替换的元素，这时就直接返回字符串 Str。

这样就实现了任意数量的字符串替换：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f7e0390108248b7babfe8115c59ad47~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FDAuE8AcFMAICVqQDYEMDG0CCzkB4BlUAJ1mgA9RoA7AEwGdZ6SBLagcwBpZhY-YAYsQD2AWzKUaDJqw7de-ACrCJVOo2bE27AHywAvD37HYRUhTXSABgBIA3mwBm0UgBloj0AF97QsT4dqZ1J4FnYAC28rBRMTAH5YWzt3TwDlAMQUDGxcPFCI0G4-UW5lHS9o2NiALlMSAG4QCBgEJDRMHGREegBXZFADVqyO3IBydh7UDlgJqfYZyY5R7nHF9mXYUdphJZ16oA)

### StringToUnion

我们想把字符串字面量类型的每个字符都提取出来组成联合类型，也就是把 'dong' 转为 'd' | 'o' | 'n' | 'g'。

怎么做呢？

很明显也是提取和构造：

```typescript
type StringToUnion<Str extends string> = 
    Str extends `${infer One}${infer Two}${infer Three}${infer Four}`
        ? One | Two | Three | Four
        : never;
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb1071c2ee7f45368ad816f7179a92a3~tplv-k3u1fbpfcp-watermark.image?)

但如果字符串长度不确定呢？

数量不确定，在类型体操中就要条件反射的想到递归。

```typescript
type StringToUnion<Str extends string> = 
    Str extends `${infer First}${infer Rest}`
        ? First | StringToUnion<Rest>
        : never;
```

类型参数 Str 为待处理的字符串类型，通过 extends 约束为 string。

通过模式匹配提取第一个字符到 infer 声明的局部变量 First，其余的字符放到局部变量 Rest。

用 First 构造联合类型，剩余的元素递归的取。

这样就完成了不确定长度的字符串的提取和联合类型的构造：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e2e1688af304c16b5ed60af0b335e3a~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAysBOBLAdgcwCoHsCqzGeQB454oIAPYCZAEwGco6EVUA+KAXigCgo-YEZStXpQABgBIA3igBmEUgDFE8JgF9pchVABKEdWN79jAfijLVwKAB8BSNFlz4iepqyPG+ALijIIANwUAbm5Q0Eg7Fkc8AlcAVwAbKy4SKJwYogByAAsIBITMTNYQoA)

### ReverseStr

我们实现了数组的反转，自然也可以实现字符串类型的反转。

同样是递归提取和构造。

```typescript
type ReverseStr<
    Str extends string, 
    Result extends string = ''
> = Str extends `${infer First}${infer Rest}` 
    ? ReverseStr<Rest, `${First}${Result}`> 
    : Result;
```
类型参数 Str 为待处理的字符串。类型参数 Result 为构造出的字符，默认值是空串。

通过模式匹配提取第一个字符到 infer 声明的局部变量 First，其余字符放到 Rest。

用 First 和之前的 Result 构造成新的字符串，把 First 放到前面，因为递归是从左到右处理，那么不断往前插就是把右边的放到了左边，完成了反转的效果。

直到模式匹配不满足，就处理完了所有的字符。

这样就完成了字符串的反转：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c366b28c97c54473a8210ce4f8da0919~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBASlAblATgZygZRCgPNlGKADxCgDsATNGNHAS3IHMAaGYGT+KNAVwBsQRUhWq0GzGAF4YAclkA+aey4wCwslRoADACQBvRgDNUMAGL10IAL4HjphHWvaVqrgH5uydFhy5HIGx6+hZWtvqOAjbaShxunABc3HyCANzAoJCwCN4YBJGCyjmoeX6yABZQ-PwA9oqpQA)

学完了字符串的递归，我们再来看下对象的。

## 对象类型的递归

### DeepReadonly

对象类型的递归，也可以叫做索引类型的递归。

我们之前实现了索引类型的映射，给索引加上了 readonly 的修饰：

```typescript
type ToReadonly<T> =  {
    readonly [Key in keyof T]: T[Key];
}
```

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/040460cc07e0448cb1cefa224515d708~tplv-k3u1fbpfcp-watermark.image?)

如果这个索引类型层数不确定呢？

比如这样：

```typescript
type obj = {
    a: {
        b: {
            c: {
                f: () => 'dong',
                d: {
                    e: {
                        guang: string
                    }
                }
            }
        }
    }
}
```
数量（层数）不确定，类型体操中应该自然的想到递归。

我们在之前的映射上加入递归的逻辑：

```typescript
type DeepReadonly<Obj extends Record<string, any>> = {
    readonly [Key in keyof Obj]:
        Obj[Key] extends object
            ? Obj[Key] extends Function
                ? Obj[Key] 
                : DeepReadonly<Obj[Key]>
            : Obj[Key]
}
```
类型参数 Obj 是待处理的索引类型，约束为 Record<string, any>，也就是索引为 string，值为任意类型的索引类型。

索引映射自之前的索引，也就是 Key in keyof Obj，只不过加上了 readonly 的修饰。

值要做下判断，如果是 object 类型并且还是 Function，那么就直接取之前的值 Obj[Key]。

如果是 object 类型但不是 Function，那就是说也是一个索引类型，就递归处理 DeepReadonly<Obj[Key]>。

否则，值不是 object 就直接返回之前的值 Obj[Key]。

这样就完成了任意层数的索引类型的添加 readonly 修饰：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03730514e65a409ba6ad49473cfbd0b0~tplv-k3u1fbpfcp-watermark.image?)

我们取处理以后的索引 a 的值看一下，发现 b 已经加上了 readonly 修饰。

测试一下：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e9b45c558b344b8bc28356e05b830c1~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAIhFgEoQIYBMD2A7ANiAPAPIBGAVlBAB7ARZoDOUyAxhgE5r73BsCWWAcwA0UFFhAA+CVAC8UAN4AoKCqhtUmXCCgBtANIRt-KAGtDGAGZQSpALoAuZauc39h2xWq0GUDGQjMwE7OIVAA-NZkbiAeVDR0jABiAK5YgbzYwaHZEa4GMVBZ2SH2sPBIGth4RFH5thJF2aV57ooAvoqKoJC+ZLIKWSilSsXEw42hzOPFxRalABQAlLLSAOSaAqtCEzNo0zMHEPsHJ1ACyWICpdx8gjunHafOjycvoW9QHR1d4NBwCMh0FUQMh6MkcMB+v8KkCtPg-KQJDpVihVrYANydbp-cqAzR4UHg4AAJihuMqcIRSJRaORxFpq2YaMxQA)

为啥这里没有计算呀？

因为 ts 的类型只有被用到的时候才会做计算。

所以可以在前面加上一段 Obj extends never ? never 或者 Obj extends any 等，从而触发计算：

```typescript
type DeepReadonly<Obj extends Record<string, any>> =
    Obj extends any
        ? {
            readonly [Key in keyof Obj]:
                Obj[Key] extends object
                    ? Obj[Key] extends Function
                        ? Obj[Key] 
                        : DeepReadonly<Obj[Key]>
                    : Obj[Key]
        }
        : never;
```

这样就显示了计算后的类型：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03051aaaca3b4eed8cbf822ab7882a39~tplv-k3u1fbpfcp-watermark.image?)

而且写 Obj extends any 还有额外的好处就是能处理联合类型，这个可以看套路五，会有解释。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAIhFgEoQIYBMD2A7ANiAPAPIBGAVlBAB7ARZoDOUyAxhgE5r73BsCWWAcwA0UFFhAA+CVAC8AKCiKoJclRp1GYkAqW6A-FADeO3aahtUmXCCgBtANIQb-KAGsnGAGbKyAXQBcJmbBKg5OvhTUtAxQGGQQzMBBwSlQBqGOIBFq0YwAYgCuWIm82MmpFelkYVlQ5RUp-rDwSJbYeETVmb4S9Q2KTRnhfQC+fU1YEABuEGwA3HJyoJCxZLJGQShNxinE2326zPv9up5NABQAlLLSAORWArdCB8FoxydmEO8fKQIFYgImtw+IIXhUxj8oBCGtCzLCoXIxktwNA4AhkOh2iBkPQCjhgOs0a1MdZ8HFSBI5kA)

## 总结

递归是把问题分解成一个个子问题，通过解决一个个子问题来解决整个问题。形式是不断的调用函数自身，直到满足结束条件。

在 TypeScript 类型系统中的高级类型也同样支持递归，**在类型体操中，遇到数量不确定的问题，要条件反射的想到递归。** 比如数组长度不确定、字符串长度不确定、索引类型层数不确定等。

如果说学完了提取和构造可以做一些基础的类型体操，那再加上递归就可以实现各种复杂类型体操了。

[本文案例的合并](https://www.typescriptlang.org/play?#code/PTAEAUCcHsFsEsDOBTAXAKHSUARZyAHKOJZANQEMAbAV2QBUBPAtdAF2eV3yJgRUq0GnADzhQyAB5tkAOwAmiCH1IiasgNazoAd1kA+faAC86UOYgTpcxcpIoR8WQDNkkUILpMWRsxf8A-B7UXpxWMgpKxPzIapraevp+-imgQXiE0aSewiwiOd7ISampqMFChckpZbLIAG5uANyYHCzcmSooAErIiDRUbCbtvPbkIbmxWQ5TsT0AxtCQ8iKIbJBOAOYANKAUsoyGhs1YYBkjMQWcAEzsYWczlyxXIvRGxqBV9OE2UZ2xTq53I8ih8Smlhg9xoVnsDiiUyvRjq0uPc-sCrj0lO9UaN0WI-vjRoSYiJZDRYAAjNyHfTHbCAB1NACN+gCx-zDYHoNSAoACCkEgGGRoA5bh5fJEvPcUgitnUWl0sgA2gBdN6giwS76RUAKgFuUAAMXgXLYOwAdObde5MWwlWrUkEFebTcKucgJSJrfodobjbaqv4yhKkWEXaLIJj+oN3qG3WKFQBGLZXLYAZi2ABYtgBWFV0sAASVkc1o8l6tzaheLNFLiHFfM1Mvi8uV3qc8nzMlgqqqGqlP21loNRtWZotLj11qV-osQXziAAogBHGjUEQ+kdDhQd5BdhtKNZ0af20AH5BH6qgSsl3oe3omzftztw0qgZzUFDBisL5er7k7ABCqoABTcnuoD-uCp6gGUb5UCgACUoAAGSgEBEF9lqoFBFBMHvsg8GflwV7Vr0EYDEMxE1iICY7MmoBpqAmagDmOzprSLRhJRpG9JGVwUUW161jRoB0QxTEsaAABs7EnEKO7QA026wOWXA9LACnIEpdaStYWqygkipKjsSk7GRgwYY2cp6MqQzKt2-i9rptg6uO7jrveTqDpO56zt+K5UGuw73kpRgWfukCHmCgRyepimdreG4mXJfQDM+UVlGpGladaxmdjsjrmmZra+mlAbJZGhExVlnZmUMmVxTu1GJsmyYpkZIkydg-40PAVDyBKFCMCp4E9X1A2MCIAAycgbGwAAWYFkpSbg7FU85UFw7z6fKq0OfWYWgNt1m2u8dkmD2fIKgA5BtsizXNV22gd013fNdopEEGrnmU3W9f1fKDVNM3zTs63IPlToSqDG25hxbS-WNfK1e8CP-ZAgNZp1YCAOragBk3oATHKAN4+gDR6myYA9AQVAUHMbpUFQw0U1TNPcnTIgAMprGBqzrHdu0WPqfBc2smx8+Y9DQELPMbPZJQczp0pKAABgAJAA3oO03OGwAC+asC3Auvq65QrwBsc064r57RSrquazravi4bjPU7TAVdKb5venwOzi-o2uW1FFhlHLlXO8zdPI3JlMuyzAVXRsK53aACd7BsyeJxsV07PHGdZ6AV3yNAd1XVjoBy5s4sAKqyPARfDeXd1VzXRfs5zB3c5sMvmHLYE24O7mG15d7+z5Q7GqAAA+ZfC430DV7XsgJWwpVB6AtScsc9czxsTcL5HDc73PzeL1dc3IHT0Al3mcmcigcsM-UIrIHLrfy-2He8+9tXt9vQxXSXQwqg9wOn3Y2A81ZD1WP7d60UYwvxyqAG24DVZmX9r4MEGUeIDFDo-V0ctI5wLWCIU+58qCX1LoAIl9ACo+iTVkskzg9AoIXWQVAhrDQYcgJhRdWEiAAPIUgAFZgXmIsZYH9ti7H2IYc6-h+FCIOnsIaYIgiqythYSAnDmGsO1AAaWQIwUAThQAaH0dAZwoA5FKgwIHVIciFR6MYE9JyShoCCOQHMNgajA5BDsQ4pxCsDTqA8QvLxNjzA+MEfY-RfowlhLKBwrhLCJq+OiSvWJ0ELGRL8eebW30164Mqq4oR7xVH+AoGUUpJQKQVNCXMGp6TzDODKEBRCxgjAFyLpnLYoT-DyHqQ0-waBQCVIGakFOd0yjiJ6SUXJAzZk2PmakRZoBcm5PYTwRhWjGCRwSVskQRT2JAA)

(其实这节的 IsEqual 判断是不完善的，套路六里面会讲原因)



## 8.套路四：数组长度做计数

类型系统不是图灵完备，各种逻辑都能写么，但好像没发现数值相关的逻辑。

没错，数值相关的逻辑比较绕，被我单独摘了出来，就是这节要讲的内容。

这是类型体操的第四个套路：数组长度做计数。

## 数组长度做计数

TypeScript 类型系统没有加减乘除运算符，怎么做数值运算呢？

不知道大家有没有注意到数组类型取 length 就是数值。

比如：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87dd9ef8842f4c7bb02f4250c00105be~tplv-k3u1fbpfcp-watermark.image?)

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/27952090670b41868c7af26a2503a40f~tplv-k3u1fbpfcp-watermark.image?)

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47a0951774f1492c9fa9519199286266~tplv-k3u1fbpfcp-watermark.image?)


而数组类型我们是能构造出来的，那么通过构造不同长度的数组然后取 length，不就是数值的运算么？

**TypeScript 类型系统中没有加减乘除运算符，但是可以通过构造不同的数组然后取 length 的方式来完成数值计算，把数值的加减乘除转化为对数组的提取和构造。**

(严格来说构造的是元组，大家知道数组和元组的区别就行)

这点可以说是类型体操中最麻烦的一个点，需要思维做一些转换，绕过这个弯来。

下面我们就来做一些真实的案例来掌握它吧。

## 数组长度实现加减乘除

### Add

我们知道了数值计算要转换为对数组类型的操作，那么加法的实现很容易想到：

构造两个数组，然后合并成一个，取 length。

比如 3 + 2，就是构造一个长度为 3 的数组类型，再构造一个长度为 2 的数组类型，然后合并成一个数组，取 length。

构造多长的数组是不确定的，需要递归构造，这个我们实现过：

```typescript
type BuildArray<
    Length extends number, 
    Ele = unknown, 
    Arr extends unknown[] = []
> = Arr['length'] extends Length 
        ? Arr 
        : BuildArray<Length, Ele, [...Arr, Ele]>;
```

类型参数 Length 是要构造的数组的长度。类型参数 Ele 是数组元素，默认为 unknown。类型参数 Arr 为构造出的数组，默认是 []。

如果 Arr 的长度到达了 Length，就返回构造出的 Arr，否则继续递归构造。

构造数组实现了，那么基于它就能实现加法：

```typescript
type Add<Num1 extends number, Num2 extends number> = 
    [...BuildArray<Num1>,...BuildArray<Num2>]['length'];
```

我们拿大一点的数测试下：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aff4bf817a464261951540341c3a8e33~tplv-k3u1fbpfcp-watermark.image?)

结果是对的。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgrgSwDYBMCCAnDBDEAeAKCmKgBkIA7Ac2AAsoIAPYSlAZygrgFsAjCDABooREgFEk0ALxQ4FANYUA9gHcKw0cUwYGzVhzmLVFANoBdKDPMEAfJajaTAcknU6Ti0xYV2ZSjXpNEmIAfgcsEWDggC5YRFRtXDxyN1phCQhhEwA6XO10yTMbAG4CMtBIBxQUPAA5HgBGXW9fLj4BYXruACZm-U4efgw7GSCc3PhkdCwkroabQVzsyYSZ-C7umzNnVwCPUvLwaDRqgCUINjgkYHsTmoBmbuFugFYSoA)

就这样，我们通过构造一定长度的数组取 length 的方式实现了加法运算。

### Subtract

加法是构造数组，那减法怎么做呢？

减法是从数值中去掉一部分，很容易想到可以通过数组类型的提取来做。

比如 3 是 [unknown, unknown, unknown] 的数组类型，提取出 2 个元素之后，剩下的数组再取 length 就是 1。

所以减法的实现是这样的：

```typescript
type Subtract<Num1 extends number, Num2 extends number> = 
    BuildArray<Num1> extends [...arr1: BuildArray<Num2>, ...arr2: infer Rest]
        ? Rest['length']
        : never;
```

类型参数 Num1、Num2 分别是被减数和减数，通过 extends 约束为 number。

构造 Num1 长度的数组，通过模式匹配提取出 Num2 长度个元素，剩下的放到 infer 声明的局部变量 Rest 里。

取 Rest 的长度返回，就是减法的结果。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87bcd660f6b24b5dbd93df016e4588ef~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgrgSwDYBMCCAnDBDEAeAKCmKgBkIA7Ac2AAsoIAPYSlAZygrgFsAjCDABooREgFEk0ALxQ4FANYUA9gHcKw0cUwYGzVhzmLVFANoBdKDPMEAfJajaTAcknU6Ti0xYV2ZSjXpNEmIAfgcsEWDggC5YRFRtXDxyN1phCQhhEwA6XO10yTMbAG4CAlBIKABlOF5gHABjYDwAOR4ARl1vXy4+AWE27gAmLv1OHn4MOxkg+GR0LCTB9rsvMZzc7Cx22LmExfxBoZthXOytjCHYhAoAMwEoACUINmAzIOCw59fnVwCPD4kWIUCAANwEpTKFWgNTqjWA3zgSGA9lh9WwTTwAGYscJ2sdSkA)

就这样，我们通过数组类型的提取实现了减法运算。

有同学可能会问，后面那部分需要 infer 提取，所以起个 arr2 的名字没问题。前面那部分不需要名字呀，可以去掉 arr1 么？

试一下就知道了：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1170d6d8c48e4be8b7776cfe77bb9902~tplv-k3u1fbpfcp-watermark.image?)

报错显示元组成员或者全部有名字，或者全部没有。

### Multiply

我们把加法转换为了数组构造，把减法转换为了数组提取。那乘法怎么做呢？

为了解释乘法，我去翻了下小学教材，找到了这样一张图：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0292cd57da6a447b8b6666efb00177a5~tplv-k3u1fbpfcp-watermark.image?)

1 乘以 5 就相当于 1 + 1 + 1 + 1 + 1，也就是说乘法就是多个加法结果的累加。

那么我们在加法的基础上，多加一个参数来传递中间结果的数组，算完之后再取一次 length 就能实现乘法：

```typescript
type Mutiply<
    Num1 extends number,
    Num2 extends number,
    ResultArr extends unknown[] = []
> = Num2 extends 0 ? ResultArr['length']
        : Mutiply<Num1, Subtract<Num2, 1>, [...BuildArray<Num1>, ...ResultArr]>;
```
类型参数 Num1 和 Num2 分别是被加数和加数。

因为乘法是多个加法结果的累加，我们加了一个类型参数 ResultArr 来保存中间结果，默认值是 []，相当于从 0 开始加。

每加一次就把 Num2 减一，直到 Num2 为 0，就代表加完了。

加的过程就是往 ResultArr 数组中放 Num1 个元素。

这样递归的进行累加，也就是递归的往 ResultArr 中放元素。

最后取 ResultArr 的 length 就是乘法的结果。

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb2656f0fdc647c884405a5324d9fb2a~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgrgSwDYBMCCAnDBDEAeAKCmKgBkIA7Ac2AAsoIAPYSlAZygrgFsAjCDABooREgFEk0ALxQ4FANYUA9gHcKw0cUwYGzVhzmLVFANoBdKDPMEAfJajaTAcknU6Ti0xYV2ZSjXpNEmIAfgcsEWDggC5YRFRtXDxyN1phCQhhEwA6XO10yTMbAG4CAlBIKABlOF5gHABjYDwAOR4ARl1vXy4+AWE27gAmLv1OHn4MOxkg+GR0LCTB9rsvMZzc7Cx22LmExfxBoZthXOytjCHYhAoAMwEoACUINmAzIOCw59fnVwCPD4kWIUCAANwEpXK4GgAFk4MAEGAkIcOqMfBxepMBjwRmt0eM+kIni84EhgGjfIZlGpzPZzNMgkcKRwAAxQL4ksm-fzud5RIFQOEIpEo7jtYQ1OqNZpHYQrLJnPYLHCi+VQM7fUlvEplMoVWHwxHIzVk+xCo34ADMwiGtpKQA)

就这样，我们通过递归的累加实现了乘法。
### Divide

乘法是递归的累加，那除法不就是递归的累减么？

我再去翻了下小学教材，找到了这样一张图：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/645f92b42eed457d9c3f65fc2e8ce24e~tplv-k3u1fbpfcp-watermark.image?)

我们有 9 个苹果，分给美羊羊 3 个，分给懒羊羊 3 个，分给沸羊羊 3 个，最后剩下 0 个。所以 9 / 3 = 3。

所以，除法的实现就是被减数不断减去减数，直到减为 0，记录减了几次就是结果。

也就是这样的：

```typescript
type Divide<
    Num1 extends number,
    Num2 extends number,
    CountArr extends unknown[] = []
> = Num1 extends 0 ? CountArr['length']
        : Divide<Subtract<Num1, Num2>, Num2, [unknown, ...CountArr]>;
```
类型参数 Num1 和 Num2 分别是被减数和减数。

类型参数 CountArr 是用来记录减了几次的累加数组。

如果 Num1 减到了 0 ，那么这时候减了几次就是除法结果，也就是 CountArr['length']。

否则继续递归的减，让 Num1 减去 Num2，并且 CountArr 多加一个元素代表又减了一次。

这样就实现了除法：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ebd7f21f2ed5441888321f204cf9355d~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgrgSwDYBMCCAnDBDEAeAKCmKgBkIA7Ac2AAsoIAPYSlAZygrgFsAjCDABooREgFEk0ALxQ4FANYUA9gHcKw0cUwYGzVhzmLVFANoBdKDPMEAfJajaTAcknU6Ti0xYV2ZSjXpNEmIAfgcsEWDggC5YRFRtXDxyN1phCQhhEwA6XO10yTMbAG4CMtBIKABlOF5gHABjYDwAOR4ARl1vXy4+AWE27gAmLv1OHn4MOxkg+GR0LCTB9rsvMZzc7Cx22LmExfxBoZthXOytjCHYhAoAMwEoACUINmAzIOCw59fnVwCPD4kWIUCAANwEpXK4GgABEEKCECgIK0OqMfBxepMBjwRmt0eM+kIoABhJRyYDaNG+QzKNTmezmaZBZZUjgABigYVJ5McLn87neUSBUDhCKReBqdUazWW2OGJygRyyNOMp1y3IoFKwRUhUMqosREG+cCQwHsBvFAGY2cIAKwlMpAA)

就这样，我们通过递归的累减并记录减了几次实现了除法。

做完了加减乘除，我们再来做一些别的数值计算的类型体操。

## 数组长度实现计数

### StrLen

数组长度可以取 length 来得到，但是字符串类型不能取 length，所以我们来实现一个求字符串长度的高级类型。

字符串长度不确定，明显要用递归。每次取一个并计数，直到取完，就是字符串长度。

```typescript
type StrLen<
    Str extends string,
    CountArr extends unknown[] = []
> = Str extends `${string}${infer Rest}` 
    ? StrLen<Rest, [...CountArr, unknown]> 
    : CountArr['length']
```
类型参数 Str 是待处理的字符串。类型参数 CountArr 是做计数的数组，默认值 [] 代表从 0 开始。

每次通过模式匹配提取去掉一个字符之后的剩余字符串，并且往计数数组里多放入一个元素。递归进行取字符和计数。

如果模式匹配不满足，代表计数结束，返回计数数组的长度 CountArr['length']。

这样就能求出字符串长度：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7b0a4bed15a1402bbf7f526fcc617845~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAysBOAZCA7APAKCt2CoQA9hUATAZyjIQEsUBzAGixwGEB7AVxWAEF558RUhS4BrFGwDuKANoBdKAF4o8jAD4luAYWIpyUAAYASAN5V4tOgF9TtAGYQBAJQhUrBqAH4tydC6oMKgB0IexcvPyBYhLSchoAXFBh3HzwMgDkADaodMAAFulyGMUYoJA+qP4cmcCacEioaOkAEhCZmWxQAOps8Jkk6WoA3EA)

### GreaterThan

能够做计数了，那也就能做两个数值的比较。

我们往一个数组类型中不断放入元素取长度，如果先到了 A，那就是 B 大，否则是 A 大：

```typescript
type GreaterThan<
    Num1 extends number,
    Num2 extends number,
    CountArr extends unknown[] = []
> = Num1 extends Num2 
    ? false
    : CountArr['length'] extends Num2
        ? true
        : CountArr['length'] extends Num1
            ? false
            : GreaterThan<Num1, Num2, [...CountArr, unknown]>;
```
类型参数 Num1 和 Num2 是待比较的两个数。

类型参数 CountArr 是计数用的，会不断累加，默认值是 [] 代表从 0 开始。

如果 Num1 extends Num2 成立，代表相等，直接返回 false。

否则判断计数数组的长度，如果先到了 Num2，那么就是 Num1 大，返回 true。

反之，如果先到了 Num1，那么就是 Num2 大，返回 false。

如果都没到就往计数数组 CountArr 中放入一个元素，继续递归。

这样就实现了数值比较。

当 3 和 4 比较时：

![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e80b78ebf4a344c78a7bfc6e0bc50c1a~tplv-k3u1fbpfcp-watermark.image?)

当 6 和 4 比较时：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9d121e0430b458a9506903a07b2fe36~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBA4gJygQxFBAVAFsgdgHmBmJgDkBXAWwEYYoAPNXAEwGcZcqAjdAGiJIVKAJjqMoLdp0o8E-EjADCAe3K4QAQQQIxTNjDUBrXMoDuuANoBdGAF4Y14AD47ZKrQZ72Q0QOIB+GAAzZAAbVig-GAAuJVV1LQQLAHJQiQBzECxkm08JfR8ohUCQBHJIhQVYlTVNbRS03Ezs3PFJNxoiyoDgsIiu7tjEFDRMHAIhal4O4WmLADpFmoTtaaMTcysnAG5gPfBoeCRUdGw8ACUoVnJQkFdhk7G8fABmaYAWHf3IWAfRs9wl2ut1E9j+p3G+AAbB8dkA)

### Fibonacci

谈到了数值运算，就不得不提起经典的 Fibonacci 数列的计算。

Fibonacci 数列是 1、1、2、3、5、8、13、21、34、…… 这样的数列，有当前的数是前两个数的和的规律。

*F*(0) = 1，*F*(1) = 1, *F*(n) = *F*(n - 1) + *F*(n - 2)（*n* ≥ 2，*n* ∈ N*）

也就是递归的加法，在 TypeScript 类型编程里用构造数组来实现这种加法：
```typescript
type FibonacciLoop<
    PrevArr extends unknown[], 
    CurrentArr extends unknown[], 
    IndexArr extends unknown[] = [], 
    Num extends number = 1
> = IndexArr['length'] extends Num
    ? CurrentArr['length']
    : FibonacciLoop<CurrentArr, [...PrevArr, ...CurrentArr], [...IndexArr, unknown], Num> 

type Fibonacci<Num extends number> = FibonacciLoop<[1], [], [], Num>;
```

类型参数 PrevArr 是代表之前的累加值的数组。类型参数 CurrentArr 是代表当前数值的数组。

类型参数 IndexArr 用于记录 index，每次递归加一，默认值是 []，代表从 0 开始。

类型参数 Num 代表求数列的第几个数。

判断当前 index 也就是 IndexArr['length'] 是否到了 Num，到了就返回当前的数值 CurrentArr['length']。

否则求出当前 index 对应的数值，用之前的数加上当前的数 [...PrevArr, ... CurrentArr]。

然后继续递归，index + 1，也就是 [...IndexArr, unknown]。

这就是递归计算 Fibinacci 数列的数的过程。

可以正确的算出第 8 个数是 21:
![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/291e04736cce485fb023c767eb8ad464~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAYgSwEYHsB2BDAxlhAZFFCAHmBnJgAUAnKANwEFrqYoAPEKNAEwGcYArmgDWaFAHc0AbQC6AGhhkKAYQHMuIJi3ace-IaInT5iijACSPdltYcufQSLGTZMALwxZCpeQByAgFtbXQc0QKQoFg8ARmAAPncLKzYtKQByABsuAHMQAAs0mWD7fn8AnxgAfhhVdTRNZnSstFyCmQqALnhkdGxcAiJiWtp6rQUpADopmnoxmCmJ4Y0tE0mpy25rZgUDZzQTMoTgUEhYRFRMHARiMuK9GDCAiOoEj3Peq4GSKWjVv4VDgBuY7AAD0oJg0UAgAzQgBMUIAzFCAKxQgAcMKRsOhCIALCdoN0Ln0EAAlKC8AQZECJd6XXDENFxQFAA)

## 总结

TypeScript 类型系统没有加减乘除运算符，所以我们**通过数组类型的构造和提取，然后取长度的方式来实现数值运算**。

我们通过构造和提取数组类型实现了加减乘除，也实现了各种计数逻辑。

用数组长度做计数这一点是 TypeScript 类型体操中最麻烦的一个点，也是最容易让新手困惑的一个点。

[本文案例的合并](https://www.typescriptlang.org/play?#code/PTAEEEBNIKAFwJ4AcCmoBCBXAlgG0uAE6ECGCAPDKNaADIoB2A5nABagoAecjkAzqAaYAtgCMUhADSgqNAKK40AXlCYGAawYB7AO4Nps6kUIduvAWs26GAbQC6oFfZgA+RxGI2A5IuZsvDlw8DPx0jCzshjTUAPweJlHRAFwYOPjGZOT0fqzSCijSNgB0JcZ5inYuANwwtYioENDkAHIiAIymwaFCYhLSrcIATJ3mgiLihG4qUcUlWHgExJkDbS6SJUXz6UsUA4Mudt6+EQE1dchoUJAASih8mLhw7lfkAMyD0oMArNW1MCCgADKmFEcFIAGM4PALkCQWCSJCWu0RiEBD0Jv0RMMgqN0RIpjJoltFqRdu03DjUaBZkUSMQ2iliRkyUM1qANnTCIMUtgGAAzCSgW58OB2RI0OLCuBHcL+MXRZKCFAANwkZ3qaGBoIhcGFDyeKi18MRr1e0ja+zOAIAsvrsEhcAhoQ1bXB7Y6kcIOpTuuM+qA9ijfb0pEK7vqgxYNNo9PZ3PYplFAz6BAAGUCS8OPGU5ALi6gpV3ulltaRGnWej6gVaFDZMnaemvskp6x6VdUwosOhCtg2gLses2gQYj37-MAAEWwyuwkBQzrQU5nc8bkbGIcxQzXeNDAGEtGo4MY15YY7YHE5Ko4k8iU6B03F94fjDmTvKFQXQEvZyhyOWEXAjabvswGFKe1jSBsT4MEexDtucDTfnOvbuEhv6vKm0g-Gc45AmC2QLnhhDZJQ0SAmCa4ioQvJMJIUTQbBJh3uBsYXtSYoEuRTFmFSAAGAAkADeVE0QAvkJvICiYUqibxGZESRUq1iUDFlKo0bWFeKSqZ4PiyqweaEVx2QoYa+GMOQXgABIoLguBaKAADqWiEPgXhjrhADihAoCQPCEAAKqwJAMIR3m+f5QUhaRNArNufpSDeW53judHRDp3FdFGVisfGHHuHFd6BlEcR8iQuB8POioZa+cprns+byWCmBVR+oDaQeMEvnpuaBDxoQrI10SleVlVDTQKThX5EhRQwQEBliylFBl0gsQw8EIWgU2RcFDCmaA20zbtbzSAALGOGoHT502BbtvbDCoh23dFABsZ1jgCABi2CiFoDAIuC2CEd9v3-eCgO0FoWhIDF1AAAo+cqx7MRprEGOlmDEIwjEnqj57ozQACSIRcMj-XZWecaXgT1ADPFIbuG0rjuMTc6cN1xx1UVIglaAu6Yz5XW6ZzBnvp+IN-QD2CQ9D5D81jQuhjSCMqmpUEC9jxh2EtrOk8Qq149rC3CG4m2gBLYOA569MTASFtSzLMM2G0Rv2IURsDB5AJtIAgAy+4MPuvD7Xw+wAHH7QeDL7ryncDP2S+D2D7fbifkKH1RAA)


## 9.套路五：联合分散可简化

联合类型在类型编程中是比较特殊的，TypeScript 对它做了专门的处理，写法上可以简化，但也增加了一些认知成本。

这是类型体操的第五个套路：联合分散可简化。

## 分布式条件类型

**当类型参数为联合类型，并且在条件类型左边直接引用该类型参数的时候，TypeScript 会把每一个元素单独传入来做类型运算，最后再合并成联合类型，这种语法叫做分布式条件类型。**

比如这样一个联合类型：

```typescript
type Union = 'a' | 'b' | 'c';
```
我们想把其中的 a 大写，就可以这样写：

```typescript
type UppercaseA<Item extends string> = 
    Item extends 'a' ?  Uppercase<Item> : Item;
```
![](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/842143798583491aae9dbec0da327da8~tplv-k3u1fbpfcp-watermark.image?)

可以看到，我们类型参数 Item 约束为 string，条件类型的判断中也是判断是否是 a，但传入的是联合类型。

这就是 TypeScript 对联合类型在条件类型中使用时的特殊处理：会把联合类型的每一个元素单独传入做类型计算，最后合并。

这和联合类型遇到字符串时的处理一样：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b29105cf568f4eeeac7240f7f4b5619f~tplv-k3u1fbpfcp-watermark.image?)

这样确实是简化了类型编程逻辑的，不需要递归提取每个元素再处理。

TypeScript 之所以这样处理联合类型也很容易理解，因为联合类型的每个元素都是互不相关的，不像数组、索引、字符串那样元素之间是有关系的。所以设计成了每一个单独处理，最后合并。

知道了 TypeScript 怎么处理的联合类型，趁热打铁来练习一下：

## CamelcaseUnion

Camelcase 我们实现过，就是提取字符串中的字符，首字母大写以后重新构造一个新的。

```typescript
type Camelcase<Str extends string> = 
    Str extends `${infer Left}_${infer Right}${infer Rest}`
    ? `${Left}${Uppercase<Right>}${Camelcase<Rest>}`
    : Str;
```

提取 _ 左右的字符，把右边字符大写之后构造成新的字符串，余下的字符串递归处理。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5bc1e45afeb244e9a64be8ef9aeba12a~tplv-k3u1fbpfcp-watermark.image?)

如果是对字符串数组做 Camelcase，那就要递归处理每一个元素：

```typescript
type CamelcaseArr<
  Arr extends unknown[]
> = Arr extends [infer Item, ...infer RestArr]
  ? [Camelcase<Item & string>, ...CamelcaseArr<RestArr>]
  : [];
```
类型参数 Arr 为待处理数组。

递归提取每一个元素做 Camelcase，因为 Camelcase 要求传入 string，这里要 & string 来变成 string 类型。

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30fa987f5f7741e3b23255035aa0e27f~tplv-k3u1fbpfcp-watermark.image?)

那如果是联合类型呢？

联合类型不需要递归提取每个元素，TypeScript 内部会把每一个元素传入单独做计算，之后把每个元素的计算结果合并成联合类型。

```typescript
type CamelcaseUnion<Item extends string> = 
  Item extends `${infer Left}_${infer Right}${infer Rest}` 
    ? `${Left}${Uppercase<Right>}${CamelcaseUnion<Rest>}` 
    : Item;
 ```

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31fe16b1436f41578fbd65dc7bcfb102~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/FAFwngDgpgBAwgQwLZQDYGMEGcoB4DKIATjFAB4hQB2AJljFsQJZUDmAfDALwzAz8xCJcpVr0ABgBIA3iwBmUEgBkockAF8A+jPmKYAJSasAFhp1UFJfVEbrxfAQH4YU6SrXqZAVQjQimHFxDExB2T2lEFAxsPGtGMPsBGAAuQWIAbmBQSFhItACoOIBXVBBueGR8mNwAcgQETXrGhBr2TOzoCqiCgEEiIlwHPuEKajoYIqoAayoAewB3KgBtAF1gTh5h0lGxGCXdEgBJSiQAGhgAOiuDgxsQYbX+ZyW86MDjqCQYADIGZjZ2OcrhdXr1+kE7sN2I8UnsVu1wJ1QTFhsVSuVkThhrglnUGk16jVzjUAEYkzRkikkokwGrodCaemM9A1FZtLKI3KVN5QLxUJizKi4D5fERjeiMIgsDjlBwi7aicauG7uDTaWQWPTBUzhG5xDTiXhJZyuVXhHx+ApBIymMIyTG8-mCiHxOxGgSpEUInJdKo4PkCqhoso8B0B5145rNGowAA+tMpiepcdpTLTLLaQA)

这不和单个字符串的处理没区别么？

没错，对联合类型的处理和对单个类型的处理没什么区别，TypeScript 会把每个单独的类型拆开传入。不需要像数组类型那样需要递归提取每个元素做处理。

确实简化了很多，好像都是优点？

也不全是，其实这样处理也增加了一些认知成本，不信我们再来看个例子：

## IsUnion

判断联合类型我们会这样写：

```typescript
type IsUnion<A, B = A> =
    A extends A
        ? [B] extends [A]
            ? false
            : true
        : never
```
当传入联合类型时，会返回 true：

![](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/978314675e0f448f9d0c0e6cd643fbd8~tplv-k3u1fbpfcp-watermark.image?)

当传入其他类型时，会返回 false：
![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f947f111a34c4bb4b338243a7030651f~tplv-k3u1fbpfcp-watermark.image?)

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAkgzgVQHYEsD2SA8BBANFAISgF4psA+EgKClrKggA9gIkATOMmungfigDaBALoNmrDoOzDuPOVH4AzAIYAbOBFny6ALijAATgFdN2qHqQQAbhANUqoSLESoMAJQhwjq4CWfJ0LAByZSCAHyCAI3CggGMYtiDyAG57R2h4APdPb2AAJj9M1ywBKBCgqDCy6Mqy+OEUoA)

是不是在心里会问：什么鬼？这段逻辑是啥？

这就是分布式条件类型带来的认知成本。

我们先来看这样一个类型：
```typescript
type TestUnion<A, B = A> = A  extends A ? { a: A, b: B} : never;

type TestUnionResult = TestUnion<'a' | 'b' | 'c'>;
```

传入联合类型 'a' | 'b' | 'c' 的时候，结果是这样的：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/551f7861406c4ba591f6c50ffe17b153~tplv-k3u1fbpfcp-watermark.image?)

A 和 B 都是同一个联合类型，为啥值还不一样呢？

因为条件类型中如果左边的类型是联合类型，会把每个元素单独传入做计算，而右边不会。

所以 A 是 'a' 的时候，B 是 'a' | 'b' | 'c'， A 是 'b' 的时候，B 是 'a' | 'b' | 'c'。。。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAKhDOwCqA7AlgexQHgIIBooAhKAXilwD4yKooIAPYCFAE3loH4oBvKAQwBcFQgCNhRAL5RhKCADcIAJwDcAKDWhIsBMnRYASggCuAG2A04iVJhwByfnagAfKHdFPXdgMZ3KKoA)

那么利用这个特点就可以实现 Union 类型的判断：

```typescript
type IsUnion<A, B = A> =
    A extends A
        ? [B] extends [A]
            ? false
            : true
        : never
```

类型参数 A、B 是待判断的联合类型，B 默认值为 A，也就是同一个类型。

A extends A 这段看似没啥意义，主要是为了触发分布式条件类型，让 A 的每个类型单独传入。

[B] extends [A]  这样不直接写 B 就可以避免触发分布式条件类型，那么 B 就是整个联合类型。

B 是联合类型整体，而 A 是单个类型，自然不成立，而其它类型没有这种特殊处理，A 和 B 都是同一个，怎么判断都成立。

利用这个特点就可以判断出是否是联合类型。

其中有两个点比较困惑，我们重点记一下：

**当 A 是联合类型时：**

- **A extends A 这种写法是为了触发分布式条件类型，让每个类型单独传入处理的，没别的意义。**

- **A extends A 和 [A] extends [A] 是不同的处理，前者是单个类型和整个类型做判断，后者两边都是整个联合类型，因为只有 extends 左边直接是类型参数才会触发分布式条件类型。**

理解了这两点，分布式条件类型就算掌握了。

掌握了难点之后，我们再做些练习：

## BEM

bem 是 css 命名规范，用 block__element--modifier 的形式来描述某个区块下面的某个元素的某个状态的样式。

那么我们可以写这样一个高级类型，传入 block、element、modifier，返回构造出的 class 名：

这样使用：

```typescript
type bemResult = BEM<'guang', ['aaa', 'bbb'], ['warning', 'success']>;
```

它的实现就是三部分的合并，但传入的是数组，要递归遍历取出每一个元素来和其他部分组合，这样太麻烦了。

而如果是联合类型就不用递归遍历了，因为联合类型遇到字符串也是会单独每个元素单独传入做处理。

数组转联合类型可以这样写：

![](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf5ac5ee90d44f24a06fae128c43ecb3~tplv-k3u1fbpfcp-watermark.image?)

那么 BEM 就可以这样实现：

```typescript
type BEM<
    Block extends string,
    Element extends string[],
    Modifiers extends string[]
> = `${Block}__${Element[number]}--${Modifiers[number]}`;
```

类型参数 Block、Element、Modifiers 分别是 bem 规范的三部分，其中 Element 和 Modifiers 都可能多个，约束为 string[]。

构造一个字符串类型，其中 Element 和 Modifiers 通过索引访问来变为联合类型。

字符串类型中遇到联合类型的时候，会每个元素单独传入计算，也就是这样的效果：

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b7efa1dc1714cbe9b19138bac87e257~tplv-k3u1fbpfcp-watermark.image?)
[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAQgogWQDwCgrtgGwPYGMDWUEAHsBAHYAmAzlNcAE4CW5A5gDRoZyYQC2FYEVIUadRi1YBtALqcMUBNkpMAZkwgNaJMlVr1mbWSgB8UALxQABgBIA3jBwEAvgH1X9nv0FTyAVz4AI00ZZwBaMPslFXVNal8A4IZQqwBuFAzQSChgvgAlCGo-TCFLeGQAclY-AEM2CvYoKQqa1oaoCsCuirkmioB3GoZySXaKotxcQuoek1SgA)

可以看到，用好了联合类型，确实能简化类型编程逻辑。

## AllCombinations

我们再来实现一个全组合的高级类型，也是联合类型相关的：

希望传入 'A' | 'B' 的时候，能够返回所有的组合： 'A' | 'B' | 'BA' | 'AB'。

这种全组合问题的实现思路就是两两组合，组合出的字符串再和其他字符串两两组和：

比如 'A' | 'B' | 'c'，就是 A 和 B、C 组合，B 和 A、C 组合，C 和 A、B 组合。然后组合出来的字符串再和其他字符串组合。

任何两个类型的组合有四种：A、B、AB、BA

```typescript
type Combination<A extends string, B extends string> =
    | A
    | B
    | `${A}${B}`
    | `${B}${A}`;
```
然后构造出来的字符串再和其他字符串组合。

所以全组合的高级类型就是这样：

```typescript
type AllCombinations<A extends string, B extends string = A> = 
    A extends A
        ? Combination<A, AllCombinations<Exclude<B, A>>>
        : never;
```

类型参数 A、B 是待组合的两个联合类型，B 默认是 A 也就是同一个。

A extends A 的意义就是让联合类型每个类型单独传入做处理，上面我们刚学会。

A 的处理就是 A 和 B 中去掉 A 以后的所有类型组合，也就是 Combination<A, B 去掉 A 以后的所有组合>。

而 B 去掉 A 以后的所有组合就是 AllCombinations<Exclude<B, A>>，所以全组合就是 Combination<A, AllCombinations<Exclude<B, A>>>。

![](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ba9469c0c3ea4ac0a5e1ebe96ac8bb1f~tplv-k3u1fbpfcp-watermark.image?)

这里利用到了分布式条件类型的特性，通过 A extends A 来取出联合类型中的单个类型。

[试一下](https://www.typescriptlang.org/play?#code/C4TwDgpgBAwg9gWwEYEsB2BDYK5oDwCCUEAHsBGgCYDOU1wATugOYA0UAQsWRTXYywB8UALwAoKJKgAfKAQlTZHBZNkADACQBvAgF9tHXWpUyomrYe161AbgljQkOQBtn8ZOiw401Qt3JUtPRMaGyc-rxBAqGicsIichGBciYA-LCIqJjYuITsBK7uWV64vgCiJADGzgCulBB4HPmCLSYAXFBoEABuEAx2DuDQBW6Znjk+AEoQ1DXOwLEjRePevgDkBGumaxxbsmswa4I2QA)

## 总结

**联合类型中的每个类型都是相互独立的，TypeScript 对它做了特殊处理，也就是遇到字符串类型、条件类型的时候会把每个类型单独传入做计算，最后把每个类型的计算结果合并成联合类型。**

条件类型左边是联合类型的时候就会触法这种处理，叫做分布式条件类型。

有两点特别要注意：

- A extends A 不是没意义，意义是取出联合类型中的单个类型放入 A

- A extends A 才是分布式条件类型， [A] extends [A] 就不是了，只有左边是单独的类型参数才可以。

我们后面做了一些案例，发现联合类型的这种 distributive 的特性确实能简化类型编程，但是也增加了认知成本，不过这也是不可避免的事。

[本文案例的合并](https://www.typescriptlang.org/play?#code/PTAEGEEMFsFMBsDGkDOsBQAXAngB1hDAsmgDwDKmATqLAB6awB2AJiqCtQJZMDmAfKAC8odKHGhKNeo1bsABgBIA3jwBmsGgBlYazAF8A+ivWbQAJS68AFgZNMNNc7E775YiQH5QS5Tr36KgCquPhUJLCkljaY-IHKUHBIqJHOnHHuEqAAXJLUANzoWHgEicQpaQCu8JjChEkRpADkkJCGre2QTfyFxfj15WgAglRUpB4j0gzMbKCVTADWTAD2AO5MANoAuuiCIpO003KgG6Y0AJKM0AA0oAB0D2cWLpiTO+LeG2XJZJew0KAAGQcbh8fi3B53b4RSZRF6TfjvHInLa9HD9aEpSZVGp1THDUakDYtNodVpNW5NABGVMMNLpVIpoCaiEQhlZ7MQTS2PSK6NKRB+sCCTC4yyYpD+AJkM3YnCoPAEdQ8UsOslmvie-gMxlUDjM0Vs8SeaQM8lEWW8vm18RCYUahti8XxwtF4rh6TcFokuSlaJKAyFIrFTBxtRELuD7pJnU6TVAAB9mfSU4zE8yOZmubz0CBQOcUFGmHyAwWi6QhrcAEJ1IZ7DziIZq2WgIYNrKgT5VrbN44bIZIjsd7xqSDwNDtofiXLUSoYKfIpiwABumhL-TLbtDLmq4fzha3zS6CepTRPXJPLG6-o3B5DYYATHVNyGicyuunT5+uTzenmACovEWfQEIBnDlpWoA1vseytuIMrHE23jKKAkC5JBVK5FW+iLiumg3qBQFbmGdRgZg5YtPGSZftR2Z-mAVYAKIALIgVBLHjFkVbwMsiALL2szyoq1ztox8D-MwtQIYJoK8NsIlZMxywsFwahcJo7DSXKsnbLsdS+NxvELEYupiRJTCYBsTCVNAVKaFs+gALSOSoSkqWpGlWTZdlUA58i9GxdnQCRIhMcxzS8JUkB8EyxKtF0lI0oyWy3MSqyQFQooxZSKCVKyLgoNyOZ5kM8DwOAyy2TwkCYCGKBsRVVVMDVr5NlpIIKnw1YCdpnVKkI7ZJm2WRJlWg0+CoQzxNhmQSEmBnxFN-liGxpXlZVVLVbV4ooBWPUdcJUH7UJfC1rBbVHLMw1eBAG1ba1txrY1m3NdtTC7YxdCIPAlQsJEVaPfwQPtrkS6rlQBGtmVz33TtIVQ+tTUtTtzRDFRzJVujTTgNeQA)

