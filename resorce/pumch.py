import re
from datetime import datetime
import time
from asyncio import Queue
import aiohttp
import asyncio

from fake_useragent import UserAgent
from pyquery import PyQuery as pq


sleep_interval = 0.1


def get_department_url(base_url):
    try:
        doc = pq(base_url)
        urls = doc('div.box.clearfix > div > div > div.h2 > a').items()
        return urls
    except Exception as e:
        print(e)

def is_first_level_url(url):
    if re.search('department', url, re.S):
        return True
    return False


class Crawler:
    def __init__(self, departments, max_tries=4, max_tasks=10, _loop=None):
        self.loop = _loop or asyncio.get_event_loop()
        self.headers = {}
        self.max_tries = max_tries
        self.max_tasks = max_tasks
        self.urls_queue = Queue(loop=self.loop)
        self.seen_urls = set()
        self.session = aiohttp.ClientSession(loop=self.loop)
        for item in departments:
            url = 'https://www.pumch.cn' + item.attr('href')
            self.urls_queue.put_nowait(url)

        self.start_at = datetime.now()
        self.end_at = None

    async def close(self):
        await self.session.close()

    @staticmethod
    async def fetch(response):
        if response.status == 200:
            text = await response.text()
            doc = pq(text)
            return doc

    def parse_first_etree(self, doc):
        doctor_urls = doc('#datalist > div.list.clearfix a').items()
        for url in doctor_urls:
            second_level_url = 'https://www.pumch.cn' + url.attr('href')
            # print(second_level_url)
            self.urls_queue.put_nowait(second_level_url)

    def parse_second_etree(self, doc):
        name = doc('div.text-box > div.dorname > div.title1').text()
        print(name)

    async def handle(self, url):
        tries = 0
        while tries < self.max_tries:
            try:
                self.headers['User-Agent'] = UserAgent(verify_ssl=False).chrome
                response = await self.session.get(url, headers=self.headers, allow_redirects=False)
                break
            except aiohttp.ClientError as e:
                print(repr(e))
            tries += 1
            print("try {}: {}".format(tries, url))
        try:
            doc = await self.fetch(response)
            if is_first_level_url(url):
                print("first_level: {}".format(url))
                self.parse_first_etree(doc)
            else:
                print("second level: {}".format(url))
                self.parse_second_etree(doc)
        finally:
            await response.release()

    async def work(self):
        try:
            while True:
                url = await self.urls_queue.get()
                await self.handle(url)
                time.sleep(sleep_interval)
                self.urls_queue.task_done()
        except asyncio.CancelledError as e:
            pass

    async def run(self):
        workers = [asyncio.ensure_future(self.work(), loop=self.loop)
                   for _ in range(self.max_tasks)]
        await self.urls_queue.join()
        for w in workers:
            w.cancel()
        self.end_at = datetime.now()

if __name__ == '__main__':
    base_url = 'https://www.pumch.cn/doctors.html'
    departments = get_department_url(base_url)
    loop = asyncio.get_event_loop()
    crawler = Crawler(departments, max_tasks=100)
    loop.run_until_complete(crawler.run())
    # print(content)
    crawler.close()
    print(crawler.end_at -crawler.start_at)
    loop.close()
