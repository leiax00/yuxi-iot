# 固件构建

microPython官方文档: [https://micropython.org/download/ESP32_GENERIC_S3/](https://micropython.org/download/ESP32_GENERIC_S3/)

串口驱动下载: [https://www.wch.cn/downloads/CH343SER_EXE.html](https://www.wch.cn/downloads/CH343SER_EXE.html)

## esptool

esptool官方地址: [https://github.com/espressif/esptool](https://github.com/espressif/esptool)

### 烧录方式

1. 复制 `esptool.py` 到 [esptool.py](esptool_starter/esptool.py)
2. 复制固件到 [sources](resources) 目录下, 例如: ESP32_GENERIC_S3-20241025-v1.24.0.bin
3. 安装依赖: `pip install -r requirements.txt`
4. 擦除原有固件
    ```bash
    # 注意修改串口号 COM8
    python -m esptool --chip esp32s3 --port COM3 erase_flash
    ```
5. 烧录固件
    ```bash
   python -m esptool --chip esp32s3 --port COM3 write_flash -z 0x0000 resources/firmware.bin
    ```

### 固件说明

| 固件                                                                                         | 说明                             |
|--------------------------------------------------------------------------------------------|--------------------------------|
| [ESP32-S3-N16R8-MPY-V1.1.bin](resources%2FESP32-S3-N16R8-MPY-V1.1.bin)                     | microPython_v1.19.1, 开启了psram  |
| [ESP32_GENERIC_S3-20241025-v1.24.0.bin](resources%2FESP32_GENERIC_S3-20241025-v1.24.0.bin) | microPython_v1.24.0, 未开启了psram |
