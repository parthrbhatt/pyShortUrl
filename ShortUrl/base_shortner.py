
import conf

class BaseShortner:
    """Base class for the url shortners in the lib"""

    def __init__(self, api_key):
        # goo.gl mandates that requests containing JSON content bodies must be
        # accompanied by a "Content-Type: application/json" request header.
        # Otherwise, the request will result in an Error (400: Bad Request).
        self.headers = {'Content-Type': 'application/json',
            'User-Agent': conf.USER_AGENT_STRING}
        self.api_key = api_key

    def set_api_key(self, api_key):
        self.api_key = api_key

    def shorten_url(self, long_url):
        raise NotImplementedError()

    def expand_url(self, short_url):
        raise NotImplementedError()

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
            This method will raise service specific exceptions. For eg. `GooglError`
            will be raised in case of goo.gl

        """
        image_data = self.get_qr_code(short_url)

        # ToDo: Handle errors.
        fd = open(image_path, 'w')
        fd.write(image_data)
        fd.close()

