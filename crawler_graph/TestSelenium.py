#-*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
"""

graph_config = {
	#节点配置
	'nodes' : [
		{
			'event_actions': {'Default': 'Start'},
			'event_links': {'Out': {1: 'In'}},
			'inputs': {},
			'outputs': {}
		},

		{
			'event_actions': {'In': 'SeleniumUrl'},
			'event_links'  : {'Out': {2: 'In'}},
			# 'event_links'  : {'Out': {2: 'In' , 3: 'In'}},
			'inputs'       : {'Url': 0, 'Account':1,'Query':2},
			'outputs'      : {'result':3 }
		},
		{
			'event_actions': {'In': 'ConsoleOutput'},
			'event_links'  : {},
			'inputs'       : {'result':3},
			'outputs'      : { }
		},

		# {
		# 	'event_actions': {'In': 'ParsePagesource'},
		# 	'event_links'  : {},
		# 	'inputs'       : {'page_source':3, 'Fields':4},
		# 	'outputs'      : { }
		# },
		#
	],
	'runtime_data': [
		'http://chinackd.medidata.cn/login.jsp',
		{'UserName' : 'demo3','PassWord' : 'tpqr6844'},
		['AAAA','BBBBBB','CCCCCCCCCCC','DDDDDDDDDDDDDD'],
		None,   #page_source网页源代码
		# {
		# 	#xpath解析规则
		# 	'name'           : [],
		# 	'title'          : [],
		# 	'department'     : [],
		# 	'special'        : [],
		# 	'resume'         : [],
		# 	'outpatient_info': []
		# },
	],
	'roots': [0]
}

if __name__ == '__main__':
	#第一步
	from runtime.Runtime import GraphRunnerInstance

	instance = GraphRunnerInstance()
	instance.run_graph(graph_config)

