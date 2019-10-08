# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
contact blacknepia@dingtail.com for more information
contact blacknepia@dingtail.com for more information
"""
from runtime.Action import Action


class Url_joint(Action):
    '''12306根据两个js文件，经行url的组成'''

    def __call__(self, args, io):
        import urllib.parse
        import re
        city_serial_dict = args['city_serial_dict']
        co = args['result_dict']
        data_time = args['data_time_str']
        list_tran_no = []
        list_url = []
        for key, value in co.items():
            for key, value in value.items():
                for i in value:
                    didian = i['station_train_code']
                    train_no = i['train_no']
                    if train_no not in list_tran_no:
                        list_tran_no.append(train_no)
                        didian = re.findall(r'.*\((.*)\)', didian)[0].split('-')
                        from_station_telecode = didian[0]
                        to_station_telecode = didian[1]
                        depart_date = data_time
                        try:
                            from_station_telecode = city_serial_dict[from_station_telecode]
                            to_station_telecode = city_serial_dict[to_station_telecode]
                            data = {
                                'train_no': train_no,
                                'from_station_telecode': from_station_telecode,
                                'to_station_telecode': to_station_telecode,
                                'depart_date': depart_date,
                            }
                            query_string = urllib.parse.urlencode(data)
                            url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?' + query_string
                            if url not in list_url:
                                io.set_output('url_str', url)
                                io.push_event('Out')
                                list_url.append(url)
                        except:
                            continue

    id = '76fc0440-e968-11e9-952a-8cec4bd887f3'
