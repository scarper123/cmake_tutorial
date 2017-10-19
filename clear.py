#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-19 16:21:25
# @Author  : Shanming Liu
# @Link    : http://example.org
# @Version : $Id$

import os
import sys
import re
import shutil

args = sys.argv
SAVED = [r'^\w*?\.(c|cc|cpp)$', r'^\w*?\.h$', r'^CMakeLists.txt$', ]

SAVED = [re.compile(x) if isinstance(x, basestring) else x for x in SAVED]

DELETE_FOLDERS = ['CMakeFiles', 'CMakeTmp', 'hello\.dir']
DELETE_FOLDERS = [re.compile(x) if isinstance(
    x, basestring) else x for x in DELETE_FOLDERS]


def delete_folder(folder_name):
    basename = os.path.basename(folder_name)
    if basename in DELETE_FOLDERS:
        print('Delete folder -> %s' % folder_name)
        shutil.rmtree(folder_name)


def delete_file(filename):
    basename = os.path.basename(filename)
    # print('Base name -> %s' % basename)
    if any(map(lambda x: x.search(basename), SAVED)):
        return
    print('Delete file -> %s' % filename)
    os.remove(filename)


def clear_folder(folder):
    for root, dirs, filenames in os.walk(folder):
        for folder_name in dirs:
            delete_folder(os.path.join(root, folder_name))
        for filename in filenames:
            delete_file(os.path.join(root, filename))


for name in args:
    clear_folder(name)
