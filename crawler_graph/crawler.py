def crawl(graph_config, input_args=None):
    import sys, os
    sys.path.append(os.path.dirname(__file__))
    from runtime.Runtime import GraphRunnerInstance
    instance = GraphRunnerInstance()
    instance.run_graph(graph_config, input_args)



