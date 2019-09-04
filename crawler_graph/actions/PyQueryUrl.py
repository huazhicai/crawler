# -*- coding: utf-8 -*-
"""
copyright. AIIT
created by LiQing.
created by LiQing
ccontact blacknepia@dingtail.com for more information
"""

from runtime.Action import Action
from pyquery import PyQuery


class PyQueryUrl(Action):

    def __call__(self, args, io):
        url = args['url_str']
        doc = PyQuery(url)
        fields = args['field_css_dict']
        result = {}
        for field, (selector, is_list, attr) in fields.items():
            item = doc(selector)

            if is_list:
                item = item.items()

                if attr:
                    result[field] = [ele.attr(attr) for ele in item]

                else:
                    result[field] = [ele.text() for ele in item]
            else:

                if attr:
                    result[field] = item.attr(attr)

                else:
                    result[field] = item.text()

        io.set_output('doc_str', doc)
        io.set_output('result_dict', result)
        io.push_event('Out')


class PyQueryFieldHelper(Action):

    def __call__(self, args, io):
        pass
