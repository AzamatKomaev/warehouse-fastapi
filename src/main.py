import sys
import pathlib
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI


# Load env variables from .env file.
load_dotenv()

app = FastAPI()

# Append path to current dir to sys.path.
current_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(current_dir))


def add_routers():
    from auth import auth_router
    from products import products_router

    app.include_router(auth_router, prefix='/auth')
    app.include_router(products_router, prefix='/products')


add_routers()

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000, log_level="info", reload=True)
