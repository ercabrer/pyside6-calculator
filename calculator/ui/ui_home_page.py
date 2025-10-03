# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(400, 500)
        self.main_layout = QVBoxLayout(Calculator)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.display = QLineEdit(Calculator)
        self.display.setObjectName(u"display")
        self.display.setMinimumSize(QSize(0, 80))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.display.setFont(font)
        self.display.setAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.display.setReadOnly(True)

        self.main_layout.addWidget(self.display)

        self.button_grid = QGridLayout()
        self.button_grid.setSpacing(10)
        self.button_grid.setObjectName(u"button_grid")
        self.btn_clear = QPushButton(Calculator)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setMinimumSize(QSize(70, 70))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.btn_clear.setFont(font1)

        self.button_grid.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_toggle_sign = QPushButton(Calculator)
        self.btn_toggle_sign.setObjectName(u"btn_toggle_sign")
        self.btn_toggle_sign.setMinimumSize(QSize(70, 70))
        self.btn_toggle_sign.setFont(font1)

        self.button_grid.addWidget(self.btn_toggle_sign, 0, 1, 1, 1)

        self.btn_percentage = QPushButton(Calculator)
        self.btn_percentage.setObjectName(u"btn_percentage")
        self.btn_percentage.setMinimumSize(QSize(70, 70))
        self.btn_percentage.setFont(font1)

        self.button_grid.addWidget(self.btn_percentage, 0, 2, 1, 1)

        self.btn_divide = QPushButton(Calculator)
        self.btn_divide.setObjectName(u"btn_divide")
        self.btn_divide.setMinimumSize(QSize(70, 70))
        self.btn_divide.setFont(font1)

        self.button_grid.addWidget(self.btn_divide, 0, 3, 1, 1)

        self.btn_7 = QPushButton(Calculator)
        self.btn_7.setObjectName(u"btn_7")
        self.btn_7.setMinimumSize(QSize(70, 70))
        self.btn_7.setFont(font1)

        self.button_grid.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QPushButton(Calculator)
        self.btn_8.setObjectName(u"btn_8")
        self.btn_8.setMinimumSize(QSize(70, 70))
        self.btn_8.setFont(font1)

        self.button_grid.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_9 = QPushButton(Calculator)
        self.btn_9.setObjectName(u"btn_9")
        self.btn_9.setMinimumSize(QSize(70, 70))
        self.btn_9.setFont(font1)

        self.button_grid.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_multiply = QPushButton(Calculator)
        self.btn_multiply.setObjectName(u"btn_multiply")
        self.btn_multiply.setMinimumSize(QSize(70, 70))
        self.btn_multiply.setFont(font1)

        self.button_grid.addWidget(self.btn_multiply, 1, 3, 1, 1)

        self.btn_4 = QPushButton(Calculator)
        self.btn_4.setObjectName(u"btn_4")
        self.btn_4.setMinimumSize(QSize(70, 70))
        self.btn_4.setFont(font1)

        self.button_grid.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QPushButton(Calculator)
        self.btn_5.setObjectName(u"btn_5")
        self.btn_5.setMinimumSize(QSize(70, 70))
        self.btn_5.setFont(font1)

        self.button_grid.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_6 = QPushButton(Calculator)
        self.btn_6.setObjectName(u"btn_6")
        self.btn_6.setMinimumSize(QSize(70, 70))
        self.btn_6.setFont(font1)

        self.button_grid.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_subtract = QPushButton(Calculator)
        self.btn_subtract.setObjectName(u"btn_subtract")
        self.btn_subtract.setMinimumSize(QSize(70, 70))
        self.btn_subtract.setFont(font1)

        self.button_grid.addWidget(self.btn_subtract, 2, 3, 1, 1)

        self.btn_1 = QPushButton(Calculator)
        self.btn_1.setObjectName(u"btn_1")
        self.btn_1.setMinimumSize(QSize(70, 70))
        self.btn_1.setFont(font1)

        self.button_grid.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QPushButton(Calculator)
        self.btn_2.setObjectName(u"btn_2")
        self.btn_2.setMinimumSize(QSize(70, 70))
        self.btn_2.setFont(font1)

        self.button_grid.addWidget(self.btn_2, 3, 1, 1, 1)

        self.btn_3 = QPushButton(Calculator)
        self.btn_3.setObjectName(u"btn_3")
        self.btn_3.setMinimumSize(QSize(70, 70))
        self.btn_3.setFont(font1)

        self.button_grid.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_add = QPushButton(Calculator)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(70, 70))
        self.btn_add.setFont(font1)

        self.button_grid.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_0 = QPushButton(Calculator)
        self.btn_0.setObjectName(u"btn_0")
        self.btn_0.setMinimumSize(QSize(150, 70))
        self.btn_0.setFont(font1)

        self.button_grid.addWidget(self.btn_0, 4, 0, 1, 2)

        self.btn_decimal = QPushButton(Calculator)
        self.btn_decimal.setObjectName(u"btn_decimal")
        self.btn_decimal.setMinimumSize(QSize(70, 70))
        self.btn_decimal.setFont(font1)

        self.button_grid.addWidget(self.btn_decimal, 4, 2, 1, 1)

        self.btn_equals = QPushButton(Calculator)
        self.btn_equals.setObjectName(u"btn_equals")
        self.btn_equals.setMinimumSize(QSize(70, 70))
        self.btn_equals.setFont(font1)

        self.button_grid.addWidget(self.btn_equals, 4, 3, 1, 1)

        self.btn_square = QPushButton(Calculator)
        self.btn_square.setObjectName(u"btn_square")
        self.btn_square.setMinimumSize(QSize(70, 70))
        self.btn_square.setFont(font1)

        self.button_grid.addWidget(self.btn_square, 5, 0, 1, 1)


        self.main_layout.addLayout(self.button_grid)


        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Calculator", None))
        Calculator.setStyleSheet(QCoreApplication.translate("Calculator", u"QWidget {\n"
"    background-color: #000000;\n"
"}", None))
        self.display.setStyleSheet(QCoreApplication.translate("Calculator", u"QLineEdit {\n"
"    background-color: #2b2b2b;\n"
"    color: white;\n"
"    border: 2px solid #555;\n"
"    border-radius: 10px;\n"
"    padding: 10px;\n"
"}", None))
        self.display.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.btn_clear.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #a6a6a6;\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #bfbfbf;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #8a8a8a;\n"
