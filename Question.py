# author:孔德昱
# datetime:2023/5/17 16:38
"""
description：
"""


class Question:
    def __init__(self, content=None, question_type=None, difficulty=None, topic=None, source=None):
        self.content = content
        self.question_type = question_type
        self.difficulty = difficulty
        self.topic = topic
        self.source = source

    def display_question(self):
        print("题目内容:", self.content)
        print("题目类型:", self.question_type)
        print("题目难度:", self.difficulty)
        print("题目考点:", self.topic)
        print("题目来源:", self.source)
