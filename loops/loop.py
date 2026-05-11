# # For in
# # goes from 0 to 2
# for number in range(3):
#     print("Attempted", number+1, (number+1) * ".")
# # goes from 1 to 3
# for number in range(1, 4):
#     print("Attempted", number, number*".")
# # goes from 1 to 9 and skips 2 values
# for number in range(1, 10, 2):
#     print("Attempted", number, number*".")

# For Else
# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break

# else:
#     print("Attempted 3 times and failed")
# Nested loops
# for x in range(5):
#     for y in range(3):
#         print(f"({x},{y})")


# print(type(5))
# print(type(range(5)))

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# Infinity loops
# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count = count+1
        print(number)
print(f"We have {count} even numbers")
