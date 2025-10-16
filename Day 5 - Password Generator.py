  #For Loop
import random
import string
from random import random
             
Student_Scores = [10, 142, 120,171, 184, 149, 24, 9, 8, 199, 78,89,86] 
max_score = 0 
for score in Student_Scores:            
    if score > max_score:        
        max_score=score     
print(max_score)       
                       
                           
#For Loops and Range function  
x=0      
for number in range(1,101):    
    x +=number 
print(x) 
 
#Task  
for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0): 
        print("FizzBuzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)
#bUILDING A PASSWORD GENERATOR\
lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)

letters = lowercase_letters + uppercase_letters
numbers = list(range(0,10))
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n "))
nr_symbols = int(input(f"How many symbols would you like?\n "))
nr_numbers = int(input(f"How many numbers would you like?\n "))

password = ""
for  char in range(0,nr_letters):
    import random
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += str(random.choice(numbers))
print(password)
#----Hard Part--
pasword_list = []
for  char in range(0,nr_letters):
    pasword_list += random.choice(letters)
for char in range(0, nr_symbols):
    pasword_list+= random.choice(symbols)
for char in range(0, nr_numbers):
    pasword_list += str(random.choice(numbers))
print(password)
random.shuffle(pasword_list)
print(pasword_list)

passweord = ""
for char in pasword_list:
    passweord +=char
print(f"your password is: {passweord}")
