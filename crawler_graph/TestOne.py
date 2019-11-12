graph_config = {
    'nodes': [
        {'event_actions': {'Default': 'Start'}, 'event_links': {'Out': {1: 'In'}}, 'inputs': {}, 'outputs': {}},

        {'event_actions': {'In': 'GetRequest'}, 'event_links': {'Out': {2: 'In'}},
         'inputs': {'url_str': 1,  'cookie_optional_dict': 2,
                    'resp_type_optional_str': 2}, 'outputs': {'response': 0}},

        {'event_actions': {'In': 'ConsoleOutput'}, 'event_links': {},
         'inputs': {'prefix_optional_str': 3, 'result_any': 0}, 'outputs': {}}]
    ,
    'runtime_data': [None, 'https://www.baidu.com/', None, '你好'],
    'roots': [0]
}

if __name__ == '__main__':
    from runtime.Runtime import GraphRunnerInstance

    instance = GraphRunnerInstance()
    instance.run_graph(graph_config, {})
