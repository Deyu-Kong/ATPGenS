# author:孔德昱
# datetime:2023/6/11 16:08
"""
description： 语法分析
"""
# Get the token map from the lexer.  This is required.
import sys
from io import StringIO

from utils.scanner import tokens
from pojo.paper import Paper
from pojo.question import Question
from pojo.title import Title

import ply.yacc as yacc

"""
    文法定义
"""


def p_paper(p):
    'PAPER : PAPER_HEAD PAPER_BODY'
    paper = Paper(p[1], p[2])
    p[0] = paper


def p_paper_head(p):
    'PAPER_HEAD : SCHOOL COLLEGE SCHOOL_YEAR PAPER_NAME INSTRUCTIONS'
    p[0] = Title(school=p[1], college=p[2], subject=p[4], year=p[3], instructions=p[5])


def p_empty(p):
    'empty :'


def p_texts(p):
    '''TEXTs : TEXT TEXTs
            | TEXT'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_instructions(p):
    'INSTRUCTIONS : KEY_INSTRUCTION INSTRUCTION'
    p[0] = p[1] + '\n' + p[2]


def p_instruction(p):
    '''INSTRUCTION : QUESTION_NUMBER TEXTs INSTRUCTION
                    | QUESTION_NUMBER TEXTs'''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1] + p[2] + '\n' + p[3]


def p_paper_body(p):
    'PAPER_BODY : SECTION_CHOOSE SECTION_BLANK_FILLING SECTION_JUDGMENT SECTION_SHORT_ANSWER'
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_section_choose(p):
    'SECTION_CHOOSE : KEY_CHOOSE LIST_CHOOSE'
    p[0] = p[2]
    for question in p[0]:
        question.type = "选择题"


def p_list_choose(p):
    '''LIST_CHOOSE : QUESTION_CHOOSE LIST_CHOOSE
                    | QUESTION_CHOOSE'''
    if len(p) == 3:
        p[0] = p[2]
        p[0].append(p[1])
    else:
        p[0] = []
        p[0].append(p[1])


def p_question_choose(p):
    'QUESTION_CHOOSE : QUESTION_NUMBER QUESTION_BODY OPTIONS'
    p[0] = Question(left_body=p[2], options=p[3])


def p_left_body(p):
    '''LEFT_BODY : TEXTs
                | empty'''
    try:
        p[0] = p[1]
    except Exception:
        p[0] = ""


def p_right_body(p):
    '''RIGHT_BODY : TEXTs
                    | empty'''
    try:
        p[0] = p[1]
    except Exception:
        p[0] = ""


def p_options(p):
    '''OPTIONS : OPTION_SYMBOL TEXTs OPTIONS
                | OPTION_SYMBOL TEXTs'''
    if len(p) == 4:
        p[0] = p[3]
        p[0].append(p[2])
    else:
        p[0] = []
        p[0].append(p[2])


def p_section_blank_filling(p):
    'SECTION_BLANK_FILLING : KEY_BLANK_FILLING LIST_BLANK_FILLING'
    p[0] = p[2]
    for question in p[0]:
        question.type = "填空题"


def p_list_blank_filling(p):
    '''LIST_BLANK_FILLING : QUESTION_BLANK_FILLING LIST_BLANK_FILLING
                            | QUESTION_BLANK_FILLING'''
    if len(p) == 3:
        p[0] = p[2]
        p[0].append(p[1])
    else:
        p[0] = []
        p[0].append(p[1])


def p_question_blank_filling(p):
    'QUESTION_BLANK_FILLING : QUESTION_NUMBER LEFT_BODY BLANK_AREA RIGHT_BODY'
    p[0] = Question(left_body=p[2], right_body=p[4])


def p_section_judgment(p):
    'SECTION_JUDGMENT : KEY_JUDGMENT LIST_JUDGMENT'
    p[0] = p[2]
    for question in p[0]:
        question.type = "判断题"


def p_list_judgment(p):
    '''LIST_JUDGMENT :  QUESTION_JUDGMENT LIST_JUDGMENT
                        | QUESTION_JUDGMENT'''
    if len(p) == 3:
        p[0] = p[2]
        p[0].append(p[1])
    else:
        p[0] = []
        p[0].append(p[1])


def p_question_judgment(p):
    'QUESTION_JUDGMENT : QUESTION_NUMBER QUESTION_BODY JUDGMENT_AREA'
    p[0] = Question(left_body=p[2])


def p_question_body(p):
    'QUESTION_BODY : TEXTs'
    p[0] = p[1]


def p_section_short_answer(p):
    'SECTION_SHORT_ANSWER : KEY_SHORT_ANSWER LIST_SHORT_ANSWER'
    p[0] = p[2]
    for question in p[0]:
        question.type = "简答题"


def p_list_short_answer(p):
    '''LIST_SHORT_ANSWER : QUESTION_SHORT_ANSWER LIST_SHORT_ANSWER
                        | QUESTION_SHORT_ANSWER'''
    if len(p) == 3:
        p[0] = p[2]
        p[0].append(p[1])
    else:
        p[0] = []
        p[0].append(p[1])


def p_question_short_answer(p):
    'QUESTION_SHORT_ANSWER : QUESTION_NUMBER TEXTs'
    p[0] = Question(left_body=p[2])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


yacc.yacc(debug=True)
# Build the parser
parser = yacc.yacc()


def parse(text):
    result = parser.parse(text)
    return result


def parse_with_process(text):
    # 创建一个 StringIO 对象作为标准输出流的替代品
    output = StringIO()

    # 保存原始的标准输出流
    original_stderr = sys.stderr

    # 重定向标准输出流到 StringIO 对象
    sys.stderr = output

    # 运行语法分析
    result = parser.parse(text, debug=True)

    # 恢复原始的标准输出流
    sys.stderr = original_stderr

    # 获取调试输出的字符串
    debug_output = output.getvalue()
    return result, debug_output


if __name__ == '__main__':
    from utils.fileUtil import read_txt_file

    # 打印出具体信息，即每一步的状态、符号栈、以及动作
    # result = parser.parse(read_txt_file("../input/test01.txt"), debug=True)
    # 创建一个 StringIO 对象作为标准输出流的替代品
    output = StringIO()

    # 保存原始的标准输出流
    original_stderr = sys.stderr

    # 重定向标准输出流到 StringIO 对象
    sys.stderr = output

    # 运行语法分析
    result = parser.parse(read_txt_file("../input/DB02.txt"), debug=True)

    # 恢复原始的标准输出流
    sys.stderr = original_stderr

    # 获取调试输出的字符串
    debug_output = output.getvalue()

    # 打印最终结果和调试输出
    print(f"Result: {result}")
    print(f"Debug Output:\n{debug_output}")
