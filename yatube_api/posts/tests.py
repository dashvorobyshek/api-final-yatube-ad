from django.test import TestCase
from posts.models import Post


class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post(text="Test")
        self.assertEqual(str(post), "Test")
