# -*- coding: utf-8 -*-
import os
from pprint import pprint


def read_graph_config(file_path):
    with open(file_path) as f:
        graph_data = f.read()
    return eval(graph_data)


def start(graph_config):
    pprint(graph_config)
    from runtime.Runtime import GraphRunnerInstance
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config)


if __name__ == '__main__':
    filename = 'test.txt'
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'editor', 'graph', filename)
    graph_config = read_graph_config(file_path)
    # pprint(graph_config)
    start(graph_config)
