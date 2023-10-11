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


@app.get("/translate/{method}/{lang}/{input_text}")
async def translate(method: str, lang: str, input_text: str):
    print(input_text)
    lang_list = morse.ru if lang == 'ru' else morse.eu
    res = ''
    input_text = input_text[1:]
    # Text -> Morse
    if method == 'tm':
        for i in input_text.upper():
            if i in lang_list:
                res += lang_list[i]
                res += ' '
            elif i == ' ':
                res += ' '
        return {'result': res}
    # Morse -> Text
    elif method == 'mt':
        split_morse = input_text.split(' ')
        reverse_list = dict(zip(lang_list.values(), lang_list.keys()))
        for i in split_morse:
            if i.upper() in reverse_list:
                res += reverse_list[i.upper()]
            elif i == '':
                res += ' '
        return {'result': res}


@app.exception_handler(StarletteHTTPException)
async def my_custom_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return templates.TemplateResponse('404.html', {'request': request})
    else:
        return await http_exception_handler(request, exc)


