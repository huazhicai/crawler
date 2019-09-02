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
# from runtime.Action import Action
# import requests
# import time
# from selenium import webdriver
# from time import sleep
# ss = requests.Session()
#
# class TestCookie(Action):
# 	def __init__(self):
# 		self.options = webdriver.ChromeOptions()
# 		self.options.binary_location = r"C:\Program Files (x86)\ChromeCore\ChromeCore.exe"
# 		self.chrome_driver_path = r"D:\Crawl/chromedriver.exe"
# 		self.browser = webdriver.Chrome(self.chrome_driver_path, options=self.options)
# 		self.Sesson= requests.Session()
#
#
# 	def __call__(self, args, io):
# 		url = args['Url']
# 		account = args['Account']
#
# 		UserName = account['UserName']
# 		PassWord = account['PassWord']
#
# 		self.browser.get(url)
# 		self.browser.maximize_window()
# 		sleep(2)
# 		self.browser.find_element_by_name('loginId').send_keys(UserName)
# 		self.browser.find_element_by_name('password').send_keys(PassWord)
# 		self.browser.find_element_by_name('submit').click()
# 		sleep(4)
# 		cookies = self.browser.get_cookies()
#
# 		io.set_output('cookies', cookies)
# 		io.push_event('Out')
#
#
#
