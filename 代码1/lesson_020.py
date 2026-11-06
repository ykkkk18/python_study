# 配套重写示例，非课程源码逐行转录。
def total(*values, discount=0, **metadata):
    return sum(values) - discount, metadata.get("owner", "匿名")
print(total(10, 20, discount=5, owner="小林"))
def append_item(value, items=None):
    if items is None:
        items = []
    items.append(value)
    return items
print(append_item(1), append_item(2))
