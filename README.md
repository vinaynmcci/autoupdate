# BrixUI

Simple standard desktop application for pushing Brix data in a convenient way.

## List of Contents

<!-- TOC depthFrom:2 updateOnsave:true -->

- [About Application](#about-application)

- [Prerequisites for running or building](#prerequisites-for-running-or-building)

- [Interpret python source](#interpret-python-source)

- [GUI Preview](#gui-preview)

- [Meta](#meta)
  - [Trademarks](#trademarks)

## About Application

This application is designed to create Simple User Interface for pushing the Brix data manually.
It is a cross platform GUI Application developed by using Wxpython.

## Prerequisites for running or building

<strong>On Windows:</strong>

Development environment

* OS - Windows 10 64 bit
* Python - 3.7.6
* wxpython - 4.0.7.post2
* requests - 2.26
* pyinstaller - 3.6 

Download [python3.7.6](https://www.python.org/downloads/release/python-376/) and install

```shell
pip install wxpython==4.0.7.post2
pip install requests
pip install pyinstaller
```
<strong>On Mac OS:</strong>

Development environment

* Mac OS - Catalina 10.15.7 64 bit
* Python - 3.6.9
* wxpython - 4.0.7.post2
* requests - 2.26
* pyinstaller - 4.6
```shell
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install wxpython==4.0.7.post2
sudo pip3 install requests
```

## Interpret python source

Move to the directory `destdir/src/`

Run the below command

For Windows
```shell
python main.py
```
For Mac
```shell
python3.6 main.py
```
## GUI Preview

![UI Preview](assets/BrixUI.png)



## Meta

### Trademarks

MCCI and MCCI Catena are registered trademarks of MCCI Corporation. All other marks are the property of their respective owners.