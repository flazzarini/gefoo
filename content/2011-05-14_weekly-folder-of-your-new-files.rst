Weekly folder of your new files
###############################
:date: 2011-05-14 10:05
:author: Frank Lazzarini
:category: Linux
:tags: linux, crontab, bash
:slug: weekly-folder-of-your-new-files

Do you know the problem, you have a massive directory with tons of media
data, and after work you want to watch the latest episode of your
favorite show, and you jump into that directory knowing that there is a
new episode, but that directory is cramped up with so many files, that
you can't find what you are looking for. Well I found an easy way around
that by creating a folder called **week** which holds links to the
actual files which were added a week ago. So in terms of commands, I use
**find** to find all the files that are not older than a week and **ln**
to create the links to these files. I created a little bash script which
does just that. It should be flexible enough for everyones needs.

.. code-block:: bash

    #!/bin/bash

    DIRS="/download/TV /download/Movies"
    WEEKDIR="/download/week/"
    DAYS="6"

    find=`which find`
    ln=`which ln`

    # Check if working directories exist
    for dir in $DIRS ; do
            if [ ! -d "$dir" ]; then echo "Source Directory $dir doesn't exist." && exit 1;fi
    done

    if [ ! -d "$WEEKDIR" ]; then echo "Weekly directory doesn't exist" && exit 1; fi

    # Create lists and links white spaces trick ${DIRS[@]}
    for dir in "${DIRS[@]}"; do
            find $dir/* -type d -ctime -$DAYS | while read item ; do
                    $ln -s "$item" $WEEKDIR
            done
    done

    # Delete old links
    find $WEEKDIR/* -type l -ctime $DAYS -exec rm '{}' \;

Now just execute this script from **cron.daily** and you are good to go.
