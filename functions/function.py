# def greet():
#     print("hi there")
#     print("Welcome aboard")


# greet()
# parameters
# def greet(first_name, last_name):
#     print(f"hi {first_name} {last_name}")
#     print("Welcome aboard")


# # Arguments
# greet("apple", "fruit")
# Types of functions
# 1-Perform a task
# 2-Return a value
# def greet(name):
#     print(f"Hi {name}")


# greet("Apple")


# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Apple")
# print(message)
# Key word arguments
# def increment(number, by):
#     return number+by


# print(increment(2, by=1))
# Default arguments
# def increment(number, by=1):
#     return number+by


# print(increment(2, 5))
# X args
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
