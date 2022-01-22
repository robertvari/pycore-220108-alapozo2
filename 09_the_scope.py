# global scope. global variable
name = "Robert"


def say_my_name():
    # say_my_name scope
    print(name)


def override_global():
    global name
    name = "Csaba"


override_global()
say_my_name()
