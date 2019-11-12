# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""
from runtime.Action import Action
from lxml import html


class JsonLoads(Action):
    """将json格式转化为python字符"""
    _id = 'a1596ee2-e968-11e9-b900-8cec4bd887f3'
    node_info = {"args": [['page_source_str', 'String', 'ce698beb-f3a7-11e9-9d04-8cec4bd887f3'],
                          ['In', 'Event', 'ce698bec-f3a7-11e9-9cec-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce698bed-f3a7-11e9-8057-8cec4bd887f3'],
                             ['Out', 'Event', 'ce698bee-f3a7-11e9-b427-8cec4bd887f3']]}

    def __call__(self, args, io):
        import json
        content = args['page_source_str']
        result = json.loads(content)
        io.set_output('result_dict', result)
        io.push_event('Out')


class ParseXapth(Action):
    """通过xpath ，获取指定字段"""
    _id = 'a968661a-e968-11e9-8902-8cec4bd887f3'
    node_info = {"args": [['page_source_str', 'String', 'ce698bef-f3a7-11e9-bee6-8cec4bd887f3'],
                          ['xpath_str', 'String', 'ce698bf0-f3a7-11e9-99bf-8cec4bd887f3'],
                          ['In', 'Event', 'ce698bf1-f3a7-11e9-90b3-8cec4bd887f3']],
                 "returns": [['result_list', 'List', 'ce698bf2-f3a7-11e9-9430-8cec4bd887f3'],
                             ['Out', 'Event', 'ce698bf3-f3a7-11e9-9c15-8cec4bd887f3']]}

    def __call__(self, args, io):
        page_source = args['page_source_str']
        etree = html.etree
        tree = etree.HTML(page_source)
        rule = args['xpath_str']
        result_dict = tree.xpath(rule)
        io.set_output('result_list', result_dict)
        io.push_event('Out')


class Parse_Xath_More(Action):
    """通过xpath ，获取多个字段"""
    _id = 'afa2a5ac-e968-11e9-904e-8cec4bd887f3'
    node_info = {"args": [['page_source_str', 'String', 'ce698bf4-f3a7-11e9-a142-8cec4bd887f3'],
                          ['doc_dict', 'Dict', 'ce69b234-f3a7-11e9-8d36-8cec4bd887f3'],
                          ['In', 'Event', 'ce69b235-f3a7-11e9-bd85-8cec4bd887f3']],
                 "returns": [['result_dict', 'Dict', 'ce69b236-f3a7-11e9-9743-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b237-f3a7-11e9-84d1-8cec4bd887f3']]}

    def __call__(self, args, io):
        page_source = args['page_source_str']
        etree = html.etree
        tree = etree.HTML(page_source)
        rule_dict = args['doc_dict']
        result_dict = {}
        for key, value in rule_dict.items():
            values = tree.xpath(value)
            values = ''.join(values)
            result_dict[key] = ''.join(values.split())
        io.set_output('result_dict', result_dict)
        io.push_event('Out')
