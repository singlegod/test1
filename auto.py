# -*- coding: utf-8 -*- 
"""
Project: test
Creator: wcm
Create time: 2020-03-28 16:37
IDE: PyCharm
Introduction:
"""
import requests
from pprint import pprint

# 添加课程
res = requests.post('/api/mgr/sq_mgr', data={
    'action': 'add_course',
    'data': '''{
    "name":"猴哥",
    "desc":"初中化学",
    "display_idx":"4"
    }
    '''

})
retObj = res.json()

if retObj['retcode'] == 0:
    print('检查点通过')
else:
    print("检查不通过")


pprint(res.json(), width=30)

# 列出课程
# res = requests.get('http://2.python-requests.org/zh_CN/latest/')


#
# if res.status_code == 200:
#     pprint(res.json())
# else:
#     print('不通过')
