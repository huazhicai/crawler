# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by liqing.
contact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action


class Start(Action):
    _id = '9ed37096-bc78-47c9-b0d0-44fef1f8002d'
    node_info = {"args": [['Default', 'Event', 'be723dbe-0053-11ea-8738-8cec4bd83f9f']],
                 "returns": [['Out', 'Event', 'a9f4fe1f-00b9-413c-a332-f98ef6327465']]}

    def __call__(self, args, io):
        io.push_event('Out')
