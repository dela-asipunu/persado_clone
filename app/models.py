from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import datetime

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

# user model for signup and login
class UserAuth(BaseModel):
    email: EmailStr
    password: str


#user prompt for AI
class UserPrompt(BaseModel):
    user_id: str
    input_text: str

# the response from the AI
class GeneratedContent(BaseModel):
    campaign_id: int
    generated_text: str
    tone: str
    

class Campaigns(BaseModel):
    user_id: str
    campaign_name: str
    campaign_description: str
    audience_id: int    
    start_date: datetime
    end_date: datetime

class Audiences(BaseModel):
    campaign_id: int
    audience_name: str
    id: int
    audience_type: str
    target_conditions: Dict[str, Any]
    created_at: datetime
    updated_at: datetime


