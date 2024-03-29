import requests
import json
import CloudFlare
import telebot
import os
import sys


def get_best_proxy_ip():
    # 发送 HTTP 请求
    response = requests.get("https://ipdb.api.030101.xyz/?type=bestproxy")
    
    # 检查响应状态码
    if response.status_code == 200:
        # 返回 text 数据
        return response.text
    else:
        # 返回 None 表示请求失败
        return None

# 获取优选IP
ip_addresses = get_best_proxy_ip().strip().split('\n')

# Cloudflare API 凭证
cloudflare_api_key = "替换你CF的API密钥"
cloudflare_email = "替换你登录CF的邮箱"
zone_id = "你域名的区域ID"

# 域名
domain_name = "替换你在cf托管的域名，比如dabo.free.hr"
# DNS 记录名称
record_short_name = "替换你的dns名称，比如proxyip"
# 优选域名全名称
record_name = "替换你的域名全称 比如proxyip.dabo.free.hr"

# tg机器人token以及 频道ID
tg_bot_token = "替换你的tg机器人的token, 如果不需要发送，这个字段请设置为空字符"
tg_chat_id = "替换你的频道的chat_id 比如大波妹频道 @dabo_girl"

# 要添加的 DNS 记录
dns_records = []
for ip_address in ip_addresses:
    print(ip_address)
    dns_record = {
            "type": "A",
            "name": record_short_name,
            "content": ip_address,
            "ttl": 120,
            "proxied": False,
        }
    dns_records.append(dns_record)
            
cf = CloudFlare.CloudFlare(cloudflare_email, cloudflare_api_key)
    
# 删除记录
record_type = 'A'
old_dns_records = cf.zones.dns_records.get(zone_id, params={'name': record_name, 'type': record_type})
print('开始删除DNS记录')
for record in old_dns_records:
    print(record['id'], record['name'], record['type'], record['content'])
    dns_record_id = record['id']
    cf.zones.dns_records.delete(zone_id, dns_record_id)
print('删除DNS记录完成')

# 添加记录
print('开始添加新的DNS记录')
for dns_record in dns_records:
    try:
        print(dns_record['content'])
        r = cf.zones.dns_records.post(zone_id, data=dns_record)
    except CloudFlare.CloudFlareAPIError as e:
        exit('/zones.dns_records.post %s - %d %s' % (record['name'], e, e))
print('添加新的DNS记录成功')

if (tg_bot_token != '') :
    bot = telebot.TeleBot(tg_bot_token)
    bot.send_message(tg_chat_id, text= record_name + " 反代优选域名更新成功！")
    print('发送频道消息成功')