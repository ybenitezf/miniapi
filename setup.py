"""
Miniapi
----------

A simple api application
"""
from setuptools import find_packages, setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='miniapi',
    version='0.0.1',
    url='https://github.com/ybenitezf/miniapi',
    license='GPL',
    author='Yoel Benítez Fonseca',
    author_email='ybenitezf@gmail.com',
    description='A simple api application',
    long_description=read('README.md'),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    install_requires=[
        'wheel',
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
