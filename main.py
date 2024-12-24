from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from starlette.websockets import WebSocket

# from core.models import Base, db_helper
from core.config import settings
from api_v1 import router as router_v1
from items_views import router as items_router
from users.views import router as users_router
import logging


logger = logging.Logger(__name__)
# чтобы создать новую базу данных
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with db_helper.engine.begin() as conn:
#         # движок создает все таблицы
#         await conn.run_sync(Base.metadata.create_all)
#
#     yield


app = FastAPI()
app.include_router(items_router)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)
app.include_router(users_router)

USERS: dict[str, WebSocket] = {}


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    name = await websocket.receive_text()
    USERS[name] = websocket
    while True:
        data = await websocket.receive_text()
        if USERS["vasya"] == websocket:
            await USERS["kolya"].send_text(data)
        else:
            await USERS["vasya"].send_text(data)
        # logger.error(data)
        # await websocket.send_text(data)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)
