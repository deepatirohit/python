# shopping cart program

foods = []
prices =[]
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter a price of {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----Your cart ----")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price
    
    
print()
print(f"cart total: {total}")