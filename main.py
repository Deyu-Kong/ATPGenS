# author:孔德昱
# datetime:2023/5/20 16:19
"""
description：
"""
# from utils.parser import *
from UI.MainWindow import *
from UI.QuestionsDialog import *

if __name__ == '__main__':
    # show_question()
    # show_test_paper()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

