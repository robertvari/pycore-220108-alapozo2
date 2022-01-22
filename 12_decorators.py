import random, time


def worker():
    time.sleep(random.randint(3, 10))


worker()