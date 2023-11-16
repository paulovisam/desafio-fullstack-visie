import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from docs.description import description
from docs.tags_metadata import tags_metadata
from src.people.resource import people_resource
import logging

logging.config.fileConfig('log/log_config_time.ini', disable_existing_loggers=False)
log = logging.getLogger('uvicorn')

app = FastAPI(
    openapi_tags=tags_metadata,
    title='Visie API',
    description=description,
    version='0.1.0',
    contact={
        'name': 'Desafio Visie',
    },
)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Routers
prefix = '/api/v1'
app.include_router(people_resource.router, prefix=prefix)


@app.get('/', tags=['Root'])
async def root():
    """The `return` statement in the `root()` function is returning a dictionary containing information
    about the API."""
    log.info("logging from the root logger")
    return {
        'version': '1.0.0',
        'documentation_api': 'http://localhost:8000/docs',
        'documentation_interactive': 'http://localhost:8000/redoc',
        'status': 'online',
    }


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port=8000,
        host='0.0.0.0',
        reload=True,
        proxy_headers=True,
        forwarded_allow_ips='*',
        log_config='log/log_config_time.ini',
    )
