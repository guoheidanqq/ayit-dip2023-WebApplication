from fastapi import APIRouter, UploadFile, File, HTTPException
from pathlib import Path
import uuid

router = APIRouter(
    prefix="/api/image",
    tags=["Image"]
)

# 项目根目录
BASE_DIR = Path(__file__).resolve().parents[2]

# 用户上传目录
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):

    # 1. 检查文件格式
    suffix = Path(file.filename or "").suffix.lower()

    allowed_extensions = {
        ".jpg", ".jpeg", ".png", ".bmp", ".webp"
    }

    if suffix not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image format"
        )

    # 2. 生成唯一文件名
    filename = f"{uuid.uuid4().hex}{suffix}"

    # 3. 构造保存路径
    save_path = UPLOAD_DIR / filename

    # 4. 读取并保存文件
    content = await file.read()

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Empty file"
        )

    with open(save_path, "wb") as f:
        f.write(content)

    # 5. 返回结果
    return {
        "message": "Upload successful",
        "source": "upload",
        "filename": filename,
        "url": f"/uploads/{filename}"
    }