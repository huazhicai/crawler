#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""






from runtime.Action import Action
import requests
ss = requests.Session()
"""
通过添加cookie，向指定页面发送请求，获取网页源代码
"""
class CookieRequest(Action):
    def __init__(self):
        self.ss = requests.Session()
    def __call__(self, args, io):
        ss = self.ss
        cookies = args['cookies']
        headers = args['Headers']
        url = args['Url']
        for cookie in cookies:
            ss.cookies.set(cookie['name'], cookie['value'])
        re = ss.get(url=url, headers=headers)
        con = re.text
        io.set_output('result', con)
        io.push_event('Out')



