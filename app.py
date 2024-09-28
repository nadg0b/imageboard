import os
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'
app.config['UPLOAD_FOLDER'] = 'static'
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    conn = get_db_connection()
    boards = conn.execute('SELECT * FROM boards').fetchall()
    conn.close()
    return render_template('index.html', boards=boards)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            if 'file' not in request.files:
                print("no file")
                img_url = "default.jpg"
            else:
                file = request.files['file']
                if file.filename == '':
                    print("no filename")
                    img_url = "default.jpg"
                else:
                    img_url = file.filename
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))

                conn = get_db_connection()
                conn.execute('INSERT INTO posts (title, content, img_url) VALUES (?, ?, ?)',
                            (title, content, img_url))
                conn.commit()
                conn.close()
                return redirect(url_for('index'))
        
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))


@app.route('/img/<filename>') 
def send_file(filename): 
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
    

if __name__ == "__main__":
    app.run(debug=True)