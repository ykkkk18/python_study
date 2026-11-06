# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    with requests.Session() as session:
        session.post(base + "/login", timeout=5).raise_for_status()
        response = session.get(base + "/private", timeout=5)
        print("会话自动携带cookie:", response.json()["authorized"])
