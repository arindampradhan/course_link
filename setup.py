#!/usr/bin/env python

from setuptools import setup, find_packages
import course_link


setup(  
    name='course_link', 
    version=course_link.__version__,
    description='download videos ,pdfs and pptx from coursera preview',
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='howdoi help console command line answer',
    author=course_link.__author__,
    author_email='arindampradhan10@gmail.com',
    maintainer='Arindam Pradhan',
    maintainer_email='arindampradhan10@gmail.com',
    url='https://github.com/arindampradhan/course_link',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cralink = course_link.coursera_list:ineed_link',
        ]
    },
    install_requires=[
    'beautifulsoup4',
    'requests'
    ] 
)
