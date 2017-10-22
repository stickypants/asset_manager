# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

from Qt import QtGui, QtWidgets, QtCore
from db.queries import DatabaseQueries


class ChooseProjectDialogs(QtWidgets.QDialog):
    """docstring for ClassName"""

    current_project_signal = QtCore.Signal(str)

    def __init__(self, parent=None):
        super(ChooseProjectDialogs, self).__init__(parent)

        self.setWindowTitle("PROTOTYPE PIPELINE TOOL 2017 | JULIEN CHASTAING")
        self.setFixedSize(250, 180)

        main_font = QtGui.QFont()
        main_font.setPointSize(10)
        main_font.setFamily("Arial")

        dialogs_layout = QtWidgets.QVBoxLayout()
        self.setLayout(dialogs_layout)

        path = "C:\Users\jucha\Documents\@git\icons\project.png"
        pixmap = QtGui.QPixmap(path)
        icon = QtWidgets.QLabel()
        icon.setPixmap(pixmap)
        icon.setAlignment(QtCore.Qt.AlignCenter)
        dialogs_layout.addWidget(icon)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        dialogs_layout.addWidget(sperator)

        infos = QtWidgets.QLabel("Choose your project !")
        infos.setFont(main_font)
        infos.setAlignment(QtCore.Qt.AlignLeft)
        dialogs_layout.addWidget(infos)

        self.combo_box = QtWidgets.QComboBox()
        self.combo_box.setFont(main_font)
        dialogs_layout.addWidget(self.combo_box)

        self.get_project_data()

        dialog_btn_layout = QtWidgets.QHBoxLayout()
        dialogs_layout.addLayout(dialog_btn_layout)

        ok_btn = QtWidgets.QPushButton("OK")
        ok_btn.setFont(main_font)
        ok_btn.clicked.connect(self.get_current_project)
        dialog_btn_layout.addWidget(ok_btn)

        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.setFont(main_font)
        cancel_btn.clicked.connect(self.close)
        dialog_btn_layout.addWidget(cancel_btn)

    def get_project_data(self):

        db = DatabaseQueries()

        db.cursor.execute("SELECT name FROM projects")
        project_data = db.cursor.fetchall()
        for project in project_data:
            self.combo_box.addItem(project[0])

    def get_current_project(self):

        current_project = self.combo_box.currentText()
        self.current_project_signal.emit(current_project)
        self.close()


class NewProjectDialogs(QtWidgets.QDialog):
    """docstring for ClassName"""

    def __init__(self, parent=None):
        super(NewProjectDialogs, self).__init__(parent)

        self.setWindowTitle("PROTOTYPE PIPELINE TOOL 2017 | JULIEN CHASTAING")
        self.setFixedSize(250, 180)

        main_font = QtGui.QFont()
        main_font.setPointSize(10)
        main_font.setFamily("Arial")

        dialogs_layout = QtWidgets.QVBoxLayout()
        self.setLayout(dialogs_layout)

        path = "C:\Users\jucha\Documents\@git\icons\project.png"
        pixmap = QtGui.QPixmap(path)
        icon = QtWidgets.QLabel()
        icon.setPixmap(pixmap)
        icon.setAlignment(QtCore.Qt.AlignCenter)
        dialogs_layout.addWidget(icon)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        dialogs_layout.addWidget(sperator)

        infos = QtWidgets.QLabel("Name")
        infos.setFont(main_font)
        infos.setAlignment(QtCore.Qt.AlignLeft)
        dialogs_layout.addWidget(infos)

        self.name = QtWidgets.QLineEdit()
        self.name.setFont(main_font)
        dialogs_layout.addWidget(self.name)

        path_name = QtWidgets.QLabel("Path")
        path_name.setFont(main_font)
        path_name.setAlignment(QtCore.Qt.AlignLeft)
        dialogs_layout.addWidget(path_name)

        self.path = QtWidgets.QLineEdit()
        self.path.setFont(main_font)
        dialogs_layout.addWidget(self.path)

        dialog_btn_layout = QtWidgets.QHBoxLayout(self)
        dialogs_layout.addLayout(dialog_btn_layout)

        ok_btn = QtWidgets.QPushButton("OK")
        ok_btn.setFont(main_font)
        ok_btn.clicked.connect(self.create_project)
        dialog_btn_layout.addWidget(ok_btn)

        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.setFont(main_font)
        cancel_btn.clicked.connect(self.close)
        dialog_btn_layout.addWidget(cancel_btn)

    def create_project(self):

        self.current_name = self.name.text()
        self.current_path = self.path.text()

        db = DatabaseQueries()
        db.cursor.execute("INSERT project (name, root_path) VALUES ({}, {})".format(self.current_name, self.current_path))

        self.close()
