def add_numbers(a, b) -> int:
    return a+b


def multiply_numbers(a, b):
    return a*b


def divide_numbers(a: int, b: int) -> float:
    return a/b


result = add_numbers(10, 20)
result = multiply_numbers(result, 10)
result = divide_numbers(result, 3)
print(result)