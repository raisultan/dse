from aiohttp import web
from aiohttp.web_request import Request


async def post(request: Request):
    data = await request.json()

    try:
        project_name = data['project_name']
        ad_id = data['id']
        text = data['text']
    except KeyError as exc:
        raise web.HTTPBadRequest(text=repr(exc))

    await request.app['ads_collection'].insert_entity(ad_id, project_name, text)
    return web.Response()
