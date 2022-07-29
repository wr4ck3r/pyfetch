#!/usr/bin/env python

import psutil

from modules import distro_decorations as dd

from datetime import timedelta
from datetime import datetime

from screeninfo import get_monitors

from time import sleep

from distro import LinuxDistribution

def format_info(parameter, value, colors):
    pcolor, vcolor, bold, fgreset, boldreset = (
        colors[0],
        colors[1],
        colors[2],
        colors[3],
        colors[4],
    )
    formatted_string = (
        f"{pcolor}{bold}{parameter}{fgreset} {boldreset}> {vcolor}{value}"
    )
    return formatted_string

def fetch_info():

    os_name = LinuxDistribution()._os_release_info["name"]
    os_id = LinuxDistribution().id()

    try:
        decor = dd.distros[os_id]
    except KeyError:
        decor = dd.distros["other"]
    dcolor = dd.colors
    dcolors = decor["colors"]

    uptime = timedelta(seconds=datetime.now().timestamp() - psutil.boot_time())

    monitors = get_monitors()
    if len(monitors) > 1:
        resolutions = ""
        for m in monitors():
            resolutions += f"{m.width}x{m.height} @ "
        resolutions = resolutions[:-3]
    else:
        resolutions = f"{monitors[0].width}x{monitors[0].height}   "

    parameters = {
        "CPU": f"{psutil.cpu_percent(0.1)}% [{psutil.cpu_count()}] {round(psutil.cpu_freq().max / 1000, 1)} GHz",
        "RAM": f"{round(psutil.virtual_memory().used / 8**10, 1)}G / {round(psutil.virtual_memory().total / 8**10, 1)}G ({round(psutil.virtual_memory().total / 8**10)}G)",
        "Resolution": resolutions[:-3],
        "Uptime": f"{round(uptime.seconds / 60**2, 1)} hr",
        "OS": os_name,
    }

    pcolor, vcolor, logo_color = (
        dcolors[0],
        dcolors[1],
        dcolors[2],
    )

    logo = (logo_color + decor["logo"] + dcolor["fr"]).split("\n")
    for param in parameters:
        specs = format_info(
            param,
            parameters[param],
            [pcolor, vcolor, dd.colors["eb"], dd.colors["fr"], dd.colors["rb"]],
        )
        for line in logo:
            logo[logo.index(line)] = line.replace(param, specs) + logo_color

    logo = "\n".join(logo)
    print(logo)

fetch_info()
