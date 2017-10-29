# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import os
import time

from db.queries import DatabaseQueries
from Qt import QtCore, QtGui, QtWidgets


class EntityDialogs(QtWidgets.QDialog):
    """docstring for ClassName"""

    def __init__(self, nodz, entity_type, current_project, project_path):
        super(EntityDialogs, self).__init__(nodz)

        self.current_name = ""
        self.type = entity_type
        self.nodz = nodz
        self.project = current_project
        self.path = project_path

        print self.project

        self.setWindowTitle("AM")

        main_font = QtGui.QFont()
        main_font.setPointSize(10)
        main_font.setFamily("Arial")

        dialogs_layout = QtWidgets.QVBoxLayout(self)

        path = "C:\Users\jucha\Desktop\memoire\icons\{}.png".format(self.type)
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

        dialog_btn_layout = QtWidgets.QHBoxLayout(self)
        dialogs_layout.addLayout(dialog_btn_layout)

        ok_btn = QtWidgets.QPushButton("OK")
        ok_btn.setFont(main_font)
        ok_btn.clicked.connect(self.create_node)
        dialog_btn_layout.addWidget(ok_btn)

        cancel_btn = QtWidgets.QPushButton("Cancel")
        cancel_btn.setFont(main_font)
        cancel_btn.clicked.connect(self.close)
        dialog_btn_layout.addWidget(cancel_btn)

        self.show()

    def create_node(self):

        self.current_name = self.name.text()

        node = self.nodz.createNode(name=self.current_name, preset='node_preset_1', position=None)

        self.nodz.createAttribute(node=node, name='Input', index=-1, preset='attr_preset_1',
                                  plug=False, socket=True, dataType=str)

        self.nodz.createAttribute(node=node, name='Output', index=-1, preset='attr_preset_1',
                                  plug=True, socket=False, dataType=str)

        db = DatabaseQueries()

        path = self.path + '/{}/{}'.format(self.type, self.current_name)
        os.mkdir(path)
        thumbs_path = self.path + '/{}/{}/thumbnails'.format(self.type, self.current_name)
        os.mkdir(thumbs_path)

        creation_date = time.strftime("%b %d %Y %H:%M:%S")

        db_date = "'{}'".format(creation_date)
        db_name = "'{}'".format(self.current_name)
        db_author = "'{}'".format('jchastaing')
        db_type = "'{}'".format(self.type)
        db_path = "'{}'".format(path)
        db_t_path = "'{}'".format(thumbs_path)
        db_project = "'{}'".format(self.project)

        db.cursor.execute("INSERT INTO assets (name, type, author, creation_date, path, thumnails_path, project) VALUES ({}, {}, {}, {}, {}, {}, {})".format(db_name, db_type, db_author, db_date, db_path, db_t_path, db_project))

        self.close()
