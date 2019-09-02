# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
"""
# import json
# import sys
# import os
import pprint

graph_config = {'nodes': [{'event_actions': {'Default': 'Start'},
            'event_links': {'Out': {1: 'In'}},
            'inputs': {},
            'outputs': {}},
           {'event_actions': {'In': 'RequestUrl'},
            'event_links': {'Out': {2: 'In'}},
            'inputs': {'Url': 7},
            'outputs': {'Doc': 0}},
           {'event_actions': {'In': 'ParseUrl'},
            'event_links': {'Out': {3: 'In'}},
            'inputs': {'Fields': 8, 'page_source': 0},
            'outputs': {'Result': 1}},
           {'event_actions': {'In': 'IteratorList'},
            'event_links': {'Out': {4: 'In'}},
            'inputs': {'doc_in': 1},
            'outputs': {'doc_out': 2}},
           {'event_actions': {'In': 'StringConcat'},
            'event_links': {'Out': {5: 'In'}},
            'inputs': {'prefix': 9, 'suffix': 2},
            'outputs': {'doc_out': 3}},
           {'event_actions': {'In': 'RequestUrl'},
            'event_links': {'Out': {6: 'In'}},
            'inputs': {'Url': 3},
            'outputs': {'Doc': 4}},
           {'event_actions': {'In': 'ParsePagesource'},
            'event_links': {'Out': {7: 'In'}},
            'inputs': {'Fields': 10, 'page_source': 4},
            'outputs': {'Result': 5}},
           {'event_actions': {'In': 'InterceptionText'},
            'event_links': {'Out': {8: 'In'}},
            'inputs': {'result': 5, 'rule': 11},
            'outputs': {'doc_out': 6}},
           {'event_actions': {'In': 'ConsoleOutput'},
            'event_links': {},
            'inputs': {'result': 6},
            'outputs': {}}],
 'roots': [0],
 'runtime_data': [None,
                  None,
                  None,
                  None,
                  None,
                  None,
                  None,
                  'http://www.zjuch.cn/Html/Departments/Main/DoctorTeam_24.html',
                  '/html/body/div/div[7]/div[3]/div/div[1]/div[2]/ul/li/a/@href',
                  'http://www.zjuch.cn',
                  {'department': '/html/body/div/div/div[7]/div[2]/div[2]/div[2]/p[4]/a/text()',
                   'name': '/html/body/div/div/div[7]/div[2]/div[2]/div[2]/p[1]/b[2]/text()',
                   'special': '/html/body/div/div/div[7]/div[2]/div[2]/div[4]/p[1]//text()',
                   'title': '/html/body/div/div/div[7]/div[2]/div[2]/div[2]/p[2]/text()'},
                  {'special': '专业特长：(.*)'}]}


def start(graph_config):
    from runtime.Runtime import GraphRunnerInstance
    pprint.pprint(graph_config)
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config)

start(graph_config)
