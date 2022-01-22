import random, time


def worker1():
    print("Worker1 Started")
    time.sleep(random.randint(3, 10))
    print("Worker1 finished!")


def worker2():
    print("Worker2 Started")
    time.sleep(random.randint(3, 10))
    print("Worker2 finished!")


def worker3():
    print("Worker3 Started")
    time.sleep(random.randint(3, 10))
    print("Worker3 finished!")


worker1()
worker2()
worker3()