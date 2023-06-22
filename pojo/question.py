# author:孔德昱
# datetime:2023/5/17 16:38
"""
description：
"""


class Question:
    def __init__(self, question_type=None, left_body=None, right_body=None, difficulty=None, topic=None, source=None,
                 options=None):
        if options is None:
            options = []
        self.left_body = left_body
        self.right_body = right_body
        self.type = question_type
        self.difficulty = difficulty
        self.topic = topic
        self.source = source
        self.options = options

    def __str__(self):
        if self.type == "选择题":
            return f"题目内容: {self.left_body}(  ){self.right_body}\n选项: {self.options}\n题目类型: {self.type}\n题目难度: {self.difficulty}\n" \
                   f"题目考点: {self.topic}\n\n"
        elif self.type == "填空题":
            return f"题目内容: {self.left_body}(  ){self.right_body}\n题目类型: {self.type}\n题目难度: {self.difficulty}\n" \
                   f"题目考点: {self.topic}\n\n"
        else:
            return f"题目内容: {self.left_body}\n题目类型: {self.type}\n题目难度: {self.difficulty}\n" \
                   f"题目考点: {self.topic}\n\n"

    # 仅输出题目内容，用于写入文件
    def to_text(self):
        result = ""
        if self.type == "选择题":
            result += f"{self.left_body}(  )\n"
            # 加入选项内容，同时在前面输入A、B、C、D等
            for i in range(len(self.options)):
                if i != 0:
                    result += "\t"
                result += f"{chr(65 + i)}、{self.options[i]}"
            result += "\n"
        elif self.type == "填空题":
            result += f"{self.left_body}(  ){self.right_body}\n"
        elif self.type == "判断题":
            result += f"{self.left_body}(True/Flase)\n"
        elif self.type == "简答题":
            result += f"{self.left_body}\n"
        return result
