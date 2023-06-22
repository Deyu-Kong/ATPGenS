import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QHBoxLayout, \
    QSpacerItem, QSizePolicy, QDialog

import conf
from UI.DatabaseDialog import DatabaseDialog
from UI.GenerateDialog import GenerateDialog
from UI.InputDialog import InputDialog
from UI.ParseDialog import ParseDialog
from UI.ScanDialog import ScanDialog
from UI.SemanticDialog import SemanticDialog
from utils.fileUtil import *
from utils.parser import parse, parse_with_process
from utils.scanner import scan
from data.sql import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.text = None

        self.setWindowTitle('试卷管理')
        self.setGeometry(600, 300, 800, 500)  # 设置窗口位置和大小
        self.layout = QVBoxLayout()

        self.import_button = QPushButton('导入试卷')
        self.import_button.clicked.connect(self.import_paper)
        self.layout.addWidget(self.import_button)

        self.show_cur_paper_button = QPushButton('查看当前输入试卷')
        self.show_cur_paper_button.clicked.connect(self.show_cur_paper)
        self.layout.addWidget(self.show_cur_paper_button)

        self.scanner_button = QPushButton('词法分析')
        self.scanner_button.clicked.connect(self.scan)
        self.layout.addWidget(self.scanner_button)

        self.parser_button = QPushButton('语法分析')
        self.parser_button.clicked.connect(self.parse)
        self.layout.addWidget(self.parser_button)

        self.semantic_button = QPushButton('语义分析')
        self.semantic_button.clicked.connect(self.semantic_analysis)
        self.layout.addWidget(self.semantic_button)

        self.save_button = QPushButton('分析当前试卷并导入题库')
        self.save_button.clicked.connect(self.save_paper)
        self.layout.addWidget(self.save_button)

        self.generate_button = QPushButton('组卷')
        self.generate_button.clicked.connect(self.generate_paper)
        self.layout.addWidget(self.generate_button)

        self.view_button = QPushButton('查看题库')
        self.view_button.clicked.connect(self.view_question_bank)
        self.layout.addWidget(self.view_button)

        # 添加一个弹簧组件
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer_item)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label)

        self.file_label = QLabel()
        self.layout.addWidget(self.file_label)
        self.file_label.setText("当前试卷：未导入")

        self.setLayout(self.layout)

        self.setLayout(self.layout)

        self.show()

    def show_cur_paper(self):
        if self.text:
            self.input_dialog = InputDialog(self.text)

            if self.input_dialog.exec_() == QDialog.Accepted:
                self.text = self.input_dialog.text_edit.toPlainText()
                self.status_label.setText('已修改当前试卷并保存（未写回文件）。')
            else:
                self.status_label.setText('查看当前导入试卷，已关闭。')
        else:
            self.status_label.setText('未指定当前试卷，请先导入！')

    def scan(self):
        if self.text:
            scan_result = scan(self.text)
            self.scan_dialog = ScanDialog(scan_result)
            self.scan_dialog.exec_()  # 使用exec_()而不是show()

            self.status_label.setText('词法分析完成')
        else:
            self.status_label.setText('未指定当前试卷，请先导入！')

    def parse(self):
        if self.text:
            # parse_result 是一个 Paper类型的对象。表示已经解析完成的paper对象
            parse_result, parse_process = parse_with_process(self.text)
            self.parse_dialog = ParseDialog(parse_process)
            self.parse_dialog.exec_()  # 使用exec_()而不是show()

            self.status_label.setText('语法分析完成')
        else:
            self.status_label.setText('未指定当前试卷，请先导入！')

    def semantic_analysis(self):
        if self.text:
            # parse_result 是一个 Paper类型的对象。表示已经解析完成的paper对象
            parse_result, parse_process = parse_with_process(self.text)
            if parse_result:
                self.semantic_dialog = SemanticDialog(parse_result)
                self.semantic_dialog.exec_()
                self.status_label.setText('语义分析完成')
            else:
                self.status_label.setText('当前试卷不符合语法定义，请检查！')
        else:
            self.status_label.setText('未指定当前试卷，请先导入！')

    def import_paper(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, '选择试卷文件', '', 'Text Files (*.txt);;Word Files (*.docx)',
                                                   options=file_dialog.Options())
        if file_path.endswith(".docx"):
            doc_content = read_docx_file(file_path)
            self.text = convert_document_to_string(doc_content)
        elif file_path.endswith(".txt"):
            self.text = read_txt_file(file_path)
        else:
            self.text = None
            self.status_label.setText('未导入试卷')
            return
        self.status_label.setText('导入试卷：' + file_path)
        self.file_label.setText("当前试卷：" + file_path)

    def save_paper(self):
        # 完成词法分析、语法分析和语义分析。生成中间代码（paper对象）
        paper = parse(self.text)
        if paper:
            # 将paper对象插入到数据库中
            insert_one_paper(paper)
            self.text = None
            self.file_label.setText("当前试卷：未导入")
            self.status_label.setText('试卷分析成功！已导入题库')
        else:
            self.status_label.setText('当前试卷不符合语法定义，请检查！')

    def generate_paper(self):
        # 创建并产看组卷功能对话框
        self.generate_dialog = GenerateDialog()
        if self.generate_dialog.exec_() == QDialog.Accepted:
            self.status_label.setText('组卷成功！')
        else:
            self.status_label.setText('关闭组卷窗口！')

    def view_question_bank(self):
        # 创建并显示查看题库对话框
        self.data_edit_dialog = DatabaseDialog()
        self.data_edit_dialog.exec_()  # 使用exec_()而不是show()

        self.status_label.setText('查看题库功能已关闭')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
