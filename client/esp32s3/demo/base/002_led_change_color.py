# !/usr/bin/env python
# -*- coding: utf-8 -*-

print("你好, MicroPython!")

"""
按boot键触发颜色改变
"""
from machine import Pin
from neopixel import NeoPixel
import time

# pin 是连接到 NeoPixel 数据引脚的输出引脚（Pin 48）
pin = Pin(48, Pin.OUT)

# 1 表示有 1 个 NeoPixel（1 个 RGB LED）
np = NeoPixel(pin, 1)
# np[0] 是第一个（也是唯一一个）NeoPixel 的颜色，颜色值是 (R, G, B) 格式。
# 这里设置红色 (10, 0, 0)，亮度为 10。
np[0] = (10,0,0)
# np.write() 将颜色值发送到 NeoPixel，实际更新 LED 的颜色。
np.write()

r, g, b = np[0]
def handle_interrupt(Pin):
    np[0] = (0, 0, 0)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 0, 10)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 0, 10)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 0, 0)
    np.write()
    time.sleep_ms(150)
    
    np[0] = (0, 10, 0)
    np.write()
    time.sleep_ms(150)
    
    print("test-usr key")

# 使用引脚 0 来连接按钮。
# Pin.IN 将引脚 0 设置为输入模式。
# Pin.PULL_UP 启用内部上拉电阻，使引脚默认电平为高电平（未按下时为逻辑高）
p0 = Pin(0)
p0.init(p0.IN, p0.PULL_UP)

# 设置中断, trigger=p0.IRQ_FALLING：触发条件为按键按下（电平从高到低）;
# handler=handle_interrupt：当中断触发时，调用 handle_interrupt 函数
p0.irq(trigger=p0.IRQ_FALLING, handler=handle_interrupt)