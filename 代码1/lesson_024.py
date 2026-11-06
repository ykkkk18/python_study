# 配套重写示例，非课程源码逐行转录。
for text in ["12", "错误"]:
    try:
        print(int(text))
    except ValueError:
        print("请输入整数")
    finally:
        print("本次转换结束")
