#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing. 
contact blacknepia@dingtail.com for more information
流控制, 遍历列表
"""

from runtime.Action import Action
import time

"""
对列表进行遍历
"""
class IteratorList(Action):
	def __call__(self, args, io):
		for Element in args['doc_list']:
			io.set_output('item_any', Element)
			io.push_event('Out')


