from fastapi import APIRouter
from starlette.responses import StreamingResponse

from common.entity.schema.resp import R1
from internal.cam.capture import generate_video_stream

router = APIRouter(prefix='/cam', tags=['cam'])


@router.get('/index')
async def index():
    return R1.ins().data("Hello, CAM!")


@router.get('/video')
async def video_feed():
    return StreamingResponse(generate_video_stream(),
                             media_type='multipart/x-mixed-replace; boundary=frame')
