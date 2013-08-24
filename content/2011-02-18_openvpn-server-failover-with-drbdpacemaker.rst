Openvpn Server Failover with Drbd, Heartbeat and Pacemaker
##########################################################
:date: 2011-02-18 22:47
:author: Frank Lazzarini
:category: Linux
:tags: linux, pacemaker, drbd, openvpn
:slug: openvpn-server-failover-with-drbdpacemaker

I recently needed to experiment with a setup of having a **highly
available Openvpn server**, as one of our clients asked for this. As
I've just got this working I thought I would share with the world how I
managed to get this setup working. I won't go into any details on how to
setup a basic cluster with drbd / pacemaker, there are many great
tutorials out there that already explain this, especially on the `wiki`_
of my hosting provider `Linode`_, but I am planing on writing a tutorial
aswell on how to setup a basic cluster with drbd / pacemaker / heartbeat
to provide filesystem failover and ip failover.

For now I will assume that you have a basic setup done, having drbd
being controlled by a master/slave resource in pacemaker and having a
primitive using **ocf:heartbeat:Filesystem** to get the Filesystem
mounted which is on the drbd device. So here a quick overview of what we
should have already.

- Hostnames : **box1** / **box2**
- eth0 IPs : **192.168.1.11** / **192.168.1.12**
- eth1 IPs : **10.8.0.1** / **10.8.0.2** (synchronization Link)
- Virtual IP : **192.168.1.10**
- Drbd Device : **/dev/drbd0**

Current output of *crm configure show*

::

    node $id="79aa42ba-fe71-4dd2-888b-aa26404018c1" box2 \
        attributes standby="off"
    node $id="bcada3ae-338e-4558-ab62-9cca5a312e19" box1 \
        attributes standby="on"
    primitive p_drbd ocf:linbit:drbd \
        params drbd_resource="r0" \
        op start interval="0" timeout="240" \
        op stop interval="0" timeout="100" \
        op monitor interval="10"
    primitive p_fs ocf:heartbeat:Filesystem \
        params device="/dev/drbd0" directory="/data" fstype="none" \
        op start interval="0" timeout="60" \
        op stop interval="0" timeout="60"
    primitive p_ip ocf:heartbeat:IPaddr2 \
        params ip="192.168.1.10" cidr_netmask="24" \
        op start interval="0" timeout="20" \
        op stop interval="0" timeout="20" \
        op monitor interval="10"
    group cluster p_ip p_fs \
        meta target-role="Started"
    ms msdrbd p_drbd \
        meta notify="true" target-role="Started"
    colocation cluster-with-drbdmaster inf: cluster msdrbd:Master
    order msdrbd-before-cluster inf: msdrbd:promote cluster:start
    property $id="cib-bootstrap-options" \
        dc-version="1.0.8-042548a451fce8400660f6031f4da6f0223dd5dd" \
        cluster-infrastructure="Heartbeat" \
        no-quorum-policy="ignore" \
        stonith-enabled="false" \
        last-lrm-refresh="1298028167" \
        stop-all-resources="false"

Step 1 - Installing Openvpn

Continue by basically installing **openvpn** on both hosts **box1** and
**box2**. No need to do any setups just yet, the only thing is you
should remove it from starting up at boot time, we don't want that, we
want our openvpn server beeing managed by pacemaker and not by a init
script.

::

    root@box1:/# apt-get install openvpn
    root@box1:/# update-rc.d -f openvpn remove``

::

    root@box2:/# apt-get install openvpn
    root@box2:/# update-rc.d -f openvpn remove``

Step 2 - Prepare the openvpn environment

Usually openvpn config files and keys are stored in **/etc/openvpn**, we
are going to use another path because we want the config files to be
shared on both hosts so that they are identical and as we have a shared
storage in place we should use it and put all of our config files and
keys onto that device. As you can see in my **crm configure show**
output that my **/dev/drbd0** device is to be mounted onto the directory
**/data/** this is just an example you are free to use whatever folder
you would like to use as long as it exists of course. You could even
just mount the drbd device to **/etc/openvpn**. Your choice...

Neither the less we are going to copy the needed files for openvpn to
create server / client keys into this directory, my choice beeing
**/data/openvpn/**, therefore let's create the directory and put the
**easy-rsa** directory from openvpn into this new folder. I am doing all
this on box1 because the drbd device was mounted on box1 this may be
different for you.

::

    root@box1:/# mkdir -p /data/openvpn/easy-rsa/
    root@box1:/# cp -R /usr/share/doc/openvpn/examples/easy-rsa/2.0/* /data/openvpn/easy-rsa/``

Now let's go ahead and edit **/data/openvpn/easy-rsa/vars**.

::

    root@box1:/# sudo vi /data/openvpn/easy-rsa/vars``

Change these lines at the bottom so that they reflect your new CA.

::

    export KEY_COUNTRY="LU"
    export KEY_PROVINCE="NA"
    export KEY_CITY="Luxembourg"
    export KEY_ORG="company.com"
    export KEY_EMAIL="admin@company.com"``

Step 3 - Create Certificates and server config

Now let's create the CA certificate and the server certificates.

::

    root@box1:/# cd /data/openvpn/easy-rsa/
    root@box1:/# sudo chown -R root:admin .
    root@box1:/# sudo chmod g+w .
    root@box1:/# source ./vars
    root@box1:/# ./clean-all
    root@box1:/# ./build-dh
    root@box1:/# ./pkitool --initca
    root@box1:/# ./pkitool --server server
    root@box1:/# cd keys
    root@box1:/# openvpn --genkey --secret ta.key
    root@box1:/# sudo cp server.crt server.key ca.crt dh1024.pem ta.key ../../``

