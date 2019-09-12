# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
from lxml import html
import re
import json

"""
好大夫独有节点
"""


# 对网页unicode 数据进行筛选，选取需要数据

class Unicode(Action):
    def __call__(self, args, io):
        con = args['text_str']
        script = re.findall(r'.*?letArrive\((.*?)\);</script>', con)
        contents = ""
        for i in script:
            need_con = json.loads(i)
            content = need_con['content']
            contents += content
        io.set_output('result_str', contents)
        io.push_event('Out')


"""医生url"""
class DoctorsUrl(Action):
    def __call__(self, args, io):
        originalurl = args['originalurl_str']
        page_source = args['page_source_str']
        rule = args['re_pattern_str']
        etree = html.etree
        tree = etree.HTML(page_source)
        fields = args['xpath_str']
        urls = tree.xpath(fields)
        # 页数为 len（urls）
        if len(urls) > 0:
            # 页数为
            nums = len(urls)
        else:
            nums = 1
        prefix = re.findall(rule, originalurl)[0]
        PagesList = []
        for num in range(1, nums + 1):
            DoctorsUrl = prefix + '/menzhen_' + str(num) + '.htm'
            PagesList.append(DoctorsUrl)
        io.set_output('url_list', PagesList)
        io.push_event('Out')

 # 针对简历的不同 重些
class ParsePagesource_two(Action):

    def __call__(self, args, io):
        page_source = args['page_source_str']
        fields = args['field_xpath_dict']
        field = args['field_dict']

        result = {}
        etree = html.etree
        tree = etree.HTML(page_source)

        for key, value in fields.items():
            values = tree.xpath(value)
            values = ''.join(values)
            result[key] = ''.join(values.split())

        judge = tree.xpath(field['judge'])
        if len(judge) == 5:
            resumes = tree.xpath(field['resume_ss'])

            title = tree.xpath(field['titless'])
        else:
            resumes = tree.xpath(field['resume_s'])

            title = tree.xpath(field['titles'])

        title = ''.join(title)
        resumes = ''.join(resumes)

        result['resumes'] = ''.join(resumes.split())
        result['title'] = ''.join(title.split())

        if len(result['resume']) == 0:
            del result['resume']
            result["resume"] = result.pop("resumes")
        else:
            del result['resumes']
        if len(result["province"]) == 0:
            print("啦啦啦啦啦啦啦")
        io.set_output('result_dict', result)
        io.push_event('Out')


"""解析日期"""
class ParseDate(Action):
    def __init__(self):
        self.am = {
            2: '星期一上午', 3: '星期二上午', 4: '星期三上午', 5: '星期四上午', 6: '星期五上午',
            7: '星期六上午', 8: '星期天上午',
        }
        self.pm = {
            2: '星期一下午', 3: '星期二下午', 4: '星期三下午', 5: '星期四下午', 6: '星期五下午',
            7: '星期六下午', 8: '星期天下午',
        }
        self.Date_dict = {}

    def __call__(self, args, io):
        page_source = args['page_source_str']
        etree = html.etree
        tree = etree.HTML(page_source)
        infor_list = []
        for a in range(2, 9):
            td_am = tree.xpath('//*[@id="doctortime"]/div[1]/table//tr[2]/td[%s]/img/@title' % a)
            if td_am:
                times = self.am[a]
                innfor = times + " " + td_am[0]
                infor_list.append(innfor)
            td_pm = tree.xpath('//*[@id="doctortime"]/div[1]/table//tr[3]/td[%s]/img/@title' % a)
            if td_pm:
                times = self.pm[a]
                innfor = times + " " + td_pm[0]
                infor_list.append(innfor)

        self.Date_dict["outpatient_info"] = ','.join(infor_list)

        io.set_output('result_dict', self.Date_dict)
        pass



