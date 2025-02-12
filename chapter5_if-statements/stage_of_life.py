age = int(input("Give me an age and I'll put that age in a classification. What age? "))

if age < 2:
    print(f"someone who's {age} is a baby.")
elif (age >= 2) and (age <= 4):
    print(f"someone who's {age} is a toddler")
elif (12 >= age > 4):
    print(f"someone who's {age} is a kid")
else:
    print(f"This {age} year old is basically dead.")