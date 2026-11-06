# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    from pathlib import Path
    from tempfile import TemporaryDirectory
    response = requests.get(base + "/catalog", timeout=5)
    with TemporaryDirectory() as folder:
        path = Path(folder) / "response.json"
        path.write_bytes(response.content)
        print("已保存:", path.name, "内容非空:", path.stat().st_size > 0)
