from flask import render_template, redirect, request, url_for, abort
from app import models
from app import app, member_store, post_store


@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html", posts=post_store.get_all())


@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "GET":
        return render_template("topic_add.html")
    elif request.method == "POST":
        new_post = models.Post(title = request.form["topictitle"], content = request.form["topicbody"])
        post_store.add(new_post)
        return redirect(url_for("home"))


@app.route("/topic/show/<int:id>")
def topic_show(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    return render_template("topic_show.html", post=post)


@app.route("/topic/delete/<int:id>")
def topic_delete(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    post_store.delete(id)
    return redirect(url_for("home"))


@app.route("/topic/update/<int:id>", methods=["GET", "POST"])
def topic_update(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404)
    if request.method == "GET":
        return render_template("topic_update.html", post=post)
    if request.method == "POST":
        post.title = request.form["topictitle"]
        post.content = request.form["topicbody"]
        post_store.update(post)
        return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
