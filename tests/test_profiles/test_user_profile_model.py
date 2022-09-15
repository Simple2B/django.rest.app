from profiles.models import UserProfile


def test_hashing_password(db):
    UserProfile.objects.create(username='test', email='test@mail.com', password='11111111')
    user_profile = UserProfile.objects.get(username='test')
    assert user_profile.password_hash
    assert user_profile.email == 'test@mail.com'