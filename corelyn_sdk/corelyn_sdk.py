import requests
import httpx


class CorelynSDK:
    BASE_URL = "https://corelyncloud-backend.onrender.com/chat/completions"

    def __init__(
        self,
        api_key: str,
        default_model: str = "cerebras/llama3.1-8b",
        system_prompt: str = "Your name is Corelyn"
    ):
        """
        Initialize the SDK.
        """
        self.api_key = api_key
        self.default_model = default_model
        self.system_prompt = system_prompt

    def set_model(self, model: str):
        """
        Change the default model globally.
        """
        self.default_model = model

    def get_ai_response(
        self,
        user_prompt: str = None,
        system_prompt: str = None,
        messages: list = None,
        model: str = None
    ):
        """
        Synchronous AI call.
        """

        try:

            if messages is None:
                messages = [
                    {
                        "role": "system",
                        "content": system_prompt or self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]

            payload = {
                "apiKey": self.api_key,
                "model": model or self.default_model,
                "messages": messages
            }

            response = requests.post(self.BASE_URL, json=payload)
            response.raise_for_status()

            data = response.json()

            return (
                data.get("choices", [{}])[0]
                .get("message", {})
                .get("content")
                or data.get("text")
                or data
            )

        except Exception as e:
            print("Error fetching AI response:", e)
            return None

    async def get_ai_response_async(
        self,
        user_prompt: str = None,
        system_prompt: str = None,
        messages: list = None,
        model: str = None
    ):
        """
        Async AI call.
        """

        try:

            if messages is None:
                messages = [
                    {
                        "role": "system",
                        "content": system_prompt or self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]

            payload = {
                "apiKey": self.api_key,
                "model": model or self.default_model,
                "messages": messages
            }

            async with httpx.AsyncClient() as client:
                response = await client.post(self.BASE_URL, json=payload)
                response.raise_for_status()

                data = response.json()

                return (
                    data.get("choices", [{}])[0]
                    .get("message", {})
                    .get("content")
                    or data.get("text")
                    or data
                )

        except Exception as e:
            print("Error fetching AI response:", e)
            return None
