Migrate resources depending on ocf:pacemaker:ping RA with Pacemaker
###################################################################
:date: 2012-06-07 14:12
:author: Frank Lazzarini
:category: Linux
:tags: drbd, linux, pacemaker
:slug: migrate-resources-depending-on-ocfpacemakerping-ra-with-pacemaker

The job we want to accomplish is quite simple. Let's just say you have
two nodes **nodeA and nodeB** on two different locations which both have
a individual gateways. Now let's imagine the following scenario,
gatewayA goes down, and resulting in this there is no more internet
connectivity on **nodeA**, so ideally you would want the cluster to
switch to the node which still has internet connectivity. Using the
resource agent **ping** you can create such a rule in pacemaker.

There are 3 different resource agents to accomplish this tasks, but we
are going to use just one specific.

::

        ocf:heartbeat:pingd (Deprecated you shouldn't use this one anymore)
        ocf:pacemaker:pingd
    --> ocf:pacemaker:ping

Configure
^^^^^^^^^

First let's create the ping primitive in crm and create a clone of it,
so it runs on both nodes. We are going to ping ip addresses outside of
the network, so internet ip addresses. For each successful ping result
the p\_ping primitive will **score 1** point which is going to be
multiplied by 100. But we'll come back on scoring later on.

::

    # crm
    crm(live)# primitive p_ping ocf:pacemaker:ping params host_list="8.8.8.8 4.2.2.2" multiplier="100" dampen="5s" op monitor interval="60" timeout="60"  op start interval="0" timeout="60" op stop interval="0" timeout="60"
    crm(live)# clone c_ping p_ping
    crm(live)# commit

**host\_list** the ip addresses that are going to be pinged separated by
a space *e.g "x.x.x.x y.y.y.y"*

**multiplier** each successful ping will result in a score value of 1
which is then multiplied by the multiplier value, usually you should use
100 here.

If you look at the cluster now you should see something similar to this.

::

    Online: [ nodeB nodeA ]

     Master/Slave Set: ms_drbd [p_drbd]
         Masters: [ nodeB ]
         Slaves: [ nodeA ]
     Resource Group: g_cluster
         p_fs       (ocf::heartbeat:Filesystem):    Started nodeB
         p_ip       (ocf::heartbeat:IPaddr2):       Started nodeB
     Clone Set: c_ping [p_ping]
         Started: [ nodeB nodeA ]

Counting the scores
^^^^^^^^^^^^^^^^^^^

So we have the following scenario, **nodeA** and **nodeB** have the
**p\_ping** primitive and both can ping the ip addresses 8.8.8.8 4.2.2.2
so both nodes will get **1 score** per pingagble address which will
result in score **2 \* 100 so 200 score** for each node.

::

    nodeA (OK)  --> 2 * 100 = 200
    nodeB (OK)  --> 2 * 100 = 200

Now let's cut the internet connection on **nodeA** which will result in
the following scenario. **nodeA** can't ping any of the ip addresses
anymore so it will get a score of 0 which is multiplied by 100 which
will result in a score of **0**.

::

    nodeA (NOK) --> 0 * 100 = 0
    nodeB (OK)  --> 2 * 100 = 200

With these scores we can work to get the cluster to automatically
failover. Just add a simple location rule which will migrate a resource
over to another node. Here I use my group definition as a resource,
which consists of all the services I need to have started.

::

    # crm
    crm(live)# configure
    crm(live)# location groupwithping g_cluster rule -inf: not_defined pingd or pingd lte 0
    crm(live)# commit

To test this you can simply use iptables to block all the icmp traffic
on one of the nodes.

::

    iptables -A OUTPUT -p icmp -j DROP

To disable this iptables rule again simply do

::

    iptables -F

Prefer a NodeA
^^^^^^^^^^^^^^

You might want to have a setup where you would like to prefer **nodeA**
to have always all the resources if the network connectivity is ok,
there you need to give this node an extra score. This can also be done
with a location rule.

::

    # crm
    crm(live)# configure
    crm(live)# location prefernodeA resourceA rule 50: \#uname eq nodeA
    crm(live)# commit


