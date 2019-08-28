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
            'event_actions': {'In': 'ParseDate'},
            'event_links': {},
            'inputs': {'page_source': 1, 'Fields': 2},
            'outputs': {}
        },


    ],
    'runtime_data': [
        'https://www.bjcyh.com.cn/Html/Doctors/Main/Index_944.html',

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
