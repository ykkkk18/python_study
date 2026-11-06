# 配套重写示例，非课程源码逐行转录。
import re
match = re.fullmatch(r"(?P<year>\d{4})-(?P<month>\d{2})", "2026-11")
print(match.groupdict())
print(bool(re.fullmatch(r"(\w+)-\1", "go-go")))
