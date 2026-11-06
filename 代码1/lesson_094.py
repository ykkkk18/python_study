# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    response = requests.post(base + "/echo", json={"name": "小林"}, timeout=5)
    response.raise_for_status()
    print(response.json())
