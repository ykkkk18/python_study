# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    response = requests.get(base + "/echo", headers={"User-Agent": "StudyBot/1.0"}, timeout=5)
    print(response.json()["user_agent"])
