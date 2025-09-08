from django.test import TestCase
from django.shortcuts import reverse
from datetime import datetime
from .models import Blog


# Create your tests here.
class BlogHomeViewTest(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title="title6",
            author="Mehran",
            created_at=datetime.now(),
            content="Hello. This is a development environment"
        )

    def test_blog_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_blog_home_url_by_name(self):
        response = self.client.get(reverse('blog home'))
        self.assertEqual(response.status_code, 200)

    def test_blog_home_blogs_list(self):
        response = self.client.get('/')
        self.assertContains(response, self.blog.title[:20])
        self.assertContains(response, self.blog.author)
        self.assertContains(response, self.blog.created_at)
        self.assertContains(response, self.blog.content[:30])


class BlogIndividualViewTest(TestCase):
    def setUp(self):
        self.blog = Blog.objects.create(
            title="title6",
            author="Mehran",
            created_at=datetime.now(),
            content="Hello. This is a development environment"
        )
        self.response = self.client.get(f'blog/blogs/{self.blog.title}')

    def test_blog_individual_url(self):
        self.assertEqual(self.response.status_code, 200)

    def test_blog_individual_url_by_name(self):
        response = self.client.get(reverse(self.blog.title))
        self.assertEqual(response.status_code, 200)

    def test_blog_individual_details(self):
        self.assertContains(self.response, self.blog.title)
        self.assertContains(self.response, self.blog.author)
        self.assertContains(self.response, self.blog.content)
        self.assertContains(self.response, self.blog.created_at)
