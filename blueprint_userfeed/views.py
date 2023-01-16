from flask import Blueprint, render_template, request
from utils import *


userfeed_blueprint = Blueprint('userfeed', __name__, template_folder='templates', )


@userfeed_blueprint.route('/users/<username>', methods=['GET'])
def posts_by_search(username):
    posts = get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts, username=username)
