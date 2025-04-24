import random
 
# print(help(random))

number = random.randint(1, 6)

print(number)

# Returns a random integer between a and b
low = 1
high = 20

number = random.randint(low, high)

print(number)

# Shuffles the original list in place (does not return anything).
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", "A"]

random.shuffle(cards)

print(cards)

# Returns a random float number between 0.0 and 1.0.
print(random.random())

# Returns a randomly selected element from a non-empty sequence.
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits)) 

# Returns a list of k unique elements
print(random.sample(fruits, 2)) 

# Returns a list of k randomly selected elements with replacement.
print(random.choices(fruits, k=2))