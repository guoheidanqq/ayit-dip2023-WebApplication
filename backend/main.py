
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from backend.routers.image_router import router as image_router

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

# 挂载用户上传图片
UPLOAD_DIR = BASE_DIR / "uploads"

app.mount(
    "/uploads",
    StaticFiles(directory=str(UPLOAD_DIR)),
    name="uploads"
)

# 注册图像路由
app.include_router(image_router)

# 测试 API
@app.get("/api/hello")
def hello():
    return {
        "message": "Hello, DIPWeb!",
        "status": "success"
    }

# 测试 API
@app.get("/api/gray")
def gray():
    grayFileResponse = FileResponse(FRONTEND_DIR / "gray.html")
    return grayFileResponse

# 返回网页
@app.get("/")
def index():
    return FileResponse(FRONTEND_DIR / "index.html")
