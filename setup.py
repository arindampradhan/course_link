#!/usr/bin/env python

from setuptools import setup, find_packages
import course_link



News
====

long_description = """
%(README)s

News
====

%(CHANGES)s

""" % read('README', 'CHANGES')

setup(
    name='course_link',
    version=course_link.__version__,
    description='download videos ,pdfs and pptx from coursera preview',
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='howdoi help console command line answer',
    author=course_link.__author__,
    author_email='arindampradhan10@gmail.com',
    maintainer='Arindam Pradhan',
    maintainer_email='arindampradhan10@gmail.com',
    url='https://github.com/arindampradhan/courselink',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'howdoi = howdoi.howdoi:command_line_runner',
        ]
    },
    install_requires=[
    'beautifulsoup40',
    'requests'
    ] + extra_dependencies(),
)