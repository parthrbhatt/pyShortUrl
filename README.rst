
===========
pyShortUrl
===========

A python library to shorten urls using one of the url shortening services.

pyShortUrl currently supports shortening urls using Google's URL shortening
service goo.gl. Future releases will add support for bit.ly and tinyurl.com

Install
=======

To install pyShortUrl:

::

  python setup.py install


Using pyShortUrl
================

pyShortUrl provides simple APIs that your python applications can use. Following
are some examples that show how you can use pyShortUrl:

Shorten a URL using goo.gl:

::

    from ShortUrl.goo_gl import Googl, GooglError

    long_url = 'http://www.google.com'
    service = Googl()
    try:
        short_url = service.shorten_url(long_url)
        print short_url
    except GooglError, e:
        print 'Error: %s' %e

Get QR code for a goo.gl short url:

::

    from ShortUrl.goo_gl import Googl, GooglError

    short_url = 'http://goo.gl/NMdyG'
    qr_img_path = 'qr_code.png'
    service = Googl()
    try:
        service.write_qr_image(short_url, qr_img_path)
    except GooglError, e:
        print 'Error: %s' %e


Using the pyshorturl-cli.py utility
===================================

pyShortUrl ships with a command-line utility called `pyshorturl-cli.py` that
allows you to use all the features of the library from the command line.

::

    $ python pyshorturl-cli.py -h
    Usage: pyshorturl-cli.py [options]

    Options:
      -h, --help            show this help message and exit
      -l LONG_URL, --long-url=LONG_URL
                            Shorten the specified URL.
      -s SHORT_URL, --short-url=SHORT_URL
                            Expand the specified Short URL.
      -k SVC_API_KEY, --api-key=SVC_API_KEY
                            Use API Key while communicating with the url shortening service.
      -q QR_IMG_PATH, --qr-code-file=QR_IMG_PATH
                            Used with -s. Writes the qr code for the corresponding short url.

Some examples of using the pyshorturl-cli.py utility:

::

    $ python pyshorturl-cli.py --long-url http://www.parthbhatt.com/blog/2011/geolocation-with-google-maps-javascript-api/
    http://goo.gl/NMdyG

    $ python pyshorturl-cli.py --short-url http://goo.gl/NMdyG --qr-code-file qr_code.png
    Wrote the qr code for http://goo.gl/NMdyG to qr_code.png


Unit tests
==========

