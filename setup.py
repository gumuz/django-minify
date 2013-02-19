import os
from setuptools import setup
from django_minify import __version__

if os.path.isfile('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = 'See http://pypi.python.org/pypi/django-minify/'

setup(
    name = 'django-minify',
    version = __version__,
    author = 'Rick van Hattem',
    author_email = 'Rick.van.Hattem@Fawo.nl',
    description = '''django-minify is a django app that combines and minifies
        css and javascript files.''',
    url='https://github.com/WoLpH/django-minify',
    license = 'BSD',
    install_requires=[
        'python-utils>=1.0',
        'portalocker>=0.3',
    ],
    packages=[
        'django_minify',
        'django_minify.templatetags',
    ],
    long_description=long_description,
    test_suite='nose.collector',
    setup_requires=[
        'nose>=1.0',
    ],
    package_data={'': ['yuicompressor-2.4.7.jar']},
    classifiers=[
        'License :: OSI Approved :: BSD License',
    ],
)
