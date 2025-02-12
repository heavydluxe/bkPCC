users = ['admin', 'brian', 'eva', 'hudson', 'cecily']

login = input("login: ")

if login.lower() not in users:
    print("access denied")
else:
    if login.lower() == 'admin':
        print(f'Greetings, Professor Falken. Would you like to play a game?')
    elif (login.lower() == 'brian') or (login.lower() == 'eva'):
        print(f'Greetings, {login.title()}. Glad you are back')
    else: 
        print(f"Oh no, it's {login.title()}")