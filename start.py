def main():
    # module = __import__('crawler_graph.run')
    import sys
    # module.run.run(sys.argv)
    func = {}
    exec('from crawler_graph.run import run', func)
    func['run'](sys.argv)


if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()
    main()


