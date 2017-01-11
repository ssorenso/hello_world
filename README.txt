hello_world
===========

An app that prints 'Hello World'.
---------------------------------

This is a simple script that will install a python-driven application that will
install a binary that will print 'Hello World' into the terminal when run.

Example:
--------

python ./setup.py test
python ./setup.py install
/path/to/python/bin/hello_world

Revision History
----------------
v1.0.0 - builds properly and dumps into terminal the 'Hello World' expected.
v1.0.1 - should require pytest-runner module from pip now.
v1.0.2 - Confirmed I was using a different copy of this code than I should have
    been.  I've modified it to use the original and this now does not install
    pytest or pytest-runner, but will allow the user to execute the tests as
    necessary on their local systems.
