
import conf
import urllib2

class ShortnerServiceError(Exception):
    pass

class BaseShortner:
    """Base class for the url shortners in the lib"""

    def __init__(self, api_key):
        self.headers = {
            'User-Agent': conf.USER_AGENT_STRING
        }
        self.api_key = api_key

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
            raise ShortnerServiceError('%s:%s' %(e.code, e.msg))
        except urllib2.URLError, e:
            raise ShortnerServiceError('%s' %(e.reason))

    def set_api_key(self, api_key):
        self.api_key = api_key

    def shorten_url(self, long_url):
        raise NotImplementedError()

    def expand_url(self, short_url):
        response = urllib2.urlopen(short_url)
        return response.url

    def get_qr_code(self, short_url):
        raise NotImplementedError()

    def write_qr_image(self, short_url, image_path):
        """Obtain the QR code image corresponding to the specified `short_url`
        and write the image to `image_path`.

        If the caller does not intent to use the png image file, `get_qr_code()`
        may be used to obtain raw image data.

        Keyword arguments:                                        
            long_url -- The url to be shortened.                  
                                                                  
        Returns:                                                  
            Returns raw png image data that constitutes the qr code image.

        Exceptions:
            `ShortnerServiceError` - In case of error
        """
        image_data = self.get_qr_code(short_url)

        # ToDo: Handle errors.
        fd = open(image_path, 'w')
        fd.write(image_data)
        fd.close()

