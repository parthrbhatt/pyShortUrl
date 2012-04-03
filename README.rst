
===========
pyShortUrl
===========

A python library to shorten urls using one of the supported url shortening
services.

pyShortUrl supports shortening urls using:
  - goo.gl (Google's URL shortening service)
  - bit.ly, j.mp, bitly.com
  - tinyurl.com
  - v.gd
  - is.gd

Following table explains what features are supported for which services:

  +--------------+----------------------+-----------+-------------+
  | Domain       |  Shorten/Expand URL  |  QR code  | Statistics  |
  +--------------+----------------------+-----------+-------------+
  | goo.gl       |        YES           |   YES     |    NO       |
  +--------------+----------------------+-----------+-------------+
  | bit.ly       |        YES           |   YES     |    NO       |
  +--------------+----------------------+-----------+-------------+
  | j.mp         |        YES           |   YES     |    NO       |
  +--------------+----------------------+-----------+-------------+
  | bitly.com    |        YES           |   YES     |    NO       |
  +--------------+----------------------+-----------+-------------+
  | tinyurl.com  |        YES           |   NO      |    NO       |
  +--------------+----------------------+-----------+-------------+
  | v.gd         |        YES           |   NO      |    NO       |
  +--------------+----------------------+-----------+-------------+
  | is.gd        |        YES           |   NO      |    NO       |
  +--------------+----------------------+-----------+-------------+


Install
=======

To install pyShortUrl:

::

  python setup.py install


Using pyShortUrl
================

pyShortUrl provides simple APIs that your python applications can use. Following
are some examples that show how you can use pyShortUrl with goo.gl.

Using pyShortUrl for URL shortening with *goo.gl*
-------------------------------------------------

Shorten a URL using goo.gl:

::

    from ShortUrl.goo_gl import Googl, GooglError

    long_url = 'http://www.parthbhatt.com/blog/'
    service = Googl()
    try:
        short_url = service.shorten_url(long_url)
        print short_url
    except GooglError, e:
        print 'Error: %s' %e


Expand a goo.gl short url back to the original long url:

::

    from ShortUrl.goo_gl import Googl, GooglError

    short_url = 'http://goo.gl/RwsEG'
    service = Googl()
    try:
        long_url = service.expand_url(short_url)
        print long_url
    except GooglError, e:
        print 'Error: %s' %e


Note that while it is possible to shorten a url or expand a goo.gl short url
without an api key, the API reference document explicitly states that using an
API key is *highly recommended*.

To use an API Key, provide an optional argument while instantiating `Googl()`
object as follows:

::

    service = Googl(api_key=<your_api_key>)


Get QR code for a goo.gl short url:

::

    from ShortUrl.goo_gl import Googl, GooglError

    short_url = 'http://goo.gl/RwsEG'
    qr_img_path = '/path/to/qr_code.png'
    service = Googl()
    try:
        service.write_qr_image(short_url, qr_img_path)
    except GooglError, e:
        print 'Error: %s' %e


Using pyShortUrl for URL shortening with *bit.ly*, *j.mp* and *bitly.com*
-------------------------------------------------------------------------

You can use bit.ly exactly like you'd use goo.gl. Just initialize the *service*
object in the snippets above using *Bitly* instead of *Googl*.

::

    from ShortUrl.bit_ly import Bitly, BitlyError

    service = Bitly(<your_bit.ly_login>, <your_bit.ly_api_key>)


Note that while *goo.gl* allows using its services without an API key, *bit.ly*
does not. It is mandatory to associate every call to bit.ly with a valid
account and an API Key. Hence, to use URL shortening with bit.ly you will need
to provide an account name and API key.

To shorten a url using *j.mp* or *bitly.com*, specify the domain as an argument
to the `shorten` function call as shown below:

::

    from ShortUrl.bit_ly import Bitly, BitlyError

    long_url = 'http://www.parthbhatt.com/blog/'
    service = Bitly(<your_bit.ly_login>, <your_bit.ly_api_key>)
    try:
        short_url = service.shorten_url(long_url, domain='j.mp')
        print short_url
    except BitlyError, e:
        print '%s' %e

Using pyShortUrl for URL shortening with *tinyurl.com*
------------------------------------------------------

::

    from ShortUrl.tinyurl_com import TinyUrlcom
    
    service = TinyUrlcom()

You dont need any account name or api key to use TinyUrl.


Using the pyshorturl-cli.py utility
===================================

pyShortUrl ships with a command-line utility called `pyshorturl-cli.py` that
allows you to use all the features of the library from the command line.

::

    $ python pyshorturl-cli.py -h
    Options:
      -h, --help            show this help message and exit
      -r SERVICE, --service=SERVICE
                            One of the shortening services
                            goo.gl,bit.ly,tinyurl.com,v.gd,is.gd. Defaults to
                            goo.gl
      -d DOMAIN, --domain=DOMAIN
                            Domain bit.ly, j.mp or bitly.com to use while
                            shortening with bit.ly. Defaults to bit.ly
      -u LOGIN, --login=LOGIN
                            The user account to use with the url shortening
                            service.
      -l LONG_URL, --long-url=LONG_URL
                            Shorten the specified URL.
      -k SVC_API_KEY, --api-key=SVC_API_KEY
                            Use API Key while communicating with the url
                            shortening service.
      -s SHORT_URL, --short-url=SHORT_URL
                            Expand the specified Short URL.
      -q QR_IMG_PATH, --qr-code-file=QR_IMG_PATH
                            Used with -s. Writes the QR code for the corresponding
                            short url.


Some examples of using the pyshorturl-cli.py utility:

Shorten a long url using goo.gl:

::

    $ python pyshorturl-cli.py --long-url http://www.parthbhatt.com/blog/2011/geolocation-with-google-maps-javascript-api/
    http://goo.gl/NMdyG

Obtain the original long url for a goo.gl short url:

::

    $ python pyshorturl-cli.py --short-url http://goo.gl/NMdyG
    http://www.parthbhatt.com/blog/2011/geolocation-with-google-maps-javascript-api/

Optionally, provide an api key obtained from goo.gl while shortening a url or
expanding a short url. Following example shows you how you can provide an api
key while expanding a short url:

::

    $ python pyshorturl-cli.py --short-url http://goo.gl/NMdyG --api-key <your_goo.gl_api_key>
    http://www.parthbhatt.com/blog/2011/geolocation-with-google-maps-javascript-api/

Get the QR code for a goo.gl short url:

::

    $ python pyshorturl-cli.py --short-url http://goo.gl/NMdyG --qr-code-file qr_code.png
    Wrote the qr code for http://goo.gl/NMdyG to qr_code.png

Shorten a long url using bit.ly:

::

    $ python pyshorturl-cli.py --service bit.ly --login <your_bit.ly_account> --api-key <your_bit.ly_api_key> -l http://www.parthbhatt.com/blog/
    http://bit.ly/xJHGkJ

Shorten a long url using j.mp:

::

    $ python pyshorturl-cli.py --service bit.ly --login <your_bit.ly_account> --api-key <your_bit.ly_api_key> --domain j.mp -l http://www.parthbhatt.com/blog/
    http://j.mp/xJHGkJ

Obtain the original long url for a bit.ly short url:

::

    $ python pyshorturl-cli.py --service bit.ly --login <your_bit.ly_account> --api-key <your_bit.ly_api_key> -s http://bit.ly/xJHGkJ
    http://www.parthbhatt.com/blog/

Get the QR code for a bit.ly short url:

::

    $ python pyshorturl-cli.py --service bit.ly --login <your_bit.ly_account> --api-key <your_bit.ly_api_key> --short-url http://bit.ly/xJHGkJ --qr-code-file qr_code.png
    Wrote the qr code for http://bit.ly/xJHGkJ to qr_code.png


Shorten a long url using tinyurl.com:

::

    $ python pyshorturl-cli.py --service tinyurl.com --long-url http://www.parthbhatt.com/blog/
    http://tinyurl.com/8yuvzl5

Obtain the original long url for a tinyurl.com short url:

::

    $ python pyshorturl-cli.py --service tinyurl.com --short-url http://tinyurl.com/8yuvzl5
    http://www.parthbhatt.com/blog/
