# -*- coding: utf-8 -*- 
"""
Project: test
Creator: wcm
Create time: 2020-03-28 15:36
IDE: PyCharm
Introduction:
"""
a = [1, 1.333, 'a']
a[0] = 2
print(a[0])

b = (1, 1.222, 'a', 'abc')
# b[0]=2 不支持元素定义
print(b[0])
