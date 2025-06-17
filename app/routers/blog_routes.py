from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app import models, schemas
from app.database import get_db
from app.auth import get_current_user

router = APIRouter()



@router.post("/", response_model=schemas.BlogOut)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    new_blog = models.Blog(title=blog.title, content=blog.content, user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@router.get("/", response_model=List[schemas.BlogOut])
def get_all_blogs(db: Session = Depends(get_db)):
    return db.query(models.Blog).all()



@router.get("/{id}", response_model=schemas.BlogOut)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog



@router.put("/{id}", response_model=schemas.BlogOut)
def update_blog(id: int, updated_blog: schemas.BlogCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    blog.title = updated_blog.title
    blog.content = updated_blog.content
    db.commit()
    db.refresh(blog)
    return blog



@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    db.delete(blog)
    db.commit()
    return {"message": "Blog deleted successfully"}


