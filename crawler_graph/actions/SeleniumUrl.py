# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
import requests
from lxml import html
import time
from selenium import webdriver
from time import sleep


# class SeleniumUrlsssssss(Action):
#暂时不用写这个节点
#     def __init__(self):
#         self.options = webdriver.ChromeOptions()
#         self.options.binary_location = r"C:\Program Files (x86)\ChromeCore\ChromeCore.exe"
#         self.chrome_driver_path = r"D:\Crawl/chromedriver.exe"
#         self.browser = webdriver.Chrome(self.chrome_driver_path, options=self.options)
#         self.Sesson = requests.Session()
#
#     def __call__(self, args, io):
#         url = args['Url']
#         account = args['Account']
#         querys = args['Query']
#
#         UserName = account['UserName']
#         PassWord = account['PassWord']
#
#         self.browser.get(url)
#         self.browser.maximize_window()
#         time.sleep(2)
#         self.browser.find_element_by_name('loginId').send_keys(UserName)
#         self.browser.find_element_by_name('password').send_keys(PassWord)
#         self.browser.find_element_by_name('submit').click()
#         sleep(4)
#         for query in querys:
#             self.browser.find_element_by_id('quickSearchInput').clear()
#             self.browser.find_element_by_id('quickSearchInput').send_keys(query)
#             time.sleep(3)
#             self.browser.find_element_by_id('tdAdvSearch').click()
#             time.sleep(3)
#             content = self.browser.page_source
#             io.set_output('result', content)
#             io.push_event('Out')
"""
通过selenium模拟，获取网页源代码
"""
# class SeleniumUrl_headless(Action):
#     def __init__(self):
#         self.options = webdriver.ChromeOptions()
#         self.options.add_argument("--headless")
#     def __call__(self, args, io):
#         self.options.binary_location = args['browser_address_str']
#         self.chrome_driver_path = args['driver_address_str']
#         self.browser = webdriver.Chrome(self.chrome_driver_path, options=self.options)
#         url = args['Url']
#         self.browser.get(url)
#         time.sleep(1)
#         Content = self.browser.page_source
#         etree = html.etree
#         tree = etree.HTML(Content)
#         title = tree.xpath('/html/head/title/text()')
#         title = ''.join(title)
#         title = ' '.join(title.split())
#         webpage_title = args['webpage_title_str']
#         if title == webpage_title:
#             io.set_output('response_str', Content)
#             io.push_event('Out')
#         else:
#             print("未渲染成功")
#             self.__call__(args, io)

# class SeleniumUrl(Action):
#     def __init__(self):
#         self.options = webdriver.ChromeOptions()
#     def __call__(self, args, io):
#         self.options.binary_location = args['browser_address_str']
#         self.chrome_driver_path = args['driver_address_str']
#         self.browser = webdriver.Chrome(self.chrome_driver_path, options=self.options)
#         url = args['Url']
#         self.browser.get(url)
#         time.sleep(1)
#         Content = self.browser.page_source
#         etree = html.etree
#         tree = etree.HTML(Content)
#         title = tree.xpath('/html/head/title/text()')
#         title = ''.join(title)
#         title = ' '.join(title.split())
#         webpage_title = args['webpage_title_str']
#         if title == webpage_title:
#             io.set_output('response_str', Content)
#             io.push_event('Out')
#         else:
#             print("未渲染成功")
#             self.__call__(args, io)
