 
import imghdr
import os
import sys
import unittest

from ShortUrl.goo_gl import Googl

class TestGoogl(unittest.TestCase):

    def setUp(self):
        self.test_long_url = 'http://www.google.com'
        self.test_short_url = 'http://goo.gl/fbsS'
        self.qr_image_path = 'qr.png'

    def tearDown(self):
        if os.path.exists(self.qr_image_path):
            os.unlink(self.qr_image_path)

    def test_shorten_url_with_key(self):
        service = Googl(api_key='AIzaSyC0KUGJe63CkvuG7jQfXV5PgI9U-x2IdAI')
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_shorten_url_without_key(self):
        service = Googl()
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_write_qr_image(self):
        service = Googl()
        service.write_qr_image(self.test_short_url, self.qr_image_path)

        self.assertEqual('png', imghdr.what(self.qr_image_path))


if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGoogl)
    unittest.TextTestRunner(verbosity=2).run(suite)
