from fastapi import APIRouter, Query, HTTPException
import httpx
from ..core.config import settings

router = APIRouter()

@router.get("/search")
async def search_items(q: str = Query(...)):
    headers = {
        "Authorization": f"Bearer {settings.EXA_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "query": q,
        "numResults": 5
    }

    timeout = httpx.Timeout(20.0)  # 20 seconds timeout

    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            response = await client.post("https://api.exa.ai/search", headers=headers, json=body)
            response.raise_for_status()
            return response.json()
        except httpx.ReadTimeout:
            raise HTTPException(status_code=504, detail="Request to Exa API timed out. Please try again.")
        except httpx.RequestError as exc:
            raise HTTPException(status_code=502, detail=f"Search failed due to network issue: {exc}")
