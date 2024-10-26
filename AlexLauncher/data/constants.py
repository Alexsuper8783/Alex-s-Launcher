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
from yaml import  *

Roaming = ml.utils.get_minecraft_directory().replace(".minecraft", "")
directory = r"C:\Users\gavri\PycharmProjects\Alex's Launcher"
scriptsDirectory = directory + r"\AlexLauncher\scripts"
dataDirectory = directory + r"\AlexLauncher\data"
jdkDirectory = directory + r"\AlexLauncher\Jdk"
serverDirectory = directory + r"\AlexLauncher\MineServers"

with open("config.yml", "r") as f:
    configuration = load(f)

javaver = [8, 11, 16, 17, 18, 19, 20, 21]
javapath = ["jdk-8.0.432+6\\bin\\java.exe", "jdk-11.0.25+9\\bin\\java.exe", "jdk-16.0.2+7\\bin\\java.exe", "jdk-17.0.13+11\\bin\\java.exe", "jdk-18.0.2.1+1\\bin\\java.exe", "jdk-19.0.2+7\\bin\\java.exe", "jdk-20.0.2+9\\bin\\java.exe", "jdk-21.0.5+11\\bin\\java.exe"]
jdkpath = javapath[:-13]
CORES = {
    "VANNILA" : {
        "1.7.10" : "https://getbukkit.org/get/952438ac4e01b4d115c5fc38f891710c4941df29",
        "1.8.9" : "https://getbukkit.org/get/b58b2ceb36e01bcd8dbf49c8fb66c55a9f0676cd",
        "1.9.4" : "https://getbukkit.org/get/edbb7b1758af33d365bf835eb9d13de005b1e274",
        "1.10.2" : "https://getbukkit.org/get/3d501b23df53c548254f5e3f66492d178a48db63",
        "1.11.2" : "https://getbukkit.org/get/f00c294a1576e03fddcac777c3cf4c7d404c4ba4",
        "1.12.2" : "https://getbukkit.org/get/aca9f985a2d521b3e2cb9196c2a59a70",
        "1.13.2" : "https://getbukkit.org/get/d41d8cd98f00b204e9800998ecf8427e",
        "1.14.4" : "https://getbukkit.org/get/5be16c1942635ee06179d71312a8239e",
        "1.15.2" : "https://getbukkit.org/get/17736f20cd1c875215cb5ba37ec2a285",
        "1.16.5" : "https://getbukkit.org/get/82fbeffe67b6c1ae98670cb3e066f76b",
        "1.17.1" : "https://getbukkit.org/get/c503fcf07fdff1ffb5296f656c3c7a09",
        "1.18.2" : "https://getbukkit.org/get/d7ed835fe643a40470ea6e72c60ae193",
        "1.19.4" : "https://getbukkit.org/get/37a8977887ff7d3f474eb2db67d01cff",
        "1.20.1" : "https://getbukkit.org/get/f6841098c87f7a810ae6dec98ce16085",
        "1.20.4" : "https://getbukkit.org/get/3aa7c7ddab0a25055a1f271e81f47365",
        "1.20.6" : "https://getbukkit.org/get/5a6e9a5156a258139123a673be08a5d3",
        "1.21" : "https://getbukkit.org/get/a53a0d30aa52ac352c3f52a6c4f2fad1"
    },
    "BUKKIT" : {
        "1.7.10" : "https://getbukkit.org/get/X7X2KgF0aYKu2TlU4rmLviye0sLo1fTV",
        "1.8.8" : "https://getbukkit.org/get/lZ6lfqphkPczgKPMdwAmF90p1rPRYPcC",
        "1.9.4" : "https://getbukkit.org/get/MRaXTNhVXZV3iNDueaDTyap1MyiWG3vq",
        "1.10.2" : "https://getbukkit.org/get/EOJorlNmgujzkEQbHjS9WvrixvjLW29V",
        "1.11.2" : "https://getbukkit.org/get/LM6KTipzCHHt8TbxQJ2JyVhR8aLmp6k7",
        "1.12.2" : "https://getbukkit.org/get/V1F1tpQFW3asBTkOpDS4tVQGGovdZhGv",
        "1.13.2" : 'https://getbukkit.org/get/fQ2hcjORI73x66tj7h0X8f4hteJAB64i',
        "1.14.4" : "https://getbukkit.org/get/CiNKyh4l9MuPHLpovnGSDU2oHT9gCpUc",
        "1.15.2" : "https://getbukkit.org/get/jUn4Un6oqx2qxzbcsDq9sbMSG9fGmX9D",
        "1.16.5" : "https://getbukkit.org/get/SMcQ5xHvsEgymwYGNTFf7TDxrm0V364c",
        "1.17.1" : "https://getbukkit.org/get/9bcc5cd27a1cd4ecd34292122827d3e0",
        "1.18.2" : "https://getbukkit.org/get/92f15442e8a9edea8394b208ac08d667",
        "1.19.4" : "https://getbukkit.org/get/880853f1608334e288ea088af77bb0d4",
        "1.20.1" : "https://getbukkit.org/get/0f99aa28b2d1f8251d201311e14935fc",
        "1.20.4" : "https://getbukkit.org/get/8fcc6d1ad097267ea7fb0549540f44c9",
        "1.20.6" : "https://getbukkit.org/get/8a65ca34f1b79a82ea35901d75fc2cdb",
        "1.21" : "https://getbukkit.org/get/b01b6557e8ae58e7be3287cfc64e9326"
    },
    "SPIGOT" : {
        "1.7.10" : "https://getbukkit.org/get/jWPoIQARZsxCjUaqXgj2UwcQWqQdUYDo",
        "1.8.8" : "https://getbukkit.org/get/hNiHm0tuqAg1Xg7w7zudk63uHr0xo48D",
        "1.9.4" : "https://getbukkit.org/get/aVtd1rm66P6ut7XRlr5BzInJ409qEFCo",
        "1.10.2" : "https://getbukkit.org/get/GE9W5jg4MkD62LHEDIC6BiijPbkxoWb3",
        "1.11.2" : "https://getbukkit.org/get/FnLNb42htOpfvn3NaEmYKXGmptFx4CjU",
        "1.12.2" : "https://getbukkit.org/get/Fpt2yFn7HRTrot5uE1b8NFWtpQlYITgK",
        "1.13.2" : "https://getbukkit.org/get/QMerkBxNGNl3EnQl8gACGfWuJnJtJuWB",
        "1.14.4" : "https://getbukkit.org/get/68aef01121494a41fe71890b81d69d07",
        "1.15.2" : "https://getbukkit.org/get/hJhavPDjhYFfqjyPAibsKAJecPpl7Z2V",
        "1.16.5" : "https://getbukkit.org/get/RD0y91OTotryPrElNQe4ovBLDNweoO5Z",
        "1.17.1" : "https://getbukkit.org/get/bf44510c50ddefccbaee1379c1f751de",
        "1.18.2" : "https://getbukkit.org/get/a3003972a592e3c6e668feb824b75cec",
        "1.19.4" : "https://getbukkit.org/get/aed78f3ff7f789ab0f5c8e55bc0a6ab1",
        "1.20.1" : "https://getbukkit.org/get/07b1f67275b974c9478281346e652279",
        "1.20.4" : "https://getbukkit.org/get/272245e4f948b0a66b0b4c34dfa27c49",
        "1.20.6" : "https://getbukkit.org/get/311304f700e4e62b6492c89b5ffb6587",
        "1.21" : "https://getbukkit.org/get/4063d239ce16b22d948c037ce7a9fb8c"
    },
    "PAPER" : {
        "1.8.8" : "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar",
        "1.9.4" : "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar",
        "1.10.2" : "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar",
        "1.11.2" : "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar",
        "1.12.2" : "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar",
        "1.13.2" : "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar",
        "1.14.4" : "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar",
        "1.15.2" : "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar",
        "1.16.5" : "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar",
        "1.17.1" : "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar",
        "1.18.2" : "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar",
        "1.19.4" : "https://api.papermc.io/v2/projects/paper/versions/1.19.4/builds/550/downloads/paper-1.19.4-550.jar",
        "1.20.1" : "https://api.papermc.io/v2/projects/paper/versions/1.20.1/builds/196/downloads/paper-1.20.1-196.jar",
        "1.20.4" : "https://api.papermc.io/v2/projects/paper/versions/1.20.4/builds/497/downloads/paper-1.20.4-497.jar",
        "1.20.6" : "https://api.papermc.io/v2/projects/paper/versions/1.20.6/builds/150/downloads/paper-1.20.6-150.jar",
        "1.21" : "https://api.papermc.io/v2/projects/paper/versions/1.21/builds/130/downloads/paper-1.21-130.jar",
        "1.21.1" : "https://api.papermc.io/v2/projects/paper/versions/1.21.1/builds/128/downloads/paper-1.21.1-128.jar"
    },
    "PURPUR" : {
        "1.21.1" : "https://api.purpurmc.org/v2/purpur/1.21.1/2328/download",
        "1.21" : "https://api.purpurmc.org/v2/purpur/1.21/2284/download",
        "1.20.6" : "https://api.purpurmc.org/v2/purpur/1.20.6/2233/download",
        "1.20.4" : "https://api.purpurmc.org/v2/purpur/1.20.4/2176/download",
        "1.19.4" : "https://api.purpurmc.org/v2/purpur/1.19.4/1985/download",
        "1.18.2" : "https://api.purpurmc.org/v2/purpur/1.18.2/1632/download",
        "1.17.1" : "https://api.purpurmc.org/v2/purpur/1.17.1/1428/download",
        "1.16.5" : "https://api.purpurmc.org/v2/purpur/1.16.5/1171/download"
    },
    "PUFFERFISH" : {
        "1.21.1" : "https://ci.pufferfish.host/job/Pufferfish-1.21/21/artifact/build/libs/pufferfish-paperclip-1.21.1-R0.1-SNAPSHOT-mojmap.jar",
        "1.20.4" : "https://ci.pufferfish.host/job/Pufferfish-1.20/52/artifact/build/libs/pufferfish-paperclip-1.20.4-R0.1-SNAPSHOT-reobf.jar",
        "1.19.4" : "https://ci.pufferfish.host/job/Pufferfish-1.19/73/artifact/build/libs/pufferfish-paperclip-1.19.4-R0.1-SNAPSHOT-reobf.jar",
        "1.18.2" : "https://ci.pufferfish.host/job/Pufferfish-1.18/72/artifact/build/libs/pufferfish-paperclip-1.18.2-R0.1-SNAPSHOT-reobf.jar",
        "1.17.1" : "https://ci.pufferfish.host/job/Pufferfish-1.17/22/artifact/build/libs/Pufferfish-1.17.1-R0.1-SNAPSHOT.jar"
    },
    "MOHIST" : {
        "1.20.1" : "https://mohistmc.com/api/v2/projects/mohist/1.20.1/builds/894/mohist-1.20.1-894-server.jar",
        "1.19.4" : "https://mohistmc.com/api/v2/projects/mohist/1.19.4/builds/215/mohist-1.19.4-215-server.jar",
        "1.18.2" : "https://mohistmc.com/api/v2/projects/mohist/1.18.2/builds/189/mohist-1.18.2-189-server.jar",
        "1.16.5" : "https://mohistmc.com/api/v2/projects/mohist/1.16.5/builds/1243/mohist-1.16.5-1243-server.jar",
        "1.12.2" : "https://mohistmc.com/api/v2/projects/mohist/1.12.2/builds/346/mohist-1.12.2-346-server.jar",
        "1.7.10" : "https://mohistmc.com/api/v2/projects/mohist/1.7.10/builds/46/mohist-1.7.10-46-server.jar"
    },
    "BANNER" : {
        "1.19.4" : "https://mohistmc.com/api/v2/projects/banner/1.19.4/builds/403/banner-1.19.4-403-server.jar",
        "1.20.1" : "https://mohistmc.com/api/v2/projects/banner/1.20.1/builds/766/banner-1.20.1-766-server.jar",
        "1.21.1" : "https://mohistmc.com/api/v2/projects/banner/1.21.1/builds/149/banner-1.21.1-149-server.jar"
    },
    "BUNGEECORD" : "https://ci.md-5.net/job/BungeeCord/lastSuccessfulBuild/artifact/bootstrap/target/BungeeCord.jar",
    "VELOCITY" : "https://api.papermc.io/v2/projects/velocity/versions/3.4.0-SNAPSHOT/builds/445/downloads/velocity-3.4.0-SNAPSHOT-445.jar"
}