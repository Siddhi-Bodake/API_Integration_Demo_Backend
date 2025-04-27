from fastapi import APIRouter
from pydantic import BaseModel
from ..services.gemini_service import ask_gemini

router = APIRouter()

class Prompt(BaseModel):
    message: str

@router.post("/chat")
async def chat_with_bot(prompt: Prompt):
    return await ask_gemini(prompt.message)