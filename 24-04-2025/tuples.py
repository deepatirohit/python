# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

tupleList = ("banana", "orange", "manago")
print(tupleList)

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

print(tupleList[0])
print(tupleList[1])
print(tupleList[2])

for item in tupleList:
    print(item)
    
print(len(tupleList))

print(type(tupleList))

# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

# the tuple() constructor to make a tuple.

myTupleList = tuple(("john", "james", "peter"))
print(myTupleList)

print(myTupleList[-1])
print(myTupleList[:2])

if "john" in myTupleList:
    print("name existed")
else:
    print("not existed")
    
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

myTuple = ("apple", "banan", "orange", "kiwi")

myList = list(myTuple)
myList.append("guava")

myTuple = tuple(myList)

print(myList)
print(myTuple)

# Tuple Methods
# Python has two built-in methods that you can use on tuples.

# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

print(myTuple.count("apple"))
print(myTuple.index("kiwi"))