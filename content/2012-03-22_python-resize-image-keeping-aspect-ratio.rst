Python resize image keeping aspect ratio
########################################
:date: 2012-03-22 00:01
:author: Frank Lazzarini
:category: Coding
:tags: coding, python
:slug: python-resize-image-keeping-aspect-ratio

This time I am posting just a little snippet which came in handy with
the latest web development I am doing. The problem was to resize an
uploaded image on the fly and creating an according thumbnail for that
image. For testing purposes I create a script that could be executed on
a number of files. So here it is

.. code-block:: python

    import os, sys, Image

    size = 150, 150

    for input in sys.argv[1:]:
        output = os.path.splitext(input)[0] + ".thumbnail"
        if input != output:
            try:
                im = Image.open(input)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(output, 'JPEG')
            except IOError:
                print "Could not create thumbnail for %s" % input

::

    python resize.py /path/to/files/*

Hope this helps anybody coming across the same problem. Quick and dirty
:)
