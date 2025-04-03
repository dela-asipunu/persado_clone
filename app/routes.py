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
async def logout_route():
    return logout()

@router.post("/generate")
async def generate_route(prompt: UserPrompt):
    response = generate_response(prompt.input_text)
    if not response:
        raise HTTPException(status_code=400, detail="Failed to generate response")
    return {"response": response}






@router.post("/predict")
def ai_predict(request: UserPrompt):
    try:
        response = generate_response(request.input_text)
        return {"response": response}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
