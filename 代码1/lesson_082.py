# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    response = requests.get(base + "/catalog", timeout=5)
    print(response.status_code, response.encoding, response.ok)
    print(type(response.text).__name__, type(response.content).__name__)
    print(response.json()["page"])
