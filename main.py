import uvicorn
from dotenv import load_dotenv
import os
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent
    
    # 環境変数を .env から読み込む。
    dotenv_path = os.path.join(BASE_DIR, '.env')
    load_dotenv(dotenv_path)
    HOST = os.environ.get("HOST")
    PORT = int(os.environ.get("PORT"))
    uvicorn.run("api.main:app", host=HOST, port=PORT, reload=True)
