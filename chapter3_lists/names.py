names = ['Ryan', 'Steve', 'Neal']
print(f"my first friend is {names[0]}")
print(f"my next friend is {names[1]}")
print(f"my other friend is {names[2]}")
print(f"but the last is also first, so my other first friend is {names[-1]}")

friends = []
while True:
    friend = input("Give me a name: ")
    if friend == "":
        print("That's all the friends you have")
        break
    else:
        friends.append(friend)
        print(friends)
        
        