# 配套重写示例，非课程源码逐行转录。
import ast
print(int("12"), float("3.5"), str(7))
print(tuple([1, 2]), list((3, 4)), chr(65))
print(ast.literal_eval("[1, 2, 3]"))
# 不对用户输入使用 eval；结构化数据可用 json。
