
﻿Node 里怎么打印日志呢？

有同学说，不也是用 console.log 么。

不，服务端打印日志一般不会用 console.log。

因为 console.log 打印完就没了，而服务端的日志经常要用来排查问题，需要搜索、分析日志内容，所以需要写入文件或者数据库里。

而且打印的日志需要分级别，比如有的是错误的日志，有的只是普通日志，需要能够过滤不同级别的日志。

此外，打印的日志需要带上时间戳，所在的代码位置等信息。

这些都是 console.log 没有的功能。

所以我们一般都会用专门的日志框架来做，比如 winston。

它是 Node 最流行的日志框架，[npm 官网](https://www.npmjs.com/package/winston)上可以看到每周千万级的下载量：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-1.png)

那 winston 都有什么功能？怎么用呢？

我们试试看：

```
mkdir winston-test
cd winston-test
npm init -y
```

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-2.png)

先创建个项目。

安装 winston：

```
npm install --save winston
```
然后写下 index.js

```javascript
import winston from 'winston';

const logger = winston.createLogger({
    level: 'debug',
    format: winston.format.simple(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.File({ 
            dirname: 'log', filename: 'test.log' 
        }),
    ]
});

logger.info('光光光光光光光光光');
logger.error('东东东东东东东东');
logger.debug(66666666);
```
用 createLogger 创建了 logger 实例，指定 level、format、tranports。

level：打印的日志级别

format：日志格式

transports：日志的传输方式

我们指定了 Console 和 File 两种传输方式。

在 package.json 里指定 type 为 module，也就是所有代码都是 es module 的：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-3.png)

这样代码里就可以直接用 import、export 这些语法了。

用 node 跑一下：

```
node index.js
```

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-4.png)

可以看到控制台和文件里都有了打印的日志。

再跑一遍：

```
node index.js
```
会在后面追加：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-5.png)

那么问题来了，如果所有日志都写在一个文件里，那这个文件最终会不会特别大？

不用担心，winston 支持按照大小自动分割文件：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-6.png)

我们指定 maxsize 为 1024 字节，也就是 1kb。

然后再跑几次：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-7.png)

大概跑了 10 次左右，出现了第二个文件：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-8.png)

而这时第一个日志文件刚好是 1kb：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-9.png)

这就是根据大小自动分割日志文件的功能。

有同学说，一般日志都是按照日期自动分割的，比如 2023-10-28 的日志文件，2023-10-29 的日志文件，这样之后也好管理。

这个支持么？

当然支持，但是要换别的 Transport 了。

在 [winston 文档](https://github.com/winstonjs/winston/blob/HEAD/docs/transports.md#winston-core)里可以看到有很多 Transport：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-10.png)

Console、File、Http、Stream 这几个 Transport 是内置的。

下面还有很多社区的 Transport，比如 MongoDB 的 Transport，很明显就是把日志写入 mongodb 的。

这里的 DailyRotateFile 就是按照日期滚动存储到日志文件的 Transport。

我们试试看：

```
npm install --save winston-daily-rotate-file
```
安装这个 Transport。

然后改下代码：

```javascript
import winston from 'winston';
import 'winston-daily-rotate-file';

const logger = winston.createLogger({
    level: 'debug',
    format: winston.format.simple(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.DailyRotateFile({
            level: 'info',
            dirname: 'log2',
            filename: 'test-%DATE%.log',
            datePattern: 'YYYY-MM-DD-HH-mm',
            maxSize: '1k'
        })
    ]
});

logger.info('光光光光光光光光光');
logger.error('东东东东东东东东');
logger.debug(66666666);
```

这里使用了 DailyRotateFile 的 transport，然后指定了文件名和日期格式。

指定文件名里的日志格式包含分钟，所以不同的分钟打印的日志会写入不同文件里：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-11.png)

这就达到了滚动日志的效果。

再来试试 http 的 transport：

先创建个 nest 服务：

```
nest new winston-log-server
```
![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-12.png)

添加一个路由：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-13.png)
```javascript
@Post('log')
log(@Body() body) {
    console.log(body);
}
```
把它跑起来：

```
npm run start:dev
```
![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-14.png)

然后改下 index.js

```javascript
import winston from 'winston';
import 'winston-daily-rotate-file';

const logger = winston.createLogger({
    level: 'debug',
    format: winston.format.simple(),
    transports: [
        new winston.transports.Console(),
        new winston.transports.Http({
            host: 'localhost',
            port: '3000',
            path: '/log'
        })
    ]
});

logger.info('光光光光光光光光光');
logger.error('东东东东东东东东');
logger.debug(66666666);
```
使用 http 的 transport 来传输日志。

跑一下：
```
node ./index.js
```
![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-15.png)

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-16.png)

nest 服务收到了传过来的日志。

基本上，内置的和社区的 transport 就足够用了，不管是想把日志发送到别的服务，还是把日志存到数据库等，都可以用不同 Transport 实现。

这些 transport 可以用 add、remove 方法来动态增删：

