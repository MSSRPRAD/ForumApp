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
from ForumApp.models.notification import Notification
from ForumApp import ckeditor
from ForumApp.extensions import db

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/board/<int:id>/create', methods = ['GET', 'POST'])
@login_required
def add_post(id):
    red = '/board/' + str(id)
    board = Board.query.filter_by(id=id).first()
    if request.method == 'POST':
        post = Post()
        post.content = request.form['ckeditor']
        title = request.form['title']
        post.title=title
        post.board_id = id
        post.user_id = current_user.id
        db.session.add(post)


        if board.user_id != current_user.id:
            notif = Notification()
            notif.user_id = board.user_id
            notif.message = current_user.username + " has created a post titled - " + post.title +" in your board - " + board.name
            db.session.add(notif)

        db.session.commit()
        posts = board.posts
        return redirect(red)
    posts = board.posts
    return redirect(red)

@bp.route('/board/<int:id>')
def show_board(id):
    board = Board.query.filter_by(id=id).first()
    posts = board.posts
    users = User.query.all()
    return render_template('src/post/post.html', posts=posts, board = board, users=users)
