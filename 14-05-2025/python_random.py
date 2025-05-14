import random

#  Generate a random float between 0 and 1
print(random.random()) 

# a random integer between two values
print(random.randint(1, 10))

# a random float between two values
print(random.uniform(1.5, 5.5)) 

# a random item from a list
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))

# multiple random items
numbers = [1, 2, 3, 4, 5]
print(random.sample(numbers, 3))

# Shuffle a list (random order)
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)  

# Random boolean value
print(random.choice([True, False]))

dice = random.randint(1, 6)
print("You rolled:", dice)

toss = random.choice(["Heads", "Tails"])
print("Coin Toss Result:", toss)