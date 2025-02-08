dinner_guests = ["Ronnie", "Bill", "Ted"]
print(f"You would like to have {dinner_guests} for dinner. \n")

friends = []
while True:
    friend = input("Give me a name: ")
    if friend == "":
        print("That's all the friends you have")
        break
    else:
        friends.append(friend)
        print(friends)
        