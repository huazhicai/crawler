#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
"""

from runtime.ActionIO import DataCore
from runtime.ActionIO import ActionIO

class Node(object):
	def __init__(self):
		self.io = None
		self.event_actions = {}
		self.event_links = {}

	def init(self, io, event_actions, event_links):
		self.io = io
		self.event_actions = event_actions
		self.event_links = event_links

	def get_event_action(self, event):
		return self.event_actions[event]

	def get_event_link(self, event):
		return self.event_links[event]


class NodeGraph(object):

	def __init__(self, action_manager):
		self.root_nodes = []
		self.nodes = []
		self.action_manager = action_manager  #ActionManager()

	def init_with_config(self, graph_config):

		nodes_config = graph_config['nodes']

		data_core = DataCore()
		data_core.init_runtime(graph_config['runtime_data'])

		nodes = self.nodes = [] #空列表
		for index, node_config in enumerate(nodes_config):#依次获取每个节点下标和每个节点内容
			io = ActionIO(data_core, index, node_config['inputs'], node_config['outputs'], self.push_event)
			event_actions = node_config['event_actions']
			event_links = node_config['event_links']
			node = Node()
			node.init(io, event_actions, event_links)
			nodes.append(node)

		roots = graph_config['roots']
		self.root_nodes = roots

	def start(self):
		for node_idx in self.root_nodes:
			self.execute(node_idx, 'Default')

	def execute(self, node_idx, event):
		node = self.nodes[node_idx]
		action = node.get_event_action(event)

		self.action_manager.execute_action(action, node.io.get_inputs(), node.io)


	def push_event(self, node_idx, event):
		node = self.nodes[node_idx]
		for n_index, n_event in node.get_event_link(event).items():
			self.execute(n_index, n_event)

class ActionManager(object):

	def __init__(self):
		self.action_map = {}
		self.scan_action_map()

	def scan_action_map(self):
		import os, sys
		import inspect
		from runtime.Action import Action

		actionpath = os.path.dirname(__file__) + '/../actions/'
		sys.path.append(actionpath)
		for file in os.listdir(actionpath):

			filename = os.path.splitext(os.path.basename(file))[0]
			if filename == '__init__':
				continue
			mod = __import__(filename)
			predicate = lambda member: inspect.isclass(member) and issubclass(member, Action) and member is not Action
			self.action_map.update((action[0], action[1]()) for action in inspect.getmembers(mod, predicate))
	# 数据的传输
	def execute_action(self, action_name, args, io):
		self.action_map[action_name](args, io)



class GraphRunnerInstance(object):

	def __init__(self):
		#
		# self.action_map = {}
		# self.scan_action_map()
		self.action_manager = ActionManager()

		self.node_graphs = []

	def run_graph(self, graph_config):
		node_graph = NodeGraph(self.action_manager)
		node_graph.init_with_config(graph_config)
		node_graph.start()
		self.node_graphs.append(node_graph)



if __name__ == '__main__':

	instance = GraphRunnerInstance()
	print(instance.action_manager.action_map)