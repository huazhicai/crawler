#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing. 
contact blacknepia@dingtail.com for more information
流控制, 遍历列表
"""

from runtime.Action import Action
import time

#遍历列表获取每一个元素
class IteratorList(Action):
	def __call__(self, args, io):
		for doc in args['doc_in']:
			io.set_output('doc_out', doc)
			io.push_event('Out')

