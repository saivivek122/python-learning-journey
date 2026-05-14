from array import *
arr1 = array("i", [33, 4, 55, 5, 66])
print(arr1)
# To print only values
print(arr1.buffer_info())
print(arr1.tolist())
for n in arr1:
    print(n)
