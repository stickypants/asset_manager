# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import os
import time
import shutil

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

        path = "C:\Users\jucha\Documents\@git\icons\{}.png".format(self.type)
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

        node = self.nodz.createNode(name='[E] '+ self.current_name, preset='node_preset_1', position=None)

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


class FileDialogs(QtWidgets.QDialog):
    """docstring for ClassName"""

    def __init__(self, nodz, selected_node):
        super(FileDialogs, self).__init__(nodz)

        self.current_name = ""
        self.type = 'file'
        self.nodz = nodz
        self.selected_node = selected_node

        self.setWindowTitle("AM")

        main_font = QtGui.QFont()
        main_font.setPointSize(10)
        main_font.setFamily("Arial")

        dialogs_layout = QtWidgets.QVBoxLayout(self)

        path = "C:\Users\jucha\Documents\@git\icons\{}.png".format(self.type)
        pixmap = QtGui.QPixmap(path)
        icon = QtWidgets.QLabel()
        icon.setPixmap(pixmap)
        icon.setAlignment(QtCore.Qt.AlignCenter)
        dialogs_layout.addWidget(icon)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        dialogs_layout.addWidget(sperator)

        self.name = QtWidgets.QLineEdit()
        self.name.setText(self.selected_node[0][4:])
        self.name.setFont(main_font)
        dialogs_layout.addWidget(self.name)

        ql_layout = QtWidgets.QHBoxLayout()
        dialogs_layout.addLayout(ql_layout)

        self.path = QtWidgets.QLineEdit()
        self.path.setFont(main_font)
        self.path.setReadOnly(True)
        ql_layout.addWidget(self.path)

        browse_btn = QtWidgets.QPushButton('...')
        browse_btn.clicked.connect(self.find_file)
        ql_layout.addWidget(browse_btn)

        self.file_type_cb = QtWidgets.QComboBox()
        self.file_type_cb.setFont(main_font)

        db = DatabaseQueries()
        db.cursor.execute("SELECT extension FROM filetypes")
        filetypes_data = db.cursor.fetchall()

        for i in filetypes_data:
            self.file_type_cb.addItem(i[0])

        dialogs_layout.addWidget(self.file_type_cb)

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

    def find_file(self):

        dialog = QtWidgets.QFileDialog()
        filepath = dialog.getOpenFileName(None, "Choose Your File ...")
        self.path.setText(filepath)

    def create_node(self):

        self.current_name = '{} | {}'.format(self.name.text(), self.file_type_cb.currentText())

        file_path = self.path.text()
        file_name = file_path.split('/')

        node_name = self.selected_node[0][4:]

        db = DatabaseQueries()
        db.cursor.execute("SELECT * FROM tasks WHERE name = {} ".format("'" + node_name + "'"))
        data = db.cursor.fetchall()
        output_path = data[0][2] + '/' + file_name[len(file_name) - 1]

        shutil.copyfile(file_path, output_path)

        db_name = "'{}'".format(self.current_name)
        db_path = "'{}'".format(output_path)
        db_extension = "'{}'".format(self.file_type_cb.currentText())
        db_task = "'{}'".format(self.selected_node[0][4:])

        node = self.nodz.createNode(name='[F] ' + self.current_name, preset='node_preset_2', position=None)

        self.nodz.createAttribute(node=node, name='Input', index=-1, preset='attr_preset_1',
                                  plug=False, socket=True, dataType=str)

        self.nodz.createAttribute(node=node, name='Output', index=-1, preset='attr_preset_1',
                                  plug=True, socket=False, dataType=str)

        db = DatabaseQueries()
        db.cursor.execute("INSERT INTO files (path, name, task, extension) VALUES ({}, {}, {}, {})".format(db_path, db_name, db_task, db_extension))

        self.close()
