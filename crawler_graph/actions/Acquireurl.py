from runtime.Action import Action
import time
#对url操作

#  拼接多个url
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

# 单个url拼接
class StringConcat(Action):
    def __call__(self, args, io):
        prefix = args['prefix']
        suffix = args['suffix']
        url = prefix + suffix

        io.set_output('doc_out', url)
        io.push_event('Out')

#提取url中有效参数
class Extract(Action):
    def __call__(self, args, io):
        import re
        doc = args['result']
        rule = args['rule']
        parameter = re.findall(rule,doc)
        parameter = ''.join(parameter)
        io.set_output('doc_out', parameter)
        io.push_event('Out')
