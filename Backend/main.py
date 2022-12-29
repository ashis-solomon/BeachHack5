from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine

import models
from routers import auth, todos
from companyapis import companyapis


app = FastAPI()
app.include_router(auth.router)

origins = [
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)
