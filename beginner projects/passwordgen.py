import secrets
import time
import string 

print("----- MY SIMPLE PASSWORD GENERATOR -----")
print()



while True :
    length =  input("What password length do you want? ") 
    passwordNo = input("How many passwords do you want to generate? ")

    if length.isdigit() and passwordNo.isdigit():
        length = int(length)
        passwordNo = int(passwordNo)
        break
    else:
        print("Please enter a valid integer!")
print()



characters = ""

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = "!@#$%^&*()_+"

print("Lowercase letters are included by default.")
include_upper = input("Do you want to include uppercase letters?(y/n): ").lower()
include_symbols = input("Do you want to include symbols?(y/n): ").lower()
include_numbers = input("Do you want to include numbers?(y/n): ").lower()

if include_upper == "y":
    characters+=uppercase
if include_symbols == "y":
    characters+=symbols
if include_numbers == "y":
    characters+=numbers

characters+=lowercase

print()


for i in range(passwordNo):
    password = "".join(secrets.choice(characters) for _ in range(length))
    print("Generating password...")
    time.sleep(1)
    print(f"Your password: {password} \n")


print("Exiting...")
time.sleep(1)
