import json
import os
import sys
import re
from pprint import pprint
from uuid import uuid1

ACTIONS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'crawler_graph', 'actions')


class GenerateNodes(object):
    def __init__(self):
        self.nodes = [{
            "category": "Event",
            "returns": [{
                "type": "Event",
                "name": ["Out", "a9f4fe1f-00b9-413c-a332-f98ef6327465"]
            }],
            "args": [{
                "type": "Event",
                "name": ["Default", "5168e336-f2c3-4abc-b117-6a64dd860dff"],
                "action": "Start"
            }],
            "name": ["Start", "9ed37096-bc78-47c9-b0d0-44fef1f8002d"]
        }]

    def read_file(self, file):
        with open(file, encoding='UTF-8') as f:
            result = f.read()
        return result

    def get_class_node(self, nodeSet):
        for c in os.listdir(ACTIONS_DIR):
            if c.endswith('.py') and c.find("Event") == -1:
                result = self.read_file(os.path.join(ACTIONS_DIR, c))
                # 提取类的模式
                pattern = r'\nclass.*?push_event\(\'.*?\'\)|\nclass.*?pass'
                actions = re.findall(pattern, result, re.S)
                category = c.strip('.py')
                for item in actions:
                    name = [re.search(r'class\s(.*?)\(', item).group(1), str(uuid1())]
                    # 判定节点是否存在
                    if name[0] not in nodeSet:
                        args_ = re.findall(r'args\[\'(.+?)\'\]', item)
                        args = [{"type": self.get_data_type(x), "name": [x, str(uuid1())]} for x in args_]
                        # 添加'In'事件
                        args.append({"type": "Event",
                                     "name": ["In", str(uuid1())],
                                     "action": name[0]})

                        returns_ = [x[x.index("(") + 2:-1] for x in
                                    re.findall(r'set_output\(\'.+?\'|push_event\(\'Out\'', item)]
                        returns = [{"type": self.get_data_type(x), "name": [x, str(uuid1())]} for x in returns_]
                        self.nodes.append({
                            "category": category,
                            "name": name,
                            'args': args,
                            'returns': returns
                        })

    def get_data_type(self, item):
        if item in ('Out', 'In'):
            type_ = "Event"
        else:
            type_ = item.split('_')[-1]
            if type_ == 'str':
                type_ = "String"
            elif type_ == "list":
                type_ = "List"
            elif type_ == "dict":
                type_ = "Dict"
            elif type_ == "int":
                type_ = "Int"
            elif type_ == "float":
                type_ = "Float"
            else:
                type_ = "Any"
        return type_

    def write_to_json(self):
        nodeSet = set()
        self.get_class_node(nodeSet)
        # print(self.nodes)
        with open('meta/nodes.json', 'w') as f:
            json.dump(self.nodes, f, indent=2)

    def add_to_json(self):
        nodeSet = set()
        with open('meta/nodes.json') as f:
            defData = json.load(f)
        for nodeDef in defData:
            nodeSet.add(nodeDef['name'][0])
        self.get_class_node(nodeSet)
        with open('meta/nodes.json', 'a') as f:
            json.dump(self.nodes, f, indent=2)


if __name__ == '__main__':
    nodes = GenerateNodes()
    nodes.write_to_json()
    # nodes.add_to_json()
