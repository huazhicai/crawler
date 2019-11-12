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
    _id = 'd51b409e-e967-11e9-a27a-8cec4bd887f3'
    node_info = {"args": [['string_str', 'String', 'ce693d4e-f3a7-11e9-8adf-8cec4bd887f3'],
                          ['re_pattern_str', 'String', 'ce693d4f-f3a7-11e9-823e-8cec4bd887f3']],
                 "returns": [['result_str', 'String', 'ce693d51-f3a7-11e9-bfbe-8cec4bd887f3'],
                             ['Out', 'Event', 'ce693d52-f3a7-11e9-98f4-8cec4bd887f3']]}

    def __call__(self, args, io):
        import re
        obj = args['string_str']
        rule = args['re_pattern_str']
        result = re.findall(rule, obj)
        result = ''.join(result)
        io.set_output('result_str', result)
        io.push_event('Out')


class IterationJoint(Action):
    """遍历列表，拼接字符串"""
    _id = 'dc32ecb6-e967-11e9-9dab-8cec4bd887f3'
    node_info = {"args": [['prefix_str', 'String', 'ce693d53-f3a7-11e9-9801-8cec4bd887f3'],
                          ['suffix_list', 'List', 'ce693d54-f3a7-11e9-a29c-8cec4bd887f3'],
                          ['return_type', 'Any', 'ce693d55-f3a7-11e9-bf99-8cec4bd887f3'],
                          ['In', 'Event', 'ce693d56-f3a7-11e9-a80a-8cec4bd887f3']],
                 "returns": [['url_list', 'List', '285744b9-4f47-498b-873e-993df96884ba'],
                             ['Out1', 'Event', 'ce693d58-f3a7-11e9-bb19-8cec4bd887f3'],
                             ['url_str', 'String', 'ce693d59-f3a7-11e9-beac-8cec4bd887f3'],
                             ['Out2', 'Event', 'ce693d5a-f3a7-11e9-ac0e-8cec4bd887f3']
                             ]}

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


class ListIndex(Action):
    """选取列表中直接下表元素"""
    _id = 'e4c44b9e-e967-11e9-a109-8cec4bd887f3'
    node_info = {"args": [['index_str', 'String', '6985298c-0044-11ea-9ed2-8cec4bd83f9f'],
                          ['result_list', 'List', '8dc0bec6-0044-11ea-bd92-3cec4bd83f9f'],
                          ['In', 'Event', '964b1f74-0044-11ea-82c1-8cec4bd83f9f']],
                 "returns": [['result_any', 'Any', 'cdb030da-0344-11ea-94db-8cec4bd83f9f'],
                             ['Out', 'Event', 'dde6516e-0044-11ea-9ccb-8cec4bd83f9f']]}

    def __call__(self, args, io):
        index = args['index_str']
        result_list = args['result_list']
        result_any = result_list[int(index)]
        io.set_output('result_any', result_any)
        io.push_event('Out')


class SplitString(Action):
    """ 按指定字符切割字符串并获取指定区间"""
    _id = 'e9976b6c-e967-11e9-a6e4-8cec4bd887f3'
    node_info = {"args": [['response', 'String', 'fbfedc78-acd1-4eca-a15d-693a1155773b'],
                          ['split_str', 'String', 'f7158ba3-ff3c-4ee8-9b88-b5bbd55aa482'],
                          ['start_index', 'String', 'edbba0cb-58b5-4f27-8eab-d68d483436fb'],
                          ['end_index', 'String', '7327158d-f95b-4c48-8605-f2f4e07e4099'],
                          ['In', 'Event', '9b0964dd-aa2c-4fbd-b9bf-68ab726ef2f1']],
                 "returns": [['result', 'List', '65ffbf96-70c6-4cfc-9b16-66c6104de43d'],
                             ['Out', 'Event', '7e3a00d9-70eb-481e-b725-cbd8cc12d161']]}

    def __call__(self, args, io):
        string = args['response']
        need_split = args['split']
        start_index = args['start_index']
        end_index = args['end_index']

        if not end_index and start_index:
            result_split = string.split(need_split)[int(start_index):]
        elif not start_index and end_index:
            result_split = string.split(need_split)[:int(end_index)]
        elif not end_index and not start_index:
            result_split = string.split(need_split)
        else:
            result_split = string.split(need_split)[int(start_index):int(end_index)]

        io.set_output('result', result_split)
        io.push_event('Out')


