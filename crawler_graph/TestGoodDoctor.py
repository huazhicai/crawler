# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
"""

graph_config = {
    # 节点配置
    'nodes': [
        {
            'event_actions': {'Default': 'Start'},
            'event_links': {'Out': {1: 'In'}},
            'inputs': {},
            'outputs': {}
        },
        {
            'event_actions': {'In': 'RequestUrl'},
            'event_links': {'Out': {2: 'In'}},
            'inputs': {'Url': 0, 'Charset': 1},
            'outputs': {'Doc': 2}
        },
        {
            'event_actions': {'In': 'ParseUrl'},
            'event_links': {'Out': {3: 'In'}},
            'inputs': {'page_source': 2, 'Fields': 3},
            'outputs': {'Result': 4}
        },
        {
            'event_actions': {'In': 'IteratorList'},
            'event_links': {'Out': {4: 'In'}},
            'inputs': {'doc_in': 4, },
            'outputs': {'doc_out': 5}
        },
        {
            'event_actions': {'In': 'StringConcat'},
            'event_links': {'Out': {5: 'In'}},
            'inputs': {'suffix': 5, 'prefix': 6},
            'outputs': {'doc_out': 7}
        },
        {
            'event_actions': {'In': 'RequestUrl'},
            'event_links': {'Out': {6: 'In'}},
            'inputs': {'Url': 7, 'Charset': 8},
            'outputs': {'Doc': 9}
        },

        {
            'event_actions': {'In': 'ParseUrl'},
            'event_links': {'Out': {7: 'In'}},
            'inputs': {'page_source': 9, 'Fields': 10},
            'outputs': {'Result': 11}
        },
        {
            'event_actions': {'In': 'Acquireurl'},
            'event_links': {'Out': {8: 'In'}},
            'inputs': {'Num': 11, 'Prefix': 12},
            'outputs': {'Url': 13}
        },
        {
            'event_actions': {'In': 'RequestUrl'},
            'event_links': {'Out': {9: 'In'}},
            'inputs': {'Url': 13, 'Charset': 14},
            'outputs': {'Doc': 15}
        },
        {
            'event_actions': {'In': 'DoctorsUrl'},
            'event_links': {'Out': {10: 'In'}},
            'inputs': {'page_source': 15, 'Fields': 16, 'originalurl': 13, 'rule': 17},
            'outputs': {'Result': 18}
        },

        {
            'event_actions': {'In': 'AsynchronousRequests'},
            'event_links': {'Out': {11: 'In'}},
            'inputs': {'Url': 18, },
            'outputs': {'Doc': 21}
        },
        # {
        #     'event_actions': {'In': 'IteratorList'},
        #     'event_links': {'Out': {11: 'In'}},
        #     'inputs': {'doc_in': 18, },
        #     'outputs': {'doc_out': 19}
        # },
        #
        # {
        #     'event_actions': {'In': 'RequestUrl'},
        #     'event_links': {'Out': {12: 'In'}},
        #     'inputs': {'Url': 19, 'Charset': 20},
        #     'outputs': {'Doc': 21}
        # },

        {
            'event_actions': {'In': 'ParseUrl'},
            'event_links': {'Out': {12: 'In'}},
            'inputs': {'page_source': 21, 'Fields': 22},
            'outputs': {'Result': 23}
        },
        {
            'event_actions': {'In': 'Acquireurl'},
            'event_links': {'Out': {13: 'In'}},
            'inputs': {'Num': 23, 'Prefix': 24},
            'outputs': {'Url': 25}
        },

        {
            'event_actions': {'In': 'SplashUrl'},
            'event_links': {'Out': {14: 'In',15:'In'}},
            'inputs': {'Url': 25, },
            'outputs': {'Doc': 26}
        },
        {
            'event_actions': {'In': 'ParseDate'},
            'event_links': {},
            'inputs': {'page_source': 26, },
            'outputs': {'Result': 29}
        },

        {
            'event_actions': {'In': 'ParsePagesource_two'},
            'event_links': {'Out': {16: 'In'}},
            'inputs': {'page_source': 26, 'Fields': 27,'Field': 31,},
            'outputs': {'Result': 28}
        },
        {
            'event_actions': {'In': 'FieldMakeup'},
            'event_links': {'Out': {17: 'In'}},
            'inputs': {'doc_in': 28, 'fields': 29},
            'outputs': {'doc_out': 30}
        },


        {
            'event_actions': {'In': 'ConsoleOutput'},
            'event_links': {},
            'inputs': {'result': 30},
            'outputs': {}
        },

    ],
    'runtime_data': [
        'https://www.haodf.com/yiyuan/zhejiang/hangzhou/list.htm',
        'gb2312',
        None,
        '//*[@id="el_result_content"]/div/div[2]/div[2]/div[2]/ul/li/a/@href',
        None,
        None,
        'https://www.haodf.com',
        None,  # 各个医院的url
        'gb2312',  # 8
        None,  # 所有科室主页面
        '//ul[@class="f-l-i-second"]/li/div/a/@href',  # 10
        None,
        'https:',
        None,  # 一家医院的所有科室url    13
        'gb2312',
        None,  # 每个科室页面源代码    15
        '//div[@class="p_bar"]/a/@href',
        '(.*).htm',
        None,  # 一个科室所有page_url
        None,  # 每一个医院每一个科室每一个页面url 19
        'gb2312',
        None,
        '//*[@id="doc_list_index"]/tr/td[1]/li/a[1]/@href',
        None,  # 23
        'https:',
        None,  # 25
        None,  # 每个医生页面源代码
        {
            'province'    : '//div[@class="luj"]/a[3]/text()',
            'hospital'    : '//div[@class="luj"]/a[4]/text()',
            'department'  : '//div[@class="luj"]/a[5]/text()',
            'name'        : '//div[@class="luj"]/a[6]/text()',
            'title'       : '//div[@class="doctor_about"]/div[@class="middletr"][1]/div[@class="lt"]/table[1]/tbody/tr//text()',
            'special'     : '//*[@id="full_DoctorSpecialize"]/text()',
            'resume'      : '//*[@id="full"]/text()',
            # 'resumes'      : '//*[@id="bp_doctor_about"]/div/div[2]/div/table[1]/tr[5]/td[3]/text()',
            'personal_web': '//div[@class="doctor-home-page clearfix"]/span[3]/a/text()'
        },
        None,#28
        None,#门诊信息
        None,
        {   'resume_ss'      : '//div[@class="doctor_about"]/div[@class="middletr"][1]/div[@class="lt"]/table[1]/tbody/tr[5]/td[3]/text()',
            'resume_s': '//div[@class="doctor_about"]/div[@class="middletr"][1]/div[@class="lt"]/table[1]/tbody/tr[4]/td[3]/text()',
            'judge': '//div[@class="doctor_about"]/div[@class="middletr"][1]/div[@class="lt"]/table[1]/tbody/tr',
            'titless': '//div[@class="doctor_about"]/div[@class="middletr"][1]/div[@class="lt"]/table[1]/tbody/tr[3]/td[3]/text()',
            'titles': '//div[@class="doctor_about"]/div[@class="middletr"][1]/div[@class="lt"]/table[1]/tbody/tr[2]/td[3]/text()',
        },

    ],
    'roots': [0]
}
if __name__ == '__main__':
    # 第一步
    from runtime.Runtime import GraphRunnerInstance

    instance = GraphRunnerInstance()
    instance.run_graph(graph_config)
