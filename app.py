# !/usr/bin/env python
# -*- coding: utf-8 -*-
from szpy.config.app_config import app_conf
from szpy.config.c_nacos import nacos_manager
from szpy.modules import xxl
from szpy.modules.db import sqlalchemy, redis


class AppMgr:
    @staticmethod
    def init():
        print('start to init App!')

    @staticmethod
    def release():
        print('Start to destroy app!')
