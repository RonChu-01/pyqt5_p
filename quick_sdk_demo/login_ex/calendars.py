from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calendar(object):
    def setupUi(self, calendar):
        calendar.setObjectName("calendar")
        calendar.resize(277, 247)
        self.calendarWidget = QtWidgets.QCalendarWidget(calendar)
        self.calendarWidget.setGeometry(QtCore.QRect(-3, -4, 281, 251))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(calendar)
        QtCore.QMetaObject.connectSlotsByName(calendar)

    def retranslateUi(self, calendar):
        _translate = QtCore.QCoreApplication.translate
        calendar.setWindowTitle(_translate("calendar", "Dialog"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    calendar = QtWidgets.QDialog()
    ui = Ui_calendar()
    ui.setupUi(calendar)
    calendar.show()
    sys.exit(app.exec_())
