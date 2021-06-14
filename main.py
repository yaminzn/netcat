from starlette.responses import Response
from lib.models.cat import Cat
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
  cat = Cat()
  svg = cat.get_svg()
  return Response(svg, media_type='image/svg+xml')

