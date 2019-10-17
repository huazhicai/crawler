# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing.
contact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action


class Start(Action):
    id = '9ed37096-bc78-47c9-b0d0-44fef1f8002d'
    def __call__(self, args, io):
        io.push_event('Out')
