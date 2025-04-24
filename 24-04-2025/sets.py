# Python Sets
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered and also have no duplicates.
# Sets are written with curly brackets
# Set items can be of any data type:
# You cannot access items in a set by referring to an index or a key.
# once a set is created, you cannot change its items, but you can add new items.

mySet = {}
mySet = set()

mySet = {"audi", "tata", "honda", "suzuki", "audi"}
print(mySet)

# The values False and 0 are considered the same value in sets, and are treated as duplicates:
# The values True and 1 are considered the same value in sets, and are treated as duplicates:

mySet1 = {"names", "fruits", 123, 3.14, 1, True, False, 0}
print(mySet1)

print(len(mySet1))

print(type(mySet1))

for item in mySet1:
    print(item)
    
print("names" in mySet1)
print("cars" in mySet1)
print(24 not in mySet1)

# To add one item to a set use the add() method.
mySet1.add("cars")

print(mySet1)

# To add items from another set into the current set, use the update() method.
mySet.update(mySet1)

print(mySet)

for item in mySet:
    print(item)
    
# To remove an item in a set, use the remove(), or the discard() method.
print(mySet)

mySet.remove("cars")
mySet.discard("audi")

print(mySet)

# The del keyword will delete the set completely:

# del mySet
# print(mySet)

# The union() and update() methods joins all items from both sets.

courseSet1 = {"python", "javascript", "Java", "c", "c++", "ruby"}

courseSet2 = {"React", "springboot", "vue", "Angular", "java", "javascript"}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

# The update() method inserts all items from one set into another.

# The update() changes the original set, and does not return a new set.

setList = courseSet1.update(courseSet2)

print(f"update set {setList}")

print(courseSet1)

courseSet3 = courseSet1.union(courseSet2)
courseSet3 = courseSet1 | courseSet2

courseSet3 = courseSet1.union(courseSet2, set3, set4)
courseSet3 = courseSet1 | courseSet2 | set3| set4
print(courseSet3)

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# The difference() method will return a new set that will contain only the items from the first set 
# that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
# You can use the - operator instead of the difference() method, and you will get the same result.

set3 = set1 - set2
print(set3)