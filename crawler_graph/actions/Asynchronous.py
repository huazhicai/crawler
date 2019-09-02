# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
from gevent import monkey
import gevent
from fake_useragent import UserAgent
from lxml import html

from fake_useragent import UserAgent
import requests
import time

"""
通过异步发送requests请求
"""
class AsynchronousRequests(Action):
    def __init__(self):
        self.headers = {
           'User-Agent': ''
        }
    def req(self,url,io):
        headers = self.headers
        headers['User-Agent'] = UserAgent().chrome
        re = requests.get(url=url, headers=self.headers)
        re.encoding = 'gb2312'
        con = re.text
        if re.status_code == 200 and len(con) > 0:
            io.set_output('Doc', con)
            io.push_event('Out')
        else:
            print("未渲染成功")
            self.req(url, io)
    def __call__(self, args, io):
        urls = args['Url']
        gevent.joinall([gevent.spawn(self.req, url,io) for url in urls])

"""
通过异步Splash渲染页面
"""
class AsynchronousSplash(Action):
        def __init__(self):
            self.splash_url = "http://10.0.30.10:8050//render.html"
            self.headers = {
                'User-Agent': ''}
        def req(self, url, io):
            headers = self.headers
            headers['User-Agent'] = UserAgent().chrome
            args = {
                "url": url,
                "timeout": 7,
                "wait": 0.5
            }
            re = requests.get(self.splash_url, params=args,headers=headers)
            # time.sleep(1)
            con = re.text

            if re.status_code == 200 and len(con)>0:
                io.set_output('Doc', con)
                io.push_event('Out')
            else:
                print("未渲染成功")
                self.req(url, io)

        def __call__(self, args, io):
            urls = args['Url']
            print(urls)
            gevent.joinall([gevent.spawn(self.req, url, io) for url in urls])




