#! C:\Program Files\Python37\python.exe

# A program to sheck the network for active devices on user
# input ports
#
# Author: Marcus
# Date: 15/3/2019

import ipaddress
# ask user for network
address = []
netnum = 0
network = input("Please enter start of network as type X.X.X :")
print(network)
while netnum < 255:
    ip = str(str(network) + "." + str(netnum))
    address.append(ip)
    netnum += 1
print(address)

ports = []
port = 0
print("Please enter ports, one line at a time. \n Press X to stop.")
# ask user for ports
while port != "X":
    port = (input("Port: "))
    if port.isdigit():
        if int(port) < 65535:
            ports.append(port)
        else:
            print("Input a valid port below 65535")
    elif port == "X" or port =="x":
        break
    else:
        print("Please input a valid number.")


print(ports)

# print IP and ports
for ip in address:
    for i in ports:
        print("We will scan ",ip," on port ",i)
