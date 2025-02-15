---
title: 基于 Python 实现微信公众号爬虫
author: 基于 Python 实现微信公众号爬虫
date: 2025-02-14
lang: zh-CN
---

## 0微信公众号爬虫的基本原理

# 微信公众号爬虫的基本原理

网上关于爬虫的教程多如牛毛，但很少有看到微信公众号爬虫教程，要有也是基于搜狗微信的，不过搜狗提供的数据有诸多弊端，比如文章链接是临时的，文章没有阅读量等指标，所以我想写一个比较系统的关于如何通过手机客户端利用 Python 爬微信公众号文章的教程，并对公众号文章做数据分析，为更好的运营公众号提供决策。


### 爬虫的基本原理


所谓爬虫就是一个自动化数据采集工具，你只要告诉它要采集哪些数据，丢给它一个 URL，就能自动地抓取数据了。其背后的基本原理就是爬虫程序向目标服务器发起 HTTP 请求，然后目标服务器返回响应结果，爬虫客户端收到响应并从中提取数据，再进行数据清洗、数据存储工作。


### 爬虫的基本流程

爬虫流程也是一个 HTTP 请求的过程，以浏览器访问一个网址为例，从用户输入 URL 开始，客户端通过 DNS 解析查询到目标服务器的 IP 地址，然后与之建立 TCP 连接，连接成功后，浏览器构造一个 HTTP 请求发送给服务器，服务器收到请求之后，从数据库查到相应的数据并封装成一个 HTTP 响应，然后将响应结果返回给浏览器，浏览器对响应内容进行数据解析、提取、渲染并最终展示在你面前。




