# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""

"""

__email__ = "jchastaing@studiohari.com"
__author__ = "Julien Chastaing"

import psycopg2


class DatabaseQueries():
    """docstring for ClassName"""
    def __init__(self):

        self.connect = psycopg2.connect(
            "dbname='AM' user='postgres' host='localhost' password='1003banane'")
        self.connect.autocommit = True
        self.cursor = self.connect.cursor()
