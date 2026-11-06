# 配套重写示例，非课程源码逐行转录。
import sys
print("参数:", sys.argv[1:])
print("主版本:", sys.version_info.major)
print("搜索路径是列表:", isinstance(sys.path, list))
