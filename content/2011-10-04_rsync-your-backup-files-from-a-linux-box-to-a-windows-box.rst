Rsync your backup files from a Linux box to a Windows box using cwrsync
#######################################################################
:date: 2011-10-04 11:31
:author: Frank Lazzarini
:category: Windows
:tags: windows, backup, rsync
:slug: rsync-your-backup-files-from-a-linux-box-to-a-windows-box

Have you ever had the need to do an **rsync** from a Linux box to a
Windows machine and googled around, tried it with cygwin, but you didn't
want to install the whole cygwin environment. Well I have a solution
just for you. The guys from `ITeF!x`_ put together a perfect packages,
containing all the cygwin dependencies in a single easy to install
package for Windows called **cwrsync**.

In our tutorial setup we will have a Windows Box with IP x.x.x.x which
isn't important, and a Linux Box with the Ip address 192.168.1.2.

Step 1 - Download / Install

Go to `http://www.itefix.no/i2/cwrsync`_ and download cwrsync Installer
from the sourceforge mirror (we are not going to use the cwrsync
server).
Install it using the default locations.

Step 2 - Create certificates

Next we will have to create server certificates on the Windows Box,
therefore open up a command line and do the following. In this example I
am logged in as Administrator.

::

    cd c:\Users\Administrator
    mkdir .ssh
    cd .ssh
    "C:\Program Files\cwRsync\bin\ssh-keygen.exe" -t rsa -N "" -f id_rsa

Now copy the created **id\_rsa.pub** to your Linux Box to **/root/**.
Connect to your linux box and add the public key of the Windows Box to
the **autorized\_keys** file. Therefor do the following.

::

    root@linuxbox:~$ cat id_rsa.pub >> /root/.ssh/authorized_keys

Step 3 - Execute the batch file for the first time

Here I provide you with a simple batch file, for starting cwrsync the
first time, and sync data from your Linux Box to the Windows Box.

::

    @ECHO OFF
    REM *****************************************************************
    REM
    REM Backup cwrsync script
    REM
    REM *****************************************************************

    REM Make environment variable changes local to this batch file
    SETLOCAL

    REM ** CUSTOMIZE ** Specify where to find rsync and related files (C:\CWRSYNC)
    SET CWRSYNCHOME=%PROGRAMFILES%\CWRSYNC

    REM Set HOME variable to your windows home directory. That makes sure 
    REM that ssh command creates known_hosts in a directory you have access.
    SET HOME=c:\Users\Administrator\

    REM Make cwRsync home as a part of system PATH to find required DLLs
    SET CWOLDPATH=%PATH%
    SET PATH=%CWRSYNCHOME%\BIN;%PATH%

    rsync -trzv -p --chmod=ugo=rwX root@192.168.1.2:/data/* /cygdrive/c/BackupData/
    Pause

Useful Links

- http://rsync.net/resources/howto/windows\_rsync.html
- http://www.itefix.no/i2/index.php
- http://sourceforge.net/projects/sereds/files/

Download `cwRsync\_4.2.0\_Installer`_

.. _ITeF!x: http://www.itefix.no/i2/
.. _`http://www.itefix.no/i2/cwrsync`: http://www.itefix.no/i2/cwrsync
.. _cwRsync\_4.2.0\_Installer: /static/uploads/cwRsync_4.2.0_Installer.zip
