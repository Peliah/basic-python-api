from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from functools import lru_cache

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@lru_cache(maxsize=1)
def get_cached_info():
    return {
        "email": "pelepoupa@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Peliah/basic-python-api"
    }

@app.get("/")
def get_info():
    data = get_cached_info()
    return data