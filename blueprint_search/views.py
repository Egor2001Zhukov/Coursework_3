from flask import Blueprint, render_template
from utils import *


post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates', )


@post_blueprint.route('/posts/<int:pk>', methods=['GET'])
def post_by_pk(pk):
    post = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    return render_template('post.html', post=post, comments=comments)
