# #-*- coding: utf-8 -*-
# """
# copyright. AIIT
# created by LiQing.
# created by LiQing
# ccontact blacknepia@dingtail.com for more information
"""
通过selenium模拟登录获取cookie
"""
#
from runtime.Action import Action
import requests
import time
from selenium import webdriver
from time import sleep

#需要将睡眠时间设为可输入参数
class Selenium_Acquire_Cookie(Action):
    def __init__(self):
        self.options = webdriver.ChromeOptions()

    def __call__(self, args, io):
        self.options.binary_location = args['browser_address_str']
        self.chrome_driver_path = args['driver_address_str']
        self.browser = webdriver.Chrome(self.chrome_driver_path, options=self.options)
        url = args['Url']

        UserName = args['UserName']
        PassWord = args['PassWord']
        self.browser.get(url)
        self.browser.maximize_window()
        time_sleep = args['time_sleep']
        sleep(time_sleep)
        loginId = args['loginId_label_name']
        password = args['password_label_name']
        submit = args['submit_label_name']
        self.browser.find_element_by_name(loginId).send_keys(UserName)
        self.browser.find_element_by_name(password).send_keys(PassWord)
        self.browser.find_element_by_name(submit).click()
        sleep(time_sleep)
        cookies_dict = self.browser.get_cookies()
        io.set_output('cookies_dict', cookies_dict)
        io.push_event('Out')
