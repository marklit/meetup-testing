from os.path import abspath, join, dirname

from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

import mock


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
    
    @mock.patch('storages.backends.s3boto.S3BotoStorage', FileSystemStorage)
    def test_post_photo(self):
        photo_path = join(abspath(dirname(__file__)), 'fixtures/gradient.jpg')
        with open(photo_path) as photo:
            resp = self.client.post(reverse('create'), {
                'first_name': 'Test',
                'photo': photo
            })
            redirect = 'Location: http://testserver%s' % reverse('created')
            self.assertTrue(redirect in str(resp))
