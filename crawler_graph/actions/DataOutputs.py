# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
contact blacknepia@dingtail.com for more information
数据输出和入数据库

"""

from runtime.Action import Action
import pymongo


# 将result结果打印输出
class ConsoleOutput(Action):
    def __call__(self, args, io):
        print(args['result_any'])
        pass


# 将数据存入Mongodb中
class MongoOutput(Action):
    def __call__(self, args, io):
        mongo_url = args['url_str']
        mongo_db = args['db_str']
        mongo_chart = args['collection_str']
        data = args['doc_dict']

        remote_client = pymongo.MongoClient(mongo_url)
        db = remote_client[mongo_db]
        collection = db[mongo_chart]
        collection.update_one({'url_id': data['url_id']}, {'$set': data}, True)
        pass