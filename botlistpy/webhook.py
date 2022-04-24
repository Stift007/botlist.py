import sys
import typing
import asyncio
from . import _http
import uvicorn

class Webhook:
    def __init__(self,url_prefix="/blme",coroutine:typing.Union[typing.Awaitable,typing.Coroutine]=None):
        self.url_prefix = url_prefix
        _http.coroutine = coroutine
        _http.url_prefix = url_prefix

    def run(self, port=8123, *, _runner = asyncio.run):
        print(f"Loading ASGI 0.0.0.0/{_http.url_prefix}")
        _runner(self.start_ws(port))

    async def start_ws(self,port):
        asgi = uvicorn.Server(uvicorn.Config(_http.router, host="0.0.0.0",port=port))
        await asgi.serve()
        sys.exit(0)
