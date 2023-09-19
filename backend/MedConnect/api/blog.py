from api import db
from flask import Blueprint, jsonify, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models import Posts

blog = Blueprint('blog', __name__)

@jwt_required
@blog.route('/post/<int:post_id>', strict_slashes=False)
def post(post_id):
    # get user with id
    post = Posts.query.get(posts_id)
    if post:
        return jsonify(post), 200
    abort(404)

@jwt_required
@blog.route('/posts/', strict_slashes=False)
def all_posts():
    # get all posts from db
    posts = Posts.query.all()
    if posts:
        return jsonify(posts)

@jwt_required
@blog.route("/posts/<int:id>", methods=["POST"])
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

@jwt_required
@blog.route("/posts/<int:id>", methods=["PUT"])
def update_post(post_id):
    post = Posts.query.get(id)
    if not post:
          return jsonify({'message': 'Health advice post not found'}), 404
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.content = data.get('content', post.content)

    db.session.commit()

    return jsonify({'message': 'Health advice post updated successfully'}), 200  

@jwt_required
@blog.route("/posts/<int:id>", methods=["DELETE"])
def delete_post(post_id):
    post = Posts.query.get(id)
    if not post:
        return jsonify({'message': 'Health advice post not found'}), 404
    
    db.session.delete(post)
    db.session.commit()

