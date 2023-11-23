from fastapi import APIRouter, HTTPException, Cookie, Response
from fastapi.responses import JSONResponse
import api.schemas.auth as auth_schemas
from dotenv import load_dotenv
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 環境変数を .env から読み込む。
dotenv_path = os.path.join(BASE_DIR, '.env')
load_dotenv(dotenv_path)
PASS = os.environ.get("PASS")

router = APIRouter()

@router.post("/signin", response_model=None)
def create_cookie(signin: auth_schemas.AuthBase):
    print("signin1")
    if signin.password == PASS:
        response = JSONResponse(status_code=200, content={"message": "Cookie is set"})
        response.set_cookie(key="cookie", value="fake-cookie-session-value", samesite="None", secure=True, max_age=3600)
        return response
    else:
        raise HTTPException(status_code=401, detail="Password is incorrect")


@router.post("/confirm", response_model=None)
def confirm_cookie(cookie:str |None = Cookie(default=None)):
    
    if cookie == "fake-cookie-session-value":
        print("ok")
        response = JSONResponse(status_code=200, content={"message": "Cookie is confirmed"})
        return response
    else:
        print("no")
        raise HTTPException(status_code=401, detail="Password is incorrect")
    
@router.post("/signout")
def delete_cookie(cookie:str |None = Cookie(default=None)):

    if cookie:
        response = JSONResponse(status_code=200, content={"message": "Cookie deleted"})
        response.set_cookie(key="cookie", value="", samesite="None", secure=True, max_age=0)
        return response
    else:
        raise HTTPException(status_code=400, detail="Cookie not found")
