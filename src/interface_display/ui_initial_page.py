# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_interface.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QPushButton, QScrollArea,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(645, 629)
        # Dialog.setModal(False)
        self.add_task_button = QPushButton(Dialog)
        self.add_task_button.setObjectName(u"add_task_button")
        self.add_task_button.setGeometry(QRect(560, 20, 75, 24))
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 100, 621, 471))
        self.scrollArea.setWidgetResizable(True)
        self.view_container = QWidget()
        self.view_container.setObjectName(u"view_container")
        self.view_container.setGeometry(QRect(0, 0, 619, 469))
        self.view_box = QListWidget(self.view_container)
        self.view_box.setObjectName(u"view_box")
        self.view_box.setGeometry(QRect(0, 0, 621, 531))
        self.view_box.setMovement(QListView.Snap)
        self.view_box.setProperty("isWrapping", False)
        self.scrollArea.setWidget(self.view_container)
        self.new_task_input_line = QLineEdit(Dialog)
        self.new_task_input_line.setObjectName(u"new_task_input_line")
        self.new_task_input_line.setGeometry(QRect(10, 20, 541, 22))
        self.search_button = QPushButton(Dialog)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(560, 60, 75, 24))
        self.search_task_input_line = QLineEdit(Dialog)
        self.search_task_input_line.setObjectName(u"search_task_input_line")
        self.search_task_input_line.setGeometry(QRect(10, 60, 541, 22))
        self.task_list_button = QPushButton(Dialog)
        self.task_list_button.setObjectName(u"task_list_button")
        self.task_list_button.setGeometry(QRect(10, 580, 75, 24))
        self.task_list_button.setCheckable(False)
        self.tas_history_button = QPushButton(Dialog)
        self.tas_history_button.setObjectName(u"tas_history_button")
        self.tas_history_button.setGeometry(QRect(100, 580, 75, 24))
        self.close_app_button = QPushButton(Dialog)
        self.close_app_button.setObjectName(u"close_app_button")
        self.close_app_button.setGeometry(QRect(560, 580, 75, 24))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_task_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.new_task_input_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"New Task", None))
        self.search_button.setText(QCoreApplication.translate("Dialog", u"Search", None))
        self.search_task_input_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Task Search", None))
        self.task_list_button.setText(QCoreApplication.translate("Dialog", u"Task List", None))
        self.tas_history_button.setText(QCoreApplication.translate("Dialog", u"Task History", None))
        self.close_app_button.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

