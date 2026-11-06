# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    from urllib.parse import urlencode
    params = {"q": "中文", "page": 2}
    first = requests.get(base + "/echo", params=params, timeout=5).json()
    second = requests.get(base + "/echo?" + urlencode(params), timeout=5).json()
    print(first["query"] == second["query"], first["query"])
