# encoding: utf-8

from setuptools import find_packages, setup


setup(name='travel_dct',
      description='A basic dictionary for classification of travel keywords',
      author='Scott Jackson',
      author_email='scottdhjackson@gmail.com',
      version='0.0.1',
      license='MIT',
      packages=find_packages(),
      keywords='basic dictionary for travel keywords',
      install_requires=[
          'google-api-python-client>=1.7.3',
          'python-dateutil>=2.7.3',
          'google-auth>=1.5.0',
          'google-auth-oauthlib>=0.2.0'
      ],
      test_suite='tests'
      )