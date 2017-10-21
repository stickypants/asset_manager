# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import sys
import nodz_main
from Qt import QtCore, QtGui, QtWidgets

from dialogs.login import LoginDialog


class MainWindow(QtWidgets.QMainWindow):
    """docstring for ClassName"""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.current_user = ''

        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(10)
        self.main_font.setFamily("Arial")

        self.infos_font = QtGui.QFont()
        self.infos_font.setPointSize(12)
        self.infos_font.setFamily("Arial")

        self.setWindowTitle("PROTOTYPE PIPELINE TOOL 2017 | JULIEN CHASTAING")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)

        self.menubar = self.menuBar()
        self.menubar.setFont(self.main_font)
        self.node_menu = self.menubar.addMenu('Project')
        self.node_menu.setFont(self.main_font)
        self.node_menu.addAction('Login', self.login)
        self.node_menu.addAction('New')
        self.node_menu.addAction('Change Project')

        self.node_menu = self.menubar.addMenu('Graph')
        self.node_menu.addAction('Save Graph')
        self.node_menu.addAction('Load Graph')

        self.node_menu = self.menubar.addMenu('Entity Nodes')
        self.node_menu.addAction('Character')
        self.node_menu.addAction('Props')
        self.node_menu.addAction('Set')
        self.node_menu.addSeparator()
        self.node_menu.addAction('Sequence')
        self.node_menu.addAction('Shot')
        self.node_menu.addAction('Cam')
        self.node_menu.addSeparator()
        self.node_menu.addAction('File')

        self.task_menu = self.menubar.addMenu('Taks Nodes')
        self.task_menu.addAction('Modeling')
        self.task_menu.addAction('Rigging')
        self.task_menu.addAction('Groom')
        self.task_menu.addAction('Lookdev')
        self.task_menu.addSeparator()
        self.task_menu.addAction('Set Dress')
        self.task_menu.addAction('Lighting')
        self.task_menu.addSeparator()
        self.task_menu.addAction('Layout')
        self.task_menu.addAction('Animation')
        self.task_menu.addAction('Render')
        self.task_menu.addAction('Compositing')

        self.utility_menu = self.menubar.addMenu('Utility Nodes')

        self.main_layout = QtWidgets.QVBoxLayout(self.widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.second_layout = QtWidgets.QHBoxLayout(self.widget)
        self.main_layout.addLayout(self.second_layout)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.nodz = nodz_main.Nodz(None)
        self.nodz.initialize()
        self.second_layout.addWidget(self.nodz)

        self.footer_layout = QtWidgets.QHBoxLayout(self.widget)
        self.main_layout.addLayout(self.footer_layout)

        self.full_path = QtWidgets.QLineEdit()
        self.full_path.setReadOnly(True)
        self.full_path.setFont(self.main_font)
        self.footer_layout.addWidget(self.full_path)

        self.opn_btn = QtWidgets.QPushButton()
        self.pixmap = QtGui.QPixmap("C:\Users\jucha\Documents\@git\icons\play.png")
        self.icon = QtGui.QIcon(self.pixmap)
        self.opn_btn.setIcon(self.icon)
        self.opn_btn.setFont(self.main_font)
        self.footer_layout.addWidget(self.opn_btn)

        self.fld_btn = QtWidgets.QPushButton()
        self.pixmap = QtGui.QPixmap("C:\Users\jucha\Documents\@git\icons\dossier.png")
        self.icon = QtGui.QIcon(self.pixmap)
        self.fld_btn.setIcon(self.icon)
        self.fld_btn.setFont(self.main_font)
        self.footer_layout.addWidget(self.fld_btn)

        self.save_btn = QtWidgets.QPushButton()
        self.pixmap = QtGui.QPixmap("C:\Users\jucha\Documents\@git\icons\save.png")
        self.icon = QtGui.QIcon(self.pixmap)
        self.save_btn.setIcon(self.icon)
        self.save_btn.setFont(self.main_font)
        self.footer_layout.addWidget(self.save_btn)

        self.show()

    def login(self):

        d = LoginDialog(self.widget)
        d.show()
        d.current_user_signal.connect(self.update_login)

    def update_login(self, login):
        
        self.current_user = login

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()

    stylesheet_path = 'C:/Users/jucha/Documents/@git/stylesheet.css'

    with open(stylesheet_path, 'r') as f:
        app.setStyleSheet(f.read())

    app.exec_()
