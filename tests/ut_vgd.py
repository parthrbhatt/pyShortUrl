
import imghdr
import os
import sys
import unittest
import imghdr

lib_path = os.path.abspath(os.path.join(os.getcwd(), '../'))
sys.path.append(lib_path)

from pyshorturl import Vgd

class TestVgd(unittest.TestCase):

    def setUp(self):
        self.test_long_url = 'http://www.parthbhatt.com/blog/'
        self.test_short_url = 'http://v.gd/vUIV3O'

    def test_shorten_url(self):
        service = Vgd()
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_shorten_url_with_stats(self):
        service = Vgd()
        generated_short_url = service.shorten_url(self.test_long_url, logstats=True)

        # When logstats is enabled, a new url will be generated for the long url
        # so we cannot assertEqual(). Hence, we just check if we got a short url.
        if not generated_short_url.startswith('http://v.gd/'):
            raise AssertionError('Failed to generate short url with logstats enabled.')

    def test_expand_url(self):
        service = Vgd()
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)


if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVgd)
    unittest.TextTestRunner(verbosity=2).run(suite)
