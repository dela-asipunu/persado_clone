from pydantic import BaseModel, EmailStr
from typing import Optional


class UserAuth(BaseModel):
    email: EmailStr
    password: str

#the AI text response
class GeneratedResponse(BaseModel):
    message_text: str


#user prompt for AI
class UserPrompt(BaseModel):
    user_id: str
    input_text: str

