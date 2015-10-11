#!/usr/bin/python
# -----------------------------------------------------------------------------
#
# Multicraft - Launch multiple Minecraft instances using docker
# Pedro Perez - 2015
#
#
# -----------------------------------------------------------------------------
import sys
import os
import socket
from docker import Client


debug = 0
defaultport = 25565
counter = 0
instanceCreated = 0
maxInstances = 3
imageName = "mcdocker"

# Create a new instance on an available port
def createMcInstance(port):
        directory = "/mnt/mc" + str(port)
        try:
                os.mkdir(directory)
        except:
                if debug == 1: print "Directory already exists!"
        c = Client(base_url='unix://var/run/docker.sock')
        container = c.create_container(image=imageName, ports=[25565], command='/start')
        c.start(container, port_bindings={25565: ('0.0.0.0', port)})
	return container

# Simple TCP 3WHS to check if a port is available, returns 0 if it's not.
def checkPort(localport):
        if localport < 65536:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex(('127.0.0.1', localport))
                return result
                s.close()
        else:
                return 111

# Main thread - Check if port 25565 and move to the next if it's not. Once a free port has been found, create a new instance (up to 3)
while instanceCreated == 0:
        freeport = checkPort(defaultport)
        if freeport == 0:
                defaultport += 1
                counter += 1
                if counter > maxInstances:
                        print "Too many instances! you can't run more than %s instances" % maxInstances
                        sys.exit()
        else:
                if debug == 1: print "Port %s is free" % defaultport
                container = createMcInstance(defaultport)
                instanceCreated = 1

# Return Instance ID, port and total number of instances once finished creating the server
print "Instance ID: %s" % container["Id"]
print "Listening on port %s" % defaultport
print "There are %s instances running on this server" % counter+1
sys.exit()
