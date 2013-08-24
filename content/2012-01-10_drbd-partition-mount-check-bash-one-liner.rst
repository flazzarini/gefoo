Drbd partition mount check bash one liner
#########################################
:date: 2012-01-10 10:11
:author: Frank Lazzarini
:category: Linux
:tags: linux, bash, crontab, drbd
:slug: drbd-partition-mount-check-bash-one-liner

This is just a quick tip for you out there that use `DRBD`_ in simple
Primary/Secondary mode and need to check whether a script is executed on
the node which is currently Primary and has the Drbd Filesystem mounted.
Let's just say you need to copy stuff onto your Drbd partition via a
cron script. You can use the following one liner which is checking on
the device '''/dev/drbd0''' which you probably need to adept to your
needs and will print a message to standard output if this is the node
which is holding the resources. Just replace that message output with
the command you would like to execute and you are good to go.

.. code-block:: bash

    if [ "`mount | grep /dev/drbd0 | wc -l`" == "1" ]; then echo "We are holding the resources"; fi

.. _DRBD: http://www.drbd.org/
