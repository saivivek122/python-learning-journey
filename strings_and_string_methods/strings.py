# strings
course = "Python Programming"

# length of a string
print(len(course))
# To get required character
print(course[0])
print(course[-1])
# To slice the string
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
# Escape sequences
# \"
# \'
# \\
# \n
course = "Python \nProgramming"
print(course)
# Formatted Strings
first = "hey"
last = "how are you"
full = first+" "+last
full_name = f"{first} {last}"
print(full_name)
# String methods
course = "  python programming"
# To Capitalize
print(course.upper())
# To lower
print(course.lower())
# To capitalize first letter of every word
print(course.title())
# To trim white spaces at start and end
print(course.strip())
# To trim white space at start
print(course.lstrip())
# To trim white space at end
print(course.rstrip())
# To get index of any character or string
print(course.find("pro"))
# To replace character or string
print(course.replace("p", "j"))
# To check the existence of character or string
print("pro" in course)
# To check the not existence of character or string
print("swift" not in course)
