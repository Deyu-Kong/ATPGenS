import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QDialog
from PyQt5.QtGui import QIcon
import sqlite3
from PyQt5 import QtCore

from data.sql import get_questions_table


class QuestionsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('题库')
        self.setGeometry(300, 300, 800, 500)  # 设置窗口位置和大小
        self.layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.layout.addWidget(self.table_widget)

        self.load_question_table()

        self.setLayout(self.layout)

    def load_question_table(self):
        rows, descriptions = get_questions_table()

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
