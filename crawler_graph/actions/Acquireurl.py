from runtime.Action import Action
import time

# 对url操作

"""
遍历列表+前缀拼接  一次遍历输出
"""


class Acquireurl(Action):
    def __call__(self, args, io):
        Suffix_list = args['suffix_list']
        Prefix = args['prefix_str']
        for Suffix in Suffix_list:
            url = str(Prefix) + str(Suffix)
            io.set_output('url_str', url)
            io.push_event('Out')


"""
遍历列表+前缀拼接  ，返回列表
"""


class Acquireurl_list(Action):
    def __call__(self, args, io):
        Suffix_list = args['suffix_list']
        Prefix = args['prefix_str']
        url_list = []
        for Suffix in Suffix_list:
            String = str(Prefix) + str(Suffix)
            url_list.append(String)
        io.set_output('url_list', url_list)
        io.push_event('Out')


"""
单个字符串拼接
"""


class StringConcat(Action):
    def __call__(self, args, io):
        Prefix = args['prefix_str']
        Suffix = args['suffix_str']
        string = Prefix + Suffix
        io.set_output('contacted_str', string)
        io.push_event('Out')


"""
通过正则 提取字符串中指定元素
"""


class Extract(Action):
    def __call__(self, args, io):
        import re
        Object = args['string_str']
        Rule = args['re_pattern_str']
        Result = re.findall(Rule, Object)
        Result = ''.join(Result)
        io.set_output('result_str', Result)
        io.push_event('Out')

