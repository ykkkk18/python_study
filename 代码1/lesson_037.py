# 配套重写示例，非课程源码逐行转录。
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    path = Path(folder) / "note.txt"
    path.write_text("学习Python\n", encoding="utf-8")
    print(path.read_text(encoding="utf-8").strip())
