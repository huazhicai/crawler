# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing.
contact blacknepia@dingtail.com for more information

"""

from runtime.Action import Action

"""
对数据储存
"""

class DataStore_Str(Action):
    def __call__(self, args, io):
        Data = args['Data_str']
        io.set_output('Data_str', Data)

class DataStore_List(Action):
    def __call__(self, args, io):
        Data = args['Data_List']
        io.set_output('Data_List', Data)

class DataStore_Dict(Action):
    def __call__(self, args, io):
        Data = args['Data_str']
        io.set_output('Data_str', Data)
