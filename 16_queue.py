from utilities.file_utils import get_files
import time, random, threading, queue

# create a queue from the file list
job_queue = queue.Queue()

# add files to job_queue
# standard python list not good for threading!!!!
files = get_files(r"C:\Work\_PythonSuli\pycore-220108\photos")
for i in files:
    job_queue.put(i)

def file_worker():
    while True:
        pass
