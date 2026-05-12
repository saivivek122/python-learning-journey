set1 = {23, 56, 78, 21, 56}
print(set1)
# to check whether the element in set or not
print(21 in set1)
# to check length of set
print(len(set1))
# print(type(set))
# set2 = {}
# print(type(set2))
# empty set
# set2 = set()
# print(type(set2))
# print(type(set2))
set2 = set("abcdmnop")
set3 = set("aeioupd")
print(set2)
print(set3)
# to remove all characters from set2 which are there in set3
print(set2-set3)
# to get all the values of set2 and set3
print(set2 | set3)
# to get common values in set2 and set3
print(set2 & set3)
# to get not common values from set2 and set3
print(set2 ^ set3)
