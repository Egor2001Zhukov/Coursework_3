from flask import Flask, render_template
import logging
from utils import *
from blueprint_post.views import post_blueprint
from blueprint_search.views import search_blueprint
from blueprint_userfeed.views import userfeed_blueprint


app = Flask(__name__)

app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(userfeed_blueprint)


logging.basicConfig(level=logging.INFO)
logger_api = logging.getLogger('logger_api')
file_handler = logging.FileHandler('api.log', encoding='utf-8')
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter_one)
logger_api.addHandler(file_handler)


@app.route('/api/posts', methods=['GET'])
def api_posts():
    posts = get_posts_all()
    logger_api.info('Запрос /api/posts')
    return posts


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def api_post_id(post_id):
    post = get_post_by_pk(post_id)
    logger_api.info(f'Запрос /api/posts/{post_id}')
    return post


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), error


@app.errorhandler(500)
def server_error(error):
    return render_template('error500.html'), error


@app.route('/', methods=['GET'])
def main_page():
    data_posts = get_posts_all()
    dict_of_comments = {post['pk']: get_comments_by_post_id(post['pk']) for post in data_posts}
    return render_template('index.html', data_posts=data_posts, comments=dict_of_comments)


if __name__ == "__main__":
    app.run(debug=True)
