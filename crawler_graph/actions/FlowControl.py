# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing.
contact blacknepia@dingtail.com for more information

"""
from runtime.Action import Action
import time


class Iterator_Split_Dict(Action):
    """
    对列表进行遍历,进行指定字符切割
    后将切割元素，按照指定下标进行拼接字典
    """

    def __init__(self):
        self.dict = {}

    def __call__(self, args, io):
        need_Split = args['split_str']
        key_index_str = args['key_index_str']
        value_index_str = args['value_index_str']
        for element in args['doc_list']:
            Split_after_list = element.split(need_Split)
            self.dict[Split_after_list[int(key_index_str)]] = Split_after_list[int(value_index_str)]
        io.set_output('result_dict', self.dict)
        io.push_event('Out')

    id = '7f5ae09e-e968-11e9-9e7e-8cec4bd887f3'


class IteratorList(Action):
    """
    对列表进行遍历
    """

    def __call__(self, args, io):
        doc = args['doc_list']
        for element in doc:
            io.set_output('item_any', element)
            io.push_event('Out')

    id = 'dca2b823-ddb1-11e9-bd0c-8cec4bd887f3'


class TimeSleep(Action):
    """睡眠时间"""

    def __call__(self, args, io):
        waiter = args['time_str']
        data_in = args['doc_any']
        time.sleep(int(waiter))
        io.set_output('doc_any', data_in)
        io.push_event('Out')

    id = 'adb42c92-e9a3-11e9-b650-f416630aacec'


class IsDictValue(Action):
    """判断字典中value是否存在空值"""

    def __call__(self, args, io):
        dic = args['result_dict']
        key = args['key_str']
        if dic[key]:
            io.set_output('result_dict', dic)
            io.push_event('Out')

    id = 'd7c80395-e974-11e9-bbed-f416630aacec'


class Sequence(Action):

    def __call__(self, args, io):
        io.push_event('Out1')
        io.push_event('Out2')
        io.push_event('Out3')
        io.push_event('Out4')

    id = 'd7c80395-e974-11e9-bbed-f416630aa111'
