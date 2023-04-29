import unittest
from unittest import mock
from Blog import Blog

class TestBlog(unittest.TestCase):
    def test_posts(self):
        # cria um objeto mock para a resposta da API
        mock_response = mock.Mock()
        mock_response.json.return_value = [{'id': 1, 'title': 'Test post', 'body': 'Lorem ipsum'}]

        # substitui a função requests.get pela resposta mock
        with mock.patch('requests.get', return_value=mock_response):
            # cria um objeto Blog e chama a função posts
            blog = Blog()
            posts = blog.posts()

            # verifica se a resposta é igual ao mock
            self.assertEqual(posts, [{'id': 1, 'title': 'Test post', 'body': 'Lorem ipsum'}])

    def test_post_by_user