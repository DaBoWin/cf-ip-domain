# cf-ip-domain 自建优选域名

## 前言
### 自建优选域名
### 基于vps789.com-全球主机测速平台接口： https://vps789.com/vps/sum/cfIpTop20 提供的优选IP 自动更新优选域名。特别感谢ns大佬captain102 以及vps789.com 开放了优选IP的API
### 建议结合 https://www.nodeseek.com/post-84561-1 的文档配合食用
### 2024-03-29 更新 增加自建优选反代域名脚本bestproxydomain.py 以及 tg频道通知, 特别感谢大佬ymyuuu开发优选IP的API，对应github地址： https://github.com/ymyuuu/IPDB

## 准备工作
1. 已经托管到CF的一个域名
2. 一个独立的vps（自己完全控制，并注意避免泄露自己的API KEY）

## 安装python
1.大多数 Linux 发行版都预装了 Python。您可以通过以下命令检查版本：
```
python --version
```
2.如果您的系统没有 Python，或者您需要特定版本，则可以使用发行版的包管理器进行安装。例如，在 Ubuntu 上，您可以使用以下命令：
```
sudo apt install python3
```
3.安装pip
```
sudo apt-get install python3-pip
```
4.安装cloudflare的python包
```
sudo pip install cloudflare
```
5.安装telebot的python包
```
sudo pip install pyTelegramBotAPI
```
## 下载代码文件以及修改对应配置，请仔细修改对应配置，否则可能有意想不到的错误
下载cfipdomain.py 并修改你的cf权证对应的配置，详细请参考如下代码说明：
```
# Cloudflare API 凭证
cloudflare_api_key = "替换你CF的API密钥"
cloudflare_email = "替换你登录CF的邮箱"
zone_id = "你域名的区域ID"

# 域名
domain_name = "替换你在cf托管的域名，比如dabo.free.hr"
# DNS 记录名称
record_short_name = "替换你的dns名称，比如cfip"
# 优选域名全名称
record_name = "替换你的域名全称 比如cfip.dabo.free.hr"

# tg机器人token以及 频道ID
tg_bot_token = "替换你的tg机器人的token, 如果不需要发送，这个字段请设置为空字符"
tg_chat_id = "替换你的频道的chat_id 比如大波妹频道 @dabo_girl"
```
## 上传修改好配置之后的cfipdomain.py文件 到你的vps服务器根目录
可以通过smtp本地直接上传到服务器
## 执行代码（执行完可以上cf网站进入域名的dns记录查看是否成功生成域名dns记录）
```
python3 cfipdomain.py
```
## 定时crontab任务
比如每天8点执行一次优选域名对应IP的更新, 执行crontab -e命令添加如下命令并保存
```
0 8 * * * python3 cfipdomain.py
```

