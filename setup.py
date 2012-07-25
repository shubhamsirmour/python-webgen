#!/usr/bin/env python

from distutils.core import setup
import os
import remtime

ROOT = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(ROOT, 'README')).read()

setup(name='python-webgen',
      version='0.1',
      description='static website generation',
      long_description=README,
      author=u'Remi Flamary',
      author_email='remi.flamary@gmail.com',
      url='http://remi.flamary.com',
      py_modules=['webgen'],
      platforms=['linux'],
      license = 'GPL',
      scripts=['scripts/webgen.py'],
      requires=["argparse (>=0.1)","configobj (>=4.7)","jinja2 (>= 2.6)","markdown (>= 2.1)"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Utilities'        
    ]
     )