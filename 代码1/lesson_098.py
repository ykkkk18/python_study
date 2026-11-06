# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    # 只有本地虚构会话，不读取浏览器cookie。
    with requests.Session() as first, requests.Session() as second:
        first.post(base + "/login", timeout=5)
        print("会话1:", first.get(base + "/private", timeout=5).status_code)
        print("会话2:", second.get(base + "/private", timeout=5).status_code)
