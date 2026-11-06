# 配套重写示例，非课程源码逐行转录。
# 仅解释，不关机或重启学习电脑。
commands = {"shutdown -h now": "Linux立即关机", "reboot": "Linux重启"}
for command, meaning in commands.items():
    print(command, "=>", meaning, "（未执行）")
