# -*- coding: utf-8 -*- 
"""
Project: untitled
Creator: wcm
Create time: 2020-03-30 10:31
IDE: PyCharm
Introduction:
"""
import paramiko

# 创建SSHClient实例对象
ssh = paramiko.SSHClient()

# 信任远程主机，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# 连接远程服务器
ssh.connect("192.168.1.104",  # Addr
            22,  # Port
            "stt5",  # username
            "stt5200")  # password
ssh.exec_command("")