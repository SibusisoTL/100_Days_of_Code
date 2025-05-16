print("Welcome to Treasure Island. Your mission is to find the treasure.")



y = input("Do you want to go Left ot Right? ")
if y == "right" or y == "Right":
    print("Fall into a hole. Game Over.")
elif y == "left" or y == "Left" :
    z = input("Swim or wait? ")
    if z == "swim" or z == "Swim":
        print("Attacked by trout. Game Over.")
    elif z == "Wait" or z == "wait":
        a = input("Which door, Blue, Yellow or Red? ")
        if a == "Blue" or a == "blue":
            print("Eaten by beasts. Game Over.")
        elif a == "Yellow" or a == "yellow":
            print("You Win!")
        elif a == "Red" or a == "red":
            print("Burned by fire. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")
