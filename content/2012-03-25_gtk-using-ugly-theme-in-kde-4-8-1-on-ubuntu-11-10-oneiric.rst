Gtk using ugly theme in KDE 4.8.1 on Ubuntu 11.10 Oneiric
#########################################################
:date: 2012-03-25 22:04
:author: Frank Lazzarini
:category: Linux
:tags: kde, linux, ubuntu
:slug: gtk-using-ugly-theme-in-kde-4-8-1-on-ubuntu-11-10-oneiric

.. image:: /static/images/2012-03-25_gtk-using-ugly-theme-in-kde-4-8-1-on-ubuntu-11-10-oneiric_1.png

I lately updated my laptop with the latest packages and I've got KDE
4.8.1 from the ppa. To my surprise all the gtk apps that I have
installed look terrible, with the standard GTK look, apps like
firefox/pidgin and so on. The default theme look was change from oxygen
to clearlooks, which is the default in GTK2. I knew there was a little
app called **gtk-theme-switch2** to change the default look of gtk,
which you have to install. So a simple apt-get install got me the thing
and I changed the gtk theme to the **gtk oxygen theme** which looks just
about awesome on Kde! If you experiencing the same thing, here is how
you fix it.

::

    sudo apt-get install gtk-theme-switch gtk2-engines-oxygen

Then start the it up and select **oxygen-gtk** and **voila**!

.. image:: /static/images/2012-03-25_gtk-using-ugly-theme-in-kde-4-8-1-on-ubuntu-11-10-oneiric_2.png
