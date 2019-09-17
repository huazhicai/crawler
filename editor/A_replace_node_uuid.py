import json
from uuid import UUID, uuid1
from collections import OrderedDict
from pprint import pprint


def get_nodes_data():
    with open('meta/nodes.json', 'r') as f:
        defData = json.load(f)
    return defData


def adjust_order(defData):
    """调整节点内的次序"""
    nodes_data = []
    for nodeDef in defData:
        nodeDef['category'] = nodeDef['category']
        nodeDef['name'] = nodeDef['name']
        nodeDef['args'] = nodeDef['args']
        nodeDef['returns'] = nodeDef['returns']
    pprint(defData)


def replace_all_uuid(defData):
    """替换nodes.json中的所以uuid, 慎用，执行后所有的原graph里的图将不能重新打开"""
    for nodeDef in defData:
        for arg in nodeDef['args']:
            arg['name'][1] =str(uuid1())
        for ret in nodeDef['returns']:
                ret['name'][1] = str(uuid1())
        nodeDef['name'][1] = str(uuid1())
    with open('meta/nodes.json', 'w') as f:
        json.dump(defData, f, indent=4)
    return


def replace_repeat_uuid(defData):
    """替换重复，无效的uuid"""
    uuidSet = set()
    for nodeDef in defData:
        for arg in nodeDef['args']:
            uuid = arg['name'][1]
            try:
                assert uuid not in uuidSet
                assert UUID(uuid, version=4)
            except:
                arg['name'][1] = str(uuid1())
                print(uuid, 'has been replaced by', arg['name'][1])
            uuidSet.add(uuid)

        for ret in nodeDef['returns']:
            uuid = ret['name'][1]
            try:
                assert uuid not in uuidSet
                assert UUID(uuid, version=4)
            except:
                ret['name'][1] = str(uuid1())
                print(uuid, 'has been replaced by', ret['name'][1])
            uuidSet.add(uuid)

        uuid = nodeDef['name'][1]
        try:
            assert uuid not in uuidSet
            assert UUID(uuid, version=4)
        except:
            nodeDef['name'][1] = str(uuid1())
            print(uuid, 'has been replaced by', nodeDef['name'][1])
        uuidSet.add(uuid)

    with open('meta/nodes.json', 'w') as f:
        json.dump(defData, f, indent=2)
    return


if __name__ == '__main__':
    defData = get_nodes_data()
    replace_repeat_uuid(defData)
    # adjust_order(defData)
