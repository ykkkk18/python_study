# 配套重写示例，非课程源码逐行转录。
from threading import Thread
results = [None, None]
def work(index):
    results[index] = f"任务{index + 1}完成"
threads = [Thread(target=work, args=(i,)) for i in range(2)]
for t in threads: t.start()
for t in threads: t.join()
print(results)
