from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import ai_service
from typing import Dict, Any

router = APIRouter()

class OptimizeRequest(BaseModel):
    text: str

class ImportRequest(BaseModel):
    url: str

@router.post("/optimize")
async def optimize_profile(request: OptimizeRequest) -> Dict[str, str]:
    """
    使用 AI 优化个人简介
    """
    try:
        optimized_text = await ai_service.optimize_profile(request.text)
        return {"optimized_text": optimized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/import")
async def import_profile(request: ImportRequest) -> Dict[str, Any]:
    """
    从链接导入个人信息
    """
    try:
        profile_data = await ai_service.analyze_profile(request.url)
        return profile_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
