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
    while not job_queue.empty():
        next_job = job_queue.get()
        print(f"{threading.current_thread().name}: I'm working on {next_job}")

        time.sleep(random.randint(1, 10))

        print(f"{threading.current_thread().name}: I finsihed {next_job}!!!")

        job_queue.task_done()
