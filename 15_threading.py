import time, threading


def worker1(sleep_time):
    print(f"Worker1 Started. Sleep time: {sleep_time}")
    time.sleep(sleep_time)
    print("Worker1 finished!")


def worker2(sleep_time):
    print(f"Worker2 Started Sleep time: {sleep_time}")
    time.sleep(sleep_time)
    print("Worker2 finished!")


t1 = threading.Thread(target=worker1, args=[3])
t2 = threading.Thread(target=worker2, args=[6])

t1.start()
t2.start()