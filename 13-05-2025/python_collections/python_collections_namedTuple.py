# collections:  namedtuple

from collections import namedtuple

Person = namedtuple("Person", "name, age")
person1 = Person("bob", 22)
person2 = Person("john", 26)
print(person1)
print(person2)

print(person1.age)
print(person1.name)

print(person2.name)
print(person2.age)

print(person1[0])