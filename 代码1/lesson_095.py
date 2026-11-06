# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    print("未登录:", requests.get(base + "/private", timeout=5).status_code)
    response = requests.get(base + "/private", cookies={"session": "demo"}, timeout=5)
    print("演示会话:", response.status_code, response.json())
