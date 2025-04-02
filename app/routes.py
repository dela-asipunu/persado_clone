from fastapi import APIRouter
from auth import signup, login, logout
from models import UserAuth

router = APIRouter()

@router.post("/signup")
async def signup_route(user: UserAuth):
    return signup(email=user.email, password=user.password)

@router.post("/login")
async def login_route(user: UserAuth):
    return login(email=user.email, password=user.password)

@router.post("/logout")
async def logout_route(access_token: str):
    return logout(access_token=access_token)
