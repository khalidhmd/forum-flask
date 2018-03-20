from sqlalchemy import desc, func
from app import db
import datetime

class Member(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    posts = db.relationship("Post", backref="members")

    def __repr__(self):
        return 'Name: {}, Age: {}, Posts: {}'.format(self.name, self.age, len(self.posts))

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "posts": self.member_posts
        }

class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    content = db.Column(db.String(800))
    member_id = db.Column(db.Integer, db.ForeignKey("member.id"))
    post_date = db.Column(db.Date)

    def __repr__(self):
        return 'Title: {}, Content: {}'.format(self.title, self.content)

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "member_id": self.member_id,
            "date": self.post_date
        }
        
