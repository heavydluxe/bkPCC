toppings = ['pepperoni', 'sausage', 'pineapple', 'bacon', 'kungpao chicken']
print("There are some great pizzas in the world...")
for topping in toppings:
    print(f"{topping.title()} pizza is delicious!")
print("I could eat them all")

print(f"The first three toppings were {toppings[:3]}")
print(f"The middle three toppings were {toppings[1:4]}")
print(f"The last three toppings were {toppings[-3:]}")

friend_toppings = toppings[:]
toppings.append(input("What other topping do I like? "))
friend_toppings.append(input("What other toppings does my friend like? "))

for topping in toppings:
    print(f"I like {topping} pizza.")
    
for topping in friend_toppings:
    print(f"My friend likes {topping} on their pizza")