# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
读取基础信息
"""

import gc
import os

import esp
import micropython

# 堆内存信息
free_heap = gc.mem_free()
alloc_heap = gc.mem_alloc()
total_heap = free_heap + alloc_heap

# 文件系统信息
fs_stat = os.statvfs('/')
total_fs = fs_stat[0] * fs_stat[2]
free_fs = fs_stat[0] * fs_stat[3]

print(f"Heap Memory - Free: {free_heap} bytes, Allocated: {alloc_heap} bytes, Total: {total_heap} bytes")
print(f"Filesystem - Total: {total_fs} bytes, Free: {free_fs} bytes")


# 输出内存信息
print('\nMem Info: ')
micropython.mem_info()

# 输出闪存信息
print(f"\nFlash Info: {esp.flash_size() / 1024 / 1024}Mb")
