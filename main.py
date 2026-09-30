from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
import os

load_dotenv()

from.routes import router

app = FastAPI(title="ComicCraft - AI Comic Creator")

# Mount static
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Include routes
app.include_router(router)

@app.get("/health")
def health():
    return {"status": "ok", "message": "ComicCraft running!"}

