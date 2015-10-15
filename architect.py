#!/usr/bin/python
# -----------------------------------------------------------------------------
#
# Architect - Get jobs from the queue and assign them to different Multicraft workers
# Pedro Perez - 2015
#
# -----------------------------------------------------------------------------
import sys
import os
import subprocess
from azure.storage.queue import QueueService

account_name = "mcdockerqueue"
account_key = sys.argv[1]
queuename = "pendingservers"

queue_service = QueueService(account_name, account_key)

queue_metadata = queue_service.get_queue_metadata(queuename)
count = queue_metadata['x-ms-approximate-messages-count']

print "There are %s messages in the queue" % count


if count > 0:
	messages = queue_service.get_messages(queuename)

	for message in messages:
	    print(message.message_text)

	# placeholder for DO SOME AMAZING SHIT

	print "start"
	subprocess.call(["./multicraft.py", account_key])
	print "end"

	# Remove message from the queue
	queue_service.delete_message(queuename, message.message_id, message.pop_receipt)
else:
	print "There are no messages to process"
