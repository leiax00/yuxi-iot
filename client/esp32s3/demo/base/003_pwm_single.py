# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
用于测试控制舵机转动角度
设置舵机的角度:
            0.5ms--------------0度；
            1.0ms------------45度；
            1.5ms------------90度；
            2.0ms-----------135度；
            2.5ms-----------180度；
PWM信号，频率为50Hz（舵机通常使用50Hz的PWM信号）, 1s/50 = 20ms
占空比通常以分辨率表示（例如 0-1023）, 微秒计算
因此计算:
45度 ----------- pwm.duty(1 / 20 * 1023)
直接用时间, 纳秒计算
45度 ----------- pwm.duty_ns(1 * 1000)

"""

import time

from machine import Pin, PWM


class PwmOperate:
    def __init__(self, pin_num=13):
        # 连接舵机信号线的GPIO引脚
        self.servo_pin = pin_num
        # 初始化PWM信号，频率为50Hz（舵机通常使用50Hz的PWM信号）
        self.pwm = PWM(Pin(self.servo_pin), freq=50)

    def set_angle(self, angle):
        """
        设置舵机的角度
        :param angle: 角度值（0-180）
        """
        # 将角度转换为PWM占空比，500~2500微秒（0.5ms~2.5ms）为舵机有效范围
        duty_us = 500 + (angle / 180.0) * 2000  # 转换为微秒
        # PWM信号的周期，通常是 20ms（50Hz）用于舵机。
        duty_cycle = int(duty_us / 20000 * 1023)  # 转换为占空比（0-1023）
        self.pwm.duty_ns(int(duty_us * 1000))

    def angle_loop(self):
        try:
            while True:
                # 示例：让舵机在 0° - 180° - 0° 来回摆动
                for angle in range(0, 181, 10):
                    self.set_angle(angle)
                    time.sleep(0.05)
                for angle in range(180, -1, -10):
                    self.set_angle(angle)
                    time.sleep(0.05)
        except KeyboardInterrupt:
            print("Finish by exception!")
            self.pwm.deinit()  # 释放PWM资源

    def multi_click(self, count=1, tap_time=0.05):
        while count > 0:
            self.set_angle(15)
            time.sleep(tap_time)
            self.set_angle(0)
            count -= 1
            time.sleep(0.1)
        else:
            self.set_angle(0)


pwnOp = PwmOperate()
if __name__ == '__main__':
    # pwnOp.angle_loop()
    pwnOp.multi_click(2)
