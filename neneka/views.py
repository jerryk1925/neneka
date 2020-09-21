from aiohttp import web
# from sqlalchemy.schema import CreateTable, DropTable
# from neneka.db import question, choice

async def index(request):
  # print(request.app['db'])
  # async with request.app['db'].acquire() as conn:
  #   async for row in conn.execute(question.select()):
  #     print(row.id, row.name)
  #   # print(conn)
  #   # await conn.execute(DropTable(question))
  #   # await conn.execute(CreateTable(question))
  #   # await conn.execute(question.insert().values(id=2, name='qwe'))

  return web.Response(text="Hello worasdasldfgdgd")