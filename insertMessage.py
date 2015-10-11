#!/usr/bin/python
import sys
from azure.storage.queue import QueueService

account_name = "mcdockerqueue"
account_key = sys.argv[2]
queuename = sys.argv[1]

queue_service = QueueService(account_name, account_key)

try:
	queue_service.create_queue(queuename)
except:
	print "Queue creation failed."

for i in range(0,4):
	queue_service.put_message(queuename, 'Hello World %s' %i)
	print i
