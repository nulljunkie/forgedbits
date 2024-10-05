from django.db import connection, reset_queries
from django.test import TestCase
from users.models import User

from .models import Post


class SelectRelatedTest(TestCase):

    def setUp(self):
        imad = User.objects.create(username='imad', password="PassWord@99")
        john = User.objects.create(username='john', password="PassWord@99")
        tom = User.objects.create(username='tom', password="PassWord@99")
        creg = User.objects.create(username='creg', password="PassWord@99")
        Post.objects.create(author=imad, title="post 1", content="content of post 1")
        Post.objects.create(author=imad, title="post 2", content="content of post 2")
        Post.objects.create(author=john, title="post 3", content="content of post 3")
        Post.objects.create(author=tom, title="post 4", content="content of post 4")
        Post.objects.create(author=tom, title="post 5", content="content of post 5")
        Post.objects.create(author=creg, title="post 6", content="content of post 6")

    def test_queries_without_select_related(self):

        reset_queries()

        posts = Post.objects.all()
        for post in posts:
            print(post.title, post.author.username)

        print(f"Queries executed: {len(connection.queries)}")

        for query in connection.queries:
            print(query['sql'])

    def test_queries_with_select_related(self):

        reset_queries()

        posts = Post.objects.select_related('author').all()
        for post in posts:
            print(post.title, post.author.username)

        print(f"Queries executed: {len(connection.queries)}")
        for query in connection.queries:
            print(query['sql'])
