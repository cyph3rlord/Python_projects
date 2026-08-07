foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q) to quit: ")
    if food.lower() == "q":
        break
    while True:
           try:
               price = float(input("Enter a price: $"))
               break
           except ValueError:
            print('price should be a number')
    foods.append(food)   
    prices.append(price)   
 
print('------your cart------')   
for food in foods:
    print(food, end=" ")   
print()   
for price in prices:
    print(f'${price}', end=" ")           