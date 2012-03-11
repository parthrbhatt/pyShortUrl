
import imghdr
import os
import sys
import unittest

from ShortUrl.bit_ly import Bitly

class TestBitly(unittest.TestCase):

    def setUp(self):
        self.test_long_url = 'http://www.parthbhatt.com/blog/'
        self.test_short_url = 'http://bit.ly/xJHGkJ'
        self.login = 'parthrbhatt'
        self.api_key = 'R_0938930c0e3f357efce18f2cdaf53f60'

    def test_shorten_url(self):
        service = Bitly(login=self.login, api_key=self.api_key)
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_expand_url(self):
        service = Bitly(login=self.login, api_key=self.api_key)
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)


if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBitly)
    unittest.TextTestRunner(verbosity=2).run(suite)
