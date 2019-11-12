# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""
import asyncio

from fake_useragent import UserAgent
from pyppeteer import launch
from runtime.Action import Action
from selenium import webdriver
from time import sleep
import requests
import gevent


class Selenium_Acquire_Cookie(Action):
    """通过selenium模拟登录获取cookie"""
    _id = '86c160e8-e968-11e9-a25d-8cec4bd887f3'

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


class SplashUrl(Action):
    """通过Splash Api接口 进行对页面js渲染，获取网页源代码"""

    def __init__(self):

        self.headers = {
            'User-Agent': ''}

    def __call__(self, args, io):
        splash_url = args['splash_url']
        url = args['url_str']
        Charset = args['charset_str']
        timeout = args['timeout']
        time = args['time']

        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        params = {
            "url": url,
            "timeout": timeout,
            'time': time
        }
        re = requests.get(splash_url, params=params, headers=headers)
        re.encoding = Charset

        Content = re.text
        if re.status_code == 200 and len(Content) > 0:
            io.set_output('response_str', Content)
            io.push_event('Out')
        else:
            self.__call__(args, io)

    id = '917f710a-e968-11e9-872d-8cec4bd887f3'


class AsySplash(Action):
    """通过异步Splash渲染页面"""

    def __init__(self):
        self.splash_url = "http://10.0.30.10:8050//render.html"
        self.headers = {
            'User-Agent': ''}
        self.Charset = ''

    def __call__(self, args, io):
        urls = args['url_list']
        self.Charset = args['charset_str']

        gevent.joinall([gevent.spawn(self.req, url, io) for url in urls])

    def req(self, url, io):
        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        params = {
            "url": url,
            "timeout": 4,
            "wait": 0.5
        }
        re = requests.get(self.splash_url, params=params, headers=headers)
        re.encoding = self.Charset
        content = re.text
        if re.status_code == 200 and len(content) > 0:
            io.set_output('Content', content)
            io.push_event('Out')
        else:
            print("未渲染成功")
            self.req(url, io)

    id = '9862e40c-e968-11e9-b4d6-8cec4bd887f3'


class PypCookie(Action):
    async def login(self, args, io):
        login_url = args['login_url_str']
        selector_value = args['key_value_dict']
        submit = args['submit_selector_str']

        browser = await launch({'headless': False})
        page = await browser.newPage()
        await page.setViewport({'width': 1000, 'height': 768})
        await page.goto(login_url)
        for key, value in selector_value:
            await page.type(key, value)
        await page.waitFor(1000)
        await page.click(submit)
        await page.waitFor(3000)

        cookie_list = await page.cookies()
        cookies = {}
        for cookie in cookie_list:
            cookies.update({cookie['name']: cookie['value']})

        await browser.close()
        # io.set_output('cookies_dict', cookies)
        return cookies

    def __call__(self, args, io):
        cookies = asyncio.get_event_loop().run_until_complete(self.login(args, io))
        io.set_output('cookies_dict', cookies)
        io.push_event('Out')
