from fastapi import FastAPI
from findes import Logs
from router import router, router1
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
data = Logs()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(router1)



