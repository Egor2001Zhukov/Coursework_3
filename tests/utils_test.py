import pytest
from utils import *


def test_type_get_posts_all():
    assert type(get_posts_all()) == list, "Возвращается не список"


class Test_get_post_by_pk:
    def test_type_get_post_by_pk(self):
        assert type(get_post_by_pk(1)) == dict, "Возвращается не словарь"

    def test_typeerror_get_post_by_pk(self):
        with pytest.raises(TypeError):
            get_post_by_pk("2")

    def test_valueerror_type_get_post_by_pk(self):
        with pytest.raises(ValueError):
            get_post_by_pk(0)


class Test_search_for_posts:
    def test_type_search_for_posts(self):
        assert type(search_for_posts("aaa")) == list, "Возвращается не список"

    def test_typeerror_search_for_posts(self):
        with pytest.raises(TypeError):
            search_for_posts(2)


class Test_get_comments_by_post_id:
    def test_get_comments_by_post_id(self):
        assert type(get_comments_by_post_id(1)) == list, "Возвращается не список"

    def test_typeerror_get_comments_by_post_id(self):
        with pytest.raises(TypeError):
            get_comments_by_post_id("2")

    def test_valueerror_get_comments_by_post_id(self):
        with pytest.raises(ValueError):
            get_comments_by_post_id(0)

