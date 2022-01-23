import random, time


def worker():
    print("Worker Started")
    time.sleep(random.randint(3, 10))
    print("Worker finished!")

worker()