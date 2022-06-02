from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


@app.get("/credits")
async def credits():
    return {
        "Developers": [
            'Daniel Polo',
            'Carlos Rodriguez'
        ],
        'Database': os.environ.get('DATABASE_URL')
    }
