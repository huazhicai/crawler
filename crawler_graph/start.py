# -*- coding: utf-8 -*-
import os, sys
from pprint import pprint


# def read_graph_config(file_path):
#     with open(file_path) as f:
#         defNode = f.read()
#     return defNode


def start(graph_config):
    pprint(graph_config)
    from runtime.Runtime import GraphRunnerInstance
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        """编辑器自动运行"""
        graph_config = sys.argv[1]
        graph_config = eval(graph_config)
        start(graph_config)
    else:
        """读取图形节点文件运行"""
        filename = 'test.txt'
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'editor', 'graph', filename)
        # graph_config = read_graph_config(file_path)
        # start(graph_config)
