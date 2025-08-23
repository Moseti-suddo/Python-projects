#Simple cart program

items = []
prices = []
total = 0


while True:
    item = input("Enter the item you want to purchace(q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {item}: "))
        items.append(item)
        prices.append(price)

print() #adds a newline
print("----- YOUR CART -----")
for i in range(len(items)):
    print(f"{items[i]} - ${prices[i]}")

for price in prices:
    total += price

print(f"Your total is {total}")


