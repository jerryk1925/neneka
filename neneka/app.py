import aiopg.sa

from sqlalchemy import create_engine, MetaData
from aiohttp import web
from sqlalchemy.schema import CreateTable, DropTable

from neneka.routes import init_routes
from neneka.utils import get_config
from neneka.db import question, choice


def init_config(app: web.Application, argv=None) -> None:
  app['config'] = get_config(argv)


async def init_database(app: web.Application) -> None:
    print('----------')
    config = app['config']['postgres']
    print(config)
    engine = await aiopg.sa.create_engine(**config)

    app['db'] = engine

async def close_database(app: web.Application) -> None:
    app['db'].close()
    await app['db'].wait_closed()


def init_app(argv=None) -> web.Application:
    app = web.Application()
    init_config(app, argv)
    init_routes(app)
    app.on_startup.append(init_database)
    app.on_cleanup.append(close_database)
    return app


app = init_app()
