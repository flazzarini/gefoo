Simple Conky configuration PlainConky
#####################################
:date: 2012-01-31 11:07
:author: Frank Lazzarini
:category: Linux
:tags: linux, conky
:slug: simple-conky-configuration-plainconky

.. image:: /static/images/2012-01-31_simple-conky-configuration-plainconky.png

Hey you all out there, today I want to show off my very simple but nice
conky setup that I use on my Laptop. The layout is fairly small to match
the resolution of my laptop's monitor. The configuration uses only conky
functions and uses the fonts *Terminus* and *AvantGardeLTMedium*. For
those that don't know what conky is head over to the `conky website`_ or
check out these awesome configurations `here`_ or `there`_. But if you
want to have a simple setup something to start off with I suggest you
start using mine and adjust it to your liking.

It features visualizing things such as CPU Usage, Temperature, Memory
Usage, current ip address depending on which device is up, if wlan is up
information on that device is shown, if eth0 is up that information is
shown, Disk Usage, and General Date/Time information.

**plainconky.conf**

::

    use_xft yes
    xftfont Terminus:size=8
    xftalpha 0.8
    update_interval 1.0
    total_run_times 0
    own_window yes
    own_window_transparent yes
    own_window_argb_visual yes
    own_window_type normal
    own_window_class conky-semi
    own_window_hints undecorated,below,sticky,skip_taskbar,skip_pager
    background no
    double_buffer yes
    minimum_size 300 200
    draw_shades no
    draw_outline no
    draw_borders no
    draw_graph_borders yes
    default_shade_color black
    default_outline_color white
    default_bar_size 150 5
    default_gauge_size 20 20
    imlib_cache_size 0
    draw_shades no
    alignment top_right
    gap_x 5
    gap_y 35
    no_buffers yes
    uppercase no
    cpu_avg_samples 2
    override_utf8_locale no
    default_color ECEAE4
    color1 9f907d
    color2 01C400



    TEXT
    ${font AvantGardeLTMedium:bold:size=10}${color Tan1}Info ${color slate grey}${hr 2}${font}
    ${color1}Date                   ${alignr}${color slate grey}${time %a,}${color}${time %e %B %G}
    ${color1}Time           ${alignr}${color}${time %T}

    ${font AvantGardeLTMedium:bold:size=10}${color Tan1}System ${color slate grey}${hr 2}${font}
    ${color1}Hostname       ${alignr}${color}${nodename}
    ${color1}${sysname}     ${alignr}${color}${kernel}-${machine}
    ${color1}CPU            ${alignr}${color}${freq_g}GHz
    ${color1}Loadaverage        ${alignr}${color}${loadavg 1} ${loadavg 2} ${loadavg 3}
    ${color1}Uptime         ${alignr}${color}${uptime}
    ${color1}Battery Status     ${alignr}${color}${battery_short BAT1}
    ${color1}Cpu Temperature    ${alignr}${color}${acpitemp}C
    ${color1}Hdd Temperature    ${alignr}${color}${hddtemp /dev/sda}C

    ${font AvantGardeLTMedium:bold:size=10}${color Tan1}Processors ${color slate grey}${hr 2}${font}
    ${color1}Core 1     ${alignr}${color}${cpu cpu1}%  ${cpubar cpu1}
    ${color1}Core 2     ${alignr}${color}${cpu cpu2}%  ${cpubar cpu2}

    ${font AvantGardeLTMedium:bold:size=10}${color Tan1}Memory ${color slate grey}${hr 2}${font}
    ${color1}Memory     ${color}${alignr}${memeasyfree} / ${memmax}
    ${color1}Currently  ${color}${alignr}${memperc}%   ${membar}

    ${font AvantGardeLTMedium:bold:size=10}${color Tan1}Filesystem ${color slate grey}${hr 2}${font}
    ${color1}/      ${color}${alignc}${fs_used /} / ${fs_size /} ${color}${alignr}${fs_free_perc /} %
    ${color}${fs_bar 5,300 /}

    ${font AvantGardeLTMedium:bold:size=10}${color Tan1}Networking ${color slate grey}${hr 2}${font}
    ${if_existing /proc/net/route wlan0}${color1}Ip     ${color}${alignr}${addr wlan0}
    ${color1}AP     ${color}${alignr}${wireless_essid wlan0}
    ${color1}Signal     ${color}${alignr}${wireless_link_qual_perc wlan0}${wireless_link_bar 10,100 wlan0}
    ${color1}Download   ${alignr}${color}${downspeed wlan0}${downspeedgraph wlan0 10,100}
    ${color1}Upload     ${alignr}${color}${upspeed wlan0}${upspeedgraph wlan0 10,100}
    ${color1}Total Down/Up  ${alignr}${color}${totaldown wlan0}${color1}/${color}${totalup wlan0}
    ${else}${if_existing /proc/net/route eth0}${color1}Ip       ${color}${alignr}${addr eth0}
    ${color1}Download   ${alignr}${color}${downspeed eth0}${downspeedgraph eth0 10,100}
    ${color1}Upload     ${alignr}${color}${upspeed eth0}${upspeedgraph eth0 10,100}
    ${color1}Total Down/Up  ${alignr}${color}${totaldown eth0}${color1}/${color}${totalup eth0}${endif}${endif}

    ${font AvantGardeLTMedium:bold:size=10}${color Tan1}Top Processes ${color slate grey}${hr 2}${font}
    ${color1}${top name 1}  ${alignr}${color}${top cpu 1} ${top mem 1}
    ${color1}${top name 2}  ${alignr}${color}${top cpu 2} ${top mem 2}
    ${color1}${top name 3}  ${alignr}${color}${top cpu 3} ${top mem 3}
    ${color1}${top name 4}  ${alignr}${color}${top cpu 4} ${top mem 4}
    ${color1}${top name 5}  ${alignr}${color}${top cpu 5} ${top mem 5}

.. _conky website: http://conky.sourceforge.net/
.. _here: http://www.techdrivein.com/2011/02/6-awesome-conky-configs-that-just-works.html
.. _there: http://desktopspotting.com/26/best-conky-configs-for-linux-desktop/
