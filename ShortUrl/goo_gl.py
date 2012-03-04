
import json
import urllib2

from base_shortner import BaseShortner
import conf

GOOGL_SERVICE_URL = 'https://www.googleapis.com/urlshortener/v1/url'

class GooglError(Exception):
    pass

class Googl(BaseShortner):
    def __init__(self, api_key=None):
        BaseShortner.__init__(self, api_key)

    def _get_request_url(self, url_params={}):
        request_url = GOOGL_SERVICE_URL
        param_list = []

        if self.api_key:
            param_list.append('key=%s' %self.api_key)

        for param in url_params.keys():
            param_list.append('%s=%s' %(param, url_params.get(param)))
        params = '&'.join(param_list)

        if params:
            request_url = request_url + '?' + params

        return request_url

    def _do_http_request(self, request_url, data=None):
        if data:
            request = urllib2.Request(request_url, data=data, headers=self.headers)
        else:
            request = urllib2.Request(request_url, headers=self.headers)

        try:
            connection = urllib2.urlopen(request)
            response = connection.read()
            return response
        except urllib2.HTTPError, e:
            raise GooglError('Unable to obtain QR code for %s. %s:%s' %(long_url, e.code, e.msg))
        except urllib2.URLError, e:
            raise GooglError('Unable to obtain QR code for %s. %s' %(long_url, e.reason))

    def shorten_url(self, long_url):
        data = """{"longUrl": "%s"}""" %long_url

        request_url = self._get_request_url()
        response = self._do_http_request(request_url, data)

        response = json.loads(response)
        return response.get('id')

    def expand_url(self, short_url):
        url_params = {'shortUrl':short_url}
        request_url = self._get_request_url(url_params)

        response = self._do_http_request(request_url)
        response = json.loads(response)

        status = response.get('status')
        if 'REMOVED' == status:
            raise GooglError('Unable to obtain long url for %s. The url status is REMOVED.' %short_url)
        elif 'OK' == status:
            response = response.get('longUrl')

        return response

    def get_qr_code(self, short_url):
        qr_url = short_url + '.qr'
        response = self._do_http_request(qr_url)

        return response

