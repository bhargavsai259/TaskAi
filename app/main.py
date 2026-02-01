from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.core.config import settings
from app.core.database import engine, get_db, Base

# Create tables (OK for dev, avoid in prod)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)

@app.get("/")
def read_root():
    return {"message": "Welcome to Ai Assistant"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

# API to get users without a model
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT * FROM users"))
        users = [dict(row._mapping) for row in result.fetchall()]
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
