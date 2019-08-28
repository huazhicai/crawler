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
			'event_links': {'Out': {1 : 'In'}},
			'inputs': {},
			'outputs': {}
		},
		{
			'event_actions': {'In': 'TestCookie'},
			'event_links'  : {'Out': {2 : 'In',}},
			'inputs'       : {'Url': 0, 'Account':1,},
			'outputs'      : {'cookies' : 2}
		},
		{
			'event_actions': {'In': 'Acquireurl'},
			'event_links'  : {'Out': {3 : 'In',}},
			'inputs'       : {'Num':5,'Prefix':4 },
			'outputs'      : {'Url':6}
		},
		{
			'event_actions': {'In': 'CookieRequest'},
			'event_links'  : {'Out': {4 : 'In',}},
			'inputs'       : {'cookies':2,'Headers':3 ,'Url':6},
			'outputs'      : {'result': 7}
		},
		{
			'event_actions': {'In': 'ParsePagesource'},
			'event_links'  : {'Out': {5 : 'In',}},
			'inputs'       : {'page_source':7, 'Fields':8},
			'outputs'      : {'Result': 9}
		},
		{
			'event_actions': {'In': 'OperationList'},
			'event_links'  : {'Out': {6: 'In',}},
			'inputs'       : {'result':9},
			'outputs'      : {'doc_out':10}
		},
		{
			'event_actions': {'In': 'FillupInfor'},
			'event_links'  : {'Out': {7: 'In',}},
			'inputs'       : {'result':10},
			'outputs'      : {'doc_out':11}
		},
		{
			'event_actions': {'In': 'ConsoleOutput'},
			'event_links'  : {},
			'inputs'       : {'result':11},
			'outputs'      : {}
		},
	],
	'runtime_data': [
		'http://chinackd.medidata.cn/login.jsp',
		{'UserName' : 'demo3','PassWord' : 'tpqr6844'},
		None,   #存放cookie
		{'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X)AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
		 'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
		 'accept-encoding': 'gzip, deflate, br',
         'accept-language': 'zh-CN,zh;q=0.9',},
		'http://chinackd.medidata.cn/jsp/para/pm2/pdm.jsp?PtId=',
		[83290,83287,83370,83475,83545],
		None,  #存放完整的url
		None,  #存放page_souce
		{
			'name'           : '//*[@id="P101"]/@value',
			'number'         : '//*[@id="P103"]/@value',
			'site'           : '//*[@id="P106"]/text()'
		},
		None,
		None,
		None,
		None
	],
	'roots': [0]
}

if __name__ == '__main__':
	#第一步
	from runtime.Runtime import GraphRunnerInstance

	instance = GraphRunnerInstance()
	instance.run_graph(graph_config)

