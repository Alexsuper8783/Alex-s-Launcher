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
from AlexLauncher.data.constants import *
from AlexLauncher.scripts.WorkWithFiles import *
from AlexLauncher.scripts.Jdkinstall import *
from AlexLauncher.scripts.LaunchServer import *



def create_server(name, core, version):
    if name in os.listdir(serverDirectory):
        return False
    elif core in CORES:
        if version in CORES[core]:
            os.mkdir(serverDirectory + "\\" + name)
            download(CORES[core][version], serverDirectory + "\\" + name, "server.jar")
