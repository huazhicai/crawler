# -*- coding: utf-8 -*-
import os, sys
from runtime.Runtime import GraphRunnerInstance


def resource_path(relative_path):
    """ 获取当前文件绝对路径"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def read_graph_config(file_path):
    with open(file_path) as f:
        defNode = f.read()
    return defNode


def start(graph_config, input_args=None):
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config, input_args)


def main():
    assert len(sys.argv) > 1

    file_or_config = sys.argv[1]
    if os.path.isfile(file_or_config):
        # 读取图形节点文件运行
        graph_config = eval(read_graph_config(file_or_config))
    else:
        # 编辑器自动运行
        graph_config = eval(file_or_config)

    args = {}
    if len(sys.argv) > 2:
        value = sys.argv[2].strip(' {}').split(",")
        for item in value:
            k, v = item.split(':')
            k = k.strip()
            v = v.strip()
            args[k] = v
    start(graph_config, args)
