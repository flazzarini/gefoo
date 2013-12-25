Slim raspbian default Raspberry-pi Image
########################################
:date: 2012-12-26 10:56
:author: Frank Lazzarini
:category: Linux
:tags: linux, raspberrypi
:slug: slim-raspbian-image.rst


The 'default' Raspberry-Pi image `Raspbian` comes with a lot of overhead which
is mostly not wanted at least in my case. Here is a little aptitude line which
gets rid of all the stuff we don't want on our little embedded system like 
Xorg server, fonts, X Applications, LXDE and so forth.

  ::

    sudo apt-get remove --purge x11-common x11-utils x11-xkb-utils x11-xserver-utils \
      xarchiver xauth xkb-data xinit lightdm lightdm-gtk-greeter consolekit \
      libx{composite,cb,cursor,damage,dmcp,ext,font,ft,i,inerama,kbfile,klavier,mu,pm,randr,render,res,t,xf86}* \
      lxde* lx{input,menu-data,panel,polkit,randr,session,session-edit,shortcut,task,terminal} \
      obconf openbox gtk* libgtk* python-pygame python-tk python3-tk scratch tsconf omxplayer squeak-vm penguinspuzzle \
      mupdf netsurf-gtk menu-xdg
    sudo apt-get autoremove && sudo apt-get autoclean



.. _Raspbian: http://www.raspbian.org/
