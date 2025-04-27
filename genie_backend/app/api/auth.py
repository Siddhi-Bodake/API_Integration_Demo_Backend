from fastapi import APIRouter, Depends, HTTPException
from fastapi import Response

from ..models.user_model import User
from ..services.auth_service import register_user, authenticate_user
from ..core.security import create_access_token

router = APIRouter()

@router.post("/register")
async def register(user: User):
    return await register_user(user)

@router.post("/login")
async def login(user: User):
    auth_user = await authenticate_user(user.email, user.password)
    if not auth_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": auth_user["email"]})
    return {"access_token": token, "token_type": "bearer"}


# Logout route
@router.post("/logout")
async def logout(response: Response):
    # If you're using cookies for JWT token storage, you can delete the cookie like this:
    response.delete_cookie("access_token")
    return {"message": "Successfully logged out"}