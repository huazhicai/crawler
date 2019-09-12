from runtime.Action import Action
from fake_useragent import UserAgent
import aiohttp
import asyncio

class Asyncop_url(Action):
    def __init__(self):
        self.headers = {
            'User-Agent': ''}

    async def fetch(self,session,url,charset):
        headers = self.headers
        headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
        async with session.get(url,headers=headers) as response:
            response.encoding = charset
            return await response.text()

    async def main(self,url,charset):
        async with aiohttp.ClientSession() as session:
            html = await self.fetch(session, url,charset)
            await asyncio.sleep(2)
            return html

    def __call__(self, args, io):
        url_list = args['url_list']
        charset = args['charset_str']
        tasks = [self.main(url,charset) for url in url_list]
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        con_list = loop.run_until_complete(asyncio.gather(*tasks))
        loop.close()
        for content in con_list:
            io.set_output('response_str', content)
            io.push_event('Out')




