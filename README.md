### 为什么做这个工具
其实是为了更方便的让大家下载Linux发行版的镜像，因为Linux发行版实在太多了，很难选择，而且很多下载的镜像仓库是在国外，所以会有非常感人的下载速度以及较高的失败率

![扎心](https://bbs.deepin.org/assets/image/raccoon/[sad].gif "在这里输入图片标题")

但是其实有一些国内仓库可以用的，如阿里云、华为云、腾讯云、网易、清华大学等，这是在deepin操作系统官网截的一张图，链接：[https://www.deepin.org/zh/mirrors/releases/](https://www.deepin.org/zh/mirrors/releases/)

![可以下载deepin的第三方ISO库](https://images.gitee.com/uploads/images/2020/1121/124520_a55e2bf0_7896131.png "屏幕截图.png")

所以为了方便大家更好的下载操作系统镜像，因此开发了这个程序

### 如何运行这个程序

 **注意：以前用C#写的这个的Windows版已经停止开发，里面可以下载的镜像不会及时更新** 

这个是在Linux（deepin）下进行编写的，可能在Windows上运行会有些麻烦

 **debian发行版下怎么安装：** 

```
sudo apt install git
sudo apt install wget
sudo apt install python3
sudo apt install python3-pip
pip3 install progressbar
pip3 install requests
git clone https://gitee.com/gfdgd-xi/linux-image-download-tools-python.git
```

然后赋值运行权限：


```
chmod 777 run.py
./run.py
```


### 可以下载哪些发行版的镜像

目前可以下载以下发行版及其版本：

Ubuntu：

    1. ubuntu 12.04.5 Desktop i386

    2. ubuntu 12.04.5 Desktop amd64

    3. ubuntu 14.04.6 Desktop i386

    4. ubuntu 14.04.6 Desktop amd64

    5. ubuntu 16.04.6 Desktop i386

    6. ubuntu 16.04.7 Desktop amd64

    7. ubuntu 18.04.5 Desktop amd64

    8. ubuntu 20.04.1 Desktop amd64

    9. ubuntu 20.04.1 Live Server amd64

    10.ubuntu 20.10 Desktop amd64(当前最新版本)

    11.ubuntu 20.10 Live Server amd64(当前最新版本)

deepin：

    1. deepin 15.5 Beta——小而美的功能(2017.11.15)

    2. deepin 15.5——知你所想，予你所求(2017.11.30)

    3. deepin Live 2.0(2018.3.21)

    4. deepin 15.6——细节中寻求突破(2018.6.15)

    5. deepin 15.7——性能好才是真的好(2018.8.21)

    6. deepin 15.9——跬步千里，厚积薄发(2019.1.16)

    7. deepin 15.10——安全稳定 细致入微(2019.4.28)

    8. deepin 15.11——心心随意动 畅享云端(2019.7.19)

    9.deepin 20 Beta——全新出发，为你而来(2020.4.15)

    10.deepin 20 1001(2020.8.25)

    11.deepin 20 1002——崭新视界，创无止境(2020.9.11)

    12.deepin 20 1003(2020.11.13)(当前最新版本)


