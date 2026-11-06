# 配套重写示例，非课程源码逐行转录。
import copy
original = [[1], [2]]
alias = original
shallow = copy.copy(original)
deep = copy.deepcopy(original)
original[0].append(9)
print(alias, shallow, deep)
print(alias is original, shallow is original)
