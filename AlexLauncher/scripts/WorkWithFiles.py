import os
import sys
import subprocess as subproc
import minecraft_launcher_lib as ml
import psutil
import textwrap
import jdk
import platform
import requests as rq
import customtkinter as ctk
from WorkWithText import *

from AlexLauncher.data.constants import dataDirectory

def download(url, dir, name):
    filepath = os.path.join(dir, name)
    try:
        response = rq.get(url)
        response.raise_for_status()
        with open(filepath, "wb") as dw:
            dw.write(response.content)
    except rq.exceptions.RequestException as e:
        return "Error"


def jdklist():
    return open(dataDirectory + r"\jdklist", "r").readlines(30000)
def serverlist():
    return open(dataDirectory + r"\serverlist", "r").readlines(30000)
def writejdklist():
    return open(dataDirectory + r"\jdklist.txt", "a")
def writeserverlist():
    return open(dataDirectory + r"\serverlist.txt", "a")

def addjdk(path):
    writejdklist().write(path + "\n")


def genservercfg(dir, options):
    with open(dir + r"\config.yml", "a") as cfg:
        cfg.write(f"ServerCore: {options["core"]}" + "\n")
        cfg.write(f"ServerVersion: {options["version"]}" + "\n")
        cfg.write(f"ServerJDK: {ml.java_utils.get_java_information(options["jdkpath"])}" + "\n")
        cfg.write(f"Xms: {options["Xms"]}" + "\n")
        cfg.write(f"Xmx: {options["Xmx"]}" + "\n")
        cfg.write(f"port: {options["port"]}" + "\n")

def makeproperties(dir, port, motd, maxplayers):
    with open(dir + r"\server.properties", "w") as properties:
        properties.write((f"#Minecraft server properties\n"
            f"#Sat Oct 26 02:23:03 YAKT 2024\n"
            f"enable-jmx-monitoring=false\n"
            f"rcon.port=25575\n"
            f"level-seed=\n"
            f"gamemode=survival\n"
            f"enable-command-block=false\n"
            f"enable-query=false\n"
            f"generator-settings=\n"
            f"level-name=world\n"
            f"motd={motdgen(motd)}\n"
            f"query.port={port}\n"
            f"pvp=true\n"
            f"generate-structures=true\n"
            f"difficulty=easy\n"
            f"network-compression-threshold=256\n"
            f"max-tick-time=60000\n"
            f"use-native-transport=true\n"
            f"max-players={maxplayers}\n"
            f"online-mode=false\n"
            f"enable-status=true\n"
            f"allow-flight=false\n"
            f"broadcast-rcon-to-ops=true\n"
            f"view-distance=16\n"
            f"max-build-height=256\n"
            f"server-ip=\n"
            f"allow-nether=true\n"
            f"server-port={port}\n"
            f"enable-rcon=false\n"
            f"sync-chunk-writes=true\n"
            f"op-permission-level=4\n"
            f"prevent-proxy-connections=false\n"
            f"resource-pack=\n"
            f"entity-broadcast-range-percentage=100\n"
            f"rcon.password=\n"
            f"player-idle-timeout=0\n"
            f"debug=false\n"
            f"force-gamemode=false\n"
            f"rate-limit=0\n"
            f"hardcore=false\n"
            f"white-list=false\n"
            f"broadcast-console-to-ops=true\n"
            f"spawn-npcs=true\n"
            f"spawn-animals=true\n"
            f"snooper-enabled=true\n"
            f"function-permission-level=2\n"
            f"level-type=default\n"
            f"text-filtering-config=\n"
            f"spawn-monsters=true\n"
            f"enforce-whitelist=false\n"
            f"resource-pack-sha1=\n"
            f"spawn-protection=0\n"
            f"max-world-size=29999984\n"))
