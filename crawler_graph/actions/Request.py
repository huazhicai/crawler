# -*- coding: utf-8 -*-
from runtime.Action import Action
from fake_useragent import UserAgent
from pyppeteer import launch
import requests
import aiohttp
import asyncio


class GetRequestPro(Action):
    """具有‘阿布云’代理ip接口"""
    _id = 'ded1fcae-e968-11e9-8c95-8cec4bd887f3'
    node_info = {"args": [['url_str', 'String', 'ce69b238-f3a7-11e9-b6bb-8cec4bd887f3'],
                          ['charset_str', 'String', 'ce69b239-f3a7-11e9-bdb8-8cec4bd887f3'],
                          ['proxyuser_str', 'String', 'ce69b23a-f3a7-11e9-aef4-8cec4bd887f3'],
                          ['proxyPass_str', 'String', 'ce69b23b-f3a7-11e9-b28b-8cec4bd887f3'],
                          ['In', 'Event', 'ce69b23c-f3a7-11e9-8df4-8cec4bd887f3']],
                 "returns": [['response_str', 'String', 'ce69b23d-f3a7-11e9-a396-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b23e-f3a7-11e9-a069-8cec4bd887f3']]}

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
        # else:
        #     proxies = None
        re = requests.get(targetUrl, headers=headers, proxies=proxies)
        if Charset: re.encoding = Charset
        content = re.text
        if re.status_code == 200:
            io.set_output('response_str', content)
            io.push_event('Out')
        else:
            self.__call__(args, io)


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
        # if cookies: headers.update(cookies)

        retry_count = 4
        while retry_count > 0:
            try:
                response = requests.get(url, headers=headers, cookies=cookies)
                if response and response.status_code == 200:
                    if charset:
                        response.encoding = charset
                    if response_type and response_type.lower().strip() == 'json':
                        resp = response.json()
                    elif response_type and response_type.lower().strip().startswith('byte'):
                        resp = response.content
                    else:
                        resp = response.text
                    io.set_output('response', resp)  # 参数无后缀，默认任意数据类型
                    io.push_event('Out')
                    return
                else:
                    raise requests.RequestException
            except requests.RequestException as e:
                retry_count -= 1
                print('GetRequest failed {}: {}'.format(retry_count, e))
        if retry_count == 0:
            io.set_output('failUrl_str', url)
            io.push_event('Failed')

    id = 'e8dc0bb4-e968-11e9-8b25-8cec4bd887f3'


class PostRequest(Action):
    """发送post请求，根据response_type 返回数据类型"""
    _id = '13028f7e-e969-11e9-a4fc-8cec4bd887f3'

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


class CoroutinesRequests(Action):
    """通过gevent协程发送requests请求"""
    _id = '19acd034-e969-11e9-be8d-8cec4bd887f3'
    node_info = {"args": [['url_list', 'List', 'be723dbe-0066-11ea-8738-8cec4bd83f9f'],
                          ['charset_str', 'String', 'be72355f-0053-11ea-b7e0-8cec4bd83f9f'],
                          ['In', 'Event', 'be723dc0-0053-11ea-b171-8cec4bd45f9f']],
                 "returns": [['Content', 'String', 'be723dc1-1153-11ea-96d4-8cec4bd83f9f'],
                             ['Out', 'Event', 'be723dc2-0053-11ea-835b-8abc4bd83f9f']]}

    def __init__(self):
        self.headers = {'User-Agent': ''}
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


class Asyncop_url(Action):
    _id = '1f3c7766-e969-11e9-915c-8cec4bd887f3'
    node_info = {"args": [['url_list', 'List', 'ce69b253-f3a7-11e9-a357-8cec4bd887f3'],
                          ['charset_str', 'String', 'ce69b254-f3a7-11e9-a778-8cec4bd887f3'],
                          ['In', 'Event', 'ce69b255-f3a7-11e9-8433-8cec4bd887f3']],
                 "returns": [['response_str', 'String', 'ce69b256-f3a7-11e9-b5e2-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b257-f3a7-11e9-bfd8-8cec4bd887f3']]}

    def __init__(self):
        self.headers = {'User-Agent': ''}

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


class GetRequestPro_Aiohttp(Action):
    """具有‘阿布云’代理ip接口,通过Aiohttp请求方式"""
    _id = '27f2614c-e969-11e9-bada-8cec4bd887f3'

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


class PyQueryUrl(Action):
    """通过PyQuery发送请求"""
    _id = '2ea8f46c-e969-11e9-ba99-8cec4bd887f3'

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


class PyppeteerObject(Action):
    """实例化一个Pyppeteer 的page对象"""
    _id = 'cdc4cbba-eb00-11e9-943e-8cec4bd887f3'
    node_info = {"args": [['executablePath', 'String', 'ce69b262-f3a7-11e9-b716-8cec4bd887f3'],
                          ['In', 'Event', 'ce69b263-f3a7-11e9-a658-8cec4bd887f3']],
                 "returns": [['broswer_str', 'String', 'ce69b264-f3a7-11e9-bc65-8cec4bd887f3'],
                             ['page_str', 'String', 'ce69b265-f3a7-11e9-b383-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b266-f3a7-11e9-a4c0-8cec4bd887f3']]}

    # autoClose = False,
    async def createobject(self, io, args):
        executablePath = args['executablePath']
        broswer = await launch(headless=True, args=['--disable-infobars'], executablePath=executablePath)
        io.set_output('broswer_str', broswer)
        page = await broswer.newPage()
        return page

    def __call__(self, args, io):
        try:
            page = asyncio.get_event_loop().run_until_complete(
                self.createobject(io, args))
            io.set_output('page_str', page)
            io.push_event('Out')
        except Exception as e:
            print(e)


