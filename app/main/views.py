from flask import render_template 
from . import main
from ..models import Article


@main.route('/')
def index():
    quotes = get_quotes()
    articles = Article.get_all_articles()
    popular = Article.query.order_by(Article.article_upvotes.desc()).limit(3).all()
    return render_template ('index.html',quotes = quotes ,articles = articles,popular = popular)

