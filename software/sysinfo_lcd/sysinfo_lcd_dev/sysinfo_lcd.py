#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-2020 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Display basic system information.

Needs psutil (+ dependencies) installed::

  $ sudo apt-get install python-dev
  $ sudo -H pip install psutil
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime

if os.name != 'posix':
    sys.exit('{} platform not supported'.format(os.name))

from opts import get_device
from luma.core.render import canvas
from PIL import ImageFont

try:
    import psutil
except ImportError:
    print("The psutil library was not found. Run 'sudo -H pip install psutil' to install it.")
    sys.exit()


# TODO: custom font bitmaps for up/down arrows
# TODO: Load histogram


def bytes2human(n):
    """
    >>> bytes2human(10000)
    '9K'
    >>> bytes2human(100001221)
    '95M'
    """
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = int(float(n) / prefix[s])
            return '%s%s' % (value, s)
    return "%sB" % n


def cpu_usage():
    # load average, uptime
    uptime = datetime.now() - datetime.fromtimestamp(psutil.boot_time())
    av1, av2, av3 = os.getloadavg()
    return "Load:  %.1f  %.1f  %.1f" \
        % (av1, av2, av3)

def cpu_temps():
    # load average, uptime
    temps = [c.current for c in psutil.sensors_temperatures()['coretemp']][:4]
    av1, av2, av3 = os.getloadavg()
    return "Temp: " + " ".join(['{}'.format(t) for t in temps])


def mem_usage():
    usage = psutil.virtual_memory()
    return "RAM :  %.0f%%  [%s / %s]" \
        % ( usage.percent, bytes2human(usage.used), bytes2human(usage.total))


def disk_usage(dir, txt='SD'):
    usage = psutil.disk_usage(dir)
    #return "%s:%.0f%% [%s/%s] " \
    #    % (txt, usage.percent, bytes2human(usage.used), bytes2human(usage.total), )
    return "%s:  [%s / %s] " \
        % (txt, bytes2human(usage.used), bytes2human(usage.total), )


def network(iface):
    ip = 'DOWN'
    nic = psutil.net_if_stats()[iface]
    if nic.isup:
      ip = psutil.net_if_addrs()[iface][0].address
    return "%s: %s" % \
           (iface, ip,)


def stats(device, upd_flag):
    # use custom font
    font_path = str(Path(__file__).resolve().parent.joinpath('fonts', 'C&C Red Alert [INET].ttf'))
    font2 = ImageFont.truetype(font_path, 12)

    text_col = "#3F3F3F"
    hdr_col  = "white"
    with canvas(device) as draw:
        draw.rectangle((0, 0, 127, 13), outline=hdr_col)
        if upd_flag:
          draw.text((0, 1),  " CPU / RAM                *",     font=font2, fill=hdr_col)
        else:
          draw.text((0, 1),  " CPU / RAM",               font=font2, fill=hdr_col)

        draw.text((0, 14), cpu_usage(),                     font=font2, fill=text_col)
        draw.text((0, 26), cpu_temps(),                     font=font2, fill=text_col)
        draw.text((0, 38), mem_usage(),                     font=font2, fill=text_col)

        off1=5
        draw.rectangle((0, 50+off1, 127, 62+off1), outline=hdr_col)
        draw.text((0, 51+off1),  " Disks",                      font=font2, fill=hdr_col)
        draw.text((0, 63+off1), disk_usage('/',        '/           '), font=font2, fill=text_col)
        draw.text((0, 75+off1), disk_usage('/mnt/nas', '/mnt/nas'), font=font2, fill=text_col)

        off2=5
        draw.rectangle((0, 87+off1+off2, 127, 99+off1+off2), outline=hdr_col)
        draw.text((0, 88+off1+off2),  " Network",                      font=font2, fill=hdr_col)
        draw.text((0, 100+off1+off2), network('enp2s0'),              font=font2, fill=text_col)


def main():
    upd_flag = True
    while True:
        stats(device, upd_flag)
        time.sleep(2)
        upd_flag = not upd_flag


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
