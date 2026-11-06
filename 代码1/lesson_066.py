# 配套重写示例，非课程源码逐行转录。
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
with TemporaryDirectory() as folder:
    root = Path(folder)
    (root / "a.txt").write_text("Python", encoding="utf-8")
    shutil.copyfile(root / "a.txt", root / "b.txt")
    print("复制结果:", (root / "b.txt").read_text(encoding="utf-8"))
