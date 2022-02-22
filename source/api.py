from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import uvicorn
import os
from utilities import UseConfig, GetMeTheSoup

api_url = "/api/v1/"
port = 8000
host = '127.0.0.1'

app = FastAPI(
    title='Web Scraper of Doom',
    openapi_url=api_url
)

@app.get("/")
async def serve_static():
    return FileResponse('static/index.html', media_type='text/html')


@app.get("/script.js")
async def load_js():
    return FileResponse('static/script.js')


@app.post(f"{api_url}scrape")
async def get_config(request: Request):
    config = await request.json()
    soup = GetMeTheSoup(config["url"])
    response = {}
    UseConfig(soup, config, response)
    return response  # seems to return better without json.dumps


if __name__ == '__main__':
    uvicorn.run("api:app", reload=True, port=port, host=host)