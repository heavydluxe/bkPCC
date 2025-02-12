alien_color=input("What color is the alien you caught? Red, Green, or Blue? ")

if alien_color.lower() == "green":
    print("Green aliens are worth 10 points")
    points=10
elif alien_color.lower() == "red":
    print("Red aliens are worth 15 points")
    points=15
elif alien_color.lower() == "blue":
    print("Blue aliens are worth 20 points")
    points=20
else:
    print("I dunno wtf you caught.")    
    points=0
    
print(f"You scored {points} for your {alien_color.lower()} alien")
