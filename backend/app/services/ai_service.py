import httpx
import logging
from app.core.config import settings
from typing import Dict, Any

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIService:
    def __init__(self):
        self.api_key = "sk-h8Gv3GmkEEXblUcJn3qowM6TtgNGDKnmYq4R0ki2qGSMGmP6"
        self.api_base = "https://api.moonshot.cn/v1"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        logger.info("AIService initialized with API base: %s", self.api_base)
    
    async def optimize_profile(self, text: str) -> str:
        """
        使用 Kimi API 优化个人简介
        """
        logger.info("Starting profile optimization for text length: %d", len(text))
        
        messages = [
            {
                "role": "system",
                "content": "你是一个专业的个人简介优化助手。你需要帮助用户优化他们的个人简介，使其更专业、更有吸引力，同时保持原有的核心信息。优化时注意：1. 使用更专业的措辞 2. 突出关键成就和技能 3. 保持简洁明了 4. 确保语言流畅自然"
            },
            {
                "role": "user",
                "content": f"请帮我优化以下个人简介，使其更专业、更有吸引力：\n\n{text}"
            }
        ]
        
        try:
            logger.info("Preparing to send request to Kimi API")
            request_data = {
                "model": "moonshot-v1-8k",
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 800
            }
            logger.info("Request data: %s", request_data)
            
            async with httpx.AsyncClient() as client:
                logger.info("Sending request to Kimi API")
                response = await client.post(
                    f"{self.api_base}/chat/completions",
                    headers=self.headers,
                    json=request_data,
                    timeout=30.0
                )
                
                logger.info("Received response from Kimi API with status code: %d", response.status_code)
                response.raise_for_status()
                result = response.json()
                logger.info("Raw API response: %s", result)
                
                if "choices" in result and len(result["choices"]) > 0:
                    optimized_text = result["choices"][0]["message"]["content"]
                    logger.info("Successfully optimized profile text")
                    return optimized_text
                else:
                    logger.error("No valid choices in API response")
                    raise ValueError("No valid response from AI service")
                    
        except httpx.TimeoutException as e:
            logger.error("Timeout error calling Kimi API: %s", str(e))
            raise Exception(f"Request to Kimi API timed out: {str(e)}")
        except httpx.HTTPStatusError as e:
            logger.error("HTTP error from Kimi API: %s", str(e))
            raise Exception(f"HTTP error from Kimi API: {str(e)}")
        except Exception as e:
            logger.error("Unexpected error calling Kimi API: %s", str(e), exc_info=True)
            raise Exception(f"Error calling Kimi API: {str(e)}")
    
    async def analyze_profile(self, url: str) -> Dict[str, Any]:
        """
        从链接中分析并提取个人信息
        """
        logger.info("Starting profile analysis for URL: %s", url)
        
        messages = [
            {
                "role": "system",
                "content": "你是一个专业的个人信息分析助手。你需要从提供的链接中提取和分析个人信息，并以结构化的方式返回。"
            },
            {
                "role": "user",
                "content": f"请分析这个链接中的个人信息：{url}"
            }
        ]
        
        try:
            logger.info("Preparing to send request to Kimi API for URL analysis")
            request_data = {
                "model": "moonshot-v1-8k",
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 800
            }
            logger.info("Request data: %s", request_data)
            
            async with httpx.AsyncClient() as client:
                logger.info("Sending request to Kimi API")
                response = await client.post(
                    f"{self.api_base}/chat/completions",
                    headers=self.headers,
                    json=request_data,
                    timeout=30.0
                )
                
                logger.info("Received response from Kimi API with status code: %d", response.status_code)
                response.raise_for_status()
                result = response.json()
                logger.info("Raw API response: %s", result)
                
                if "choices" in result and len(result["choices"]) > 0:
                    profile_data = result["choices"][0]["message"]["content"]
                    logger.info("Successfully analyzed profile URL")
                    return {"profile_data": profile_data}
                else:
                    logger.error("No valid choices in API response")
                    raise ValueError("No valid response from AI service")
                    
        except httpx.TimeoutException as e:
            logger.error("Timeout error calling Kimi API: %s", str(e))
            raise Exception(f"Request to Kimi API timed out: {str(e)}")
        except httpx.HTTPStatusError as e:
            logger.error("HTTP error from Kimi API: %s", str(e))
            raise Exception(f"HTTP error from Kimi API: {str(e)}")
        except Exception as e:
            logger.error("Unexpected error calling Kimi API: %s", str(e), exc_info=True)
            raise Exception(f"Error calling Kimi API: {str(e)}")

ai_service = AIService()
