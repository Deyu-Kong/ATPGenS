# author:孔德昱
# datetime:2023/6/7 20:57
"""
description：
"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox

from conf import output_file
from utils.generate import generate_paper


class GenerateDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Dialog")
        self.resize(400, 200)

        layout = QVBoxLayout()

        # 第一行
        first_row_layout = QHBoxLayout()
        label1 = QLabel("请输入科目")
        self.subject_line_edit = QLineEdit()
        first_row_layout.addWidget(label1)
        first_row_layout.addWidget(self.subject_line_edit)
        layout.addLayout(first_row_layout)

        # 第二行
        second_row_layout = QHBoxLayout()
        label2 = QLabel("选择题个数")
        self.choice_line_edit = QLineEdit()
        second_row_layout.addWidget(label2)
        second_row_layout.addWidget(self.choice_line_edit)
        layout.addLayout(second_row_layout)

        # 第三行
        third_row_layout = QHBoxLayout()
        label3 = QLabel("填空题个数")
        self.fill_in_the_blank_line_edit = QLineEdit()
        third_row_layout.addWidget(label3)
        third_row_layout.addWidget(self.fill_in_the_blank_line_edit)
        layout.addLayout(third_row_layout)

        # 第四行
        fourth_row_layout = QHBoxLayout()
        label4 = QLabel("判断题个数")
        self.true_false_line_edit = QLineEdit()
        fourth_row_layout.addWidget(label4)
        fourth_row_layout.addWidget(self.true_false_line_edit)
        layout.addLayout(fourth_row_layout)

        # 第五行
        fifth_row_layout = QHBoxLayout()
        label5 = QLabel("简答题个数")
        self.short_answer_line_edit = QLineEdit()
        fifth_row_layout.addWidget(label5)
        fifth_row_layout.addWidget(self.short_answer_line_edit)
        layout.addLayout(fifth_row_layout)

        # 第6行
        buttons_layout = QHBoxLayout()
        cancel_button = QPushButton("取消")
        ok_button = QPushButton("确定")
        buttons_layout.addWidget(cancel_button)
        buttons_layout.addWidget(ok_button)
        layout.addLayout(buttons_layout)

        # 绑定事件
        cancel_button.clicked.connect(self.reject)
        ok_button.clicked.connect(self.on_ok_button_clicked)

        self.setLayout(layout)

    # 正式组卷
    def on_ok_button_clicked(self):
        subject = self.subject_line_edit.text()
        choice_count = self.choice_line_edit.text()
        fill_in_the_blank_count = self.fill_in_the_blank_line_edit.text()
        true_false_count = self.true_false_line_edit.text()
        short_answer_count = self.short_answer_line_edit.text()

        if not subject or not choice_count or not fill_in_the_blank_count or not true_false_count or not short_answer_count:
            reply = QMessageBox.warning(self, '警告', '未输入完全，请重新输入!',
                                        QMessageBox.Ok, QMessageBox.Ok)

        status, paper_or_message = generate_paper(subject, choice_count, fill_in_the_blank_count, true_false_count,
                                       short_answer_count)
        if not status:
            reply = QMessageBox.warning(self, '警告', paper_or_message,
                                        QMessageBox.Ok, QMessageBox.Ok)
        else:
            # 将paper_or_message写入txt文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(paper_or_message.to_text())

            # 返回Accepted，并关闭窗口
            self.accept()
