import asyncio
import threading

import cv2
import time

# 全局变量，用于保存摄像头帧
global_frame = None
# 用于保存录像的输出文件
output_file = 'tmp/output_video.mp4'

def capture_camera():
    global global_frame
    cap = cv2.VideoCapture(0)

    # 设置视频编码和输出文件
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 保存帧到全局变量中，供视频流使用
        global_frame = frame

        # 将帧写入视频文件，保存录像
        out.write(frame)

        # 图像分析处理
        # analyze_frame(frame)

        # 限制帧率为 20 FPS
        time.sleep(0.05)  # 控制每秒 20 帧 (1/20 秒)

# 在后台启动摄像头捕获线程
camera_thread = threading.Thread(target=capture_camera)
camera_thread.daemon = True
camera_thread.start()
print("camera thread started!")


# 生成视频流的异步函数，返回每一帧
async def generate_video_stream():
    global global_frame
    while True:
        if global_frame is not None:
            # 将帧编码为 JPEG 格式
            ret, jpeg = cv2.imencode('.jpg', global_frame)
            if ret:
                # 使用 MJPEG 流传输帧
                frame = jpeg.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        # 控制帧率
        await asyncio.sleep(0.05)  # 每秒大约 20 帧