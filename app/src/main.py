from fastapi import FastAPI, Request
from app.src.controllers import router
from app.src.services.handler_error_service import handler_errors
from app.src.utils.settings import Settings
from app.src.utils.connection import db_engine
from app.src import models
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=db_engine)

settings = Settings()

app = FastAPI(root_path=settings.APP_PATH)

# Cors
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

route_exclude_middleware = [
    f'{settings.APP_PATH}/docs',
    f'{settings.APP_PATH}/openapi.json',
    f'{settings.APP_PATH}/health-check'
]

# Include routes
app.include_router(router)


@app.middleware("http")
async def oauth2_authorization(request: Request, call_next):
    try:

        path = request.url.path

        if path in route_exclude_middleware:
            response = await call_next(request)
            return response

        if path == "/":
            request.scope["path"] = "/docs"

        response = await call_next(request)

        return response
    except Exception as ex:
        return handler_errors(ex, "Middleware Error")
