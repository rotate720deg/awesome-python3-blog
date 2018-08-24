import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
  # 没写content_type之前，变成了下载
  return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html', charset='UTF-8')

@asyncio.coroutine
def init(loop):
  app = web.Application(loop=loop)
  app.router.add_route('GET','/', index)
  srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
  logging.info('server started at http://127.0.0.1:9000...')
  return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

# 以下写法也是可以的，为啥廖雪峰要用上面的写法呢
# def init():
#   app = web.Application()
#   app.add_routes([web.get('/', index)])
#   web.run_app(app)

# init()