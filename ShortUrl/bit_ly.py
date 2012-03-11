
import json
from urllib import urlencode
import urllib2

from base_shortner import BaseShortner, ShortnerServiceError
import conf

BITLY_SERVICE_URL = 'http://api.bit.ly/'
BITLY_API_VERSION = '2.0.1'

class BitlyError(ShortnerServiceError):
    pass

class Bitly(BaseShortner):

    def __init__(self, login, api_key):
        BaseShortner.__init__(self, api_key)
        self.login = login
        self.default_request_params = {
                  'version': BITLY_API_VERSION,
                  'format': 'json',
                  'login':  self.login,
                  'apiKey': self.api_key,
            }

    def _get_request_url(self, action, param_key, param_value):
        request_params = self.default_request_params
        request_params[param_key] = param_value
        request_params = request_params.items()

        encoded_params = urlencode(request_params)
        return "%s%s?%s" % (BITLY_SERVICE_URL, action, encoded_params)

    def _is_response_success(self, response):
        return ('OK' == response.get('statusCode'))

    def _get_error_from_response(self, response):
        # FixMe: Extract error from response dict received from bit.ly
        return 'Invalid Response'

    def shorten_url(self, long_url):
        request_url = self._get_request_url('shorten', 'longUrl', long_url)
        response = self._do_http_request(request_url)

        response = json.loads(response)
        if not self._is_response_success(response):
            msg = self._get_error_from_response(response)
            raise BitlyError(msg)

        results_dict = response.get('results')
        result = results_dict.get(long_url)
        return result.get('shortUrl')

    def expand_url(self, short_url):
        request_url = self._get_request_url('expand', 'shortUrl', short_url)
        response = self._do_http_request(request_url)

        response = json.loads(response)
        if not self._is_response_success(response):
            msg = self._get_error_from_response(response)
            raise BitlyError(msg)

        results_dict = response.get('results')
        return results_dict.values()[0].get('longUrl')

    def get_qr_code(self, short_url):
        qr_url = short_url + '.qrcode'
        response = self._do_http_request(qr_url)

        return response

    def get_short_url_info(self, short_url):
        request_url = self._get_request_url('info', 'shortUrl', short_url)
        response = self._do_http_request(request_url)

        response = json.loads(response)
        if not self._is_response_success(response):
            msg = self._get_error_from_response(response)
            raise BitlyError(msg)

        results_dict = response.get('results')
        return results_dict.values()[0]

    def get_stats(self, short_url):
        request_url = self._get_request_url('stats', 'shortUrl', short_url)
        response = self._do_http_request(request_url)

        response = json.loads(response)
        if not self._is_response_success(response):
            msg = self._get_error_from_response(response)
            raise BitlyError(msg)

        results_dict = response.get('results')
        return results_dict

