from runtime.Action import Action
from lxml.html import etree


# class Json_loads(Action):
#     def __call__(self, args, io):
#         import json
#         content = args['page_source_str']
#         result = json.loads(content)
#         io.set_output('result_str', result)
#         io.push_event('Out')


# class ParsePageSource(Action):
#     """
#     解析网页源码，返回字符文档html
#     """
#
#     def __call__(self, args, io):
#         page_source = args['page_source_str']
#         html = etree.HTML(page_source)
#         io.set_output('doc_str', html)
#         io.push_event('Out')


class ExtractSingleField(Action):
    """
    通过xpath ，提取一个字段数据,
    如果一个字段多个数据，返回列表，否则返回一个数据字符
    """

    def __call__(self, args, io):
        page_source = args['page_source_str']
        rule = args['xpath_str']
        if not isinstance(page_source, etree._Element):
            page_source = etree.HTML(page_source)
        result = page_source.xpath(rule)
        io.set_output('result_list', result)
        io.push_event('Out')


class ExtractMultiFields(Action):
    """通过xpath ，提取多个字段数据"""

    def __call__(self, args, io):
        page_source = args['page_source_str']
        rule_dict = args['fields_xpath_dict']
        if not isinstance(page_source, etree._Element):
            page_source = etree.HTML(page_source)
        result_dict = {}
        for key, value in rule_dict.items():
            values = page_source.xpath(value)
            values = ''.join(values)
            result_dict[key] = ''.join(values.split())
        io.set_output('result_dict', result_dict)
        io.push_event('Out')
