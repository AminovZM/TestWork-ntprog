import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from chat.coters import quotations
import random

app = FastAPI()

with open("chat/chat.html", 'r') as h:
    html = h.read()

html2 = """
<!DOCTYPE html>
<html>
<head>
    <title>BTC</title>
</head>
<body>
    <h1>Bitcoin</h1>
</body>
</html>

"""

@app.get("/")
async def get():
    return HTMLResponse(html)


@app.get("/{name_crypto}")
async def get():
    return HTMLResponse(html2)


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


