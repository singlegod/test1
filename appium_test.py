# -*- coding: utf-8 -*- 
"""
Project: untitled
Creator: wcm
Create time: 2020-03-29 09:07
IDE: PyCharm
Introduction:
"""
from appium import webdriver
import time, traceback

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9.0'
desired_caps['deviceName'] = 'test'
desired_caps['automationName'] = 'UiAutomator1'
desired_caps['app'] = r'/home/wcm/Code/Python/pydj/test/toutiao.apk'
desired_caps['appPackage'] = 'io.manong.developerdaily'  # 界面
desired_caps['appActivity'] = 'io.toutiao.android.ui.activity.LaunchActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
desired_caps['noReset'] = True
desired_caps['newCommandTimeout'] = 6000

# 启动Remote RPC
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    driver.implicitly_wait(10)

    # 根据id找到元素，并点击，id和html元素的id不同

    driver.find_element_by_id("io.manong.developerdaily:id/tab_bar_plus").click()

    time.sleep(1)
    driver.find_elements_by_android_uiautomator("new UiSelector().text(\"密码登录\")")[0].click()

    # 输入手机号，密码
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_phone")
    ele.send_keys('18236532735')

    # driver.find_element_by_id(
    #     'io.manong.developerdaily:id/btn_send_verifycode').click()
    time.sleep(3)
    ele = driver.find_element_by_id("io.manong.developerdaily:id/edt_password")
    ele.send_keys('123456')

    time.sleep(3)
    # 点击登录
    driver.find_element_by_id("io.manong.developerdaily:id/btn_login").click()
except:
    print(traceback.format_exc())
input("**** Press Any to quit ****")
