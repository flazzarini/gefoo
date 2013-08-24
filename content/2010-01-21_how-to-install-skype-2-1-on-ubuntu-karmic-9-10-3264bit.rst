How to get Skype 2.1 working with your webcam on Ubuntu Karmic 9.10 32/64bit
############################################################################
:date: 2010-01-21 00:56
:author: Frank Lazzarini
:category: Linux
:tags: linux, skype, ubuntu
:slug: how-to-install-skype-2-1-on-ubuntu-karmic-9-10-3264bit

So I recently tried to install skype on my new Ubuntu Installation as I
found out that skype wasn't available anymore in the `medibuntu`_
repositories for Karmic. So I installed the official deb package for
Ubuntu 8.04 from the official `skype website`_.
All just seemed to be working fine, but after a while I wanted to see
if my webcam was working as it should, which it didn't. When I went to
**Options** in Skype and wanted to test my Videodevice, all I got was
just a green snowy screen (see screenshot).

.. figure:: /static/images/2010-01-21_how-to-install-skype-2-1-on-ubuntu-karmic-9-10-3264bit.png
   :align: center
   :alt: Skype 2.1 Options

I was sure that my webcam was working after trying in out using, **
*gstreamer-properties***. So I googled a little bit around until I
found `this`_ post. As it seems although you've downloaded the skype
64bit version from the official skype website, that skype version wants
32bit *video4linux* libs. (Strange??? I know).

For a 64bit system we'll have to use *lib32v4l-0* so check if you have
them installed. Now all we need to do is point the library to a system
variable called *LD\_PRELOAD*. The simplest way to do this is to create
a small bash script in*/usr/bin/* which is called *skype.start*. Once
you've created the file don't forget making it executable with *chmod +x
/usr/bin/skype.start*.

**64 bit system**

.. code-block:: bash

    #!/bin/bash
    env LD\_PRELOAD=/usr/lib32/libv4l/v4l1compat.so /usr/bin/skype

**32 bit system**

.. code-block:: bash

    #!/bin/bash
    env LD\_PRELOAD=/usr/lib/libv4l/v4l1compat.so /usr/bin/skype

Now start skype using */usr/bin/skype.start* and you should end up with
your webcam working. Hope this was helpful.

.. _medibuntu: http://packages.medibuntu.org/karmic/index.html
.. _skype website: http://www.skype.com/intl/en/download/skype/linux/choose/
.. _this: http://ubuntuforums.org/archive/index.php/t-914952.html
