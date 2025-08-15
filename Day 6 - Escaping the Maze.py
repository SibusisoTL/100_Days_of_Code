from random import random
import string
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
    password += random.choice(letters)
for char in range(0, nr_symbols):
    password += random.choice(symbols)
for char in range(0, nr_numbers):
    password += random.choice(numbers) 
print(password)

