import random, time


def timer(func):

    def wrapper(*args, **kwargs):
        print("timer started...")

        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"Job time: {time.time() - start_time}")

        return result

    return wrapper


def my_simple_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)

    return wrapper


@timer
def worker1(sleep_time):
    print("Worker1 Started")
    time.sleep(sleep_time)
    print("Worker1 finished!")

    return 3.14


@my_simple_decorator
def worker2():
    print("Worker2 Started")
    time.sleep(random.randint(3, 10))
    print("Worker2 finished!")


@my_simple_decorator
def worker3():
    print("Worker3 Started")
    time.sleep(random.randint(3, 10))
    print("Worker3 finished!")


result = worker1(3)
print(result)