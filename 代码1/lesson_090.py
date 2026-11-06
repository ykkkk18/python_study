# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    with requests.get(base + "/media", stream=True, timeout=5) as response:
        response.raise_for_status()
        chunks = list(response.iter_content(chunk_size=4))
        print("分块数:", len(chunks), "字节数:", sum(map(len, chunks)))
    print("演示分块读取，不是真实MV")
