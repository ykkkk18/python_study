# 配套重写示例，非课程源码逐行转录。
from threading import Thread, Lock
counter = 0
lock = Lock()
def increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1
threads = [Thread(target=increment) for _ in range(2)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)
