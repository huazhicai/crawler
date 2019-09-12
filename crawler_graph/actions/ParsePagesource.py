from runtime.Action import Action
from lxml import html



class Json_loads(Action):

    def __call__(self, args, io):
        import json
        content = args['page_source_str']
        result = json.loads(content)
        io.set_output('result_str', result)
        io.push_event('Out')



"""
通过xpath ，获取多个字段
"""
class ParsePagesource(Action):
    def __call__(self, args, io):
        Page_source = args['page_source_str']
        etree = html.etree
        tree = etree.HTML(Page_source)
        Rule_dict = args['doc_dict']
        Result_dict = {}
        for key, value in Rule_dict.items():
            values = tree.xpath(value)
            values = ''.join(values)
            Result_dict[key] = ''.join(values.split())
        io.set_output('result_dict', Result_dict)
        io.push_event('Out')


"""
通过xpath ，获取指定字段
"""


class ParseUrl(Action):
    def __call__(self, args, io):
        Page_source = args['page_source_str']
        etree = html.etree
        tree = etree.HTML(Page_source)
        Rule = args['xpath_str']
        Result_dict = tree.xpath(Rule)
        io.set_output('result_list', Result_dict)
        io.push_event('Out')
