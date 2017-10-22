import pygal
from pygal.style import Style
from Qt import QtGui, QtCore, QtWidgets

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

        main_font = QtGui.QFont()
        main_font.setPointSize(10)
        main_font.setFamily("Arial")

        #self.setFixedSize(365, 350)

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
        pie_chart.title = "Asset Name"
        pie_chart.add('modeling', 19.5)
        pie_chart.add('rigging', 36.6)
        pie_chart.add('groom', 36.3)
        pie_chart.add('lookdev', 4.5)
        pie_chart.add('setdress', 4.5)
        pie_chart.add('layout', 36.3)
        pie_chart.add('animation', 36.3)
        pie_chart.add('render', 36.3)
        pie_chart.render_to_file('/tmp/chart.svg')

        chart_pixmap = QtGui.QPixmap('/tmp/chart.svg')
        resize_chart_pixmap = chart_pixmap.scaled(350, 260, transformMode=QtCore.Qt.SmoothTransformation)
        chart_label = QtWidgets.QLabel()
        chart_label.setPixmap(resize_chart_pixmap)
        chart_label.setAlignment(QtCore.Qt.AlignCenter)
        main_layout.addWidget(chart_label)

        sperator = QtWidgets.QFrame()
        sperator.setFrameStyle(QtWidgets.QFrame.HLine | QtWidgets.QFrame.Plain)
        sperator.setFixedHeight(1)
        main_layout.addWidget(sperator)

        total = QtWidgets.QLabel("Total Duration (hours) : 45 days")
        total.setFont(main_font)
        total.setAlignment(QtCore.Qt.AlignLeft)
        main_layout.addWidget(total)

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