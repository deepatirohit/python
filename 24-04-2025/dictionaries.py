# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

person = {
  "name": "Alice",
  "job": "Engineer",
  "age": 30
}

print(person)

print(person["name"])
print(person["job"])
print(person["age"])

# Dictionaries cannot have two items with the same key:

person = {
  "name": "Alice",
  "job": "Engineer",
  "age": 30,
  "age": 32  # This will overwrite the previous "age"
}
print(person)

# To determine how many items a dictionary has, use the len() function

print(len(person))

# The values in dictionary items can be of any data type:

person = {
  "name": "Alice",
  "married": True,
  "age": 32,
  "hobbies": ["reading", "cycling", "traveling"]
}

print(person)
print(type(person))

# dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.

person = dict(name = "Bob", age = 28, city = "Mumbai")
print(person)

# get()

person = {
  "name": "Alice",
  "job": "Engineer",
  "age": 32
}

print(person.get("name"))
print(person.get("job"))
print(person.get("age"))

# The keys() method will return a list of all the keys in the dictionary.

dictKeys = person.keys()
print(dictKeys)

for key in person.keys():
    print(key)

for value in person.values():
    print(value)

employee = {
  "name": "Ravi",
  "position": "Manager",
  "year_joined": 2015
}

employee["department"] = "Sales"

print(employee)
employee["year_joined"] = 2018
print(employee)

# The items() method will return each item in a dictionary, as tuples in a list.

print(employee.items())

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword

if "year_joined" in employee:
    print("existed")

# The update() method will update the dictionary with the items from the given argument.

person = {
  "name": "Alice",
  "job": "Engineer",
  "age": 32
}
print(person)
person.update({"age": 35, "name": "Anjali"})
print(person)


person = {
  "name": "john",
  "job": "Engineer",
  "age": 32
}

person.pop("age")

print(person)

# del keyword removes the item with the specified key name:
# The del keyword can also delete the dictionary completely:
student = {
    "name": "Teja",
    "roll_no": 101,
    "marks": {
        "math": 88,
        "science": 92,
        "english": 85
    },
    "pass": True
}

del student["marks"]
print(student)

# del student
# print(student)

# clear() method empties the dictionary:

product = {
    "id": "P1001",
    "name": "Wireless Mouse",
    "brand": "Logitech",
    "price": 899,
    "in_stock": True,
    "features": ["wireless", "USB receiver", "battery included"]
}

# product.clear()

print(product)

# Print all key names in the dictionary
for item in product:
    print(item)
    
# Print all values in the dictionary
for item in product:
    print(product[item])
    
# values() method to return values of a dictionary
itemsList = []
for item in product.values():
    itemsList.append(item)

print(itemsList)

# keys() method to return the keys of a dictionary:

keysList = []

for key in product.keys():
    keysList.append(key)

print(keysList)

# Loop through both keys and values, by using the items() method
for item in product.items():
    print(f"{item}")
    

# Make a copy of a dictionary with the copy() method:

copyProduct = product.copy()

print(copyProduct)
# Make a copy of a dictionary with the dict() function

print("-----product dict-----")
productDict = dict(product)

print(productDict)

# A dictionary can contain dictionaries, this is called nested dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily["child1"]["name"])
print(myfamily["child2"]["name"])
print(myfamily["child3"]["name"])
print(myfamily["child2"]["year"])
print(myfamily["child1"]["year"])