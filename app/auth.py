from database import supabase
from fastapi import HTTPException

def signup(email: str, password: str):
    try:
        response = supabase.auth.sign_up(email=email, password=password)
        if response.get("error"):
            raise HTTPException(status_code=400, detail=response["error"]["message"])
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def login(email: str, password: str):
    try:
        response = supabase.auth.sign_in(email=email, password=password)
        if response.get("error"):
            raise HTTPException(status_code=400, detail=response["error"]["message"])
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def logout():
    try:
        response = supabase.auth.sign_out()
        if response.get("error"):
            raise HTTPException(status_code=400, detail=response["error"]["message"])
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    