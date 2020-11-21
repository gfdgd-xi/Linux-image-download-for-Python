#!/bin/env python3
# Easy for users to run this program
import os
import sys
import time
import progressbar
import requests
print("Prepare the program ...") # prepare the program
p = progressbar.ProgressBar()
N = 100
for i in p(range(N)):
    time.sleep(0.01)
def download(url,path): # This method's function is download internet file
    os.system("wget "+url+" -O "+path)
print("+---------------------------------------------+") # show program inforation
print("|       Linux image download for Python        |")
print("+---------------------------------------------+")
print("|                From 2020 ~ 2020              |")
print("|               language:English               |")
print("|                  Version:1.0                 |")
print("|              Run on the terminal             |")
print("|              Run on the Python 3             |")
print("+----------------------------------------------+")
print("|Tips:                                         |")
print("|        If you want to Run the program,       |")
print("| Your computer need install Python 3 and Wget |")
print("|          and keep run don't have error       |")
print("+----------------------------------------------+")
print("\nChoose you want to download Linux system release mirror image:") # show choose release inforation
print("    1.deepin")
print("    2.ubuntu")
print("    3.See Chinese Linux Apt sources or Apt sources in your computer(Is't running on the Windows)")
release = input(">") # know users want to download which Linux release mirror image
release = release.lower()
if(release == "1" or release == "deepin"): # if users want to download deepin mirror image
    print("Choose you want to download deepin system version mirror image:") # show choose deepin system version inforation
    print("    1. deepin 15.5 Beta——小而美的功能(2017.11.15)")
    print("    2. deepin 15.5——知你所想，予你所求(2017.11.30)")
    print("    3. deepin Live 2.0(2018.3.21)")
    print("    4. deepin 15.6——细节中寻求突破(2018.6.15)")
    print("    5. deepin 15.7——性能好才是真的好(2018.8.21)")
    print("    6. deepin 15.9——跬步千里，厚积薄发(2019.1.16)")
    print("    7. deepin 15.10——安全稳定 细致入微(2019.4.28)")
    print("    8. deepin 15.11——心心随意动 畅享云端(2019.7.19)")
    print("    9.deepin 20 Beta——全新出发，为你而来(2020.4.15)")
    print("    10.deepin 20 1001(2020.8.25)")
    print("    11.deepin 20 1002——崭新视界，创无止境(2020.9.11)")
    print("    12.deepin 20 1003(2020.11.13)(new version)")
    version = input("Choose system version >") # know users want to download which deepin version's mirror image
    path = input("Input save path >") # know users want to save deepin mirror image to where
    if(os.path.exists("./Temp-ISO") == False): # if "./Temp-ISO" file folder isn't exist
        os.mkdir("./Temp-ISO") # mkdir this file folder
    if(path == ""): # if users don't input anything to save path
        path = "./Temp-ISO/deepin.iso" # save mirror deepin to give tacit consent path
    # judge user want to download which image
    version = version.lower()
    if(version == "1" or version == "15.5beta" or version == "15.5 beta"): # deepin 15.5 Beta
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("http://packages.deepin.com/deepin-cd/releases-archive/15.5.Beta/deepin-15.5-amd64-beta.iso",path)
        print("Download End")
    elif(version == "2" or version == "15.5"): # deepin 15.5
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases-archive/15.5/deepin-15.5-amd64.iso",path)
        print("Download End")
    elif(version == "3" or version == "2.0"): # deepin live 2.0
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/live-system/deepin-live-system-2.0-amd64.iso",path)
        print("Download End")
    elif(version == "4" or version == "15.6"): # deepin 15.6
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases-archive/15.6/deepin-15.6-amd64.iso",path)
        print("Download End")
    elif(version == "5" or version == "15.7"): # deepin 15.7
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases-archive/15.7/deepin-15.7-amd64.iso",path)
        print("Download End")
    elif(version == "6" or version == "15.9"): # deepin 15.9
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases-archive/15.9/deepin-15.9-amd64.iso",path)
        print("Download End")
    elif(version == "7" or version == "15.10"): # deepin 15.10
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases-archive/15.10/deepin-15.10-amd64.iso",path)
        print("Download End")
    elif(version == "8" or version == "15.11"): # deepin 15.11
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases-archive/15.11/deepin-15.11-amd64.iso",path)
        print("Download End")
    elif(version == "9" or version == "20beta" or version == "20 beta"): # deepin 20 Beta
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases/20Beta/deepin-20Beta-desktop-amd64.iso",path)
        print("Download End")
    elif(version == "10" or version == "20(1001)" or version == "20 1001" or version == "201001"): # deepin 20 1001
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/d/de/deepin/20_1001/deepin-desktop-community-1001-amd64.iso",path)
        print("Download End")
    elif(version == "11" or version == "20(1002)" or version == "20 1002" or version == "201002"): # deepin 20 1002
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases/20/deepin-desktop-community-1002-amd64.iso",path)
        print("Download End")
    elif(version == "12" or version == "20(1003)" or version == "20 1003" or version == "201003" or version == "new"): # deepin 20 1003 (new version)
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://packages.deepin.com/deepin-cd/releases/20/deepin-desktop-community-1003-amd64.iso",path)
        print("Download End")
    else:
        print("Your choose error deepin version!\nExit the Program")
