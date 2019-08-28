# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
import requests
import time


class SplashUrl(Action):
    def __init__(self):
        self.splash_url = "http://10.0.30.10:8050//render.html"
    def __call__(self, args, io):
        url = args['Url']
        print(url)
        """
        args参数说明：
        url: 需要渲染的页面地址
        timeout: 超时时间
        proxy：代理
        wait：等待渲染时间
        images: 是否下载，默认1（下载）
        js_source: 渲染页面前执行的js代码
        """
        args = {
            "url": url,
            "timeout":7,
            "wait":2,
        }
        re = requests.get(self.splash_url, params=args)
        con = re.text
        io.set_output('Doc', con)
        io.push_event('Out')






