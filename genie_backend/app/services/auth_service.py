from ..core.security import hash_password, verify_password
from ..db.mongo import db
from ..models.user_model import User

async def register_user(user: User):
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    await db.users.insert_one(user_dict)
    return {"msg": "User registered successfully"}

async def authenticate_user(email: str, password: str):
    user = await db.users.find_one({"email": email})
    if user and verify_password(password, user["password"]):
        return user
    return None