elif(release == "2" or release == "ubuntu"): # if users want to download ubuntu mirror image
    print("Choose you want to download Ubuntu system version mirror image:")
    print("    1. ubuntu 12.04.5 Desktop i386")
    print("    2. ubuntu 12.04.5 Desktop amd64")
    print("    3. ubuntu 14.04.6 Desktop i386")
    print("    4. ubuntu 14.04.6 Desktop amd64")
    print("    5. ubuntu 16.04.6 Desktop i386")
    print("    6. ubuntu 16.04.7 Desktop amd64")
    print("    7. ubuntu 18.04.5 Desktop amd64")
    print("    8. ubuntu 20.04.1 Desktop amd64")
    print("    9. ubuntu 20.04.1 Live Server amd64")
    print("    10.ubuntu 20.10 Desktop amd64(new version)")
    print("    11.ubuntu 20.10 Live Server amd64(new version)")
    version = input("Choose system version >") # know users want to download which ubuntu version's mirror image
    path = input("Input save path >") # know users want to save deepin mirror image to where
    if(os.path.exists("./Temp-ISO") == False): # if "./Temp-ISO" file folder isn't exist
        os.mkdir("./Temp-ISO") # mkdir this file folder
    if(path == ""): # if users don't input anything to save path
        path = "./Temp-ISO/ubuntu.iso" # save mirror deepin to give tacit consent path
    # judge user want to download which image
    version = version.lower()
    if(version == "1" or version == "12.04.5 i386" or version == "12.04.5i386"): # ubuntu 12.04.5 Desktop i386
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/12.04.5/ubuntu-12.04.5-desktop-i386.iso",path)
        print("Download End")
    elif(version == "2" or version == "12.04.5 amd64" or version == "12.04.5amd64"): # ubuntu 12.04.5 Desktop amd64
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/12.04.5/ubuntu-12.04.5-desktop-amd64.iso",path)
        print("Download End")
    elif(version == "3" or version == "14.04.6 i386" or version == "14.04.6i386"): # ubuntu 14.04.6 Desktop i386
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/14.04.6/ubuntu-14.04.6-desktop-i386.iso",path)
        print("Download End")
    elif(version == "4" or version == "14.04.6 amd64" or version == "14.04.6amd64"): # ubuntu 14.04.6 Desktop amd64
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/14.04.6/ubuntu-14.04.6-desktop-amd64.iso",path)
        print("Download End")
    elif(version == "5" or version == "16.04.7 i386" or version == "16.04.7i386"): # ubuntu 16.04.7 Desktop i386
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/16.04.7/ubuntu-16.04.6-desktop-i386.iso",path)
        print("Download End")
    elif(version == "6" or version == "16.04.7 amd64" or version == "16.04.7amd64"): # ubuntu 16.04.7 Desktop amd64
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/16.04.7/ubuntu-16.04.7-desktop-amd64.iso",path)
        print("Download End")
    elif(version == "7" or version == "18.04.5 amd64" or version == "18.04.5amd64"): # ubuntu 18.04.5 Desktop amd64
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/18.04.5/ubuntu-18.04.5-desktop-amd64.iso",path)
        print("Download End")
    elif(version == "8" or version == "20.04.1 amd64" or version == "20.04.1amd64"): # ubuntu 20.04.1 Desktop amd64
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/20.04.1/ubuntu-20.04.1-desktop-amd64.iso",path)
        print("Download End")
    elif(version == "9" or version == "20.04.1 live server amd64" or version == "20.04.1liveseveramd64"): # ubuntu 20.04.1 Live Server
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/20.04.1/ubuntu-20.04.1-live-server-amd64.iso",path)
        print("Download End")
    elif(version == "10" or version == "20.10 amd64" or version == "20.10amd64"): # ubuntu 20.10 Desktop amd64
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/20.10/ubuntu-20.10-desktop-amd64.iso",path)
        print("Download End")
    elif(version == "11" or version == "20.10 live server amd64" or version == "20.10liveserveramd64"): # ubuntu 20.10 Live Server amd64
        print("Now is downloading, you can input \"Ctrl + C\" to stop downloading ...")
        download("https://mirrors.aliyun.com/ubuntu-releases/20.10/ubuntu-20.10-live-server-amd64.iso",path)
        print("Download End")
    else:
        print("Your choose error Ubuntu system release!\nExit this Program")
