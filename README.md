Best thing about Kobo? you already have root access and it's linux, just connect to PC!

# SSH/SFTP

rename file `ssh-disabled` to `ssh-enabled` inside directory `/mnt/onboard/.kobo/`

```
[root@kobo .kobo]# cat ssh-disabled
To enable ssh:
- Rename this file to ssh-enabled
- Reboot the device
- Connect via: ssh root@<device_ip>
```

on first ssh login, it'll prompt to set new root password 

# Setup

all the below applications can be installed through one click package (OCP) from this [thread at mobileread](https://www.mobileread.com/forums/showthread.php?t=314220)

[OCP Backup](https://github.com/m4tu4g/kobo-setup/releases/)

script to install OCP can be found in this [post](https://www.mobileread.com/forums/showpost.php?p=3797096)

(keep script and OCP in same directory and run with `./install.command` on terminal)

## NickelMenu

[NickelMenu adds custom menu items to various menus in Kobo's eReader software.](https://pgaskin.net/NickelMenu/)

[my NickelMenu Config](https://gist.github.com/m4tu4g/c0cfec09ee9b7da67cfefc30048497ce)

## KOReader

[KOReader is a document viewer for E Ink devices](https://koreader.rocks/)

### Dictionary

- Shorter Oxford English Dictionary
- Oxford English Dictionary 2nd Edition

SOED is enough for normal readers but both are kept in StarDict formats [here](https://github.com/m4tu4g/kobo-setup/releases/), just unarchive zip inside `/mnt/onboard/.adds/koreader/data/dict`

### Plugins


## Plato

[Plato is a document reader for Kobo's e-readers.](https://github.com/baskerville/plato)
