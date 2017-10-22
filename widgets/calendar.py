# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

from db.queries import DatabaseQueries
from Qt import QtCore, QtGui, QtWidgets


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
        self.calendar.selectionChanged.connect(self.update_infos)

        weekend_color = QtGui.QTextCharFormat()
        weekend_color.setForeground(QtGui.QColor(192, 57, 43, 255))
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Saturday, weekend_color)
        self.calendar.setWeekdayTextFormat(QtCore.Qt.Sunday, weekend_color)

        self.calendar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.calendar.customContextMenuRequested.connect(self.add_event_menu)

        self.init_widget()

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

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.NoFrame | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(10)
        self.main_layout.addWidget(sperator)

        self.event_infos = QtWidgets.QTextEdit()
        self.event_infos.setFont(self.main_font)
        self.event_infos.setReadOnly(True)
        self.main_layout.addWidget(self.event_infos)

    def update_month_label(self):

        current_month = self.calendar.monthShown()
        current_year = self.calendar.yearShown()
        month_map = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 			6:'June', 7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

        self.month.setText(month_map[current_month] + " | " + str(current_year))

    def add_event_menu(self):

        mouse_point = QtGui.QCursor.pos()

        event_menu = QtWidgets.QMenu("Menu")
        event_menu.setFont(self.main_font)
        event_menu.addAction('Create New Event', self.add_event)
        event_menu.exec_(self.calendar.mapToParent(mouse_point))

    def add_event(self):

        d = NewEventDialogs(self)
        d.exec_()
        name, description = d.get_values()

        current_date = self.calendar.selectedDate()
        db_date = current_date.toString()

        db = DatabaseQueries()
        db.cursor.execute(
            "INSERT INTO events (date, description, name) VALUES (%s, %s, %s)", (db_date, description, name))

        event_color = QtGui.QTextCharFormat()
        event_color.setFontPointSize(11)
        event_color.setForeground(QtGui.QColor(46, 204, 113, 255))
        self.calendar.setDateTextFormat(current_date, event_color)

    def update_infos(self):

        current_date = self.calendar.selectedDate()
        db_date = current_date.toString()
        db_date = "'{}'".format(db_date)

        try:
            db = DatabaseQueries()
            db.cursor.execute(
                "SELECT * FROM events WHERE date = {}".format(db_date))
            data = db.cursor.fetchall()

            event_text = 'Event Title : {} \nDate : {} \nDescription : {}'.format(data[0][0], data[0][1], data[0][2])
            self.event_infos.setText(event_text)
        except:
            self.event_infos.setText("")

    def init_widget(self):

        db = DatabaseQueries()
        db.cursor.execute("SELECT date FROM events")
        data = db.cursor.fetchall()

        for i, date in enumerate(data):

            current_date = date[0]
            qdate = QtCore.QDate.fromString(current_date)

            event_color = QtGui.QTextCharFormat()
            event_color.setFontPointSize(11)
            event_color.setForeground(QtGui.QColor(46, 204, 113, 255))
            self.calendar.setDateTextFormat(qdate, event_color)

