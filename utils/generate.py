# author:孔德昱
# datetime:2023/6/7 21:09
"""
description：
"""
import random

from pojo.paper import Paper
from data.sql import *
from pojo.question import Question
from conf import *
from pojo.title import Title


def generate_paper(subject, choice_count, fill_in_the_blank_count, true_false_count, short_answer_count):

    title = Title()
    # 根据默认属性生成标题
    title.school = default_school
    title.college = default_college
    title.subject = subject
    title.year = default_year
    title.instructions = default_instructions

    paper = Paper(title=title)

    # rows 的格式：tuple(23, '在操作系统中，进程是指：', None, '选择题', None, None, 2)
    rows, descriptions = get_questions_by_subject(subject)
    # 未查询到
    if len(rows) == 0:
        return False, "无法查询到当前科目，请重新输入"

    # 选择题
    choice_questions = []
    # rows 中抽取出所有选择题
    for row in rows:
        if row[3] == '选择题':
            choice_questions.append(row)

    # 选择题不足
    if len(choice_questions) < int(choice_count):
        return False, "该科目选择题数量不足，请重新输入"

    # 从选择题列表中随机选择choice_count个选择题
    choice_questions = random.sample(choice_questions, int(choice_count))

    # 将选择题从元组转换为Question类型。同时将选项打乱重拍
    for choice_question in choice_questions:
        question = Question(question_type=choice_question[3], left_body=choice_question[1])
        # 从数据库中查询该问题的q_id对应的选项
        choices, _ = get_choices_by_q_id(choice_question[0])
        # 将选项中的文本提取出来
        choices = [choice[1] for choice in choices]
        # 将选项打乱重拍
        choices = random.sample(choices, len(choices))
        question.options = choices
        paper.questions.append(question)

    # 填空题同理
    fill_in_the_blank_questions = []
    for row in rows:
        if row[3] == '填空题':
            fill_in_the_blank_questions.append(row)

    # 填空题不足
    if len(fill_in_the_blank_questions) < int(fill_in_the_blank_count):
        return False, "该科目填空题数量不足，请重新输入"

    # 从填空题列表中随机选择fill_in_the_blank_count个填空题
    fill_in_the_blank_questions = random.sample(fill_in_the_blank_questions, int(fill_in_the_blank_count))

    # 将填空题从元组转换为Question类型。
    for fill_in_the_blank_question in fill_in_the_blank_questions:
        question = Question(question_type=fill_in_the_blank_question[3], left_body=fill_in_the_blank_question[1],
                            right_body=fill_in_the_blank_question[2])
        paper.questions.append(question)

    # 判断题同理
    true_false_questions = []
    for row in rows:
        if row[3] == '判断题':
            true_false_questions.append(row)

    # 判断题不足
    if len(true_false_questions) < int(true_false_count):
        return False, "该科目判断题数量不足，请重新输入"

    # 从判断题列表中随机选择true_false_count个判断题
    true_false_questions = random.sample(true_false_questions, int(true_false_count))

    # 将判断题从元组转换为Question类型。
    for true_false_question in true_false_questions:
        question = Question(question_type=true_false_question[3], left_body=true_false_question[1])
        paper.questions.append(question)

    # 简答题同理
    short_answer_questions = []
    for row in rows:
        if row[3] == '简答题':
            short_answer_questions.append(row)

    # 简答题不足
    if len(short_answer_questions) < int(short_answer_count):
        return False, "该科目简答题数量不足，请重新输入"

    # 从简答题列表中随机选择short_answer_count个简答题
    short_answer_questions = random.sample(short_answer_questions, int(short_answer_count))

    # 将简答题从元组转换为Question类型。
    for short_answer_question in short_answer_questions:
        question = Question(question_type=short_answer_question[3], left_body=short_answer_question[1])
        paper.questions.append(question)

    return True, paper
