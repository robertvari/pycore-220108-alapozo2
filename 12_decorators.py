import random, time
from utilities.decorators import timer, logger


@timer
def worker1(sleep_time):
    print("Worker1 Started")
    time.sleep(sleep_time)
    print("Worker1 finished!")

    return 3.14


@timer
def worker2():
    print("Worker2 Started")
    time.sleep(random.randint(3, 10))
    print("Worker2 finished!")


@timer
def worker3():
    print("Worker3 Started")
    time.sleep(random.randint(3, 10))
    print("Worker3 finished!")


result = worker1(3)
print(result)