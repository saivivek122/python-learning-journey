# data = {0: 34, 1: 35, 2: 67, 3: 8}
# print(data[2])
# data = {"apple": 3, "banana": 5, "watermelon": 9, "mango": 10}
# print(data["mango"])
# print(data.get("mango"))
# print(data.get(1))
# print(data.get("orange", "not found"))
# print(data.get("mango"))

# data = {"apple": 3, "banana": 5, "watermelon": 9, "mango": 10, "mango": 5}
# print(data)
# dictionary from set and list
# keys = {"apple", "banana", "watermelon"}
# values = [20, 30, 40]
# dict1 = dict(zip(keys, values))
# print(dict1)

# data = {"apple": 3, "banana": 5, "watermelon": 9, "mango": 10}
# # pop to remove elements from dictionary and returns the value
# print(data.pop("mango"))
# print(data)
# # del to remove element from dictionary
# del data["watermelon"]
# print(data)
# dictionary inside a dictionary
data = {"js": "vscode", "python": ["vscode", "pycharm"], "java": {
    "core": "vscode", "spring": "iij"}}
print(data)
print(data["js"])
print(data["python"])
print(data["python"][0])
print(data["java"])
print(data["java"]["spring"])
