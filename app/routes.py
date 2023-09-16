import aiohttp_cors
from aiohttp import web
from aiohttp.web_request import Request

from app.api.ads.insert import handler as ads


async def handle_hello(_: Request): return web.Response(text='Hello World! 🚀')


async def setup_routes(app: web.Application) -> None:
    cors = aiohttp_cors.setup(app, defaults={
        '*': aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers='*',
            allow_headers='*',
        ),
    })

    cors.add(app.router.add_get('/hello', handle_hello))
    cors.add(app.router.add_post('/api/ads/insert', ads.post))
