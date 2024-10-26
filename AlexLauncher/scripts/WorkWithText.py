import subprocess
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

def motdgen(motd):
    if motd is None:
        return None

    result = []

    for c in motd:
        if ord(c) > 127:
            result.append(f"\\u{ord(c):04x}")
        else:
            result.append(c)
    return ''.join(result)
