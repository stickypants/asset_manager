# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
"""

import sys

from Qt import QtGui, QtCore, QtWidgets
from db.queries import DatabaseQueries

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"


class LogWidget(QtWidgets.QWidget):
    """docstring for ClassName"""

    def __init__(self):
        super(LogWidget, self).__init__()

        self.project_name = "am_demo"

        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(12)
        self.main_font.setFamily("Arial")

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        label = QtWidgets.QLabel("Log")
        label.setStyleSheet(
            "QLabel {color: #c0392b}")
        label.setFont(self.main_font)
        main_layout.addWidget(label)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        self.q_textedit = QtWidgets.QTextEdit()
        self.q_textedit.setFont(self.main_font)
        self.q_textedit.setReadOnly(True)
        main_layout.addWidget(self.q_textedit)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        pixmap = QtGui.QPixmap('C:/Users/jucha/Documents/@git/icons/refresh.png')
        refresh_icon = QtGui.QIcon(pixmap)

        refresh_btn = QtWidgets.QPushButton("Refesh")
        refresh_btn.setIcon(refresh_icon)
        refresh_btn.setFont(self.main_font)
        refresh_btn.clicked.connect(self.refresh_log)
        main_layout.addWidget(refresh_btn)

    def refresh_log(self):

        self.q_textedit.clear()

        db = DatabaseQueries()
        db.cursor.execute("SELECT * FROM log WHERE project = '{}'".format(self.project_name))
        data = db.cursor.fetchall()

        html = ''

        for log in data:

            html += '<div style="color:{}; padding:5px;"><p><b>{}</b></p><p>{}</p></div>'.format(log[2], log[3], log[1])

        self.q_textedit.insertHtml(html)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = LogWidget()
    window.show()
    result = app.exec_()
    sys.exit(result)
