from app.extensions import db
from datetime import datetime, timezone


class Thread(db.Model):
    __tablename__ = "thread"

    id = db.Column(db.Integer, 
                   primary_key=True)
    
    title = db.Column(db.String)
    
    img_url = db.Column(db.String, 
                        nullable=False, 
                        default="default_image.jpg")
    
    created = db.Column(db.DateTime, 
                        nullable=False, 
                        default=datetime.now(timezone.utc))
    
    from_board = db.Column(db.Integer,
                           db.ForeignKey("board.id"), 
                           nullable=False)
    
    board = db.relationship("Board", 
                            back_populates="threads")
    
    posts = db.relationship("Post",
                            back_populates="thread")
        

    