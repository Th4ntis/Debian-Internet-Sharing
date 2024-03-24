#!/usr/bin/env python3
import subprocess

def run_command(command):
    """Run a shell command."""
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def setup_internet_sharing(internet_interface, device_interface):
    """Set up internet sharing from the internet interface to another USB/RNDIS Device."""
    # Enable IP forwarding
    run_command("echo 1 > /proc/sys/net/ipv4/ip_forward")

    # Configure NAT over iptables
    run_command(f"iptables -t nat -A POSTROUTING -o {internet_interface} -j MASQUERADE")
    run_command(f"iptables -A FORWARD -i {internet_interface} -o {device_interface} -m state --state RELATED,ESTABLISHED -j ACCEPT")
    run_command(f"iptables -A FORWARD -i {device_interface} -o {internet_interface} -j ACCEPT")

    # Assign an IP address to the Devices interface if needed
    run_command(f"ifconfig {device_interface} 172.16.42.1 netmask 255.255.0.0")

    print("Internet sharing setup complete.")

if __name__ == "__main__":
    internet_interface = input("Enter the name of your internet-facing interface (e.g., eth0, wlan0): ")
    device_interface = input("Enter the name of your USB/RNDIS devices interface (e.g., eth1): ")
    setup_internet_sharing(internet_interface, device_interface)
