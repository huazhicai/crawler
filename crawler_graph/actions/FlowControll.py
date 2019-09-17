# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing. 
contact blacknepia@dingtail.com for more information
流控制, 遍历列表
"""

from runtime.Action import Action
import time


class IteratorList(Action):
    """
    对列表进行遍历
    """
    def __call__(self, args, io):
        for element in args['doc_list']:
            io.set_output('item_any', element)
            io.push_event('Out')


class StringContcat(Action):
    """
    单个字符串拼接
    """
    def __call__(self, args, io):
        prefix = args['prefix_str']
        suffix = args['suffix_str']
        string = ''.join([prefix, suffix])
        io.set_output('contacted_str', string)
        io.push_event('Out')
