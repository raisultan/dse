from aiohttp import web
from aiohttp.web_request import Request


async def post(request: Request):
    data = await request.json()

    try:
        project_name = data['project_name']
        text = data['text']
    except KeyError as exc:
        raise web.HTTPBadRequest(text=repr(exc))

    result = await request.app['ads_collection'].search(project_name, text)
    return web.json_response(result)
