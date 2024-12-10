# !/usr/bin/env python
# -*- coding: utf-8 -*-

import network
import time

class WifiOperate:
    def __init__(self, ssid=None, password=None):
        self.ssid = ssid
        self.password = password

    def with_p(self, ssid, password):
        self.ssid = ssid
        self.password = password
        return self

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)  # 激活WiFi接口

        # 如果已经连接，直接返回
        if wlan.isconnected():
            print("Already connected to WiFi")
            return wlan.ifconfig()

        # 开始连接WiFi
        print(f"Connecting to WiFi network: {self.ssid}...")
        wlan.connect(self.ssid, self.password)

        # 等待连接
        timeout = 10  # 超时时间（秒）
        start_time = time.time()
        while not wlan.isconnected():
            if time.time() - start_time > timeout:
                print("Failed to connect to WiFi: Timeout")
                return None
            time.sleep(1)

        # 成功连接
        print("Connected to WiFi!")
        print("Network configuration:", wlan.ifconfig())
        return wlan.ifconfig()


wifiOp = WifiOperate()
if __name__ == '__main__':
    wifiOp.with_p("leiax00-24g", "lax4832.").connect()
