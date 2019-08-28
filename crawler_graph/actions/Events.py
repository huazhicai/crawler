#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing. 
contact blacknepia@dingtail.com for more information
传入下notes 下标和Out参数
"""

from runtime.Action import Action

#其实start 开始点
class Start(Action):
	def __call__(self, args, io):
		io.push_event('Out')

