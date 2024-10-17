# !/usr/bin/env python
# -*- coding: utf-8 -*-

from internal.cam.cam_mgr import mgr


class AppMgr:
    @staticmethod
    def init():
        print('start to init App!')
        mgr.start()

    @staticmethod
    async def release():
        print('Start to destroy app!')
        await mgr.release()
