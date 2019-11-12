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
import pymssql


class ConsoleOutput(Action):
    """屏幕输出打印信息"""
    _id = '94ca1b06-e967-11e9-9ff5-8cec4bd887f3'
    node_info = {"args": [['prefix_optional_str', 'String', 'be742dbe-0053-11ea-8738-8cec4bd83f9f'],
                          ['result_any', 'Any', 'be723dbf-0053-11ea-b7e0-7jec4bd83f9f'],
                          ['In', 'Event', 'be723dc0-0053-11ea-b171-8chf4bd83f9f']],
                 "returns": []}

    def __call__(self, args, io):
        prefix = args.get('prefix_optional_str', None)
        result = args['result_any']
        if prefix:
            print(prefix, result)
        else:
            print(result)


class DataStore(Action):
    """节点中数据暂时存储"""
    _id = '9bdf5664-e967-11e9-8d60-8cec4bd887f3'
    node_info = {"args": [['data_any', 'Any', 'd887f4dc-003a-11ea-a4ba-8cec4bd83f9f'],
                          ['In', 'Event', 'ce693d31-f3a7-11e9-8654-8cec4bd887f3']],
                 "returns": [['data_any', 'Any', 'd887f4de-003a-11ea-a242-8cec4bd83f9f']]}

    def __call__(self, args, io):
        data = args['data_any']
        io.set_output('data_any', data)


class InsertToMongo(Action):
    """将数据存入Mongodb中"""
    _id = 'bbe99e18-e967-11e9-ad5f-8cec4bd887f3'
    node_info = {"args": [['url_str', 'String', 'ce693d33-f3a7-11e9-b0ce-8cec4bd887f3'],
                          ['db_str', 'String', 'ce693d34-f3a7-11e9-8965-8cec4bd887f3'],
                          ['collection_str', 'String', 'ce693d35-f3a7-11e9-a4dd-8cec4bd887f3'],
                          ['doc_dict', 'Dict', 'ce693d36-f3a7-11e9-acae-8cec4bd887f3'],
                          ['In', 'Event', 'ce693d37-f3a7-11e9-ba03-8cec4bd887f3']],
                 "returns": []}

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


class UpdateToMongo(Action):
    """将数据存入Mongodb中"""
    _id = 'c1cdbb36-e967-11e9-b968-8cec4bd887f3'
    node_info = {"args": [['url_str', 'String', 'ce693d38-f3a7-11e9-8b6c-8cec4bd887f3'],
                          ['db_str', 'String', 'ce693d39-f3a7-11e9-b1d1-8cec4bd887f3'],
                          ['collection_str', 'String', 'ce693d3a-f3a7-11e9-9e85-8cec4bd887f3'],
                          ['doc_dict', 'Dict', 'ce693d3b-f3a7-11e9-b796-8cec4bd887f3'],
                          ['query_key_str', 'String', 'ce693d3c-f3a7-11e9-b196-8cec4bd887f3'],
                          ['In', 'Event', 'ce693d3d-f3a7-11e9-8a41-8cec4bd887f3']],
                 "returns": []}

    def __call__(self, args, io):
        mongo_url = args['url_str']
        mongo_db = args['db_str']
        mongo_chart = args['collection_str']
        data = args['doc_dict']
        query_key = args['query_key_str']

        client = pymongo.MongoClient(mongo_url)
        db = client[mongo_db]
        collection = db[mongo_chart]
        if collection.update_one({query_key: data[query_key]}, {'$set': data}, upsert=True):
            print(data)
        else:
            print('Update to mongodb failed!')


class SaveJsonFile(Action):
    """数据保存为json格式文件"""
    _id = '94ff84f8-e9a4-11e9-bbe0-f416630aacec'
    node_info = {"args": [['filename_str', 'String', 'ce693d3e-f3a7-11e9-8786-8cec4bd887f3'],
                          ['doc_dict', 'Dict', 'ce693d3f-f3a7-11e9-b1d1-8cec4bd887f3'],
                          ['In', 'Event', 'ce693d40-f3a7-11e9-8e3d-8cec4bd887f3']],
                 "returns": []}

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


class AcquireCookie(Action):
    """通过pyppeteer模拟登录获取cookie"""
    _id = '74870f18-e96a-11e9-829a-8cec4bd887f3'
    node_info = {"args": [['login_url_str', 'String', '781c3e4c-4ea1-4966-8bc4-91df09507766'],
                          ['username_str', 'String', '5e62ccd5-a4d3-4b5f-9831-8f526bc4f732'],
                          ['password_str', 'String', '308d1c24-5f67-4e4c-95d9-2da77ffda93c'],
                          ['user_css_str', 'String', '027e6a7e-6e19-45e0-b111-321cb04324c2'],
                          ['password_css_str', 'String', 'c567634f-dbbc-4e39-aefd-c32cbc0f08ba'],
                          ['submit_css_str', 'String', '03dc7fb4-c55c-403e-a42c-d637cabf531f'],
                          ['In', 'Event', '936a1f18-e232-4d52-af7f-1bc27a9000a9']],
                 "returns": [['cookie_list', 'List', '033d6b64-3d26-4fc9-9a18-c87bd0808fb6'],
                             ['Out', 'Event', 'b9a15e21-e835-414c-9d33-23a2523508e9']]}

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


