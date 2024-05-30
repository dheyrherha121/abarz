from fastapi import FastAPI, status, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from .CRUD import products, users
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(products.router)
app.include_router(users.router)
@app.get('')
def index():
    return 'welcome'
