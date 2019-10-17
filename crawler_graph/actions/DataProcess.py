# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
数据简单清洗过程
"""

from runtime.Action import Action


class ReExtract(Action):
    """正则获取指定元素"""

    def __call__(self, args, io):
        import re
        obj = args['string_str']
        rule = args['re_pattern_str']
        result = re.findall(rule, obj)
        result = ''.join(result)
        io.set_output('result_str', result)
        io.push_event('Out')

    id = 'd51b409e-e967-11e9-a27a-8cec4bd887f3'


class IterationJoint(Action):
    """遍历列表，拼接字符串"""

    def __call__(self, args, io):
        prefix = args['prefix_str']
        suffix_list = args['suffix_list']
        return_type = args['return_type']
        if return_type == 'list':
            url_list = []
            for suffix in suffix_list:
                string = str(prefix) + str(suffix)
                url_list.append(string)
            io.set_output('url_list', url_list)
            io.push_event('Out1')
        else:
            for suffix in suffix_list:
                url = str(prefix) + str(suffix)
                io.set_output('url_str', url)
                io.push_event('Out2')

    id = 'dc32ecb6-e967-11e9-9dab-8cec4bd887f3'


class ListIndex(Action):
    """选取列表中直接下表元素"""

    def __call__(self, args, io):
        index = args['index_str']
        result_list = args['result_list']
        result_any = result_list[int(index)]
        io.set_output('result_any', result_any)
        io.push_event('Out')

    id = 'e4c44b9e-e967-11e9-a109-8cec4bd887f3'


class SplitString(Action):
    """ 按指定字符切割字符串并获取指定区间"""

    def __call__(self, args, io):
        string = args['response_str']
        need_split = args['split_str']
        start_index = args['start_index_str']
        end_index = args['end_index_str']

        if not end_index and start_index:
            result_split = string.split(need_split)[int(start_index):]
        elif not start_index and end_index:
            result_split = string.split(need_split)[:int(end_index)]
        elif not end_index and not start_index:
            result_split = string.split(need_split)
        else:
            result_split = string.split(need_split)[int(start_index):int(end_index)]

        io.set_output('result_list', result_split)
        io.push_event('Out')

    id = 'e9976b6c-e967-11e9-a6e4-8cec4bd887f3'


class StripString(Action):
    """删除字符串中指定元素"""

    def __call__(self, args, io):
        string = args['response_str']
        need_strip = args['strip_str']
        result_strip = string.strip(need_strip)
        io.set_output('result_str', result_strip)
        io.push_event('Out')

    id = 'f15518f0-e967-11e9-bb56-8cec4bd887f3'


class AddDict(Action):
    """ 向字典中添加键值对"""

    def __call__(self, args, io):
        key = args['key_any']
        value = args['value_any']
        dic = args['doc_dict']
        dic[key] = value
        io.set_output('result_dict', dic)
        io.push_event('Out')

    id = 'f5a77602-e967-11e9-8b5f-8cec4bd887f3'


class AddingDict(Action):
    """字典相加"""

    def __call__(self, args, io):
        dict_one = args['doc1_dict']
        dict_two = args['doc2_dict']
        new_dict = dict(dict_one.items() + dict_two.items())
        io.set_output('result_dict', new_dict)
        io.push_event('Out')

    id = 'ff705a30-e967-11e9-afb9-8cec4bd887f3'


class JointDict(Action):
    """组成字典"""

    def __call__(self, args, io):
        key = args['key_any']
        value = args['value_any']
        dic = {}
        dic[key] = value
        io.set_output('result_dict', dic)
        io.push_event('Out')

    id = '0634379c-e968-11e9-b579-8cec4bd887f3'


class MergeDict(Action):
    """两个字典合并，"""

    def __call__(self, args, io):
        dict_one = args['doc1_dict']
        for Key, Value in args['doc2_dict'].items():
            if Key not in dict_one:
                dict_one[Key] = Value
        io.set_output('result_dict', dict_one)
        io.push_event('Out')

    id = '0b4e0ad8-e968-11e9-bd14-8cec4bd887f3'


class GetValueDict(Action):
    """已知Key  从字典中获取Value"""

    def __call__(self, args, io):
        dic = args['doc_dict']
        io.set_output('value_any', dic[args['key_any']])
        io.push_event('Out')

    id = '12166c3a-e968-11e9-a718-8cec4bd887f3'


class CleaningList(Action):
    """去除字典中value[value为列表]中的 \t \n,"""

    def __call__(self, args, io):
        dic = args['doc_dict']
        for key, value in dic.items():
            value = ''.join(value)
            value = ' '.join(value.split())
            dic[key] = value
        io.set_output('result_dict', dic)
        io.push_event('Out')

    id = '91f5ecd4-e9a3-11e9-9b9e-f416630aacec'


class FillUpInfor(Action):
    """当dict中value为空时，补充信息"""

    def __call__(self, args, io):
        dic = args['doc_dict']
        for key, vule in dic.items():
            if len(vule) == 0:
                dic[key] = '信息不详'
        io.set_output('result_dict', dic)
        io.push_event('Out')

    id = '7c429c80-e9a3-11e9-962f-f416630aacec'


class InterceptionText(Action):
    """
    如果多个字段在一个标签中，用正则截取多个字段，对内容的提取
    对value中字符串进行正则匹配
    """

    def __call__(self, args, io):
        import re
        dic = args['doc1_dict']
        rule_dict = args['doc2_dict']
        for key, value in rule_dict.items():
            if key in dic.keys():
                con = re.findall(value, dic[key])
                con = ''.join(con).strip(' ')
                dic[key] = con

        io.set_output('result_dict', dic)
        io.push_event('Out')

    id = '19bd24ee-e968-11e9-b671-8cec4bd887f3'


class StringContact(Action):
    """
    单个字符串拼接
    """

    def __call__(self, args, io):
        prefix = args['prefix_str']
        suffix = args['suffix_str']
        string = ''.join([prefix, suffix])
        io.set_output('contacted_str', string)
        io.push_event('Out')

    id = '321dfffa-e968-11e9-b5c3-8cec4bd887f3'


class GetExternalVarStr(Action):

    def __call__(self, args, io):
        key = args['key_str']
        value = io.get_external_var(key)
        io.set_output('value_str', str(value))

    id = 'aa739124-289e-452d-a593-485ed88d3206'
