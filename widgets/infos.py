# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

from Qt import QtCore, QtGui, QtWidgets


class InfoWidget(QtWidgets.QWidget):
    """docstring for ClassName"""

    def __init__(self):
        super(InfoWidget, self).__init__()

        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(12)
        self.main_font.setFamily("Arial")

        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.project = QtWidgets.QLabel("")
        self.project.setFont(self.main_font)
        self.project.setStyleSheet(
            "QLabel {color: #c0392b}")
        self.project.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.project)

        self.login = QtWidgets.QLabel("")
        self.login.setFont(self.main_font)
        self.login.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.login)

        self.frame_snap = QtWidgets.QGroupBox(self)
        self.frame_snap.setFixedSize(365, 350)

        self.snap_layout = QtWidgets.QVBoxLayout()
        self.frame_snap.setLayout(self.snap_layout)

        self.snapshot = QtGui.QPixmap("C:/Users/jucha/Documents/maya/2017/scripts/WIP_SOURCECODE/LoginSystem_IMAGES/Snapshot.png")
        self.snapshot_result_label = QtWidgets.QLabel()
        self.snapshot_result_label.setPixmap(self.snapshot)
        self.snapshot_result_label.setAlignment(QtCore.Qt.AlignCenter)
        self.snap_layout.addWidget(self.snapshot_result_label)

        self.snap_btn = QtWidgets.QPushButton("Take Snapshot")
        self.snap_btn.setFont(self.main_font)
        self.snap_layout.addWidget(self.snap_btn)

        self.main_layout.addWidget(self.frame_snap)

        self.name = QtWidgets.QLabel("")
        self.name.setFont(self.main_font)
        self.name.setStyleSheet(
            "QLabel {color: #c0392b}")
        self.name.setAlignment(QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.name)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        self.main_layout.addWidget(sperator)

        self.type = QtWidgets.QLabel("")
        self.type.setFont(self.main_font)
        self.type.setStyleSheet(
            "QLabel {color: #eff0f1}")
        self.type.setAlignment(QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.type)

        self.author = QtWidgets.QLabel("")
        self.author.setFont(self.main_font)
        self.author.setStyleSheet(
            "QLabel {color: #eff0f1}")
        self.author.setAlignment(QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.author)

        self.date = QtWidgets.QLabel("")
        self.date.setFont(self.main_font)
        self.date.setStyleSheet(
            "QLabel {color: #eff0f1}")
        self.date.setAlignment(QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.date)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        self.main_layout.addWidget(sperator)

        self.task_label = QtWidgets.QLabel("Task Status")
        self.task_label.setFont(self.main_font)
        self.task_label.setAlignment(QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.task_label)

        self.status_combox = QtWidgets.QComboBox()
        self.status_combox.setFont(self.main_font)
        self.main_layout.addWidget(self.status_combox)

        status_list = ['wts', 'ip', 'rev', 'rtk', 'fin']
        status_name = ['Waiting to Start', 'In Progress', 'To Review', 'Retake', 'Ok']

        for i, status in enumerate(status_list):
            self.status_combox.addItem(QtGui.QIcon("C:/Users/jucha/Documents/@git/icons/{}.png".format(status)), status_name[i])

        self.version_label = QtWidgets.QLabel("Versions")
        self.version_label.setFont(self.main_font)
        self.version_label.setAlignment(QtCore.Qt.AlignLeft)
        self.main_layout.addWidget(self.version_label)

        self.version_combox = QtWidgets.QComboBox()
        self.version_combox.setFont(self.main_font)
        self.main_layout.addWidget(self.version_combox)
