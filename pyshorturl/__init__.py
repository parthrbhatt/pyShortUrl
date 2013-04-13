'''pyShortUrl: URL Shortening lib written in Python.

Copyright (c) 2012 Parth Bhatt

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN
AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

__version__ = '0.0.1'
__author__ = "Parth Bhatt <parthrbhatt@gmail.com>"

# Mark the user agent string for http requests with the lib version & shove it
# into the conf module.
import ShortUrl.conf
ShortUrl.conf.USER_AGENT_STRING = 'pyShortUrl v%s' %__version__

from ShortUrl.bit_ly import Bitly, BitlyError
from ShortUrl.bit_ly_v2 import Bitly as BitlyV2, BitlyError as BitlyV2Error
from ShortUrl.goo_gl import Googl, GooglError
from ShortUrl.is_gd import Isgd
from ShortUrl.v_gd import Vgd, VgdError
from ShortUrl.git_io import Gitio, GitioError
from ShortUrl.tinyurl_com import TinyUrlcom, TinyUrlcomError

from ShortUrl.base_shortener import BaseShortener, ShortenerServiceError
from ShortUrl.conf import SUPPORTED_SERVICES, SUPPORTED_DOMAINS
