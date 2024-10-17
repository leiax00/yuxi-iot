# !/usr/bin/env python
# -*- coding: utf-8 -*-

from internal.cam.capture import *

class AppMgr:
    @staticmethod
    def init():
        print('start to init App!')

    @staticmethod
    def release():
        print('Start to destroy app!')
