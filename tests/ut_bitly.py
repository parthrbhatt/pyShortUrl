
import imghdr
import os
import sys
import unittest
import imghdr

lib_path = os.path.abspath(os.path.join(os.getcwd(), '../'))
sys.path.append(lib_path)

from pyshorturl import Bitly, BitlyV2

class TestBitly(unittest.TestCase):

    def setUp(self):
        self.login = 'pyshorturl'
        self.api_key = 'R_8a316454593adcec10cf5a56ac663e68'
        self.test_long_url = 'http://www.parthbhatt.com/blog/'
        self.test_short_url = 'http://bit.ly/HqeEe8'
        self.test_short_url_hash = 'HqeEe8'
        self.qr_image_path = 'qr.png'

    def tearDown(self):
        if os.path.exists(self.qr_image_path):
            os.unlink(self.qr_image_path)

    def test_shorten_url(self):
        service = Bitly(login=self.login, api_key=self.api_key)
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_shorten_url_with_domain(self):
        service = Bitly(login=self.login, api_key=self.api_key)

        for domain in ('bit.ly', 'j.mp', 'bitly.com'):
            generated_short_url = service.shorten_url(self.test_long_url, domain=domain)
            expected_short_url = 'http://' + domain + '/' + self.test_short_url_hash
            self.assertEqual(expected_short_url, generated_short_url)

    def test_expand_url(self):
        service = Bitly(login=self.login, api_key=self.api_key)
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)

    def test_write_qr_image(self):
        service = Bitly(login=self.login, api_key=self.api_key)
        service.write_qr_image(self.test_short_url, self.qr_image_path)

        self.assertEqual('png', imghdr.what(self.qr_image_path))

    def test_validate(self):
        service = Bitly(login=self.login, api_key=self.api_key)
        result = service.validate()
        self.assertEqual(True, result)

        result = service.validate(login=self.login+'x', api_key=self.api_key)
        self.assertEqual(False, result)

    def test_shorten_url_v2(self):
        service = BitlyV2(login=self.login, api_key=self.api_key)
        generated_short_url = service.shorten_url(self.test_long_url)

        self.assertEqual(self.test_short_url, generated_short_url)

    def test_expand_url_v2(self):
        service = BitlyV2(login=self.login, api_key=self.api_key)
        generated_long_url = service.expand_url(self.test_short_url)

        self.assertEqual(self.test_long_url, generated_long_url)

    def test_write_qr_image_v2(self):
        service = Bitly(login=self.login, api_key=self.api_key)
        service.write_qr_image(self.test_short_url, self.qr_image_path)

        self.assertEqual('png', imghdr.what(self.qr_image_path))


if '__main__' == __name__:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBitly)
    unittest.TextTestRunner(verbosity=2).run(suite)
