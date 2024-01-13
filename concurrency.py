# 多进程 Process (multiprocessing), python中只有多进程可以利用多核CPU
# 多线程 Thread (threading), python中的线程不能利用多CPU
# 多协程 Corroutine (asyncio)， 支持库有限制，代码实现复杂


# 全局解释器锁 GIL
# Python比C++ 慢 100~200倍
# 慢的其中一个原因就是 GIL 无法利用多核CPU并发执行
# GIL： Global Interpreter Lock， 它使得任何时刻仅有一个线程在执行
# 即便在多核处理器上，使用GIL的解释器也只允许同一时间执行一个线程。

import requests
import threading
import time

urls = [
    f"https://www.cnblogs.com/#p{page}"
    for page in range(1, 51)
]


def craw(url):
    r = requests.get(url)
    print(url, len(r.text))


def single_thread():
    print("single_thread start")
    for url in urls:
        craw(url)
    print("single_thread end")


def multi_thread():
    print("multi_thread start")
    threads = []
    for url in urls:
        threads.append(
            threading.Thread(target=craw, args=(url,))  # 创建一个线程，target参数是目标方法，args是传给目标方法的参数
        )

    for thread in threads:
        thread.start()  # 开始线程

    for thread in threads:
        thread.join()

    print("multi_thread end")


if __name__ == '__main__':
    start = time.time()
    single_thread()
    end = time.time()
    print("Single thread cost: ", end - start, "seconds")

    start = time.time()
    multi_thread()
    end = time.time()
    print("Multi thread cost: ", end - start, "seconds")
