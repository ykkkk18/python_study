# 配套重写示例，非课程源码逐行转录。
import gevent
events = []
def work(name):
    events.append(name + "开始")
    gevent.sleep(0)
    events.append(name + "结束")
gevent.joinall([gevent.spawn(work, "A"), gevent.spawn(work, "B")])
print(events)
