import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'editor'))
sys.path.insert(1, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'crawler_graph'))


def main():
    # module = __import__('crawler_graph.run')
    # module.run.run(sys.argv)
    func = {}
    exec('from run import run', func)
    func['run'](sys.argv)


if __name__ == '__main__':
    import multiprocessing

    multiprocessing.freeze_support()
    main()
