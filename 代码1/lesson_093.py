# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
class CatalogClient:
    def __init__(self, base):
        self.base = base
    def fetch(self, page):
        response = requests.get(self.base + "/catalog", params={"page": page}, timeout=5)
        response.raise_for_status()
        return response.json()["items"]
with local_server() as base:
    client = CatalogClient(base)
    print(client.fetch(2))