![](https://user-gold-cdn.xitu.io/2017/12/18/16068a321d8613c3?w=818&h=365&f=jpeg&s=32929)


HTTP 协议的请求和响应都必须遵循固定的格式，只有遵循统一的 HTTP 请求格式，服务器才能正确解析不同客户端发的请求，同样地，服务器遵循统一的响应格式，客户端才得以正确解析不同网站发过来的响应。

### HTTP 请求格式

HTTP 请求由请求行、请求头、空行、请求体组成。

![](https://user-gold-cdn.xitu.io/2017/12/23/1607f417a70d604f?w=478&h=220&f=jpeg&s=23091)
请求行由三部分组成：

1. 第一部分是请求方法，常见的请求方法有 GET、POST、PUT、DELETE、HEAD
2. 第二部分是客户端要获取的资源路径
3. 第三部分是客户端使用的 HTTP 协议版本号

请求头是客户端向服务器发送请求的补充说明，比如 User-Agent 向服务器说明客户端的身份。

请求体是客户端向服务器提交的数据，比如用户登录时需要提高的账号密码信息。请求头与请求体之间用空行隔开。请求体并不是所有的请求都有的，比如一般的GET都不会带有请求体。

上图就是浏览器登录豆瓣时向服务器发送的HTTP POST 请求，请求体中指定了用户名和密码。


### HTTP 响应格式

HTTP 响应格式与请求的格式很相似，也是由响应行、响应头、空行、响应体组成。

![](https://user-gold-cdn.xitu.io/2017/12/23/1607f4b5edd376b5?w=478&h=220&f=jpeg&s=24097)

响应行也包含三部分，分别是服务端的 HTTP 版本号、响应状态码、状态说明，响应状态码常见有 200、400、404、500、502、304 等等，一般以 2 开头的表示服务器正常响应了客户端请求，4 开头表示客户端的请求有问题，5 开头表示服务器出错了，没法正确处理客户端请求。状态码说明就是对该状态码的一个简短描述。

第二部分就是响应头，响应头与请求头对应，是服务器对该响应的一些附加说明，比如响应内容的格式是什么，响应内容的长度有多少、什么时间返回给客户端的、甚至还有一些 Cookie 信息也会放在响应头里面。

第三部分是响应体，它才是真正的响应数据，这些数据其实就是网页的 HTML 源代码。

### 小结

这仅仅只是一个爬虫基本原理的介绍，涉及的 HTTP 协议的内容也非常有限，但不可能用一篇文章事无巨细的介绍完，因为 HTTP 协议是一个很大的话题，用一本书也写不完，深入了解推荐两本书《图解HTTP》、《HTTP权威指南》。








## 10小结

# 小结
《基于 Python 实现微信公众号爬虫》到此告一段路。小册的初衷是以公众号爬虫作为引子，帮助大家提高 Python 实践能力，小册从爬虫的基本原理说起，然后简单介绍了 HTTP 请求库 Requests 的基本使用方法，还有抓包工具 Fiddler 的使用，最后介绍了数据分析工具 Pandas、Matplotlib。

小册内容我并没有往深的角度去写，比如如何爬更多公众号，如何每天定时去抓公众号，抓回来的数据如何处理等等。由于篇幅有限这些内容没法一一展开，欢迎和大家一起讨论，这本小册在这里只是一个抛砖引玉的作用，如果你能从中受到启发，基于这个思路做出实用的产品，比如基于公众号数据做个数据分析平台，比如将公众号的文章制作成电子书等等，那将是我的荣幸。

谢谢大家。

## 1使用 Requests 实现一个简单网页爬虫

# 使用 Requests 实现一个简单网页爬虫

```!
友情提示：小册代码全部基于 Python3.6 实现
```

第一节我们简单介绍了爬虫的基本原理，理解原理可以帮助我们更好的实现代码。Python 提供了非常多工具去实现 HTTP 请求，但第三方开源库提供的功能更丰富，你无需从 socket 通信开始写，比如使用Pyton内建模块 `urllib` 请求一个 URL 代码示例如下：


```python
import ssl

from urllib.request import Request
from urllib.request import urlopen

context = ssl._create_unverified_context()

# HTTP 请求
request = Request(url="https://foofish.net/pip.html",
                  method="GET",
                  headers={"Host": "foofish.net"},
                  data=None)

# HTTP 响应
response = urlopen(request, context=context)
headers = response.info()  # 响应头
content = response.read() # 响应体
code = response.getcode() # 状态码
```

发起请求前首先要构建请求对象 Request，指定 url 地址、请求方法、请求头，这里的请求体 data 为空，因为你不需要提交数据给服务器，所以你也可以不指定。urlopen 函数会自动与目标服务器建立连接，发送 HTTP 请求，该函数的返回值是一个响应对象 Response，里面有响应头信息，响应体，状态码之类的属性。

但是，Python 提供的这个内建模块过于低级，需要写很多代码，使用简单爬虫可以考虑 Requests，Requests 在GitHub 有近30k的Star，是一个很Pythonic的框架。先来简单熟悉一下这个框架的使用方式

### 安装 requests

```python
pip install requests
```

### GET 请求

```python
>>> r = requests.get("https://httpbin.org/ip")
>>> r
<Response [200]> # 响应对象
>>> r.status_code  # 响应状态码
200

>>> r.content  # 响应内容
'{\n  "origin": "183.237.232.123"\n}\n'
```

### POST 请求


```python
>>> r = requests.post('http://httpbin.org/post', data = {'key':'value'})
```

### 自定义请求头

这个经常会用到，服务器反爬虫机制会判断客户端请求头中的User-Agent是否来源于真实浏览器，所以，我们使用Requests经常会指定UA伪装成浏览器发起请求

```python
>>> url = 'https://httpbin.org/headers'
>>> headers = {'user-agent': 'Mozilla/5.0'}
>>> r = requests.get(url, headers=headers)
```

### 参数传递

很多时候URL后面会有一串很长的参数，为了提高可读性，requests 支持将参数抽离出来作为方法的参数（params）传递过去，而无需附在 URL 后面，例如请求 url http://bin.org/get?key=val ，可使用

```python
>>> url = "http://httpbin.org/get"
>>> r = requests.get(url, params={"key":"val"})
>>> r.url
u'http://httpbin.org/get?key=val'
```

### 指定Cookie
Cookie 是web浏览器登录网站的凭证，虽然 Cookie 也是请求头的一部分，我们可以从中剥离出来，使用 Cookie 参数指定

```python
>>> s = requests.get('http://httpbin.org/cookies', cookies={'from-my': 'browser'})
>>> s.text
u'{\n  "cookies": {\n    "from-my": "browser"\n  }\n}\n'
```

### 设置超时

当发起一个请求遇到服务器响应非常缓慢而你又不希望等待太久时，可以指定 timeout 来设置请求超时时间，单位是秒，超过该时间还没有连接服务器成功时，请求将强行终止。

```python
r = requests.get('https://google.com', timeout=5)
```

### 设置代理

一段时间内发送的请求太多容易被服务器判定为爬虫，所以很多时候我们使用代理IP来伪装客户端的真实IP。

```python
import requests

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080',
}

r = requests.get('http://www.kuaidaili.com/free/', proxies=proxies, timeout=2)
```

### Session

如果想和服务器一直保持登录（会话）状态，而不必每次都指定 cookies，那么可以使用 session，Session 提供的API和 requests 是一样的。

```python
import requests

s = requests.Session()
s.cookies = requests.utils.cookiejar_from_dict({"a": "c"})
r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {"a": "c"}}'

r = s.get('http://httpbin.org/cookies')
print(r.text)
# '{"cookies": {"a": "c"}}'
```
### 小试牛刀

现在我们使用Requests完成一个爬取知乎专栏用户关注列表的简单爬虫为例，找到任意一个专栏，打开它的[关注列表](https://zhuanlan.zhihu.com/pythoneer)。用 Chrome 找到获取粉丝列表的请求地址：[https://www.zhihu.com/api/v4/columns/pythoneer/followers?include=data%5B%2A%5D.follower_count%2Cgender%2Cis_followed%2Cis_following&limit=10&offset=20](https://www.zhihu.com/api/v4/columns/pythoneer/followers?include=data%5B%2A%5D.follower_count%2Cgender%2Cis_followed%2Cis_following&limit=10&offset=20)。 我是怎么找到的？就是逐个点击左侧的请求，观察右边是否有数据出现，那些以 `.jpg`，`js`，`css` 结尾的静态资源可直接忽略。


![](https://user-gold-cdn.xitu.io/2018/9/27/16618c3de5516ff1?w=1038&h=805&f=png&s=113952)

现在我们用 Requests 模拟浏览器发送请求给服务器，写程序前，我们要先分析出这个请求是怎么构成的，请求URL是什么？请求头有哪些？查询参数有哪些？只有清楚了这些，你才好动手写代码，掌握分析方法很重要，否则一头雾水。

回到前面那个URL，我们发现这个URL是获取粉丝列表的接口，然后再来详细分析一下这个请求是怎么构成的。

![](https://user-gold-cdn.xitu.io/2018/9/28/1661efcfb3260e81?w=1368&h=888&f=png&s=127718)

* 请求URL：https://www.zhihu.com/api/v4/columns/pythoneer/followers
* 请求方法：GET
* user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36
* 查询参数：
    * include: data[*].follower_count,gender,is_followed,is_following
    * offset: 0
    * limit: 10

利用这些请求数据我们就可以用requests这个库来构建一个请求，通过Python代码来抓取这些数据。

```python

import requests


class SimpleCrawler:

    def crawl(self, params=None):
        # 必须指定UA，否则知乎服务器会判定请求不合法

        url = "https://www.zhihu.com/api/v4/columns/pythoneer/followers"
        # 查询参数
        params = {"limit": 20,
                  "offset": 0,
                  "include": "data[*].follower_count, gender, is_followed, is_following"}

        headers = {
            "authority": "www.zhihu.com",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        }
        response = requests.get(url, headers=headers, params=params)
        print("请求URL：", response.url)
        # 你可以先将返回的响应数据打印出来，拷贝到 http://www.kjson.com/jsoneditor/ 分析其结构。
        print("返回数据：", response.text)

        # 解析返回的数据
        for follower in response.json().get("data"):
            print(follower)


if __name__ == '__main__':
    SimpleCrawler().crawl()
```
输出：

```
请求URL： https://www.zhihu.com/api/v4/columns/pythoneer/followers?limit=20&offset=0&include=data%5B%2A%5D.follower_count%2C+gender%2C+is_followed%2C+is_following
返回数据： {'paging': {'is_end': False, 'totals': 10436, 'previous': 'http://www.zhihu.com/api/v4/columns/pythoneer/followers?include=data%5B%2A%5D.follower_count%2C+gender%2C+is_followed%2C+is_following&limit=20&offset=0', 'is_start': True, 'next': 'http://www.zhihu.com/api/v4/columns/pythoneer/followers?include=data%5B%2A%5D.follower_count%2C+gender%2C+is_followed%2C+is_following&limit=20&offset=20'}, 'data': [{'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/v2-71a02b83135bf403099b5d3f6a260c5f_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '欢迎关注公众号：「乔尔事务所」 → 城市 | 地理 | 规划 | 经济', 'url_token': 'joe1324', 'id': '130894ff204e72b96719a09b5a6565bc', 'type': 'people', 'name': '乔尔爱冒险', 'url': 'http://www.zhihu.com/api/v4/people/130894ff204e72b96719a09b5a6565bc', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/v2-71a02b83135bf403099b5d3f6a260c5f_is.jpg', 'is_org': False, 'follower_count': 4, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic3.zhimg.com/v2-339c1f09cd793f43dbccae18af9bfbec_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '', 'url_token': 'hei-tai-yang-91', 'id': 'bbeba0903e14a32d19b27ffa0016ac55', 'type': 'people', 'name': 'JOJO', 'url': 'http://www.zhihu.com/api/v4/people/bbeba0903e14a32d19b27ffa0016ac55', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic3.zhimg.com/v2-339c1f09cd793f43dbccae18af9bfbec_is.jpg', 'is_org': False, 'follower_count': 4, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic3.zhimg.com/v2-b6d02ae5a289dc93151c547fc3ae2837_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '2333333333', 'url_token': 'wo-zai-xue-xi-ni-87', 'id': '696dcf2ff66b23ae0ff39474f9f48c5e', 'type': 'people', 'name': '我在学习呢', 'url': 'http://www.zhihu.com/api/v4/people/696dcf2ff66b23ae0ff39474f9f48c5e', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic3.zhimg.com/v2-b6d02ae5a289dc93151c547fc3ae2837_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic2.zhimg.com/v2-905d2532655664de3972b9867d47513e_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '逻辑至上', 'url_token': 'wang-zhu-yi-65', 'id': '0580427bffd2815ee8e8007fbb2419b1', 'type': 'people', 'name': '王朮屹', 'url': 'http://www.zhihu.com/api/v4/people/0580427bffd2815ee8e8007fbb2419b1', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic2.zhimg.com/v2-905d2532655664de3972b9867d47513e_is.jpg', 'is_org': False, 'follower_count': 17, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic1.zhimg.com/009687428186cd079b98c419eb194449_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '笨鸟先飞', 'url_token': 'wei-sen-ken', 'id': '7d938d55321c34eee0cde88359e827ff', 'type': 'people', 'name': '魏森肯', 'url': 'http://www.zhihu.com/api/v4/people/7d938d55321c34eee0cde88359e827ff', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic1.zhimg.com/009687428186cd079b98c419eb194449_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/da8e974dc_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': 'holo', 'url_token': 'zhang-feng-wei', 'id': 'c6ba181c10593256fa71d9ecb8dcdb90', 'type': 'people', 'name': 'goingon', 'url': 'http://www.zhihu.com/api/v4/people/c6ba181c10593256fa71d9ecb8dcdb90', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/da8e974dc_is.jpg', 'is_org': False, 'follower_count': 9, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic2.zhimg.com/v2-e8595f20a7d84adea1f06988e6fea8b6_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '在读大学生', 'url_token': 'fu-teng-53', 'id': 'b7ef951f5b89373ed369a07ea5cb7553', 'type': 'people', 'name': 'fuPatrick', 'url': 'http://www.zhihu.com/api/v4/people/b7ef951f5b89373ed369a07ea5cb7553', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic2.zhimg.com/v2-e8595f20a7d84adea1f06988e6fea8b6_is.jpg', 'is_org': False, 'follower_count': 1, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/da8e974dc_{size}.jpg', 'user_type': 'people', 'is_following': False, 'url_token': 'hu-chen-92-42-74', 'id': 'f88db2870e4e9cdbe589b5846fccd70c', 'type': 'people', 'name': '胡沈', 'url': 'http://www.zhihu.com/api/v4/people/f88db2870e4e9cdbe589b5846fccd70c', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/da8e974dc_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/da8e974dc_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '', 'url_token': 'zhi-bei-bu-nan', 'id': '63220b9e8cadb266b236ed0e1d76d1ed', 'type': 'people', 'name': '只北不南', 'url': 'http://www.zhihu.com/api/v4/people/63220b9e8cadb266b236ed0e1d76d1ed', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/da8e974dc_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/479227614_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '道路不止一条 终点不必相同 人生各自精彩', 'url_token': 'xi-zi-31-56', 'id': '8e3014e0c8e4bf4cd73f34398ee21379', 'type': 'people', 'name': '西子', 'url': 'http://www.zhihu.com/api/v4/people/8e3014e0c8e4bf4cd73f34398ee21379', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/479227614_is.jpg', 'is_org': False, 'follower_count': 1, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic1.zhimg.com/eff9fca94_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': 'I know nothing.', 'url_token': '42195', 'id': 'ce5e19c125f8570bee02cdb414f6e233', 'type': 'people', 'name': 'Gladius', 'url': 'http://www.zhihu.com/api/v4/people/ce5e19c125f8570bee02cdb414f6e233', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic1.zhimg.com/eff9fca94_is.jpg', 'is_org': False, 'follower_count': 74, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/da8e974dc_{size}.jpg', 'user_type': 'people', 'is_following': False, 'url_token': 'willbillion', 'id': '0ee103930c20c21d314a998a371abe82', 'type': 'people', 'name': 'willbillion', 'url': 'http://www.zhihu.com/api/v4/people/0ee103930c20c21d314a998a371abe82', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/da8e974dc_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/da8e974dc_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '', 'url_token': 'yang-guang-xiao-tong', 'id': '1637b7761fe90da99519d4878a4a991f', 'type': 'people', 'name': '阳光小桐', 'url': 'http://www.zhihu.com/api/v4/people/1637b7761fe90da99519d4878a4a991f', 'gender': 0, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/da8e974dc_is.jpg', 'is_org': False, 'follower_count': 1, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/da8e974dc_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': 'Access', 'url_token': 'wang-hua-18-79', 'id': 'd0a5fd983546174636af438651c13018', 'type': 'people', 'name': '王华', 'url': 'http://www.zhihu.com/api/v4/people/d0a5fd983546174636af438651c13018', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/da8e974dc_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic3.zhimg.com/5fa6a8e5aa7207fcbfd917dc8ce50d50_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '', 'url_token': 'oriver', 'id': 'cd9bcc01b125999b10d3f19e872601f2', 'type': 'people', 'name': '瑞木', 'url': 'http://www.zhihu.com/api/v4/people/cd9bcc01b125999b10d3f19e872601f2', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic3.zhimg.com/5fa6a8e5aa7207fcbfd917dc8ce50d50_is.jpg', 'is_org': False, 'follower_count': 28, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/v2-613200caa6f358b464f77943dd2f3e58_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '略。', 'url_token': 'yuan-yi-ming-75', 'id': '7fa634179ecab220235bfb92b7fb3774', 'type': 'people', 'name': '明明就是我', 'url': 'http://www.zhihu.com/api/v4/people/7fa634179ecab220235bfb92b7fb3774', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/v2-613200caa6f358b464f77943dd2f3e58_is.jpg', 'is_org': False, 'follower_count': 10, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/v2-ae335a25be4fd6c5bc3c051bb609e2bf_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '纯属无聊，打发时间', 'url_token': 'abandon-65-76', 'id': 'e98a2e7d53e048dfc8d8a05e60b361fd', 'type': 'people', 'name': 'Abandon', 'url': 'http://www.zhihu.com/api/v4/people/e98a2e7d53e048dfc8d8a05e60b361fd', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/v2-ae335a25be4fd6c5bc3c051bb609e2bf_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic3.zhimg.com/v2-050a58566ea8d633236ea4cfddf8fa82_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '这个人很懒什么都没留下', 'url_token': '10-07-zhihu-er', 'id': '2652bced43a18f45849f4f8ea760ef05', 'type': 'people', 'name': '10点睡7点起', 'url': 'http://www.zhihu.com/api/v4/people/2652bced43a18f45849f4f8ea760ef05', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic3.zhimg.com/v2-050a58566ea8d633236ea4cfddf8fa82_is.jpg', 'is_org': False, 'follower_count': 15, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/da8e974dc_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '', 'url_token': 'zjsroom', 'id': '50b846d7a5988ac7bbc74b2a4f651c7f', 'type': 'people', 'name': 'zjsroom', 'url': 'http://www.zhihu.com/api/v4/people/50b846d7a5988ac7bbc74b2a4f651c7f', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/da8e974dc_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}, {'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/v2-ce57364925dc28389b7daed195abe1b6_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '程序猿', 'url_token': 'yi-di-jin-guang', 'id': 'e7d124798d91d28e983330ec2b72d311', 'type': 'people', 'name': '一地金光', 'url': 'http://www.zhihu.com/api/v4/people/e7d124798d91d28e983330ec2b72d311', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/v2-ce57364925dc28389b7daed195abe1b6_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}]}
{'is_followed': False, 'avatar_url_template': 'https://pic4.zhimg.com/v2-71a02b83135bf403099b5d3f6a260c5f_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '欢迎关注公众号：「乔尔事务所」 → 城市 | 地理 | 规划 | 经济', 'url_token': 'joe1324', 'id': '130894ff204e72b96719a09b5a6565bc', 'type': 'people', 'name': '乔尔爱冒险', 'url': 'http://www.zhihu.com/api/v4/people/130894ff204e72b96719a09b5a6565bc', 'gender': 1, 'is_advertiser': False, 'avatar_url': 'https://pic4.zhimg.com/v2-71a02b83135bf403099b5d3f6a260c5f_is.jpg', 'is_org': False, 'follower_count': 4, 'badge': []}
{'is_followed': False, 'avatar_url_template': 'https://pic3.zhimg.com/v2-339c1f09cd793f43dbccae18af9bfbec_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '', 'url_token': 'hei-tai-yang-91', 'id': 'bbeba0903e14a32d19b27ffa0016ac55', 'type': 'people', 'name': 'JOJO', 'url': 'http://www.zhihu.com/api/v4/people/bbeba0903e14a32d19b27ffa0016ac55', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic3.zhimg.com/v2-339c1f09cd793f43dbccae18af9bfbec_is.jpg', 'is_org': False, 'follower_count': 4, 'badge': []}
{'is_followed': False, 'avatar_url_template': 'https://pic3.zhimg.com/v2-b6d02ae5a289dc93151c547fc3ae2837_{size}.jpg', 'user_type': 'people', 'is_following': False, 'headline': '2333333333', 'url_token': 'wo-zai-xue-xi-ni-87', 'id': '696dcf2ff66b23ae0ff39474f9f48c5e', 'type': 'people', 'name': '我在学习呢', 'url': 'http://www.zhihu.com/api/v4/people/696dcf2ff66b23ae0ff39474f9f48c5e', 'gender': -1, 'is_advertiser': False, 'avatar_url': 'https://pic3.zhimg.com/v2-b6d02ae5a289dc93151c547fc3ae2837_is.jpg', 'is_org': False, 'follower_count': 0, 'badge': []}
...
}

Process finished with exit code 0
```

### 作业

上面的示例只抓到了20条粉丝数据，如何将该专栏的所有粉丝爬下来并保存到文件中。


### 小结
这就是一个最简单的基于 Requests 的单线程知乎专栏粉丝列表的爬虫，requests 非常灵活，请求头、请求参数、Cookie 信息都可以直接指定在请求方法中，返回值 response 如果是 json 格式可以直接调用json()方法返回 python 对象。关于 Requests 的更多使用方法可以参考官方文档：[http://docs.python-requests.org/en/master/](http://docs.python-requests.org/en/master/)


## 2使用 Fiddler 抓包分析公众号请求过程

# 使用 Fiddler 抓包分析公众号请求过程

上一节我们熟悉了 Requests 基本使用方法，配合 Chrome 浏览器实现了一个简单爬虫，但因为微信公众号的封闭性，微信公众平台并没有对外提供 Web 端入口，只能通过手机客户端接收、查看公众号文章，所以，为了窥探到公众号背后的网络请求，我们需要借以代理工具的辅助。

HTTP代理工具又称为抓包工具，主流的抓包工具 Windows 平台有 Fiddler，macOS 有 Charles，阿里开源了一款工具叫 AnyProxy。它们的基本原理都是类似的，就是通过在手机客户端设置好代理IP和端口，客户端所有的 HTTP、HTTPS 请求就会经过代理工具，在代理工具中就可以清晰地看到每个请求的细节，然后可以分析出每个请求是如何构造的，弄清楚这些之后，我们就可以用 Python 模拟发起请求，进而得到我们想要的数据。



![](https://user-gold-cdn.xitu.io/2017/12/21/16076ebe7c39555e?w=400&h=189&f=png&s=16585)


Fiddler 下载地址是 [https://www.telerik.com/download/fiddler](https://www.telerik.com/download/fiddler)，安装包就 4M 多，在配置之前，首先要确保你的手机和电脑在同一个局域网，如果不在同一个局域网，你可以买个随身WiFi，在你电脑上搭建一个极简无线路由器。安装过程一路点击下一步完成就可以了。

### Fiddler 配置

选择  **Tools > Fiddler Options > Connections**

Fiddler 默认的端口是使用 8888，如果该端口已经被其它程序占用了，你需要手动更改，勾选 Allow remote computers to connect，其它的选择默认配置就好，配置更新后记得重启 Fiddler。一定要重启 Fiddler，否则代理无效。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ec4c6769b0e?w=545&h=332&f=jpeg&s=59210)

接下来你需要配置手机，我们以 Android 设备为例，现在假设你的手机和电脑已经在同一个局域网（只要连的是同一个路由器就在同局域网内），找到电脑的 IP 地址，在 Fiddler 右上角有个 Online 图标，鼠标移过去就能看到IP了，你也可以在CMD窗口使用 `ipconfig` 命令查看到


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ec782894dc7?w=545&h=229&f=png&s=11588)

### Android 手机代理配置

进入手机的 WLAN 设置，选择当前所在局域网的 WiFi 链接，设置代理服务器的 IP 和端口，我这是以小米设备为例，其它 Android 手机的配置过程大同小异。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ecb29d33fed?w=606&h=419&f=png&s=33194)

测试代理有没有设置成功可以在手机浏览器访问你配置的地址：http://192.168.31.236:8888/ 会显示 Fiddler 的回显页面，说明配置成功。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ecef988458a?w=545&h=266&f=png&s=28894)


现在你打开任意一个HTTP协议的网站都能看到请求会出现在 Fiddler 窗口，但是 HTTPS 的请求并没有出现在 Fiddler 中，其实还差一个步骤，需要在 Fiddler 中激活 HTTPS 抓取设置。在 Fiddler 选择 **Tools > Fiddler Options > HTTPS > Decrypt HTTPS traffic**， 重启 Fiddler。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ed2835c948a?w=539&h=260&f=jpeg&s=24448)


为了能够让 Fiddler 截取 HTTPS 请求，客户端都需要安装且信任 Fiddler 生成的 CA 证书，否则会出现“网络出错，轻触屏幕重新加载:-1200”的错误。在浏览器打开 Fiddler 回显页面 http://192.168.31.236:8888/ 下载 **FiddlerRoot certificate**，下载并安装证书，并验证通过。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ed5fe54365c?w=926&h=283&f=jpeg&s=65828)

iOS下载安装完成之后还要从 **设置->通用->关于本机->证书信任设置** 中把 Fiddler 证书的开关打开



![](https://user-gold-cdn.xitu.io/2017/12/21/16076ed87c067644?w=637&h=534&f=png&s=96133)


Android 手机下载保存证书后从系统设置里面找到系统安全，从SD卡安装证书，如果没有安装证书，打开微信公众号的时候会弹出警告。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076edb9b11af6e?w=471&h=407&f=jpeg&s=18776)





至此，所有的配置都完成了，现在打开微信随便选择一个公众号，查看公众号的所有历史文章列表。微信在2018年6月份对 iOS 版本的微信以及部分 Android 版微信针对公众号进行了大幅调整，改为现在的信息流方式，现在要获取某个公众号下面「所有文章列表」大概需要经过以下四个步骤：


![](https://user-gold-cdn.xitu.io/2018/9/8/165b6bfe0e38ebe1?w=1226&h=462&f=jpeg&s=101256)

如果你的微信版本还不是信息流方式展示的，那么应该是Android版本（微信采用的ABTest，不同的用户呈现的方式不一样）


![](https://user-gold-cdn.xitu.io/2018/9/8/165b6c1674c35006?w=933&h=658&f=jpeg&s=120420)

同时观察 Fiddler 主面板


![](https://user-gold-cdn.xitu.io/2017/12/21/16076f01e2d43cc4?w=657&h=222&f=gif&s=16040)

进入「全部消息」页面时，在 Fiddler 上已经能看到有请求进来了，说明公众号的文章走的都是HTTP协议，这些请求就是微信客户端向微信服务器发送的HTTP请求。

注意：第一次请求「全部消息」的时候你看到的可能是一片空白：


![](https://user-gold-cdn.xitu.io/2018/9/8/165b6ca355fc077a?w=748&h=510&f=jpeg&s=21348)

在Fiddler或Charles中看到的请求数据是这样的：


![](https://user-gold-cdn.xitu.io/2018/9/8/165b6cb6368e4386?w=1840&h=666&f=png&s=154258)

这个时候你要直接从左上角叉掉重新进入「全部消息」页面。

现在简单介绍一下这个请求面板上的每个模块的意义。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ee298ad70f6?w=1146&h=594&f=jpeg&s=135253)

这样说明这个请求被微信服务器判定为一次非法的请求，这时你可以叉掉该页面重新进入「全部消息」页面。不出意外的话就能正常看到全部文章列表了，同时也能在Fiddler中看到正常的数据请求了。

我把上面的主面板划分为 7 大块，你需要理解每块的内容，后面才有可能会用 Python 代码来模拟微信请求。

1、服务器的响应结果，200 表示服务器对该请求响应成功  
2、请求协议，微信的请求协议都是基 于HTTPS 的，所以前面一定要配置好，不然你看不到 HTTPS 的请求。  
3、微信服务器主机名   
4、请求路径   
5、请求行，包括了请求方法（GET），请求协议（HTTP/1.1），请求路径（/mp/profile_ext...后面还有很长一串参数） 
6、包括Cookie信息在内的请求头。  
7、微信服务器返回的响应数据，我们分别切换成 TextView 和 WebView 看一下返回的数据是什么样的。


TextView 模式下的预览效果是服务器返回的 HTML 源代码


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ee4cce9a909?w=750&h=229&f=jpeg&s=28314)

WebView 模式是 HTML 代码经过渲染之后的效果，其实就是我们在手机微信中看到的效果，只不过因为缺乏样式，所以没有手机上看到的美化效果。


![](https://user-gold-cdn.xitu.io/2017/12/21/16076ee68550314d?w=753&h=213&f=jpeg&s=18543)

如果服务器返回的是 Json格式或者是 XML，你还可以切换到对应的页面预览查看。


### 小结

配置好Fiddler的几个步骤主要包括指定监控的端口，开通HTTPS流量解密功能，同时，客户端需要安装CA证书。下一节我们基于Requests模拟像微信服务器发起请求。

## 3抓取微信公众号第一篇文章

# 抓取第一篇微信公众号文章

上一节我们熟悉了 Fiddler 的基本操作以及每个模块所代表的意义，这节我们详细了解获取微信公众号历史文章接口的请求情况，以及如何使用 Python 模拟微信发送请求获取公众号文章的基本信息。


打开微信历史消息页面，我们从 Fiddler 看到了很多请求，为了找到微信历史文章的接口，我们要逐个查看 Response 返回的内容，最后发现第 11 个请求 "https://mp.weixin.qq.com/mp/profile_ext?action=home..." 就是我们要寻找的（我是怎么找到的呢？这个和你的经验有关，你可以点击逐个请求，看看返回的Response内容是不是期望的内容）


![](https://user-gold-cdn.xitu.io/2017/12/21/160786568551ab61?w=993&h=552&f=png&s=106968)

确定微信公众号的请求HOST是 mp.weixin.qq.com 之后，我们可以使用过滤器来过滤掉不相关的请求。


![](https://user-gold-cdn.xitu.io/2017/12/21/1607865a1a5665bd?w=1075&h=392&f=png&s=53664)


爬虫的基本原理就是模拟浏览器发送 HTTP 请求，然后从服务器得到响应结果，现在我们就用 Python 实现如何发送一个 HTTP 请求。这里我们使用 requests 库来发送请求。




**创建一个 Pycharm 项目**

我们使用 Pycharm 作为开发工具，你也可以使用其它你熟悉的工具，Python 环境是 Python3（推荐使用 Python3.6），先创建一个项目 weixincrawler


![](https://user-gold-cdn.xitu.io/2017/12/21/1607865d62ac4cb1?w=653&h=293&f=png&s=24747)

现在我们来编写一个最粗糙的版本，你需要做两件事：

* 1：找到完整URL请求地址
* 2：找到完整的请求头（headers）信息，Headers里面包括了cookie、User-agent、Host 等信息。

我们直接从 Fiddler 请求中拷贝 URL 和 Headers， **右键 -> Copy -> Just Url/Headers Only**


![](https://user-gold-cdn.xitu.io/2017/12/21/16078660b4f52944?w=878&h=289&f=png&s=37508)

最终拷贝出来的URL很长，它包含了很多的参数

```python
url = "https://mp.weixin.qq.com/mp/profile_ext" \
      "?action=home" \
      "&__biz=MjM5MzgyODQxMQ==" \
      "&scene=124" \
      "&devicetype=android-24" \
      "&version=26051633&lang=zh_CN" \
      "&nettype=WIFI&a8scene=3" \
      "&pass_ticket=MXADI5SFjXvX7DFPRuUEJhWHEWvRha2x1Re%2BoJkveUxIonMfnxY1kM9cOPmm6JRx" \
      "&wx_header=1"
```
暂且不去分析（猜测）每个参数的意义，也不知道那些参数是必须的，总之我把这些参数全部提取出来。然后把 Headers 拷贝出来，发现 Fiddler 把 请求行、响应行、响应头都包括进来了，我们只需要中间的请求头部分。


![](https://user-gold-cdn.xitu.io/2017/12/21/1607866d6574c050?w=633&h=385&f=png&s=50880)

因为 requests.get 方法里面的 headers 参数必须是字典对象，所以，先要写个函数把刚刚拷贝的字符串转换成字典对象。

```python
def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典对象
    {
        "Host": "mp.weixin.qq.com",
        "Connection": "keep-alive",
        "Cache-Control":"max-age="
    }
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers
```

最终 v0.1 版本出来了，不出意外的话，公众号历史文章数据就在 response.text 中。如果返回的内容非常短，而且title标签是`<title>验证</title>`，那么说明你的请求参数或者请求头有误，最有可能的一种请求就是 Headers 里面的 Cookie 字段过期，从手机微信端重新发起一次请求获取最新的请求参数和请求头试试。

```python
# v0.1
def crawl():
    url = "https://mp.weixin.qq.com/..." # 省略了
    headers = """  # 省略了
Host: mp.weixin.qq.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)
```

最后，我们顺带把响应结果另存为html文件，以便后面重复使用，分析里面的内容

```python
with open("weixin_history.html", "w", encoding="utf-8") as f:
    f.write(response.text)
```

用浏览器打开 weixin_history.html 文件，查看该页面的源代码，搜索微信历史文章标题的关键字 "11月赠书"（就是我以往发的文章），你会发现，历史文章封装在叫 msgList 的数组中（实际上该数组包装在字典结构中），这是一个 Json 格式的数据，但是里面还有 html 转义字符需要处理


![](https://user-gold-cdn.xitu.io/2017/12/21/160786716cba2f1d?w=690&h=324&f=png&s=26530)

接下来我们就来写一个方法提取出历史文章数据，分三个步骤，首先用正则提取数据内容，然后 html 转义处理，最终得到一个列表对象，返回最近发布的10篇文章。

```python
def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles
```

最终提取出来的数据总共有10条，就是最近发表的10条数据，我们看看每条数据返回有哪些字段。

```python
article = {'app_msg_ext_info': 
                {'title': '11月赠书，总共10本，附Python书单',
                 'copyright_stat': 11,
                 'is_multi': 1,
                 'content': '',
                 'author': '刘志军',
                 'subtype': 9,
                 'del_flag': 1,
                 'fileid': 502883895,
                 'content_url': 'http:\\/\\/mp.weixin.qq.com...',
                 ''
                 'digest': '十一月份赠书福利如期而至，更多惊喜等着你',
                 'cover': 'http:\\/\\/mmbiz.qpic.cn\\...',
                 'multi_app_msg_item_list': [{'fileid': 861719336,
                                              'content_url': 'http:\\/\\/mp.weixin.qq.com',
                                              'content': '', 'copyright_stat': 11,
                                              'cover': 'http:\\/\\/mmbiz.qpic.cn',
                                              'del_flag': 1,
                                              'digest': '多数情况下，人是种短视的动物',
                                              'source_url': '',
                                              'title': '罗胖60秒：诺贝尔奖设立时，为何会被骂？',
                                              'author': '罗振宇'
                                              }],
                 'source_url': 'https:\\/\\/github.com\'
                 },
      'comm_msg_info': {'datetime': 1511827200,
                        'status': 2,
                        'id': 1000000161,
                        'fakeid': '2393828411',
                        'content': '',
                        'type': 49}}
```
我们结合下面这张图来看：

![](https://user-gold-cdn.xitu.io/2017/12/29/1609e23c801d5770?w=400&h=599&f=png&s=271704)

上面这张图是微信作为单次推送发给用户的多图文消息，有发送时间对应`comm_msg_info.datetime`，`app_msg_ext_info`中的字段信息就是第一篇文章的字段信息，分别对应：

* title：文章标题
* content_url：文章链接
* source_url：原文链接，有可能为空
* digest：摘要
* cover：封面图
* datetime：推送时间

后面几篇文章以列表的形式保存在 `multi_app_msg_item_list` 字段中。

到此，公众号文章的基本信息就抓到了，但也仅仅只是公众号的前10条推送，如何获取更多历史文章等问题放在下节讲解。

本节完整代码可以在GitHub仓库[weixincrawler_v](https://github.com/pythonzhichan/weixincrawler/tree/v0.1)查看。


## 4抓取微信公众号所有历史文章

# 抓取公众号所有历史文章

我们按照第三节使用 Fiddler 抓包方式，打开手机某个微信公众号历史文章列表，上拉加载更多，找到加载更多文章的 URL 请求地址，你会看到 Fiddler 会有一个加载更多文章列表的请求。


![](https://user-gold-cdn.xitu.io/2017/12/23/1607f86a0e361895?w=1218&h=628&f=jpeg&s=138352)

### 分析抓包数据

该接口返回的数据是 JSON 格式，这种数据格式处理起来非常方便，首先我们把数据拷贝到 Chrome 插件 JSON Editor 或者找一个[JSON Online Formatter](https://jsonformatter.curiousconcept.com/) 对返回的数据进行格式化处理，以便查看每个字段所代表的意义。


![](https://user-gold-cdn.xitu.io/2017/12/23/1607f86e8b11adca?w=564&h=286&f=jpeg&s=22098)

你可以大概猜出来每个字段的意思

* ret：请求是否成功，0就表示成功
* msg_count： 返回的数据条数
* can_msg_continue： 是否还有下一页数据
* next_offset： 下一次请求的起始位置
* general_msg_list：真实数据

`general_msg_list`是历史文章里面的基本信息，包括每篇文章的标题、发布时间、摘要、链接地址、封面图等，而像文章的阅读数、点赞数、评论数、赞赏数这些数据都需要通过额外接口获取。

### 代码实现

分析完后，用代码实现其实非常简单，按照上节的方式，我们把 URL 和 Header 信息直接从 Fiddler 中拷贝过来。

```python
# crawler.py
# -*- coding: utf-8 -*-

import logging
import utils
import requests

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


class WeiXinCrawler:
    def crawl(self):
        """
        爬取更多文章
        :return:
        """
        url = "https://mp.weixin.qq.com/mp/profile_ext?" \
                "action=getmsg&" \
                "__biz=MjM5MzgyODQxMQ==" \
                "&f=json&" \
                "offset=11&" \
                "count=10&" \
                "is_ok=1" \
                "&scene=124&" \
                "uin=777&key=777&" \
                "pass_ticket=25llsA6zWUPC9KHOvP4oE%2BQwJ3nS%2F3CjeWxeKBjDhxCb7V1lQQJa6d0ZrgSmCvWa&wxtoken=&" \
                "appmsg_token=936_qKN8I1KSEO%252BWB2YUShHV8kgkIGXgzl-CT8JJpw~~&" \
                "x5=0&" \
                "f=json"


        headers = """
                    Host: mp.weixin.qq.com
                    .... 省略了，自己补充 ...
                    """
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            logger.info("抓取数据：offset=%s, data=%s" % (offset, msg_list))
        else:
            # 错误消息
            # {"ret":-3,"errmsg":"no session","cookie_count":1}
            logger.error("无法正确获取内容，请重新从Fiddler获取请求参数和请求头")
            exit()


if __name__ == '__main__':
    crawler = WeiXinCrawler()
    crawler.crawl()

```

成功爬取了第二页的数据，那么第三页呢，第四页呢？所以，我们还需要对该方法进行重构，使得它可以抓取公众号全部历史文章。通过字段 can_msg_continue 确定是否继续抓取，再结合 next_offset 就可以加载更多数据，我们需要把 url 中可变的参数 offset 用变量来代替，递归调用直到 `can_msg_continue` 为 0 说明所有文章都爬取完了。

```python
    def crawl(self, offset=0):
        """
        爬取更多文章
        :return:
        """
        url = "https://mp.weixin.qq.com/mp/profile_ext?" \
              "action=getmsg&" \
              "__biz=MjM5MzgyODQxMQ==&" \
              "f=json&" \
              "offset={offset}&" \
              "count=10&" \
              "is_ok=1&" \
              "scene=&" \
              "uin=777&" \
              "key=777&" \
              "pass_ticket=25llsA6zWUPC9KHOvP4oE+QwJ3nS/3CjeWxeKBjDhxCb7V1lQQJa6d0ZrgSmCvWa&" \
              "wxtoken=&" \
              "appmsg_token=936_qKN8I1KSEO%2BWB2YUShHV8kgkIGXgzl-CT8JJpw~~&" \
              "x5=1&" \
              "f=json".format(offset=offset)  # 请将appmsg_token和pass_ticket替换成你自己的

        headers = """
Host: mp.weixin.qq.com
.... 省略了，自己补充 ...
"""
        headers = utils.str_to_dict(headers)
        response = requests.get(url, headers=headers, verify=False)
        result = response.json()
        if result.get("ret") == 0:
            msg_list = result.get("general_msg_list")
            logger.info("抓取数据：offset=%s, data=%s" % (offset, msg_list))
            # 递归调用
            has_next = result.get("can_msg_continue")
            if has_next == 1:
                next_offset = result.get("next_offset")
                time.sleep(2)
                self.crawl(next_offset)
        else:
            # 错误消息
            # {"ret":-3,"errmsg":"no session","cookie_count":1}
            logger.error("无法正确获取内容，请重新从Fiddler获取请求参数和请求头")
            exit()
```

当 has_next 为 0 时，说明已经到了最后一页，这时才算爬完了一个公众号的所有历史文章，现在把所有的文章摘要数据抓取下来了，但是数据还没有存储，下一节，我们将使用MongoDB将数据进行持久化。

本节完整代码地址：[weixincrawler/v0.2](https://github.com/pythonzhichan/weixincrawler/tree/v0.2)


## 5将爬取的文章存储到MongoDB

# 将爬取的文章存储到MongoDB

关于数据的存储有很多选择，最简单的方式就是直接保存到 CSV 文件中，这种方式操作简单，适合数据量少的情况，Python的标准库 `csv` 模块就可以直接支持。如果遇到数据量非常大的情况，就必须要用到专业的数据库系统，你既可以使用 MySQL 这样的关系型数据库，也可以使用 MongoDB 一类的文档型数据库。用Python 操作 MongoDB 非常方便，无需定义表结构就可以直接将数据插入，所以我们在这一节采用 MongoDB 来存储数据。

### MongoDB 安装

MongoDB 目前最新版本是3.6，在官网地址[https://www.mongodb.com/download-center#community](https://www.mongodb.com/download-center#community)选择相应平台下载安装。


![](https://user-gold-cdn.xitu.io/2017/12/25/1608ae95b25c3215?w=1071&h=465&f=png&s=34487)

Windows 默认安装在 C:\Program Files\MongoDB\Server\3.6\，macOS 也可以直接通过 brew 命令安装，Linux平台直接下载压缩包解压即可。

```
brew install mongodb --with-openssl
```

### 启动 MongoDB

```
mongod --dbpath <path to data directory> 
```

默认端口是 27017，为了更好的查看数据，我们可以装一个 MongoDB 客户端， 官方自带有 compass，也可以下载第三方工具 Robo 3T [https://robomongo.org/](https://robomongo.org/)，这里推荐大家使用免费的 Robo 3T。


![](https://user-gold-cdn.xitu.io/2017/12/25/1608aea6b3f9332f?w=546&h=382&f=png&s=7891)


### MongoEngine

MongoEngine 是 MongoDB 的 DOM（Document-Object Mapper）框架，一种类似于关系型数据库中的ORM框架 ，使用它可以更方便并写出简洁的代码

安装

```
$ pip install mongoengine
```

连接

```python
from mongoengine import connect
# 连接 mongodb，无需事先创建数据库
connect('weixin', host='localhost', port=27017)
```

定义数据模型

```python
# -*- coding: utf-8 -*-
from datetime import datetime

from mongoengine import DateTimeField
from mongoengine import Document
from mongoengine import IntField
from mongoengine import StringField
from mongoengine import URLField
from mongoengine import connect

__author__ = "liuzhijun"

# 连接 mongodb
connect('weixin2', host='localhost', port=27017)


class Post(Document):
    """
    文章信息
    """
    title = StringField()  # 文章标题
    content_url = StringField()  # 文章链接
    content = StringField()  # 文章内容
    source_url = StringField()  # 原文链接
    digest = StringField()  # 文章摘要
    cover = URLField(validation=None)  # 封面图
    p_date = DateTimeField()  # 推送时间

    read_num = IntField(default=0)  # 阅读数
    like_num = IntField(default=0)  # 点赞数
    comment_num = IntField(default=0)  # 评论数
    reward_num = IntField(default=0)  # 赞赏数
    author = StringField()  # 作者

    c_date = DateTimeField(default=datetime.now)  # 数据生成时间
    u_date = DateTimeField(default=datetime.now)  # 最后更新时间

```

### 数据保存

在第五小节中，我们只是把抓取的数据简单的打印出来，现在我们就把它存数据库，因为抓取的数据中有很多无用的字段，所以，这里我们写一个工具函数叫 `sub_dict` 用于获取指定字段信息。

```python
import html
def sub_dict(d, keys):
    return {k: html.unescape(d[k]) for k in d if k in keys}

d = {"a": "1", "b": 2, "c": 3}
sub_dict(d, ["a", "b"]) # {"a":"1", "b": "2"}
```

获取字典的子字典可以用字典推导式实现，我这里还导入了`html.unescape`方法是希望保存到数据库的数据都是经过反转义处理的。


```python
    @staticmethod
    def save(msg_list):

        msg_list = msg_list.replace("\/", "/")
        data = json.loads(msg_list)
        msg_list = data.get("list")
        for msg in msg_list:
            p_date = msg.get("comm_msg_info").get("datetime")
            msg_info = msg.get("app_msg_ext_info")  # 非图文消息没有此字段
            if msg_info:
                WeiXinCrawler._insert(msg_info, p_date)
                multi_msg_info = msg_info.get("multi_app_msg_item_list") # 多图文推送，把第二条第三条也保存
                for msg_item in multi_msg_info:
                    WeiXinCrawler._insert(msg_item, p_date)
            else:
                logger.warning(u"此消息不是图文推送，data=%s" % json.dumps(msg.get("comm_msg_info")))

    @staticmethod
    def _insert(item, p_date):
        keys = ('title', 'author', 'content_url', 'digest', 'cover', 'source_url')
        sub_data = utils.sub_dict(item, keys)
        post = Post(**sub_data)
        p_date = datetime.fromtimestamp(p_date)
        post["p_date"] = p_date
        logger.info('save data %s ' % post.title)
        try:
            post.save()
        except Exception as e:
            logger.error("保存失败 data=%s" % post.to_json(), exc_info=True)

```

如果是文字推送就没有`app_msg_ext_info`字段，无需保存，`multi_app_msg_item_list`是多图文推送字段，而且和外层的`app_msg_ext_info`字段是一致的，有标题、封面图、摘要、链接等信息，所以我们把插入数据库的代码`_insert`作为私有方法抽离出来共用。


最后我们看一下保存的数据。



![](https://user-gold-cdn.xitu.io/2017/12/29/1609e87c99c34c71?w=1394&h=814&f=png&s=257664)


### 小结

本节完成代码在GitHub [v0.3](https://github.com/pythonzhichan/weixincrawler/tree/v0.3)，这小节我们主要熟悉 Mongodb 的安装以及如何用Python连接 Mongodb 进行数据存储，推荐两个资源，第一个是：[《MongoDB 入门指南》](https://jockchou.gitbooks.io/getting-started-with-mongodb/content/)，第二个是 [MongoEngine 教程](http://docs.mongoengine.org/index.html)，如果你想进行系统的学习 MongoDB，推荐两本书籍《MongoDB权威指南》和《MongoDB实战》。

## 6获取文章阅读数、点赞数、评论数、赞赏数

# 获取文章阅读数、点赞数、评论数、赞赏数

如果只是获取所有文章的基本信息价值并不大，最多能对文章做检索，只有得到文章的阅读数、点赞数、评论数和赞赏数之后数据才有数据分析的价值。这节就来讨论如何获取这些数据。


### 抓包分析

点开任意一篇文章，通过 Fiddler 或 Charles 抓包分析，逐个分析每个请求，通过观察发现获取文章阅读数、点赞数的URL接口为（我们命名为 data_url）：https://mp.weixin.qq.com/mp/getappmsgext ，后面有很多查询参数，请求方法为 POST


![](https://user-gold-cdn.xitu.io/2018/1/4/160bfdc73a91ccf2?w=1105&h=662&f=jpeg&s=137185)

该请求的查询参数有28个之多，另外还附有请求 Body。


![](https://user-gold-cdn.xitu.io/2018/1/4/160bfdcc3f9674dd?w=840&h=330&f=jpeg&s=76312)

返回的响应数据是JSON格式，根据字段名称基本能猜出其中的意义，阅读数、点赞数、赞赏数都包含在其中

```python
{
    "advertisement_num": 0, 
    "advertisement_info": [ ], 
    "appmsgstat": {
        "show": true, 
        "is_login": true, 
        "liked": false, 
        "read_num": 6395,  # 阅读数
        "like_num": 190,   # 点赞数
        "ret": 0, 
        "real_read_num": 0
    }, 
    "comment_enabled": 1, 
    "timestamp": 1514972862, 
    "reward_head_imgs": [  # 赞赏头像列表
        "http://wx.qlogo.cn/mmhead/V3bYdzb7P4DLf3e7Xf74qSicESO8QdeupE5ibs8YI6xibE/132", 
        "http://wx.qlogo.cn/mmhead/Q3auHgzwzM7KF8PIsOicjLuRpsRzFhibeKs3sHFJGKkxDguAnF2gQJdA/132", 
    ], 
    "reward_total_count": 16,  # 赞赏数
    "can_reward": 1, 
    "only_fans_can_comment": true, 
    "user_can_reward": 1, 
    "reward_qrcode_ticket": "%2B%2FfLw%2BXXGQwDD0ik6GwpMhSzLBMFCkwhjpXhStXNjXo%3D", 
    "base_resp": {
        "wxtoken": 723698581
    }
}
 ```

确定了请求的URL及查询参数，请求方法，请求体，请求头也能查看到，返回的数据也有了，剩下的问题是如何批量获取不同文章的数据，这需要从请求的 data_url 着手分析。

为了找出 data_url 中查询参数的规律，先对比文章详情的 content_url （就是在上一节得到的文章详情URL）

```
# 文章的URL
content_url = "http://mp.weixin.qq.com/s?" \
              "__biz=MjM5MzgyODQxMQ==&" \
              "mid=2650367413&idx=1&" \
              "sn=637de06b162c21605eef3db41ee4a1bb&" \
              "chksm=be9cdee189eb57f78994371ce1b5b42656bf77160eeee592507df06bae0cea58b542aeabe0a4&" \
              "scene=27"
```

不得而知，`__biz`，mid，idx，sn，scene，chksm 是构成一篇文章的完整URL，而文章阅读数的URL是：

```
# 阅读数URL
data_url = "https://mp.weixin.qq.com/mp/getappmsgext?" \
           "__biz=MjM5MzgyODQxMQ==&" \
           "appmsg_type=9&" \
           "mid=2650367720&" \
           "sn=87e32a97392f320c17960c31f1035182&" \
           "idx=1&" \
           "scene=27&" \
           "title=2018%20%E5%B9%B4%EF%BC%8C%E5%AD%A6%E7%82%B9%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%EF%BC%88%E8%B5%A0%E4%B9%A68%E6%9C%AC%EF%BC%89&" \
           "ct=1514505600&" \
           "abtest_cookie=AwABAAoADAANAAkAJIgeAGKIHgD8iB4Ab4keAPiJHgAHih4AD4oeAEyKHgBdih4AAAA=&" \
           "devicetype=iOS10.3.3&" \
           "version=/mmbizwap/zh_CN/htmledition/js/appmsg/index3a9713.js&" \
           "f=json&" \
           "r=0.341679623927889&is_need_ad=0&" \
           "comment_id=2810810222&" \
           "is_need_reward=1&" \
           "both_ad=0&" \
           "reward_uin_count=27&" \
           "msg_daily_idx=1&" \
           "is_original=0&" \
           "uin=777&" \
           "key=777&" \
           "pass_ticket=y0QRNge7UkQaFPA9SKuvpeee2eNqvasPGVmFo9z8MUBt4ApaTKt0Ps38VaDKpqQ6&" \
           "wxtoken=217065932&" \
           "devicetype=iOS10.3.3&" \
           "clientversion=16060123&" \
           "appmsg_token=938_vSjt2FisNybtpLZCYw5DGyn0L2PK7qpCkzVlZySGKUjQDC0UMw3SNoS1Atum66a7ElZYWWb5amRtAy8m&" \
           "x5=0&" \
           "f=json"
```

对比两个URL，你会发现 content_url 中的参数除了 chksm 其它几个参数都在 data_url 中，我们把 content_url 中的参数替换到 data_url 再来验证请求会不会正常返回数据。至于其他参数要不要改，怎么改我们先放一边（这是一个不断猜想、验证的过程，经过我的多次试验，除了 appmsg_token 有一定的时效之外，其它值可以保持不变，也就是说不同的文章，只要把content_url中的参数替换到 data_url 中就可以获取该文章的数据了。）


### 代码实现


```python
    @staticmethod
    def update_post(post):
        """
        post 参数是从mongodb读取出来的一条数据
        稍后就是对这个对象进行更新保存
        :param post:
        :return:
        """

        # 这个参数是我从Fiddler中拷贝出 URL，然后提取出查询参数部分再转换成字典对象
        # 稍后会作为参数传给request.post方法
        data_url_params = {'__biz': 'MjM5MzgyODQxMQ==', 'appmsg_type': '9', 'mid': '2650367727',
                           'sn': '08ce54f6f36873e74c638421012bb495', 'idx': '1', 'scene': '0',
                           'title': '2017%E5%B9%B4%EF%BC%8C%E6%84%9F%E8%B0%A2%E4%BD%A0%E4%BB%AC%EF%BC%8C2018%E5%B9%B4%EF%BC%8C%E6%88%91%E4%BB%AC%E7%BB%A7%E7%BB%AD%E5%8A%AA%E5%8A%9B%E5%89%8D%E8%A1%8C',
                           'ct': '1514796292',
                           'abtest_cookie': 'AwABAAoADAANAAgAJIgeALuIHgDhiB4A/IgeAPqJHgANih4ATYoeAF6KHgAAAA==',
                           'devicetype': 'android-24',
                           'version': '/mmbizwap/zh_CN/htmledition/js/appmsg/index3a9713.js', 'f': 'json',
                           'r': '0.6452677228890584', 'is_need_ad': '1', 'comment_id': '1741225191',
                           'is_need_reward': '1', 'both_ad': '0', 'reward_uin_count': '24', 'msg_daily_idx': '1',
                           'is_original': '0', 'uin': '777', 'key': '777',
                           'pass_ticket': 'mXHYjLnkYux1rXx8BxNrZpgW4W%252ByLZxcuvpDWlxbBrjvJo3ECB%252BckDAsy%252FTJJK6P',
                           'wxtoken': '1805512665', 'clientversion': '26060133',
                           'appmsg_token': '938_VN3Rr7O4RIU7lm%2F8_amSJbZBo3RJXACjIMDwDu5ZPbSm2_SW6RpnZGb2Vrp6ECxr9y5QoVCI7H-iQotJ',
                           'x5': '1'}

        # url转义处理
        content_url = html.unescape(post.content_url)
        # 截取content_url的查询参数部分
        content_url_params = urlsplit(content_url).query
        # 将参数转化为字典类型
        content_url_params = utils.str_to_dict(content_url_params, "&", "=")
        # 更新到data_url
        data_url_params.update(content_url_params)
        body = "is_only_read=1&req_id=03230SZyTR8kQlPVkKwxbt1A&pass_ticket=mXHYjLnkYux1rXx8BxNrZpgW4W%25252ByLZxcuvpDWlxbBrjvJo3ECB%25252BckDAsy%25252FTJJK6P&is_temp_url=0"
        data = utils.str_to_dict(body, "&", "=")

        headers = """
Host: mp.weixin.qq.com
Connection: keep-alive
Content-Length: 155
Origin: https://mp.weixin.qq.com
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Linux; Android 7.0; M1 E Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060133) NetType/WIFI Language/zh_CN
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept: */*
Referer: https://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650367727&idx=1&sn=08ce54f6f36873e74c638421012bb495&chksm=be9cddbb89eb54ad436af5c27c0d0db06da7e3aec613a33dd99f935d684a77b555241207f1ba&scene=0&ascene=7&devicetype=android-24&version=26060133&nettype=WIFI&abtest_cookie=AwABAAoADAANAAgAJIgeALuIHgDhiB4A%2FIgeAPqJHgANih4ATYoeAF6KHgAAAA%3D%3D&lang=zh_CN&pass_ticket=mXHYjLnkYux1rXx8BxNrZpgW4W%2ByLZxcuvpDWlxbBrjvJo3ECB%2BckDAsy%2FTJJK6P&wx_header=1
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,en-US;q=0.8
Cookie: rewardsn=05c38771473771b68376; wxtokenkey=92c034f1d4d5cfe011a9222522d96c3af508a6e35160b5f6fefa185431bda832; wxuin=525477518; devicetype=android-24; version=26060133; lang=zh_CN; pass_ticket=mXHYjLnkYux1rXx8BxNrZpgW4W+yLZxcuvpDWlxbBrjvJo3ECB+ckDAsy/TJJK6P; wap_sid2=CI7NyPoBElx2ZFNJVXFOVFh2S3U5X1hLS2pZb2Z0Ujd1NTBPdlMzbEpwMjdVRlYtTHluRWkwZzIwUzY4ZVM3Y294MzU5aDM5eWxfRWVKOVJoY0dvVmZuQTk2S1JLS29EQUFBfjCQ5LPSBTgNQAE=
Q-UA2: QV=3&PL=ADR&PR=WX&PP=com.tencent.mm&PPVN=6.6.1&TBSVC=43602&CO=BK&COVC=043632&PB=GE&VE=GA&DE=PHONE&CHID=0&LCID=9422&MO= M1E &RL=1080*1920&OS=7.0&API=24
Q-GUID: 0fd685fa8c515a30dd9f7caf13b788cb
Q-Auth: 31045b957cf33acf31e40be2f3e71c5217597676a9729f1b
        """

        headers = utils.str_to_dict(headers)

        data_url = "https://mp.weixin.qq.com/mp/getappmsgext"
        
        r = requests.post(data_url, data=data, verify=False, params=data_url_params, headers=headers)

        result = r.json()
        if result.get("appmsgstat"):
            post['read_num'] = result.get("appmsgstat").get("read_num")
            post['like_num'] = result.get("appmsgstat").get("like_num")
            post['reward_num'] = result.get("reward_total_count")
            post['u_date'] = datetime.now()
            logger.info("「%s」read_num: %s like_num: %s reward_num: %s" %
                        (post.title, post['read_num'], post['like_num'], post['reward_num']))
            post.save()
        else:
            logger.warning(u"没有获取的真实数据，请检查请求参数是否正确，返回的数据为：data=%s" % r.text)
```

需要注意的是 iOS 没有赞赏功能，所以如果要获取赞赏数据，我们必须用 Android 设备来抓取数据。现在就来遍历更新每条数据的内容：

```python
  crawler = WeiXinCrawler()
    for post in Post.objects(read_num=0):
        crawler.update_post(post)
        time.sleep(1) # 防止恶意刷
```

不出意外的话，能正常获取到数据，在抓取的过程中，微信会有反爬虫限制，爬了一段时间后，返回的数据成了：

```
{"base_resp":{"ret":301,"errmsg":"default"}}
```

这个时候需要休息一会儿才能继续爬虫，换IP也没用，因为微信会根据你的微信账号进行限制，如果需要大规模爬虫就有必要准备多个微信号来操作。本节完整代码：[weixincrawler-v0.4](https://github.com/pythonzhichan/weixincrawler/tree/v0.4)

## 7搭建数据分析环境：Anaconda、Jupyter Notebook

# 搭建数据分析环境：Anaconda、Jupyter Notebook
Anaconda 是一个针对数据分析领域的 Python 发行版本，它提供了包管理（packages）工具和虚拟环境（environment）管理， `conda` 命令可用于安装、卸载、更新包、创建不同版本的 Python 独立环境，可用于替换 `pip` 和 `virtualenv` 这两个工具。此外，Anaconda 自带了很多数据科学的依赖包以及Juypter Notebook 等工具。


### Anaconda 下载安装

可直接从 Anaconda [官方网站](https://www.anaconda.com/download/)进行下载，选择 Python3.6 的版本，因为 Python2.7即将被废弃，下载后根据提示安装即可


![](https://user-gold-cdn.xitu.io/2018/1/7/160cc8346a38b48e?w=748&h=417&f=png&s=70931)



macOS/Linux 安装完成之后会自动把 Anaconda 添加到 PATH 环境变量（在 ~/.bash_profile 文件中可以看到），如果你的终端默认 SHELL 不是 bash 的话（用 `echo $SHELL` 查看默认 shell 是啥），加了系统也找不到 conda 命令，比如我的 mac 默认 shell 是 zsh ，需要把下面这行添加到 ~/.zshrc 文件中

```
# added by Anaconda3 5.0.1 installer
export PATH="/Users/你的用户名/anaconda3/bin:$PATH"
```

再检查 conda 命令是否能用

```
conda -V
conda 4.3.30
```

Windows 平台安装的时候请自动勾选加入 PATH 路径，如果安装的时候没有勾选，要手动找到 Anoconda 的安装路径加入到 PATH 变量中，否则一样找不到 conda 命令。


![](https://user-gold-cdn.xitu.io/2018/1/7/160cc8307b95901c?w=499&h=387&f=png&s=21224)

为了使用 conda 安装包的过程中加快速度，可以把镜像地址修改为国内清华大学的镜像：编辑  ~/.condrc，（Windows 是在C:\Users\你的用户名\.condrc，如果没有该文件就创建一个），添加内容：
```
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
ssl_verify: false
show_channel_urls: true

```


### 常用 conda 命令

包管理

```python
# 查看帮助
conda -h 
# 查看conda版本
conda --version
# 安装 matplotlib 
conda install matplotlib
# 查看已安装的包
conda list 
# 包更新
conda update matplotlib
# 删除包
conda remove matplotlib
```

环境管理

```python
# 基于python3.6版本创建一个名字为test的python独立环境
conda create --name test python=3.6 
# 激活此环境
activate test  
source activate test # linux/mac
# 退出当前环境
deactivate test 
# 删除该环境
conda remove -n test --all
# 或者 
conda env remove  -n test

# 查看所有安装的python环境
conda info -e
test              *  D:\Programs\Anaconda3\envs\test
root                     D:\Programs\Anaconda3（安装 conda 默认生成的）

```

其他命令

```python
# 更新conda本身
conda update conda
# 更新anaconda 应用
conda update anaconda
# 更新python，假设当前python环境是3.6.1，而最新版本是3.6.2，那么就会升级到3.6.2
conda update python
```


安装完 Anoconda 之后，Jupyter Notebook 也装好了。


Jupyter Notebook 是一个强大的数据分析工具，你可以在上面写代码、运行代码、写文档、列方程式、做数据可视化展示。 正如其名，它就像一个草稿本可以在上面随意地涂写改改画画，画错了还可以擦除重做。

### 启动jupyter
在命令行直接输入：
```
jupyter notebook
```

Jupyter 启动成功后，在浏览器中会自动打开 notebook 的主界面，新建一个notebook时要点击右上角的 `New`，选择 Python3 ，这里的 Python3 就是 jupyter 的内核，是安装 Anaconda 的时候的名字为root的默认 python 环境。


![](https://user-gold-cdn.xitu.io/2018/1/7/160cc83cabb5d763?w=1251&h=500&f=gif&s=530756)


新建了 notebook 之后你就可以在单元格里面写代码或者写 markdown 文档，或者基于用 matplotlib 制图。



![](https://user-gold-cdn.xitu.io/2018/1/7/160cc83ff1e148dc?w=1292&h=544&f=png&s=60523)


### 补充

如何查看 jupyter 使用了哪些 kernel

```
 ~ jupyter kernelspec list

Available kernels:
  weixin     /Users/xxx/Library/Jupyter/kernels/weixin
  python3    /Users/xxx/anaconda3/share/jupyter/kernels/python3
```

如何新增 kernel

```
# 创建python环境
conda create -n weixin python=3.6 
# 激活
source activate weixin
# 加入到juypter
python -m ipykernel install --user --name weixin --display-name "Python (weixin)"

```

![](https://user-gold-cdn.xitu.io/2018/1/7/160cc849749ca1a9?w=645&h=319&f=png&s=21108)

新增了 kernel 之后，你可以在不同的 kernel 之间切换运行代码，本质上 kernel 还是 Python 的虚拟环境。


推荐一个Jupyter Notebook 的视频教程：[Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough](https://www.youtube.com/watch?v=HW29067qVWk)（需要翻墙）

## 8利用 Pandas 对爬取数据进行分析

# 数据分析工具 Pandas 介绍


### 什么是Pandas

Pandas 是做数据分析的基础包，提供了灵活的数据结构和其它方便进行向量化计算的工具和函数, 使得 Python 也能够像 R 语言一样方便地用于数据分析和处理。在 Pandas 中有两种常见数据结构，分别是 Series 和 DataFrame。

Series 是一种增强型的一维数组，与 Python 中的列表相似，由 index（索引）和 values（值）组成， Series 中的值是相同的数据类型。



![](https://user-gold-cdn.xitu.io/2018/1/14/160f4bfd5f87c0d3?w=301&h=265&f=jpeg&s=7172)
而 DataFrame 是增强型的二维数组，就像 Excel 中的表格，有行标签和列表索引，这种数据结构在Pandas 中最为常用。


![](https://user-gold-cdn.xitu.io/2018/1/15/160f6ed775ea137d?w=429&h=339&f=jpeg&s=14268)


在做数据分析前，我们会约定俗成地引入 Numpy 、Pandas、Matplotlib 三个工具包，并使用其简称 np，pd，plt。numpy 是科学计算基础包，pandas 依赖于 numpy，而 matplitlib 是绘图工具。(以下代码均在 IPython 中完成，如果你已经成功安装了 Anoconda，那么可以直接运行 `ipython` 命令进入)


```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### Series

用列表可创建Series对象

```python
In [30]: s = pd.Series(['a','b','c'])

In [31]: s
Out[31]:
0    a
1    b
2    c
dtype: object
```

Series 和列表一样每个元素有对应的索引，默认是0到n（n是列表的长度），也手动指定索引名字

```python
In [42]: s = pd.Series(['a','b','c'], index=['x','y','z'])

In [43]: s
Out[43]:
x    a
y    b
z    c
dtype: object
```

可以通过索引获取元素

```python
In [50]: s['x']
Out[50]: 'a'
```

像列表一样，支持切片
```python
In [51]: s[:2]
Out[51]:
x    a
y    b
dtype: object

```

可以使用字典创建Series（Series也可以看做是一个特殊的字典对象，都是索引到值的映射）
```python
In [272]: s2 = pd.Series({1:"a",2:"b",3:"c"})

In [273]: s2
Out[273]:
1    a
2    b
3    c
dtype: object
```

### DataFrame

有很多方法可以创建 DataFrame 对象，可以通过用相等长度的列表组成的字典对象来构建 DataFrame


```python
In [52]: data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
    ...:         'year': [2000, 2001, 2002, 2001, 2002],
    ...:         'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    ...:


In [54]: df = pd.DataFrame(data)

In [55]: df
Out[55]:
   pop   state  year
0  1.5    Ohio  2000
1  1.7    Ohio  2001
2  3.6    Ohio  2002
3  2.4  Nevada  2001
4  2.9  Nevada  2002
```

也可以通过 Numpy 的二维数组来构建 DataFrame

```python
# 随机生成6行4列的二维数组
In [58]:  df = pd.DataFrame(np.random.randn(6,4))

In [59]: df
Out[59]:
          0         1         2         3
0  0.447964 -0.486327 -1.593023 -0.314114
1  1.004132 -0.058186  0.076479  0.076231
2  0.445284  0.592718  0.214101 -0.322876
3 -0.006924 -0.738673  0.277461  0.448946
4  0.100352  1.416282  0.353527  0.640276
5  0.804352 -0.374634  0.734836  0.247061
```

还可以从 csv 文件、数据库中获取，现在先来熟悉 DataFrame 中常用属性和操作方法，以便后续能够灵活运用 Pandas。


DataFrame 既有行索引（index）也有列索引（columns），构建 DataFrame 时可以指定每行的名字和每列的名字，例如下面的 DataFrame 用时间作为行索引，字母 A、B、C、D 作为列索引。

```python
In [61]: dates = pd.date_range('20130101',periods=6)

In [62]: dates
Out[62]:
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [63]: df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

In [64]: df
Out[64]:
                   A         B         C         D
2013-01-01  0.513286 -1.475824  1.939876 -0.163942
2013-01-02 -0.518291  1.345230  0.510746  1.284767
2013-01-03 -0.434865 -0.464227  1.830259 -0.719290
2013-01-04  0.654418 -0.994241  0.162705  2.816623
2013-01-05  1.540274 -0.227124  1.843401 -2.977880
2013-01-06  0.888156  1.932291  0.998568  0.143846
```


DataFrame 其实就是由3部分组成的，分别是 index、columns、values

```python
In [79]: df.columns
Out[79]: Index(['A', 'B', 'C', 'D'], dtype='object')

In [80]: df.index
Out[80]:
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [81]: df.values
Out[81]:
array([[ 0.51328621, -1.475824  ,  1.93987575, -0.16394233],
       [-0.51829132,  1.34522999,  0.51074601,  1.2847668 ],
       [-0.43486491, -0.46422712,  1.83025914, -0.71928957],
       [ 0.65441841, -0.99424111,  0.16270488,  2.81662335],
       [ 1.54027403, -0.22712424,  1.84340078, -2.97787999],
       [ 0.88815632,  1.93229088,  0.99856774,  0.14384553]])
```


### head()

head() 返回 DataFrame 的头部数据（默认返回表格中的前5行数据），也可以指定返回的行数

```python
In [70]: df.head(3)
Out[70]:
                   A         B         C         D
2013-01-01  0.513286 -1.475824  1.939876 -0.163942
2013-01-02 -0.518291  1.345230  0.510746  1.284767
2013-01-03 -0.434865 -0.464227  1.830259 -0.719290
```

### tail()
tail() 返回 DataFrame 的尾部数据（默认返回表格中的最后5行数据）

```python
In [72]: df.tail()
Out[72]:
                   A         B         C         D
2013-01-02 -0.518291  1.345230  0.510746  1.284767
2013-01-03 -0.434865 -0.464227  1.830259 -0.719290
2013-01-04  0.654418 -0.994241  0.162705  2.816623
2013-01-05  1.540274 -0.227124  1.843401 -2.977880
2013-01-06  0.888156  1.932291  0.998568  0.143846
```


### 按索引排序

```python
# 按照列索引的降序排列：D->C->B->A 
In [96]: df.sort_index(axis=1, ascending=False)
Out[96]:
                   D         C         B         A
2013-01-01 -0.163942  1.939876 -1.475824  0.513286
2013-01-02  1.284767  0.510746  1.345230 -0.518291
2013-01-03 -0.719290  1.830259 -0.464227 -0.434865
2013-01-04  2.816623  0.162705 -0.994241  0.654418
2013-01-05 -2.977880  1.843401 -0.227124  1.540274
2013-01-06  0.143846  0.998568  1.932291  0.888156

# 按照行索引的降序排列：2012-01-06->...->2013-01-01
In [97]: df.sort_index(axis=0, ascending=False)
Out[97]:
                   A         B         C         D
2013-01-06  0.888156  1.932291  0.998568  0.143846
2013-01-05  1.540274 -0.227124  1.843401 -2.977880
2013-01-04  0.654418 -0.994241  0.162705  2.816623
2013-01-03 -0.434865 -0.464227  1.830259 -0.719290
2013-01-02 -0.518291  1.345230  0.510746  1.284767
2013-01-01  0.513286 -1.475824  1.939876 -0.163942
```

### 按值排序

```python
# 根据B列的值的升序排列
In [99]: df.sort_values(by='B')
Out[99]:
                   A         B         C         D
2013-01-01  0.513286 -1.475824  1.939876 -0.163942
2013-01-04  0.654418 -0.994241  0.162705  2.816623
2013-01-03 -0.434865 -0.464227  1.830259 -0.719290
2013-01-05  1.540274 -0.227124  1.843401 -2.977880
2013-01-02 -0.518291  1.345230  0.510746  1.284767
2013-01-06  0.888156  1.932291  0.998568  0.143846

# 先按A的升序排，再按B的降序排
In [161]: df.sort_values(by=['A','B'], ascending=[True, False])
Out[161]:
                   A         B         C         D
2013-01-02 -0.518291  1.345230  0.510746  1.284767
2013-01-03 -0.434865 -0.464227  1.830259 -0.719290
2013-01-01  0.513286 -1.475824  1.939876 -0.163942
2013-01-04  0.654418 -0.994241  0.162705  2.816623
2013-01-06  0.888156  1.932291  0.998568  0.143846
2013-01-05  1.540274 -0.227124  1.843401 -2.977880
```

### 选择数据

```python
# 选择一列，返回 Series 对象
In [100]: df['A']
Out[100]:
2013-01-01    0.513286
2013-01-02   -0.518291
2013-01-03   -0.434865
2013-01-04    0.654418
2013-01-05    1.540274
2013-01-06    0.888156
Freq: D, Name: A, dtype: float64

# 选择多列，返回 DataFrame 对象
In [102]: df[['A','B']]
Out[102]:
                   A         B
2013-01-01  0.513286 -1.475824
2013-01-02 -0.518291  1.345230
2013-01-03 -0.434865 -0.464227
2013-01-04  0.654418 -0.994241
2013-01-05  1.540274 -0.227124
2013-01-06  0.888156  1.932291
```

### 切片操作

```python
In [101]: df[0:3]
Out[101]:
                   A         B         C         D
2013-01-01  0.513286 -1.475824  1.939876 -0.163942
2013-01-02 -0.518291  1.345230  0.510746  1.284767
2013-01-03 -0.434865 -0.464227  1.830259 -0.719290
```

### 通过loc、.iloc 高效获取数据

```python
# 通过行索引切片获取指定列数据
In [145]: df.loc["2013-01-01":"2013-01-03", ['A','B']]
Out[145]:
                   A         B
2013-01-01  0.513286 -1.475824
2013-01-02 -0.518291  1.345230
2013-01-03 -0.434865 -0.464227

# 通过行号切片获取（1到4行，0到2列）数据
In [149]: df.iloc[1:4, 0:2]
Out[149]:
                   A         B
2013-01-02 -0.518291  1.345230
2013-01-03 -0.434865 -0.464227
2013-01-04  0.654418 -0.994241

```


### 通过条件过滤数据

```python
In [104]: df[df.A>0]
Out[104]:
                   A         B         C         D
2013-01-01  0.513286 -1.475824  1.939876 -0.163942
2013-01-04  0.654418 -0.994241  0.162705  2.816623
2013-01-05  1.540274 -0.227124  1.843401 -2.977880
2013-01-06  0.888156  1.932291  0.998568  0.143846
```

### 求和

```python
In [115]: df.sum()
Out[115]:
A    2.642979
B    0.116104
C    7.285554
D    0.384124
```

### 求平均值

```python
In [121]: df.mean()
Out[121]:
A    0.440496
B    0.019351
C    1.214259
D    0.064021
dtype: float64
```

### 求最大/小值

```python
In [157]: df.max()
Out[157]:
A    1.540274
B    1.932291
C    1.939876
D    2.816623

In [159]: df.min()
Out[159]:
A   -0.518291
B   -1.475824
C    0.162705
D   -2.977880
dtype: float64
```

### 分组 groupby

```python
In [252]: df.groupby('A').size()
Out[252]:
A
-0.518291    1
-0.434865    1
 0.513286    1
 0.654418    1
 0.888156    1
 1.000000    1
 1.540274    1
```

groupby 的参数还可以是函数

```python
# 添加E为时间列，根据时间的年进行分组
In [255]: df['E'] = df.index

In [256]: df
Out[256]:
                            A         B         C         D          E
2013-01-01 00:00:00  0.513286 -1.475824  1.939876 -0.163942 2013-01-01
2013-01-02 00:00:00 -0.518291  1.345230  0.510746  1.284767 2013-01-02
2013-01-03 00:00:00 -0.434865 -0.464227  1.830259 -0.719290 2013-01-03
2013-01-04 00:00:00  0.654418 -0.994241  0.162705  2.816623 2013-01-04
2013-01-05 00:00:00  1.540274 -0.227124  1.843401 -2.977880 2013-01-05
2013-01-06 00:00:00  0.888156  1.932291  0.998568  0.143846 2013-01-06
2014-01-06 00:00:00  1.000000  1.000000  1.000000  1.000000 2014-01-06

In [257]: df.groupby(lambda x : df.E[x].year).size()
Out[257]:
2013    6
2014    1
dtype: int64
```

关于Pandas更多详细的用法可以参考Pandas官方文档[https://pandas.pydata.org](https://pandas.pydata.org)，下一节我们将正式进入数据分析环节。

## 9基于 Matplotlib 实现数据可视化展示

# 基于 Matplotlib 实现数据可视化

上节我们介绍了 Pandas 的基本操作，这节我们使用 Pandas 结合 Matplotlib 对数据进行可视化展示。首先我们把数据加载到 Pandas，现在假设你已经拥有了数据，如果没有数据可以下载我给你准备的[JSON文件](https://github.com/pythonzhichan/weixincrawler/blob/master/post.csv)。


### 加载数据

启动 juypter notebook 之后基于Python3 新建一个 notebook，之所以不选择叫 weixin 的 Python 解释器是因为默认的 Python3 已经包含了所有的数据分析相关包，无需另外下载。


![](https://user-gold-cdn.xitu.io/2018/1/21/16118c88a86cb6fa?w=433&h=225&f=png&s=33460)

在终端查看我的系统里有哪些虚拟环境
```
conda info -e
# conda environments:
#
crawler-toturial         /Users/lzjun/anaconda3/envs/crawler-toturial
crawler_test             /Users/lzjun/anaconda3/envs/crawler_test
weixin                   /Users/lzjun/anaconda3/envs/weixin
root                  *  /Users/lzjun/anaconda3
```
以上是我系统里面用 conda 管理的虚拟环境，juypter notebook 中的 Python3 对应的就是 root 环境，我们现在切换到 root 环境来安装其它第三方包。

```
# windows 不需要加 source
source activate root
# 安装 pymongo
pip install pymongo
```

回到 jupyter notebook ，导入基础包（以下代码都是在 jupyter notebook 中完成）

```python
# 加这行不需要再写plt.show()，直接显示图像出来
%matplotlib inline 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

display_columns = ["title","read_num","like_num","comment_num","reward_num","p_date"]
```

#### 从 MongoDB 导入数据


```python
import pymongo
from pymongo import MongoClient
# 连接 mongodb
c = MongoClient()
cursor = c.weixin3['post'].find()
df = pd.DataFrame(list(cursor))

# 删除 "_id"列
df = df.drop("_id", axis=1)
# 重新设置列的顺序
df = df.reindex(columns=display_columns)
# 将p_date的数据类型从timestamp 转换成 datetime
df.p_date = pd.to_datetime(df['p_date'])
df.head()
```

前5条数据：


![](https://user-gold-cdn.xitu.io/2018/1/21/16118c8f2419b4cc?w=1622&h=480&f=png&s=112552)

#### 从 CSV 文件中导入

如果你的 MongoDB 没有数据，可以用我给你准备的[JSON文件](https://github.com/pythonzhichan/weixincrawler/blob/master/post.csv)，下载到本地后用 Pandas 导入进来

```python
# 从csv文件中加载
df = pd.read_csv("post.csv")
# 重新设置列的顺序
df = df.reindex(columns=display_columns)
# 将p_date的数据类型从timestamp 转换成 datetime
df.p_date = pd.to_datetime(df['p_date'])
```

### 文章与阅读数

数据加载到 Pandas 之后，先来看下数据的总体概览情况


![](https://user-gold-cdn.xitu.io/2018/1/21/16118c955d78d595?w=900&h=457&f=png&s=115980)

从上面看出公众号一共发了 203 篇文章，文章平均阅读量是 2404，标准差 2005 说明文章阅读量波动非常大，从最高阅读量 8628 到最低阅读量 124 可以证明其波动性。为什么标准差这么大呢？这个其实很容易说明，因为公众号初期订阅读者少，阅读量也不高，但是随着你读者越来越多，阅读量也会越来越高。

这里的文章赞赏数和点赞数有一定的误差，因为我在初始化数据的时候，给每篇文章赞赏数默认设置为了0，而正确的方式应该是设置为None，如果为None 数据就不会统计进来。


获取阅读量最高的10篇文章


```python
# 根据阅读数排序，ascending 表示降序排列
top_read_num_10 = df.sort_values(by=['read_num'], ascending=False)[:10]
top_read_num_10 = top_read_num_10[display_columns]
# 重置行索引，drop 表示删除原来的行索引
top_read_num_10.reset_index(drop=True)
```

![](https://user-gold-cdn.xitu.io/2018/1/21/16118c9e029b92fb?w=1582&h=852&f=png&s=183651)

历史文章阅读量变化曲线

```python
ax = df.plot(y='read_num', x='p_date', title="文章阅读量趋势",figsize=(9,6))
# 设置y轴标签
ax.set_ylabel("阅读量")
# 设置x轴标签
ax.set_xlabel("")
# 隐藏图例
ax.legend().set_visible(False)
```

![](https://user-gold-cdn.xitu.io/2018/1/21/16118d08578cce2f?w=560&h=355&f=png&s=23710)

一眼就看出来，阅读量都集中在 2017 这一年，那么前几年究竟发生什么了？是没写文章还是写了文章没人看？我们来统计一下这几年的文章数。



![](https://user-gold-cdn.xitu.io/2018/1/21/16118d15aab3de9b?w=1478&h=620&f=png&s=81099)

数据告诉我们，13年发了2篇文章（笑cry表情），而17年发了 149 篇文章（棒棒哒），平均每周大概有近 3 篇文章的更新频率，用柱状图展示就是这样：

```python
ax = year_df.plot(x='p_date', y='total', kind='bar', figsize=(9,6), fontsize=15)
ax.set_ylabel("文章数")
ax.set_xlabel("")
ax.legend().set_visible(False)
# 柱状图上显示数字
for p in ax.patches:
    ax.annotate(str(p.get_height()), xy=(p.get_x(), p.get_height()))
```

![](https://user-gold-cdn.xitu.io/2018/1/21/16118ca136919996?w=563&h=381&f=png&s=8514)


### 文章与赞赏

再来分析我们的文章赞赏情况



![](https://user-gold-cdn.xitu.io/2018/1/21/16118caed671fcb5?w=1374&h=536&f=png&s=95735)
总共有101篇文章赞赏，平均两篇文章就有1次赞赏，读者一共贡献了 518 次赞赏，谢谢可爱读者们支持（微笑表情）

用同样的方式可以得到文章赞赏数前10的数据：

```python
top_reward_num = df.sort_values(by=['reward_num'], ascending=False)[:10]
top_reward_num = top_reward_num[display_columns]
top_reward_num
top_reward_num.reset_index(drop=True)
```


![](https://user-gold-cdn.xitu.io/2018/1/21/16118ca62963193e?w=1370&h=614&f=png&s=154653)

最高的一篇文章有83个打赏，这究竟是一篇什么文章，戳-->[自学Python编程怎么学才不那么孤独](http://mp.weixin.qq.com/s?__biz=MjM5MzgyODQxMQ==&mid=2650367720&idx=1&sn=87e32a97392f320c17960c31f1035182&chksm=be9cddbc89eb54aa0277dd7e79acbb7fc44319156b0ec59ff9e9b30ffdac18489b10b663c7c2&scene=27#wechat_redirect)


```python
ax = top_reward_num.plot(x='title',
                         y='reward_num', 
                         kind='barh', 
                         figsize=(9,6),
                         fontsize=14)
ax.set_ylabel("")
ax.set_xlabel("赞赏数")
ax.legend().set_visible(False)
```

这里的 kind 用 "barh" 表示横向的条形图


![](https://user-gold-cdn.xitu.io/2018/1/21/16118cbbbc606baa?w=751&h=376&f=png&s=33966)

### 文章与点赞

说完赞赏的数据，再来看看点赞数与文章阅读数有什么关系，我们可以用散点图来表示二者之间关系，散点图用两组数据构成多个坐标点，表示因变量随自变量而变化的大致趋势。

```python
# 散点图
ax = df.plot(kind="scatter", y='like_num', x='read_num',s=10, figsize=(9,6), fontsize=15)
ax.set_xlabel("阅读量")
ax.set_ylabel("点赞数")

z = np.polyfit(df.read_num, df.like_num, 1)
p = np.poly1d(z)
plt.plot(df.read_num,p(df.read_num),"r--")
```

![](https://user-gold-cdn.xitu.io/2018/1/21/16118cb351523ca0?w=562&h=376&f=png&s=16650)

可以看出文章点赞数大部分集中在10~50之间，而且存在某种线性正相关性，也就是说，文章阅读数越高，点赞数也就越高，如果某篇文章阅读量很高，但是点赞数却很低，这样的文章是标题党或者是资讯类的文章的可能性比较大。


### 标题关键字


最后，我想基于文章标题做一个词云效果展示，看看这些文章标题都用了哪些关键字。这里需要用到另个包，一个是结巴分词，另一个词云包

```
conda install jieba
conda install wordcloud
```

```
from wordcloud import WordCloud
import jieba

words = []
for i in  df.title:
    seg_list = jieba.cut(i, cut_all=False)
    words.append(" ".join(seg_list))
wordcloud = WordCloud(font_path='/Library/Fonts/Songti.ttc',
                      background_color="white", 
                      max_words=80,).generate(" ".join(words))
plt.figure(figsize=(9,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
```


把所有文章的标题同结巴库分词处理加入到 words 列表中，传递给 WordCloud 组件，另外还需要指定一个中文字体，因为 wordcloud 默认无法处理中文。max_words 用于指定最多显示多少词语


![](https://user-gold-cdn.xitu.io/2018/1/21/16118cca83ffb68c?w=542&h=284&f=png&s=132459)

### 小结

到这里，我们就完成了一个公众号基本分析工作，得到一些结论，比如阅读量高的往往不是某个具体的知识点干货内容，而是一些更通俗的文章，要么是资讯，要么是一些工具介绍，或者是编程的方法论等文章。而赞赏文章基本集中在带有福利的文章里面，从文章标题得知公众号文章都是围绕Python写的文章。

本节ipynb源代码地址：[https://github.com/pythonzhichan/weixincrawler](https://github.com/pythonzhichan/weixincrawler)




