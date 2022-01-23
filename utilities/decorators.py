import time, logging


def timer(func):

    def wrapper(*args, **kwargs):
        print("timer started...")

        start_time = time.time()

        result = func(*args, **kwargs)

        print(f"Job time: {time.time() - start_time}")

        return result

    return wrapper


def logger(func):
    logging.basicConfig(filename="my_log.log", level=logging.INFO)

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper
