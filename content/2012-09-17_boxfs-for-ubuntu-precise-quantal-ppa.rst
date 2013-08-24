boxfs for Ubuntu Precise Quantal ppa
####################################
:date: 2012-09-17 09:46
:author: Frank Lazzarini
:category: Linux
:tags: linux, ubuntu
:slug: boxfs-for-ubuntu-precise-quantal-ppa

Do you have a `box.com`_ Account. For those who do not know
http://www.box.com, it is a cloud storage system just like
http://www.dropbox.com but it uses an open standard API called `OpenBox
API`_. Domenico Rotiroti wrote a fuse driver called `boxfs`_ to mount
your box.com account as a filesystem in Linux. Pretty awesome, if you
compare it to Dropbox where you only sync from one folder to your
Dropbox account. Well anyways over the past weekend I created a ppa
repository to install `boxfs`_ onto Ubuntu in three easy steps.

- First get **python-software-properties** (this will give you 
  add-apt-repository)

   ::

        sudo apt-get install python-software-properties

- Next register my ppa ppa:flazzarini/boxfs (hit ENTER when it asks
  you to)

   ::

        sudo add-apt-repository ppa:flazzarini/boxfs

- Do an update of your apt sources

   ::

        sudo apt-get update

- And finally install boxfs

   ::

        sudo apt-get install boxfs



You should have everything you need, to get going. To mount your
`box.com`_ account do the following.

::

     cd ~
     mkdir box.com
     boxfs -u YouUsername -p YourPassword box.com/

To unmount simply do

::

     umount ~/box.com/

For any bugs please report them to
`https://launchpad.net/~flazzarini/+archive/boxfs`_

.. _box.com: http://www.box.com
.. _OpenBox API: http://developers.box.com/
.. _boxfs: http://code.google.com/p/boxfs/
.. _`https://launchpad.net/~flazzarini/+archive/boxfs`: https://launchpad.net/~flazzarini/+archive/boxfs
