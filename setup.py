
""" Install script for pyShortUrl """

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyShortUrl",
    version = "0.0.1",
    author = "Parth Bhatt",
    author_email = "parthrbhatt@gmail.com",
    description = ("A python library to shorten urls using one of the url shortening services"),
    license = "BSD",
    keywords = "url shortening qrcode qr goo.gl bit.ly tinyurl.com j.mp bitly.com v.gd is.gd",
    url = "https://github.com/parthrbhatt/pyShortUrl",
    packages=['pyshorturl', 'pyshorturl/ShortUrl'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
