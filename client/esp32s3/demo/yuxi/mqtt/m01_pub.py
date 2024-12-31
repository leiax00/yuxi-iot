# !/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from umqtt.simple import MQTTClient


def main(server="localhost"):
    c = MQTTClient("esp32s3-mqtt", server)
    try:
        c.connect()
        c.publish(b"root/esp32s3/test", json.dumps({"hello": "world"}))
    except Exception as e:
        print("err happen", e)
    finally:
        c.disconnect()


if __name__ == "__main__":
    main("192.168.0.7")
