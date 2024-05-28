import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from chat.coters import quotations
import random

from chat.router import router as router_application

app = FastAPI()

with open("templates/chat.html", 'r', encoding='utf-8') as h:
    html = h.read()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_json(quotations)
            await asyncio.sleep(random.randint(1, 10))
            for i in range(random.randint(0, 10), 10):
                quotations[i]["price"] += random.randint(-5, 5)
    except WebSocketDisconnect:
        pass

app.include_router(router_application)
