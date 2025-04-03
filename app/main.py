from fastapi import FastAPI
from routes import router
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "I am the Billionaire"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)