def say_hello(name):
    print(f"Hello! {name}")

say_hello("Ryan")
say_hello("Maya")
say_hello("Aysel")

# user_name = input("What is your name?")

# say_hello(user_name)


def say_hello(username="Cuthbert", language="RU"):
    if language == "EN":
        print("Hello "+username)
    elif language == "RU":
        print("Privet "+username)
    else:
        print("This language is not supported: " + language)

say_hello("EN")