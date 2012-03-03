
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

    def _get_request_url(self):
        request_url = GOOGL_SERVICE_URL
        if self.api_key:
            request_url = request_url + "?key=%s" %self.api_key
        return request_url

    def shorten_url(self, long_url):
        data = """{"longUrl": "%s"}""" %long_url

        request_url = self._get_request_url()
        request = urllib2.Request(request_url, data=data, headers=self.headers)
        try:
            connection = urllib2.urlopen(request)
            response = connection.read()

            response = json.loads(response)
            return response.get('id')
        except urllib2.HTTPError, e:
            raise GooglError('Unable to obtain QR code for %s. %s:%s' %(long_url, e.code, e.msg))
        except urllib2.URLError, e:
            raise GooglError('Unable to obtain QR code for %s. %s' %(long_url, e.reason))

    def get_qr_code(self, short_url):
        qr_url = short_url + '.qr'

        request = urllib2.Request(qr_url, headers=self.headers)
        try:
            connection = urllib2.urlopen(request)
            response = connection.read()

            return response
        except urllib2.HTTPError, e:
            raise GooglError('Unable to obtain QR code for %s. %s:%s' %(short_url, e.code, e.msg))
        except urllib2.URLError, e:
            raise GooglError('Unable to obtain QR code for %s. %s' %(short_url, e.reason))

