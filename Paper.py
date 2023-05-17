# author:孔德昱
# datetime:2023/5/17 16:53
"""
description：
"""

from Title import Title


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
        return str(self.title)+'\n题目: \n'+str(self.questions)
