Multiple Firebird Servers on Ubuntu
###################################
:date: 2011-02-21 23:34
:author: Frank Lazzarini
:category: Linux
:tags: linux, firebird, ubuntu
:slug: multiple-firebird-servers-on-ubuntu

In this tutorial I will show you how to install multiple separate
Firebird 2.1 servers on a single Host, lets just say you are short on
budget and you want to have your testing/integration database running on
the same environment as your production database, which is usually not
preferable, but in some weird cases you find yourself needing such a
setup. Or for instance you have a number of production environments and
you want to have them a bit seperated from each other saying you want to
be able to kill all open sessions of a certain production environment,
sometimes this can be very useful but like I said usually you shouldn't
really do this. But anyways I was asked once to do exactly such a setup
and I wanted to share my knowledge on how to do exactly this with
Firebird 2.1, the same procedure should also be adaptable to other
versions of Firebird as long as you want to use Classic Server. Mixing
different version should also work cause the required libraries will all
be isolated in single directories.

When the setup is done you will have two separate Firebird 2.1
installations one which I will call **firebird01** and one which i will
call **firebird02** with two different fb\_inet\_server executables to
distinguish them further more, **fb\_inet\_server01** and
**fb\_inet\_server02**. **Firebird01** will listen on standard firebird
port **3050** and **firebird02** will listen on **3060**. Here a little
overview of what we want to accomplish.

+------------------+--------+-------------------+------------------------------------------+
| Name             | Port   | Directory         | Exectuable                               |
+==================+========+===================+==========================================+
| **Firebird01**   | 3050   | /opt/firebird01   | /opt/firebird01/bin/fb\_inet\_server01   |
+------------------+--------+-------------------+------------------------------------------+
| **Firebird02**   | 3060   | /opt/firebird02   | /opt/firebird02/bin/fb\_inet\_server02   |
+------------------+--------+-------------------+------------------------------------------+

Step 1 - Download / Install

Instead of using ubuntus repositories we are going to do a manual setup,
which gives us a bit more flexibility in terms of which versions we want
to use. To get started go to the `offical Firebird site`_ and download
the desired package, I chose `FirebirdCS-2.1.3.18185-0.i686.tar.gz`_.
Next we will need libstdc++5 in Ubuntu 10.10 Maverick they are available
through the standard repositories, so just use *apt-get*.

::

    root@host:/# apt-get install libstdc++5

Now let's extract the **FirebirdCS-2.1.3.18185-0.i686.tar.gz** package
which we've just downloaded. Inside this package you will find a file
called **buildroot.tar.gz**, this file holds all the files needed to get
the Firebird 2.1 server up and running. After extracting
**FirebirdCS-2.1.3.18185-0.i686.tar.gz** extract
**FirebirdCS-2.1.3.18185-0.i686/buildroot.tar.gz**, and finally copy the
**FirebirdCS-2.1.3.18185-0.i686/opt/firebird** over to
**/opt/firebird01**.

