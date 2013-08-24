Rename white spaces in folders to dots
######################################
:date: 2011-03-15 12:04
:author: Frank Lazzarini
:category: Linux
:tags: coding, bash, linux
:slug: rename-white-spaces-in-folders-to-dots

Don't you just hate when you get a copy of a scene release from
somewhere and the guy that gave it to you "descened" the release folder,
i.e out of **Something.other.than.Potato.HDTV.XviD** became **Something
other than Potato HDTV XviD**. So how to fix this, in linux it's quite
easy to do it by just using a little bash magic. Here is how.

Just create a new file called **fixfolders.sh** and add the following to
the file and finally make it executable.

.. code-block:: bash

    #!/bin/bash

    for i in *; do
        mv "$i" $(echo "$i" | tr " " ".")
    done

Now **cd** into the directory which contains folders with spaces in it
and run the script here.

That's it for today folks :) hope you liked it.
