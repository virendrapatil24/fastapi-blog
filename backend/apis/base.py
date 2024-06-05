from apis.v1 import route_blog, route_user
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(route_user.router, prefix="/v1/user", tags=["user"])
api_router.include_router(route_blog.router, prefix="/v1/blog", tags=["blog"])
