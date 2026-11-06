# 配套重写示例，非课程源码逐行转录。
from urllib.parse import urlsplit
for url in ["http://example.test/a", "https://example.test/a"]:
    parts = urlsplit(url)
    print(parts.scheme, parts.hostname, parts.path)
print("HTTPS在HTTP传输外提供TLS保护；本地演示服务使用HTTP")
