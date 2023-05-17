from docx import Document

import re
from Title import Title
from Paper import Paper


def read_docx(file_path):
    document = Document(file_path)
    content = []

    for paragraph in document.paragraphs:
        content.append(paragraph.text)

    return content


def lexical_analysis(content):
    pattern_school = "([\S]{2,10}(?:学校|大学|中学|小学))"
    pattern_college = "([\S]{2,10}学院)"
    pattern_year = "([0-9]{4}-[0-9]{4})"
    pattern_subject = "(.{2,10})\s?(:?期末|期中|随堂|摸底)(:?考试|测试)"
    pattern_instructions = "(注意事项)"
    pattern_main = "选择题|填空题|判断题|简答题"

    paper = Paper()
    paper.title.instructions = ""
    paper.questions = []
    flag_main = False
    flag_instructions = False

    for paragraph in doc_content:
        # 试卷头
        if not flag_main:
            if flag_instructions:
                if paragraph == "\n" or re.findall(pattern_main, paragraph):
                    flag_main = True
                else:
                    paper.title.instructions += paragraph+'\n'
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
                    paper.title.instructions += paragraph+'\n'
                    flag_instructions = True
                if re.findall(pattern_main, paragraph):
                    flag_main = True
        # 试卷体
        else:
            paper.questions.append(paragraph)

    return paper


# 测试
if __name__ == "__main__":
    file_path = 'test01.docx'
    doc_content = read_docx(file_path)
    paper = lexical_analysis(doc_content)
    print(paper)
    # print(lexical_analysis_result)
