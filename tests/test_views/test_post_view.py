from posts.models import Post
from tests.conftest import create_posts_in_view, RANGE_COUNT


def test_create_post_in_view(create_posts_in_view):
    posts = Post.objects.all()
    for i in range(RANGE_COUNT):
        assert posts[i].id == i+1
        assert posts[i].title == f'test_post{i}'


def test_get_post_by_view(create_posts_in_view):
    first_post = Post.objects.get(pk=1)
    assert first_post.title == 'test_post0'


def test_get_post_list_by_view(create_posts_in_view):
    posts = Post.objects.all()
    assert len(posts) == RANGE_COUNT
