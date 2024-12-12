# !/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()

from yuxi.base.d004_wifi import wifiOp
wifiOp.try_connect([
    ("leiax00-24g", "lax4832."),
    ("uu_exp", "lax4832.")
])