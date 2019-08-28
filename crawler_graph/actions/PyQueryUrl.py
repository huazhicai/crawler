#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
from pyquery import PyQuery

class PyQueryUrl(Action):


	def __call__(self, args, io):
		url = args['Url']
		doc = PyQuery(url)

		# {'departments': ['.clearfix > li > a', True, 'href']},链接
		fields = args['Fields']

		result = {}
		# {'doctors': ['.ks_yishi > ul > li > a', True, 'href']},
		for field, (selector, is_list, attr) in fields.items():
			item = doc(selector)
			#如果是列表 多个数据
			if is_list:
				item = item.items()
				#如果是链接href
				if attr:
					result[field] = [ele.attr(attr) for ele in item]
	# print(result){'departments': ['web/ksindex/58.html', 'web/ksindex/50.h。。。。
				else:
					result[field] = [ele.text() for ele in item]
			else:
				#如果是href
				if attr:
					result[field] = item.attr(attr)
				#文本内容
				else:
					result[field] = item.text()
		#写入内存 doc为网页源代码
		io.set_output('Doc', doc)
		io.set_output('Result', result)

		io.push_event('Out')

class PyQueryFieldHelper(Action):

	def __call__(self, args, io):
		pass
