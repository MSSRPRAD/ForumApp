from ForumApp.comments import bp
from flask import render_template, flash
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from flask_bcrypt import Bcrypt
from flask import current_app as app
bcrypt = Bcrypt(app)
from ForumApp.models.user import User
from ForumApp.models.post import Post
from ForumApp.models.comment import Comment
from flask import render_template, redirect, url_for, session, request, Flask
from ForumApp.models.board import Board
from ForumApp.models.notification import Notification

from ForumApp.extensions import db

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/board/<int:boardid>/<int:postid>/create', methods = ['GET', 'POST'])
def add_comment(boardid, postid):
    board = Board.query.filter_by(id=boardid).first()
    post = Post.query.filter_by(id=postid).first()
    red = '/board/' + str(boardid) + '/' + str(postid)
    if request.method == 'POST':
        comment = Comment()
        comment.user_id = current_user.id
        comment.post_id = postid
        comment.content = request.form['content']
        db.session.add(comment)
        if current_user.id != post.user_id:
            notification = Notification()
            notification.user_id = post.user_id
            notification.message= current_user.username + " has commented under your post - " + post.title + " !"
            db.session.add(notification)
        db.session.commit()
        return redirect(red)
    return redirect(red)
@bp.route('/board/<int:boardid>/<int:postid>')
@login_required
def show_comments(boardid, postid):
    board = Board.query.filter_by(id=boardid).first()
    post = Post.query.filter_by(id=postid).first()
    comments = post.comments
    users = User.query.all()
    return render_template('src/comment/comment.html', post=post,board = board, comments=comments, users=users)
