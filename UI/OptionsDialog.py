# author:孔德昱
# datetime:2023/6/12 16:08
"""
description：
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QDialog
from PyQt5.QtGui import QIcon
import sqlite3
from PyQt5 import QtCore

from data.sql import get_options_table


class OptionsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('所有选择题选项')
        self.setGeometry(400, 400, 800, 500)
        self.layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.load_options_table()

        self.setLayout(self.layout)

    def load_options_table(self):
        rows, descriptions = get_options_table()

        # 设置表格行数和列数
        if len(rows) == 0:
            self.table_widget.setRowCount(len(rows) + 1)
            columnCount = len(descriptions)
        else:
            self.table_widget.setRowCount(len(rows) + 1)
            columnCount = len(rows[0])
        self.table_widget.setColumnCount(columnCount)

        # 设置表头
        column_names = [description[0] for description in descriptions]
        self.table_widget.setHorizontalHeaderLabels(column_names)

        if len(rows) == 0:
            # If no data is available, display an empty row
            item = QTableWidgetItem('')
            item.setFlags(QtCore.Qt.ItemIsEnabled)  # Make the item non-editable
            self.table_widget.setItem(0, 0, item)

        else:
            # Fill the table with data
            for row_idx, row in enumerate(rows):
                for col_idx, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.table_widget.setItem(row_idx, col_idx, item)
