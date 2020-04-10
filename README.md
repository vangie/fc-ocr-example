# 函数计算 Python tesserocr 示例

该示例借助于 [Funfile](./Funfile) 机制安装了最新的 4.1.1 版本的 tesseract，相比于包管理器的 3.0.2 版本识别率大幅度提升。

## 依赖工具

本项目是在 MacOS 下开发的，涉及到的工具是平台无关的，对于 Linux 和 Windows 桌面系统应该也同样适用。在开始本例之前请确保如下工具已经正确的安装，更新到最新版本，并进行正确的配置。

* [Docker](https://www.docker.com/)
* [Funcraft](https://github.com/alibaba/funcraft)

对于 MacOS 用户可以使用 [homebrew](https://brew.sh/) 进行安装：

```bash
brew cask install docker
brew tap vangie/formula
brew install fun
```

Windows 和 Linux 用户安装请参考：

1. https://github.com/aliyun/fun/blob/master/docs/usage/installation.md
2. https://github.com/aliyun/fcli/releases

安装好后，记得先执行 `fun config` 初始化一下配置。

**备注: 本文介绍的技巧需要 Fun 版本大于等于 3.6.8 。**

## 初始化

```bash
git clone https://github.com/vangie/fc-ocr-example.git
```

## 安装依赖


```bash
$ fun install
```

## 本地测试

包含文字的示例图片 [sample.jpg](./sample.jpg)

![](https://img.alicdn.com/tfs/TB1_bIFBxD1gK0jSZFKXXcJrVXa-422-492.jpg)

```bash
$ fun local invoke
using template: template.yml

Missing invokeName argument, Fun will use the first function tesserocr/tesserocr as invokeName

mounting local nas mock dir /Users/vangie/Workspace/fc-ocr-example/.fun/nas/auto-default/tesserocr into container /mnt/auto

mounting local nas mock dir .fun/root into container /mnt/auto/root

mounting local nas mock dir .fun/python into container /mnt/auto/python

mounting local nas mock dir tessdata_fast into container /mnt/auto/tessdata

skip pulling image aliyunfc/runtime-python3.6:1.9.4...
FunctionCompute python3 runtime inited.
FC Invoke Start RequestId: b8a4236a-f8eb-4025-8147-ad700efcd3e4
2020-04-10T13:03:15.268Z b8a4236a-f8eb-4025-8147-ad700efcd3e4 [INFO] Funcraft

(have)Fun with Serverless

2020-04-10T13:03:15.269Z b8a4236a-f8eb-4025-8147-ad700efcd3e4 [INFO] [92, 90, 93, 92]
FC Invoke End RequestId: b8a4236a-f8eb-4025-8147-ad700efcd3e4
Funcraft

(have)Fun with Serverless


RequestId: b8a4236a-f8eb-4025-8147-ad700efcd3e4          Billed Duration: 527 ms         Memory Size: 1989 MB    Max Memory Used: 33 MB
```

从上面的日志看到 OCR 识别的内容

```text
Funcraft

(have)Fun with Serverless
```

## 同步文件到 NAS

同步模型目录 `tessdata_fast` 和 依赖目录 `.fun/root` `.fun/python` 到 NAS 盘。

```bash
$ fun nas sync
```

## 部署

```bash
$ fun deploy
using template: template.yml
using region: cn-shanghai
using accountId: ***********3743
using accessKeyId: ***********Ptgk
using timeout: 60

Collecting your services information, in order to caculate devlopment changes...

Resources Changes(Beta version! Only FC resources changes will be displayed):

┌───────────┬──────────────────────────────┬────────┬──────────────────────┐
│ Resource  │ ResourceType                 │ Action │ Property             │
├───────────┼──────────────────────────────┼────────┼──────────────────────┤
│           │                              │        │ Description          │
│ tesserocr │ Aliyun::Serverless::Service  │ Add    ├──────────────────────┤
│           │                              │        │ NasConfig            │
├───────────┼──────────────────────────────┼────────┼──────────────────────┤
│           │                              │        │ Handler              │
│           │                              │        ├──────────────────────┤
│           │                              │        │ Runtime              │
│ tesserocr │ Aliyun::Serverless::Function │ Add    ├──────────────────────┤
│           │                              │        │ CodeUri              │
│           │                              │        ├──────────────────────┤
│           │                              │        │ EnvironmentVariables │
└───────────┴──────────────────────────────┴────────┴──────────────────────┘

service tesserocr deploy success


===================================== Tips for nas resources ==================================================
Fun has detected the .nas.yml file in your working directory, which contains the local directory:

        /Users/vangie/Workspace/fc-ocr-example/.fun/root
        /Users/vangie/Workspace/fc-ocr-example/.fun/python
        /Users/vangie/Workspace/fc-ocr-example/tessdata_fast
  
The above directories will be automatically ignored when 'fun deploy'.
Any content of the above directories changes，you need to use 'fun nas sync' to sync local resources to remote.
===============================================================================================================
```

## 执行

```bash
$ fun invoke
using template: template.yml

Missing invokeName argument, Fun will use the first function tesserocr/tesserocr as invokeName

========= FC invoke Logs begin =========
FC Invoke Start RequestId: 5da45c0e-1978-4591-84a3-3986d1dcf024
2020-04-10T13:22:46.359Z 5da45c0e-1978-4591-84a3-3986d1dcf024 [INFO] Funcraft

(have)Fun with Serverless

2020-04-10T13:22:46.359Z 5da45c0e-1978-4591-84a3-3986d1dcf024 [INFO] [92, 90, 93, 92]
FC Invoke End RequestId: 5da45c0e-1978-4591-84a3-3986d1dcf024

Duration: 597.09 ms, Billed Duration: 600 ms, Memory Size: 128 MB, Max Memory Used: 80.66 MB
========= FC invoke Logs end =========

FC Invoke Result:
Funcraft

(have)Fun with Serverless
```
