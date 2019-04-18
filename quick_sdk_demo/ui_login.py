# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(370, 506)
        font = QtGui.QFont()
        font.setFamily("Browallia New")
        Form.setFont(font)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 352, 488))
        self.widget.setObjectName("widget")

        # 整个登录框页面吹布局
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 登录框上部widget
        self.widget1 = QtWidgets.QWidget(self.widget)
        self.widget1.setMinimumSize(QtCore.QSize(350, 120))
        self.widget1.setObjectName("widget1")

        # 登录框上部widget--图标
        self.graphicsView = QtWidgets.QGraphicsView(self.widget1)
        self.graphicsView.setGeometry(QtCore.QRect(160, 10, 51, 41))
        self.graphicsView.setObjectName("graphicsView")

        # 登录框上部widget--关闭按钮
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setGeometry(QtCore.QRect(314, 10, 20, 20))

        # 登录框上部widget--关闭按钮--设置字体以及name
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        # 登录框上部widget--文字
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setGeometry(QtCore.QRect(80, 70, 231, 31))

        # 登录框上部widget--文字--设置字体以及名字
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # 将上部控件添加进垂直布局中
        self.verticalLayout_2.addWidget(self.widget1)

        # 登录框下部widget
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(350, 360))
        self.widget_2.setObjectName("widget_2")

        # 登录按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 210, 300, 50))
        self.pushButton_2.setMinimumSize(QtCore.QSize(300, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        # 登录按钮注册&控制台控件
        self.widget2 = QtWidgets.QWidget(self.widget_2)
        self.widget2.setGeometry(QtCore.QRect(100, 310, 160, 22))
        self.widget2.setObjectName("widget2")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_4.setContentsMargins(20, 0, 5, 0)
        self.horizontalLayout_4.setSpacing(35)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_5 = QtWidgets.QLabel(self.widget2)
        self.label_5.setMinimumSize(QtCore.QSize(50, 20))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_6 = QtWidgets.QLabel(self.widget2)
        self.label_6.setMinimumSize(QtCore.QSize(50, 20))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)

        # 登录按钮与注册&控制台控件间隔线
        self.widget3 = QtWidgets.QWidget(self.widget_2)
        self.widget3.setGeometry(QtCore.QRect(30, 270, 300, 22))
        self.widget3.setObjectName("widget3")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setSpacing(35)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.line = QtWidgets.QFrame(self.widget3)
        self.line.setMinimumSize(QtCore.QSize(100, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.horizontalLayout_3.addWidget(self.line)

        self.graphicsView_8 = QtWidgets.QGraphicsView(self.widget3)
        self.graphicsView_8.setMinimumSize(QtCore.QSize(20, 20))
        self.graphicsView_8.setObjectName("graphicsView_8")

        self.horizontalLayout_3.addWidget(self.graphicsView_8)

        self.line_3 = QtWidgets.QFrame(self.widget3)
        self.line_3.setMinimumSize(QtCore.QSize(100, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.horizontalLayout_3.addWidget(self.line_3)

        # 用户名密码以及记住密码区域控件
        self.widget4 = QtWidgets.QWidget(self.widget_2)
        self.widget4.setGeometry(QtCore.QRect(30, 41, 302, 136))
        self.widget4.setObjectName("widget4")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.widget_3 = QtWidgets.QWidget(self.widget4)
        self.widget_3.setMinimumSize(QtCore.QSize(300, 50))
        self.widget_3.setObjectName("widget_3")

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget_3)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setGeometry(QtCore.QRect(70, 10, 211, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QtWidgets.QWidget(self.widget4)
        self.widget_4.setMinimumSize(QtCore.QSize(300, 50))
        self.widget_4.setObjectName("widget_4")

        self.graphicsView_3 = QtWidgets.QGraphicsView(self.widget_4)
        self.graphicsView_3.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.graphicsView_3.setObjectName("graphicsView_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 10, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.verticalLayout.addWidget(self.widget_4)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setSpacing(160)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.checkBox = QtWidgets.QCheckBox(self.widget4)
        self.checkBox.setMinimumSize(QtCore.QSize(30, 20))
        self.checkBox.setObjectName("checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.label_2 = QtWidgets.QLabel(self.widget4)
        self.label_2.setMinimumSize(QtCore.QSize(30, 20))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addWidget(self.widget_2)

        self.retranslateUi(Form)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", "一键连接 全新服务"))
        self.pushButton_2.setText(_translate("Form", "登录"))
        self.label_5.setText(_translate("Form", "注册"))
        self.label_6.setText(_translate("Form", "控制台"))
        self.checkBox.setText(_translate("Form", "记住密码"))
        self.label_2.setText(_translate("Form", "忘记密码"))

