# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import pyscreenshot as ImageGrab
from db.queries import DatabaseQueries


def create_screenshot(asset_name, asset_path):

    thumbnails_path = asset_path + 'thumnails.png'

    img = ImageGrab.grab()
    img.save(thumbnails_path, 'png')

    db = DatabaseQueries()
    db.cursor.execute("UPDATE assets SET thumnails_path = '{}' WHERE name = '{}')".format(asset_name, asset_path))

    return thumbnails_path

if __name__ == '__main__':

    create_screenshot('toto', r'C:\Users\jucha\Desktop\memoire\project_test\\')