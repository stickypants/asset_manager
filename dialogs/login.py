# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import sys

from Qt import QtGui, QtWidgets, QtCore
from db.queries import DatabaseQueries


class LoginDialog(QtWidgets.QDialog):

    current_user_signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)

        self.login = ''

        self.setWindowTitle("PROTOTYPE PIPELINE TOOL 2017 | JULIEN CHASTAING")
        self.setFixedSize(500, 250)

        main_font = QtGui.QFont()
        main_font.setPointSize(10)
        main_font.setFamily("Arial")

        dialogs_layout = QtWidgets.QVBoxLayout()
        self.setLayout(dialogs_layout)

        username_label = QtWidgets.QLabel("Username")
        username_label.setFont(main_font)
        dialogs_layout.addWidget(username_label)

        self.q_editline_login = QtWidgets.QLineEdit()
        self.q_editline_login.setFont(main_font)
        dialogs_layout.addWidget(self.q_editline_login)

        password_label = QtWidgets.QLabel("Password")
        password_label.setFont(main_font)
        dialogs_layout.addWidget(password_label)

        self.q_editline_password = QtWidgets.QLineEdit()
        self.q_editline_password.setFont(main_font)
        self.q_editline_password.setEchoMode(QtWidgets.QLineEdit.Password)
        dialogs_layout.addWidget(self.q_editline_password)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        dialogs_layout.addWidget(sperator)

        ok_btn = QtWidgets.QPushButton("Login")
        ok_btn.setFont(main_font)
        ok_btn.clicked.connect(self.check_password)
        dialogs_layout.addWidget(ok_btn)

    def check_password(self):

        self.login = self.q_editline_login.text()
        db_login = "'{}'".format(self.login)
        password = self.q_editline_password.text()

        db = DatabaseQueries()
        db.cursor.execute("SELECT password FROM users WHERE login = {}".format(db_login))
        data = db.cursor.fetchall()
        db_pasword = data[0][0]

        if password == db_pasword:
            self.close()
            self.current_user_signal.emit(self.login)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    d = LoginDialog()
    d.exec_()
