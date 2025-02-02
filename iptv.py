'''
Author: zeyujay zeyujay@gmail.com
Date: 2024-07-04 21:44:25
LastEditors: zeyujay zeyujay@gmail.com
LastEditTime: 2024-07-04 22:12:43
FilePath: /channel/iptv.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''
import requests
 
# 目标URL
url = 'http://tonkiang.us/hoteliptv.php'
 
# 表单数据
data = {
    'search': '上海电信',
    'Submit': ''
}
 
# 发送POST请求
response = requests.post(url, data=data)
 
# 输出响应内容
print(response.text)