name = "Robert"


def say_hello(in_name):
    print(name)
    print(in_name)

    email = "mail.pythonsuli@gmail.com"

    def say_my_name():
        email = "csaba@gmail.com"
        print(email)

    say_my_name()
    print(email)

say_hello("Csaba")