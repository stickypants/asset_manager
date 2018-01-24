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

        self.subgraph_btn = QtWidgets.QPushButton("View SubGraph")
        self.subgraph_btn.setFont(self.main_font)
        self.subgraph_btn.setEnabled(False)
        self.main_layout.addWidget(self.subgraph_btn)

        self.previous_graph_btn = QtWidgets.QPushButton("Previous Graph")
        self.previous_graph_btn.setFont(self.main_font)
        self.main_layout.addWidget(self.previous_graph_btn)