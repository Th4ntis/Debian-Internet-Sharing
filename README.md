# Debian-Internet-Sharing
This is a python script to setup connection sharing from your internet-facing interface to a USB/RNDIS Device. This was originally made to be used on Debain 12 and a [WiFi Pineapple](https://shop.hak5.org/products/wifi-pineapple) but this can be used on other devices as well.

You may need to install the `iptables` package. On Debian or debian based distros(ubuntu, kali, etc), you can run
```bash
sudo apt install -y iptables
```

As this modifies IP Tables, this will need to be run as sudo/root.
