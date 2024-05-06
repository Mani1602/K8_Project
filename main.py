from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="/code")
#templates = Jinja2Templates(directory="/home/mani/Desktop/python")

@app.get("/")
def from_post(request: Request):
    return templates.TemplateResponse('form.html', context={'request': request})
