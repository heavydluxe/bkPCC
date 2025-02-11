cuisines = ["Chinese", "American", "Indian", "French"]

for cuisine in cuisines:
    print(cuisine)
    
# I can append while cuisines is a list.  If it's a tuple, I can't.
cuisines.append("TexMex")
print(cuisines)