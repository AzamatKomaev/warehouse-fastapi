import sys
import pathlib
from fastapi import FastAPI


app = FastAPI()

current_dir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(current_dir)


def add_routers():
    from auth import auth_router
    from products import products_router

    app.include_router(auth_router, prefix='/auth')
    app.include_router(products_router, prefix='/products')


add_routers()
