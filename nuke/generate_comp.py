# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Arnold Standard AOV

# Direct Diffuse
# Indirect Diffuse
# Direct Specular
# Indirect Specular
# Reflection
# Emission
# AO
# ZDepth

# Passes folder must be named as follow.

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import os

# put your images folder here !
path = ''

images_folders = os.listdir(path)

for folder in images_folders:
    nuke.nodes.Read(name = folder, file="")