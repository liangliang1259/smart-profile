import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_service import ai_service
from typing import Dict, Any

# 配置日志
logger = logging.getLogger(__name__)

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
    logger.info("Received optimize profile request with text length: %d", len(request.text))
    try:
        optimized_text = await ai_service.optimize_profile(request.text)
        logger.info("Successfully optimized profile")
        return {"optimized_text": optimized_text}
    except Exception as e:
        logger.error("Error in optimize_profile endpoint: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/import")
async def import_profile(request: ImportRequest) -> Dict[str, Any]:
    """
    从链接导入个人信息
    """
    logger.info("Received import profile request for URL: %s", request.url)
    try:
        profile_data = await ai_service.analyze_profile(request.url)
        logger.info("Successfully imported profile data")
        return profile_data
    except Exception as e:
        logger.error("Error in import_profile endpoint: %s", str(e), exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
