# 配套重写示例，非课程源码逐行转录。
from queue import Queue
from threading import Thread
queue = Queue()
def produce():
    for i in range(3): queue.put(i)
    queue.put(None)
thread = Thread(target=produce)
thread.start()
items = []
while True:
    item = queue.get()
    if item is None: break
    items.append(item)
thread.join()
print(items)
