# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    response = requests.get(base + "/catalog", timeout=5)
    print("客户端发送:", response.request.method)
    print("服务端返回:", response.status_code)
    print("Python请求不会自动执行网页JavaScript")
