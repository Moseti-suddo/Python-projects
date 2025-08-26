import random

low = 1
high = 100

guesses = 0
is_running = True
answer = random.randint(low, high)

print("---- Python Guessing Game ----")
print()
print(f"Enter a number between {low} and {high}")

while is_running:
    guess = input("Your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses+=1

        if guess>high or guess<low:
            print(f"Pick a value within the range {low} and {high}")
            print("Try again")
            print()

        elif guess > answer:
            print("Too high! Try again")
        elif guess < answer:
            print("Too low! Try again")

        else:
            print()
            print(f"CORRECT!! The number was {answer}")
            print(f"You guessed within {guesses} tries ")
            is_running = False


    else: 
        print("Invalid input")
        print("Please enter a valid integer within the designated range")
        print()