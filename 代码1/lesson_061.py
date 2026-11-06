# 配套重写示例，非课程源码逐行转录。
import logging
from io import StringIO
buffer = StringIO()
handler = logging.StreamHandler(buffer)
handler.setFormatter(logging.Formatter("%(name)s|%(levelname)s|%(message)s"))
logger = logging.getLogger("study")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.propagate = False
logger.info("完成任务")
print(buffer.getvalue().strip())
