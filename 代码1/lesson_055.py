# 配套重写示例，非课程源码逐行转录。
import os
from tempfile import TemporaryDirectory
with TemporaryDirectory() as folder:
    path = os.path.join(folder, "notes")
    os.mkdir(path)
    print(os.path.isdir(path), os.listdir(folder))
