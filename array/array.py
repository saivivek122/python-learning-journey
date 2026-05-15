from array import *
# arr1 = array("i", [33, 4, 55, 5, 66])
# print(arr1)
# # To print only values
# print(arr1.buffer_info())
# print(arr1.tolist())
# for n in arr1:
#     print(n)

# Array functions
arr1 = array("i", [33, 4, 55, 5, 66])
# # append adds the element at the end
# arr1.append(77)
# # reverse reverse the array
# arr1.reverse()

# for n in arr1:
#     print(n)
# Create a new array
arr2 = array(arr1.typecode, arr1.tolist())
arr2 = array(arr1.typecode, (n for n in arr1))
arr1[2] = 54
print(arr1)
print(arr2)
