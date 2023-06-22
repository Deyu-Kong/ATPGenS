# author:孔德昱
# datetime:2023/6/11 15:07
"""
description：
"""

import ply.lex as lex

# tokens = ('学校', '大学', '中学', '小学', '学院', '期末', '期中', '随堂', '摸底',
#           '考试', '测试', '注意事项', '选择题', '填空题', '判断题', '简答题')
# all = ('PAPER', 'PAPER_HEAD', 'PAPER_BODY', 'SCHOOL', 'COLLEGE', 'TEXT', 'SCHOOL_YEAR', 'YEAR', 'NUMBER', 'SEMESTER',
#           'SUBJECT', 'PAPER_NAME', 'INSTRUCTIONS', 'SECTION_CHOOSE', 'SECTION_BLANK_FILLING', 'SECTION_JUDGMENT',
#           'SECTION_SHORT_ANSWER', 'LIST_CHOOSE', 'LIST_BLANK_FILLING', 'LIST_JUDGMENT''LIST_SHORT_ANSWER',
#           'QUESTION_CHOOSE', 'LEFT_QUESTION', 'RIGHT_QUESTION', 'OPTIONS', 'CAPITAL_LETTER', 'QUESTION_BLANK_FILLING',
#           'QUESTION_BODY','LINE_FEED')
# 词法单元
tokens = ['SCHOOL', 'COLLEGE', 'BLANK_AREA', 'JUDGMENT_AREA', 'SCHOOL_YEAR', 'QUESTION_NUMBER',
          'SEMESTER', 'PAPER_NAME', 'KEY_INSTRUCTION', 'OPTION_SYMBOL', 'LINE_FEED', 'BLANK', 'KEY_CHOOSE',
          'KEY_BLANK_FILLING', 'KEY_JUDGMENT', 'KEY_SHORT_ANSWER', 'TEXT']


# t_PAPER_NAME = r'(.{2,10})\s?(:?期末|期中|随堂|摸底)(:?考试|测试)'
def t_PAPER_NAME(t):
    r'(.{2,10})\s?(:?期末|期中|随堂|摸底)(:?考试|测试)'
    t.value = t.value[:-4]
    return t


t_SCHOOL = r'[\S]{2,10}(?:学校|大学|中学|小学)'
t_COLLEGE = r'[\S]{2,10}学院'


# t_SCHOOL_YEAR = r'[0-9]{4}-[0-9]{4}学年度'
def t_SCHOOL_YEAR(t):
    r'[0-9]{4}-[0-9]{4}学年度'
    t.value = t.value[:-3]
    return t


t_QUESTION_NUMBER = r'[0-9]+\.'
t_OPTION_SYMBOL = r'[a-g]\)'
t_KEY_CHOOSE = r'(?:一、|二、|三、|四、|五、)选择题'
t_KEY_BLANK_FILLING = r'(?:一、|二、|三、|四、|五、)填空题'
t_KEY_JUDGMENT = r'(?:一、|二、|三、|四、|五、)判断题'
t_KEY_SHORT_ANSWER = r'(?:一、|二、|三、|四、|五、)简答题'
t_KEY_INSTRUCTION = r'注意事项：'
t_BLANK_AREA = r'_{3,20}'
t_JUDGMENT_AREA = r'\(True/False\)'
t_BLANK = r'\s+'
t_TEXT = r'.'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def scan(text):
    lexer.input(text)
    toks = []
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        toks.append(tok)
    return toks


if __name__ == '__main__':
    from fileUtil import read_txt_file

    lexer.input(read_txt_file("../input/DB01.txt"))
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
