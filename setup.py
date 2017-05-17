#!/usr/bin/env python
from distutils.core import setup
import setuptools
setup(name='vm2ami',
      version='1.0.0',
      description="Export a vCenter VM's vmdks and ovf descriptor to local file system. Then upload a vmdk to the aws "
                  "s3 s bucket specified, convert the image to an AMI, then finally rename, and copy the image to "
                  "all specified regions.",
      author='Douglas Rohde',
      author_email='drohde@sciencelogic.com',
      packages=['vm2ami'],
      keywords='export vmdk vCenter vm ami upload ',
      url='todo',
      license="MIT",
      install_requires=[
          'ovfexporter',
          'amiuploader',
      ],
      scripts=['bin/vm2ami'],
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 4 - Beta',

          # Indicate who your project is intended for
          'Intended Audience :: Developers, Sys Admins',
          'Topic :: Other/Nonlisted Topic :: Export Tools',

          # Pick your license as you wish (should match "license" above)
          "License :: MIT License",

          # Specify the Python versions you support here. In particular, ensure
          # that you indicate whether you support Python 2, Python 3 or both.
          'Programming Language :: Python :: 2.7',

      ]

      )
