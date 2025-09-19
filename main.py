from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

# 실행
# uvicorn main:app --reload
# uvicorn main:app --reload --port 8081
