# 配套重写示例，非课程源码逐行转录。
tax = 0.1
def price_with_tax(price):
    local_total = price * (1 + tax)
    return round(local_total, 2)
print(price_with_tax(100))
print(sorted([("甲", 80), ("乙", 95)], key=lambda row: row[1]))