::

    root@host:/root# tar xzvf FirebirdCS-2.1.3.18185-0.i686.tar.gz 
    FirebirdCS-2.1.3.18185-0.i686/
    FirebirdCS-2.1.3.18185-0.i686/scripts/
    FirebirdCS-2.1.3.18185-0.i686/scripts/tarMainInstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/postuninstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/preinstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/preuninstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/taruninstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/postinstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/tarinstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/rpmfiles.txt
    FirebirdCS-2.1.3.18185-0.i686/scripts/tarMainUninstall.sh
    FirebirdCS-2.1.3.18185-0.i686/scripts/rpmheader.txt
    FirebirdCS-2.1.3.18185-0.i686/install.sh
    FirebirdCS-2.1.3.18185-0.i686/buildroot.tar.gz
    FirebirdCS-2.1.3.18185-0.i686/manifest.txt
    root@host:/root# cd FirebirdCS-2.1.3.18185-0.i686/
    root@host:/root/FirebirdCS-2.1.3.18185-0.i686# tar xzvf buildroot.tar.gz 
    ./
    ./opt/
    ./opt/firebird/
    ./opt/firebird/misc/
    ./opt/firebird/misc/upgrade/
    ./opt/firebird/misc/upgrade/ib_udf/
    ./opt/firebird/misc/upgrade/ib_udf/ib_udf_upgrade.sql
    ./opt/firebird/misc/upgrade/ib_udf/ib_udf2_params.txt
    ./opt/firebird/misc/upgrade/ib_udf/ib_udf_params.txt
    ./opt/firebird/misc/upgrade/metadata/
    ./opt/firebird/misc/upgrade/metadata/metadata_charset.txt
    ./opt/firebird/misc/upgrade/metadata/metadata_charset_drop.sql
    ./opt/firebird/misc/upgrade/metadata/metadata_charset_create.sql
    ./opt/firebird/misc/upgrade/security/
    ./opt/firebird/misc/upgrade/security/security_database.sql
    ./opt/firebird/misc/upgrade/security/security_database.txt
    ./opt/firebird/misc/intl.sql
    ./opt/firebird/misc/firebird.xinetd
    ./opt/firebird/UDF/
    ./opt/firebird/UDF/ib_udf.sql
    ./opt/firebird/UDF/ib_udf.so
    ./opt/firebird/UDF/fbudf.sql
    ./opt/firebird/UDF/ib_udf2.sql
    ./opt/firebird/UDF/fbudf.so
    ./opt/firebird/WhatsNew
    ./opt/firebird/aliases.conf
    ....... TOO MUCH OUTPUT .......
    root@host:/root/FirebirdCS-2.1.3.18185-0.i686# mkdir /opt/firebird01
    root@host:/root/FirebirdCS-2.1.3.18185-0.i686# cp -R opt/firebird/* /opt/firebird01/

Now you have your first firebird directory created, we can check if the
dependencies for lifbclient.so are met and so on therefore go into the
directory you've just created **/opt/firebird01/lib** and run **ldd**
against **libfbclient.so.2.1.3** if you get an output with no ouput
saying **not found** you are good.

::

    root@host:/opt/firebird01/lib# ldd libfbclient.so.2.1.3 
        linux-gate.so.1 =>  (0x00635000)
        libm.so.6 => /lib/libm.so.6 (0x00110000)
        libdl.so.2 => /lib/libdl.so.2 (0x006f9000)
        libncurses.so.5 => /lib/libncurses.so.5 (0x00a46000)
        libpthread.so.0 => /lib/libpthread.so.0 (0x00281000)
        libc.so.6 => /lib/libc.so.6 (0x0029b000)
        /lib/ld-linux.so.2 (0x00f59000)

We need to add a new user called firebird which we will use to run the
firebird server, to do so do the following.

::

    root@host:/# groupadd firebird
    root@host:/# useradd -d /opt/firebird01 -s /bin/false -c "Firebird Database Owner" -g firebird firebird

Step 2 - Setup first environment

Firebird needs to have a default password set for the **SYSDBA** user
which is basically the admin user of the Firebird Server. We have to set
this one up, therefore do the following.

::

    root@host:/opt/firebird01/lib# export FIREBIRD=/opt/firebird01/
    root@host:/opt/firebird01/lib# export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/firebird01/lib/
    root@host:/opt/firebird01/lib# cd ../bin
    root@xubuntu:/opt/firebird01/bin# ./gsec 
    GSEC> modify SYSDBA -pw masterkey
    Warning - maximum 8 significant bytes of password used
    GSEC> quit

Now as we have one working environment setup we just make a copy of it.

::

    root@host:/opt# cd /opt
    root@host:/opt# cp firebird01/ firebird02/ -R

Final but last modification in this step, changing the names of the
executables in both directories.

::

    root@host:/opt# mv firebird01/bin/fb_inet_server firebird01/bin/fb_inet_server01 
    root@host:/opt# mv firebird02/bin/fb_inet_server firebird02/bin/fb_inet_server02 

So let's move on to the next step, setting up **xinetd** to start the
right server depending on which port the server receives incoming
connections.

Step 3 - Xinetd

Now we have two seperate intallation of Firebird 2.1.3 Classic Server.
The next step will be to setup **xinetd** to associate different ports
with the different Firebird Servers.

Xinetd is a connection manager a so called **Super Internet Server**
which will launch a specified server only when a user is trying to
connect to a specified port. So let's say you have an ftp server set up
which should be listening on port 21. When a connection is being made to
the port 21, xinetd will be launching the service associated with the
port 21. In the following example it will be clear to you what will
happen.

