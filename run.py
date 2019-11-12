# -*- coding: utf-8 -*-
import json

from crawler_graph.crawler import crawl
from editor import main


def read_graph_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def run(argv):
    if len(argv) < 2:
        main.main()
    else:
        filename = argv[1]
        data = read_graph_file(filename)
        from editor.A_Exporter import single_file_export
        graph_config = single_file_export(data)
        args = {}
        if len(argv) > 2:
            values = argv[2].strip(' {}').split(',')
            for item in values:
                k, v = item.split(':')
                k.strip()
                v.strip()
                args[k] = v
        crawl(graph_config, args)
