from api import db
from flask import Blueprint, jsonify, abort

posts = Blueprint('posts', __name__)

class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(15), nullable=True, index=True)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        """ Defines the appointment object string representation """
        return f"Post('{self.id}': '{self.title}' '{self.category}' '{self.date_posted}')"


@post.route('post/<int:post_id>', strict_slashes=False)
def post(post_id):
    # get user with id
    post = Posts.query.get(posts_id)
    if post:
        return jsonify(post), 200
    abort(404)

@posts.route('/posts/', strict_slashes=False)
def all_posts():
    # get all posts from db
    posts = Posts.query.all()
    if posts:
        return jsonify(posts)
