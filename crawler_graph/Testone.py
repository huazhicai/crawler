# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
"""

graph_config = {
    # 节点配置
    'nodes': [
        {
            'event_actions': {'Default': 'Start'},
            'event_links': {'Out': {1: 'In'}},
            'inputs': {},
            'outputs': {}
        },
        {
            'event_actions': {'In': 'RequestUrl'},
            'event_links': {'Out': {2: 'In', }},
            'inputs': {'Url': 0},
            'outputs': {'Doc': 1}
        },
        {
            'event_actions': {'In': 'ParseUrl'},
            'event_links': {'Out': {3: 'In'}},
            'inputs': {'page_source': 1, 'Fields': 2},
            'outputs': {'Result': 3}
        },
        {
            'event_actions': {'In': 'IteratorList'},
            'event_links': {'Out': {4: 'In'}},
            'inputs': {'doc_in': 3, },
            'outputs': {'doc_out': 4},
        },
        {
            'event_actions': {'In': 'StringConcat'},
            'event_links': {'Out': {5: 'In'}},
            'inputs': {'suffix': 4, 'prefix': 5},
            'outputs': {'doc_out': 6},
        },
        {
            'event_actions': {'In': 'RequestUrl'},
            'event_links': {'Out': {6: 'In'}},
            'inputs': {'Url': 6, },
            'outputs': {'Doc': 7},
        },
        {
            'event_actions': {'In': 'ParsePagesource'},
            'event_links': {'Out': {7: 'In'}},
            'inputs': {'page_source': 7, 'Fields': 8},
            'outputs': {'Result': 9}
        },
        {
            'event_actions': {'In': 'InterceptionText'},
            'event_links':{'Out': {8: 'In'}},
            'inputs': {'result': 9, 'rule': 10},
            'outputs': {'doc_out':11}
        },
        {
            'event_actions': {'In': 'ConsoleOutput'},
            'event_links': {},
            'inputs': {'result': 11, },
            'outputs': {}
        },

    ],
    'runtime_data': [
        'http://www.zjuch.cn/Html/Departments/Main/DoctorTeam_24.html',
        None,
        '/html/body/div/div[7]/div[3]/div/div[1]/div[2]/ul/li/a/@href',
        None,
        None,
        'http://www.zjuch.cn',
        None,
        None,  # page_souce
        {
            'name': '/html/body/div/div/div[7]/div[2]/div[2]/div[2]/p[1]/b[2]/text()',
            'title': '/html/body/div/div/div[7]/div[2]/div[2]/div[2]/p[2]/text()',
            'department': '/html/body/div/div/div[7]/div[2]/div[2]/div[2]/p[4]/a/text()',
            'special' : '/html/body/div/div/div[7]/div[2]/div[2]/div[4]/p[1]//text()',
        },
        None,
        {
            'special': r'专业特长：(.*)',

        },
        None,
        None,
        None,
        None,
    ],
    'roots': [0]
}

if __name__ == '__main__':
    # 第一步
    from runtime.Runtime import GraphRunnerInstance

    instance = GraphRunnerInstance()
    instance.run_graph(graph_config)
