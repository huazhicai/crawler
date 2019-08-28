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


class RequestUrl(Action):
    def __init__(self):


        self.headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }
    def __call__(self, args, io):
        url = args['Url']
        re = requests.get(url=url, headers=self.headers)
        # time.sleep(1)
        # Charset = args['Charset']
        # re.encoding = Charset
        con = re.text
        io.set_output('Doc', con)
        io.push_event('Out')


