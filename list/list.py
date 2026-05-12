# nums = [12, 20, 90, 35, 99]
# print(nums)
# # First number
# print(nums[0])
# # Last number
# print(nums[-1])
# # Slicing
# print(nums[2:4])
# print(nums[2:])

# names = ["apple", "banana", "watermelon"]
# print(names)
# mix = ["apple", 99, 99.5]
# print(mix)
# # Combining two lists
# mix = [nums, names]
# print(mix)
# print(mix[0])
# print(mix[0][0])
# print(mix[1][2])

# # Combine two lists as single list
# mix = nums+names
# print(mix)

# List functions
nums = [23, 56, 14, 36, 45]
names = ["apple", "banana", "watermelon"]
mix = nums+names
# print(mix)
# append adds value at the end
nums.append(33)
print(nums)
# count to know how many times a number appearing
print(nums.count(23))
# insert to add number at required index
nums.insert(1, 55)
print(nums)
# remove to remove any element
nums.remove(56)
print(nums)
# pop to remove element based on index and returns the removed value and if no index given removes last value
print(nums.pop(4))
print(nums)
print(nums.pop())
print(nums)
# del to remove multiple elements need to give start and end index start index included end index not included
del nums[2:4]
print(nums)
# extend to add multiple values need to give new list
nums.extend([44, 56, 11, 99])
print(nums)
# to replace two values
nums[2:4] = [54, 76]
print(nums)
# to reverse a list
nums.reverse()
print(nums)
# to sort a list
nums.sort()
print(nums)
# In built functions
# min number
print(min(nums))
print(min(names))
# max number
print(max(nums))
# sum of numbers
print(sum(nums))
