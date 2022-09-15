import pytest
import requests
from profiles.models import UserProfile
from posts.models import Post
from posts.views import PostViewSet


RANGE_COUNT = 3


@pytest.fixture
def create_user(db) -> UserProfile:
    return UserProfile.objects.create(username='test', email='test@mail.com', password='11111111')


@pytest.fixture
def create_posts(create_user) -> list:
    return [Post.objects.create(title=f'test_post{i}', content='test_content{i}', published=True, user_profile=create_user) for i in range(RANGE_COUNT)]


@pytest.fixture
def create_posts_in_view(create_user) -> None:
    pv_obj = PostViewSet(request=None, format_kwarg=None)
    for i in range(RANGE_COUNT):
        serializer = pv_obj.get_serializer(data={'title': f'test_post{i}', 'content': 'test_content{i}', 'published': True, 'user_profile': create_user.pk})
        serializer.is_valid(raise_exception=True)
        pv_obj.perform_create(serializer)
