# author:孔德昱
# datetime:2023/5/17 16:48
"""
description：
"""


class Title:
    def __init__(self, school=None, college=None, subject=None, year=None, instructions=None):
        self.school = school
        self.college = college
        self.subject = subject
        self.year = year
        self.instructions = instructions

    def display(self):
        print("出题学校:", self.school)
        print("学院:", self.college)
        print("科目:", self.subject)
        print("时间:", self.year)
        print(self.instructions)

    def __str__(self):
        return f"出题学校: {self.school}\n学院: {self.college}\n" \
               f"科目: {self.subject}\n时间: {self.year}\n{self.instructions}"

