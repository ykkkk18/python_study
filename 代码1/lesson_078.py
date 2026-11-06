# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    response = requests.get(base + "/catalog?page=2", timeout=5)
    print("方法:", response.request.method)
    print("状态:", response.status_code)
    print("内容类型:", response.headers["Content-Type"])
    print("页码:", response.json()["page"])
