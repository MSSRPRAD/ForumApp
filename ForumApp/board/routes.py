from ForumApp.board import bp
from flask import render_template, flash
from flask_login import login_required, login_user, LoginManager, current_user, logout_user
from flask_bcrypt import Bcrypt
from flask import current_app as app
bcrypt = Bcrypt(app)
from ForumApp.models.user import User
from flask import render_template, redirect, url_for, session, request, Flask
from ForumApp.models.board import Board

from ForumApp.extensions import db

@app.login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/board')
@login_required
def board():
    boards = Board.query.all()
    return render_template('board/board.html', boards = boards)

@bp.route('/board/create', methods = ['GET', 'POST'])
@login_required
def create_board():
    if request.method == 'POST':
        name = request.form['name']
        about = request.form['about']
        board = Board()
        board.name=name
        board.about=about

        existing_board = Board.query.filter_by(name=name).first()
        if existing_board:
            flash("That name is already taken, please choose another")
            return render_template('board/board.html', boards = Board.query.all())
        else:
            db.session.add(board)
            db.session.commit()
            return render_template('board/board.html', boards = Board.query.all())
