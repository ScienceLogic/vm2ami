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

          'Development Status :: 4 - Beta',
          'Intended Audience :: System Administrators',
          'Topic :: Other/Nonlisted Topic',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',

      ]

      )
