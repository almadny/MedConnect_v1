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


@posts.route('post/<int:id>', strict_slashes=False)
def post(id):
    # get user with id
    post = Posts.query.filter_by(posts.id=id).first()
    if post:
        return jsonify(post), 200
    abort(404)

@posts.route('/posts/', strict_slashes=False)
def all_posts():
    # get all posts from db
    posts = Posts.query.all()
    if posts:
        return jsonify(posts)

@posts.route("/posts/<int:id>", methods=["POST"])
def create_posts():
    data = request.get_json()
    doctor_id = data.get('doctor_id')
    title = data.get('title')
    content = data.get('content')

    doctor = Doctor.query.get(doctor_id)
    if not doctor:
         return jsonify({'message': 'Only doctors can drop health advice'}), 404
    new_post = Posts(doctor_id=doctor_id, title=title, content=content)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message': 'Health advice post added successfully'}), 201


@posts.route("/posts/<int:id>", methods=["PUT"])
def update_post(post_id):
    post = Posts.query.get(id)
    if not post:
          return jsonify({'message': 'Health advice post not found'}), 404
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)

    db.session.commit()

    return jsonify({'message': 'Health advice post updated successfully'}), 200  

@posts.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(post_id):
    post = Posts.query.get(id)
    if not post:
        return jsonify({'message': 'Health advice post not found'}), 404
    
    db.session.delete(post)
    db.session.commit()
