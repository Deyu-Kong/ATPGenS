# author:孔德昱
# datetime:2023/5/20 15:10
"""
description：
"""

import sqlite3
from conf import db_name

conn = sqlite3.connect(db_name)


# 查询所有表的信息
def show_tables():
    # 连接到SQLite数据库
    cursor = conn.cursor()

    # 查询所有表的信息
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    # 遍历并展示每个表的信息
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        print(f"表格名称: {table_name}")
        print("列信息:")
        for column in columns:
            column_name = column[1]
            data_type = column[2]
            print(f"  列名: {column_name}, 数据类型: {data_type}")

        print()

    # 关闭连接
    conn.close()


def do_simple_sql(sql):
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def create_questions_table():
    sql = "CREATE TABLE IF NOT EXISTS questions(" \
          "q_id INTEGER PRIMARY KEY," \
          "left_body VARCHAR(255)," \
          "right_body VARCHAR(255)," \
          "type INTEGER," \
          "difficulty INT," \
          "topic VARCHAR(255)," \
          "source INT," \
          "FOREIGN KEY (source) REFERENCES papers(p_id))"
    do_simple_sql(sql)


def create_papers_table():
    sql = "CREATE TABLE IF NOT EXISTS papers(" \
          "p_id INTEGER PRIMARY KEY," \
          "school VARCHAR(255)," \
          "college VARCHAR(255)," \
          "subject VARCHAR(255)," \
          "year VARCHAR(255)," \
          "instructions VARCHAR(255))"
    do_simple_sql(sql)


def create_options_table():
    sql = "CREATE TABLE IF NOT EXISTS options(" \
          "o_id INTEGER PRIMARY KEY," \
          "content VARCHAR(255)," \
          "question INT," \
          "FOREIGN KEY (question) REFERENCES questions(q_id))"
    do_simple_sql(sql)


def drop_questions_table():
    sql = "DROP TABLE IF EXISTS questions"
    do_simple_sql(sql)


def drop_papers_table():
    sql = "DROP TABLE IF EXISTS papers"
    do_simple_sql(sql)


def drop_options_table():
    sql = "DROP TABLE IF EXISTS options"
    do_simple_sql(sql)


def insert_one_option(option, q_id):
    # 使用数据库连接对象创建游标
    cursor = conn.cursor()

    # 插入数据的SQL语句
    sql = "INSERT INTO options(content, question) VALUES (?, ?)"

    # 执行SQL语句插入数据
    cursor.execute(sql, (option, q_id))

    # 提交更改
    conn.commit()

    # 关闭游标
    cursor.close()


def insert_one_question(question, source):
    # 使用数据库连接对象创建游标
    cursor = conn.cursor()

    # 插入数据的SQL语句
    sql = "INSERT INTO questions(left_body, right_body, type, difficulty, topic, source) VALUES (?, ?, ?, ?, ?, ?)"

    # 执行SQL语句插入数据
    cursor.execute(sql, (question.left_body, question.right_body,
                         question.type, question.difficulty, question.topic, source))

    question_id = cursor.lastrowid

    # 插入所有选项
    for option in question.options:
        insert_one_option(option, question_id)

    # 提交更改
    conn.commit()

    # 关闭游标
    cursor.close()


def insert_one_paper(paper):
    # create_paper_table()
    # 使用数据库连接对象创建游标
    cursor = conn.cursor()

    # 插入数据的SQL语句
    sql = "INSERT INTO papers(school, college, subject, year, instructions) VALUES (?, ?, ?, ?, ?)"

    # 插入paper表
    cursor.execute(sql, (paper.title.school, paper.title.college, paper.title.subject,
                         paper.title.year, paper.title.instructions))

    paper_id = cursor.lastrowid

    # 插入所有问题
    for questions in paper.questions:
        insert_one_question(questions, paper_id)

    # 提交更改
    conn.commit()

    # 关闭游标
    cursor.close()


# ===================后面均为查询的代码====================

def get_questions_table():
    cursor = conn.cursor()

    # 查询表的所有数据
    cursor.execute("SELECT * FROM questions")
    data = cursor.fetchall()
    return data, cursor.description


def get_papers_table():
    cursor = conn.cursor()

    # 查询表的所有数据
    cursor.execute("SELECT * FROM papers")
    data = cursor.fetchall()
    return data, cursor.description


def get_options_table():
    cursor = conn.cursor()

    # 查询表的所有数据
    cursor.execute("SELECT * FROM options")
    data = cursor.fetchall()
    return data, cursor.description


def get_questions_by_subject(subject):
    cursor = conn.cursor()

    # 查询表的所有数据。
    cursor.execute("SELECT * FROM questions WHERE source IN(SELECT p_id FROM papers WHERE subject='" + subject + "')")
    data = cursor.fetchall()
    return data, cursor.description


# 从数据库中查询该问题的q_id对应的选项
def get_choices_by_q_id(qid):
    cursor = conn.cursor()

    # 查询表的所有数据。
    cursor.execute("SELECT * FROM options WHERE question=" + str(qid))
    data = cursor.fetchall()
    return data, cursor.description


if __name__ == "__main__":
    # drop_questions_table()
    # drop_paper_table()
    # create_questions_table()
    # create_paper_table()
    show_tables()
