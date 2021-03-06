# # -*- coding: utf-8 -*-
# """
# copyright. AIIT
# created by LiQing.
# contact blacknepia@dingtail.com for more information
# contact blacknepia@dingtail.com for more information
# """
# from runtime.Action import Action
#
#
# class UrlJoint(Action):
#     """12306根据两个js文件，经行url的组成"""
#
#     def __call__(self, args, io):
#         import urllib.parse
#         import re
#         city_serial_dict = args['city_serial_dict']
#         co = args['result_dict']
#         data_time = args['data_time_str']
#         list_tran_no = []
#         list_url = []
#         for key, value in co.items():
#             for key, value in value.items():
#                 for i in value:
#                     didian = i['station_train_code']
#                     train_no = i['train_no']
#                     if train_no not in list_tran_no:
#                         list_tran_no.append(train_no)
#                         didian = re.findall(r'.*\((.*)\)', didian)[0].split('-')
#                         from_station_telecode = didian[0]
#                         to_station_telecode = didian[1]
#                         depart_date = data_time
#                         try:
#                             from_station_telecode = city_serial_dict[from_station_telecode]
#                             to_station_telecode = city_serial_dict[to_station_telecode]
#                             data = {
#                                 'train_no': train_no,
#                                 'from_station_telecode': from_station_telecode,
#                                 'to_station_telecode': to_station_telecode,
#                                 'depart_date': depart_date,
#                             }
#                             query_string = urllib.parse.urlencode(data)
#                             url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?' + query_string
#                             if url not in list_url:
#                                 io.set_output('url_str', url)
#                                 io.push_event('Out')
#                                 list_url.append(url)
#                         except:
#                             continue
#
#     id = '76fc0440-e968-11e9-952a-8cec4bd887f3'
#
#
# class CkdXpath(Action):
#     """ckd页面所需要的所有xpath"""
#
#     def __call__(self, args, io):
#         xpath_dict = {
#
#             '病人姓名': '//*[@id="tr_101"]/span[2]/input/@value',
#             '性别': '//*[@id="tr_102"]/span[2]/label[1]/text()',
#             '病人编号': '//*[@id="P103"]/@value',
#             '职业': '//*[@id="P104"]/@value',
#             '身份证号': '//*[@id="P108"]/@value',
#             '原发病': '//*[@id="P1181"]/@value',
#         }
#
#         io.set_output('xpath_dict', xpath_dict)
#         io.push_event('Out')
#
#     id = 'd65c8ed8-ec93-11e9-9106-8cec4bd887f3'
#
#
# class Ckdneedxpath(Action):
#     """CKD 根据输入的字段，选取需要的xpath"""
#
#     def __call__(self, args, io):
#         xpath_dict = args['xpath_dict']
#         xpathtitle_list = args['xpath_list']
#         needxpath_dict = {}
#         for key in xpathtitle_list:
#             if xpath_dict[key]:
#                 needxpath_dict[key] = xpath_dict[key]
#         io.set_output('needxpath_dict', needxpath_dict)
#         io.push_event('Out')
#
#     id = 'bc8f2f34-ee2f-11e9-a5b3-8cec4bd887f3'
#
# class InHosxpath(Action):
#     '''入院记录页面所需要的xpath'''
#     def __call__(self, args,io):
#         xpath_dict = {
#
#            }
#         io.set_output('xpath_dict', xpath_dict)
#         io.push_event('Out')
#
#     id = '8ce0e1d2-f3e9-11e9-be00-8cec4bd887f3'
#
# class OutHosxpath(Action):
#     '''出院记录页面所需要的xpath'''
#     def __call__(self, args,io):
#         xpath_dict = {
#
#            }
#         io.set_output('xpath_dict', xpath_dict)
#         io.push_event('Out')
#
#     id = 'e622f512-f3e9-11e9-9c40-8cec4bd887f3'
#
# class StandingOrderxpath(Action):
#     '''长期医嘱单所需要的xpath'''
#     def __call__(self, args,io):
#         xpath_dict = {
#
#            }
#         io.set_output('xpath_dict', xpath_dict)
#         io.push_event('Out')
#
#     id = '2f96e41c-f467-11e9-bd94-8cec4bd887f3'
#
# class ProgressNotexpath(Action):
#     '''病程记录所需要的xpath'''
#     def __call__(self, args,io):
#         xpath_dict = {
#            }
#         io.set_output('xpath_dict', xpath_dict)
#         io.push_event('Out')
#
#     id = '00b7db9c-f468-11e9-8c34-8cec4bd887f3'
#
# class Reportxpath(Action):
#     '''报告查询xpath
#         报告查询中有四种报告，
#         每种报告需要的xpath都不同'''
#     def __call__(self, args, io):
#         url = args['url_str']
#         xpath_dict = {}
#         parames_one = args['paraames_one_str']
#         parames_two = args['paraames_two_str']
#         parames_three = args['paraames_three_str']
#         parames_four = args['paraames_four_str']
#
#         # if '151600'in url:
#         if parames_one in url:
#             xpath_dict = {
#                 '首页':'/html/body/div[3]/div/ul/li[1]/a/text()'
#             }
#         # if '812' in url:
#         if parames_two in url:
#             xpath_dict = {
#                 '药品': '/html/body/div[3]/div/ul/li[2]/a/text()'
#             }
#         # if '867' in url:
#         if parames_three in url:
#             xpath_dict = {
#                 '非药品': '/html/body/div[3]/div/ul/li[3]/a/text()',
#                 '美肤商场':'/html/body/div[3]/div/li/ul/li[3]/a/text()'
#             }
#         # if '155' in url:
#         if parames_four in  url:
#             xpath_dict = {
#                 '男科中心': '/html/body/div[3]/div/ul/li[4]/a/text()'
#             }
#         io.set_output('xpath_dict', xpath_dict)
#         io.push_event('Out')
#
#     id = '29cf0600-f477-11e9-8b14-8cec4bd887f3'
#
#
