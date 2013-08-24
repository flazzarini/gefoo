Python Kinterbasdb from source on ubuntu
########################################
:date: 2011-12-30 09:48
:author: Frank Lazzarini
:category: Coding
:tags: python, coding, linux, firebird
:slug: python-kinterbasdb-from-source

This is a little tutorial about how to compiler python-kinterbasdb from
source in ubuntu, due to the fact that the official packages are broke.
First off you need the following dependencies **build-essentials**,
**python-dev**, **firebird2.1-dev**.

::

    root@linuxbox:~$ apt-get install build-essential python-dev firebird2.1-dev

Afterwords download the latest package from
`https://launchpad.net/ubuntu/+source/python-kinterbasdb`_ and extract
that file. Next you need to build the source package using the
**setup.py** script.

::

    root@linuxbox:~$ cd kinterbasdb-3.3.0/
    root@linuxbox:~$ python setup.py build
    root@linuxbox:~$ python setup.py install
    root@linuxbox:~$ python
    Python 2.7.2+ (default, Oct  4 2011, 20:06:09)
    [GCC 4.6.1] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import kinterbasdb
    >>>

That's all folks, if you have any question feel free to comment...

.. _`https://launchpad.net/ubuntu/+source/python-kinterbasdb`: https://launchpad.net/ubuntu/+source/python-kinterbasdb
