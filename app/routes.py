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


from flask import Blueprint, request, jsonify
from app.ai import generate_response

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/predict", methods=["POST"])
def ai_predict():
    try:
        data = request.json["prompt"]  # Expecting {"prompt": "your text here"}
        response = generate_response(data)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
