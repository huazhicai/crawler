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
		#解析科室总页面，获取所有科室url
		{
			'event_actions': {'In': 'RequestUrl'},
			'event_links'  : {'Out': {2: 'In', 3: 'In'}},
			'inputs'       : {'Url': 0, 'Fields':1},#url输入所有科室网页 Fields获取科室href的选择器（）投入
			'outputs'      : {'Doc': 2, 'Result':3} # 将返回结果存入内存 ，结果为装有 多个链接的字典
		},
		{
			'event_actions' : {'In': 'ConsoleOutput'}, #将args['result']结果输出，打印在控制台                 DataOutputs
			'event_links'  : {},
			'inputs': {'result': 3},#（那内存3 所在的数据）{'departments': ['web/ksindex/58.html', 'web/ksindex/50.html', 'web/ksi
			'outputs': {}
		},
		{
			'event_actions': {'In': 'ContainerGetItem'}, #DataProcesses 处理字典 获得 链接列表
			'event_links'  : {'Out': {4: 'In'}},
			'inputs'       : {'doc_in': 3, 'field': 4},#3是字典中装有多个链接{'departments': ['web/ksindex/58.html', 'web/ksindex/50.html', 'web/ksindex
			'outputs'      : {'doc_out': 5}#['web/ksindex/58.html', 'web/ksindex/50.html', 'web/ksindex/48.html', 'web/ksindex/53.html', 'web/ksindex/56.html', 'web/ksindex/55.html', 'web/ksinde
		},
		{
			'event_actions': {'In': 'IteratorList'}, #FlowControll 流控制，遍历列表       这里有遍历！！！！！！！！！
			'event_links'  : {'Out': {5: 'In'}},
			'inputs'       : {'doc_in': 5},#['web/ksindex/58.html', 'web/ksindex/50.html', 'web/ksindex/48.html', 'web/ksindex/53.
			'outputs'      : {'doc_out': 6}#web/ksindex/58.html  输出每一个科室的url
		},
		{
			'event_actions': {'In': 'StringConcat'},#DataProcesses
			'event_links'  : {'Out': {6: 'In', 7: 'In'}},
			'inputs'       : {'prefix': 7, 'suffix': 6}, #将url的域和参数拼接
			'outputs'      : {'doc_out': 8}  #8 为所有科室的完整url
		},
		{
			'event_actions': {'In': 'ConsoleOutput'},# DataOutputs
			'event_links'  : {},
			'inputs'       : {'result': 8}, #打印输出http://www.301hospital.mil.cn/web/showexp/myhcv/58/505.html
			'outputs'      : {}
		},
		#解析具体科室url，获取医生链接
		{
			'event_actions': {'In': 'RequestUrl'},#解析页面获取每一个医生链接
			'event_links'  : {'Out': { 8:'In' }},  #
			'inputs'       : {'Url': 8, 'Fields':9},#	{'doctors': ['.ks_yishi > ul > li > a', True, 'href']},
			'outputs'      : {'Doc': 10, 'Result':11}#{'doctors': ['web/ksindex/58.html', 'web/ksindex/50.html', 'web/ksi
		},
		{
			'event_actions': {'In': 'ContainerGetItem'},#DataProcesses 处理字典 获得 链接列表
			'event_links'  : {'Out': {9: 'In'}},
			'inputs'       : {'doc_in': 11, 'field': 12},#将字典中的医生列表获取
			'outputs'      : {'doc_out': 13}#['web/ksindex/58.html', 'web/ksindex/50.html', 'web/ksi
		},
		{
			'event_actions': {'In': 'IteratorList'},##FlowControll遍历  医生url列表  ！！！！！！遍历
			'event_links'  : {'Out': {10: 'In'}},
			'inputs'       : {'doc_in': 13},     #拿入医生url 列表
			'outputs'      : {'doc_out': 14}      #输出每一个医生的url
		},
		{
			'event_actions': {'In': 'StringConcat'},#DataProcesses
			'event_links'  : {'Out': {11: 'In', 12: 'In'}},
			'inputs'       : {'prefix': 15, 'suffix': 14}, #将url 域和参数拼接
			'outputs'      : {'doc_out': 16}    #输出一个完整的医生url
		},
		{
			'event_actions': {'In': 'ConsoleOutput'},# DataOutputs
			'event_links'  : {},
			'inputs'       : {'result': 16}, #打印输入完整的医生url
			'outputs'      : {}
		},
		#解析每一个url 获取想要的字段信息
		{
			'event_actions': {'In': 'RequestUrl'},
			'event_links'  : {'Out': {13: 'In'}},
			'inputs'       : {'Url': 16, 'Fields': 17},#拿url  和css选择器
			'outputs'      : {'Doc': 18, 'Result': 19}#输出结果到内存中{'name': '姓名：潘长玉', 'title': '姓名：潘长玉\xa0\xa0\xa0\xa0\xa0\xa0职称：主任医师、教
		},
		{
			'event_actions': {'In': 'FieldMakeup'},#DataProcesses   手动增加多余字段
			'event_links'  : {'Out': {14: 'In'}},
			'inputs'       : {'doc_in': 19, 'fields': 20},#20{'hospital': '北京301医院', 'grade': '三甲'},
			'outputs'      : {'doc_out': 21}         #在原来的字段中添加多余字段  写入内存
		},
		#考虑问题，如何判断是否有异常符号
		{
			'event_actions': {'In': 'OperationList'},#除去字段中的异常符号
			'event_links'  : {'Out': {15: 'In'}},
			'inputs'       : {'result': 21},
			'outputs'      : {'doc_out': 22}
		},
		#
		{
			'event_actions': {'In': 'InterceptionText'},
			'event_links'  : {'Out': {16: 'In'}},
			'inputs'       : {'result': 22,'rule' : 23},
			'outputs'      : {'doc_out': 24}
		},


		{
			'event_actions': {'In': 'ConsoleOutput'},#打印数据到控制台
			'event_links'  : {},
			'inputs'       : {'result': 24},
			'outputs'      : {}
		},
	],
	'runtime_data': [
		'http://www.301hospital.mil.cn/web/keshi/ksdh.html',
		{'departments': '/html/body/div[3]/div/div[3]/div[4]/ul/li/a/@href'},
		None,
		None,
		'departments',
		None,
		None,
		'http://www.301hospital.mil.cn/',
		None,
		{'doctors': '//div[@class="ks_yishi"]/ul/li/a/@href',},
		None,

		None,
		'doctors',
		None,
		None,
		'http://www.301hospital.mil.cn/',
		None,
		{
			'name'           : '//*[@id="showexpdiv"]/ul/li[1]/strong/text()',
			'title'          : '//*[@id="showexpdiv"]/ul/li[1]//text()',
			'department'     : '//*[@id="showexpdiv"]/ul/li[1]//text()',
			'special'        : '/html/body/div[4]/div[11]//text()',
			'resume'         : '//*[@id="showexpdiv"]/ul/li[3]/p//text()',
			'outpatient_info': '/html/body/div[4]/div[14]/table//text()',
		},
		None,
		None,
		{'hospital': '北京301医院', 'grade': '三甲'},

		None,
		None,
		{
			'name'          : r'姓名：(.*)',
			'title'			: r'职称：(.*).*?科室：.*',
			'department'    : r'科室：(.*).*?'

		},
		None,
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

