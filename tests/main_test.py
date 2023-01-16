from run import app, api_posts, api_post_id


def test_app():
    response = app.test_client().get('/')
    assert response.status_code == 200


class TestAPI:
    def test_type_api_all_posts(self):
        # response = app.test_client().get('/api/posts')
        assert type(api_posts()) == list, 'Это не список'

    def test_keys_api_all_posts(self):
        keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
        for post in api_posts():
            for key in post.keys():
                assert key in keys, 'Ключи не соответствуют'

    def test_api_post_id(self):
        assert type(api_post_id(1)) == dict, 'Это не словарь'

    def test_keys_api_post_id(self):
        keys = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']
        for key in api_post_id(1):
            assert key in keys, 'Ключи не соответствуют'
