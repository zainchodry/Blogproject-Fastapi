from fastapi import FastAPI
from app.database import SessionLocal
from app.routers import user_routes, blog_routes


app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(blog_routes.router, prefix="/blogs", tags=["Blogs"])
