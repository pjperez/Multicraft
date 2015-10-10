#!/usr/bin/python
# -----------------------------------------------------------------------------
#
# Multicraft - Launch multiple Minecraft instances using docker
# Pedro Perez - 2015
#
# -----------------------------------------------------------------------------
import sys
import socket
from docker import Client
import os

debug = 1
defaultport = 25565
counter = 0

def createMcInstance(port):
        directory = "/mnt/mc" + str(port)
        try:
                os.mkdir(directory)
        except:
                print "Directory already exists!"
        c = Client(base_url='unix://var/run/docker.sock')
        container = c.create_container(image='mcdocker', ports=[25565], command='/start')
        c.start(container, port_bindings={25565: ('0.0.0.0', port)})


def checkPort(localport):
        if localport < 65536:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = s.connect_ex(('127.0.0.1', localport))
                return result
                s.close()
        else:
                return 111

while 1:
        freeport = checkPort(defaultport)
        if freeport == 0:
                defaultport += 1
                counter += 1
                if counter > 5:
                        print "too many instances!"
                        sys.exit()
        else:
                if debug == 1: print "Port %s is free" % defaultport
                createMcInstance(defaultport)
                sys.exit()
