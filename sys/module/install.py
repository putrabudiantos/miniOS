#!/usr/bin/python3 /bin/python3/filename

import sys
import os
from os.path import join, dirname, abspath
from os import listdir
from os.path import isfile, isdir, islink
from os.path import exists
from os.path import splitext
from display import *

class Installation:
    def __init__(self):
        pass

    @staticmethod
    def get_installation_path(self):
        return abspath(join(dirname(__file__), '..'))

    def choose(self):
        print("Choose your installation path:")
        print(self.get_installation_path())
        print()

        while True:
            path = input("Path: ")

    def main(self):
        if not exists(self.get_installation_path()):
            os.mkdir(self.get_installation_path())

        self.choose()




#
#   Copyright (c) 2021 Project CHIP Authors Putra