class StripString(Action):
    """删除字符串中指定元素"""
    _id = 'f15518f0-e967-11e9-bb56-8cec4bd887f3'
    node_info = {"args": [['response_str', 'String', 'ce693d67-f3a7-11e9-ad41-8cec4bd887f3'],
                          ['strip_str', 'String', 'ce693d68-f3a7-11e9-89d7-8cec4bd887f3'],
                          ['In', 'Event', 'ce693d69-f3a7-11e9-a7a2-8cec4bd887f3']],
                 "returns": [['result_str', 'String', 'ce693d6a-f3a7-11e9-b25c-8cec4bd887f3'],
                             ['Out', 'Event', 'ce693d6b-f3a7-11e9-8fa5-8cec4bd887f3']]}

    def __call__(self, args, io):
        string = args['response_str']
        need_strip = args['strip_str']
        result_strip = string.strip(need_strip)
        io.set_output('result_str', result_strip)
        io.push_event('Out')


class AddDict(Action):
    """ 向字典中添加键值对"""
    _id = 'f5a77602-e967-11e9-8b5f-8cec4bd887f3'
    node_info = {"args": [['key', 'Any', '6987297c-0044-11ea-9ed2-8cec4bd83f9f'],
                          ['value', 'Any', '8dc0bec6-0044-11ea-bd92-8cec4b283f9f'],
                          ['doc', 'Dict', 'bc7e59f6-0044-11ea-a1ee-8cec4bd83f9f'],
                          ['In', 'Event', 'ce693d6f-f3a7-11e9-99fa-8cec4bd887f3']],
                 "returns": [['result', 'Dict', 'cdb030da-0044-11ea-94db-8cec4bd83f9f'],
                             ['Out', 'Event', 'dde6c16e-0044-11ea-9ccb-8cec4bd83f9f']]}

    def __call__(self, args, io):
        key = args['key']
        value = args['value']
        dic = args['doc']
        dic[key] = value
        io.set_output('result', dic)
        io.push_event('Out')


class AddingDict(Action):
    """字典相加"""
    _id = 'ff705a30-e967-11e9-afb9-8cec4bd887f3'
    node_info = {"args": [['doc1', 'Dict', 'd70845d0-ffa7-11e9-8494-42a5ef45c2c9'
                                           ''],
                          ['doc2', 'Dict', 'f94fccec-ffa7-11e9-b356-42a6kf45c2c9'],
                          ['In', 'Event', 'ce693d74-f3a7-11e9-a4ce-8cec4bd887f3']],
                 "returns": [['result', 'Dict', 'f94fccec-ffa7-11e9-b356-42a5ef45c2c9'],
                             ['Out', 'Event', '6c13347e-ffc4-11e9-bece-42a5ef45c2c9']]}

    def __call__(self, args, io):
        dict_one = args['doc1']
        dict_two = args['doc2']
        new_dict = {**dict_one, **dict_two}
        io.set_output('result', new_dict)
        io.push_event('Out')


class JointDict(Action):
    """组成字典"""
    _id = '0634379c-e968-11e9-b579-8cec4bd887f3'
    node_info = {"args": [['key_any', 'Any', 'ce696462-f3a7-11e9-b0a7-8cec4bd887f3'],
                          ['value_any', 'Any', 'ce696463-f3a7-11e9-9f33-8cec4bd887f3'],
                          ['In', 'Event', 'ce696464-f3a7-11e9-a613-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce696465-f3a7-11e9-b7e5-8cec4bd887f3'],
                             ['Out', 'Event', 'ce696466-f3a7-11e9-ac5e-8cec4bd887f3']]}

    def __call__(self, args, io):
        key = args['key_any']
        value = args['value_any']
        dic = {}
        dic[key] = value
        io.set_output('result_dict', dic)
        io.push_event('Out')


class MergeDict(Action):
    """两个字典合并，"""
    _id = '0b4e0ad8-e968-11e9-bd14-8cec4bd887f3'
    node_info = {"args": [['doc1_dict', 'Dict', 'ce696467-f3a7-11e9-a604-8cec4bd887f3'],
                          ['doc2_dict', 'Dict', 'ea0589cb-9fa9-4b5a-b6e7-df3b3afdbbb1'],
                          ['In', 'Event', 'ce696468-f3a7-11e9-932e-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce696469-f3a7-11e9-82cb-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69646a-f3a7-11e9-8e30-8cec4bd887f3']]}

    def __call__(self, args, io):
        dict_one = args['doc1_dict']
        for Key, Value in args['doc2_dict'].items():
            if Key not in dict_one:
                dict_one[Key] = Value
        io.set_output('result_dict', dict_one)
        io.push_event('Out')


