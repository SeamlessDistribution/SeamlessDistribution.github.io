---
layout: default
title: Merchant API - Python howto
description: SEQR Merchant, webshop, POS integration
---
 
## Getting started with python

### OSX and Linux

Python is normally installed on these platforms, you might need to get the suds and qrcode python library. For this you could use easy_install suds and qrcode.  Our examples are made for the terminal to simplify the code. 

### Windows

Here are the steps to download, install and configure python to run merchant on a windows machine:
* Go to http://www.python.org/getit/ and download python for windows
* Execute the installation package
* Open python shell
* Install setuptools on Windows, download ez_setup.py and run it. The script will download the appropriate .egg file and install it for you.
* Open Windows command prompt
* Execute C:\Python33\scripts\easy_install suds-jurko to install suds library
* Execute C:\Python33\scripts\easy_install qrcode to install qrcode library

(print_tty() is reported to fail in windows for printing qrcodes, if so, use pillow instead with: 
    image = qr.make_image() 
    image.show()

