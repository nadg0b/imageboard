from app.extensions import db
from datetime import datetime, timezone


class Board(db.Model):
    __tablename__ = "board"

    id = db.Column(db.Integer, 
                   primary_key=True)
    
    title = db.Column(db.String, 
                      nullable=False)
    
    description = db.Column(db.String)
    
    img_url = db.Column(db.String, 
                        nullable=False, 
                        default="default_image.jpg")
    
    created = db.Column(db.DateTime, 
                        nullable=False, 
                        default=datetime.now(timezone.utc))
    
    threads = db.relationship("Thread",
                            back_populates="board")
        