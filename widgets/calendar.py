# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

from db.queries import DatabaseQueries
from Qt import QtCore, QtGui, QtWidgets


class EventDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(EventDialog, self).__init__(parent)

        main_font = QtGui.QFont()
        main_font.setPointSize(12)
        main_font.setFamily("Arial")

        self.setWindowTitle("AM")

        dialogs_layout = QtWidgets.QVBoxLayout()
        self.setLayout(dialogs_layout)

        self.event_infos = QtWidgets.QTextEdit()
        self.event_infos.setFont(main_font)
        dialogs_layout.addWidget(self.event_infos)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.NoFrame | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(10)
        dialogs_layout.addWidget(sperator)

        self.task_label = QtWidgets.QLabel("Task Status")
        self.task_label.setFont(main_font)
        self.task_label.setAlignment(QtCore.Qt.AlignLeft)
        dialogs_layout.addWidget(self.task_label)

        self.status_combox = QtWidgets.QComboBox()
        self.status_combox.setFont(main_font)
        dialogs_layout.addWidget(self.status_combox)

        status_list = ['wts', 'ip', 'rev', 'rtk', 'fin']
        status_name = ['Waiting to Start', 'In Progress', 'To Review', 'Retake', 'Ok']

        for i, status in enumerate(status_list):
            self.status_combox.addItem(QtGui.QIcon("C:/Users/jucha/Documents/@git/icons/{}.png".format(status)), status_name[i])

        create_btn = QtWidgets.QPushButton("Create")
        create_btn.setFont(main_font)
        create_btn.clicked.connect(self.close)
        dialogs_layout.addWidget(create_btn)


class CalendarWidget(QtWidgets.QWidget):
    """docstring for ClassName"""

    def __init__(self):
        super(CalendarWidget, self).__init__()

        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(12)
        self.main_font.setFamily("Arial")

        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.month = QtWidgets.QLabel("")
        self.month.setFont(self.main_font)
        self.month.setStyleSheet(
            "QLabel {color: #c0392b}")
        self.month.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.month)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        self.main_layout.addWidget(sperator)

        self.calendar = QtWidgets.QCalendarWidget(self)
        self.calendar.setFont(self.main_font)
        self.calendar.showToday()
        self.calendar.setNavigationBarVisible(False)
        #self.calendar.selectionChanged.connect(self.update_infos)

        weekend_color = QtGui.QTextCharFormat()
        weekend_color.setForeground(QtGui.QColor(192, 57, 43, 255))
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Saturday, weekend_color)
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Sunday, weekend_color)

        self.update_month_label()

        self.main_layout.addWidget(self.calendar)

        self.btn_layout = QtWidgets.QHBoxLayout(self)
        self.main_layout.addLayout(self.btn_layout)

        self.previous_btn = QtWidgets.QPushButton("<")
        self.previous_btn.setFont(self.main_font)
        self.previous_btn.clicked.connect(self.calendar.showPreviousMonth)
        self.previous_btn.clicked.connect(self.update_month_label)
        self.btn_layout.addWidget(self.previous_btn)

        self.next_btn = QtWidgets.QPushButton(">")
        self.next_btn.setFont(self.main_font)
        self.next_btn.clicked.connect(self.calendar.showNextMonth)
        self.next_btn.clicked.connect(self.update_month_label)
        self.btn_layout.addWidget(self.next_btn)

        self.event_btn = QtWidgets.QPushButton("Add Event")
        self.event_btn.setFont(self.main_font)
        self.main_layout.addWidget(self.event_btn)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        self.main_layout.addWidget(sperator)

        self.event_infos = QtWidgets.QTextEdit()
        self.event_infos.setFont(self.main_font)
        self.event_infos.setReadOnly(True)
        self.main_layout.addWidget(self.event_infos)

    def update_month_label(self):

        current_month = self.calendar.monthShown()
        current_year = self.calendar.yearShown()
        month_map = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

        self.month.setText(month_map[current_month] + " | " + str(current_year))
