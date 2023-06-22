# author:孔德昱
# datetime:2023/5/17 16:53
"""
description：
"""

from pojo.title import Title


class Paper:
    def __init__(self, title=None, questions=None):
        if title is None:
            self.title = Title()
        else:
            self.title = title
        if questions is None:
            self.questions = []
        else:
            self.questions = questions

    def __str__(self):
        result = str(self.title) + '\n题目: \n'
        for question in self.questions:
            result += str(question)
        return result

    # 将该试卷对象转化为对应的字符串，用于写入文件
    def to_text(self):
        result = self.title.to_text() + '\n'

        # 为每一个问题添加题号，同时为第一个选择题、填空题、判断题、简答题添加题目类型
        first_choice = False
        first_fill = False
        first_judge = False
        first_short = False
        for i in range(len(self.questions)):
            # 判断是否为第一个题型
            if self.questions[i].type == "选择题" and not first_choice:
                result += "一、选择题\n"
                first_choice = True
            elif self.questions[i].type == "填空题" and not first_fill:
                result += "\n二、填空题\n"
                first_fill = True
            elif self.questions[i].type == "判断题" and not first_judge:
                result += "\n三、判断题\n"
                first_judge = True
            elif self.questions[i].type == "简答题" and not first_short:
                result += "\n四、简答题\n"
                first_short = True
            # 为每一个问题添加题号
            result += f"{i + 1}、{self.questions[i].to_text()}"
        return result
