# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
数据简单清洗过程

"""

from runtime.Action import Action


# 向字典中添加键值对
class AddDict(Action):
    def __call__(self, args, io):
        Key = args['key_any']
        Value = args['value_any']
        Dict = args['doc_dict']
        Dict[Key] = Value
        io.set_output('result_dict', Dict)
        io.push_event('Out')


# 字典相加
class AddingDict(Action):
    def __call__(self, args, io):
        Dict_one = args['doc1_dict']
        Dict_two = args['doc2_dict']

        New_dict = dict(Dict_one.items() + Dict_two.items())
        io.set_output('result_dict', New_dict)
        io.push_event('Out')


# 组成字典
class JointDict(Action):
    def __call__(self, args, io):
        Key = args['key_any']
        Value = args['value_any']
        Dict = {}
        Dict[Key] = Value

        io.set_output('result_dict', Dict)
        io.push_event('Out')


"""
两个字典合并，
"""
class FieldMakeup(Action):
    def __call__(self, args, io):
        Dict_one = args['doc1_dict']
        for Key, Value in args['doc2_dict'].items():
            if Key not in Dict_one:
                Dict_one[Key] = Value
        io.set_output('result_dict', Dict_one)
        io.push_event('Out')


"""
已知Key  从字典中获取Value
"""
class ContainerGetItem(Action):
    def __call__(self, args, io):
        Dict = args['doc_dict']
        io.set_output('value_any', Dict[args['key_any']])
        io.push_event('Out')


"""
去除字典中value中的  \t \n,将value中list转变str
"""
class OperationList(Action):
    def __call__(self, args, io):
        Dict = args['doc_dict']
        for key, vule in Dict.items():
            vule = ''.join(vule)
            vule = ' '.join(vule.split())
            Dict[key] = vule
        io.set_output('result_dict', Dict)
        io.push_event('Out')


"""
当dict中value为空时，补充信息
"""
class FillupInfor(Action):
    def __call__(self, args, io):
        Dict = args['doc_dict']
        for key, vule in Dict.items():
            if len(vule) == 0:
                Dict[key] = '信息不详'
        io.set_output('result_dict', Dict)
        io.push_event('Out')


"""
如果多个字段在一个标签中，用正则截取多个字段，对内容的提取
对value中字符串进行正则匹配
"""
class InterceptionText(Action):
    def __call__(self, args, io):
        import re
        Dict = args['doc1_dict']
        Rule_dict = args['doc2_dict']
        for key, value in Rule_dict.items():
            if key in Dict.keys():
                con = re.findall(value, Dict[key])
                con = ''.join(con).strip(' ')
                Dict[key] = con

        io.set_output('result_dict', Dict)
        io.push_event('Out')
