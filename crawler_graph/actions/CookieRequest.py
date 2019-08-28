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

class CookieRequest(Action):
    def __init__(self):

        self.ss = requests.Session()
        # self.url='http://chinackd.medidata.cn/jsp/para/pm2/pdm.jsp?PtId=83290'


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



