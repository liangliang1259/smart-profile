import httpx
from app.core.config import settings
from typing import Dict, Any

class AIService:
    def __init__(self):
        self.api_key = settings.KIMI_API_KEY
        self.api_base = settings.KIMI_API_BASE
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    async def optimize_profile(self, text: str) -> str:
        """
        使用 Kimi API 优化个人简介
        """
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
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_base}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": "moonshot-v1-8k",
                        "messages": messages,
                        "temperature": 0.7,
                        "max_tokens": 800
                    },
                    timeout=30.0
                )
                
                response.raise_for_status()
                result = response.json()
                
                if "choices" in result and len(result["choices"]) > 0:
                    return result["choices"][0]["message"]["content"]
                else:
                    raise ValueError("No valid response from AI service")
                    
        except Exception as e:
            print(f"Error calling Kimi API: {str(e)}")
            raise
    
    async def analyze_profile(self, url: str) -> Dict[str, Any]:
        """
        分析个人主页链接并提取关键信息
        """
        messages = [
            {
                "role": "system",
                "content": "你是一个专业的个人信息分析助手。你需要分析用户提供的个人主页链接，并提取关键信息。请以JSON格式返回以下字段：name（姓名）, title（职位）, company（公司）, bio（简介）, skills（技能列表）"
            },
            {
                "role": "user",
                "content": f"请分析这个个人主页链接并提取关键信息：{url}"
            }
        ]
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_base}/chat/completions",
                    headers=self.headers,
                    json={
                        "model": "moonshot-v1-8k",
                        "messages": messages,
                        "temperature": 0.3,
                        "max_tokens": 1000
                    },
                    timeout=30.0
                )
                
                response.raise_for_status()
                result = response.json()
                
                if "choices" in result and len(result["choices"]) > 0:
                    # 解析AI返回的JSON字符串
                    import json
                    content = result["choices"][0]["message"]["content"]
                    try:
                        return json.loads(content)
                    except:
                        # 如果JSON解析失败，返回空值
                        return {
                            "name": "",
                            "title": "",
                            "company": "",
                            "bio": "",
                            "skills": []
                        }
                else:
                    raise ValueError("No valid response from AI service")
                    
        except Exception as e:
            print(f"Error calling Kimi API: {str(e)}")
            raise

ai_service = AIService()
