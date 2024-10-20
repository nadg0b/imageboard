from flask import render_template

from app.main import bp
from app.extensions import db
from app.models.board import Board
from app.models.thread import Thread
from app.models.post import Post


@bp.route('/')
def index():
    boards = db.session.execute(db.select(Board).order_by(Board.id)).scalars()
    print(boards)

    random_pic = 1
    thread_url = "cats/1"
    
    return render_template("home.html", 
                           title = "ImageBoard - Home",
                           header = "Welcome to my ImageBoard",
                           boards = boards, 
                           random_pic = random_pic, 
                           thread_url = thread_url)


@bp.route("/<board_name>")
def board(board_name):
    threads = db.session.execute(db.select(Thread).filter_by(from_board = board_name)).scalars()
    print(threads)

    return render_template("threads.html", threads = threads)


@bp.route("/<board_name>/<int:thread_id>")
def thread(board_name, thread_id):
    posts = db.session.execute(db.select(Post).filter_by(id = thread_id)).scalars()
    print(posts)

    return render_template("posts.html", posts = posts)