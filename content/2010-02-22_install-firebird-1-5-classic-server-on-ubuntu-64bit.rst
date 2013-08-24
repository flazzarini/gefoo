Install Firebird 1.5 Classic Server on Ubuntu 64bit
###################################################
:date: 2010-02-22 12:35
:author: Frank Lazzarini
:category: Linux
:tags: linux, firebird, ubuntu
:slug: install-firebird-1-5-classic-server-on-ubuntu-64bit

In Ubuntu versions > 8.04 you will encounter the problem that there are
no more packages of Firebird 1.5 Classic Server available in the package
repository. Therefore we need to install all dependencies and all
packages manually. Firebird 1.5 only exists in 32bit which results in
even more problems to install it. In Ubuntu you have always the
possibility to install old 32bit libraries via apt-get. In this tutorial
I will show you how to do just that.

**Installing packages**

First we will need the following packages **ia32-libs**, **lib32ncurses5**, 
**openbsd-inetd** (for Firebird). These are 32bit libraries needed for
Firebird 1.5 Classic.

::

    root@host:/# apt-get install ia32-libs lib32ncurses5 openbsd-inetd

But this is still not enough to satisfy Firebird, it still needs version
5.x of http://gcc.gnu.org/libstdc++/ which isn't included
in Ubuntu > 8.04 anymore. We will need to get our hands a little dirty
and install this librarie by hand. First go get the lib from ubuntu's
package repository website at http://packages.ubuntu.com. Once you
have transfered the file to your host continue doing the following to
extract the data from the deb file.

Updated 03.02.2011:

The link to the packages.ubuntu.com site isn't working anymore, here is
a new link to the libstdc++5 i386 library file
`http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-3.3/libstdc++5\_3.3.6-17ubuntu1\_i386.deb`_.

::

    root@host:~# ar xv libstdc++5_3.3.6-17ubuntu1_i386.deb
    root@host:~# tar xzvf data.tar.gz

All extracted from the debian package, now let's control if it is really
a 32bit File, if so we will install it to our systems 32bit library
directory.

::

    root@host:~# cd usr/lib/
    root@host:/usr/lib# file libstdc++.so.5.0.7
    libstdc++.so.5.0.7: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, stripped

The output of '''file''' seems to be correct, it reports a 32bit file so
we can go ahead.

::

    root@host:~/usr/lib# install libstdc++.so.5.0.7 /usr/lib32/
    root@host:~/usr/lib# cd /usr/lib32/
    root@host:/usr/lib32# ln -s libstdc++.so.5.0.7 libstdc++.so.5

Now we are good to go we have all the needed libraries to install
Firebird 1.5 Classic Server.

**Install Firebird 1.5 Classic Server**

Go to the `Firebird`_ website and download the following file
`FirebirdCS-1.5.6.5026-0.i686.tar.gz`_. Put that file onto your host and
extract it.

::

    root@host:~# tar xzvf FirebirdCS-1.5.6.5026-0.i686.tar.gz
    root@host:~# cd FirebirdCS-1.5.6.5026-0.i686
    root@host:~# ./install.sh``

One last thing, **/opt/firebird/bin** is still not in our **PATH**, so
let's add it. Open up **/etc/profile** and add the following line to the
end of the file.

::

    PATH=$PATH:/opt/firebird/bin

Test your firebird connection using one of the following commands...

::

    root@host:~# isql -user SYSDBA -pass yourpasswd localhost:employees

    or

    root@host:~# telnet localhost 3050

There you go you should have Firebird 1.5 32bit running on your 64bit
Server. Next post I will explain you how to install multiple firebird
server instances on one machine.

.. _`http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-3.3/libstdc++5\_3.3.6-17ubuntu1\_i386.deb`: http://mirrors.kernel.org/ubuntu/pool/universe/g/gcc-3.3/libstdc++5_3.3.6-17ubuntu1_i386.deb
.. _Firebird: http://www.firebirdsql.org/index.php?op=files&id=engine_156
.. _FirebirdCS-1.5.6.5026-0.i686.tar.gz: http://sourceforge.net/projects/firebird/files/firebird-linux-i386/1.5.6-Release/FirebirdCS-1.5.6.5026-0.i686.tar.gz/download
