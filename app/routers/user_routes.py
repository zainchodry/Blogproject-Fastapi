from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import schemas, models, hashing, jwt_handler
from app.database import get_db

router = APIRouter()



@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hashing.hash_password(user.password)
    new_user = models.User(username=user.username, email=user.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not hashing.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid Credentials")
    access_token = jwt_handler.create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}



