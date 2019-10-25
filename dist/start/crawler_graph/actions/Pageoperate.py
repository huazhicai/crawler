# -*- coding: utf-8 -*-
from runtime.Action import Action
import asyncio


class Pagetype(Action):
    """
    通过pyppeteer的page对象 找到输入框并输入文本
    """

    async def pagetype(self, args, io):
        await asyncio.sleep(1)
        page = args['page_str']
        type_css = args['type_css_str']
        content = args['content_str']
        while not await page.querySelector(type_css):
            pass
        await page.type(type_css, content)
        io.set_output('page_str', page)

    def __call__(self, args, io):

        asyncio.get_event_loop().run_until_complete(
            self.pagetype(args, io))

        io.push_event('Out')

    id = '573050c6-eb03-11e9-9543-8cec4bd887f3'


class Pageclick(Action):
    """
    通过pyppeteer的page对象 找到输入框并输入文本
    """

    async def pagetype(self, args, io):
        page = args['page_str']
        click_css = args['click_css_str']
        while not await page.querySelector(click_css):
            pass
        try:
            await asyncio.gather(
                page.click(click_css),
                page.waitForNavigation(),
            )
        except:
            await page.click(click_css)
            await asyncio.sleep(1)

        io.set_output('page_str', page)

    def __call__(self, args, io):
        print('----')
        asyncio.get_event_loop().run_until_complete(
            self.pagetype(args, io))
        io.push_event('Out')

    id = 'd84b0266-ebc9-11e9-a303-8cec4bd887f3'


class Pagecookie(Action):
    """
    通过page登录后，获取当前登录页面的cookie值
    """

    async def pagecookie(self, args, io):
        page = args['page_str']
        cookie = await page.cookies()

        io.set_output('cookie_list', cookie)
        io.set_output('page_str', page)

    def __call__(self, args, io):
        asyncio.get_event_loop().run_until_complete(
            self.pagecookie(args, io))

        io.push_event('Out')

    id = 'ee8e7f58-eb30-11e9-8551-8cec4bd887f3'


class Pagecontent(Action):
    """
    通过page，获取页面源代码
    """

    async def pagecontent(self, args, io):
        page = args['page_str']
        doc = await page.content()
        io.set_output('doc_str', doc)

    def __call__(self, args, io):
        asyncio.get_event_loop().run_until_complete(
            self.pagecontent(args, io))
        io.push_event('Out')

    id = 'a639d25a-eb3d-11e9-a625-8cec4bd887f3'


class Pagepulldown(Action):
    """
    通过page，将页面滚动到页面底部
    """

    async def pagepulldown(self, args, io):
        page = args['page_str']
        await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
        # await asyncio.sleep(1)
        io.set_output('page_str', page)

    def __call__(self, args, io):
        asyncio.get_event_loop().run_until_complete(
            self.pagepulldown(args, io))
        io.push_event('Out')

    id = '484da1a2-ebef-11e9-898d-8cec4bd887f3'


class PageClose(Action):

    async def pageclose(self, args):
        page = args['broswer_str']
        await page.close()

    def __call__(self, args, io):
        asyncio.get_event_loop().run_until_complete(
            self.pageclose(args))

    id = 'effc5424-ec0c-11e9-921c-8cec4bd887f3'
