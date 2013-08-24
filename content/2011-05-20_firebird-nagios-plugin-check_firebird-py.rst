Firebird Nagios plugin check_firebird.py
########################################
:date: 2011-05-20 16:41
:author: Frank Lazzarini
:category: Coding
:tags: linux, python, coding, firebird
:slug: firebird-nagios-plugin-check_firebird-py

At work we use a lot of Firebird databases, and so far our system admins
checked the availability of a Firebird Database by simply trying to
connect via telnet to the port 3050 and see if they would get a
response. With this kind of check you can't really determine if the
database is really up and running, let's just say for instance if in
your **aliases.conf** (the file in firebird which holds an alias which
then points to the database filename), you have an alias which points to
a database file that doesn't exist anymore, you would still get a
response from the Firebird Server via telnet but if you would try to
connect to the that specific database you would get an error. We 've
also tried `fbexport`_ which relies on a library called ipbb which we
couldn't get to compile. Therefore they asked me if I could write a
plugin for nagios which would do a real check to ensure that the
Databases are up and running, here is my result.

I chose to write the plugin in python, due it's simplicity, and because
I already wrote some script using the `python-kinterbasdb`_ extension.
The script requires a few parameters like **hostname**,
**databasealias**, **username**, **password** and optionally you can
specify a different **port**. For the actual check I simply do an SQL
Query onto the Database, which gives me a list of tables which hold
relations between each other. I thought this would be a good enough
check, but if you have a better idea let me know about it. Let's get to
actual source code, we are still testing the plugin, and I am going to
post it onto `http://exchange.nagios.org/`_.

::

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-  
    # Firebird Nagios plugin
    #
    # A plugin for Nagios which checks the firebird
    # connection to a specific host by connecting
    # to it and executing an SQL Statement which should
    # return all relations between the tables which
    # are in the database, be aware if you have an
    # empty database without any tables you will get
    # a critical error.
    #
    # Based on a template from
    # http://bsd.dischaos.com/2009/04/29/nagios-plugin-template-in-python/
    #
    # Requirements :
    #    python-kinterbasdb
    #
    # Example :
    #    check_firebird.py -h 192.168.1.1 -a employee -u sysdba -p masterkey -d 3050 
    __author__  = 'Frank Lazzarini'
    __contact__ = 'flazzarini at gmail.com'
    __version__ = '0.3.6'
    __license__ = 'GPLv3'

    try:
        import kinterbasdb
    except ImportError, _:
        pass

    import sys, getopt, socket


    nagios_codes = {'OK': 0, 'WARNING': 1, 'CRITICAL': 2, 'UNKNOWN': 3, 'DEPENDENT': 4}


    def usage():
        # Returns the nagios status UNKOWN with a usage description
        nagios_return('UNKNOWN', 'usage: {0} -h  -a  -u  -p  -d  -a " must be given as a parameter otherwise
        # the script will print the usage description using nagios_return()
        # function, else parse/verify the parameters
        if len(sys.argv) < 8:
            usage()

        try:
            opts , args = getopt.getopt(sys.argv[1:], 'h:a:u:p:d:', ['host=', 'pass=', 'alias=', 'user=', 'password=', 'destport='])
        except getopt.GetoptError, err:
            usage()

        # If destport is not given an argument assume 
        # default Firebird Port 3050
        if not ('-d', '--destport') in opts:
            destport = '3050'

        # Run through the opts and get the parameters
        for o, value in opts:
            if o in ('-h', '--host'):
                if not is_valid_ipv4_address(value): 
                    nagios_return('UNKNOWN', value + ' is not a valid ipv4 address.'.format(sys.argv[0]))
                else :
                    host = value
            elif o in ('-a', '--alias'):
                dbalias = value
            elif o in ('-u', '--user'):
                username = value
            elif o in ('-p', '--pass'):
                password = value
            elif o in ('-d', '--destport'):
                destport = value
            else:
                usage()

        result = check_condition(host, destport, dbalias, username, password)
        nagios_return(result['code'], result['message'])

    if __name__ == '__main__':
        main()

Download link : `check\_firebird.py-0.3.6.tar`_

If you happen to be on ubuntu simply apt-get **python-kinterbasdb** and
put the python script into **/usr/lib/nagios/plugins/** and make it
**executable**. After that you have to tell nagios that there is a new
command that nagios can use, therefore create a new file in
**/etc/nagios-plugins/config** call it **firebird.cfg** and put the
following in it.

::

    define command{
            command_name    check_firebird
            command_line    /usr/lib/nagios/plugins/check_firebird.py -h '$HOSTADDRESS$' -a '$ARG1$' -u '$ARG2$' -p '$ARG3$' -d '$ARG4$'
    }

After that you configure the Host plus its service in
**/etc/nagios3/conf.d/host.cfg**.

::

    define host {
            use    generic-host
            host_name    fb21
            alias    fb21
            address    10.90.91.21
            }


    define service {
            use    generic-service
            host_name    fb21
            service_description    FIREBIRD-test
            check_command    check_firebird!test!sysdba!masterkey  
            ;Optional you could put !3051 for a different port
            }

Hope this was helpful :)

.. _fbexport: http://fbexport.sourceforge.net/nagios.html
.. _python-kinterbasdb: http://kinterbasdb.sourceforge.net/
.. _`http://exchange.nagios.org/`: http://exchange.nagios.org/
.. _check\_firebird.py-0.3.6.tar: /static/uploads/2011/05/check_firebird.py-0.3.6.tar.gz
