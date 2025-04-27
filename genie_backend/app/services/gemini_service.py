import httpx
from ..core.config import settings

async def ask_gemini(prompt: str):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"

    payload = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload)

    print("RESPONSE:", response.status_code, response.text)
    return response.json()
