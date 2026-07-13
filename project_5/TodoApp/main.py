from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates
from . import models
from .database import engine
from .routers import auth, todos, admin, user
from fastapi.staticfiles import StaticFiles
from pathlib import Path


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


@app.get("/.well-known/appspecific/com.chrome.devtools.json", include_in_schema=False)
def chrome_devtools_config():
    return Response(status_code=204)


@app.get("/")
def test(request: Request):
    # old style of TemplateResponse creation
    # return templates.TemplateResponse("home.html", {"request": request})
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