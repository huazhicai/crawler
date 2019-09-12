import aiohttp
import asyncio
from queue import Queue
import requests
import time
from pyquery import PyQuery as pq

q1 = Queue()
q2 = Queue()

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(encoding='utf-8')

async def main(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        return q1.put(html)

def parser(html):
    doc = pq(html)
    urls = doc('#m1 > div > div.box.clearfix div.h2 > a').items()
    urls = [x.attr('href') for x in urls]
    return urls

def parse_url(html):
    doc = pq(html)
    urls = doc('#datalist > div.list.clearfix > div > a').items()
    # print([url.attr('href') for url in urls])
    return [q2.put(url.attr('href')) for url in urls]

def parse_name(html):
    doc = pq(html)
    name = doc('div.text-box > div.dorname > div.title1').text()
    print(name)

if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    html = requests.get('https://www.pumch.cn/doctors.html').text
    tasks = [main('https://www.pumch.cn'+url) for url in parser(html)]
    loop.run_until_complete(asyncio.wait(tasks))
    while not q1.empty():
        # print(q.get())
        parse_url(q1.get())
    loop = asyncio.get_event_loop()
    task = [main('https://www.pumch.cn'+url) for url in q2.get()]
    loop.run_until_complete(asyncio.wait(task))
    while not q1.empty():
        # print(q1.get())
        parse_name(q1.get())
    end = time.time()
    print(end-start)