from db.base import Blog
from schemas.blog import CreateBlog
from sqlalchemy.orm import Session


def create_new_blog(blog: CreateBlog, db: Session, author_id: int = 1) -> Blog:
    new_blog = Blog(
        title=blog.title,
        slug=blog.slug,
        content=blog.content,
        author_id=author_id,
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def retrieve_blog(id: int, db: Session) -> Blog:
    return db.query(Blog).filter(Blog.id == id).first()


def retrieve_all_blogs(db: Session) -> Blog:
    return db.query(Blog).all()
