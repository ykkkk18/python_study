# 配套重写示例，非课程源码逐行转录。
tasks = ["变量", "循环"]
tasks.append("函数")
tasks[0] = "类型"
removed = tasks.pop(1)
print(tasks, removed)
print([n * n for n in range(5) if n % 2 == 0])
