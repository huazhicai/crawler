from runtime.Action import Action
import time
#对url操作

"""
遍历列表+前缀拼接  一次遍历输出
"""
class Acquireurl(Action):

    def __call__(self, args, io):
        Num = args['Num']
        Prefix = args['Prefix']
        for num in Num:
            url = str(Prefix) + str(num)
            io.set_output('Url', url)
            io.push_event('Out')


class Acquireurl_list(Action):

    def __call__(self, args, io):
        Num = args['Num']
        Prefix = args['Prefix']
        url_list=[]
        for num in Num:
            url = str(Prefix) + str(num)
            url_list.append(url)
        io.set_output('Url', url_list)
        io.push_event('Out')
"""
单个字符串拼接
"""
class StringConcat(Action):
    def __call__(self, args, io):
        prefix = args['prefix']
        suffix = args['suffix']
        url = prefix + suffix
        io.set_output('doc_out', url)
        io.push_event('Out')
"""
通过正则 提取字符串中指定元素
"""
class Extract(Action):
    def __call__(self, args, io):
        import re
        doc = args['result']
        rule = args['rule']
        parameter = re.findall(rule,doc)
        parameter = ''.join(parameter)
        io.set_output('doc_out', parameter)
        io.push_event('Out')
