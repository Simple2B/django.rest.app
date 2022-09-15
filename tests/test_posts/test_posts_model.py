from posts.models import Post
from tests.conftest import create_posts, RANGE_COUNT


def test_create_post(create_posts):
    posts = Post.objects.all()
    for i in range(RANGE_COUNT):
        assert posts[i].id == i+1
        assert posts[i].title == f'test_post{i}'


def test_get_post(create_posts):
    first_post = Post.objects.get(pk=1)
    assert first_post.title == 'test_post0'


def test_get_post_list(create_posts):
    posts = Post.objects.all()
    assert len(posts) == RANGE_COUNT
