Get QuakeLive Plugin working in Firefox 5 on Linux
##################################################
:date: 2011-06-30 15:57
:author: Frank Lazzarini
:category: Linux
:tags: linux, games
:slug: get-quakelive-plugin-working-in-firefox-5-on-linux

As `Firefox 5`_ got released for linux, and as most of you already
switched to it I wanted to update my `earlier post`_ about getting the
`QuakeLive`_ Plugin to work on `Firefox 4`_ . Not much changed, basically
all you need to do is changed the **maxVersion** in the **install.rdf**
to **5.0.\***. So you would have the following.

Thanks to Pliskin who commented already on `this`_.

::

        quakeliveplugin@idsoftware.com
        1.0.433

            toolkit@mozilla.org
            1.9
            5.0.*

        QuakeLive.com Game Launcher
        Extension required for play on www.quakelive.com
        id Software, Inc.
        true

That's already everything you need to change to get `QuakeLive`_ to work
with `Firefox 5`_. But if you feel lazy go ahead and download my
prepared `QuakeLivePlugin\_433.xpi`_.


.. _Firefox 5: http://www.mozilla.com/en-US/firefox/fx/
.. _earlier post: http://www.gefoo.org/generalfoo/?p=179
.. _QuakeLive: http://www.quakelive.com
.. _Firefox 4: http://www.mozilla.com/en-US/firefox/fx/
.. _this: http://www.gefoo.org/generalfoo/?p=179
.. _QuakeLivePlugin\_433.xpi: /static/uploads/QuakeLivePlugin_433-FF5.tar.gz