class FormatData(Action):
    """接收爬虫输出字典数据，转换为['name': some, 'value': other ]"""
    _id = 'af5b8e9a-ef20-11e9-9bb3-f416630aacec'
    node_info = {"args": [['doc_dict', 'Dict', 'ce693d4a-f3a7-11e9-a298-8cec4bd887f3'],
                          ['In', 'Event', 'ce693d4b-f3a7-11e9-aef3-8cec4bd887f3']],
                 "returns": [['output_str', 'String', 'ce693d4c-f3a7-11e9-ac04-8cec4bd887f3'],
                             ['Out', 'Event', 'ce693d4d-f3a7-11e9-a090-8cec4bd887f3']]}

    def __call__(self, args, io):
        doc = args['doc_dict']
        output = []
        for key, value in doc.items():
            temp = {}
            temp['name'] = key
            temp['value'] = value
            output.append(temp)

        io.set_output('output_str', json.dumps(output).replace("'", '"'))
        io.push_event('Out')


class WithOpenTxt(Action):
    """将接受的数据写入本地，Txt格式"""
    _id = '9246b900-f3a1-11e9-86df-8cec4bd887f3'
    node_info = {"args": [['data_any', 'Any', '391c4b6a-f3a8-11e9-aef8-8cec4bd887f3'],
                          ['file_name_str', 'String', '391c4b6b-f3a8-11e9-8658-8cec4bd887f3'],
                          ['write_way_str', 'String', '391c4b6c-f3a8-11e9-b5cc-8cec4bd887f3'],
                          ['encoding_str', 'String', 'b56ad691-f3a8-11e9-aa1b-8cec4bd887f3'],
                          ['In', 'Event', '391c4b6d-f3a8-11e9-aaf0-8cec4bd887f3']],
                 "returns": []}

    def __call__(self, args, io):
        data = args['data_any']
        file_name = args['file_name_str']
        write_way = args['write_way_str']
        encoding = args['encoding_str']
        with open(file_name, write_way, encoding=encoding) as fp:
            fp.write(data)


class ConnectSQLServer(Action):
    """连接SQL Server数据库"""
    _id = '07bca6b8-ff66-11e9-b668-8cec4bd83f9f'
    node_info = {"args": [['host_str', 'String', 'd8881382-003a-11ea-b9ad-8cec4bd83f9f'],
                          ['port_int', 'Int', 'd8881383-003a-11ea-96f3-8cec4bd83f9f'],
                          ['user_str', 'String', 'd8881384-003a-11ea-b245-8cec4bd83f9f'],
                          ['password_str', 'String', 'd8881385-003a-11ea-9d1d-8cec4bd83f9f'],
                          ['database_str', 'String', 'd8881386-003a-11ea-88b4-8cec4bd83f9f'],
                          ['charset_str', 'String', 'd8881387-003a-11ea-b283-8cec4bd83f9f'],
                          ['In', 'Event', 'd8881388-003a-11ea-87cd-8cec4bd83f9f']],
                 "returns": [['connect', 'Any', 'd8881389-003a-11ea-bebf-8cec4bd83f9f'],
                             ['Out', 'Event', 'd888138a-003a-11ea-9add-8cec4bd83f9f']]}

    def __call__(self, args, io):
        host = args['host_str']
        port = args['port_int']
        user = args['user_str']
        password = args['password_str']
        database = args['database_str']
        charset = args['charset_str']

        connect = pymssql.connect(host=host, port=port, user=user, password=password,
                                  database=database, charset=charset)
        io.set_output('connect', connect)
        io.push_event('Out')


class FetchSQLServerData(Action):
    """获取sql server数据"""
    _id = '15bffa1e-ff66-11e9-877e-8cec4bd83f9f'
    node_info = {"args": [['table_str', 'String', 'd888138b-003a-11ea-8d68-8cec4bd83f9f'],
                          ['field_list', 'List', 'd888138c-003a-11ea-bb95-8cec4bd83f9f'],
                          ['connect', 'Any', 'd888138d-003a-11ea-a8d1-8cec4bd83f9f'],
                          ['In', 'Event', 'd888138e-003a-11ea-9b0e-8cec4bd83f9f']],
                 "returns": [['data_list', 'List', 'd888138f-003a-11ea-9a43-8cec4bd83f9f'],
                             ['Out', 'Event', 'd8881390-003a-11ea-a3bf-8cec4bd83f9f']]}

    def __call__(self, args, io):
        table = args['table_str']
        fields = args['field_list']
        connect = args['connect']
        cursor = connect.cursor()

        out_data = []
        if fields:
            place_holder = ['%s' for i in range(len(fields))]
            place_holder = ', '.join(place_holder)
            sql = 'select ' + place_holder % tuple(fields) + ' from %s' % table

            cursor.execute(sql)
            row = cursor.fetchone()
            while row:
                temp = dict((fields[i], row[i])
                            for i in range(len(fields)))
                out_data.append(temp)
                row = cursor.fetchone()

        connect.close()
        io.set_output('data_list', out_data)
        io.push_event('Out')


class GetSQLServerData(Action):
    _id = '15bffa1e-f416-11e9-877e-8cec4bd75f9f'
    node_info = {"args": [['sql_statement', 'String', 'd8881391-003a-11ea-bd46-8cec4bd83f9f'],
                          ['connect', 'Any', 'd8881392-003a-11ea-ae94-8cec4bd83f9f'],
                          ['In', 'Event', 'd8881393-003a-11ea-a93b-8cec4bd83f9f']],
                 "returns": [['output_data', 'List', 'd8881394-003a-11ea-9372-8cec4bd83f9f'],
                             ['Out', 'Event', 'd8881395-003a-11ea-a110-8cec4bd83f9f']]}

    def __call__(self, args, io):
        sql_statement = args['sql_statement']
        connect = args['connect']
        cursor = connect.cursor()

        out_data = []
        if sql_statement:
            cursor.execute(sql_statement)
            row = cursor.fetchone()
            while row:
                out_data.append(row)
                row = cursor.fetchone()

        connect.close()
        io.set_output('output_data', out_data)
        io.push_event('Out')
