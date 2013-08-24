Using your luxtrust token with Ubuntu 11.10
###########################################
:date: 2012-02-29 22:24
:author: Frank Lazzarini
:category: Linux
:tags: java, linux
:slug: using-your-luxtrust-token-with-ubuntu-11-10

.. image:: /static/images/2012-02-29_using-your-luxtrust-token-with-ubuntu-11-10.png

For those of you out there not living/working in Luxembourg a short
introduction. `Luxtrust`_ is a company based in Luxembourg selling
authenication tokens or cards to use in combination with your online
banking. The login they use is done via a Java Applet which is all fine
so far if `Luxtrust`_ wouldn't check the version of the Java plugin in
your browser and would accept openjdk icetea plugin which they don't.
But as Ubuntu doesn't include the original Sun/Oracle Java 6 or 7
anymore and we are told to switch to openjdk we are stuck. So this is
just a little tutorial showing you how you get online banking back on
track by installing Sun/Oracle Java 6 runtime and copying/linking the
javaplugin to the right place so your browser will recognize is and so
Luxtrust will recognize java running on your box. In this tutorial I
will only show you how this is done with `Firefox`_, but it should be
similar when you are using the `Chromium Browser`_.

Let's get started ....

Step 1 - Install third party repo for Java

We'll add a third party repository as of Ubuntu 11.10 sun-java6-jre is
not available anymore in the partner repositories, so we'll have to use
the following repository.

::

    sudo apt-get install python-software-properties
    sudo add-apt-repository ppa:ferramroberto/java
    sudo apt-get update
    sudo apt-get install sun-java6-jdk sun-java6-plugin

You may want to also add the following

::

    sudo update-alternatives --config java

If you get something like the following that means that you still have
openjdk installed, so you should select the newly installed java6-sun.
Select 2 here and press Enter.

::

    Selection    Path                                      Priority   Status
    ------------------------------------------------------------------------------
    * 0            /usr/lib/jvm/java-6-openjdk/jre/bin/java   1061      auto mode
      1            /usr/lib/jvm/java-6-openjdk/jre/bin/java   1061      manual mode
      2            /usr/lib/jvm/java-6-sun/jre/bin/java       63        manual mode

    Press enter to keep the current choice[*], or type selection number: 2

Step 2 - Link the plugin to firefox

Now lets create a link in the .mozilla directory in your home directory.

::

    mkdir ~/.mozilla/plugins/
    ln -s /usr/lib/jvm/java-6-sun/jre/lib/amd64/libnpjp2.so ~/.mozilla/plugins/libnpjp2.so

Restart Firefox. In Addons under Plugins you should see Java(TM) Plug-in
1.6.0\_26 beeing listed. To check if everything works as planed go to
the following site.

`https://secure.dexia-bil.lu/ssl/trust/lxtst\_checker.asp`_

.. _Luxtrust: https://www.luxtrust.lu/
.. _Firefox: http://www.mozilla.org/en-US/firefox/fx/
.. _Chromium Browser: http://www.chromium.org/
.. _`https://secure.dexia-bil.lu/ssl/trust/lxtst\_checker.asp`: https://secure.dexia-bil.lu/ssl/trust/lxtst_checker.asp
