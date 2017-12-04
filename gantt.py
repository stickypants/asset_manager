# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

import sys
import time
import datetime

from Qt import QtGui, QtCore, QtWidgets
from db.queries import DatabaseQueries


__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

class GanttWidget(QtWidgets.QWidget):
    """docstring for ClassName"""

    def __init__(self):
        super(GanttWidget, self).__init__()

        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(12)
        self.main_font.setFamily("Arial")

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        label = QtWidgets.QLabel("Gantt")
        label.setStyleSheet(
            "QLabel {color: #c0392b}")
        label.setFont(self.main_font)
        main_layout.addWidget(label)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        self.table_view = QtWidgets.QTableWidget()
        self.table_view.setColumnCount(40)
        self.init_headers()
        main_layout.addWidget(self.table_view)

        create_btn = QtWidgets.QPushButton("Create New Phase")
        create_btn.setFont(self.main_font)
        create_btn.clicked.connect(self.add_phase)
        main_layout.addWidget(create_btn)

    def init_headers(self):

        self.header_list = ['Phase Name', 'Start Date', 'End Date', 'Color']
        date = datetime.datetime.now().strftime('%U - %b - %Y')
        self.header_list.append(date)

        for i in range(1, 36):
            modified_date = datetime.datetime.now() + datetime.timedelta(weeks=i)
            modified_date = modified_date.strftime('%U - %b - %Y')
            self.header_list.append(modified_date)

        self.table_view.setHorizontalHeaderLabels(self.header_list)

    def add_phase(self):

        row_count = self.table_view.rowCount()
        self.table_view.insertRow(row_count)

        self.table_view.setItem(row_count, 0, QtWidgets.QTableWidgetItem('Modeling Layout'))
        self.table_view.setItem(row_count, 1, QtWidgets.QTableWidgetItem('12-11-17'))
        self.table_view.setItem(row_count, 2, QtWidgets.QTableWidgetItem('12-12-17'))
        self.table_view.setItem(row_count, 3, QtWidgets.QTableWidgetItem('255, 0, 125, 255'))

        for date in self.header_list:
            pass


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = GanttWidget()
    window.show()
    result = app.exec_()
    sys.exit(result)