class PyppeteerGoto(Action):
    """通过pyppeteer的page对象模拟打开一个网页"""
    _id = 'd54c3a66-eb00-11e9-b459-8cec4bd887f3'
    node_info = {"args": [['page_str', 'String', 'ce69b267-f3a7-11e9-be08-8cec4bd887f3'],
                          ['login_url', 'String', 'ce69b268-f3a7-11e9-9a33-8cec4bd887f3'],
                          ['In', 'Event', 'ce69b269-f3a7-11e9-b21d-8cec4bd887f3']],
                 "returns": [['page_str', 'String', 'ce69b26a-f3a7-11e9-be26-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b26b-f3a7-11e9-a4c0-8cec4bd887f3']]}

    async def pagegoto(self, args, io):
        page = args['page_str']
        login_url = args['login_url']
        await page.setUserAgent(UserAgent(verify_ssl=False).random)
        await page.goto(login_url)
        # await page.waitForNavigation()
        # await asyncio.sleep(2)
        io.set_output('page_str', page)

    def __call__(self, args, io):
        asyncio.get_event_loop().run_until_complete(
            self.pagegoto(args, io))
        io.push_event('Out')


class SessionSetcookie(Action):
    _id = '56bacec0-ec08-11e9-b289-8cec4bd887f3'
    node_info = {"args": [['cookies_list', 'List', 'ce69b26c-f3a7-11e9-8ad0-8cec4bd887f3'],
                          ['cookies_dict', 'Dict', 'ebff8f8f-0050-11ea-8ba7-8cec4bd83f9f'],
                          ['In', 'Event', 'ce69b26d-f3a7-11e9-a091-8cec4bd887f3']],
                 "returns": [['ss_str', 'String', 'ce69b26e-f3a7-11e9-b240-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b26f-f3a7-11e9-949a-8cec4bd887f3']]}

    def __call__(self, args, io):
        cookies_list = args['cookies_list']
        cookies_dict = args['cookies_dict']
        import requests
        ss = requests.session()
        if cookies_list:
            for cookie in cookies_list:
                ss.cookies.set(cookie['name'], cookie['value'])
        if cookies_dict:
            for name, value in cookies_dict.items():
                ss.cookies.set(name, value)
        io.set_output('ss_str', ss)
        io.push_event('Out')


class SessionGeturl(Action):
    """通过session会话机制, 对登录后的页面进行访问"""
    _id = '5c7bd658-ec08-11e9-aa5f-8cec4bd887f3'
    node_info = {"args": [['ss_str', 'String', 'ce69b270-f3a7-11e9-a372-8cec4bd887f3'],
                          ['url_str', 'String', 'ce69b271-f3a7-11e9-a910-8cec4bd887f3'],
                          ['data_dict', 'Dict', 'ce69b272-f3a7-11e9-b3b0-8cec4bd887f3'],
                          ['In', 'Event', 'ce69b273-f3a7-11e9-b851-8cec4bd887f3']],
                 "returns": [['ss_str', 'String', 'ce69b274-f3a7-11e9-8b92-8cec4bd887f3'],
                             ['content_str', 'String', 'ce69b275-f3a7-11e9-ad5b-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b276-f3a7-11e9-8ef5-8cec4bd887f3']]}

    def __call__(self, args, io):
        ss = args['ss_str']
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        url = args['url_str']
        data = args['data_dict']
        if data:
            response = ss.get(url, headers=headers, params=data)
        else:
            response = ss.get(url, headers=headers)
        content = response.text
        io.set_output('ss_str', ss)
        io.set_output('content_str', content)
        io.push_event('Out')


class SessionPosturl(Action):
    """通过sessionhuihuajizhi，发post请求"""
    _id = 'c4db4bac-ee1e-11e9-8875-8cec4bd887f3'
    node_info = {"args": [['ss_str', 'String', 'ce69b277-f3a7-11e9-834e-8cec4bd887f3'],
                          ['url_str', 'String', 'ce69b278-f3a7-11e9-8889-8cec4bd887f3'],
                          ['data_dict', 'Dict', 'ce69b279-f3a7-11e9-a9b5-8cec4bd887f3'],
                          ['In', 'Event', 'ce69b27a-f3a7-11e9-8ae4-8cec4bd887f3']],
                 "returns": [['cookie_dict', 'Dict', 'ebff8f9e-0050-11ea-a245-8cec4bd83f9f'],
                             ['ss_str', 'String', 'ce69b27b-f3a7-11e9-b2a8-8cec4bd887f3'],
                             ['content_str', 'String', 'ce69b27c-f3a7-11e9-9f62-8cec4bd887f3'],
                             ['Out', 'Event', 'ce69b27d-f3a7-11e9-9d30-8cec4bd887f3']]}

    def __call__(self, args, io):
        ss = args['ss_str']
        headers = {'User-Agent': UserAgent(verify_ssl=False).random}
        url = args['url_str']
        data = args['data_dict']
        response = ss.post(url, headers=headers, params=data)
        longin_cookie = requests.utils.dict_from_cookiejar(response.cookies)
        io.set_output('cookie_dict', longin_cookie)
        io.set_output('ss_str', ss)
        io.set_output('content_str', response.text)
        io.push_event('Out')
