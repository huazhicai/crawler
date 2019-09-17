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

class ConsoleOutput(Action):
    def __call__(self, args, io):
        prefix = args.get('prefix_optional_str', None)
        result = args['result_any']
        if prefix:
            print(prefix, result)
        else:
            print(result)
        pass


class MongoOutput(Action):
    # 将数据存入Mongodb中
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




# class DataStore_Str(Action):
    """
    对数据储存
    """
#     def __call__(self, args, io):
#         Data = args['Data_str']
#         io.set_output('Data_str', Data)
#
# class DataStore_List(Action):
#     def __call__(self, args, io):
#         Data = args['Data_List']
#         io.set_output('Data_List', Data)
#
# class DataStore_Dict(Action):
#     def __call__(self, args, io):
#         Data = args['Data_str']
#         io.set_output('Data_str', Data)
