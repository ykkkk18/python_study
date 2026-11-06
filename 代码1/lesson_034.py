# 配套重写示例，非课程源码逐行转录。
class TextReport:
    def render(self):
        return "文字报告"
class HtmlReport:
    def render(self):
        return "<h1>报告</h1>"
class Score:
    @staticmethod
    def valid(value):
        return 0 <= value <= 100
    @classmethod
    def kind(cls):
        return cls.__name__
print([r.render() for r in [TextReport(), HtmlReport()]])
print(Score.valid(90), Score.kind())
