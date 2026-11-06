# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    agent = "PythonStudyClient/1.0"
    response = requests.get(base + "/echo", headers={"User-Agent": agent}, timeout=5)
    print("服务端收到:", response.json()["user_agent"])
