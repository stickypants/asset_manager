# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

from Qt import QtGui, QtWidgets, QtCore
from db.queries import DatabaseQueries


class SearchBarDialogs(QtWidgets.QDialog):

    def __init__(self, nodz, current_project, parent=None):
        super(SearchBarDialogs, self).__init__(parent)

        self.nodz = nodz
        self.current_project = current_project

        self.setWindowTitle("PROTOTYPE PIPELINE TOOL 2017 | JULIEN CHASTAING")
        self.setFixedSize(250, 70)

        main_font = QtGui.QFont()
        main_font.setPointSize(10)
        main_font.setFamily("Arial")

        dialogs_layout = QtWidgets.QVBoxLayout()
        self.setLayout(dialogs_layout)

        db = DatabaseQueries()
        db.cursor.execute("SELECT * FROM assets")
        data = db.cursor.fetchall()

        entity_name_list = []
        self.entity_type = {}
        self.entity_tasks = {}

        for i in data:
            if i[6] == current_project:
                entity_name_list.append(i[0])
                self.entity_type[i[0]] = i[1]
                self.entity_tasks[i[0]] = i[7]
            else:
                continue

        model = QtCore.QStringListModel()
        model.setStringList(entity_name_list)

        completer = QtWidgets.QCompleter()
        completer.setModel(model)

        self.lineedit = QtWidgets.QLineEdit()
        self.lineedit.setCompleter(completer)
        self.lineedit.returnPressed.connect(self.create_node)
        dialogs_layout.addWidget(self.lineedit)

    def create_node(self):

        self.current_name = self.lineedit.text()
        self.type = self.entity_type[self.current_name]

        node = self.nodz.createNode(name=self.current_name, preset='node_preset_1', position=None)

        if self.type == 'set':
            self.nodz.createAttribute(node=node, name='Input', index=-1, preset='attr_preset_1',
                                      plug=False, socket=True, dataType=str)
        if self.type == 'shot':

            self.nodz.createAttribute(node=node, name='Input', index=-1, preset='attr_preset_1',
                                      plug=False, socket=True, dataType=str)
               
            self.nodz.createAttribute(node=node, name='Cam', index=-1, preset='attr_preset_1',
                                      plug=False, socket=True, dataType=str)

        self.nodz.createAttribute(node=node, name='Output', index=-1, preset='attr_preset_1',
                                  plug=True, socket=False, dataType=str)

        self.close()
        