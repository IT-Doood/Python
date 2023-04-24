#this app will generate a password


import string
import random

def generate_password(length, include_letters, include_numbers, include_symbols):
    password_characters = ""
#ascii_letters contains all enlish letters
    if include_letters:
        password_characters += string.ascii_letters
#string.digits will get 0-9
    if include_numbers:
        password_characters += string.digits
# string.puncuation will give all puctionation or symbols when refering to passwords
    if include_symbols:
        password_characters += string.punctuation
# this will creat a random sequence based on the length and characters you decide for your pasword. 
    password = ''.join(random.sample(password_characters, length))
    return password

print("Password Generator\n")

# Prompt the user for password criteria
length = int(input("Enter password length: "))
include_letters = input("Include letters? (y/n): ").lower() == "y"
include_numbers = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

# Generate and print the password
password = generate_password(length, include_letters, include_numbers, include_symbols)
print(f"\nYour generated password is: {password}")
