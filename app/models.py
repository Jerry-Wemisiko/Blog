from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    articles = db.relationship('Article',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')   

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
        
    def __repr__(self):
        return f'User {self.username}'   


class Quote:
    '''
    Quote class to define Quote Objects
    '''
    def __init__(self,id,quote_text,quote_author):
        self.id =id
        self.quote_text = quote_text
        self.quote_author = quote_author

class Article(db.Model):
    'Article model schema'
    __tablename__ = 'articles'
    id = db.Column(db.Integer,primary_key = True)
    article_title = db.Column(db.String)
    article_body = db.Column(db.String)
    article_tag = db.Column(db.String)
    article_cover_path = db.Column(db.String())
    article_comments_count = db.Column(db.Integer, default=0)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    article_upvotes = db.Column(db.Integer, default=0)
    article_downvotes = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'article',lazy = "dynamic")
