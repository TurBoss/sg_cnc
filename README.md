
# SG CNC for linuxcnc

#### Surface Grinder CNC



## Quick install

install linuxcnc 2.80 using the debian 10 iso

http://www.linuxcnc.org/

### Dependencies

```
$ sudo apt install python-pyqt5 python-pyqt5.qtquick python-dbus.mainloop.pyqt5 python-pyqt5.qtopengl python-pyqt5.qsci python-pyqt5.qtmultimedia qml-module-qtquick-controls gstreamer1.0-plugins-bad libqt5multimedia5-plugins pyqt5-dev-tools python-dev python-setuptools python-pip git
```

### installation

```
$ git clone https://github.com/kcjengr/sg_cnc.git
$ cd sg_cnc
$ pip install -e .
```

## Customize

now you can run editvcp to edit the interface

```
$ editvcp sg_cnc
```

## Resources

* [Development](https://github.com/kecjengr/sg_cnc)
* [Documentation](https://qtpyvcp.com)
* [Issue Tracker]()


## Dependancies

* [LinuxCNC](https://linuxcnc.org) 2.80
* Python 2.7
* PyQt5 or PySide2
* [QtPyVCP](https://qtpyvcp.com/)

SG_CNC is developed and tested using the LinuxCNC Debian 10 (buster) [Live ISO](http://www.linuxcnc.org/) It should run on any system that can have PyQt5 installed, but Debian 10 is the only OS
that is officially supported.


## DISCLAIMER

THE AUTHORS OF THIS SOFTWARE ACCEPT ABSOLUTELY NO LIABILITY FOR
ANY HARM OR LOSS RESULTING FROM ITS USE.  IT IS _EXTREMELY_ UNWISE
TO RELY ON SOFTWARE ALONE FOR SAFETY.  Any machinery capable of
harming persons must have provisions for completely removing power
from all motors, etc, before persons enter any danger area.  All
machinery must be designed to comply with local and national safety
codes, and the authors of this software can not, and do not, take
any responsibility for such compliance.


Copyright (c) 2020 All rights reserved.
