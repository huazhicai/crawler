# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing.
contact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action


class Start(Action):
    id = '53116498-e968-11e9-b251-8cec4bd887f3'
    def __call__(self, args, io):
        io.push_event('Out')
