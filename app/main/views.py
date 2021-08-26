from flask import render_template ,flash,url_for,abort,redirect,request
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from .forms import UpdateProfile,CommentForm
from ..models import Article, User,Comment
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

        return redirect(url_for('main.profile', username = user.username))

    return render_template('profile/update.html')

@main.route('/profile/<username>/update/pic',methods = ['POST'])
@login_required

def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path

        flash('Image has been updated succesfully')

    return redirect(url_for('main.update_profile',username = username))


@main.route('/article/new',methods = ['GET','POST'])
@login_required
def new_article():
    if request.method == 'POST':
        article_title = request.form['title']
        article_body = request.form['body']
        article_tag = request.form['tag']
        filename = photos.save(request.files['photo'])
        article_cover_path = f'photos/{filename}'

        new_article = Article(article_title = article_title,article_body= article_body,article_tag = article_tag,article_cover_path=article_cover_path)
        new_article.save_article()

@main.route('/articles/tag/<tag>')
@login_required
def article_by_tag(tag):

   
  
    articles=Article.query.filter_by(article_tag=tag).order_by(Article.posted.desc()).all()
    
    return render_template('article_by_tag.html',articles=articles,tag=tag)    

@main.route('/article_details/<article_id>', methods = ['GET','POST'])
@login_required
def article_details(article_id):

    form = CommentForm()
    article=Article.query.get(article_id)
    comments=Comment.query.filter_by(article_id=article_id).order_by(Comment.posted.desc()).all()
    
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment,user=current_user,article=article)
        new_comment.save_comment()
        article.article_comments_count = article.article_comments_count+1

        db.session.add(article)
        db.session.commit()
        flash('Comment posted')
        return redirect(url_for('blog.article_details',article_id=article_id))

    return render_template('article_details.html',comment_form=form,article=article,comments=comments)


