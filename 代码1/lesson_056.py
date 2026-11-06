# 配套重写示例，非课程源码逐行转录。
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    root = Path(folder)
    source = root / "old.txt"
    source.write_text("demo", encoding="utf-8")
    target = source.rename(root / "new.txt")
    print(target.name, target.suffix, target.exists())
