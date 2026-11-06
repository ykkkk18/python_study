# 配套重写示例，非课程源码逐行转录。
from multiprocessing import Process, Queue
def work(queue):
    queue.put(sum(range(1, 6)))
if __name__ == "__main__":
    queue = Queue()
    process = Process(target=work, args=(queue,))
    process.start()
    print("收到:", queue.get(timeout=10))
    process.join()
    queue.close()
    queue.join_thread()
