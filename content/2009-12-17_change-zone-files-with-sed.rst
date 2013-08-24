Change zone files with sed
##########################
:date: 2009-12-17 12:00
:author: Frank Lazzarini
:category: Linux
:tags: linux, dns, bash
:slug: change-zone-files-with-sed

As we had to move our server roma from root.lu to our home, and as roma
serves as dns server, we had to change IPs and serials in all the zone
files. Therefore we forged together some regular expressions to use with
**sed**. **sed** is a stream editor for unix, with this little army knife
you can search for string occurrences in change occurrences in files
really simple. Before you start please make sure that you have the
latest version of sed. At least >= **4.2.0**.

    sed (stream editor) is a Unix utility that (a) parses text files and
    (b) implements a programming language which can apply textual
    transformations to such files. It reads input files line by line
    (sequentially), applying the operation which has been specified via
    the command line (or a sed script), and then outputs the line. It
    was developed from 1973 to 1974 as a Unix utility by Lee E. McMahon
    of Bell Labs, and is available today for most operating systems.

The following is an zone file we'll change.

::

    @ IN SOA   ns1.domain.com. webdev.domain.com. (
            2006080101  ; serial
            8H      ; refresh
            2H      ; retry
            1W      ; expire
            4h)     ; minimum ttl

            NS  ns1.domain.com.
            NS  ns2.domain.com.
            MX 10   mail1.domain.com.
            MX 20   mail2.domain.com.

    domain.com.     A   192.168.0.1
    mail1           A   192.168.0.1
    mail2           A   192.168.0.2

    www         CNAME   domain.com.
    ftp         CNAME   www
    webmail         CNAME   www

First we'll change the serial to something new using the following
command. This searches and replaces the serial number with **2009121802
; serial**. The whitespaces are meant for keeping the format alike.

::

    sed -i 's/\s*[0-9]\{10\}\s*;\s*serial/                2009121802      ; serial/' *.zone

Changing minimum ttl (replace 4h or 8h to 1h)

::

    sed -i 's/[48]h)/1h)/g' *.zone

Now changing the Ip addresses is rather simple. This will replace
83.342.9.220 with 80.45.15.69.

::

    sed -i 's/192.168.0.1/80.45.15.69/' *.zone

That's it ....

**Useful links**

- `http://rubular.com/`_
- `http://sed.sourceforge.net/sed1line.txt`_

.. _`http://rubular.com/`: http://rubular.com/
.. _`http://sed.sourceforge.net/sed1line.txt`: %20http://sed.sourceforge.net/sed1line.txt
