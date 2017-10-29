# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import sys
import os
import nodz_main

from Qt import QtCore, QtGui, QtWidgets

from db.queries import DatabaseQueries

from dialogs.login import LoginDialogs
from dialogs.project import NewProjectDialogs, ChooseProjectDialogs
from dialogs.search_bar import SearchBarDialogs
from dialogs.entity import EntityDialogs

from widgets.calendar import CalendarWidget
from widgets.infos import InfoWidget
from widgets.graph import AnalyticsWidget
from widgets.library import TreeWidget


class MainWindow(QtWidgets.QMainWindow):
    """docstring for ClassName"""
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.current_user = ''
        self.current_project = ''
        self.selected_node = ''
        self.current_project_path = ''

        self.main_font = QtGui.QFont()
        self.main_font.setPointSize(12)
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
        self.node_menu = self.menubar.addMenu('Login/Project')
        self.node_menu.setFont(self.main_font)
        self.node_menu.addAction('Login', self.login)
        self.node_menu.addSeparator()
        self.node_menu.addAction('New', self.new_project)
        self.node_menu.addAction('Change Project', self.change_project)

        self.node_menu = self.menubar.addMenu('Graph')
        self.node_menu.setFont(self.main_font)
        self.node_menu.addAction('Save Graph', self.save_current_graph)
        self.node_menu.addAction('Load Graph', self.load_previous_graph)

        self.node_menu = self.menubar.addMenu('Entity Nodes')
        self.node_menu.setFont(self.main_font)
        self.node_menu.addAction('Character', lambda: self.entity_menu_action('character', self.current_project, self.current_project_path))
        self.node_menu.addAction('Props', lambda: self.entity_menu_action('props', self.current_project, self.current_project_path))
        self.node_menu.addAction('Set', lambda: self.entity_menu_action('set', self.current_project, self.current_project_path))
        self.node_menu.addSeparator()
        self.node_menu.addAction('Sequence', lambda: self.entity_menu_action('sequence', self.current_project, self.current_project_path))
        self.node_menu.addAction('Shot', lambda: self.entity_menu_action('shot', self.current_project, self.current_project_path))
        self.node_menu.addSeparator()
        self.node_menu.addAction('File')

        self.task_menu = self.menubar.addMenu('Taks Nodes')
        self.task_menu.setFont(self.main_font)
        self.task_menu.addAction('Modeling', lambda: self.create_new_task('modeling'))
        self.task_menu.addAction('Rigging', lambda: self.create_new_task('rigging'))
        self.task_menu.addAction('Groom', lambda: self.create_new_task('groom'))
        self.task_menu.addAction('Lookdev', lambda: self.create_new_task('lookdev'))
        self.task_menu.addSeparator()
        self.task_menu.addAction('Set Dress', lambda: self.create_new_task('setdress'))
        self.task_menu.addAction('Lighting', lambda: self.create_new_task('lighting'))
        self.task_menu.addSeparator()
        self.task_menu.addAction('Layout', lambda: self.create_new_task('layout'))
        self.task_menu.addAction('Animation', lambda: self.create_new_task('animation'))
        self.task_menu.addAction('Render', lambda: self.create_new_task('render'))
        self.task_menu.addAction('Compositing', lambda: self.create_new_task('compositing'))

        self.utility_menu = self.menubar.addMenu('Utility Nodes')
        self.node_menu.setFont(self.main_font)

        self.main_layout = QtWidgets.QVBoxLayout(self.widget)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.second_layout = QtWidgets.QHBoxLayout(self.widget)
        self.main_layout.addLayout(self.second_layout)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        self.nodz = nodz_main.Nodz(None)
        self.nodz.initialize()
        self.nodz.signal_NodeSelected.connect(self.update_selected_node_infos)
        self.nodz.signal_KeyPressed.connect(self.key_event)
        self.second_layout.addWidget(self.nodz)

        self.calendar = CalendarWidget()
        self.infos = InfoWidget()
        self.graph = AnalyticsWidget()
        self.tree = TreeWidget(self.nodz)

        self.tab = QtWidgets.QTabWidget()
        self.tab.setFont(self.main_font)
        self.tab.setTabShape(QtWidgets.QTabWidget.Triangular)

        self.tab.addTab(self.infos, "Infos")
        self.tab.addTab(self.calendar, "Calendar")
        self.tab.addTab(self.graph, "Graphs")
        self.tab.addTab(self.tree, "Library")

        self.second_layout.addWidget(self.tab)

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
        self.fld_btn.clicked.connect(self.open_folder_btn)
        self.footer_layout.addWidget(self.fld_btn)

        self.save_btn = QtWidgets.QPushButton()
        self.pixmap = QtGui.QPixmap("C:\Users\jucha\Documents\@git\icons\save.png")
        self.icon = QtGui.QIcon(self.pixmap)
        self.save_btn.setIcon(self.icon)
        self.save_btn.setFont(self.main_font)
        self.footer_layout.addWidget(self.save_btn)

        self.show()

    def login(self):

        d = LoginDialogs(self.widget)
        d.show()
        d.current_user_signal.connect(self.update_login)

    def update_login(self, login):

        self.current_user = login
        self.infos.login.setText(login)

    def new_project(self):

        d = NewProjectDialogs(self.widget)
        d.show()

    def change_project(self):

        d = ChooseProjectDialogs(self.widget)
        d.show()
        d.current_project_signal.connect(self.update_project)

    def update_project(self, project):

        self.current_project = project
        db_project = "'{}'".format(self.current_project)

        db = DatabaseQueries()
        db.cursor.execute("SELECT root_path FROM projects WHERE name = {}".format(db_project))
        data = db.cursor.fetchall()

        path = data[0][0]
        self.current_project_path = path.replace("\\", "/")
        self.infos.project.setText(self.current_project)
        self.tree.project_name = self.current_project

    def key_event(self, event):

        if event == 32:  # spacebar
            d = SearchBarDialogs(self.nodz, self.current_project, self.widget)
            d.show()

    def update_selected_node_infos(self, current_node):

        self.selected_node = current_node
        self.graph.create_graph(self.selected_node)

        if len(self.selected_node) != 0:
            node_name = "'{}'".format(self.selected_node[0])
            project_name = "'{}'".format(self.current_project)
            db = DatabaseQueries()

            db.cursor.execute("SELECT * FROM assets WHERE name = {} AND project = {}".format(node_name, project_name))
            data = db.cursor.fetchall()

            self.infos.name.setText(data[0][0])
            self.infos.type.setText(data[0][1])
            self.infos.author.setText(data[0][2])
            self.infos.date.setText(data[0][3])

            self.full_path.setText(data[0][4])

        else:
            self.infos.name.setText('')
            self.infos.type.setText('')
            self.infos.author.setText('')
            self.infos.date.setText('')
            self.full_path.setText('')

    def save_current_graph(self):
        self.nodz.saveGraph("C:\Users\jucha\Documents\@git\saved_graph.json")

    def load_previous_graph(self):
        self.nodz.loadGraph("C:\Users\jucha\Documents\@git\saved_graph.json")

    def entity_menu_action(self, entity_name, project, current_project_path):
        d = EntityDialogs(self.nodz, entity_name, project, current_project_path)
        d.exec_

    def open_folder_btn(self):

        path = str(self.full_path.text() + '/')
        os.startfile(path)

    def create_new_task(self, task_name):

        current_selection = self.infos.name.text()

        name = current_selection + '_' + task_name
        path = self.full_path.text()
        os.mkdir(path + '/{}'.format(name))

        node = self.nodz.createNode(name=name, preset='node_preset_1', position=None)

        self.nodz.createAttribute(node=node, name='Input', index=-1, preset='attr_preset_1',
                                  plug=False, socket=True, dataType=str)

        self.nodz.createAttribute(node=node, name='Output', index=-1, preset='attr_preset_1',
                                  plug=True, socket=False, dataType=str)

        db = DatabaseQueries()
        current_selection = "'{}'".format(current_selection)
        db.cursor.execute("UPDATE assets SET {} = True WHERE name = {} AND project = '{}';".format(task_name, current_selection, self.current_project))


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    main_win = MainWindow()

    stylesheet_path = 'C:/Users/jucha/Documents/@git/stylesheet.css'

    with open(stylesheet_path, 'r') as f:
        app.setStyleSheet(f.read())

    app.exec_()
