# -*- coding: utf-8 -*-
import os
from pprint import pprint


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
