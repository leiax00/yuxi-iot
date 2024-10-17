from fastapi import APIRouter

router = APIRouter(prefix='/cam', tags=['cam'])


async def index():