```javascript
import winston from 'winston';

const console = new winston.transports.Console();
const file = new winston.transports.File({ filename: 'test.log' });

const logger = winston.createLogger({
    level: 'debug',
    format: winston.format.simple()
});

logger.clear();
logger.add(console);
logger.remove(console);
logger.add(file);

logger.info('光光光光光光光光光');
logger.error('东东东东东东东东');
logger.debug(66666666);
```
比如我先 clear，然后动态添加又删除了 console，然后又添加了一个 file 的 transport。

效果就是只有一个 file 的 transport：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-17.png)

再就是日志级别，winston 有 6 种级别的日志：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-18.png)

从上往下，重要程度依次降低。

比如当你指定 level 是 info 时，那 info、warn、error 的日志会输出，而 http、debug 这些不会。

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-19.png)

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-20.png)

日志级别的功能虽然简单，但却是很实用的功能。

日志可以通过 format 指定格式：

simple：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-21.png)

json：
![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-22.png)

prettyPrint（比 json 的格式多了一些空格）：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-23.png)

用 combine 组合 timestamp 和 json：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-24.png)

或者再组合个 label：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-25.png)

加上个标签，再搜索相关日志就方便多了。

彩色：

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-26.png)

通过这些，就可以指定各种日志格式。

但现在有个问题，如果我不同的 transport 要指定不同的格式呢？

可以这样：

```javascript
import winston from 'winston';

const logger = winston.createLogger({
    level: 'debug',
    transports: [
        new winston.transports.Console({
            format: winston.format.combine(
                winston.format.colorize(),
                winston.format.simple()
            ),
        }),
        new winston.transports.File({ 
            dirname: 'log3',
            filename: 'test.log',
            format: winston.format.json()
        }),
    ]
});

logger.info('光光光光光光光光光');
logger.error('东东东东东东东东');
logger.debug(66666666);
```

每个 transport 单独指定 format 就好了。

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-27.png)

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-28.png)

那如果我有的日志只想 console，而有的日志希望写入文件，而且配置都不同呢？

我们可以创建多个 logger 实例，每个 logger 实例有不同的 format、transport、level 等配置：

```javascript
import winston from 'winston';

winston.loggers.add('console', {
    format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
    ),
    transports: [
        new winston.transports.Console()
    ]
});

winston.loggers.add('file', {
    format:winston.format.combine(
        winston.format.timestamp(),
        winston.format.json()
    ),
    transports: [
        new winston.transports.File({
            dirname: 'log4',
            filename: 'test.log',
            format: winston.format.json()
        })
    ]
});


const logger1 = winston.loggers.get('console');

logger1.info('aaaaa');
logger1.error('bbbbb');

const logger2 = winston.loggers.get('file');

logger2.info('xxxx');
logger2.info('yyyy');
```
我们创建了 2 个 logger 实例，其中一个只写入 console，另一个只写入 file，并且 format 都不同。

然后分别用不同的 logger 来打印日志。

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-29.png)

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-30.png)

这样，项目中有不同的日志需求的时候，就可以创建多个 logger 实例。

此外，winston 还支持指定如何处理未捕获的错误的日志：

```javascript
import winston from 'winston';

const logger = winston.createLogger({
    level: 'debug',
    format: winston.format.simple(),
    transports: [
        new winston.transports.Console()
    ],
    exceptionHandlers: [
        new winston.transports.File({
            filename: 'error.log'
        })
    ]
});

throw new Error('xxx');

logger.info('光光光光光光光光光');
logger.error('东东东东东东东东');
logger.debug(66666666);
```
跑一下，可以看到错误日志被输出到了 error.log

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-31.png)

除了 error 外，Promise 的未捕获异常也可以指定如何处理日志：

```javascript
import winston from 'winston';

const logger = winston.createLogger({
    level: 'debug',
    format: winston.format.simple(),
    transports: [
        new winston.transports.Console()
    ],
    rejectionHandlers: [
        new winston.transports.File({
            filename: 'rejection.log'
        })
    ]
});

(async function(){
    throw Error('yyy');
})();

logger.info('光光光光光光光光光');
logger.error('东东东东东东东东');
logger.debug(66666666);
```

![](//liushuaiyang.oss-cn-shanghai.aliyuncs.com/nest-docs/image/第27章-32.png)

这些就是 winston 的主要功能了。

案例代码在[小册仓库](https://github.com/QuarkGluonPlasma/nestjs-course-code/tree/main/winston-test)。

## 总结

Node 服务端我们不会用 console.log 打印日志，而是会用日志框架，比如 winston。

winston 支持 tranport 配置，可以把日志传输到 console、file、通过 http 发送到别的服务，写入 mongodb 数据库等。

社区有很多 transport 可用，我们尝试了滚动日志的 transport，可以根据日期来自动分割日志文件。

winston 还支持 level 配置，可以根据级别来过滤日志。

而且还支持 format 的设置，比如 json、simple、label、timstamp 等，一般我们输出到文件里的都是 json 格式，并且给他加上时间戳和 label，这样方便之后分析。

每个 transport 都可以单独指定 format，而且还可以创建多个 logger，每个 logger 用不同的配置。

此外，winston 还支持指定未捕获的 error 的日志怎么处理。

总之，相比直接 console.log，用 winston 这样的灵活强大的日志框架可太香了。
