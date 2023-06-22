# author:孔德昱
# datetime:2023/6/13 16:20
"""
description：语义分析结果
"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit, QPushButton, QScrollArea, QHBoxLayout
from utils.fileUtil import read_txt_file
from conf import parser_table_file


class SemanticDialog(QDialog):
    def __init__(self, paper):
        super().__init__()
        self.setWindowTitle("Dialog")
        self.resize(1200, 600)

        self.paper = paper
        # 创建垂直布局
        layout = QHBoxLayout(self)

        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # 创建文本框并添加到滚动区域
        self.text_edit = QTextEdit()
        scroll_area.setWidget(self.text_edit)

        # 创建按钮并添加到布局
        button1 = QPushButton("查看中间结果", self)
        button1.clicked.connect(self.show_paper)

        # 将按钮添加到布局中
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)

        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def show_paper(self):
        self.text_edit.setText(str(self.paper))

