from os.path import abspath, join, dirname
from shutil import rmtree
from tempfile import mkdtemp


from django.core.files.storage import FileSystemStorage
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from django.test.utils import override_settings
import mock


class ViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.media_folder = mkdtemp()

    def tearDown(self):
        rmtree(self.media_folder)

    @mock.patch('storages.backends.s3boto.S3BotoStorage', FileSystemStorage)
    def test_post_photo(self):
        photo_path = join(abspath(dirname(__file__)), 'fixtures/gradient.jpg')

        with open(photo_path) as photo:
            with override_settings(MEDIA_ROOT=self.media_folder):
                resp = self.client.post(reverse('create'), {
                    'first_name': 'Test',
                    'photo': photo
                })
                redirect = 'Location: http://testserver%s' % reverse('created')
                self.assertTrue(redirect in str(resp))
