
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

app = FastAPI(
    title="DIPWeb",
    description="Digital Image Processing Web Platform",
    version="1.0.0"
)

# 前端跨域配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 项目目录
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# 测试 API
@app.get("/api/hello")
def hello():
    return {
        "message": "Hello, DIPWeb!",
        "status": "success"
    }

# 返回网页
@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")
