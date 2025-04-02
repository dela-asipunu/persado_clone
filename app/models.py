from pydantic import BaseModel, EmailStr
from typing import Optional

'''
This file contains the Pydantic models for the application.
They're models used to validate and serialize the data that is sent to and from the API.
The database models were created directly using supabase's sql editor.
but i basically created
Campaigns table
Audiences table
Messages table
Subcriptions table
'''

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


