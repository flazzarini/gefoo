Git visualization with gource
#############################
:date: 2012-05-06 23:01
:author: Frank Lazzarini
:category: Linux
:tags: coding, linux, git, svn
:slug: git-visualization-with-gource

Are you using git/svn/mercurial/bazaar as version control system and you
ever wanted to visualize your work, how the project developed over time
well `Gource`_ is there to visualize all this in a beautiful way. It
takes the history of your svn/git/mercurial/bazaar repository and
visualizes the changes over time, by whom they were done and so forth.

.. youtube:: ZV5DIbrOMzk
 :width: 800
 :height: 500
 :align: center


First we need to install gource if you are on Ubuntu/Debian do the following

::

    sudo apt-get install gource

Now run the following with path/to/project being your projects root
directory, and give gource the .git subfolder. Run it and you should see
the animation being presented.

::

    gource /path/to/project/.git/

Now to export this to an mpeg4 video do the following.

::

    gource /path/to/project/.git/ --stop-at-end --output-ppm-stream - | ffmpeg -y -b 6000k -r 60 -f image2pipe -vcodec ppm -i - -vcodec mpeg4 /tmp/gource.mp4

.. _Gource: http://code.google.com/p/gource/
