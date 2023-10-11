from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler
import ar as morse

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })


@app.get("/api")
async def api(request: Request):
    return {'1': 1}


@app.get("/translate/{lang}/{input_text}")
async def translate(lang: str, input_text: str):
    lang_list = morse.ru if lang == 'ru' else morse.eu
    res = ''
    for i in input_text.upper():
        if i in lang_list:
            res += lang_list[i]
            res += ' '
        elif i == ' ':
            res += '  '
    return {'result': res}


@app.exception_handler(StarletteHTTPException)
async def my_custom_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse('404.html', {'request': request})
    else:
        # Just use FastAPI's built-in handler for other errors
        return await http_exception_handler(request, exc)


