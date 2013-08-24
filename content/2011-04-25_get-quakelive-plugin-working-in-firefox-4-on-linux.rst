Get QuakeLive Plugin working in Firefox 4 on Linux
##################################################
:date: 2011-04-25 11:51
:author: Frank Lazzarini
:category: Linux
:tags: linux, games
:slug: get-quakelive-plugin-working-in-firefox-4-on-linux

For all of those out there who have problems getting the `QuakeLive`_
plugin to work with Firefox 4 in Linux here's a little how to on getting
it up and running. When you go to the page and you don't have the plugin
installed yet, the page tries to install it for you, but it will
complain about the version of Firefox 4 being incompatible with the
quakelive plugin. This is why we need to modify the plugin file a little
bit so our Firefox 4 will accept it.

Basically all you need to do is get the xpi file
*QuakeLivePlugin\_433.xpi* open it up with your Archive Manager and edit
the *install.rdf* file and add the following content to the file.

::
        quakeliveplugin@idsoftware.com
        1.0.433

            toolkit@mozilla.org
            1.9
            2.0.*

        QuakeLive.com Game Launcher
        Extension required for play on www.quakelive.com
        id Software, Inc.
        true

Once you've done that simply drag and drop the modded
*QuakeLivePlugin\_433.xpi* to Firefox 4 and it will ask you to confirm.


.. image:: /static/images/2011-04-25_get-quakelive-plugin-working-in-firefox-4-on-linux.png

If you are to lazy to modded the xpi your own, simply download my modded
version. I confirm that it's malware free etc. I am using the same one
so I wouldn't infect myself right! So there you go
`QuakeLivePlugin\_433.xpi`_.

Open up Firefox 4 again and you should be able to go to
`www.quakelive.com`_ without the site complaining.

If it's still not working try the following...
Once you've installed the plugin close down Firefox 4 and open up a
console. We'll need to copy the \*.so files from the plugin to
*~/.mozilla/plugins/*.

::

    root@box:~$ cd .mozilla/
    root@box:~$ mkdir plugins
    root@box:~$ cd plugins
    root@box:~$ cp ~/.mozilla/firefox/profileid/extensions/quakeliveplugin\@idsoftware.com/plugins/* .

Open up Firefox 4 again and you should be able to go to
`www.quakelive.com`_ without the site complaining.

If you should have trouble try ldd on the so files to see if you have
every needed dependencies installed.

::

    root@box:~$ cd .mozilla/plugins/
    root@box:~$ ldd *.so
    npquakelive.i386.so:                                                                                                
            linux-gate.so.1 =>  (0xf76f5000)                                                                            
            libX11.so.6 => /usr/lib32/libX11.so.6 (0xf73ed000)                                                          
            libXxf86dga.so.1 => /usr/lib32/libXxf86dga.so.1 (0xf73e7000)                                                
            libXxf86vm.so.1 => /usr/lib32/libXxf86vm.so.1 (0xf73e1000)                                                  
            libXext.so.6 => /usr/lib32/libXext.so.6 (0xf73d2000)                                                        
            libasound.so.2 => /usr/lib32/libasound.so.2 (0xf731d000)                                                    
            libdl.so.2 => /lib32/libdl.so.2 (0xf7319000)                                                                
            libz.so.1 => /lib32/libz.so.1 (0xf7306000)                                                                  
            libresolv.so.2 => /lib32/libresolv.so.2 (0xf72f1000)                                                        
            libpthread.so.0 => /lib32/libpthread.so.0 (0xf72d8000)                                                      
            libstdc++.so.6 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.4.5/32/libstdc++.so.6 (0xf71df000)                     
            libm.so.6 => /lib32/libm.so.6 (0xf71b9000)                                                                  
            libgcc_s.so.1 => /lib32/libgcc_s.so.1 (0xf719c000)                                                          
            libc.so.6 => /lib32/libc.so.6 (0xf7055000)                                                                  
            libxcb.so.1 => /usr/lib32/libxcb.so.1 (0xf703b000)                                                          
            libXau.so.6 => /usr/lib32/libXau.so.6 (0xf7037000)
            libXdmcp.so.6 => /usr/lib32/libXdmcp.so.6 (0xf7030000)
            librt.so.1 => /lib32/librt.so.1 (0xf7027000)
            /lib/ld-linux.so.2 (0xf76f6000)
    npquakelive.x64.so:
            linux-vdso.so.1 =>  (0x00007ffffebff000)
            libX11.so.6 => /usr/lib64/libX11.so.6 (0x00007f467ffe2000)
            libXxf86dga.so.1 => /usr/lib64/libXxf86dga.so.1 (0x00007f467fdda000)
            libXxf86vm.so.1 => /usr/lib64/libXxf86vm.so.1 (0x00007f467fbd2000)
            libXext.so.6 => /usr/lib64/libXext.so.6 (0x00007f467f9bd000)
            libasound.so.2 => /usr/lib64/libasound.so.2 (0x00007f467f6e6000)
            libdl.so.2 => /lib64/libdl.so.2 (0x00007f467f4e1000)
            libz.so.1 => /lib64/libz.so.1 (0x00007f467f2c9000)
            libresolv.so.2 => /lib64/libresolv.so.2 (0x00007f467f0b3000)
            libpthread.so.0 => /lib64/libpthread.so.0 (0x00007f467ee96000)
            libstdc++.so.6 => /usr/lib/gcc/x86_64-pc-linux-gnu/4.4.5/libstdc++.so.6 (0x00007f467eb83000)
            libm.so.6 => /lib64/libm.so.6 (0x00007f467e902000)
            libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007f467e6ea000)
            libc.so.6 => /lib64/libc.so.6 (0x00007f467e391000)
            libxcb.so.1 => /usr/lib64/libxcb.so.1 (0x00007f467e173000)
            librt.so.1 => /lib64/librt.so.1 (0x00007f467df69000)
            /lib64/ld-linux-x86-64.so.2 (0x00007f4680711000)
            libXau.so.6 => /usr/lib64/libXau.so.6 (0x00007f467dd65000)
            libXdmcp.so.6 => /usr/lib64/libXdmcp.so.6 (0x00007f467db5e000)

Hope this helped someone out there, keep on fraggin'. Credit goes out to
the whole `quakelive forum`_ and especially to the users
`LinuxFromRussia`_, `Diplodok`_ and so forth.

**Download `here`_.**

.. _QuakeLive: http://www.quakelive.com
.. _QuakeLivePlugin\_433.xpi: /static/uploads/2011/04/QuakeLivePlugin_433.xpi_.zip
.. _www.quakelive.com: http://www.quakelive.com
.. _quakelive forum: http://www.quakelive.com/forum/
.. _LinuxFromRussia: http://www.quakelive.com/forum/member.php?258863-LinuxFromRussia
.. _Diplodok: http://www.quakelive.com/forum/member.php?11195-Diplodok
.. _here: /static/uploads/2011/04/QuakeLivePlugin_433.xpi_.zip
