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


import requests
import time


class AsynchronousRequests(Action):
    def __init__(self):
        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
    def req(self,url,io):
        re = requests.get(url=url, headers=self.headers)
        re.encoding = 'gb2312'
        con = re.text
        io.set_output('Doc', con)
        io.push_event('Out')
    def __call__(self, args, io):
        urls = args['Url']
        gevent.joinall([gevent.spawn(self.req, url,io) for url in urls])

class AsynchronousSplash(Action):
        def __init__(self):
            self.splash_url = "http://10.0.30.10:8050//render.html"

        def req(self, url, io):
            args = {
                "url": url,
                "timeout": 7,
                "wait": 2,
            }
            re = requests.get(self.splash_url, params=args)
            con = re.text
            io.set_output('Doc', con)
            io.push_event('Out')

        def __call__(self, args, io):
            urls = args['Url']
            print(urls)
            gevent.joinall([gevent.spawn(self.req, url, io) for url in urls])




