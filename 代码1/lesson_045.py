# 配套重写示例，非课程源码逐行转录。
from multiprocessing import Process
def work():
    print("子进程完成")
if __name__ == "__main__":
    process = Process(target=work)
    process.start()
    process.join(timeout=10)
    print("已结束:", not process.is_alive(), "退出码:", process.exitcode)
