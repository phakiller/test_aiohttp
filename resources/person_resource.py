import json

from aiohttp import web
from models.person import Person

person_route = web.RouteTableDef()

@person_route.view('/person')
class viewTest(web.View):
    async def get(self):
        response_obj = {'http_verb': 'get'}
        return web.Response(text=json.dumps(response_obj), status=200)
    
    async def post(self):
        response_obj = {'http_verb': 'post'}
        return web.Response(text=json.dumps(response_obj), status=201)