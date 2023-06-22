# author:孔德昱
# datetime:2023/5/23 11:46
"""
description：
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QDialog, QTableWidget, \
    QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIcon
import sqlite3

from UI.PapersDialog import PapersDialog
from UI.QuestionsDialog import QuestionsDialog
from UI.OptionsDialog import OptionsDialog
from data.sql import *


class DatabaseDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('题库管理')
        self.setGeometry(300, 300, 800, 500)
        self.layout = QVBoxLayout()

        self.return_button = QPushButton('返回')
        self.return_button.clicked.connect(self.close)
        self.layout.addWidget(self.return_button)

        self.view_papers_button = QPushButton('查看所有试卷')
        self.view_papers_button.clicked.connect(self.view_all_papers)
        self.layout.addWidget(self.view_papers_button)

        self.view_questions_button = QPushButton('查看所有题目')
        self.view_questions_button.clicked.connect(self.view_all_questions)
        self.layout.addWidget(self.view_questions_button)

        self.view_options_button = QPushButton('查看所有选择题选项')
        self.view_options_button.clicked.connect(self.view_all_options)
        self.layout.addWidget(self.view_options_button)

        self.delete_papers_button = QPushButton('删除所有试卷')
        self.delete_papers_button.clicked.connect(self.delete_all_papers)
        self.layout.addWidget(self.delete_papers_button)

        self.delete_questions_button = QPushButton('删除所有题目')
        self.delete_questions_button.clicked.connect(self.delete_all_questions)
        self.layout.addWidget(self.delete_questions_button)

        self.delete_options_button = QPushButton('删除所有选择题选项')
        self.delete_options_button.clicked.connect(self.delete_all_options)
        self.layout.addWidget(self.delete_options_button)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

        self.setLayout(self.layout)

    def view_all_papers(self):
        self.papers_window = PapersDialog()
        self.papers_window.exec_()
        self.status_label.setText('查询试卷表')

    def view_all_questions(self):
        self.questions_window = QuestionsDialog()
        self.questions_window.exec_()
        self.status_label.setText('查询题目表')

    def view_all_options(self):
        self.options_window = OptionsDialog()
        self.options_window.exec_()
        self.status_label.setText('查询选择题选项')

    def delete_all_papers(self):
        # 删除所有试卷的逻辑
        reply = QMessageBox.question(self, '警告', '确定要执行操作吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 执行你的代码
            drop_papers_table()
            create_papers_table()
            self.status_label.setText('已删除所有试卷')
        else:
            self.status_label.setText("取消操作")

    def delete_all_questions(self):
        # 删除所有题目的逻辑
        reply = QMessageBox.question(self, '警告', '确定要执行操作吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 执行你的代码
            drop_questions_table()
            create_questions_table()
            self.status_label.setText('已删除所有题目')
        else:
            self.status_label.setText("取消操作")

    def delete_all_options(self):
        # 删除所有题目的逻辑
        reply = QMessageBox.question(self, '警告', '确定要执行操作吗？',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            # 执行你的代码
            drop_options_table()
            create_options_table()
            self.status_label.setText('已删除所有选择题选项')
        else:
            self.status_label.setText("取消操作")

