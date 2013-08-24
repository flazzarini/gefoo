Conky Amarok integration - Show current playing song
####################################################
:date: 2012-07-10 10:43
:author: Frank Lazzarini
:category: Coding
:tags: amarok, conky, linux, python
:slug: conky-amarok-integration-show-current-playing-song

Last weekend, I worked a little bit on a python script that connects via
dbus to Amarok_, and fetches information of the currently playing track.
It also has the feature to copy the cover art to a fix location so you
can use it in conky as a static image.

So for all of you guys out there using Conky_ and loving Amarok_, here is
the perfect combination of both.

For the source go to my `github`_ repository and look in tools for the
python script. You can also read the entire post for the source code.

.. code-block:: python

    #!/usr/bin/env python
    #-*- coding: utf-8 -*-
    #
    # anowplaying.py
    #
    #  Connects to dbus and retrieves
    #  information about the currently
    #  playing track in amarok.
    #

    import dbus, optparse, shutil

    class Nowplaying():
        def __init__(self):
            ''' Connect to dbus and retrieve the amarok dictionary containg
                all the information about the currently playing track 
            '''
            bus = dbus.SessionBus()
            amarok = bus.get_object('org.kde.amarok', '/Player')
            amarokdict = amarok.GetMetadata()

            self.artist = self.title = self.album = self.genre = self.year = \
            self.track = self.bitrate = self.sample = self.cover = ""

            if amarokdict :
                self.artist  = amarokdict['artist']
                self.title   = amarokdict['title']
                self.album   = amarokdict['album']
                self.genre   = amarokdict['genre']
                self.year    = amarokdict['year']
                self.track   = amarokdict['tracknumber']
                self.bitrate = amarokdict['audio-bitrate']
                self.sample  = amarokdict['audio-samplerate']
                self.cover   = amarokdict['arturl']

        def getArtist(self):
            return self.artist

        def getTitle(self):
            return self.title

        def getAlbum(self):
            return self.album

        def getGenre(self):
            return self.genre

        def getYear(self):
            return self.year

        def getTrack(self):
            return self.track

        def getBitrate(self):
            return self.bitrate

        def getSample(self):
            return self.sample

        def getCover(self, destination):
            ''' Copy amaroks cache cover art to a static location so it can be used in conky'''
            if self.cover != "" :
                try :
                    shutil.copyfile(self.cover.replace('file://', ''), destination)
                    return ""
                except Exception, e:
                    print e
                    return ""
            else :
                return ""

    if __name__ == '__main__':
        '''Set up the command line parser'''
        usage = 'usage: %prog [options]'
        parser = optparse.OptionParser(usage=usage)
        parser.add_option('-a',  '--artist',  action='store_true', help='artist name')
        parser.add_option('-t',  '--title',   action='store_true', help='title of the track')
        parser.add_option('-l',  '--album',   action='store_true', help='album name')
        parser.add_option('-g',  '--genre',   action='store_true', help='genre of the current track')
        parser.add_option('-y',  '--year',    action='store_true', help='year of the track')
        parser.add_option('-n',  '--track',   action='store_true', help='track number')
        parser.add_option('-b',  '--bitrate', action='store_true', help='bitrate of the track')
        parser.add_option('-s',  '--sample',  action='store_true', help='sample rate of the track')
        parser.add_option('-c',  '--cover',   metavar='filename',  help='copy cover art to destination file')

        '''Get the parser options passed to the program'''
        (opts, args) = parser.parse_args()
        now = Nowplaying()

        if opts.artist :
            print now.getArtist()
        if opts.title :
            print now.getTitle()
        if opts.album :
            print now.getAlbum()
        if opts.genre :
            print now.getGenre()
        if opts.year :
            print now.getYear()
        if opts.track :
            print now.getTrack()
        if opts.bitrate :
            print now.getBitrate()
        if opts.sample :
            print now.getSample()
        if opts.cover :
            print now.getCover(opts.cover)


.. image:: /static/images/2012-07-10_conky-amarok-integration-show-current-playing-song.png

.. _github: https://github.com/flazzarini/conkyconfig
.. _Amarok: http://amarok.kde.org/
.. _Conky: http://conky.sourceforge.net/
