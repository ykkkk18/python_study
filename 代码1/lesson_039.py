# 配套重写示例，非课程源码逐行转录。
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    path = Path(folder) / "中文.txt"
    with path.open("w", encoding="utf-8") as file:
        file.write("你好")
    print([f.name for f in Path(folder).iterdir()])
    print(path.read_text(encoding="utf-8"))
