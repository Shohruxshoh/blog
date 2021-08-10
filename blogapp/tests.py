from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from blogapp.models import Post


class BlogAppTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Testuser",
            email="test@gmail.com",
            password="123456"
        )

        self.post = Post.objects.create(
            title = "test title",
            body = "test body",
            author = self.user,
        )

    def test_string_representatoin(self):
        post = Post(title="Post mavzusi")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'test title')
        self.assertEqual(f'{self.post.author}', 'Testuser')
        self.assertEqual(f'{self.post.body}', 'test body')

    def test_post_list_view(self):
        resource = self.client.get(reverse('home'))
        self.assertEqual(resource.status_code, 200)
        self.assertContains(resource, 'test body')
        self.assertTemplateUsed(resource, 'home.html')

    def test_post_detail_view(self):
        resource = self.client.get(reverse('/post/1/'))
        no_resource = self.client.get(reverse('/post/1000/'))
        self.assertEqual(resource.status_code, 200)
        self.assertEqual(resource.status_code, 404)
        self.assertContains(resource, 'test title')
        self.assertTemplateUsed(resource, 'post_detail.html')
