# 配套重写示例，非课程源码逐行转录。
text = "  python,python,java  "
cleaned = text.strip().replace("java", "SQL")
print(cleaned.split(","))
print(cleaned.find("SQL"), "123".isdigit())