Let's first create the firebird service entry. Therefore open up
**/etc/services**. Remove the following two lines

::

    gds_db          3050/tcp                        # InterBase server
    gds_db          3050/udp

Add these two lines to the end of the file.

::

    # Local services
    firebird01        3050/tcp                        # Firebird01 2.1
    firebird01        3050/udp
    firebird02        3060/tcp                        # Firebird02 2.1
    firebird02        3060/udp

Now we'll have to specify what xinetd should start when a connection
attempt is being made to port **3050** or **3060**. Therefore we'll have
to create two files **/etc/xinet.d/firebird01** and
**/etc/xinet.d/firebird2** which will hold the definitions for xinetd
for these services.

::

    service firebird01
    {
            flags                   = REUSE
            socket_type             = stream
            wait                    = no
            user                    = firebird
            server                  = /opt/firebird01/bin/fb_inet_server01
            env                     =FIREBIRD=/opt/firebird01
            env                    +=LD_LIBRARY_PATH=/opt/firebird01/lib:LD_LIBRARY_PATH
            disable                 = no
    }

::

    service firebird02
    {
            flags                   = REUSE
            socket_type             = stream
            wait                    = no
            user                    = firebird
            server                  = /opt/firebird02/bin/fb_inet_server02
            instances               = UNLIMITED
            env                     =FIREBIRD=/opt/firebird02
            env                    +=LD_LIBRARY_PATH=/opt/firebird02/lib:LD_LIBRARY_PATH
            disable                 = no
    }

Okey, so we have the services ports defined in **/etc/services** and
we've got two xinetd definitions in **/etc/xinetd.d/** so to see if you
have setup everything correctly for xinetd you can try to **restart**
xinetd and take a look at the log xinetd creates in
**/var/log/daemon.log**, if you see a line saying **2 available
services** you 've done good and you didn't do any mistakes in the
syntax.

::

    root@host:/# /etc/init.d/xinetd restart
     * Stopping internet superserver xinetd                                                 [ OK ]
     * Starting internet superserver xinetd                                                 [ OK ]
    root@host:/# tail -f /var/log/daemon.log
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing daytime
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing daytime
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing discard
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing discard
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing echo
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing echo
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing time
    Feb 18 19:28:49 xubuntu xinetd[19919]: removing time
    Feb 18 19:28:49 xubuntu xinetd[19919]: xinetd Version 2.3.14 started with libwrap loadavg options compiled in.
    Feb 18 19:28:49 xubuntu xinetd[19919]: Started working: 2 available services

The only one thing left now is the **firebird.conf** file where we need
to adjust which port firebird should listen on, so as you would have
guessed it we need to assign **3050** to **firebird01** 's config file
and **3060** to **firebird02** 's config file.

In **/opt/firebird01/firebird.conf** change

::

    # RemoteServicePort = 3050

 to

::

    RemoteServicePort = 3050


In **/opt/firebird02/firebird.conf** change

::

    # RemoteServicePort = 3050

 to

::

    RemoteServicePort = 3060

Alright that should it, you can try to connect to you two seperate
firebird servers using telnet, if you get something like the following
you are good, try to assign different databases in **aliases.conf** to
the different Firebird servers and try to connect either by using port
3050 or 3060.

::

    root@host:/# telnet localhost 3050
    Trying ::1...
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.``

    Connection closed by foreign host
    root@host:/# telnet localhost 3060
    Trying ::1...
    Trying 127.0.0.1...
    Connected to localhost.
    Escape character is '^]'.

    Connection closed by foreign host

All done and all working just fine. I hope this tutorial helps anybody
having to do the same setup I was asked to do, and I would be grateful
if you could comment on your experiences or if you have any sugguestions
or questions on this tutorial. *May the bird be with you!*

.. _offical Firebird site: http://www.firebirdsql.org/
.. _FirebirdCS-2.1.3.18185-0.i686.tar.gz: http://sourceforge.net/projects/firebird/files/firebird-linux-i386/2.1.3-Release/FirebirdCS-2.1.3.18185-0.i686.tar.gz/download
