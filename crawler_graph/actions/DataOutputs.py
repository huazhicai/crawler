#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
contact blacknepia@dingtail.com for more information
数据输出和入数据库

"""

from runtime.Action import Action
import pymongo

#将result结果打印输出
class ConsoleOutput(Action):
	def __call__(self, args, io):
		print(args['result'])


		# pass


class Mongodb(Action):


	def __call__(self, args, io):

		mongo_url = args['url']
		mongo_db  = args['db']
		mongo_chart = args['chart']
		result = args['result']

		remote_client = pymongo.MongoClient(mongo_url)
		db = remote_client[mongo_db]
		collection = db[mongo_chart]

		collection.update_one({'url_id': result['url_id']}, {'$set': result}, True)






class MongoOutput(Action):

	"""
	todo asynchronized
	"""
	def __init__(self):
		super(MongoOutput, self).__init__()
		self.mongo_client_pool = {}

	def __call__(self, args, io):
		mongo_url = args['url']
		if mongo_url not in self.mongo_client_pool:
			import pymongo
			self.mongo_client = pymongo.MongoClient(mongo_url)

		mongo_db = args['db']
		mongo_collection = args['collection']
		mongo_key = args['key']

		result = args['result']
		if '_id' not in result and mongo_key:
			result['_id'] = mongo_key

		self.mongo_client[mongo_db][mongo_collection].update_one({'_id':result['id']}, {'$set':result}, upsert=True)