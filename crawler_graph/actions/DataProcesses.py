#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
数据简单清洗过程

"""

from runtime.Action import Action

#向字典中添加键值对
class AddDict(Action):
	def __call__(self, args, io):

		Key = args['key']
		Value = args['value']
		doc = args['doc']
		doc[Key] = Value
		io.set_output('doc_out', doc)
		io.push_event('Out')



#字典相加
class AddingDict(Action):
	def __call__(self, args, io):
		dict1 = args['dict1']
		dict2 = args['dict2']


		dictMerged1 = dict(dict1.items() + dict2.items())
		io.set_output('doc_out', dictMerged1)
		io.push_event('Out')



#组成字典
class JointDict(Action):
	def __call__(self, args, io):
		Key = args['key']
		Value = args['value']
		dict_url ={}
		dict_url[Key] = Value
		print(dict_url)
		io.set_output('doc_out', dict_url)
		io.push_event('Out')



"""
在原有字典中，添加键值对
"""
class FieldMakeup(Action):

	def __call__(self, args, io):
		doc = args['doc_in']
		for field, value in args['fields'].items():
			if field not in doc:
				doc[field] = value
		io.set_output('doc_out', doc)
		io.push_event('Out')

"""
将字典中的字典取出，返回字典中字典中的value
"""
class ContainerGetItem(Action):
	def __call__(self, args, io):
		doc = args['doc_in']
		io.set_output('doc_out', doc[args['field']])
		io.push_event('Out')

"""
去除字典中value中的  \t \n,将value中list转变str
"""
class OperationList(Action):
	def __call__(self, args, io):
		doc = args['result']
		for key, vule in doc.items():
			vule =''.join(vule)
			vule = ' '.join(vule.split())
			doc[key] = vule
		io.set_output('doc_out', doc)
		io.push_event('Out')


"""
当dict中value为空时，补充信息
"""
class FillupInfor(Action):
	def __call__(self, args, io):
		doc = args['result']
		for key, vule in doc.items():
			if len(vule) == 0 :
				doc[key] = '信息不详'
		io.set_output('doc_out', doc)
		io.push_event('Out')



"""
如果多个字段在一个标签中，用正则截取多个字段，对内容的提取
"""
class InterceptionText(Action):
	def __call__(self, args,io):
		import re
		doc = args['result']
		rule = args['rule']


		for key ,value in rule.items():
			if key in doc.keys():
				con = re.findall(value,doc[key])
				con = ''.join(con).strip(' ')
				doc[key] = con

		io.set_output('doc_out', doc)
		io.push_event('Out')

