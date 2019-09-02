from runtime.Action import Action
from lxml import html
#页面解析内容

"""
通过xpath ，获取多个字段
"""
class ParsePagesource(Action):

    def __call__(self, args, io):
        page_source = args['page_source']
        etree = html.etree
        tree = etree.HTML(page_source)
        fields = args['xpath']
        result = {}
        for key , value  in fields.items():
            values = tree.xpath(value)
            values = ''.join(values)
            result[key] = ''.join(values.split())
        io.set_output('Result', result)
        io.push_event('Out')
"""
通过xpath ，获取指定字段
"""
class ParseUrl(Action):
    def __call__(self, args, io):
        page_source = args['page_source']
        etree = html.etree
        tree = etree.HTML(page_source)
        fields = args['Fields']
        urls = tree.xpath(fields)
        io.set_output('Result', urls)
        io.push_event('Out')


