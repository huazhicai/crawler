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

    def __call__(self, args, io):
        import json
        content = args['page_source_str']
        result = json.loads(content)
        io.set_output('result_dict', result)
        io.push_event('Out')

    id = 'a1596ee2-e968-11e9-b900-8cec4bd887f3'


class ParseXapth(Action):
    """通过xpath ，获取指定字段"""

    def __call__(self, args, io):
        page_source = args['page_source_str']
        etree = html.etree
        tree = etree.HTML(page_source)
        rule = args['xpath_str']
        result_dict = tree.xpath(rule)
        io.set_output('result_list', result_dict)
        io.push_event('Out')

    id = 'a968661a-e968-11e9-8902-8cec4bd887f3'


class Parse_Xath_More(Action):
    """通过xpath ，获取多个字段"""

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

    id = 'afa2a5ac-e968-11e9-904e-8cec4bd887f3'
