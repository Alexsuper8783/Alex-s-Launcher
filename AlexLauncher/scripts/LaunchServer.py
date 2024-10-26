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

def launch_server(ServerID, JavaVer, Min, Max):
    if checkjdk(JavaVer) and ServerID <= len(serverlist()) and Max < (psutil.virtual_memory()):
        locjavapath = javapath[javaver.index(JavaVer)]
        locserverpath = serverlist()[ServerID]
        os.chdir(locserverpath)
        if configuration["autoeula"]:
            print("test")