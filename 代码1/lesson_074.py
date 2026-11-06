# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    from urllib.robotparser import RobotFileParser
    rules = RobotFileParser()
    rules.parse(requests.get(base + "/robots.txt", timeout=5).text.splitlines())
    print("catalog:", rules.can_fetch("StudyBot", base + "/catalog"))
    print("private:", rules.can_fetch("StudyBot", base + "/private"))
