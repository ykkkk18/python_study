# 配套重写示例，非课程源码逐行转录。
categories = {"通用爬虫": "广泛收集", "聚焦爬虫": "限定主题", "增量爬虫": "仅处理新增数据"}
known = {1, 2}
incoming = [2, 3, 4]
print(categories)
print("新增:", [item for item in incoming if item not in known])
