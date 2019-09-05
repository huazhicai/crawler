# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
from fake_useragent import UserAgent
import requests
import time

"""
需要带encoding,发送reques请求
"""


class RequestUrl_Charset(Action):
    def __init__(self):
        self.headers = {
            'User-Agent': ''}

    def __call__(self, args, io):
        url = args['url_str']
        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        re = requests.get(url=url, headers=headers)
        time.sleep(1)
        Charset = args['charset_str']
        re.encoding = Charset
        Content = re.text
        if re.status_code == 200 and len(Content) > 0:
            io.set_output('response_str', Content)
            io.push_event('Out')
        else:
            self.__call__(args, io)


"""
直接发送reques请求
"""
class RequestUrl(Action):
    def __init__(self):
        self.headers = {
            'User-Agent': ''}

    def __call__(self, args, io):
        url = args['url_str']
        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        re = requests.get(url=url, headers=headers)
        Content = re.text
        if re.status_code == 200 and len(Content) > 0:
            io.set_output('response_str', Content)
            io.push_event('Out')
        else:
            self.__call__(args, io)
