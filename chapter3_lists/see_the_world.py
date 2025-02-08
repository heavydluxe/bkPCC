locations = []
turns = 0

while turns < 5:
    location=input("Where would you like to go? ")
    locations.append(location)
    turns = turns+1

print("")    
print(f"Your list in original order: {locations}\n")
print(f"Your list *printed* in alpa order: {sorted(locations)}\n")
print(f"Your list *printed* in reverse order: {sorted(locations, reverse=True)}\n")
print(f"But the list var is still in original order: {locations}\n")

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)


    