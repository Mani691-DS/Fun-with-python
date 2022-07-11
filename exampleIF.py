print("Welcome to treasure island")
choice = input("Enter left or right:- ")
if choice == 'right':
    print("Game over")
else:
    choice1 = input("Enter swim or wait:- ")
    if choice1 == 'swim':
        print("Game over")
    else:
        choice2 = input("Enter door colour red , blue , yellow:- ")
        if choice2 == 'red' or choice2 == 'blue':
            print("Game over")
        else:
            print("You have won the game ")
