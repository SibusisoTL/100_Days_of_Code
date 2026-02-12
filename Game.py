#OPTION 1

import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(random.choice(friends))   
#OPTION 2    
from random import randint       
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]   
q = randint(0, 4)           
                                                       
print(friends[q])                              
#GAME!                 
game_images = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor "))
if user_choice >= 0 and user_choice <= 2: 
    print(game_images[user_choice]
computer_choice = random.randint(a:0,b:2)     
print("computer choice:")  
print(game_images[computer_choice])  
   
         
if user_choice >=3 or user_choice < 0:
    print("You type and invalid number. You Lose!")
elif user_choice == 0 and computer_choice ==2:
    print("You win!")
elif computer_choice ==0 and user_choice ==2: 
    print("You Lose!")
elif computer_choice> user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a Draw!")
    
#----------------------------------------------------------------------------
#Treasure Hunt Game
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
    
