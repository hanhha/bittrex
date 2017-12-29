#!/usr/bin/env python3

from setuptools import setup
setup (name = 'bittrex',
			version = '1.0',
			py_modules=['bittrex'],
      description = 'A Python wrapper for Bittrex exchange API',
      author = 'Hanh Ha',
      author_email = 'tranhanh.haminh@gmail.com',
      license = 'MIT',
			url = 'https://github.com/hanhha/bittrex',
      install_requires = [
        'requests',
        'retrying',
        'simplejson',
      ]
    )
