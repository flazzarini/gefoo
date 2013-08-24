Run through folder add files with a certain extension to a list - Python Oneliner
#################################################################################
:date: 2012-03-26 23:23
:author: Frank Lazzarini
:category: Coding
:tags: python, coding
:slug: run-through-folder-add-files-with-a-certain-extension-to-a-list-python-oneliner

Here is great Python Oneliner I came across, to put a list of files
ending with a certain extension or name to a list, all this in just one
line...

.. code-block:: python

    import os

    list = []
    list += [each for each in os.listdir('path/to/files') if each.endswith('.jpg')]

