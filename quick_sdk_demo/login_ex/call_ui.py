from main_q import Ui_MainWindow
from calendars import Ui_calendar

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
import sys


class ParentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)


class ChildWindow(QDialog):
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.calendars = Ui_calendar()
        self.calendars.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParentWindow()
    child = ChildWindow()

    # 通过按钮将两个窗体关联
    btn = window.main_ui.pushButton
    btn.clicked.connect(child.show)

    # 显示
    window.show()
    sys.exit(app.exec_())
