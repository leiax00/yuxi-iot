from contextlib import asynccontextmanager

from fastapi import FastAPI

import routes
from app import AppMgr


# 定义 startup 事件处理程序，在应用程序启动时调用
@asynccontextmanager
async def lifespan(main: FastAPI):
    # 启动时执行初始化资源
    AppMgr.init()
    yield
    # 关闭时释放资源
    await AppMgr.release()


app = FastAPI(lifespan=lifespan)
routes.register_to(app)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
