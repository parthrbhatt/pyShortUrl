
import unittest

from ShortUrl.tinyurl_com import TinyUrlcom

class TestTinyUrlcom(unittest.TestCase):

    def setUp(self):
        self.test_long_url = 'http://www.parthbhatt.com/blog/'
        self.test_short_url = 'http://tinyurl.com/8yuvzl5'

    def test_shorten_url(self):
        service = TinyUrlcom()
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_expand_url(self):
        service = TinyUrlcom()
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)


if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTinyUrlcom)
    unittest.TextTestRunner(verbosity=2).run(suite)
