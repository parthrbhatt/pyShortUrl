
from optparse import OptionParser
import os
import sys

try:
    from ShortUrl.goo_gl import Googl, GooglError
except:
    print 'pyShortUrl is not installed.'
    sys.exit(-1)

if '__main__' == __name__:

    parser = OptionParser()
    parser.add_option("-l", "--long-url", dest="long_url",
                      help="Shorten the specified URL.")

    parser.add_option("-s", "--short-url", dest="short_url",
                      help="Expand the specified Short URL.")

    parser.add_option("-k", "--api-key", dest="svc_api_key",
                      help="Use API Key while communicating with the url shortening service.")

    parser.add_option("-q", "--qr-code-file", dest="qr_img_path",
                      help="Used with -s. Writes the qr code for the corresponding short url.")

    (options, args) = parser.parse_args()

    if options.qr_img_path:
        if not options.short_url:
            print 'You need to specify a short url to get qr code.'
            print 'Usage: python %s -s <short_url> -q <image_path>' %(sys.argv[0])
            sys.exit(-1)

        service = Googl(options.svc_api_key)
        try:
            service.write_qr_image(options.short_url, options.qr_img_path)
        except GooglError, e:
            print e

        if os.path.exists(options.qr_img_path):
            print 'Wrote the qr code for %s to %s' %(options.short_url, options.qr_img_path)

        sys.exit(0)

    if options.long_url:
        service = Googl(options.svc_api_key)
        try:
            short_url = service.shorten_url(options.long_url)
            print short_url
        except GooglError, e:
            print e
        sys.exit(0)

    if options.short_url:
        service = Googl(options.svc_api_key)
        try:
            long_url = service.expand_url(options.short_url)
            print long_url
        except GooglError, e:
            print e
        sys.exit(0)

