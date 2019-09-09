# -*- coding: utf-8 -*-
import os
from pprint import pprint

graph_config = {'nodes': [{'event_actions': {'Default': 'Start'},
                           'event_links': {'Out': {1: 'In'}},
                           'inputs': {},
                           'outputs': {}},
                          {'event_actions': {'In': 'RequestUrl'},
                           'event_links': {'Out': {2: 'In'}},
                           'inputs': {'url_str': 7},
                           'outputs': {'response_str': 0}},
                          {'event_actions': {'In': 'ParseUrl'},
                           'event_links': {'Out': {3: 'In'}},
                           'inputs': {'page_source_str': 0, 'xpath_str': 8},
                           'outputs': {'result_list': 1}},
                          {'event_actions': {'In': 'IteratorList'},
                           'event_links': {'Out': {4: 'In'}},
                           'inputs': {'doc_list': 1},
                           'outputs': {'item_any': 2}},
                          {'event_actions': {'In': 'StringConcat'},
                           'event_links': {'Out': {5: 'In'}},
                           'inputs': {'prefix_str': 9, 'suffix_str': 2},
                           'outputs': {'contacted_str': 3}},
                          {'event_actions': {'In': 'RequestUrl'},
                           'event_links': {'Out': {6: 'In'}},
                           'inputs': {'url_str': 3},
                           'outputs': {'response_str': 4}},
                          {'event_actions': {'In': 'ParsePagesource'},
                           'event_links': {'Out': {7: 'In'}},
                           'inputs': {'doc_dict': 10, 'page_source_str': 4},
                           'outputs': {'result_dict': 5}},
                          {'event_actions': {'In': 'InterceptionText'},
                           'event_links': {'Out': {8: 'In'}},
                           'inputs': {'doc1_dict': 5, 'doc2_dict': 11},
                           'outputs': {'result_dict': 6}},
                          {'event_actions': {'In': 'ConsoleOutput'},
                           'event_links': {},
                           'inputs': {'result_any': 6},
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


# def read_graph_config(file_path):
#     with open(file_path) as f:
#         graph_data = f.read()
#     return eval(graph_data)


def start(graph_config, qt_text=None):
    # pprint(graph_config)
    for node in graph_config['nodes'][1:]:
        if node['event_actions']['In'] == 'ConsoleOutput':
            node['inputs'].update({'qt_text': -1})
            graph_config['runtime_data'].append(qt_text)

    from runtime.Runtime import GraphRunnerInstance
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config)


if __name__ == '__main__':
    filename = 'test.txt'
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'editor', 'graph', filename)
    # graph_config = read_graph_config(file_path)
    # pprint(graph_config)
    start(graph_config)
