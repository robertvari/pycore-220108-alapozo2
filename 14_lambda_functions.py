add_numbers = lambda a, b: a+b
multiply_numbers = lambda a, b: a*b
divide_numbers = lambda a, b: a/b

print(add_numbers(10, 2))
print(multiply_numbers(10, 2))
print(divide_numbers(10, 2))

name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]
print(sorted(name_list))
print(sorted(name_list, key=lambda name: name.split()[-1]))

students = {
    "0": {"name": "Vári Róbert", "grade": 45},
    "1": {"name": "Kiss Elemér", "grade": 32},
    "3": {"name": "Nagy Adrienn", "grade": 56},
    "4": {"name": "Tóth Barna", "grade": 12},
    "5": {"name": "Kiss Elemér Aladár", "grade": 86},
}

print(sorted(students, key=lambda id: students[id]["grade"]))