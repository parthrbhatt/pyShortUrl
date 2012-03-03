""" Install script for pyShortUrl
"""
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

"""
pyShortUrl Source Tree:

    pyShortURL/
    |-- README.rst
    |-- setup.py
    |-- ShortUrl
    |   |-- __init__.py
    |   |-- base_shortner.py
    |   |-- conf.py
    |   |-- goo_gl.py
"""

setup(
    name = "pyShortUrl",
    version = "0.0.1",
    author = "Parth Bhatt",
    author_email = "parthrbhatt@gmail.com",
    description = ("A python library to shorten urls using one of the url shortening services"),
    license = "BSD",
    keywords = "url shortening using goo.gl",
    #url = "",
    packages=['ShortUrl'],
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
