# author:孔德昱
# datetime:2023/6/13 16:33
"""
description：
"""

import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit, QPushButton, QScrollArea, QHBoxLayout
from utils.fileUtil import read_txt_file
from conf import parser_table_file


class InputDialog(QDialog):
    def __init__(self, input_txt):
        super().__init__()
        self.setWindowTitle("Dialog")
        self.resize(1200, 600)

        self.input_txt = input_txt
        # 创建垂直布局
        layout = QHBoxLayout(self)

        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # 创建文本框并添加到滚动区域
        self.text_edit = QTextEdit()
        scroll_area.setWidget(self.text_edit)

        # 创建按钮并添加到布局
        button1 = QPushButton("仅查看输入文件", self)
        button1.clicked.connect(self.show_input_txt)
        button2 = QPushButton("编辑输入文件", self)
        button2.clicked.connect(self.edit_input_txt)
        button3 = QPushButton("保存并退出", self)
        button3.clicked.connect(self.closeDialog)

        # 将按钮添加到布局中
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.show_input_txt()

    def show_input_txt(self):
        self.text_edit.setText(self.input_txt)
        self.text_edit.setReadOnly(True)

    def edit_input_txt(self):
        self.text_edit.setReadOnly(False)

    def closeDialog(self):
        self.accept()
