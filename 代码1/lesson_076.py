# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    response = requests.get(base + "/catalog", timeout=5)
    response.raise_for_status()
    items = response.json()["items"]
    print("请求 -> 响应 -> 解析 -> 保存候选:", len(items))
