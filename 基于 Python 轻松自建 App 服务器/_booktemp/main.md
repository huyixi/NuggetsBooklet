---
title: 基于 Python 轻松自建 App 服务器
author: 基于 Python 轻松自建 App 服务器
date: 2025-02-15
lang: zh-CN
---

## 0App 与后端服务器通信方法简介

# App 与后端服务器通信方法简介

## 在开始之前

本小册的目标是希望大家在学习完成之后，能少掉笔者当初入门服务器端开发的烦恼。通过本小册，不仅能快速搭建起自己或公司的后端服务器，也能进一步优化，扩展，从而满足业务增长对服务器端的需要。

### 你将学到什么？

本小册将从基本的 App 与服务器端的通信讲起，涵盖数据的交互、图片的上传加载、H5 页面的请求加载。在基本通信场景功能的基础上，笔者将带领大家一起学习反向代理服务器 Nginx，并为保障业务通信的安全性及反 HTTP 劫持，学习使用 HTTPS。

最后，笔者也将以多年的后端服务器开发经验，就大型服务器端架构设计的演化路径和读者一起探讨。

总的来说，读者将从本小册学习到如下课题：
1. 腾讯云上配置开发环境
2. 基于 Tornado 的 HTTP 服务器框架
3. App 客户端/服务器端之间的数据通信
4. 服务器端对数据库 MySQL 的操作
5. 基于 Nginx 的反向代理及基于 HTTPS 的数据加密
6. 完成一款大型服务器的进阶方案和演进路线

本小册所使用的开发语言为 Python 3.6.2，各模块的版本信息将在后续章节中详细介绍。下面进入我们的正式学习阶段。

## 通信方法简介

很多朋友会问，App 客户端如何与服务器端进行通信呢？格式是什么？场景有那些？本小节将着重解答这些问题。

当前手机 App 客户端与服务器端通信，通常有两种模式：一种是短连接，一般通过 HTTP 进行通信；第二种是长连接，一般为 socket，长连接需要手机客户端与服务器端一直保持连接状态，服务器端压力较大，一般在游戏，服务器端主动向客户端推送服务信息时应用较为广泛。作为入门指南，本小册只讨论短连接 HTTP 的通信场景。而在短连接 HTTP 通信中，数据交互可以自定义，也可使用业界通用方法，即客户端和服务器端的数据交互采用 JSON 格式。本小册将使用业界通用方法，使用 JSON 的原因是 JSON 作为一种通用数据交换格式，被众多计算机语言支持，且开销小，省流量。


