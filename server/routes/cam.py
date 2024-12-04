from fastapi import APIRouter
from starlette.responses import StreamingResponse

from server.common.entity.schema.resp import R1
from server.internal.cam.cam_mgr import mgr

router = APIRouter(prefix='/cam', tags=['cam'])


@router.get('/index')
async def index():
    return R1.ins().data("Hello, CAM!")


@router.get('/stream')
async def video_feed():
    return StreamingResponse(mgr.generate_video_stream(),
                             media_type='multipart/x-mixed-replace; boundary=frame')
