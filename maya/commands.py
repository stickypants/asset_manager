# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

from mayaPyManager import MayaPyManager


class MayaCommandsHandler():
    """docstring for MayaCommandsHandler"""
    def __init__(self):

        self.mayapy = MayaPyManager('C:/Program Files/Autodesk/Maya2017/bin/mayapy.exe', None)

    def reference_file(self, source_path, dest_path):

        command = "import maya.standalone; \
                   import maya.cmds as cmds;\
                   import sys; maya.standalone.initialize(name='python'); \
                   cmds.loadPlugin('mtoa');\
                   cmds.file('{}', o=True, f = True);\
                   cmds.file('{}', r=True, f = True);\
                   cmds.file(save=True, type='mayaAscii')".format(dest_path, source_path)

        output, errors = self.mayapy.run_command(command)

        print output, errors

if __name__ == "__main__":

    maya = MayaCommandsHandler()
    maya.reference_file("C:/Users/jucha/Desktop/rewind_tool/test2.ma", "C:/Users/jucha/Desktop/rewind_tool/test.ma")
