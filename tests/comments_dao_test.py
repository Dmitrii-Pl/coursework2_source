import pytest

from app.posts.dao.comments_dao import CommentsDAO
from app.config import *

class TestCommentsDAO:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDAO(COMMENTS)

    @pytest.fixture
    def keys_expected(self):
        return {"post_id", "commenter_name", "comment", "pk"}

    def test_get_by_post_pk_check_type(self, comments_dao):
        comments = comments_dao.get_by_post_id(1)
        assert type(comments) == list, "Результат должен быть списком"
        assert type(comments[0]) == dict, "Результат должен быть словарем"

    def test_get_by_post_pk_check_keys(self, comments_dao, keys_expected):
        comment = comments_dao.get_by_post_id(1)[0]
        comment_keys = set(comment.keys())
        assert comment_keys == keys_expected, "Список ключей не соответствует"

