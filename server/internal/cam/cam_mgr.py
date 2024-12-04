import asyncio
import os.path
from asyncio import Queue, QueueFull
from datetime import datetime

import cv2


class CamMgr:
    def __init__(self, out_dir='tmp', cam_index=0, max_queue_size=10):
        """
        初始化摄像头管理对象
        :param cam_index: 摄像头编号, 默认第0个
        :param max_queue_size: 帧最大缓存数, 默认10
        """
        self.cam_index = cam_index
        self.fps = 20
        # 摄像头帧尺寸 & 视频输出帧尺寸, 注意两者独立, 仅程序设置成一致
        self.size = (640, 480)
        self.cap = None
        self.out_dir = out_dir
        self.frame_queue = Queue(max_queue_size)
        self.stream_frame = None  # 视频流帧存储, 暂时保存一帧; 如果丢帧严重, 再跳转

    def open_camera(self):
        self.cap = cv2.VideoCapture(self.cam_index)
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size[1])

    async def release(self):
        if self.cap is not None:
            self.cap.release()
        await self.frame_queue.put(None)

    # 摄像头捕获协程
    async def capture_camera(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            try:
                self.stream_frame = frame
                self.frame_queue.put_nowait(frame)
            except QueueFull:
                print("Queue Full, dropping frame!")

            # 控制帧率（可以根据需要调整）, 当不支持cv2帧率设置时, 通过休眠方式来设置
            await asyncio.sleep(1 / self.fps)

    # 生成视频流
    async def generate_video_stream(self):
        while True:
            # 将帧编码为 JPEG 格式
            ret, jpeg = cv2.imencode('.jpg', self.stream_frame)
            if ret:
                frame = jpeg.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            await asyncio.sleep(0.05)  # 控制帧率

    async def write_video(self):
        if not os.path.exists(self.out_dir):
            os.makedirs(self.out_dir)

        out = cv2.VideoWriter(
            os.path.join(self.out_dir, f'cam_{datetime.now().strftime("%Y%m%d%H%M%S")}.mp4'),
            cv2.VideoWriter.fourcc(*'MJPG'),
            self.fps,
            self.size
        )
        while True:
            if self.frame_queue:
                # 从队列中获取最新的帧
                frame = await self.frame_queue.get()
                if frame is None:
                    break
                out.write(frame)

        out.release()

    def start(self):
        self.open_camera()
        asyncio.create_task(self.capture_camera())
        asyncio.create_task(self.write_video())


# 实例化摄像头管理类
mgr = CamMgr()
