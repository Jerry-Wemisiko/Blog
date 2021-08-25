from flask import render_template ,flash
from flask.helpers import url_for
from flask_login import login_required
from werkzeug.exceptions import abort
from werkzeug.utils import redirect
from . import main
from .. import db
from ..models import Article, User
from ..requests import get_quotes

@main.route('/')

def index():
    quotes = get_quotes()
    articles = Article.get_all_articles()
    popular = Article.query.order_by(Article.article_upvotes.desc()).limit(3).all()
    return render_template ('index.html',quotes = quotes ,articles = articles,popular = popular)

@main.route('/profile/<username>')
@login_required

def profile(username):

    user = User.query.filter_by(username = username).first()

    if user in None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/profile/<username>/update', methods = ['GET','POST'])
@login_required

def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = update_profile()

    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()

        flash('Profile has been updated successfully.')

        return redirect(url_for('blog.profile', username = user.username))

    return render_template('profile/update.html')
