from flask import render_template, redirect, request, url_for, abort, jsonify
from flask_api import status
from app import models
from app import app, member_store, post_store


@app.route("/api/topic/all")
def topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/add", methods = ["POST"])
def topic_create():
    request_data = request.get_json()
    new_post = models.Post(request_data["title"], request_data["body"])
    post_store.add(new_post)
    return jsonify(new_post.__dict__())


@app.route("/api/topic/get_topic/<int:id>")
def get_topic(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    return jsonify(post.__dict__())


@app.route("/api/topic/delete/<int:id>", methods=["DELETE"])
def delete(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    post_store.delete(id)
    return '', status.HTTP_204_NO_CONTENT


@app.route("/api/topic/update/<int:id>", methods=["PUT"])
def update(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    request_data = request.get_json()
    post.title = request_data["title"]
    post.body = request_data["body"]
    post_store.update(post)
    return jsonify(post.__dict__())


@app.errorhandler(404)
def page_not_found(e):
    return '', status.HTTP_404_NOT_FOUND

