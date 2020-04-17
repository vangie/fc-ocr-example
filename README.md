# 函数计算 Python tesserocr 示例

该示例借助于 [Funfile](./Funfile) 机制安装了最新的 4.1.1 版本的 tesseract，相比于包管理器的 3.0.2 版本识别率大幅度提升。

![](https://img.alicdn.com/tfs/TB15bTyCvb2gK0jSZK9XXaEgFXa-1455-935.gif)

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

```bash
$ fun local start domain_for_ocr
using template: template.yml
CustomDomain domain_for_ocr of tesserocr/tesserocr was registered
        url: http://localhost:8000/
        methods: [ 'GET', 'POST' ]
        authType: ANONYMOUS

function compute app listening on port 8000!
```

使用浏览器打开 http://localhost:8000/

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

...

Detect 'DomainName:Auto' of custom domain 'domain_for_ocr'
Fun will reuse the temporary domain 1712300-1986114430573743.test.functioncompute.com, expired at 2020-04-27 19:35:00, limited by 1000 per day.

Waiting for custom domain domain_for_ocr to be deployed...
custom domain domain_for_ocr deploy success

...
```
注意上面返回的临时域名地址：1712300-1986114430573743.test.functioncompute.com

使用浏览器打开 http://1712300-1986114430573743.test.functioncompute.com