import requests
import httpx
import asyncio

class CorelynSDK:
    BASE_URL = "https://corelyncloud-backend.onrender.com/chat/completions"

    def __init__(self, api_key: str, default_model: str = "nvidia/moonshotai/kimi-k2.5"):
        """
        Initialize the SDK.
        
        Args:
            api_key (str): Your Corelyn API key.
            default_model (str): Default AI model to use.
        """
        self.api_key = api_key
        self.default_model = default_model

    def get_ai_response(self, prompt: str, model: str = None):
        """
        Synchronous AI call.

        Args:
            prompt (str): The prompt for the AI.
            model (str, optional): Optional model override.

        Returns:
            str: AI response text.
        """
        try:
            payload = {
                "apiKey": self.api_key,
                "model": model or self.default_model,
                "prompt": prompt
            }
            response = requests.post(self.BASE_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content") or data.get("text") or data
        except Exception as e:
            print("Error fetching AI response:", e)
            return None

    async def get_ai_response_async(self, prompt: str, model: str = None):
        """
        Asynchronous AI call.

        Args:
            prompt (str): The prompt for the AI.
            model (str, optional): Optional model override.

        Returns:
            str: AI response text.
        """
        try:
            payload = {
                "apiKey": self.api_key,
                "model": model or self.default_model,
                "prompt": prompt
            }
            async with httpx.AsyncClient() as client:
                response = await client.post(self.BASE_URL, json=payload)
                response.raise_for_status()
                data = response.json()
                return data.get("choices", [{}])[0].get("message", {}).get("content") or data.get("text") or data
        except Exception as e:
            print("Error fetching AI response:", e)
            return None
