from fastapi import FastAPI

app = FastAPI()


@app.get("/credits")
async def credits():
    return {"Developers": ['Daniel Polo', 'Carlos Rodriguez']}
