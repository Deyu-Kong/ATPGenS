# author:孔德昱
# datetime:2023/6/12 21:01
"""
description：词法分析的界面
"""

import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QListWidgetItem


# 创建自定义对话框类
class ScanDialog(QDialog):
    def __init__(self, token_data):
        super().__init__()
        self.resize(800,600)
        self.token_data = token_data

        # 创建布局
        layout = QHBoxLayout()

        # 创建左侧列表
        self.list_widget = QListWidget()

        # 创建右侧按钮
        button1 = QPushButton('查看单词表')

        # 将按钮添加到布局中
        button_layout = QVBoxLayout()
        button_layout.addWidget(button1)

        # 设置布局
        layout.addWidget(self.list_widget, 75)
        layout.addLayout(button_layout)

        # 将布局应用于对话框
        self.setLayout(layout)

        # 绑定按钮点击事件
        button1.clicked.connect(self.showList)

    def showList(self):
        for item in self.token_data:
            list_item = QListWidgetItem(str(item))
            self.list_widget.addItem(list_item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = ScanDialog()
    dialog.show()
    sys.exit(app.exec_())