"}", None))
        self.btn_clear.setText(QCoreApplication.translate("Calculator", u"C", None))
        self.btn_toggle_sign.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #a6a6a6;\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #bfbfbf;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #8a8a8a;\n"
"}", None))
        self.btn_toggle_sign.setText(QCoreApplication.translate("Calculator", u"\u00b1", None))
        self.btn_percentage.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #a6a6a6;\n"
"    color: black;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #bfbfbf;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #8a8a8a;\n"
"}", None))
        self.btn_percentage.setText(QCoreApplication.translate("Calculator", u"%", None))
        self.btn_divide.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #ff9500;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ffad33;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #cc7700;\n"
"}", None))
        self.btn_divide.setText(QCoreApplication.translate("Calculator", u"\u00f7", None))
        self.btn_7.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_7.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.btn_8.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_8.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.btn_9.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_9.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.btn_multiply.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #ff9500;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ffad33;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #cc7700;\n"
"}", None))
        self.btn_multiply.setText(QCoreApplication.translate("Calculator", u"\u00d7", None))
        self.btn_4.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_4.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.btn_5.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_5.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.btn_6.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_6.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.btn_subtract.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #ff9500;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ffad33;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #cc7700;\n"
"}", None))
        self.btn_subtract.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.btn_1.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_1.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.btn_2.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_2.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.btn_3.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_3.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.btn_add.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #ff9500;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ffad33;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #cc7700;\n"
"}", None))
        self.btn_add.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.btn_0.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_0.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.btn_decimal.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_decimal.setText(QCoreApplication.translate("Calculator", u".", None))
        self.btn_equals.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #ff9500;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #ffad33;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #cc7700;\n"
"}", None))
        self.btn_equals.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.btn_square.setStyleSheet(QCoreApplication.translate("Calculator", u"QPushButton {\n"
"    background-color: #333333;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 35px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #4d4d4d;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1a1a1a;\n"
"}", None))
        self.btn_square.setText(QCoreApplication.translate("Calculator", u"x\u00b2", None))
    # retranslateUi

