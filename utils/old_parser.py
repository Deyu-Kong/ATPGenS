# author:孔德昱
# datetime:2023/5/19 21:09
"""
description：
"""

import re

from docx import Document
from pojo.paper import Paper
from pojo.question import Question
from data.sql import *


def lexical_analysis(content):
    pattern_school = "([\S]{2,10}(?:学校|大学|中学|小学))"
    pattern_college = "([\S]{2,10}学院)"
    pattern_year = "([0-9]{4}-[0-9]{4})"
    pattern_subject = "(.{2,10})\s?(:?期末|期中|随堂|摸底)(:?考试|测试)"
    pattern_instructions = "(注意事项)"
    pattern_main = "选择题|填空题|判断题|简答题"
    pattern_types = ["选择题", "填空题", "判断题", "简答题"]
    question_type = ""

    paper = Paper()
    paper.title.instructions = ""
    paper.questions = []

    flag_main = False
    flag_instructions = False

    question_number = 1
    tmp_question = ""

    for paragraph in content:
        # 试卷头
        if not flag_main:
            if flag_instructions:
                if paragraph == "\n" or re.findall(pattern_main, paragraph):
                    flag_main = True
                    # tmp_question += paragraph
                    if re.findall(pattern_types[0], paragraph):
                        question_type = pattern_types[0]
                    elif re.findall(pattern_types[1], paragraph):
                        question_type = pattern_types[1]
                    elif re.findall(pattern_types[2], paragraph):
                        question_type = pattern_types[2]
                    elif re.findall(pattern_types[3], paragraph):
                        question_type = pattern_types[3]
                else:
                    paper.title.instructions += paragraph + '\n'
            else:
                if re.findall(pattern_school, paragraph):
                    paper.title.school = re.search(pattern_school, paragraph).group(1)
                if re.findall(pattern_college, paragraph):
                    paper.title.college = re.search(pattern_college, paragraph).group(1)
                if re.findall(pattern_year, paragraph):
                    paper.title.year = re.search(pattern_year, paragraph).group(1)
                if re.findall(pattern_subject, paragraph):
                    paper.title.subject = re.search(pattern_subject, paragraph).group(1)
                if re.findall(pattern_instructions, paragraph):
                    paper.title.instructions += paragraph + '\n'
                    flag_instructions = True
                if re.findall(pattern_main, paragraph):
                    flag_main = True
        # 试卷体
        else:
            if re.findall(str(question_number), paragraph):
                if question_number > 1:
                    paper.questions.append(Question(content=tmp_question, question_type=question_type,
                                                    source=paper.title.school + paper.title.college))
                question_number += 1
                tmp_question = paragraph
            elif re.findall(pattern_main, paragraph):
                if question_number > 1:
                    paper.questions.append(Question(content=tmp_question, question_type=question_type,
                                                    source=paper.title.school + paper.title.college))
                question_number = 1
                tmp_question = ""
                if re.findall(pattern_types[0], paragraph):
                    question_type = pattern_types[0]
                elif re.findall(pattern_types[1], paragraph):
                    question_type = pattern_types[1]
                elif re.findall(pattern_types[2], paragraph):
                    question_type = pattern_types[2]
                elif re.findall(pattern_types[3], paragraph):
                    question_type = pattern_types[3]
            elif paragraph != "":
                tmp_question += '\n' + paragraph
    return paper


# 测试
if __name__ == "__main__":
    file_path = '../input/test01.docx'
    doc_content = read_docx(file_path)
    paper = lexical_analysis(doc_content)
    print(paper)
    insert_one_paper(paper)
    # print(lexical_analysis_result)
