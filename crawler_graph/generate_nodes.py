import json
import os

from runtime.Runtime import ActionManager


class GenerateNodes(object):
    def __init__(self):
        self.uuidSet = set()
        self.action_manager = ActionManager()

    def check_uuid(self, name_id):
        assert name_id not in self.uuidSet, f'重复的 uuid: {name_id}'
        self.uuidSet.add(name_id)

    def check_type(self, data_type):
        allow_type = ['Int', 'String', 'Float', 'Dict', 'List', 'Event', 'Bool', 'Tuple', 'Any']
        assert data_type in allow_type, f'数据类型错误: {data_type}'

    def node_args(self, action_name, action):
        args = action.node_info['args']
        temp = []
        for arg in args:
            self.check_uuid(arg[2])
            self.check_type(arg[1])
            if arg[1] == 'Event':
                temp.append({
                    'type': arg[1],
                    'name': [arg[0], arg[2]],
                    'action': action_name
                })
            else:
                temp.append({
                    'type': arg[1],
                    'name': [arg[0], arg[2]]
                })
        return temp

    def node_returns(self, action):
        returns = action.node_info['returns']
        temp = []
        for ret in returns:
            self.check_uuid(ret[2])
            self.check_type(ret[1])
            temp.append(
                {
                    'type': ret[1],
                    'name': [ret[0], ret[2]]
                })

    def gen_nodes(self):
        nodes = []
        for action_name, action in self.action_manager.action_map.items():
            self.check_uuid(action._id)
            nodes.append({
                'category': action.__module__.lstrip('actions.'),
                'name': [action_name, action._id],
                'args': self.node_args(action_name, action),
                'return': self.node_returns(action)
            })
        return nodes

    def save_to_json(self, filename):
        nodes = self.gen_nodes()

        # 原有的节点数据写入到一个old文件中
        with open(filename, 'r') as f:
            old_data = json.load(f)

        parts = os.path.splitext(filename)
        old_filename = parts[0] + '_old' + parts[1]
        with open(old_filename, 'w') as f:
            json.dump(old_data, f, indent=4)

        with open(filename, 'w') as f:
            json.dump(nodes, f, indent=3)
            print("Update Successfully!")


if __name__ == '__main__':
    filename = '../editor/meta/nodes.json'
    generater = GenerateNodes()
    generater.save_to_json(filename)
