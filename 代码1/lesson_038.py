# 配套重写示例，非课程源码逐行转录。
from tempfile import TemporaryFile
with TemporaryFile(mode="w+b") as file:
    file.write(b"abcdef")
    file.seek(2)
    print(file.read(2).decode(), file.tell())
