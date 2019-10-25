import json
import sys, os

exec('from editor import main')
exec('from crawler_graph.crawler import crawl')
exec('from editor.A_Exporter import single_file_export')


def read_graph_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def start():
    print(sys.argv)
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        data = read_graph_file(filename)
        graph_config = single_file_export(data)
        args = {}
        if len(sys.argv) > 2:
            values = sys.argv[2].strip(' {}').slip(',')
            for item in values:
                k, v = item.split(':')
                k.strip()
                v.strip()
                args[k] = v
        crawl(graph_config, args)
    else:
        if len(sys.argv) == 1:
            main.mian()
        else:
            pass


if __name__ == '__main__':
    start()

