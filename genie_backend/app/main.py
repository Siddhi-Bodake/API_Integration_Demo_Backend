from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, search, chatbot

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allow your React frontend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods like GET, POST, PUT
    allow_headers=["*"],  # Allow all headers
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(search.router, tags=["Search"])
app.include_router(chatbot.router, prefix="/chat", tags=["Chatbot"])

@app.get("/")
async def root():
    return {"message": "Genie Backend is up and running!"}