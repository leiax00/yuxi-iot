from contextlib import asynccontextmanager

from fastapi import FastAPI

from app import AppMgr
from routes import cam


# 定义 startup 事件处理程序，在应用程序启动时调用
@asynccontextmanager
async def lifespan(main: FastAPI):
    # 启动时执行初始化资源
    AppMgr.init()
    yield
    # 关闭时释放资源
    AppMgr.release()

app = FastAPI(lifespan=lifespan)

app.include_router(cam.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)