# Ternary operators
age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

# Logical operators
# and
# or
# not
high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
# Short circuit evaluation
if high_income or good_credit or student:
    print("Eligible")
# Chaining comparison operators
# Age should be between 18 and 65
# if age >= 18 and age < 65:
if 18 <= age < 65:
    print("Eligible")
