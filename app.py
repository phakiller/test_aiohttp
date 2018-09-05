from aiohttp import web
import json

from resources.person_resource import person_route

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = "Hello, " + name
    return web.Response(text=text)

async def myTeste(request):
    response_obj = {'status': 'success'}
    return web.Response(text=json.dumps(response_obj))

async def new_user(request):
    try:
        user = request.query['name']
        print('Creating new user with name: ', user)
        response_obj = {'status': 'success'}
        return web.Response(text=json.dumps(response_obj), status=200)
    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)

app = web.Application()
app.add_routes(person_route)

web.run_app(app)