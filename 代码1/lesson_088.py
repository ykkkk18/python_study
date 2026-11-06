# 配套重写示例，非课程源码逐行转录。
import requests
from code_support import local_server
with local_server() as base:
    from pathlib import Path
    from tempfile import TemporaryDirectory
    response = requests.get(base + "/image", timeout=5)
    response.raise_for_status()
    with TemporaryDirectory() as folder:
        path = Path(folder) / "demo.svg"
        path.write_bytes(response.content)
        print(path.name, "包含SVG:", b"<svg" in path.read_bytes())