class GetValueDict(Action):
    """已知Key  从字典中获取Value"""
    _id = '12166c3a-e968-11e9-a718-8cec4bd887f3'
    node_info = {"args": [['doc_dict', 'Dict', 'ce69646b-f3a7-11e9-bb86-8cec4bd887f3'],
                          ['In', 'Event', 'ce69646c-f3a7-11e9-9703-8cec4bd887f3']],
                 "returns": [['value_any', 'Any', 'ce69646d-f3a7-11e9-906e-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69646e-f3a7-11e9-b7b0-8cec4bd887f3']]}

    def __call__(self, args, io):
        dic = args['doc_dict']
        io.set_output('value_any', dic[args['key_any']])
        io.push_event('Out')


class CleaningList(Action):
    """去除字典中value[value为列表]中的 \t \n,"""
    _id = '91f5ecd4-e9a3-11e9-9b9e-f416630aacec'
    node_info = {"args": [['doc_dict', 'Dict', 'ce69646f-f3a7-11e9-8b6d-8cec4bd887f3'],
                          ['In', 'Event', 'ce696470-f3a7-11e9-8f29-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce696471-f3a7-11e9-a107-8cec4bd887f3'],
                             ['Out', 'Event', 'ce696472-f3a7-11e9-a81c-8cec4bd887f3']]}

    def __call__(self, args, io):
        dic = args['doc_dict']
        for key, value in dic.items():
            value = ''.join(value)
            value = ' '.join(value.split())
            dic[key] = value
        io.set_output('result_dict', dic)
        io.push_event('Out')


class FillUpInfor(Action):
    """当dict中value为空时，补充信息"""
    _id = '7c429c80-e9a3-11e9-962f-f416630aacec'
    node_info = {"args": [['doc_dict', 'Dict', 'ce696473-f3a7-11e9-ae32-8cec4bd887f3'],
                          ['In', 'Event', 'ce696474-f3a7-11e9-b0b9-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce696475-f3a7-11e9-9eea-8cec4bd887f3'],
                             ['Out', 'Event', 'ce696476-f3a7-11e9-ac67-8cec4bd887f3']]}

    def __call__(self, args, io):
        dic = args['doc_dict']
        for key, vule in dic.items():
            if len(vule) == 0:
                dic[key] = '信息不详'
        io.set_output('result_dict', dic)
        io.push_event('Out')


class InterceptionText(Action):
    """
    如果多个字段在一个标签中，用正则截取多个字段，对内容的提取
    对value中字符串进行正则匹配
    """
    _id = '19bd24ee-e968-11e9-b671-8cec4bd887f3'
    node_info = {"args": [['doc1_dict', 'Dict', 'ce696477-f3a7-11e9-96f6-8cec4bd887f3'],
                          ['doc2_dict', 'Dict', 'ce696478-f3a7-11e9-ba2d-8cec4bd887f3'],
                          ['In', 'Event', 'ce696479-f3a7-11e9-95c0-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce69647a-f3a7-11e9-ade2-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69647b-f3a7-11e9-9ce6-8cec4bd887f3']]}

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


class StringContact(Action):
    _id = '321dfffa-e968-11e9-b5c3-8cec4bd887f3'
    node_info = {"args": [['prefix_str', 'String', 'ce69647c-f3a7-11e9-a691-8cec4bd887f3'],
                          ['suffix_str', 'String', 'ce69647d-f3a7-11e9-9c70-8cec4bd887f3'],
                          ['In', 'Event', 'ce69647e-f3a7-11e9-bc2f-8cec4bd887f3']],
                 "returns": [['contacted_str', 'String', 'ce69647f-f3a7-11e9-b1e6-8cec4bd887f3'],
                             ['Out', 'Event', 'ce696480-f3a7-11e9-b813-8cec4bd887f3']]}

    def __call__(self, args, io):
        prefix = args['prefix_str']
        suffix = args['suffix_str']
        string = ''.join([prefix, suffix])
        io.set_output('contacted_str', string)
        io.push_event('Out')


class GetExternalVarStr(Action):
    _id = 'aa739124-289e-452d-a593-485ed88d3206'
    node_info = {"args": [['key_str', 'String', 'e1e73e20-ee99-4a04-b72f-1ae6f62ad6b8'],
                          ['In', 'Event', 'c6d71d22-e008-4621-a455-5516ab2a5c4d']],
                 "returns": [['value_str', 'String', 'b90006b6-f97a-49d7-8259-98b2f09bde2f'],
                             ['Out', 'Event', '487e82e2-4b07-4b94-b0d4-f7bd5c5da42c']]}

    def __call__(self, args, io):
        key = args['key_str']
        value = io.get_external_var(key)
        io.set_output('value_str', str(value))


