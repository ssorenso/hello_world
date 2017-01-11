#!/git/playground/hello_world/bin/python

# copyright 2017 F5 networks Inc.
#   All Rights Reserved
#
#   Licensed under the Apache License, Version 2.0 (the "License").
#
# Purpose:
#   This is a learning tool to simply install a simple module using setuptools.
#   This module will simply perform a 'hello world' functionality.
#


from setuptools import setup
from setuptools.command.test import test as TestCommand
import HelloWorld
import sys


version = HelloWorld.version
name = HelloWorld.name
author = HelloWorld.author
license = HelloWorld.license
author_email = HelloWorld.author_email
url = HelloWorld.url
keywords = HelloWorld.keywords
packages = HelloWorld.packages
tests_require = ['pytest']
setup(version=version, name=name, author=author, license=license,
      author_email=author_email, url=url, keywords=keywords, packages=packages,
      entry_points={'console_scripts':
                    ['hello_world = HelloWorld.__main__:main']},
      tests_require=tests_require, cmdclass={'test': PyTest},
      setup_requires=['pytest-runner'])
