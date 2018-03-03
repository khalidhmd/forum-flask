from app import models
from app import stores
from flask import Flask, render_template
from app import dummy_data as dm


app = Flask(__name__)

member_store = stores.MemberStore()
post_store = stores.PostStore()

from app.views import *
dm.seed_stores(member_store, post_store)