Good now let's move on to creating the server configuration file.
**Remember** to put the **virtual Ip address** as the local ip.

::

    root@box1:/# cd /data/openvpn/
    root@box1:/# vi server.conf``

::

    mode server
    tls-server

    local 192.168.1.10
    port 1194
    proto udp

    dev tun

    persist-key
    persist-tun

    #certificates and encryption
    ca ca.crt
    cert server.crt
    key server.key  # This file should be kept secret
    dh dh1024.pem
    tls-auth ta.key 0 # This file is secret

    cipher BF-CBC        # Blowfish (default)
    comp-lzo

    #DHCP Information
    server      10.9.0.0 255.255.255.0
    max-clients 10

    #log and security
    user nobody
    group nogroup
    keepalive 10 120
    status openvpn-status.log
    verb 3

Alright now we have everything we need to get to the next part creating
the pacemaker rule.

Step 4 - Create Pacemaker rules

Open up the crm shell and create a new primitive which is called
**p\_openvpn** which uses the **ocf:heartbeat:anything** resource agent
and calls **/usr/sbin/openvpn** with the following command line options
: **--daemon --writepid /var/run/openvpn.pid --config
/data/openvpn/server.conf --cd /data/openvpn**

`` root@box1:/# crm crm(live)# configure crm(live)configure# show p_openvpn crm(live)configure# primitive p_openvpn ocf:heartbeat:anything  params binfile="/usr/sbin/openvpn" cmdline_options="--writepid /var/run/openvpn.pid --config /data/openvpn/server.conf --cd /data/openvpn --daemon" pidfile="/var/run/openvpn.pid" op start timeout="20" op stop timeout="30" op monitor interval="20" crm(live)configure# edit cluster   # add p_openvpn to the cluster group p_ip p_fs p_openvpn crm(live)configure# commit crm(live)configure# quit``

So you end up with this...

::

    node $id="79aa42ba-fe71-4dd2-888b-aa26404018c1" box2 \
            attributes standby="off"
    node $id="bcada3ae-338e-4558-ab62-9cca5a312e19" box1 \
            attributes standby="on"
    primitive p_drbd ocf:linbit:drbd \
            params drbd_resource="r0" \
            op start interval="0" timeout="240" \
            op stop interval="0" timeout="100" \
            op monitor interval="10"
    primitive p_fs ocf:heartbeat:Filesystem \
            params device="/dev/drbd0" directory="/data" fstype="none" \
            op start interval="0" timeout="60" \
            op stop interval="0" timeout="60"
    primitive p_ip ocf:heartbeat:IPaddr2 \
            params ip="192.168.1.10" cidr_netmask="24" \
            op start interval="0" timeout="20" \
            op stop interval="0" timeout="20" \
            op monitor interval="10"
    primitive p_nfs lsb:nfs-kernel-server \
            op monitor interval="5s" \
            meta target-role="Started"
    primitive p_openvpn ocf:heartbeat:anything \
            params binfile="/usr/sbin/openvpn" cmdline_options="--daemon --writepid /var/run/openvpn.pid --config /data/openvpn/server.conf --cd /data/openvpn" pidfile="/var/run/openvpn.pid" \
            op start timeout="20" \
            op stop timeout="30" \
            op monitor interval="20" \
            meta target-role="Started"
    group cluster p_ip p_fs p_nfs p_openvpn \
            meta target-role="Started"
    ms msdrbd p_drbd \
            meta notify="true" target-role="Started"
    colocation cluster-with-drbdmaster inf: cluster msdrbd:Master
    order msdrbd-before-cluster inf: msdrbd:promote cluster:start
    property $id="cib-bootstrap-options" \
            dc-version="1.0.8-042548a451fce8400660f6031f4da6f0223dd5dd" \
            cluster-infrastructure="Heartbeat" \
            no-quorum-policy="ignore" \
            stonith-enabled="false" \
            last-lrm-refresh="1298028167" \
            stop-all-resources="false"

crm\_mon output

::

    ============
    Last updated: Fri Feb 18 22:42:53 2011
    Stack: Heartbeat
    Current DC: box1 (bcada3ae-338e-4558-ab62-9cca5a312e19) - partition with quorum
    Version: 1.0.8-042548a451fce8400660f6031f4da6f0223dd5dd
    2 Nodes configured, unknown expected votes
    2 Resources configured.
    ============

    Online: [ box1 box2 ]

     Master/Slave Set: msdrbd
         Masters: [ box1 ]
         Slaves: [ box2 ]
     Resource Group: cluster
         p_ip       (ocf::heartbeat:IPaddr2):       Started box1
         p_fs       (ocf::heartbeat:Filesystem):    Started box1
         p_openvpn  (ocf::heartbeat:anything):      Started box1

And we are done, you have an openvpn server in failover. Now if you want
to create client keys, you have to create them always on the host which
is currently active and holds the drbd mount. That's about it, wasn't
that hard now was it. I hope my little tutorial helped you in achieving
your goal. If you have any questions or suggestions please feel free to
comment.

.. _wiki: http://library.linode.com/linux-ha/ip-failover-heartbeat-pacemaker-drbd-mysql-ubuntu-10.04
.. _Linode: http://www.linode.com
