from runtime.Action import Action
from fake_useragent import UserAgent
import requests
from retrying import retry
import time


# class RequestUrl(Action):
#     """
#     直接发送request请求
#     """
#     def __init__(self):
#         self.headers = {}
#
#     def __call__(self, args, io):
#         url = args['url_str']
#         headers = self.headers
#         headers['User-Agent'] = UserAgent(verify_ssl=False).random
#         re = requests.get(url=url, headers=headers)
#         Content = re.text
#         if re.status_code == 200 and len(Content) > 0:
#             io.set_output('response_str', Content)
#             io.push_event('Out')
#         else:
#             self.__call__(args, io)
#
#
# class RequestUrl_Charset(Action):
#     """
#     需要带encoding,发送reques请求
#     """
#
#     def __init__(self):
#         self.headers = {
#             'User-Agent': ''}
#
#     def __call__(self, args, io):
#         url = args['url_str']
#         headers = self.headers
#         headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
#         re = requests.get(url=url, headers=headers)
#         time.sleep(1)
#         Charset = args['charset_str']
#         re.encoding = Charset
#         Content = re.text
#         if re.status_code == 200 and len(Content) > 0:
#             io.set_output('response_str', Content)
#             io.push_event('Out')
#         else:
#             self.__call__(args, io)


class GetText(Action):
    """
    发送get请求，返回text(文本)内容;
    retry: 默认重新请求5次
    """
    def __call__(self, args, io):
        url = args['url_str']
        charset = args.get('charset_optional_str', None)
        params = args.get('params_optional_dict', None)
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        response = requests.get(url, headers=headers, params=params)
        if charset:
            response.encoding = charset
        text = response.text
        if response.status_code == 200 and len(text) > 0:
            io.set_output('response_str', text)
            io.push_event('Out')
        else:
            # self.__call__(args, io)
            io.set_output('response_str', '请求失败：{}'.format(response.status_code))
            io.push_event('Out')


class GetContent(Action):
    """发送get请求，返回二进制内容"""
    def __call__(self, args, io):
        url = args['url_str']
        charset = args.get('charset_optional_str', None)
        params = args.get('params_optional_dict', None)
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        response = requests.get(url, headers=headers, params=params)
        if charset:
            response.encoding = charset
        content = response.content
        if response.status_code == 200 and len(content) > 0:
            io.set_output('response_str', content)
            io.push_event('Out')
        else:
            # self.__call__(args, io)
            io.set_output('response_str', '请求失败：{}'.format(response.status_code))
            io.push_event('Out')


class GetJson(Action):
    """发送get请求，返回json内容"""
    def __call__(self, args, io):
        url = args['url_str']
        charset = args.get('charset_optional_str', None)
        params = args.get('params_optional_dict', None)
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        response = requests.get(url, headers=headers, params=params)
        if charset:
            response.encoding = charset
        json = response.json()
        if response.status_code == 200 and len(json) > 0:
            io.set_output('response_dict', json)
            io.push_event('Out')
        else:
            # self.__call__(args, io)
            io.set_output('response_str', '请求失败：{}'.format(response.status_code))
            io.push_event('Out')


class PostText(Action):
    """发送post请求，返回text(文本)内容"""
    def __call__(self, args, io):
        url = args['url_str']
        charset = args.get('charset_optional_str', None)
        data = args.get('data_dict')
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        response = requests.post(url, headers=headers, data=data)
        if charset:
            response.encoding = charset
        text = response.text
        if response.status_code == 200 and len(text) > 0:
            io.set_output('response_str', text)
            io.push_event('Out')
        else:
            # self.__call__(args, io)
            io.set_output('response_str', '请求失败：{}'.format(response.status_code))
            io.push_event('Out')


class PostJson(Action):
    """发送post请求，返回json内容"""
    def __call__(self, args, io):
        url = args['url_str']
        charset = args.get('charset_optional_str', None)
        data = args.get('data_dict')
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        response = requests.post(url, headers=headers, data=data)
        if charset:
            response.encoding = charset
        json = response.json()
        if response.status_code == 200 and len(json) > 0:
            io.set_output('response_dict', json)
            io.push_event('Out')
        else:
            # self.__call__(args, io)
            io.set_output('response_str', '请求失败：{}'.format(response.status_code))
            io.push_event('Out')
