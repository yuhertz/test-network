import os
import subprocess

def create_fake_network(interface, ssid):
    subprocess.call(f"airmon-ng start {interface}", shell=True)
    subprocess.call(f"airbase-ng -e {ssid} -c 6 mon0", shell=True)

def stop_fake_network():
    subprocess.call("airmon-ng stop mon0", shell=True)

if __name__ == "__main__":
    interface = input("Enter the name of wireless interface (iwconfig): ")
    ssid = input("Enter SSID for network (name): ")

    create_fake_network(interface, ssid)
    print("fake network created")

    input("Press enter to stop the netwokrk")
    stop_net_work()
    print("Fake network stopped!")
