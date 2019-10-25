"""
存在新增节点，修改节点。但是又不希望uuid生成新的uuid ?
老节点数据保存到old_nodes.json, 新生成的节点保存到nodes.json
新生成数据中的老节点用原来的uuid， 老数据没有的生成新的uuid
"""
import json
import os
import re
from pprint import pprint
from uuid import uuid1, UUID

ACTIONS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'crawler_graph', 'actions')


class GenerateNodes(object):
    def __init__(self):
        self.start_node = {
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
        }
        self.uuidSet = set()

    def read_file(self, file):
        with open(file, encoding='UTF-8') as f:
            result = f.read()
        return result

    def check_node_id(self, name_id):
        assert name_id not in self.uuidSet, f'duplicate uuid: {name_id}'
        try:
            assert UUID(name_id, version=4)
        except Exception:
            print(name_id)
            raise
        self.uuidSet.add(name_id)

    def get_class_node(self):
        for c in os.listdir(ACTIONS_DIR):
            if c.find('generate_nodes') == -1 and c.endswith('.py') and c.find("Events") == -1:

                result = self.read_file(os.path.join(ACTIONS_DIR, c))
                pattern = r"\nclass.*?\tid *= *.+?[\'\"]"
                actions = re.findall(pattern, result, re.S)
                category = c.strip('.py')
                for item in actions:
                    # pprint(item)
                    name_id = re.search(r'id *= *[\'\"](.*?)[\'\"]', item).group(1)
                    self.check_node_id(name_id)
                    name = [re.search(r'class\s(.*?)\(', item).group(1), name_id]
                    args_ = re.findall(r'= args.*?\'(.+?)\'', item)
                    args = [{"type": self.get_data_type(x), "name": [x, str(uuid1())]} for x in args_]
                    # 添加'In'事件
                    args.append({"type": "Event",
                                 "name": ["In", str(uuid1())],
                                 "action": name[0]})

                    returns_ = [x[x.index("(") + 2:-1] for x in
                                re.findall(r'set_output\(\'.+?\'|push_event\(\'Out.*?\'', item)]
                    returns = [{"type": self.get_data_type(x), "name": [x, str(uuid1())]} for x in returns_]
                    yield {
                        "category": category,
                        "name": name,
                        'args': args,
                        'returns': returns
                    }

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
            elif type_ == 'Any':
                type_ = "Any"
            else:
                type_ = 'Any'
        return type_

    def write_to_json(self, filename):
        with open(filename, 'r') as f:
            # 读取nodes.json文本数据
            oldData = json.load(f)

        newData = []
        for newNode in self.get_class_node():
            for oldNode in oldData:
                if newNode['name'][1] == oldNode['name'][1]:

                    for arg in newNode['args']:
                        for argdef in oldNode['args']:
                            if arg['name'][0] == argdef['name'][0]:
                                arg['name'][1] = argdef['name'][1]

                    for ret in newNode['returns']:
                        for retdef in oldNode['returns']:
                            if ret['name'][0] == retdef['name'][0]:
                                ret['name'][1] = retdef['name'][1]
            newData.append(newNode)

        # 原有的节点数据写入到一个old文件中
        parts = os.path.splitext(filename)
        oldFilename = parts[0] + '_old' + parts[1]
        with open(oldFilename, 'w') as f:
            json.dump(oldData, f, indent=4)

        # 新的节点数据覆盖原来的文件
        sorted(newData, key=lambda x: x['category'])
        newData.insert(0, self.start_node)
        with open(filename, 'w') as f:
            json.dump(newData, f, indent=3)
            print("Update Successfully!")


if __name__ == '__main__':
    file_path = 'meta/nodes.json'
    generate = GenerateNodes()
    generate.write_to_json(file_path)
