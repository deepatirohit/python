# Concession stand program

menu = {
    "popcorn": 50,
    "soda": 30,
    "nachos": 70,
    "hot dog": 60,
    "candy": 25,
    "ice cream": 40,
    "burger": 80,
    "fries": 45
}
cart = []
total = 0

print("--------------MENU--------------")

for key, value in menu.items():
    print(f"{key:10} : {value:.2f}") 
    
print("----------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
        
print()
print(f"total is: {total}")