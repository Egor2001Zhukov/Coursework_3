import json


def get_posts_all():
    """Возвращает посты"""
    with open('../data/posts.json', 'r', encoding='utf-8')as file:
        return json.load(file)


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя.
    Функция должна возвращать пустой список, если у нет постов, у которых указан автором этот пользователь"""
    posts_user = []
    posts = get_posts_all()
    for post in posts:
        if post['poster_name'].lower() == user_name.lower():
            posts_user.append(post)
    return posts_user


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста.
    Функция должна вызывать ошибку ValueError если такого поста нет и пустой список, если у поста нет комментов"""
    post_pk = 0
    comments_of_post = []
    posts = get_posts_all()
    for post in posts:
        if post_id == post['pk']:
            post_pk = post_id
    if post_pk:
        with open('../data/comments.json', 'r', encoding='utf-8')as file:
            for comment in json.load(file):
                if comment["post_id"] == post_id:
                    comments_of_post.append(comment)
        return comments_of_post
    else:
        raise ValueError("No find post")


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    posts = get_posts_all()
    posts_query = []
    for post in posts:
        if query.lower() in post["content"].lower():
            posts_query.append(post)
    return posts_query


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post

print(get_post_by_pk(2))
