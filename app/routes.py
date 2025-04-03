from fastapi import APIRouter, HTTPException
from auth import signup, login, logout
from models import UserAuth,UserPrompt
from ai import generate_response

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






@router.post("/predict")
def ai_predict(request: UserPrompt):
    try:
        response = generate_response(request.input_text)
        return {"response": response}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
