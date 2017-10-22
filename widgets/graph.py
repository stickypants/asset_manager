import pygal
from pygal.style import Style
from Qt import QtGui, QtCore, QtWidgets

from db.queries import DatabaseQueries

# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"


class AnalyticsWidget(QtWidgets.QWidget):
    """docstring for ClassName"""

    def __init__(self):
        super(AnalyticsWidget, self).__init__()

        self.selected_asset_name = ''

        main_font = QtGui.QFont()
        main_font.setPointSize(12)
        main_font.setFamily("Arial")

        main_layout = QtWidgets.QVBoxLayout(self)

        infos = QtWidgets.QLabel("Timelogs (hours)")
        infos.setFont(main_font)
        infos.setStyleSheet(
            "QLabel {color: #c0392b}")
        infos.setAlignment(QtCore.Qt.AlignLeft)
        main_layout.addWidget(infos)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        chart_pixmap = QtGui.QPixmap('/tmp/chart.svg')
        resize_chart_pixmap = chart_pixmap.scaled(350, 260, transformMode=QtCore.Qt.SmoothTransformation)
        self.chart_label = QtWidgets.QLabel()
        self.chart_label.setPixmap(resize_chart_pixmap)
        self.chart_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.chart_label)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        self.total = QtWidgets.QLabel("Total Duration (hours) :")
        self.total.setFont(main_font)
        self.total.setAlignment(QtCore.Qt.AlignLeft)
        main_layout.addWidget(self.total)

        estimated = QtWidgets.QLabel("Estimated Duration (hours) : 40 days")
        estimated.setFont(main_font)
        estimated.setAlignment(QtCore.Qt.AlignLeft)
        main_layout.addWidget(estimated)

        overdue = QtWidgets.QLabel("Overdue : 112.5 %")
        overdue.setFont(main_font)
        overdue.setStyleSheet(
            "QLabel {color: #c0392b}")
        overdue.setAlignment(QtCore.Qt.AlignLeft)
        main_layout.addWidget(overdue)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        timelog_label = QtWidgets.QLabel("Timelog Duration (hours)")
        timelog_label.setFont(main_font)
        infos.setStyleSheet(
            "QLabel {color: #c0392b}")
        timelog_label.setAlignment(QtCore.Qt.AlignLeft)
        main_layout.addWidget(timelog_label)

        self.timelog_duration = QtWidgets.QLineEdit()
        self.timelog_duration.setFont(main_font)
        main_layout.addWidget(self.timelog_duration)

        create_timelog_btn = QtWidgets.QPushButton("Create New Timelog")
        create_timelog_btn.setFont(main_font)
        create_timelog_btn.clicked.connect(self.create_timelog)
        main_layout.addWidget(create_timelog_btn)

    def create_graph(self, selected_node):

        self.selected_asset_name = selected_node[0]
        bd_name = "'{}'".format(self.selected_asset_name)

        custom_style = Style(background='#2a2a2a',
                             plot_background='#2a2a2a',
                             foreground='#eff0f1',
                             foreground_strong='#eff0f1',
                             foreground_subtle='#eff0f1',
                             opacity='1',
                             opacity_hover='1',
                             font_family='Arial',
                             title_font_family='Arial',
                             transition='400ms ease-in',
                             title_font_size=25,
                             legend_font_size=25,
                             colors=('#2ecc71', '#3498db', '#e67e22', '#c0392b',
                                     '#34495e', '#95a5a6', '#bdc3c7', '#9b59b6'))

        pie_chart = pygal.Pie(inner_radius=.4, style=custom_style)
        pie_chart.title = self.selected_asset_name

        db = DatabaseQueries()

        db.cursor.execute("SELECT * FROM timelogs WHERE entity = {}".format(bd_name))
        data = db.cursor.fetchall()

        total_duration = 0

        for timelog in data:
            total_duration += float(timelog[1])
            pie_chart.add(timelog[3], timelog[1])

        self.total.setText("Total Duration (hours) : {} hours".format(total_duration))

        pie_chart.render_to_file('/tmp/chart.svg')
        chart_pixmap = QtGui.QPixmap('/tmp/chart.svg')
        resize_chart_pixmap = chart_pixmap.scaled(350, 260, transformMode=QtCore.Qt.SmoothTransformation)
        self.chart_label.setPixmap(resize_chart_pixmap)

    def create_timelog(self):

        entity = self.selected_asset_name
        duration = self.timelog_duration.text()
        task = entity.split('_')
        task = task[len(task) - 1]

        print entity, duration, task
