from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routers import auth
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 環境変数を .env から読み込む。
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)
origin = os.environ.get("ALLOW_ORIGIN")
origin = origin.split(",")

app = FastAPI()
app.include_router(auth.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
