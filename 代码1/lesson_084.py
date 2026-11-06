# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    # 仅演示选择配置；不用于绕过站点限制。
    agents = ["StudyClient/Desktop", "StudyClient/Mobile"]
    for agent in agents:
        response = requests.get(base + "/echo", headers={"User-Agent": agent}, timeout=5)
        print(response.json()["user_agent"])
