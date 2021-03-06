#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

setuptools.setup(
    name = "commons_py",
    version = "0.2.1",
    author = "Hive Solutions Lda.",
    author_email = "development@hive.pt",
    description = "Commons Python",
    license = "Apache License, Version 2.0",
    keywords = "commons framework utilities",
    url = "http://commons_py.hive.pt",
    packages = [
        "commons"
    ],
    test_suite = "commons.test",
    package_dir = {
        "" : os.path.normpath("src")
    },
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
    ]
)
