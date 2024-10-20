from app.extensions import db
from datetime import datetime, timezone


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, 
                   primary_key=True)
    
    content = db.Column(db.String, 
                        nullable=False)
    
    img_url = db.Column(db.String, 
                        nullable=False, 
                        default="default_image.jpg")
    
    created = db.Column(db.DateTime, 
                        nullable=False, 
                        default=datetime.now(timezone.utc))
    
    from_thread = db.Column(db.Integer,
                            db.ForeignKey("thread.id"), 
                            nullable=False)
    
    thread = db.relationship("Thread", 
                            back_populates="posts")