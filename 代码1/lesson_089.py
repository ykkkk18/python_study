# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    # 使用本地自制字节演示二进制保存，不下载商业歌曲。
    response = requests.get(base + "/media", timeout=5)
    response.raise_for_status()
    print("收到二进制:", response.content.decode())
    print("这是演示字节，不是真实音频")
