from api import db
from flask import Blueprint, jsonify, abort, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.models import Posts, Doctors

blog = Blueprint('blog', __name__)

@jwt_required()
@blog.route('/post/<int:id>', strict_slashes=False)
def getPost(id):
    """
    get a blog Post
    """
    # get user with id
    post = Posts.query.get(id)
    if not post:
        return jsonify({'status' : 'post not found'}), 404
    return jsonify({
        'id' : post.id,
        'title' : post.title,
        'post' : post.content,
        'category' : post.category,
        'doctor_id' : post.doctor_id,
        'date_posted' : post.date_posted
        }), 200


@jwt_required()
@blog.route('/posts/', strict_slashes=False)
def getAllPosts():
    """
    Get all posts

    Args:
        None
    
    Returns:
        list - a serialized list of all posts

    """
    # get all posts from db
    posts = Posts.query.all()

    # Create a list of all posts
    all_posts = [
            {
                'id' : post.id,
                'title' : post.title,
                'post' : post.content,
                'category' : post.category,
                'doctor_id' : post.doctor_id,
                'date_posted' : post.date_posted
            }
            for post in posts
            ]
    # return the list of posts
    return jsonify({'posts': all_posts}), 200

@jwt_required()
@blog.route("/addpost", methods=["POST"], strict_slashes=False)
def addPost():
    """
    Add a post

    Args:
        None

    Returns:
        dict: A JSON dictionary with the status code of the operation
    """
    try:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        category = data.get('category')
        doctor_id = data.get('doctor_id')
        date_posted = data.get('date_posted')

        post = Posts(
                title=title,
                content=content,
                category=category,
                doctor_id=doctor_is,
                date_posted=date_posted
                )
        db.session.add(post)
        db.session.commit()
        return jsonify({'status': 'post added successfully'}), 200
    except Exception as e:
        print(e)
        return jsonify({'msg': 'error adding post'}), 400


@jwt_required()
@blog.route("/posts/<int:id>", methods=["PUT"])
def updatePost(id):
    """
    update post
    """
    post = Posts.query.get(id)
    if not post:
        return jsonify({'msg': 'post not found'}), 404
    try:
        data = request.get_json()
        post.title = data.get('title', post.title)
        post.content = data.get('content', post.content)
        post.category = data.get('category', post.category)

        db.session.commit()
        return jsonify({'msg': 'post updated successfully'}), 200
    except Exception as e:
        print(e)
        return jsonify({'msg': 'error updating post'}), 400


@jwt_required()
@blog.route("/posts/<int:id>", methods=["DELETE"])
def deletePost(id):
    post = Posts.query.get(id)
    if not post:
        return jsonify({'msg': 'post not found'}), 404
    
    db.session.delete(post)
    db.session.commit()
    return jsonify({'status' : 'post successfully deleted'}), 200


@blog.route("/posts/<int:id>", strict_slashes=False)
@jwt_required()
def getDoctorPosts(id):
    """
    Get all post by a particular doctor
    """
    # get doctor first
    doctor = Doctors.query.get(id)

    # check if doctor is available
    if not doctor:
        return jsonify({'msg': 'doctor not found'}), 404

    # Create a list of all post by doctor
    all_post = [
            {
                'id' : post.id,
                'title' : post.title,
                'content' : post.content,
                'category' : post.category,
                'date_posted' : post.date_posted
            }
            for post in doctor.posts
            ]
    # return the list of all post by doctor
    return jsonify({'posts': all_post}), 200