elif(release == "3" or release == "apt" or release == "source" or release == "apt source" or release == "aptsource"):
    while(True):
        print("Choose the task to done:")
        print("    1.See your computer apt sources")
        print("    2.See Chinese deepin Apt sources(mirror.aliyun.com)")
        print("    3.See Chinese Ubuntu Apt sources(mirror.aliyun.com)")
        print("    4.Change your computer Apt sources")
        print("    5.Exit the Program")
        task = input(">")
        if(task == "1"):
            print("Your computer Apt source:\n################################################################################\n")
            os.system("cat /etc/apt/sources.list")
            print("\n######################################################\n")
        if(task == "2"):
            print("Chinese deepin Apt sources(mirror.aliyun.com)\n################################################################\n")
            os.system("cat ./sources/deepin-sources.list")
            print("\n######################################################\n")
            pass
        if(task == "3"):
            print("Which Ubuntu Apt sources do you want to see:")
            print("    1.Ubuntu 14.04.5")
            print("    2.Ubuntu 16.04")
            print("    3.Ubuntu 18.04")
            print("    4.Ubuntu 20.04")
            version = input(">").lower()
            if(version == "1"):
                print("#######################################\n")
                os.system("cat ./sources/ubuntu14.04.5-sources")
                print("\n#######################################")
            if(version == "2"):
                print("#######################################\n")
                os.system("cat ./sources/ubuntu16.04-sources")
                print("\n#######################################")
            if(version == "3"):
                print("#######################################\n")
                os.system("cat ./sources/ubuntu18.04-sources")
                print("\n#######################################")
            if(version == "4"):
                print("#######################################\n")
                os.system("cat ./sources/ubuntu20.04-sources")
                print("\n#######################################")
            pass
        if(task == "4"):
            choose = input("Tips:\nProgram will open Apt sources with Vim with root\nIf you want to next, please press down Enter, if you want to stop next operating, please input \"exit\" and press down Enter>")
            if(choose.lower() == "exit"):
                pass
            else:
                os.system("sudo vim /etc/apt/sources.list")
        if(task.lower() == "e" or task.lower == "exit" or task.lower() == "5"):
            break
elif(release == "E" or release == "exit"): # if users want to exit this program
    pass # Exit the Program 
else: # if users don't input right things
    print("Your chosse error Linux system release!\nExit the Program") # show tips information
