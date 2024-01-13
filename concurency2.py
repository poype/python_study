import queue
import random
import threading
import time

import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 51)
]


def craw(url):
    r = requests.get(url)
    return r.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title")
    return [(link["href"], link.get_text()) for link in links]


def do_craw(url_queue: queue.Queue, html_queue: queue.Queue):
    while True:
        url = url_queue.get()
        html = craw(url)
        html_queue.put(html)
        print(threading.current_thread().name)
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: queue.Queue):
    while True:
        html = html_queue.get()
        results = parse(html)

        for result in results:
            print(result)

        print(threading.current_thread().name)
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in urls:
        url_queue.put(url)

    for i in range(3):
        t = threading.Thread(target=do_craw, args=(url_queue, html_queue))  # 生产者线程
        t.start()

    for i in range(3):
        t = threading.Thread(target=do_parse, args=(html_queue,))  # 消费者线程
        t.start()

# queue.Queue() 多线程之间的，线程安全的数据通信
