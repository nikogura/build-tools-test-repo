from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='blah-blah-blah',
    version='1.0.2',
    url='https://github.com/nikogura/build-tools',
    author='Nik Ogura',
    author_email='nik.ogura@gmail.com',
    license='Apache 2.0',
    classifiers=[
        'Development Status ::4 - Beta',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='build',
    packages=['some-package'],
    package_dir={'foo': './'},
    install_requires=['requests'],
    extras_require={},
    package_data={},
    entry_points={}

)
