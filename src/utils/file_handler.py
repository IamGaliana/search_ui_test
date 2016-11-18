#! /usr/bin/env python
# encoding:utf8
__author__ = 'gaoyanjun'

class FileHandler(object):

    def open_file(self, filename):
        file_obj = open(filename)
        try:
            all_text = file_obj.read()
        finally:
            file_obj.close()

    def read_file(self, filename):
        file_obj = open(filename, 'r')
        file_obj.read()
