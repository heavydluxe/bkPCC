ords = []
for i in range(1,11,1):
    ords.append(i)

for ord in ords:
    if ord == 1:
        print(f"{ord}st")
    elif ord == 2:
        print(f'{ord}nd')
    elif ord == 3:
        print(f'{ord}rd')
    else:
        print(f"{ord}th")