class CumulativeDcit(Action):
    """字典的累加"""
    _id = '8232d950-f4aa-11e9-83ab-8cec4bd887f3'
    node_info = {"args": [['doc_dict', 'Dict', 'a30a9d5c-f4aa-11e9-956e-8cec4bd887f3'],
                          ['url_str', 'String', '56833196-f4ad-11e9-87ce-8cec4bd887f3'],
                          ['distinguish_str', 'String', '6af7f3f5-f5f8-11e9-abe5-8cec4bd887f3'],
                          ['In', 'Event', 'a30a9d5d-f4aa-11e9-a1f2-8cec4bd887f3']],
                 "returns": [['dict_new', 'Dict', 'a30a9d5e-f4aa-11e9-afd5-8cec4bd887f3'],
                             ['Out', 'Event', 'a30a9d5f-f4aa-11e9-8c68-8cec4bd887f3']]}

    dict_all = {}

    def __call__(self, args, io):
        dict_one = args['doc_dict']
        url = args['url_str']
        self.dict_all = {**dict_one, **self.dict_all}
        distinguish_param = args['distinguish_str']
        if distinguish_param in url:
            """当url为最后一个时候，字典累加完成，节点向后输出"""
            io.set_output('dict_new', self.dict_all)
            io.push_event('Out')


class AddingList(Action):
    """列表相加"""
    _id = '04966ce4-fbc0-11e9-b67d-8cec4bd887f3'
    node_info = {"args": [['doc1_list', 'List', 'ebf269b0-0050-11ea-b2e3-8cec4bd83f9f'],
                          ['doc2_list', 'List', 'ebf269b1-0050-11ea-a615-8cec4bd83f9f'],
                          ['In', 'Event', 'ebf269b2-0050-11ea-9fd6-8cec4bd83f9f']],
                 "returns": [['result_list', 'List', 'ebf269b3-0050-11ea-a06d-8cec4bd83f9f'],
                             ['Out', 'Event', 'ebf269b4-0050-11ea-b010-8cec4bd83f9f']]}

    def __call__(self, args, io):
        list_one = args['doc1_list']
        list_two = args['doc2_list']
        new_list = list_one + list_two
        io.set_output('result_list', new_list)
        io.push_event('Out')


class ListFetch(Action):
    _id = '04966ce4-fbc0-11e9-b67d-8cec4bd00000'
    node_info = {"args": [['input_list', 'List', 'be723dbe-0053-11ea-8738-8cec43383f9f'],
                          ['index_int', 'Int', 'be723dbf-0053-11ea-b7e0-8cec4bd83f9f'],
                          ['In', 'Event', 'be723dc0-0053-22ea-b171-8cec4bd83f9f']],
                 "returns": [['result_any', 'Any', 'be723dc1-0053-11ea-96d4-8cec4bd83f9f'],
                             ['Out', 'Event', 'be723dc2-0053-11ea-835b-8cec4bd83f9f']]}

    def __call__(self, args, io):
        list_in = args['input_list']
        index = args['index_int']
        io.set_output('result_any', list_in[index])
        io.push_event('Out')


class StrListJoin(Action):
    _id = '61c891f1-55df-4d31-8d49-de18489a0413'
    node_info = {"args": [['prefix_str', 'String', 'fc168ab4-0073-11ea-bedc-8cec4bd83f9f'],
                          ['input_list', 'List', 'fc168ab5-0073-11ea-8314-8cec4bd83f9f'],
                          ['div_str', 'String', 'fc168ab6-0073-11ea-9da5-8cec4bd83f9f'],
                          ['subfix_str', 'String', 'fc168ab7-0073-11ea-a467-8cec4bd83f9f'],
                          ['In', 'Event', 'fc168ab8-0073-11ea-ac91-8cec4bd83f9f']],
                 "returns": [['string_out', 'Any', 'fc168ab9-0073-11ea-9a32-8cec4bd83f9f'],
                             ['Out', 'Event', 'fc168aba-0073-11ea-9bad-8cec4bd83f9f']]}

    def __call__(self, args, io):
        prefix = args['prefix_str'] or ''
        list_in = args['input_list']
        div_char = args['div_str'] or ''
        subfix = args['subfix_str'] or ''

        io.set_output('string_out', prefix + div_char.join(list_in) + subfix)
        io.push_event('Out')
