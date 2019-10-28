def main():
    func = {}
    exec('from crawler_graph.run import run', func)
    func['run']()


if __name__ == '__main__':
    main()
