# 配套重写示例，非课程源码逐行转录。
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    root = Path(folder)
    (root / "practice").mkdir()
    print("mkdir效果:", (root / "practice").is_dir())
    print("ls效果:", [x.name for x in root.iterdir()])