![](https://user-gold-cdn.xitu.io/2018/4/23/162f0999afb8716b?w=718&h=177&f=png&s=28959)

下面重点介绍一下 HTTP 和 JSON。

## HTTP 与 JSON 简介

### HTTP 协议

超文本传输协议（HTTP）是一个客户端和服务器端请求和应答的标准（TCP）。通过使用 App 客户端、Web 浏览器或者其他的工具，客户端发起一个到服务器上指定端口（默认端口为 80）的 HTTP 请求。 HTTP 有多种请求方式，而 App 客户端与服务器端的请求应答中，最常用的就是 GET 和 POST，本小册只会介绍这两种方式。如对其他方法感兴趣，可自行谷歌。

#### GET 方法

当发送一个 HTTP 请求时，查询字符串（名称/值对）是在 GET 请求的 URL 中发送的，即入参暴露在请求 URL 中，如：  
`http://www.demo.com/test?name1=value1&name2=value2`

##### GET 请求的特点

- GET 请求可被缓存  
- GET 请求保留在浏览器历史记录中  
- GET 请求可被收藏为书签  
- GET 请求不应在处理敏感数据时使用  
- GET 请求有长度限制  
- GET 请求只应当用于取回数据

#### POST 方法

当发送一个 HTTP 请求时，查询字符串（键/值对）是在 POST 请求的 HTTP 消息主体（body）中发送的，如：  
`http://www.demo.com/test`  
Request body 中：`name1=value1&name2=value2`

##### POST 请求的特点

- POST 请求不会被缓存
- POST 请求不会保留在浏览器历史记录中
- POST 不能被收藏为书签
- POST 请求对数据长度没有要求

对于第一次接触 HTTP 的同学，可能还是难以理解如何去使用它们，对吧？不要紧，上面的解释只是作为一种通用理解，刚入门的同学可以这样简单记忆：对安全性要求较高，或键/值对较多的，用 POST，其他的用 GET。后面从第 6 小节起，将介绍如何去使用 GET/POST 方法。

#### JSON

JSON 是一种轻量级的数据交换格式，易于阅读并能提升网络传输效率。JSON 的语法中，键/值对是用来保存对象的一种方式，如
`{"name1": "value1"}`。
对于熟悉 Python 的同学来讲，JSON 的格式和 Python 的字典很像。简单地理解，Python 的字典数据格式就是 JSON 的数据格式，但它们的不同也显而易见。JSON 的键/值对只允许使用双引号（`""`）作为边界符号，而 Python 的字典则可以使用多种方式，包括单引号。

## 小结
本小节重点介绍了 App 客户端与服务器端的通信场景，包括数据交互方式，及 HTTP 和 JSON 的介绍，简单小结如下：
1.	App 客户端与服务器端的消息请求应答使用 HTTP 协议；
2.	App 客户端与服务器端的消息格式使用 JSON 格式；
3.	HTTP 的重点请求方式有两种方式，分别为 GET 和 POST；
4.	GET/POST 采用键/值对的方式，信息保密性要求高些，或键/值对多些时，使用 POST 方式。


## 10搭建基于 Nginx 的代理服务器

# 搭建基于 Nginx 的代理服务器

[Nginx](https://nginx.org/en/) 是俄罗斯人编写的十分轻量级的 HTTP 服务器，是一个高性能的 HTTP 和反向代理服务器。相较于 [Apache](https://httpd.apache.org/)、[lighttpd](https://www.lighttpd.net/) ，它具有占有内存少、稳定性高等优势。它最常见的用途是提供反向代理服务。

在本小节中，我们将利用 Nginx 的反向代理及负载均衡能力。所谓的负载均衡，是当单台服务器的性能无法满足业务需求时，需横向添加多台服务器；负载均衡就是让访问流量均匀的落在这个服务器集群的每个服务器上。具体逻辑图如下：
 
![](https://user-gold-cdn.xitu.io/2018/4/17/162cf4279defaf8f?w=749&h=545&f=png&s=27262)

App 客户端将请求发送至 Nginx，Nginx 收到请求后，将其转发给后端的服务器集群。在本小册中，我们的 Demo 只有一台虚拟机，现将 Nginx 和后端服务器放在一起，Nginx 架设在 Tornado 之前，其基本框架图如下。
 

![](https://user-gold-cdn.xitu.io/2018/4/26/162fed7f862487ae?w=648&h=613&f=png&s=27863)

## 安装 Nginx

输入 `yum install nginx` 安装 Nginx，安装完成后，输入 `nginx -v` 查看 Nginx 是否安装成功。

![](https://user-gold-cdn.xitu.io/2018/4/17/162cf42e5f0860bd?w=727&h=354&f=png&s=33791)

这里显示安装已成功，版本号为 `1.12.2`。

## 配置随系统自启动

配置 Nginx 随系统自启动，即 Linux 系统启动时，Nginx 能自启动，而不是人为干预启动。
```shell
chkconfig --levels 235 nginx on
service nginx start
```

![](https://user-gold-cdn.xitu.io/2018/4/17/162cf4315115e6d2?w=1555&h=72&f=png&s=17810)

 
![](https://user-gold-cdn.xitu.io/2018/4/17/162cf432baa6a329?w=658&h=49&f=png&s=7930)

## 配置 Nginx

进入 `/etc/nginx/`, 编辑 `nginx.conf` 文件。
 
![](https://user-gold-cdn.xitu.io/2018/4/17/162cf437db1850dc?w=964&h=157&f=png&s=17939)
在 `nginx.conf` 中，增加后端服务器 IP 和端口，由于 Nginx 和服务器在同一台机器上，这里填入：

```
upstream frontends {
    server 127.0.0.1:8000;
}
```

当 Nginx 和后端服务器不在同一台机器上，并有多台后端服务器设备时，则配置具体服务器的 `IP:端口` 即可，Nginx 会负载均衡的将流量均匀分配到这些服务器上。此时配置如下：
```
upstream frontends {
    server x.x.x.x:nnn;
    server y.y.y.y:mmm;
    server z.z.z.z:lll;
}
```
由于 Nginx 对大小超过 1MB 的文件上传有限制，这里将默认限制 1MB 修改为 50MB，即添加配置 `client_max_body_size 50m;`，具体位置如下图所示。
 
![](https://user-gold-cdn.xitu.io/2018/4/17/162cf43a5a748c1f?w=798&h=503&f=png&s=38078)

在 `nignx.conf` 文件中的 `location` 下，添加如下代理配置，即所有收到的请求，都转发到 `frontends` （如上所述的 `upstream frontends`）处理，具体如下：

```
    proxy_pass_header Server;
    proxy_set_header Host $http_host;
    proxy_redirect false;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Scheme $scheme;
    proxy_pass http://frontends;
```
具体位置如下：

![](https://user-gold-cdn.xitu.io/2018/4/17/162cf4a15297a1b6?w=773&h=421&f=png&s=34375)

至此，我们已完成了 Nginx 的配置。

## 其他配置项介绍

```
# For more information on configuration, see:
#   * Official English Documentation: http://nginx.org/en/docs/
#   * Official Russian Documentation: http://nginx.org/ru/docs/

user nginx;
# worker_processes 一般设置与 cpu 个数相等，也可配置为auto
worker_processes auto;
# 全局错误日志及 pid 目录
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;

# Load dynamic modules. See /usr/share/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;

events {
    # 单个后台 worker proces s进程的最大并发链接数 
    worker_connections 1024;
}

http {
    # 设置 log 格式
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    # 配置上游服务器，此处为 Tornado 服务器 IP+Port
    upstream frontends {
        server 127.0.0.1:8000;
        #server 10.10.10.10:8001;
    }

    # 访问日志
    access_log  /var/log/nginx/access.log  main;

    # sendfile 指令指定 nginx 是否调用 sendfile 函数（zero copy 方式）来输出文件，普通应用，设置为 on 即可；
    # keepalive_timeout 配置超时时间；
    # types_hash_max_size 影响散列表的冲突率。types_hash_max_size 越大，就会消耗更多的内存，但散列key的冲突率会降低，检索速度就更快。types_hash_max_size 越小，消耗的内存就越小，但散列key的冲突率可能上升。
    # client_max_body_size 客户端上传的body的最大值。
    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;
    client_max_body_size 50m; 

    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;

    # Load modular configuration files from the /etc/nginx/conf.d directory.
    # See http://nginx.org/en/docs/ngx_core_module.html#include
    # for more information.
    include /etc/nginx/conf.d/*.conf;

    server {
        # 监听端口为 80
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  _;
        # 默认网站根目录位置
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        # 设置默认请求代理，此处使用frontends，即请求代理至 Tronado 服务器
        location / {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect false;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://frontends;
        }
        
        # 定义 404 错误页
        error_page 404 /404.html;
            location = /40x.html {
        }

        # 定义 50x 错误页
        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
}

```

## 重启 Nginx 服务

```
service nginx stop
service nginx start
```
![](https://user-gold-cdn.xitu.io/2018/4/17/162cf43c1832618c?w=672&h=116&f=png&s=17417)

接下来测试从 App 客户端向 Nginx 服务器发送 HTTP 请求，查看是否能正常转发至后端服务器上。在这里，我们看到 `nginx.conf` 有如下配置，即表示其对外服务的端口号为 80。实际项目中，可以根据具体情况进行修改。
 
![](https://user-gold-cdn.xitu.io/2018/4/17/162cf44047e8a3ca?w=750&h=251&f=png&s=17718)

## 请求测试

我们还是以上一小节 App 客户端请求加载 H5 页面为例。由于 Nginx 对外提供服务的端口号是 80，而 80 端口在 HTTP 请求中可以不用输入，此时客户端请求的 URL 为：
http://150.109.33.132/users/login?phone=18866668888&password=demo123456

### 服务端输出
 
![](https://user-gold-cdn.xitu.io/2018/4/17/162cf44249203218?w=1251&h=290&f=png&s=71079)

### 客户端加载结果
 
<div style="text-align: center; margin-top: 30px">
<img src="https://user-gold-cdn.xitu.io/2018/4/17/162cf44586567600?w=1080&h=1920&f=jpeg&s=236689" style="width: 480px">
</div>

至此，我们已完成了 Nginx 的学习及服务器端的配置。
## Nginx 配置下载

链接：[百度网盘 - nginx.conf](https://pan.baidu.com/s/1-3p1N08YY5rfALqocX8YZw)  
密码：xtmr

## 小结

本节我们完成了 Nginx 服务器的搭建，并通过一个简单的例子，讲解了 Nginx 作为反向代理服务器和负载均衡器的应用。


## 11基于 HTTPS 的数据加密

# 基于 HTTPS 的数据加密
本小节为可选章节，因为 HTTPS 证书需要域名（域名需另行购买）才能申请。有域名的读者可以按步骤实践，没有域名的读者，只需要了解即可。

## HTTPS 与 HTTP 区别

在前面的小节中，客户端与服务器端的请求响应都是用的 HTTP， HTTP 和 HTTPS 有什么区别呢？

HTTP 协议传输的数据都是未加密的，也就是明文的，因此使用 HTTP 协议传输隐私信息非常不安全，为了保证这些隐私数据能加密传输，网景公司设计了 SSL（Secure Sockets Layer）协议用于对 HTTP 协议传输的数据进行加密，从而就诞生了 HTTPS。简单来说，HTTPS 协议是由 SSL+HTTP 协议构建的可进行加密传输、身份认证的网络协议，要比 HTTP 协议安全。

HTTPS 和 HTTP 的区别主要如下：
1. HTTPS 协议需要到 CA 中心申请证书
2. HTTP 是超文本传输协议，信息是明文传输，HTTPS 则是具有安全性的 SSL 加密传输协议
3. HTTP 和 HTTPS 使用的是完全不同的连接方式，前者默认是 80，后者是 443
4. HTTP 的连接很简单，是无状态的；HTTPS 协议是由 SSL+HTTP 协议构建的可进行加密传输、身份认证的网络协议，比 HTTP 协议安全

HTTP 由于是明文传输未加密，缺点可见一斑。这里插入一个小故事，在笔者开发第一款 App 的时候，为了提高效率，采用了 HTTP，在 客户端和服务器调试期间，笔者发现客户端的最下面，经常会莫名其妙地出现垃圾广告，一开始并不清楚为啥会出现这种情况，客户端和服务器端还花好长一段时间进行调试定位。最后发现是运营商的问题，广告也是运营商嵌入的，这就是不加密的后果：HTTP 被劫持了。后面改为 HTTPS，整个世界也就清静了。

## HTTPS 工作原理

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff2a191787c9d?w=781&h=160&f=png&s=18154)

这里涉及很多新的概念，如公钥和私钥。简单的理解即为，我们的服务器端需要安装 CA 证书（证书下载后面会讲解），证书包含两个东西，一个是私钥，一个是公钥，私钥就是自己留着的，别人不会知道，公钥是别人使用 HTTPS 请求时，发给别人的密钥。当客户端需要发送加密报文时，会使用服务器端给的公钥进行加密，此时在网络中传输的就是一串无序的字符串。当报文被服务器端接收到时，服务器端使用私钥进行解密，这样就能保证整个链路的安全性。关于公钥和私钥，这里有一篇有趣的讲解供读者参考（[公钥与私钥，HTTPS详解](https://www.cnblogs.com/shijingjing07/p/5965792.html)），本节作为简单的抛砖引玉，不作过多的阐述。下面看一下整个通信流程。

客户端在使用 HTTPS 方式与服务器端通信时有以下几个步骤，如图所示。

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff2a5c8f7a7c3?w=365&h=411&f=gif&s=5305)

1. 客户使用 HTTPS 的 URL 访问服务器，要求与服务器建立 SSL 连接
2. 服务器收到客户端请求后，会将站点的证书信息（证书中包含公钥）传送一份给客户端
3. 客户端与服务器开始协商SSL连接的安全等级，也就是信息加密的等级
4. 客户端的浏览器根据双方同意的安全等级，建立会话密钥，然后利用服务器端的公钥将会话密钥加密，并传送给客户端
5. 服务器利用自己的私钥解密出会话密钥

## 下载证书

如上所述，首先需要申请下载证书，并将其存放在服务器端。目前安全性较高的数字证书都是付费的。读者可以根据自身项目的诉求，选择不同的证书级别，个人或者小微企业可选择使用免费的数字证书。由于我们只是 Demo，这里选择免费证书。免费的证书可以直接上公有云提供商下载，如腾讯云、阿里云等。本小册以腾讯云为例。

### 申请证书

登录腾讯云，输入如下链接，申请“域名型免费版(DV)”：  
https://buy.cloud.tencent.com/ssl?fromSource=ssl

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff2ab8a3f1b33?w=1009&h=837&f=png&s=80937)

按照步骤一步步完成购买。

### 下载上传

将证书从腾讯云上下载下来（214225718810040.zip），并将其上传到服务器上。假定证书也放在 demo 目录下，在 demo 目录下创建 cert 目录。并将其解压至此目录。

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff2aec17cbc15?w=1007&h=394&f=png&s=47529)

### 配置 Nginx 

正如前面介绍 HTTPS 时所述，HTTPS 使用的是 443 端口，此时需要修改 Nginx 监听的端口为 443。另外，需要在 Nginx 的配置文件中指定 HTTPS 证书的路径。配置 Nginx 的 server 如下：

```
listen 443;
server_name  _;
ssl on;
root html;
index index.html index.htm;
ssl_certificate   cert/214225718810040.pem;
ssl_certificate_key  cert/214225718810040.key;
ssl_session_timeout 5m;
ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
ssl_prefer_server_ciphers on;
```
具体位置如下：
![](https://user-gold-cdn.xitu.io/2018/4/26/162ff2b23641a07c?w=1221&h=420&f=png&s=44459)

### 重启 Nginx

配置完成后，需要重启 Nginx，在服务器上直接输入如下命令重启 Nginx：

```
service nginx stop
service nginx start
```
至此，已完成服务器端 HTTPS 的准备，此时从客户端使用 HTTPS 请求，就可以保证数据的安全性。
## 小结
本小节介绍了 HTTPS 的原理及在 Nginx 上的配置和使用方法。作为可选章节，读者在有条件的时候练习即可。


## 12大型 HTTP 服务器架构演进路线及思路

# 大型 HTTP 服务器架构演进路线及思路

一个成熟的大型后端服务器（如京东、淘宝等）并不是一开始的设计就具备完整的高性能、高可用、高安全等特性。它是随着业务和用户量的增长，业务功能不断地扩展演化而来的。在这个过程中，团队的增加带来开发模式的转变，性能瓶颈带来技术架构及设计思想的改变。随着业务的增长，开始出现业务功能的侧重点，如微信在发展成十亿级别的用户体量后，业务侧重的就是如何解决数十亿用户实时消息传输的通达性，百度慢慢地发展为如何处理海量数据的搜索请求。这些技术架构方案及思想，各有各的不同，无法一蹴而就，而是业务驱动。本节无法详尽提及每一种架构的设计方案，而只提供一种通用的思想，这些思路广泛应用于现在大型的后端服务器设计架构中，希望读者在具体的项目中，随着业务的增长，能从这里找到一些思路。下面将从服务器的演进路线进行讲解。

## 1. 项目初期

在项目的初期，一般为了抢夺市场时间窗口，产品需要快速推向市场。此时，访问量低，业务单一，对服务器要求不高。正如本小册的方式，应用程序、数据库和文件全部放在单一的服务器中，如下图所示。

![](https://user-gold-cdn.xitu.io/2018/4/20/162e026ef90afe18?w=787&h=456&f=png&s=38531)

但需要注意的是，单一不代表粗糙，应用程序设计阶段，应秉承解耦的思想，各业务组件之间相对独立，各层级清晰，如本小册的 views 模块分层逻辑、数据库处理模块化等。

## 2. 应用程序、数据、存储分离

随着业务的发展，单台服务器已无法满足业务需求，此时应将应用程序、数据库和存储进行拆分，将其各自部署在不同的服务器上。

![](https://user-gold-cdn.xitu.io/2018/4/20/162e0271827df293?w=927&h=455&f=png&s=44148)

## 3. 负载均衡

当服务器的访问量大于单台服务器能提供的能力时，此时需要部署多台服务器进行横向扩展。在服务器集群前增加负载均衡器，以使访问流量通过负载均衡器能均衡地分配到后端服务器集群上，以此来满足大流量、高并发、海量数据请求问题。目前主流的负载均衡分软件和硬件两种，软件有主流的 Nginx，硬件需要购买专门的负载均衡器设备，成本较高，但处理能力更强。

![](https://user-gold-cdn.xitu.io/2018/4/20/162e02745557113b?w=1013&h=459&f=png&s=58520)

## 4. 缓存技术

缓存技术能大大提高服务器性能，世间万物大多遵循 2/8 原则，用在这里，即 80% 的访问量落在 20% 的业务数据上。对热点数据（20%）进行跟踪并进行缓存，能大大提高访问效率。缓存分为文件缓存、内存缓存及数据库缓存。缓存主要分两种，一是使用本地缓存，另一种是分布式缓存。本地缓存一般用于单机模式，缓存数据量有限；而分布式缓存可以缓存海量数据，易扩展，容灾性强，常用的分布式缓存有 Memcache 及 Redis。

![](https://user-gold-cdn.xitu.io/2018/4/20/162e0276b8288bfc?w=1023&h=648&f=png&s=66201)

在缓存技术中，还有一个重量级的服务，叫 CDN。简单讲，即就近接入，提高用户访问速度。当目标用户分散在全国各地，此时部分用户受地域、网络等限制，访问服务器存在延迟问题，特别是点播、直播等场景。CDN 就是这样的一种技术，它能将源站点内容抓取分发到最接近用户的节点，从而提高用户的访问速度和提升用户体验。

![](https://user-gold-cdn.xitu.io/2018/4/20/162e02792dec28c0?w=1016&h=758&f=png&s=72188)

## 5. 分布式文件系统

随着用户数据的增长，产生的文件也越来越多，单台文件服务器已无法满足业务需要，需采用分布式文件系统以支撑。常见的分布式文件系统有 NFS。

![](https://user-gold-cdn.xitu.io/2018/4/20/162e027b2f219ae6?w=1028&h=767&f=png&s=75331)

## 6. 应用程序拆分

随着业务的发展，应用程序进一步膨胀，此时已不适合将其所有的组件部署在一起，而是需要按业务模块进行应用程序的拆分。每个业务模块负责相对独立的业务运作，包括版本迭代更新、业务演进。业务模块之间通过数据库或消息请求进行处理。现在主流的业务模块通信会使用 RESTful API 进行通信。各业务模块有自己的缓存系统、文件服务器系统和分布式数据库系统。

![](https://user-gold-cdn.xitu.io/2018/4/20/162e02899ad1019c?w=1047&h=774&f=png&s=82160)

以上即为通用大型服务器方案架构演进路线。
 
## 小结

本小节简单高度概括了服务器端演进的整个过程。这里只提供一些思路，具体的架构和方案还要看具体的项目而行。后台架构方案可以千差万别，适合自己业务模式的才是最好的。

上面提到的很多技术，如负载均衡、CDN 分发、分布式缓存和分布式数据库等，在传统的架设中，从物理连线到软件安装，都需要人力投入。自从公有云服务推出后，这些技术已经作为公有云的基础设施推给客户。现在的企业，不用再自己去购买硬件设备并维护机房，而只需要通过购买服务的方式搭建这个业务生态环境，大大提高了工作效率及管理效率。


## 13总结

# 总结

至此，我们已完成了本小册的讲解。我们从 HTTP 和 JSON 的格式和方法讲起，进而过渡到 Tornado 服务器的介绍。完成了 Tornado 的介绍后，我们开始了服务器端代码编写之旅。从第一条数据请求响应，到图片上传加载，再到 H5 页面的返回，这些基本通信场景在 App 客户端与服务器端的通信中，每天都在上演。只有把这些基本功打好，才能迈开一步，朝着大型服务器的方向迈进。

在基本通信场景功能的基础上，我们一起学习了反向代理服务器 Nginx，并结合小册内容学习了如何架设 Nginx。为了保障业务通信的安全性及反 HTTP 劫持，我们学习使用 HTTPS 并应用在我们的服务器开发上。

这些内容的讲解，在于以一手的经验，手把手带领大家一步步认清后端服务器的设计。希望大家在学习完这些章节之后，能真正掌握小册之前提到的如下技能点。

1. 腾讯云上配置开发环境
2. 基于 Tornado 的 HTTP 服务器框架
3. App 客户端/服务器端之间的数据通信
4. 服务器端对数据库 MySQL 的操作
5. 基于 Nginx 的反向代理及基于 HTTPS 的数据加密
6. 完成一款大型服务器的进阶方案和演进路线

也希望大家在学习完本小册之后，能少掉笔者当初入门的烦恼，而是真正通过本小册，快速搭建起了自己或公司的后端服务器。

小册的最后，也提出了完成一款大型后端服务器在思路和设计上的演进。这部分内容作为进阶方案，希望读者在学习之后，能结合具体的业务需求，完善和优化整个后端服务器。

至此，我们已学习完全部内容，感谢大家的关注，希望本小册能给大家带来帮助，也希望大家在工作生活中顺顺利利，一路向前。


## 1本小册要完成的通信场景功能

# 本小册要完成的通信场景功能

本小册将重点关注入门与实践，并在入门的基础上提供设计一款大型服务器架构的思路。在简单了解了 App 客户端和服务器端的通信后，本小节将介绍，如何利用前面介绍的 HTTP 方法和 JSON 格式，来学习一些基本的交互场景。在 App 客户端和服务器端的通信场景中，一般会涉及 3 种场景，分别为简单的数据请求响应、图片上传加载及 H5 页面请求加载。下面将覆盖以上场景，并且在实现这些通信场景的过程中，我们也将一步步推进介绍如何使用 HTTP 服务器框架 Tornado，以及数据库 MySQL。在后续的章节中，我们也将重点介绍基于 Nginx 的反向代理负载均衡及基于 HTTPS 的数据加密。最后，会给出一种设计思路，随着业务的增长，一款大型的 HTTP 服务器是如何演化的。

以上所有的实现逻辑及代码，将在后续的章节中详细介绍。下面先简单介绍一下 3 种场景。

### 场景一：用户注册

App 客户端发送 HTTP 请求注册用户信息，服务器端收到 HTTP 请求后，校验请求并写入数据库，返回注册成功或失败信息。
 
![](https://user-gold-cdn.xitu.io/2018/4/2/162836d78ea32eb5?w=705&h=198&f=png&s=23841)

### 场景二：图片上传加载

App 客户端发起图片上传，服务器端收到 HTTP 请求后，校验并接收图片上传，写入硬盘和数据库，并返回图片上传成功或失败信息。App 客户端根据返回的图片链接，请求加载图片。
 
![](https://user-gold-cdn.xitu.io/2018/4/2/162836da80237f0b?w=706&h=198&f=png&s=24562)

### 场景三：加载 H5 页面

App 客户端用户登录，服务器端校验通过后返回首页 H5 URL，App 客户端加载请求首页页面，服务器端收到 HTTP 请求后，校验并更新数据库，返回预设的 H5 页面。
 
![](https://user-gold-cdn.xitu.io/2018/4/18/162d5c90cbc07b4f?w=684&h=271&f=png&s=29928)

## 小结

本小节简单介绍了本小册要完成的几种通信场景及整本小册要完成的使命，希望读者在学习完本小册后，不仅能在项目启动阶段快速搭建起一个完整的 App 后端服务器，也能在后期迭代中，演进服务器端设计以适应业务增长的需要。


## 2服务器端组件框架的选择与介绍

# 服务器端组件框架的选择与介绍

本小册的目标在于搭建一款简洁、高效，并能快速部署及上手的 App 后端服务器。

在编程语言的选择上，我们选择了 Python 3.6.2，这也是本小册对读者的基本要求，从 HTTP 服务器，到数据库操作及逻辑分析处理，将全部使用 Python 语言。

前两节的介绍中讲到，我们使用 HTTP 协议来定义 App 客户端与服务器端之间的通信。我们不可能自己写一个 HTTP 服务器来响应客户端的 HTTP 请求，所以在 App 服务器端开发中，我们工作的重中之重，就是要寻找到一款合适的、支持高并发、易扩展并真正能阐释代码简洁美的框架。在调研了众多的 HTTP 服务器框架之后（如 Django、Pyramid），笔者最终选择了 Tornado。从多年前第一次遇到 Tornado 开始，笔者就爱上了它：简洁高效，易扩展，高并发。著名的知乎也是建立在 Tornado 之上。好好利用这把利剑，必定能在平时的生活工作中，助你更上一层楼。

除了编程语言和 HTTP 服务器框架外，我们还要选择操作系统及数据库。本小册中将使用 CentOS 7.2 x64 作为操作系统，MySQL 作为数据库，操作数据库使用 ORM（Object Relational Mapping）的方式。服务器端的整体框架如下图所示。

![](https://user-gold-cdn.xitu.io/2018/4/2/1628374240e888c0?w=646&h=380&f=png&s=19648)

### CentOS

CentOS 是大名鼎鼎的 Red Hat 的开源版本，由 Red Hat 公司维护测试，并在 Linux 内核稳定分支上进行开发，系统相对稳定。 Red Hat 一早就在中国布局，市面上书籍众多，网上资料丰富，很多公司，第一版优先支持的版本也是 CentOS，这也是我们选择 CentOS 的原因，当出现疑难杂症时，能第一时间找到解决方案。在本次服务器端开发中，我们并不需要精通 CentOS，只需要会简单地使用 Linux 的命令即可，如 `yum install <module name>`。

### MySQL

MySQL 是最流行的关系型数据库管理系统，在 Web 应用方面是最好的关系型数据库管理系统软件之一， 也是最早一批被国内用户熟知的数据库软件之一。 同样，当出现疑难杂症时，丰富的图书及网络资源能帮助我们尽快找到解决方案。

### SQLAlchemy

在操作数据（如 MySQL）的过程中，我们可以使用原生的 MySQL 语句（如`insert`、`update`、`delete`），也可以使用 ORM（Object Relational Mapping）的方式。简单来说，可以使用第三方软件来操作数据库，使用第三方的好处是很多底层 MySQL 的命令被封装成简单的API暴露给用户，并提供强大的整合功能。当然坏处也有，如相对于原生命令效率低些，学习成本高些。而选择 SQLAlchemy 的原因是其使用 Pythonic 的代码风格，在本小册中不会给读者增加太多学习成本，另外，SQLAlchemy 全面的 API 参考文档也是我们选择它的原因之一。

### Tornado

Tornado 作为我们选用的 HTTP 服务器框架，在后续的章节中，我们将作详尽的诠释。

## 小结
本小节简单介绍了整个服务器端的组件框架，从下一节开始，我们将进入环境搭建并开始真正的代码编写。



## 3基于腾讯云的服务器端环境搭建

# 基于腾讯云的服务器端环境搭建

在不区分软硬件的情况下，服务器端开发需要准备的环境主要有如下几个：
1.	服务器：服务器端代码开发及执行环境；
2.	Linux 虚拟终端软件：登录服务器，并编辑和执行服务器端代码，推荐 secureCRT；
3.	代码编辑器：通过 FTP/SFTP 获取服务器端代码并编写代码的工具。

下面分别展开介绍及配置。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3cf30f446ca?w=838&h=411&f=png&s=28851)

## 购买服务器

服务器端开发，首先需要一台服务器。这里我们有三种方式选择搭建服务器。
1.	传统的方式，购买一台物理主机，在主机上安装操作系统及配置相应的开发环境；
2.	在家用电脑中，安装虚拟机，安装相应的操作系统及配置相应的开发环境；
3.	使用公有云服务，节省环境准备时间，即买即用，本小册采用这种方式。

从 2006 年亚马逊推出公有云提供 IT 基础设施服务开始，传统的方式已慢慢被颠覆，这里，我们并不需要了解公有云是个什么东西，只需要知道，传统的购买服务器行为，已经可以在公有云上按照虚拟机的方式进行购买。这样的好处也是显而易见的：一是公有云提供商提供物理及软件环境管理，如水电、空间物理管理、虚拟机稳定性、安全等；二是用完即走，续用灵活，在课程结束后，即可选择停用虚拟机或者续用，相比物理机，费用大大降低。在国内，目前主要的提供商有腾讯云和阿里云，本小册以腾讯云为例，如已购买了阿里云云主机，安装相同操作系统版本的情况下，其他操作基本一致。<br>

**注：** 目前很多公有云提供商都有促销体验活动，如华为云有限额15天免费体验期，腾讯云和百度云有限额7天免费体验期，读者学习期间可以关注主要云提供商（阿里云，腾讯云，金山云，华为云，百度云，青云等）的促销活动。

### 注册购买云主机
进入此页面注册：[注册 - 腾讯云](https://cloud.tencent.com/register)

进入此页面购买云主机：[云主机](https://console.cloud.tencent.com/cvm/index)

我们并不需要购买很强大的服务器，只需要入门级虚拟机即可，如是公有云使用入门者，建议使用如下模板创建虚拟机。如果已是熟练的公有云使用者，可按照自身的情况选择虚拟机。

这里推荐两种方案，如读者打算使用服务器的时间低于半个月，推荐第一种方案，如时间高于半个月，使用第二种方案更为优惠。

#### 方案一

按照如下红框所示购买云主机。

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff013b3a852a0?w=1170&h=955&f=png&s=82233)

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff0171eb31020?w=1094&h=697&f=png&s=44838)

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff01929af215f?w=1015&h=787&f=png&s=57040)

![](https://user-gold-cdn.xitu.io/2018/4/26/162ff01b08397048?w=850&h=844&f=png&s=59863)

#### 方案二

按照如下红框所示购买云主机。

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3d277981aa9?w=1143&h=921&f=png&s=88424)

购买完成后，几分钟后即可在[云主机列表](https://console.cloud.tencent.com/cvm/index)中看到已购买的虚拟机。

如下图中的“主IP地址”一栏，即为该虚拟机对外服务的外网 IP 地址，我们只需要通过这个 IP 地址，即可访问到该虚拟机。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3d4f620e4d6?w=1174&h=260&f=png&s=30887)

## Linux 虚拟终端软件

通过 Linux 虚拟终端软件登录服务器，主流的有 Putty、Xshell 及 SecureCRT 等软件，本小册以 secureCRT 为例。

### 下载 SecureCRT

SecureCRT 为付费软件，但有 30 天的免费体验期，访问 [SecureCRT 官网](https://www.vandyke.com/download/securecrt/download.html) 下载，或者通过以下地址获取：  
链接: [百度网盘 - SecureCRT 8.3.2](https://pan.baidu.com/s/1aY8gLSWQdHpMS5_CeRce5A)   
密码: 5vv2
![](https://user-gold-cdn.xitu.io/2018/4/26/162fd9375fb41f60?w=882&h=453&f=png&s=42651)

### 创建会话连接

打开 secureCRT，依次单击“文件” -> “连接”，如下所示。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3d6fa54d0ae?w=381&h=204&f=png&s=19511)

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3db478a2724?w=646&h=637&f=png&s=52328) 

“主机名”为腾讯云虚拟机对外的 IP（请替换为自己的云虚拟机 IP，余同），如下所示，其他按默认配置直至完成即可。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3dd45f58fa7?w=870&h=598&f=png&s=58015)

### 登录虚拟机
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3df3eb49dc8?w=563&h=511&f=png&s=23703)

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3e12160fc06?w=697&h=146&f=png&s=9525) 

## 配置开发环境

根据第 3 节的介绍，开发环境需要安装如下软件：Python 3、Tornado、MySQL 和 SQLAlchemy。

### 安装 Python 3.6.2

CentOS 7.2 操作系统自带的 Python 版本为 2.7.5，本小册将以 Python 3.6.2 的版本进行讲解。即安装完 Python 3.6.2 后，系统上同时存在 Python 2.7.5 和 Python 3.6.2 两个版本。

#### 安装依赖包

```shell
yum -y groupinstall "Development tools"
yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
```

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b235146a7ad?w=1603&h=336&f=png&s=64608)

#### 下载 Python 3.6.2

```shell
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz
```

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b277b6be9fa?w=1435&h=306&f=png&s=44459)

#### 创建安装目录

```shell
mkdir /usr/local/python3
```

#### 安装 gcc

由于 Python 3.6.2 的编译需要编译环境，故需安装 gcc。

```shell
yum -y install gcc
```

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b29c175c98e?w=1271&h=290&f=png&s=58305)

#### 安装 Python 3.6.2

解压 Python 3.6.2 并安装在 `/usr/local/python3` 目录下。

```shell
tar -xvJf  Python-3.6.2.tar.xz
cd Python-3.6.2
./configure --prefix=/usr/local/python3
make && make install
```

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b2e03eddeb6?w=1329&h=289&f=png&s=80548)

#### 创建软连

```shell
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
```
#### 测试 python3

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b301c0c73c8?w=914&h=157&f=png&s=20307)

### 安装 Tornado

CentOS 下还无法直接使用 `yum install tornado`，但可以使用 pip 安装 Tornado。先执行 `pip3 install --upgrade pip` 命令升级 pip，再执行 `pip3 install tornado` 命令安装 Tornado。

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b7813b3239d?w=1094&h=118&f=png&s=11833)

测试 Tornado 是否安装成功：

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b796cb13d63?w=932&h=162&f=png&s=18458)

执行 `import tornado` 没有报错，表示 Tornado 已安装成功。

### 安装 MySQL

```shell
yum install mysql-devel
wget http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm
rpm -ivh mysql-community-release-el7-5.noarch.rpm
yum -y install mysql-community-server
pip3 install mysqlclient
service mysqld restart
```

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b9530ea4a16?w=1530&h=305&f=png&s=43010)

安装 MySQL 会比较久，大概 10 分钟左右，当看到 “Complete!” 后，表示安装成功。

测试 MySQL 安装是否成功：

```
systemctl status mysqld.service
```
![](https://user-gold-cdn.xitu.io/2018/4/21/162e8b9a02bd9cc5?w=928&h=244&f=png&s=43138)


### 安装 SQLAlchemy

使用 pip3 安装 SQLAlchemy：

```shell
pip3 install SQLAlchemy
```

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8ba3694a14a3?w=901&h=200&f=png&s=26621)

测试 SQLAlchemy 是否安装成功，服务器端依次输入如下命令。

```shell
python3
import sqlalchemy
```
![](https://user-gold-cdn.xitu.io/2018/4/21/162e8ba5bc8d4f0d?w=880&h=156&f=png&s=19654)

没有报错，证明 SQLAlchemy 已安装成功。

## 代码编辑器 Notepad++

当前代码编辑器/IDE 众多，较为人熟知的有 Source insight、Eclipse 和 PyCharm 等，但大都收费，读者可以利用手头的编辑器，能远程编辑代码即可。如果读者刚好在 Windows 上编辑代码，这里推荐使用 Notepad++, Notepad++ 作为一款免费的 Windows 文本编辑器，内置很多丰富的工具来编写代码。

### 安装 Notepad++

Notepad++ 是一款基于 Windows 平台的免费编辑器，读者可以到[官网](https://notepad-plus-plus.org/download/v7.5.6.html)自行下载安装，也可以通过如下链接获取：  
链接：[百度网盘 - notepad++](https://pan.baidu.com/s/1L0g02zJS-mDXSHQ25i05jg)  
密码：tl26

### 配置 Notepad++

Notepad++ 下载下来后，并不能立即通过 SFTP 的方法从远端服务器拉取源代码到本地计算机进行编辑，还需要安装 NppFTP 来实现这个功能。

#### 安装远程编辑功能插件 NppFTP

打开 Notepad++，依次选择“插件” -> “Plugin Manager” -> “Show Plugin Manager”，找到NppFTP。

![](https://user-gold-cdn.xitu.io/2018/4/24/162f72192a5ba521?w=530&h=195&f=png&s=25345)
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3f2eb23cde0?w=788&h=436&f=png&s=303407)

#### 配置远程远端服务器

##### 打开 NppFTP 插件面板

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3f512412be1?w=534&h=240&f=png&s=15193)

##### 配置远程服务器

本小册的后续所有代码将存放在远程服务器的 data 目录下，这里配置服务器端目录时，直接拉取 data 目录。

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3f6f9025094?w=419&h=211&f=png&s=18772)
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3f8cb7f7a07?w=619&h=523&f=png&s=28136)

#### 获取远端目录文件

首先我们在服务器的 data 目录下，创建 demo 目录，并使用 Notepad++ 拉取该目录。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3ee58aa8ef5?w=572&h=161&f=png&s=14443)
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3fa7f076d6a?w=412&h=208&f=png&s=16980)
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e3fc68a2e524?w=397&h=221&f=png&s=16894) 

#### 上传下载远端目录文件

安装 lrzsz，lrzsz 包的 `rz` 命令能支持从本地 Windows 上传小文件到远端服务器，而 `sz` 命令支持从远端服务器下载小文件到本地 Windows 上。

![](https://user-gold-cdn.xitu.io/2018/4/21/162e8becae92e86e?w=1066&h=189&f=png&s=18708)

##### 常用参数

- **-b**：以二进制方式，默认为文本方式（Binary (tell it like it is) file transfer override.）
- **-e**：对所有控制字符转义（Force sender to escape all control characters; normally XON, XOFF, DLE, CR-@-CR, and Ctrl-X are escaped.）

如果要保证上传的文件内容在服务器端保存之后与原始文件一致，最好同时设置这两个标志，如下所示方式使用：

```
rz -be
```

至此，我们已完成了服务器端的环境搭建。

## 小结

本小节重点介绍了如何使用腾讯云购买虚拟机的服务，以及如何配置 App 服务器端开发环境。


## 4基于 Tornado 的 HTTP 服务器简介及代码组织框架

# 基于 Tornado 的 HTTP 服务器简介及代码组织框架

Tornado 是一个 Python Web 框架和异步网络库，最初是在 FriendFeed 开发的。通过使用非阻塞网络I/O，Tornado 可以扩展到数以万计的开放连接，但却在创建和编写时足够的轻量级。

## Tornado 的特点

Tornado 和现在的很多主流 Web 服务器框架（包括大多数 Python 框架）有着明显的区别：它是非阻塞式异步服务器。大多数社交网络应用都会展示实时更新来提醒新消息、状态变化以及用户通知，客户端需要保持一个打开的连接来等待服务器端的任何响应。这些长连接或推送请求使得非异步服务器线程池迅速饱和。一旦线程池的资源耗尽，服务器将不能再响应新的请求。异步服务器在这一场景中的应用则不同，当负载增加时，诸如 Tornodo 这样的服务器，会把当前请求正在等待来自其他资源的数据，加以控制并挂起请求，以满足新的请求。这也是 Tornado 在高并发、高效率的 Web 服务器应用很广的原因之一。

## Tornado 入门

### 编写 Hello, world

上面我们已介绍了 Tornado 的强大，现在我们从一个简单的 `Hello World` 开始。在服务器上任意目录下（如 /data ），创建 `hello.py` 文件，输入如下代码：

```python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
```
编写一个 Tornado 应用中最多的工作是定义类继承 Tornado 的 `RequestHandler` 类。在这个例子中，我们创建了一个简单的应用，Tornado 监听给定的端口 `8888`，并在根目录（"/"）响应请求，响应的处理方法为继承了 `RequestHandler` 的 `MainHandler` 类。在 `MainHandler` 中返回 `Hello, world`。

### 测试代码


![](https://user-gold-cdn.xitu.io/2018/4/26/1630200d319e8bfc?w=405&h=87&f=png&s=3125)

在浏览器上打开 `http://150.109.33.132:8888`，测试结果如下：

![](https://user-gold-cdn.xitu.io/2018/4/21/162e5904ade344e0?w=502&h=113&f=png&s=5260)

**注：** 服务器上需要放开 8888 端口，如果是公有云云主机，注意安全组配置是否已放开。

至此，我们已完成基于 Tornado 服务器的 `Hello, world`。下面来简单介绍一下 Tornado 的整体框架。

## Tornado 框架

Tornado 大体上可以被分为 4 个主要的部分:
1. Web 框架 (包括创建 Web 应用的 `RequestHandler` 类，还有很多其他支持的类)；
2. HTTP的客户端和服务端实现 (HTTPServer and AsyncHTTPClient)；
3. 异步网络库 (IOLoop and IOStream), 
为HTTP组件提供构建模块，也可以用来实现其他协议；
4. 协程库 (tornado.gen) 允许异步代码写得更直接而不用链式回调的方式。

这里只做简单的了解，如需深入了解 Tornado，建议读者通读学习  [Tornado 官方文档](http://tornado-zh.readthedocs.io/zh/latest/guide.html)。

## 代码组织框架

在认识了 Tornado 之后，我们将正式进入本小册核心的学习。首先 Tornado 的学习必定是从 `Hello, world` 开始，并逐步按照个人编程习惯和组织习惯完善整个框架。

代码的组织框架因人而异，作为入门小册，这里提供一种简化的组织框架思路并贯穿整个小册，读者在熟练应用后，可采用自身的风格。

在某个目录下，创建本次的工程文件，如 demo，并依次创建如下文件：

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e4c9c2acd225?w=376&h=242&f=png&s=9428)

## 目录及文件说明

common：存放公共类和方法  
conf: 存放配置文件  
log：存放相关日志  
static：存放静态文件，如样式（CSS）、脚本（js）、图片等  
templates：公用模板目录，主要存放 HTML 文件  
views：视图函数，业务逻辑代码目录  
main.py：Tornado 主程序入口  
models.py：数据库表结构定义

## 小结

本小节简单介绍了 Tornado HTTP 服务器及本小册中使用的代码组织框架，从下一小节开始，正式进入代码编写讲解。


## 5第一次数据请求 1：服务器接收用户注册信息

# 第一次数据请求，服务器接收用户注册信息

本小节将是我们编写服务器端代码的开始。现在假设有这样一个 App（见下图），用户需要通过该界面提交注册信息。服务器端在接收到客户端的注册请求后，返回注册成功信息，并将该用户写入数据库表用户信息中。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e5245ff4d0d4?w=407&h=718&f=png&s=42477)

## 客户端模拟

考虑到本小册讲解的是服务器端，这里不作 App 端的介绍，我们将使用 HTTP 发包工具来模拟上面的 App 注册信息的提交。

HTTP 发包工具：[Getman](https://getman.cn/)

约定服务器端 HTTP server 的端口号为 8000，服务器端和客户端定义的请求是 `/users/regist`，那么完整的 URL 为 `http://150.109.33.132:8000/users/regist?`（请用自己的云虚拟机 IP 替换其中的 IP）。
参数为手机号（`phone`）、密码（`password`）及验证码（`code`），参数放入 HTTP 的 body 中，具体为：
`{"phone":"18866668888","password":"demo123456","code":"123456"}`<br>

**注：** 
1. 确保服务器端 8000 端口已放通；
2. 在实际的项目中，密码不会明文的传输，一般会在客户端先使用 md5 进行加密，服务器端存储的也是加密后的密码字符串。本小册作为学习示例，将使用明文讲解。<br>

**发包器模拟如下：**
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e672605297b9?w=779&h=279&f=png&s=17104)

客户端的请求至此已初步完成，现在，服务器端接收到客户端这个请求后，将如何处理呢？

## 服务器端处理

### 调用逻辑

![](https://user-gold-cdn.xitu.io/2018/4/17/162d421ec503ec5a?w=685&h=572&f=png&s=26711)

客户端以 POST 的方式，发送注册请求至服务器端，请求进入服务器端的 `main.py` 后，将调用 `url_router` 转发到 `users_url.py` 中，在 `users_urls.py` 中，对应的 URL 将调用 `users_views.py` 的 `RegistHandle` 类， `RegistHandle` 为真正的代码处理逻辑，在校验用户信息正确的情况下，返回 JSON 格式的注册成功信息给客户端。

### 编写服务器端入口函数

 `main.py` 是 Tornado 作为 HTTP 服务器的统一入口，根据前面的约定，Tornado 对外服务的端口号为 8000。

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Author: demo
# Email: demo@demo.com
# Version: demo

import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define,options

class Application(tornado.web.Application):
    def __init__(self):
        #定义 Tornado 服务器的配置项，如 static/templates 目录位置、debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, **settings)
 
 
 
if __name__ == '__main__':
    print ("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
```

保存 `main.py` 代码后，在服务器端运行此段代码
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e6756e0779e5?w=831&h=116&f=png&s=12072)

此时再次点击 HTTP 发包模拟器发送注册信息  
URL: `http://150.109.33.132:8000/users/regist?`  
入参：`{"phone":"18866668888","password":"demo123456","code":"123456"}`
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e6772d17bd6b?w=872&h=566&f=png&s=35971)

再次查看服务器端
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e6792966cf9e?w=971&h=164&f=png&s=18437)

此条打印说明，客户端的 HTTP 请求已到达服务器，服务器接收成功但处理失败了，原因为找不到路径 `/users/regist`。下面在服务器端编写针对  `/users/regist` 的处理代码。

### 编写路由转发

首先，服务器端从 `main.py` 收到客户端的请求后，需要将其转发给对应的处理模块。进入 common 目录，创建 `url_router.py` 文件
 

![](https://user-gold-cdn.xitu.io/2018/4/26/162fec3892c373b3?w=864&h=162&f=png&s=19504)

在 `url_router.py` 中输入如下代码。

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from importlib import import_module

def include(module):
    '''根据传入的字符串，调用相应的模块,如 module 为字符串 regist 时，
    调用views.users.users_views.RegistHandle 模块
    '''
    res = import_module(module)
    urls = getattr(res, 'urls', res)
    return urls
    
    
def url_wrapper(urls):
    '''拼接请求 url，调用对应的模块，如拼接 users 和 regist 成 url /users/regist，
    调用 views.users.users_views.RegistHandle 模块
    '''
    wrapper_list = []
    for url in urls:
        path, handles = url
        if isinstance(handles, (tuple, list)):
            for handle in handles:
                #分离获取字符串（如regist）和调用类（如views.users.users_views.RegistHandle）
                pattern, handle_class = handle
                #拼接url，新的url调用模块
                wrap = ('{0}{1}'.format(path, pattern), handle_class)
                wrapper_list.append(wrap)
        else:
            wrapper_list.append((path, handles))
    return wrapper_list
```
接下来修改 `main.py`，调用 `url_router.py` 将用户请求的路径转发给对应的请求模块。

增加如下几行，从 `common` 目录的 `url_router` 导入所需函数（ `from common.url_router import include, url_wrapper`），并在 `Application` 的类中，拼接转发路由。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e683eae8d788?w=651&h=616&f=png&s=41332)

完成后的代码如下：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Author: demo
# Email: demo@demo.com
# Version: demo

import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define,options
from common.url_router import include, url_wrapper
from tornado.options import define,options


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url_wrapper([
        (r"/users/", include('views.users.users_urls'))
        ])
        #定义 Tornado 服务器的配置项，如 static/templates 目录位置，debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__),"static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)
 

if __name__ == '__main__':
    print ("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
```
至此，`main.py` 的路由转发已完成，接下来将编写真正的处理模块。

进入 views 目录，创建 users 目录，该目录将存放所有跟用户信息处理相关的代码。在该目录下，创建 `users_urls.py`、`users_views.py`。
 

![](https://user-gold-cdn.xitu.io/2018/4/26/1630193b94de9b25?w=457&h=117&f=png&s=6776)
其中，`users_urls.py` 处理针对 `users` 相关的路由及调用类之间的路由，`users_views.py` 为真正的逻辑处理。在 `users_urls.py` 中输入如下代码：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .users_views import (
    RegistHandle
)

urls = [
    #从 /users/regist 过来的请求，将调用 users_views 里面的 RegistHandle 类
    (r'regist', RegistHandle)
]
	
```
在 `users_views.py` 文件中，输入如下代码：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode

# 从commons中导入http_response方法
from common.commons import (
    http_response,
)

# 从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)
 
class RegistHandle(tornado.web.RequestHandler):
    """handle /user/regist request
    :param phone: users sign up phone
    :param password: users sign up password
    :param code: users sign up code, must six digital code
    """
        
    def post(self):
        try:
            #获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            # 获取入参失败时，抛出错误码及错误信息
            http_response(self, ERROR_CODE['1001'], 1001)
            return 
            
        # 处理成功后，返回成功码“0”及成功信息“ok”
        http_response(self, ERROR_CODE['0'], 0)
```

在`users_views.py` 中看到，我们从公共方法库（`commons`）中导入了方法，并从配置文件中导入了错误码定义。接下来编写 `commons` 及 `base` 配置文件。
进入 common 目录，并创建 `commons.py` 文件，在 `commons.py` 中输入如下代码：
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e68ccde8beef?w=642&h=84&f=png&s=10262)

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

import json

def http_response(self, msg, code):
    self.write(json.dumps({"data": {"msg": msg, "code": code}}))

        
if __name__ == "__main__":
   http_response()
```

在 conf 目录下，创建 `base.py` 文件：
 

![](https://user-gold-cdn.xitu.io/2018/4/26/1630196b72f2d727?w=489&h=134&f=png&s=6687)

在 `base.py` 文件中，输入如下代码：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

ERROR_CODE = {
    "0": "ok",
    #Users error code
    "1001": "入参非法"
}
```
至此，我们已经完成了基本的用户注册以及服务器端处理逻辑代码，重新运行 `main.py`，查看是否启动正常。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e69187e0fc2a?w=836&h=133&f=png&s=14983)

现在再从 HTTP 发包模拟器
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e6931784b422?w=795&h=583&f=png&s=25718)

此时看到返回的 JSON 消息已成功。

再次查看服务器端，此时控制台打印的 log 提示 HTTP 200，表示该条 URL 请求已正确处理并返回。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e695cfc9bfd8?w=987&h=153&f=png&s=19756)

假如此时 HTTP 发包模拟器入参少了 `code` 参数，将提示错误信息。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e697a5a92e2d?w=683&h=582&f=png&s=25059)

至此，我们第一次客户端与服务器端的数据请求及回复已讲解完毕。完成后的目录结构及文件如下。

![](https://user-gold-cdn.xitu.io/2018/4/22/162ea8b6d4f5c4c6?w=818&h=520&f=png&s=59180)

## 代码下载

到目前为止，服务器端代码如下：  
[demo6](https://github.com/Jawish185/demo6.git)

## 小结
本小节讲解了客户端与服务器端的第一次数据请求及回复。代码比较简单，重点在于理解其中的 URL 路由转发，以达到触类旁通的效果。代码还有很多待完善的地方，如增加 log 管理，进一步抽象类和方法等。下一小节，我们将为代码加入 log 管理。


## 6第一次数据请求 2：为用户处理模块增加 log 管理

# 为用户处理模块增加 log 管理

作为一个程序员，log 管理几乎是必备技能，本小节将在原来代码的基础上，增加 log 管理，以方便调试。进入 log 目录，并创建 users 目录。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e7188017afcc?w=853&h=186&f=png&s=18537)
进入 `users_views.py`，导入 `logging` 模块，并指定 log 目录文件（`log/users/users.log`），指定 log 级别（`DEBUG`）和 log 保留方式（这里设定按天保存，保留 30 天的 log 记录），并在处理方法中加入对应的 log 信息。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e71ad3457ad9?w=534&h=588&f=png&s=38020)
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e71c8fccad36?w=475&h=394&f=png&s=24933)
`users_views.py` 的完整代码如下：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler

#从commons中导入http_response方法
from common.commons import (
    http_response,
)

#从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)
 

########## Configure logging #############
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")  
logger.setLevel(logging.DEBUG)  
handler = TimedRotatingFileHandler(logFilePath,  
                                   when="D",  
                                   interval=1,  
                                   backupCount=30)  
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)  
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)
 
 
class RegistHandle(tornado.web.RequestHandler):
    """handle /user/regist request
    :param phone: users sign up phone
    :param password: users sign up password
    :param code: users sign up code, must six digital code
    """
        
    def post(self):
        try:
            #获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            #获取入参失败时，抛出错误码及错误信息
            logger.info("RegistHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return 
            
        #处理成功后，返回成功码“0”及成功信息“ok”
        logger.debug("RegistHandle: regist successfully")
        http_response(self, ERROR_CODE['0'], 0)
```

再次执行 `main.py`
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e7200615e2a4?w=998&h=169&f=png&s=25114)

HTTP 客户端发起正确的注册请求
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e721e89630dc?w=760&h=577&f=png&s=25499)

查看 `log/users/users.log`
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e723ba998464?w=1135&h=191&f=png&s=27275)

在日志文件中，日志的格式包含时间、文件名、打印代码行数、log 级别和自定义 log 信息。这些信息足以满足问题定位及排错。在前面的配置信息中，我们定义的 log 级别是 `DEBUG`，下面看看入参出错时，报的 `INFO` 日志。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e72638e45fe7?w=745&h=568&f=png&s=25457)

查看 `log/users/users.log`
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e7283ad03005?w=1221&h=291&f=png&s=46000)

这里看到日志文件中多出了一行日志，级别为 INFO。前面我们也提到，我们定义了日志文件的记录保留，本小册由于是新建讲解项目，还无法直接查看日志保留记录。这里贴出之前项目的记录，可以看到历史保留文件是以天为后缀的，当天的文件还是在 `users.log` 中。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e72a64423a2c?w=742&h=450&f=png&s=28047)

## 代码下载

到目前为止，服务器端代码如下：  
[demo7](https://github.com/Jawish185/demo7.git)

## 小结

本小节简单介绍了日志服务在服务器端开发中的应用，开发者可以自定义 log 级别及其历史保留记录。开发者可以根据自己的喜好及习惯，去定义具体的级别和信息。下一小节，我们将讲解如何利用 ORM 的方式和数据库打交道，并将用户注册信息写入数据库中。


## 7第一次数据请求 3：将用户信息写入 MySQL 数据库

# 将用户信息写入 MySQL 数据库

上两小节已完成逻辑代码，这小节将学习使用 ORM 的方式将用户注册信息写入数据库中。

## 整个逻辑架构图

![](https://user-gold-cdn.xitu.io/2018/4/17/162d43602b033d38?w=769&h=578&f=png&s=33871)

数据库的信息（如地址、端口、用户名和密码等）存放在 `base.py` 中，`model.py` 中定义了数据库表并从 `base.py` 中获取数据库信息。当 `main.py` 启动时，其将调用 `model.py` 初始化数据库。而 `users_views.py` 负责将客户端的请求数据写入数据库中，并返回注册成功信息。

## 配置数据用户名和密码

用户名为 `root`，密码为 `pwd@demo`，
在服务器端输入如下命令配置数据库。

```shell
mysql -u root
set password for 'root' @localhost = password('pwd@demo');
```
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e761b234df07?w=1023&h=423&f=png&s=46537)

## 创建数据库

在服务器端输入如下命令创建数据库。

```shell
CREATE DATABASE demo CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';
```

创建完成后，使用 `show databases` 检查数据库是否创建成功。

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e764100fcc65?w=984&h=326&f=png&s=22404)

## 代码中配置数据库

在配置文件 `base.py` 中指定数据库，需修改 `conf/base.py`，增加如下代码：

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql://root:pwd@demo@localhost:3306/demo?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()
```

![](https://user-gold-cdn.xitu.io/2018/4/22/162ea967a288b36f?w=827&h=224&f=png&s=16085)
## 代码中定义数据库表
在前面的介绍中，我们提到，`models.py` 这个文件主要包含数据库表的定义及初始化。从第 6 小节中看到，用户注册信息包含手机号、密码和验证码。这里需要记录在数据库中的有手机号（`phone`）和密码（`password`），当然还包括创建的时间（`createTime`）。这些信息作为数据库表项，在 `models.py` 中定义，在 `models.py` 文件中输入如下代码：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

from conf.base import BaseDB, engine
import sys
from sqlalchemy import (
Column, 
Integer,
    String, 
    DateTime
)

    
class Users(BaseDB):
    """table for users
    """
    __tablename__ = "users"
    #定义表结构，包括id，phone，password，createTime
    id = Column(Integer, primary_key=True)
    phone = Column(String(50), nullable=False)
    password = Column(String(50), nullable=True)
    createTime = Column(DateTime, nullable=True)
    
    def __init__(self, phone, password, createTime):
        self.phone = phone
        self.password = password
        self.createTime = createTime
    
    
def initdb():
    BaseDB.metadata.create_all(engine)
    
if __name__ == '__main__':
    print ("Initialize database")
    initdb()
```	

## 代码中初始化数据库
在 `main.py` 中，调用 `models.py` 初始化数据库并启用数据库

![](https://user-gold-cdn.xitu.io/2018/4/22/162ea9ceea5f9845?w=705&h=672&f=png&s=52336)
具体代码如下：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-
# Author: demo
# Email: demo@demo.com
# Version: demo

import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define, options
from common.url_router import include, url_wrapper
from tornado.options import define, options
from models import initdb
from sqlalchemy.orm import scoped_session, sessionmaker
from conf.base import BaseDB, engine


class Application(tornado.web.Application):
    def __init__(self):
        initdb()
        handlers = url_wrapper([
        (r"/users/", include('views.users.users_urls'))
        ])
        #定义tornado服务器的配置项，如static/templates目录位置，debug级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db = scoped_session(sessionmaker(bind=engine,
                                  autocommit=False, autoflush=True,
                                  expire_on_commit=False))
 
 
if __name__ == '__main__':
    print ("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()
```
## 代码将用户信息写入数据库
修改 `users_views.py`，将用户数据写入数据库中，修改内容包括从 `models` 中导入 `Users` 类表，并判断用户是否在数据库中。如果存在，返回注册失败信息；如果不存在，将用户信息写入数据库，并返回注册成功信息。

![](https://user-gold-cdn.xitu.io/2018/4/22/162eaacef4db547f?w=555&h=469&f=png&s=24382)

![](https://user-gold-cdn.xitu.io/2018/4/22/162eaad1013a7464?w=601&h=680&f=png&s=53202)

`users_views.py` 完整代码如下：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
import sys
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime


#从commons中导入http_response方法
from common.commons import (
    http_response,
)

#从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)

from models import (
    Users
)
  
 
########## Configure logging #############
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")  
logger.setLevel(logging.DEBUG)  
handler = TimedRotatingFileHandler(logFilePath,  
                                   when="D",  
                                   interval=1,  
                                   backupCount=30)  
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)  
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)
 
 
class RegistHandle(tornado.web.RequestHandler):
    """handle /user/regist request
    :param phone: users sign up phone
    :param password: users sign up password
    :param code: users sign up code, must six digital code
    """
    
    @property
    def db(self):
        return self.application.db
        
    def post(self):
        try:
            #获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            #获取入参失败时，抛出错误码及错误信息
            logger.info("RegistHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return 
            
        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            #如果手机号已存在，返回用户已注册信息
            http_response(self, ERROR_CODE['1002'], 1002)
            self.db.close()
            return
        else:
            #用户不存在，数据库表中插入用户信息
            logger.debug("RegistHandle: insert db, user: %s" %phone)
            create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            add_user = Users(phone, password, create_time)                         
            self.db.add(add_user)
            self.db.commit()
            self.db.close()
            #处理成功后，返回成功码“0”及成功信息“ok”
            logger.debug("RegistHandle: regist successfully")
            http_response(self, ERROR_CODE['0'], 0)
            
```

## 增加错误码处理

修改 base.py，增加错误码 1002：

```python
"1002": "用户已注册，请直接登录",
```

![](https://user-gold-cdn.xitu.io/2018/4/22/162eaaee9fc4d2a5?w=857&h=242&f=png&s=18751)

## 结果检查
上面的几大步骤，从配置数据库，到代码指定数据库，再到将用户信息写入数据库，我们已完成了数据库部分代码的编写，下面执行 `main.py` 文件，查看是否运行正常。
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e7716c1fbcc4?w=987&h=123&f=png&s=15264)

### HTTP 发包模拟器再次请求注册信息
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e773c3e1648d?w=806&h=584&f=png&s=25959)

### 查看控制台
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e775c4e51c32?w=1016&h=103&f=png&s=18891)

### 查看数据库

![](https://user-gold-cdn.xitu.io/2018/4/7/1629e777a8c83dee?w=1025&h=765&f=png&s=69867) 

### 在 HTTP 发包模拟器上再次点击注册
 
![](https://user-gold-cdn.xitu.io/2018/4/7/1629e779988d7341?w=779&h=585&f=png&s=26334)

可以看到，服务器端返回的错误信息提示该用户已注册。

## 代码下载

到目前为止，服务器端代码如下：  
[demo8](https://github.com/Jawish185/demo8.git)

## 小结

至此，我们已完成了数据库的写入，加上前两节的逻辑处理和 log 处理，客户端与服务器端的第一条消息请求交互已完成。这里只是使用到了 SQLAlchemy 很有限的功能，SQLAlchemy 具有很强大的功能，感兴趣的同学可以访问 [SQLAlchemy 官网](http://docs.sqlalchemy.org/en/latest/)学习。


## 8服务器接收客户端图片上传，并保存在硬盘中

# 服务器接收客户端图片上传，并保存在硬盘中

前面几小节，我们已完成了 JSON 格式的纯数据交互，在 App 服务器端的设计中，我们难免会接收客户端图片的上传，并提供端图片下载。本小节将讲解，对于客户端向服务器端上传图片，服务器端将如何处理。简单交互过程如下。
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b016baced81f9?w=706&h=198&f=png&s=24562)

同样，在这一小节中，我们也使用工具来代替 App 客户端模拟图片的上传。我们将要用到的工具是 JMeter，它是一个强大的工具，最为熟知的是 HTTP 的测试。这里我们不去深入了解 JMeter，而只是取其一个小功能 —— HTTP POST 图片的功能来完成讲解，读者如果感兴趣，可以自行学习拓展。

## 下载 JMeter

通过官网下载 JMeter：[Download Apache JMeter](http://jmeter.apache.org/download_jmeter.cgi)
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b016f2582b9d1?w=1048&h=681&f=png&s=139458)

## 安装 JMeter

下载完成后，解压文件夹，进入 bin 目录，点击  `jmeter.bat` 进行 JMeter 的安装，安装成功后的界面如下。
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b0172c6aa7e48?w=1515&h=848&f=png&s=70006)

## 配置测试计划

### 切换语言
 
依次选择“Options” -> “Choose Language” -> “Chinese (Simplified)”，如下图所示。

![](https://user-gold-cdn.xitu.io/2018/4/10/162b0175614cebde?w=742&h=463&f=png&s=42771)

### 配置 HTTP 请求

右击 “Test Plan”，点击“添加” -> “Threads (Users)”  -> “线程组”
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b017d5d4ed6e9?w=586&h=277&f=png&s=29665)

右击 “线程组”，点击 “添加” -> “Sampler” -> “HTTP 请求”
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b017fce1d6291?w=611&h=344&f=png&s=37222)

在弹出的「HTTP 请求」框中进行如下设置：

- 第 1~4 步，按照截图输入或选择；  
- 第 5 步，设定我们要上传图片（文件）的 URL 路径是 `upload/file`；  
- 第 6 步，选择 “Files Upload”；  
- 第 7 步，点击 ”添加”；  
- 第 8 步，点击 “浏览”，从本地随便选取一张图片（或本小节末尾提供的图片）；  
- 第 9 步，输入该图片对象的参数名 `image`；  
- 第 10 步，输入我们上传的文件类型 `image`。
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b0182eb3d2e1b?w=994&h=735&f=png&s=38839)

至此，请求页面已配置完毕，点击 “文件” -> “保存测试计划” 如下。
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b01853ef37a86?w=435&h=256&f=png&s=19368)

## 测试请求

点击如下 “启动” 按钮，测试是否请求成功
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b0188040102af?w=656&h=396&f=png&s=32936)

### 查看服务器端
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b018b29ac28c2?w=994&h=167&f=png&s=20565)

此打印说明服务器端接收客户端请求成功，但由于 `/upload/file` 路径的代码未实现，服务器端返回 404 找不到路径。接下来，将进行服务器端图片上传代码编写。

## 服务器端代码编写

### 调用逻辑

![](https://user-gold-cdn.xitu.io/2018/4/17/162d43e54cccf2e6?w=692&h=569&f=png&s=27412)

与第 6 小节用户注册请求服务器端实现类似，客户端上传图片，进入 `main.py`，将调用 `url_router` 转发到 `upload_url.py` 中，在 `upload_urls.py` 中，对应的 URL 将调用 `upload_views.py` 的 `UploadFileHandle` 类，`UploadFileHandle` 为真正的代码处理逻辑，在校验用户信息正确的情况下，返回图片 URL 给客户端，客户端加载该图片。

### 创建目录

在 views 下面创建 upload 目录，在 upload 下创建 `upload_urls.py`、`upload_views.py`等文件。
 

![](https://user-gold-cdn.xitu.io/2018/4/26/163019a3f15879f9?w=477&h=194&f=png&s=11522)

在 log 目录下创建 upload 目录，用于存放日志。
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b018ff477d6fe?w=770&h=169&f=png&s=18322)

图片一般会放在 static 目录下，在实际项目中，static 下的图片目录也是分层级的，此次讲解，我们将简化，把图片直接放在 `static/image` 目录下。创建 image 目录如下：
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b0194ac9e4f25?w=898&h=162&f=png&s=19749)

### 编写逻辑代码

修改 `main.py` 文件，增加 `views.upload.upload_urls`下的 url 路由，修改 `handers` 如下：

```python
        handlers = url_wrapper([
        (r"/users/", include('views.users.users_urls')),
        (r"/upload/", include('views.upload.upload_urls'))
        ])
```

![](https://user-gold-cdn.xitu.io/2018/4/22/162eb057967dbeb7?w=667&h=303&f=png&s=26303)
 
修改 `upload_urls.py`，输入如下代码：

```python
#!/usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .upload_views import (
    UploadFileHandle
)

urls = [
    #从/upload/file过来的请求，将调用upload_views里面的UploadFileHandle类
    (r'file', UploadFileHandle)
]
```
修改 `upload_views.py`，输入如下代码：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
import os
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler
import json


#从commons中导入http_response及save_files方法
from common.commons import (
    http_response,
    save_files
)

#从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
    SERVER_HEADER
)

########## Configure logging #############
logFilePath = "log/upload/upload.log"
logger = logging.getLogger("Upload")  
logger.setLevel(logging.DEBUG)  
handler = TimedRotatingFileHandler(logFilePath,  
                                   when="D",  
                                   interval=1,  
                                   backupCount=30)  
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)  
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)
 
 
class UploadFileHandle(tornado.web.RequestHandler):
    """handle /upload/file request, upload image and save it to static/image/
    :param image: upload image
    """
        
    def post(self):
        try:
            #获取入参
            image_metas = self.request.files['image']
        except:
            #获取入参失败时，抛出错误码及错误信息
            logger.info("UploadFileHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return 
            
        image_url = ""
        image_path_list = []
        if image_metas:
            #获取当前的路径
            pwd = os.getcwd()
            save_image_path = os.path.join(pwd, "static/image/")
            logger.debug("UploadFileHandle: save image path: %s" %save_image_path)
            #调用save_file方法将图片数据流保存在硬盘中
            file_name_list = save_files(image_metas, save_image_path)
            image_path_list = [SERVER_HEADER + "/static/image/" + i for i in file_name_list]
            ret_data = {"imageUrl": image_path_list}
            #返回图片下载地址给客户端
            self.write(json.dumps({"data": {"msg": ret_data, "code": 0}}))
        else:
            #如果图片为空，返回图片为空错误信息
            logger.info("UploadFileHandle: image stream is empty")
            http_response(self, ERROR_CODE['2001'], 2001)
```
这里，我们从 `common` 导入 `save_files` 用于处理图片的保存，从 conf 的 `base` 中导入 `SERVER_HEADER`，定义了我们服务器的 URL 前缀。同时也看到，`upload` 和 `users` 的 Log 配置（如级别）是单独配置的，这样有助于单模块调试。下面修改 conf 目录下的 `base.py` 文件，增加如下：


![](https://user-gold-cdn.xitu.io/2018/4/22/162eaffe8896b51d?w=852&h=309&f=png&s=24281)
完整代码如下：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql://root:pwd@demo@localhost:3306/demo?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()

#服务器端 IP+Port，请修改对应的IP
SERVER_HEADER = "http://150.109.33.132:8000"

ERROR_CODE = {
    "0": "ok",
    #Users error code
    "1001": "入参非法",
    "1002": "用户已注册，请直接登录",
    
    "2001": "上传图片不能为空"
}
```

`commons.py` 下，导入 `os` 模块（ `import os` ），并增加 `save_files` 方法：

```python
import os

def save_files(file_metas, in_rel_path, type='image'):
    """
    Save file stream to server
    """
    file_path = ""
    file_name_list = []
    for meta in file_metas:
        file_name = meta['filename']
        file_path = os.path.join( in_rel_path, file_name )
        file_name_list.append( file_name )
        #save image as binary
        with open( file_path, 'wb' ) as up:
            up.write( meta['body'] )
    return file_name_list
```
至此，服务器端的代码已完成。再次从 JMeter 触发图片上传，在触发图片上传之前，我们先创建 JMeter 的结果树。所谓结果树，就是在触发请求之后，查看服务器端返回的结构。右击 “HTTP 请求”，依次选择“添加” -> ”监听器” -> “查看结果树”，如下图所示。
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b01a2427e2341?w=799&h=472&f=png&s=56335)

触发 JMeter 图片上传，点击 “察看结果树”，切到 “响应数据” 页面，可以看到服务器端返回的数据信息：

```json
{"data": {"msg": {"imageUrl": ["http://150.109.33.132:8000/static/image/demo.jpg"]}, "code": 0}}
```
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b01a450869998?w=1156&h=458&f=png&s=61558)
查看服务器端进程打印：
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b01a60d7352fd?w=1257&h=161&f=png&s=21992)
查看图片是否上传：
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b01a7e78bd9fd?w=993&h=179&f=png&s=18882)
查看 log 是否成功写入：
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b01a9d7cdfc23?w=1496&h=161&f=png&s=29180)

此时，客户端就可以通过服务器端返回的图片 URL（`http://150.109.33.132:8000/static/image/demo.jpg`）加载图片了，在浏览器中输入图片 URL，查看加载是否成功。
 
![](https://user-gold-cdn.xitu.io/2018/4/10/162b01ac3f15236a?w=1112&h=669&f=png&s=965733)

## 代码下载

到目前为止，服务器端代码及图片如下：  
[demo9](https://github.com/Jawish185/demo9.git)

## 小结
至此，我们完成了服务器端图片上传的接收及图片 URL 返回，客户端根据服务器返回的图片 URL，即可加载该图片。这里没有写数据库的操作，读者可以尝试参考第 8 节的讲解，定义图片的 `models`，并将图片 URL 和其他信息写入数据库中。


## 9服务器接收客户端请求，并返回 H5 页面

# 服务器接收客户端请求，并返回 H5 页面

在前几节中，我们讲解了客户端与服务器端数据的交互及图片的上传加载，这一节将讲解 H5 页面的请求及加载。

在 App 客户端的设计中，一般的公司都会要求两个端，分别为 Android 和 iOS 端。如果是客户端负责页面的生成，那 Android 端和 iOS 端都将分别做重复的工作，另一个问题是，可能由于开发人员不一样，页面的设计有出入。现在主流的思想会倾向于使用 H5 嵌入客户端当中，H5 文件存放在服务器端，客户端只负责请求并加载。这样就给服务器端提出了一个问题：如何将服务器上的 H5 文件返回给客户端？本小节将解答这个问题。

## 调用逻辑

在第 6 小节的讲解中，用户的信息已注册并写入数据库，这一小节中，我们将模拟该用户登录请求，并在登录成功后，返回 App 首页（即本小节预设的 H5 页面）。下面是本小节涉及的请求流程图。

![](https://user-gold-cdn.xitu.io/2018/4/15/162c75200f75aacc?w=708&h=635&f=png&s=27319)

由于我们需要通过浏览器代替 App 客户端进行用户注册请求模拟，此次客户端请求将使用 GET 方法。请求进入服务器端的 `main.py` 后，将调用 `url_router` 转发到 `users_url.py` 中，在 `users_urls.py` 中，对应的 URL 将调用 `users_views.py` 的 `LoginHandle`  类。`LoginHandle`  为真正的代码处理逻辑，在校验用户信息正确的情况下，返回 `index.html` 页面给客户端，客户端加载该页面。

## 服务器端实现

由上面的调用逻辑图可知，我们将从 `main.py` 开始修改，由于在第 6 小节中， `main.py` 针对 `users` 的路由已配置，这里 `main.py` 不需要修改。接下来修改 `users_url.py`，在 `users_url.py` 中增加 `LoginHandle` 的调用，添加如下两行。

![](https://user-gold-cdn.xitu.io/2018/4/15/162c7a800ee5ed2f?w=595&h=290&f=png&s=10318)

完整代码如下：

```python
#! /usr/bin/python3
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
from .users_views import (
    RegistHandle,
    LoginHandle
)

urls = [
    #从/users/regist过来的请求，将调用users_views里面的RegistHandle类
    (r'regist', RegistHandle),
    (r'login', LoginHandle)
]
```

接下来，添加真正的代码处理，修改 `users_views.py`，增加 `LoginHandle` 类代码如下：

```python
class LoginHandle(tornado.web.RequestHandler):
    """handle /user/regist request
    :param phone: users sign up phone
    :param password: users sign up password
    """
    
    @property
    def db(self):
        return self.application.db
        
    def get(self):
        try:
            #获取入参
            phone = self.get_argument( "phone" )
            password = self.get_argument( "password" )
        except:
            #获取入参失败时，抛出错误码及错误信息
            logger.info("LoginHandle: request argument incorrect")
            http_response(self, ERROR_CODE['1001'], 1001)
            return 
        
        #从数据库 Users 表查找入参中的 phone 是否存在    
        ex_user = self.db.query(Users).filter_by(phone=phone).first()
        if ex_user:
            #如果手机号已存在，返回首页 H5 页面 index.html
            logger.debug( "LoginHandle: get user login: %s" %phone )
            self.render( "index.html" )
            self.db.close()
            return
        else:
            #用户不存在，提示用户未注册
            http_response( self, ERROR_CODE['1003'], 1003 )
            self.db.close()
            return
```

这里的新增错误码 `1003` 表示用户未注册，需在配置文件中添加此错误码，编辑 `base.py` 增加如下代码：

```python
"1003": "用户尚未注册，请先注册",
```

![](https://user-gold-cdn.xitu.io/2018/4/22/162eb107c1edd1e1?w=556&h=172&f=png&s=8902)

至此，服务器端的代码逻辑已基本完成，现在唯一缺少的就是 `index.html` 这个文件。

## H5 页面代码

由于本小册的重点并不是讲解 H5，这里请读者直接按照指导将 H5 涉及的代码输入服务器端，本小册不做另外的讲解。

### 新增 index.html 文件

进入 “templates” 目录，创建并编辑 `index.html` 文件，输入如下代码：
 
![](https://user-gold-cdn.xitu.io/2018/4/15/162c75a1b09eb2d5?w=907&h=184&f=png&s=21218)

```HTML
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>css网页布局</title>
    <link rel="stylesheet" href="../static/css/index.css">
</head>
<body>
<!--整体到部分，左到右，上到下-->
    <!--头部-->
    <div class="header">
        <div class="logo">
            <ul>
                <li>DEMO</li>
            </ul>
        </div>
        <div class="nav">
            <ul>
                <li>About</li>
            </ul>
        </div>
    </div>
    <!--主体-->
    <div class="main">
        <div class="top">
            <img src="../static/image/index/index.jpg" alt="topimg">
        </div>
        <!--遮罩层-->
        <div class="topplayer"></div>
        <!--最上层的内容-->
        <div class="topplayer-top">
            <div class="word">MY DEMO H5</div>
        </div>
        <div class="middle">
            <div class="m-top">
                <div class="demo-layer demo1">
                    <img src="../static/image/index/1.jpg" alt="DEMO1">
                    <div class="demo">DEMO1</div>
                </div>
                <div class="demo-layer demo1">
                    <img src="../static/image/index/2.jpg" alt="DEMO2">
                    <div class="demo">DEMO2</div>
                </div>
                <div class="demo-layer demo3">
                    <img src="../static/image/index/3.jpg" alt="DEMO3">
                    <div class="demo">DEMO3</div>
                </div>
                <div class="clear"></div>
            </div>
            <div class="m-middle">
                "Life is like riding a bicycle. To keep your balance, you must keep moving."
            </div>
            <div class="m-bottom">
                <div class="m-com">
                    <img src="../static/image/index/4.jpg" alt="4.jpg">
                    <div class="demo4">Cool Demo</div>
                    <div class="demo5">Make it cool</div>
                </div>
                <div class="m-com">
                    <img src="../static/image/index/5.jpg" alt="5.jpg">
                    <div class="demo4">Great Demo</div>
                    <div class="demo5">Make it great</div>
                </div>
                <div class="m-com">
                    <img src="../static/image/index/6.jpg" alt="6.jpg">
                    <div class="demo4">Wonderful Demo</div>
                    <div class="demo5">Make it wonderful</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
```

### 新增 index.css 文件

进入 “static/css” 目录，创建并编辑 `index.css` 文件，输入如下代码：

![](https://user-gold-cdn.xitu.io/2018/4/15/162c75a6be8f0e49?w=980&h=163&f=png&s=19497)

```css
* {
    margin: 0;
    padding: 0;
}
.header {
    width: 100%;
    height: 100px;
}
.header img {
    width: 300px;
    height: 85px;
    padding-left: 100px;
    padding-top: 8px;
}
.header .logo {
    float: left;
    margin-top: 40px;
    margin-left: 40px;
}
.header .nav {
    float: right;
}
.header .nav ul {
    margin-right: 20px;
}
.header .nav ul li {
    float: left;
    list-style: none;
    width: 80px;
    height: 100px;
    line-height: 100px;
    color: #7d7d7d;
    font-size: 15px;
    font-weight: bolder;
}
.main .top {
    width: 100%;
    height: 600px;
}
.main .top img {
    width: 100%;
    height: 600px;
}
.main .topplayer {
    position: absolute;
    top: 100px;
    background: #000000;
    width: 100%;
    height: 600px;
    opacity: 0.5; /* 透明度 */
}
.main .topplayer-top {
    width: 500px;
    height: 300px;
    position: absolute;
    top: 400px;
    margin-top: -150px;
    z-index: 2;
    right: 50%;
    margin-right: -250px;
}
.main .topplayer-top .word {
    padding-top: 100px;
    color: #ffffff;
    font-size: 45px;
    font-weight: bolder;
    text-align: center;
    font-family: "微软雅黑";
}
.main .topplayer-top button {
    width: 200px;
    height: 60px;
    margin-top: 50px;
    color: #ffffff;
    background: #f5704f;
    font-family: 微软雅黑;
    text-align: center;
    font-weight: bolder;
    font-size: 14px;
    border-radius: 8px; /* 圆角 */
    margin-left: 150px;
}
.main .middle {
    width: 1000px;
    margin: 0 auto;
}
.main .middle .m-top .demo-layer {
    float: left;
    width: 33.3%;
    padding-top: 50px;
    text-align: center;
}
.main .middle .m-top .demo-layer img {
    width: 100px;
    height: 100px;
}
.main .middle .m-top .demo-layer .demo {
    font-size: 20px;
    color: #7d7c7f;
    font-weight: bold;
    padding-top: 20px;
}
.main .middle .m-middle {
    font-size: 25px;
    color: #000000;
    font-weight: bold;
    padding-top: 50px;
    text-align: center;
    padding-bottom: 50px;
}
.clear {
    clear: both;
}
.main .middle .m-bottom .m-com {
    float: left;
    padding: 10px;
    text-align: center;
    font-weight: bold;
    font-size: 20px;
}
.main .middle .m-bottom .m-com img {
    width: 310px;
    height: 260px;
}
.main .middle .m-bottom .demo4 {
    padding-top: 20px;
    color: #7d7d7f;
}
.main .middle .m-bottom .demo5 {
    padding-top: 10px;
    color: #bdbdbc;
}
.main .bottom {
    width: 1000px;
    margin: 0 auto;
}
.footer {
    width: 100%;
    height: 100px;
    text-align: center;
    line-height: 100px;
    background: #292c35;
    color: white;
    font-family: "微软雅黑";
    font-size: 15px;
}
```
### 上传 H5 页面图片

进入 “static/image” 目录，创建 `index` 文件夹，上传 H5 页面图片。

```
mkdir index
cd index/
rz -be
```
具体如下图所示：
![](https://user-gold-cdn.xitu.io/2018/4/15/162c75aca938c399?w=898&h=202&f=png&s=24452)

![](https://user-gold-cdn.xitu.io/2018/4/15/162c75b0998b006b?w=743&h=217&f=png&s=20033)

至此，H5 的页面准备工作已结束， 服务器端的代码已全部完成。接下来将测试请求是否成功。

### 客户端请求 H5 页面

由于 App 客户端嵌入 H5 页面和手机浏览器直接打开 H5 页面的效果一样，这里在手机的浏览器中直接输入请求 URL 进行测试，URL 为：
`http://150.109.33.132:8000/users/login?phone=18866668888&password=demo123456`。请求成功后，可以看到加载的效果如下：

<div style="text-align: center">
<img src="https://user-gold-cdn.xitu.io/2018/4/15/162c75b3c03dce17?w=1080&h=1920&f=jpeg&s=237165" style="width: 480px">
</div>

## 代码下载
到目前为止，服务器端代码及图片如下：  
[demo10](https://github.com/Jawish185/demo10.git)

## 小结

这一小节中，我们探讨了为什么建议客户端嵌套 H5 页面，并完成了客户端向服务器端请求 H5 页面的整个代码逻辑学习过程，希望读者能触类旁通，提高产品上线效率。


