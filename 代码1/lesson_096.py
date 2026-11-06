# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    # 练习POST表单，不依赖可能变化的第三方翻译接口。
    response = requests.post(base + "/echo", data={"text": "hello", "target": "zh"}, timeout=5)
    print("提交表单:", response.json()["data"])
    print("此接口只回显表单，不提供真实翻译")
