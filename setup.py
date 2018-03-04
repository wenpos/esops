#!/usr/bin/env python
from distutils.core import setup
setup(name='esops',
      version='1.0',
      description='a tool for elasticsearch ops',
      author='wenpos',
      author_email='gward@python.net',
      url='https://github.com/wenpos/esops',
      install_requires=[
          'elasticsearch>=5.4.0,<6.0.0'
      ],
      packages=['esops'],
     )