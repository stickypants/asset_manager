import maya.standalone
import maya.cmds as cmds
import sys

sys.path.append('C:\solidangle\mtoadeploy\2017\scripts')

maya.standalone.initialize(name='python')
cmds.loadPlugin('mtoa')

cmds.polyCube(n='toto')
cmds.commandPort(5000)

cmds.file(rename='C:/Users/jucha/Desktop/rewind_tool/test.ma')
cmds.file(save=True, type='mayaAscii')
