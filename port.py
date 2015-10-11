#!/usr/bin/python
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex(('127.0.0.1', int(sys.argv[1])))
print result
