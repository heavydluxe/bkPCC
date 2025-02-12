toppings = ["pepperoni", "pineapple", "ham", "bacon"]

request = input("What would you like on your pizza? ")

if request in toppings:
    print("fine")
else:
    print(f"We only have {toppings}")
