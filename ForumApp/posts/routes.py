from ForumApp.posts import bp
from flask import render_template, flash
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from flask_bcrypt import Bcrypt
from flask import current_app as app
bcrypt = Bcrypt(app)
from ForumApp.models.user import User
from ForumApp.models.post import Post
from flask import render_template, redirect, url_for, session, request, Flask
from ForumApp.models.board import Board

from ForumApp.extensions import db

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/board/<int:id>/create', methods = ['GET', 'POST'])
def add_post(id):
    board = Board.query.filter_by(id=id).first()
    if request.method == 'POST':
        post = Post()
        post.content = request.form['content']
        title = request.form['title']
        post.title=title
        post.board_id = id
        db.session.add(post)
        db.session.commit()
        posts = board.posts
        return render_template('post/post.html', posts = posts, board = board)
    posts = board.posts
    return render_template('post/post.html', posts=posts, board=board)
@bp.route('/board/<int:id>')
@login_required
def show_board(id):
    board = Board.query.filter_by(id=id).first()
    posts = board.posts
    return render_template('post/post.html', posts=posts, board = board)
