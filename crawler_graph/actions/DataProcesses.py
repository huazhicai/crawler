#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
数据简单清洗过程

"""

from runtime.Action import Action




#添加多余字段
class FieldMakeup(Action):

	def __call__(self, args, io):
		doc = args['doc_in']
		for field, value in args['fields'].items():
			if field not in doc:
				doc[field] = value
		io.set_output('doc_out', doc)
		io.push_event('Out')

#将字典中链接列表提取 用于多个url时候
class ContainerGetItem(Action):
	def __call__(self, args, io):
		doc = args['doc_in']
# doc   为{'departments': ['web/ksindex/58.html', 'web/ksindex/50.html', 'web/ksindex
		io.set_output('doc_out', doc[args['field']])
		io.push_event('Out')

#去除字典中value中的\xao \t \n,将字典中list转变str
class OperationList(Action):
	def __call__(self, args, io):
		doc = args['result']
		for key, vule in doc.items():
			vule =''.join(vule)
			vule = ' '.join(vule.split())
			doc[key] = vule
		io.set_output('doc_out', doc)
		io.push_event('Out')

#当信息为空时填补信息
class FillupInfor(Action):
	def __call__(self, args, io):
		doc = args['result']
		for key, vule in doc.items():
			if len(vule) == 0 :
				doc[key] = '信息不详'
		io.set_output('doc_out', doc)
		io.push_event('Out')


#如果多个字段在一个标签中，用正则截取想要的字段，对内容的提取
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

