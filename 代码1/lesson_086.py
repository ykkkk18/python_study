# 配套重写示例，非课程源码逐行转录。
from urllib.parse import urlencode, quote, unquote
query = urlencode({"q": "Python 中文", "page": 2})
print(query)
print(unquote(quote("中文")))
