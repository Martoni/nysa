#Distributed under the MIT licesnse.
#Copyright (c) 2014 Dave McCoy (dave.mccoy@cospandesign.com)

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

"""
Base Platform Script for use with Nysa Viewer
"""
__author__ = 'dave.mccoy@cospandesign.com (Dave McCoy)'

import argparse
import sys
import os
import time
from array import array as Array

import platform
SYSTEM_NAME = platform.system()
SYSTEM_DIST = ("","","")
if SYSTEM_NAME == "Linux":
    SYSTEM_DIST = platform.linux_distribution()
 

sys.path.append(os.path.join(os.path.dirname(__file__),
                             os.pardir))
class Platform(object):

    IS_PLATFORM = True

    def __init__(self, status):
        self.status = status
        self.dev_dict = {}

    def add_device_dict(self, unique_id, device):
        self.dev_dict[unique_id] = device

    def get_type(self):
        raise AssertionError("%s not implemented" % sys._getframe().f_code.co_name)

    def get_unique_ids(self):
        raise AssertionError("%s not implemented" % sys._getframe().f_code.co_name)

    def scan(self):
        raise AssertionError("%s not implemented" % sys._getframe().f_code.co_name)

    def test_build_tools(self):
        raise AssertionError("%s not implemented" % sys._getframe().f_code.co_name)

    def setup_platform(self):
        return

    def uninstall_platform(self):
        return

