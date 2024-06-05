from db.repository.blog import create_new_blog, retrieve_blog
from db.session import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.blog import CreateBlog, ShowBlog
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
