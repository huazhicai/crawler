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
    _id = '7f5ae09e-e968-11e9-9e7e-8cec4bd887f3'
    node_info = {"args": [['split_str', 'String', 'ce696492-f3a7-11e9-ab8b-8cec4bd887f3'],
                          ['key_index_str', 'String', 'ce696493-f3a7-11e9-bfba-8cec4bd887f3'],
                          ['value_index_str', 'String', 'ce696494-f3a7-11e9-9e64-8cec4bd887f3'],
                          ['doc_list', 'List', 'ce677bd3-f3a7-11e9-9100-8cec4bd887f3'],
                          ['In', 'Event', 'ce698bd4-f3a7-11e9-b27d-8abc4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce696496-f3a7-11e9-9b17-8cec4bd887f3'],
                             ['Out', 'Event', 'ce698bd6-f3a7-11e9-83e5-8cec4bd457f3']]}

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


class IteratorList(Action):
    """对列表进行遍历"""
    _id = 'dca2b823-ddb1-11e9-bd0c-8cec4bd887f3'
    node_info = {"args": [['doc_list', 'Dict', 'ce696498-f3a7-11e9-92c0-8cec4bd887f3'],
                          ['In', 'Event', 'ce696499-f3a7-11e9-90c1-8cec4bd887f3']],
                 "returns": [['item_any', 'Any', 'ad4b61c2-f4aa-11e9-9c0f-8cec4bd887f3'],
                             ['index_int', 'Int', 'be72646d-0053-11ea-a36f-8cec4bd83f9f'],
                             ['Out', 'Event', 'ce69649b-f3a7-11e9-a3e2-8cec4bd887f3']]}

    def __call__(self, args, io):
        doc = args['doc_list']
        for index, element in enumerate(doc):
            io.set_output('item_any', element)
            io.set_output('index_int', index)
            io.push_event('Out')


class TimeSleep(Action):
    """睡眠时间"""
    _id = 'adb42c92-e9a3-11e9-b650-f416630aacec'
    node_info = {"args": [['time_str', 'String', 'ce69649c-f3a7-33e9-afd6-8cec4bd887f3'],
                          ['In', 'Event', 'ce69649e-f3a7-11e9-944b-8cec4bdef7f3']],
                 "returns": [['Out', 'Event', 'ce4364a0-f3a7-11e9-b97f-8cec4bd887f3']]}

    def __call__(self, args, io):
        waiter = args['time_str']
        time.sleep(float(waiter))
        io.push_event('Out')


class IsDictValue(Action):
    """判断字典中value是否存在空值"""
    _id = 'd7c80395-e974-11e9-bbed-f416630aacec'
    node_info = {"args": [['result_dict', 'Dict', 'ce69649c-f3a7-45-afd6-8cec4bd887f3'],
                          ['key_str', 'String', 'ce69649c-f3a7-11e9-afd6-8cec4bd887f3'],
                          ['In', 'Event', 'ce69649e-f3a7-11e9-944b-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce6923a0-f3a7-11e9-b97f-8cec4bd887f3'],
                             ['Out', 'Event', 'ce6964a0-f3a7-11e9-b97f-8cec4bd887f3']]}

    def __call__(self, args, io):
        dic = args['result_dict']
        key = args['key_str']
        if dic[key]:
            io.set_output('result_dict', dic)
            io.push_event('Out')


class Sequence(Action):
    _id = 'd7c80395-e974-11e9-bbed-f416630aa111'
    node_info = {"args": [['In', 'Event', 'ce6964a6-f3a7-11e9-975a-8cec4bd887f3']],
                 "returns": [['Out1', 'Event', 'ce6964a7-f3a7-11e9-9628-8cec4bd887f3'],
                             ['Out2', 'Event', 'ce6964a8-f3a7-33e9-bcbd-8cec4bd887f3'],
                             ['Out3', 'Event', 'ce6964a8-f3a7-11e9-bcbd-8cec4bd887f3'],
                             ['Out4', 'Event', 'ce6964a9-f3a7-11e9-8e87-8cec4bd887f3']]}

    def __call__(self, args, io):
        io.push_event('Out1')
        io.push_event('Out2')
        io.push_event('Out3')
        io.push_event('Out4')


class Islist(Action):
    """列表不为空，节点继续进行"""
    _id = 'baf04774-f954-11e9-862e-8cec4bd887f3'
    node_info = {"args": [['doc_list', 'List', 'c2bfbbcb-f954-11e9-bb41-8cec4bd887f3'],
                          ['reminder_any', 'Any', '40e9a5b9-f955-11e9-a72c-8cec4bd887f3'],
                          ['In', 'Event', 'c2bfbbcc-f954-11e9-8ee0-8cec4bd887f3']],
                 "returns": [['result_list', 'List', 'c2bfbbcd-f954-11e9-8001-8cec4bd887f3'],
                             ['Out', 'Event', 'c2bfbbce-f954-11e9-9ee0-8cec4bd887f3']]}

    def __call__(self, args, io):
        doc = args['doc_list']
        if doc:
            io.set_output('result_list', doc)
            io.push_event('Out')
        else:
            """但列表为空时，节点不需要继续经行，输出提示语reminder"""
            reminder = args['reminder_any']
            print(reminder)


class ExternalArgs(Action):
    _id = 'baf04774-f854-11e9-872e-8cec4bd887f3'
    node_info = {"args": [['args_dict', 'Dict', 'd8921242-003a-11ea-a7f4-8cec4bd83f9f'],
                          ['In', 'Event', 'd8921243-003a-11ea-bb22-8cec4bd83f9f']],
                 "returns": [['output_dict', 'Dict', 'd8921244-003a-11ea-8600-8cec4bd83f9f'],
                             ['Out', 'Event', 'd8921245-003a-11ea-b06e-8cec4bd83f9f']]}

    def __call__(self, args, io):
        inputargs = args['args_dict']
        io.set_output('output_dict', inputargs)
        io.push_event('Out')


class StrContains(Action):
    _id = 'bd014538-0050-11ea-b1d5-8cec4bd83f9f'
    node_info = {"args": [['inputarg_str', 'String', 'ebf4f4a7-0050-11ea-88b0-8cec4bd83f9f'],
                          ['target_str', 'String', 'ebf4f4a8-0050-11ea-b8ed-8cec4bd83f9f'],
                          ['In', 'Event', 'ebf4f4a9-0050-11ea-bb5c-8cec4bd83f9f']],
                 "returns": [['output_bool', 'Bool', 'ebf4f4aa-0050-11ea-8a95-8cec4bd83f9f'],
                             ['Out', 'Event', 'ebf4f4ab-0050-11ea-a02a-8cec4bd83f9f']]}

    def __call__(self, args, io):
        inputarg = args['inputarg_str']
        target = args['target_str']
        io.set_output('output_bool', inputarg.find(target) != -1)
        io.push_event('Out')


class ConditionIf(Action):
    _id = 'd41dbe58-0050-11ea-85d1-8cec4bd83f9f'
    node_info = {"args": [['condition', 'Any', 'ebf4f4ac-0050-11ea-b284-8cec4bd83f9f'],
                          ['In', 'Event', 'ebf4f4ad-0050-11ea-9c50-8cec4bd83f9f']],
                 "returns": [['True', 'Event', '0ae3f38d-0054-11ea-8241-8cec4bd83f9f'],
                             ['False', 'Event', '0ae3f38e-0054-11ea-9fdc-8cec4bd83f9f']]}

    def __call__(self, args, io):
        condition = args['condition']
        if condition:

            io.push_event('Out1')
        else:
            io.push_event('Out2')
