from runtime.Action import Action
from lxml import html
#页面解析内容

#提取页面多个字段
class ParsePagesource(Action):

    def __call__(self, args, io):
        page_source = args['page_source']
        etree = html.etree
        tree = etree.HTML(page_source)
        fields = args['Fields']
        result = {}
        for key , value  in fields.items():
            values = tree.xpath(value)
            values = ''.join(values)
            result[key] = ''.join(values.split())
        io.set_output('Result', result)
        io.push_event('Out')

#提取页面某个指定内容
class ParseUrl(Action):
    def __call__(self, args, io):
        page_source = args['page_source']
        etree = html.etree
        tree = etree.HTML(page_source)
        fields = args['Fields']
        urls = tree.xpath(fields)
        io.set_output('Result', urls)
        io.push_event('Out')


# #对页面  正则提取指定url
# class RuleUrl(Action):
#     def __call__(self, args, io):
#         import re
#         doc = args['result']
#         rule = args['rule']
#         print(rule)
#         # parameter = re.findall(rule,doc)
#         # parameter = ''.join(parameter)
#         # io.set_output('doc_out', parameter)
#         # io.push_event('Out')
#

#
# class ParseDate(Action):
#
#     def __call__(self, args, io):
#
#         page_source = args['page_source']
#
#         etree = html.etree
#         tree = etree.HTML(page_source)
#         fields = args['Fields']
#         xx = tree.xpath('//*[@id="scheduling"]/div[2]/table//tr[1]//text()')
#         long_tr=tree.xpath('//*[@id="scheduling"]/div[2]/table/tr')
#         long=len(long_tr)


