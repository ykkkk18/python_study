# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    items = []
    for page in range(1, 4):
        response = requests.get(base + "/catalog", params={"page": page}, timeout=5)
        response.raise_for_status()
        items.extend(response.json()["items"])
    print("总数:", len(items), "ID:", [row["id"] for row in items])
