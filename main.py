from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def credits():
    return {"Developers": ['Daniel Polo', 'Carlos Rodriguez']}
