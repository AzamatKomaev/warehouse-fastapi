import sys
import pathlib
from fastapi import FastAPI


app = FastAPI()

current_dir = str(pathlib.Path(__file__).parent.resolve())
sys.path.append(current_dir)


def add_routers():
    from auth.router import router as auth_router
    app.include_router(auth_router, prefix='/auth')


add_routers()
