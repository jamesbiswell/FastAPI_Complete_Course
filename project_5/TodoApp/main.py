from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from . import models
from .database import engine
from .routers import auth, todos, admin, user
from fastapi.staticfiles import StaticFiles


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="project_5/TodoApp/templates")

app.mount("/static", StaticFiles(directory="project_5/TodoApp/static"), name="static")


@app.get("/")
def test(request: Request):
    # old style of TemplateResponse creation
    # return templates.TemplateResponse("home.html",
    #                                   {"request": request})
    return templates.TemplateResponse(
        request=request,
        name="home.html",
    )


@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(user.router)