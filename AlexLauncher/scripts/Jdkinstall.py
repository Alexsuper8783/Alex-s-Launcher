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


def jdkinstall(version):
    if version > 21:
        version = 21
    if jdkpath[javaver.index(version)] in os.listdir(jdkDirectory):
        print("")
    else:
        jdk.install(version, path=jdkDirectory)
        addjdk(path=jdkDirectory + "\\" + javapath[javaver.index(version)])
        return True
    if javapath[javaver.index(version)] in jdklist():
        return False
    else:
        addjdk(path=jdk + "\\" + javapath[javaver.index(version)])
        return True
def checkjdk(version):
    if jdkpath[javaver.index(version) in os.listdir(jdkDirectory)]:
        if javapath.index(javaver.index(version)) in jdklist():
            return True
        else:
            return False
    return False