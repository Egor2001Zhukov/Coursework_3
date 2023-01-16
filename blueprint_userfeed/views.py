from flask import Blueprint, render_template, request
from utils import *


search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates', )


@search_blueprint.route('/search', methods=['GET'])
def posts_by_search():
    text = request.args.get('words')
    posts = search_for_posts(text)
    dict_of_comments = {post['pk']: get_comments_by_post_id(post['pk']) for post in get_posts_all()}
    return render_template('search.html', posts=posts, comments=dict_of_comments)
