import random, time


def timer(func):

    def wrapper(*args, **kwargs):
        print("timer started...")

        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"Job time: {time.time() - start_time}")

        return result

    return wrapper


@timer
def worker1():
    print("Worker1 Started")
    time.sleep(random.randint(3, 10))
    print("Worker1 finished!")


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


worker1()
worker2()
worker3()