from db.base import Blog
from schemas.blog import CreateBlog, UpdateBlog
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
    return db.query(Blog).filter(Blog.is_active == True).all()


def update_blog_by_id(id: int, blog: UpdateBlog, db: Session) -> Blog:
    blog_to_update = db.query(Blog).filter(Blog.id == id).first()
    if not blog_to_update:
        return
    blog_to_update.title = blog.title
    blog_to_update.content = blog.content
    db.add(blog_to_update)
    db.commit()
    db.refresh(blog_to_update)
    return blog_to_update


def delete_blog_by_id(id: int, db: Session) -> Blog:
    blog_to_delete = db.query(Blog).filter(Blog.id == id).first()
    if not blog_to_delete:
        return {"error": "Blog not found"}
    blog_to_delete.is_active = False
    db.add(blog_to_delete)
    db.commit()
    db.refresh(blog_to_delete)
    return {"msg": "Blog deleted successfully"}
