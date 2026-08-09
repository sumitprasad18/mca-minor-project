from fastapi import FastAPI
from database import engine
from sqlalchemy import text

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "GRWM AI backend is running"}

@app.get("/test-db")
def test_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return {"db_connection": "success", "result": result.scalar()}