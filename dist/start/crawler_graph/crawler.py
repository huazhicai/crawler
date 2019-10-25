# -*- coding: utf-8 -*-
import os, sys

sys.path.append(os.path.dirname(__file__))


def resource_path(relative_path):
    """ 获取当前文件绝对路径"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def read_graph_config(file_path):
    with open(file_path) as f:
        defNode = f.read()
    return defNode


def crawl(graph_config, input_args=None):
    from runtime.Runtime import GraphRunnerInstance
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config, input_args)




