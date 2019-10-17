# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
contact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
from pyppeteer import launch
import json
import pymongo
import os
import asyncio


class ConsoleOutput(Action):
    """屏幕输出打印信息"""

    def __call__(self, args, io):

        prefix = args.get('prefix_optional_str', None)
        result = args['result_any']
        if prefix:
            print(prefix, result)
        else:
            print(result)

    id = '94ca1b06-e967-11e9-9ff5-8cec4bd887f3'


class DataStore(Action):
    """节点中数据暂时存储"""

    def __call__(self, args, io):
        data = args['data_any']
        io.set_output('data_any', data)

    id = '9bdf5664-e967-11e9-8d60-8cec4bd887f3'


class InsertToMongo(Action):
    """将数据存入Mongodb中"""

    def __call__(self, args, io):
        mongo_url = args['url_str']
        mongo_db = args['db_str']
        mongo_chart = args['collection_str']
        data = args['doc_dict']

        client = pymongo.MongoClient(mongo_url)
        db = client[mongo_db]
        collection = db[mongo_chart]
        if collection.insert_one(data):
            print(data)
        else:
            print('Insert to mongodb failed!')

    id = 'bbe99e18-e967-11e9-ad5f-8cec4bd887f3'


class UpdateToMongo(Action):
    """将数据存入Mongodb中"""

    def __call__(self, args, io):
        mongo_url = args['url_str']
        mongo_db = args['db_str']
        mongo_chart = args['collection_str']
        data = args['doc_dict']
        query_key = args['query_key_str']

        client = pymongo.MongoClient(mongo_url)
        db = client[mongo_db]
        collection = db[mongo_chart]
        if collection.update_one({query_key: data[query_key]}, {'$set': data}, True):
            print(data)
        else:
            print('Update to mongodb failed!')

    id = 'c1cdbb36-e967-11e9-b968-8cec4bd887f3'


class ToJsonFile(Action):
    """数据保存为json格式文件"""

    def __call__(self, args, io):
        filename = args['filename_str'].strip()
        if filename.endswith('.txt'):
            filename = filename.strip('.txt')

        if not filename.endswith('.json'):
            filename = filename + '.json'

        data = args['doc_dict']
        file = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', filename)
        with open(file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')

    id = '94ff84f8-e9a4-11e9-bbe0-f416630aacec'


class AcquireCookie(Action):
    """通过pyppeteer模拟登录获取cookie"""

    async def login(self, login_url, username, password, user_css, password_css, submit_css, ):

        broswer = await launch(headless=False, autoClose=False, args=['--disable-infobars'])
        # browser = await launch(headless=True, args=['--disable-infobars', f'--window-size={self.width},{self.height}'])
        page = await broswer.newPage()
        # 是否启用JS，enabled设为False，则无渲染效果
        # await page.setJavaScriptEnabled(enabled=False)
        print("###开始登录###")
        await page.goto(login_url)
        await page.type(user_css, username)

        await page.type(password_css, password)
        await page.click(submit_css)
        # await asyncio.sleep(1)
        page_url = page.url
        if page_url != login_url:
            await asyncio.sleep(1)
            print("###登录成功###")
            cookie_obj = await page.cookies()
            cookie = cookie_obj
            await broswer.close()
            return cookie
        else:
            print('登录失败请重新输入')

    def __call__(self, args, io):
        login_url = args['login_url_str']
        username = args['username_str']
        password = args['password_str']
        user_css = args['user_css_str']
        password_css = args['password_css_str']
        submit_css = args['submit_css_str']
        try:
            cookie = asyncio.get_event_loop().run_until_complete(
                self.login(login_url, username, password, user_css, password_css, submit_css, ))
            io.set_output('cookie_list', cookie)
            io.push_event('Out')
        except Exception as e:
            print(e)

    id = '74870f18-e96a-11e9-829a-8cec4bd887f3'


class FormatData(Action):
    """接收爬虫输出字典数据，转换为['name': some, 'value': other ]"""

    def __call__(self, args, io):
        doc = args['doc_dict']

        output = []
        for key, value in doc.items():
            temp = dict()
            temp['name'] = key
            temp['value'] = value
            output.append(temp)

        io.set_output('output_str', json.dumps(output).replace("'", '"'))
        io.push_event('Out')

    id = 'af5b8e9a-ef20-11e9-9bb3-f416630aacec'
