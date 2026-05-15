# default arguments
# def add(num1=0, num2=0):
#     return num1+num2

# variable length arguments
# def add(num1, *num2):
#     sum = num1
#     for n in num2:
#         sum += n
#     return sum


# result = add(4, 5, 6, 7)
# print(result)

# key word arguments
# def person(name, age=18):
#     print("name:", name)
#     print("age:", age)


# person(age=30, name="sai")

# variable keyword length arguments
def person(name, **kwlargs):
    print("name:", name)
    for k, v in kwlargs.items():
        print(k, ":", v)


person(age=30, name="sai", loc="hnk", tech="python")
