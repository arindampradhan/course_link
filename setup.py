#!/usr/bin/env python
import course_link
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='course_link',
    description='simple course_link using http://ip-api.com/docs/api:json',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

    keywords='course_link',
    version=course_link.__version__,
    author=course_link.__author__,
    author_email=course_link.__author_email__,
    maintainer=course_link.__maintainer__,
    maintainer_email=course_link.__maintainer_email__,
    url=course_link.__url__,
    license='MIT',
    packages=['course_link',],
    entry_points={
        'console_scripts': [
            'coursr = course_link.course_link:main',
        ]
    },
    install_requires=['requests','BeautifulSoup4'],
)


print "\n####################\n# command - coursr #\n####################\n"