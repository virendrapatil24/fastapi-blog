from typing import List

from db.repository.blog import (
    create_new_blog,
    delete_blog_by_id,
    retrieve_all_blogs,
    retrieve_blog,
    update_blog_by_id,
)
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    blog = create_new_blog(blog=blog, db=db, author_id=1)
    return blog


@router.get("/{id}", response_model=ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found",
        )
    return blog


@router.get("/{slug}", response_model=ShowBlog)
def get_blog_by_slug(slug: str, db: Session = Depends(get_db)):
    blog = retrieve_blog(slug=slug, db=db)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {slug} not found",
        )
    return blog


@router.get("", response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = retrieve_all_blogs(db=db)
    return blogs


@router.put("/{id}", response_model=ShowBlog)
def update_blog(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
    blog = update_blog_by_id(id=id, db=db, blog=blog)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with id {id} not found",
        )
    return blog


@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    message = delete_blog_by_id(id=id, db=db)
    if message.get("error"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=message.get("error")
        )
    return {"msg": "Blog deleted successfully"}
