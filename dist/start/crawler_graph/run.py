# -*- coding: utf-8 -*-
import json
import os, sys
from editor import main
from editor.A_Exporter import single_file_export

sys.path.append(os.path.dirname(__file__))


def crawl(graph_config, input_args=None):
    from runtime.Runtime import GraphRunnerInstance
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config, input_args)


def read_graph_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def run():
    print(sys.argv)
    if len(sys.argv) < 2:
        main.main()
    else:
        filename = sys.argv[1]
        data = read_graph_file(filename)
        graph_config = single_file_export(data)
        args = {}
        if len(sys.argv) > 2:
            values = sys.argv[2].strip(' {}').split(',')
            for item in values:
                k, v = item.split(':')
                k.strip()
                v.strip()
                args[k] = v
        crawl(graph_config, args)


if __name__ == '__main__':
    run()
