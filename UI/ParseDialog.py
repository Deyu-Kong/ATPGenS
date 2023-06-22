# author:孔德昱
# datetime:2023/6/12 22:20
"""
description：语法分析结果查看
"""
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTextEdit, QPushButton, QScrollArea, QHBoxLayout
from utils.fileUtil import read_txt_file
from conf import parser_table_file


class ParseDialog(QDialog):
    def __init__(self, parse_process):
        super().__init__()
        self.setWindowTitle("Dialog")
        self.resize(1200, 600)

        self.parse_process = parse_process
        # 创建垂直布局
        layout = QHBoxLayout(self)

        # 创建滚动区域
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # 创建文本框并添加到滚动区域
        self.text_edit = QTextEdit()
        scroll_area.setWidget(self.text_edit)

        # 创建按钮并添加到布局
        button1 = QPushButton("查看语法分析过程", self)
        button1.clicked.connect(self.show_parse_process)
        button2 = QPushButton("查看分析表", self)
        button2.clicked.connect(self.show_LALR_table)

        # 将按钮添加到布局中
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        layout.addWidget(scroll_area)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def show_parse_process(self):
        self.text_edit.setText(self.parse_process)

    def show_LALR_table(self):
        text = read_txt_file(parser_table_file)
        self.text_edit.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = ParseDialog("test")
    dialog.show()
    sys.exit(app.exec_())
