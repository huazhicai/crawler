# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
from fake_useragent import UserAgent
from lxml import html
import requests
import time

"""
通过Splash Api接口 进行对页面js渲染，获取网页源代码
"""


class SplashUrl(Action):
    def __init__(self):
        self.splash_url = "http://10.0.30.10:8050//render.html"
        self.headers = {
            'User-Agent': ''}

    def __call__(self, args, io):
        url = args['url_str']
        Charset = args['charset_str']
        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome

        params = {
            "url": url,
            "timeout": 7,
            'time': 0.5
        }
        re = requests.get(self.splash_url, params=params, headers=headers)
        re.encoding = Charset
        time.sleep(1)
        Content = re.text
        if re.status_code == 200 and len(Content) > 0:
            io.set_output('response_str', Content)
            io.push_event('Out')
        else:
            self.__call__(args, io)
