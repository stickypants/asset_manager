# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

import sys

from Qt import QtGui, QtCore, QtWidgets
from db.queries import DatabaseQueries

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"


class TreeWidget(QtWidgets.QWidget):
    """docstring for ClassName"""

    def __init__(self, nodz):
        super(TreeWidget, self).__init__()

        self.nodz = nodz
        self.project_name = ""

        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(12)
        self.main_font.setFamily("Arial")

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        label = QtWidgets.QLabel("Project Library")
        label.setStyleSheet(
            "QLabel {color: #c0392b}")
        label.setFont(self.main_font)
        main_layout.addWidget(label)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        self.tree = QtWidgets.QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setFont(self.main_font)
        self.tree.itemDoubleClicked.connect(self.create_node)
        main_layout.addWidget(self.tree)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        pixmap = QtGui.QPixmap('C:/Users/jucha/Documents/@git/icons/refresh.png')
        refresh_icon = QtGui.QIcon(pixmap)

        refresh_btn = QtWidgets.QPushButton("Refesh")
        refresh_btn.setIcon(refresh_icon)
        refresh_btn.setFont(self.main_font)
        refresh_btn.clicked.connect(self.init_tree)
        main_layout.addWidget(refresh_btn)

    def init_tree(self):

        self.tree.clear()

        entity_type = ['character', 'props', 'set', 'sequence', 'shot', 'file']

        project_item = QtWidgets.QTreeWidgetItem(['{}'.format(self.project_name)])
        self.tree.addTopLevelItem(project_item)

        for entity in entity_type:
            category_item = QtWidgets.QTreeWidgetItem(['{}'.format(entity)])
            project_item.addChild(category_item)

            db = DatabaseQueries()
            db.cursor.execute("SELECT * FROM assets WHERE project = '{}' AND type = '{}'".format(self.project_name, entity))
            data = db.cursor.fetchall()

            for asset in data:
                asset_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0])])
                category_item.addChild(asset_item)

                if asset[7] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_modeling')])
                    asset_item.addChild(task_item)

                if asset[8] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_rigging')])
                    asset_item.addChild(task_item)

                if asset[9] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_groom')])
                    asset_item.addChild(task_item)

                if asset[10] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_lookdev')])
                    asset_item.addChild(task_item)

                if asset[11] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_setdress')])
                    asset_item.addChild(task_item)

                if asset[12] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_lighting')])
                    asset_item.addChild(task_item)

                if asset[13] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_layout')])
                    asset_item.addChild(task_item)

                if asset[14] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_animation')])
                    asset_item.addChild(task_item)

                if asset[15] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_render')])
                    asset_item.addChild(task_item)

                if asset[16] == True:
                    task_item = QtWidgets.QTreeWidgetItem(['{}'.format(asset[0] + '_compositing')])
                    asset_item.addChild(task_item)

        self.tree.expandAll()

    def create_node(self, item_name):

        node_name = item_name.text(0)

        node = self.nodz.createNode(name=node_name, preset='node_preset_1', position=None)

        self.nodz.createAttribute(node=node, name='Input', index=-1, preset='attr_preset_1',
                                  plug=False, socket=True, dataType=str)

        self.nodz.createAttribute(node=node, name='Output', index=-1, preset='attr_preset_1',
                                  plug=True, socket=False, dataType=str)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = TreeWidget()
    window.show()
    result = app.exec_()
    sys.exit(result)
