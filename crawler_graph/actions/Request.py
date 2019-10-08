# -*- coding: utf-8 -*-
from runtime.Action import Action
from fake_useragent import UserAgent
import requests
import aiohttp
import asyncio


class GetRequestPro(Action):
    '''具有‘阿布云’代理ip接口'''

    def __call__(self, args, io):
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        url = args['url_str']
        Charset = args['charset_str']
        # 要访问的目标页面
        targetUrl = url
        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"
        # 代理隧道验证信息
        proxyUser = args['proxyuser_str']
        proxyPass = args['proxyPass_str']
        proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }
        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        if proxyHost and proxyPass:
            proxies = proxies
        else:
            proxies = None
        re = requests.get(targetUrl, headers=headers, proxies=proxies)
        if Charset: re.encoding = Charset
        content = re.text
        if re.status_code == 200:
            io.set_output('response_str', content)
            io.push_event('Out')
        else:
            self.__call__(args, io)

    id = 'ded1fcae-e968-11e9-8c95-8cec4bd887f3'


class GetRequest(Action):
    """
    发送get请求，根据response_type返回数据类型内容;
    retry: 默认重新请求5次
    """

    def __call__(self, args, io):
        url = args['url_str']
        charset = args.get('charset_optional_str', None)  # 可选参数
        cookies = args['cookie_optional_dict']
        response_type = args.get('resp_type_optional_str')  # 返回的数据类型

        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        if cookies: headers.update(cookies)

        tries = 0
        while tries < 4:
            try:
                response = requests.get(url, headers=headers)
                if charset:
                    response.encoding = charset
                if response_type and response_type.lower().strip() == 'json':
                    resp = response.json()
                elif response_type and response_type.lower().strip().startswith('byte'):
                    resp = response.content
                else:
                    resp = response.text
                if response.status_code == 200:
                    io.set_output('response', resp)  # 参数无后缀，默认任意数据类型
                    io.push_event('Out')
                break
            except requests.RequestException as e:
                tries += 1
                print('post failed {}: {}'.format(tries, e))

    id = 'e8dc0bb4-e968-11e9-8b25-8cec4bd887f3'


class PostRequest(Action):
    """发送post请求，根据response_type 返回数据类型"""

    def __call__(self, args, io):
        url = args['url_str']
        data = args['data_dict']
        charset = args.get('charset_optional_str', None)
        cookies = args.get('cookie_optional_dict', None)
        response_type = args.get('responseType_optional_str')

        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        if cookies:
            headers.update(cookies)

        tries = 0
        while tries < 4:
            try:
                response = requests.post(url, headers=headers, data=data)
                if charset:
                    response.encoding = charset
                if response_type and response_type.lower().strip() == 'json':
                    resp = response.json()
                elif response_type and response_type.lower().strip().startswith('byte'):
                    resp = response.content
                else:
                    resp = response.text
                if response.status_code == 200:
                    io.set_output('response', resp)
                    io.push_event('Out')
                break
            except requests.RequestException as e:
                tries += 1
                print('post failed {}: {}'.format(tries, e))

    id = '13028f7e-e969-11e9-a4fc-8cec4bd887f3'


class CoroutinesRequests(Action):
    '''通过gevent协程发送requests请求'''

    def __init__(self):
        self.headers = {
            'User-Agent': ''
        }
        self.Charset = ''

    def req(self, url, io):
        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        re = requests.get(url=url, headers=self.headers)
        re.encoding = self.Charset
        Content = re.text
        if re.status_code == 200 and len(Content) > 0:
            io.set_output('Content', Content)
            io.push_event('Out')
        else:
            print("未渲染成功")
            self.req(url, io)

    def __call__(self, args, io):
        import gevent
        urls = args['url_list']
        if urls:
            self.Charset = args['charset_str']
            gevent.joinall([gevent.spawn(self.req, url, io, ) for url in urls])

    id = '19acd034-e969-11e9-be8d-8cec4bd887f3'


class Asyncop_url(Action):

    def __init__(self):
        self.headers = {
            'User-Agent': ''}

    async def fetch(self, session, url, charset):
        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        try:
            async with session.get(url, headers=headers) as response:
                response.encoding = charset
                return await response.text()
        except:
            print(' Cannot connect to host')

    async def main(self, url, charset):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, url, charset)
            # await asyncio.sleep(2)
            return html

    def __call__(self, args, io):

        url_list = args['url_list']
        charset = args['charset_str']
        if url_list:
            tasks = [self.main(url, charset) for url in url_list]
            asyncio.set_event_loop(asyncio.new_event_loop())
            loop = asyncio.get_event_loop()
            con_list = loop.run_until_complete(asyncio.gather(*tasks))
            loop.close()
            for content in con_list:
                io.set_output('response_str', content)
                io.push_event('Out')

    id = '1f3c7766-e969-11e9-915c-8cec4bd887f3'


class GetRequestPro_Aiohttp(Action):
    '''具有‘阿布云’代理ip接口,通过Aiohttp请求方式'''

    def __call__(self, args, io):
        url = args['url_str']
        targetUrl = url
        # 代理服务器
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"
        # 代理隧道验证信息
        proxyUser = "HX18ZZ42001605OD"
        proxyPass = "F5FAF0A29BC584A3"

        proxyServer = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
            "host": proxyHost,
            "port": proxyPort,
            "user": proxyUser,
            "pass": proxyPass,
        }
        userAgent = "curl/7.x/line"

        async def entry():
            conn = aiohttp.TCPConnector(verify_ssl=False)
            async with aiohttp.ClientSession(headers={"User-Agent": userAgent}, connector=conn) as session:
                async with session.get(targetUrl, proxy=proxyServer) as resp:
                    body = await resp.read()
                    if resp.status == 200 and len(body) > 0:
                        loop = asyncio.get_event_loop()
                        loop.run_until_complete(entry())
                        loop.run_forever()
                        io.set_output('response_str', body)
                        io.push_event('Out')
                    else:
                        self.__call__(args, io)

    id = '27f2614c-e969-11e9-bada-8cec4bd887f3'


class PyQueryUrl(Action):
    '''通过PyQuery发送请求'''

    def __call__(self, args, io):
        from pyquery import PyQuery
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

    id = '2ea8f46c-e969-11e9-ba99-8cec4bd887f3'
