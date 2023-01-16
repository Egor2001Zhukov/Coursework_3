from flask import Flask, request, render_template
from utils import *
from blueprint_post.views import post_blueprint
from blueprint_search.views import search_blueprint
from blueprint_userfeed.views import userfeed_blueprint


app = Flask(__name__)

app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(userfeed_blueprint)


@app.route('/', methods=['GET'])
def main_page():
    data_posts = get_posts_all()
    dict_of_comments = {post['pk']: get_comments_by_post_id(post['pk']) for post in data_posts}
    return render_template('index.html', data_posts=data_posts, comments=dict_of_comments)


if __name__ == "__main__":
    app.run(debug=True)

