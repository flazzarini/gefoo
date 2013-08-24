Install Firebird 2.5 onto Ubuntu 10.04 via PPA
##############################################
:date: 2012-04-27 09:44
:author: Frank Lazzarini
:category: Linux
:tags: firebird, linux, ubuntu
:slug: install-firebird-2-5-onto-ubuntu-10-04-via-ppa

As of Ubuntu 12.04 Firebird 2.5 packages are included in the official
repositories, but here I am focusing on installing Firebird 2.5 on older
installations with Ubuntu 10.04 LTS. So you want to install Firebird 2.5
onto Ubuntu 10.04 without the need to install everything by hand, you
can go ahead and use a ppa which has Firebird 2.5 packages. But there
seems to be a problem with the gpg keys so a simple *sudo
add-apt-repository ppa:mapopa* like it is stated on the official `Ubuntu
Documentation`_ doesn't work. So here is what did the trick for me.

`Mariuz's PPA`_

First we'll have to import the key from Mariuz's PPA by hand.

::

    sudo gpg --ignore-time-conflict --no-options --no-default-keyring --secret-keyring /etc/apt/secring.gpg --trustdb-name /etc/apt/trustdb.gpg --keyring /etc/apt/trusted.gpg --primary-keyring /etc/apt/trusted.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv 0BE6D09EEF648708

Once we did that add the next two values to your
**/etc/apt/sources.list**

::

    deb http://ppa.launchpad.net/mapopa/ppa/ubuntu lucid main 
    deb-src http://ppa.launchpad.net/mapopa/ppa/ubuntu lucid main 

After that you're done .. do a **apt-get update** and a **apt-cache
search firebird** and you should see the following packages in your
results.

::

    firebird2.5-classic - Firebird Classic Server - an RDBMS based on InterBase 6.0 code
    firebird2.5-classic-common - common files for firebird 2.5 "classic" and "superclassic" servers
    firebird2.5-classic-dbg - collected debug symbols for firebird2.5-classic and -superclassic
    firebird2.5-common - common files for firebird 2.5 servers and clients
    firebird2.5-server-common - common files for firebird 2.5 servers
    firebird2.5-super - Firebird Super Server - an RDBMS based on InterBase 6.0 code
    firebird2.5-super-dbg - collected debug symbols for firebird2.5-super
    firebird2.5-superclassic - Firebird SupecClassic Server - an RDBMS based on InterBase 6.0 code

.. _Ubuntu Documentation: https://help.ubuntu.com/community/Firebird2.5
.. _Mariuz's PPA: https://launchpad.net/~mapopa/+archive/ppa
