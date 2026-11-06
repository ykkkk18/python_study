# 配套重写示例，非课程源码逐行转录。
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    path = Path(folder) / "notes.zip"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("note.txt", "学习Python")
    with zipfile.ZipFile(path) as archive:
        print(archive.namelist())
        print(archive.read("note.txt").decode("utf-8"))
