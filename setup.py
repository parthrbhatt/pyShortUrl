
""" Install script for pyShortUrl """

import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyShortUrl",
    version = "0.0.9",
    author = "Parth Bhatt",
    author_email = "parthrbhatt@gmail.com",
    description = ("A python library to shorten urls using one of the url shortening services"),
    license = "MIT",
    keywords = "url shortening qrcode qr goo.gl bit.ly tinyurl.com j.mp bitly.com v.gd is.gd",
    platforms = ['Linux', 'Max OS X', 'Windows', 'BSD', 'Unix'],
    url = "https://github.com/parthrbhatt/pyShortUrl",
    data_files=[
        ('.', ['README.rst']),
      ],
    packages = ['pyshorturl', 'pyshorturl/ShortUrl'],
    long_description = read('README.rst'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Communications",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
