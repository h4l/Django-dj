#!/usr/bin/env python
from distutils.core import setup
from os import path

README = path.join(path.dirname(__file__), "README.rst")
with open(README) as f:
    LONG_DESCRIPTION = f.read()

setup(
    name="Django-dj",
    version="0.3.0",
    description=("A short command which replaces calls to Django's manage.py "
            "scripts"),
    author="Hal Blackburn",
    author_email="hal@caret.cam.ac.uk",
    url="https://github.com/h4l/Django-dj",
    scripts=["dj"],
    requires=[
        "Django (>=1.4)"
    ],
    license="BSD",
    classifiers=[
        "Intended Audience :: Developers",
        "Environment :: Console",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Internet :: WWW/HTTP",
    ],
    long_description=LONG_DESCRIPTION,
)
