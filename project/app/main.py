from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import getdata


api = FastAPI(
    title='Human-Rights-First-Labs28-ds-b',
    description='',
    version='0.1',
    docs_url='/',
)

api.include_router(getdata.router)


api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(api)
