import random, time, threading


def worker1():
    print("Worker1 Started")
    time.sleep(random.randint(3, 10))
    print("Worker1 finished!")


def worker2():
    print("Worker2 Started")
    time.sleep(random.randint(3, 10))
    print("Worker2 finished!")


t1 = threading.Thread(target=worker1)
t2 = threading.Thread(target=worker2)

t1.start()
t2.start()