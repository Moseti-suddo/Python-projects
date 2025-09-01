import random
import time

def choose_difficulty():
     print("Choose a difficulty(easy/ medium/ hard)")
     choice = input("> ").lower()

     if choice == "easy":
          return 1, 10, 5
     if choice == "medium":
          return 1, 50, 7
     if choice == "hard":
          return 1, 100, 10
     else:
          print("Thats an invalid choice. \nDefaulting to easy...")
          time.sleep(2)
          return 1, 10, 5
         
     


def attempts(attempt): 
        print(f"You have {attempt} attempts left")


low, high, attempt = choose_difficulty()

answer = random.randint(low, high)
attempt_count = 0

print(f"Guess a number between {low} and {high} to win!")

while attempt > 0: #Using while... else
    guess = input("\nEnter your guess: ")
    attempt-=1
    attempt_count+=1


    if guess.isdigit():
        guess = int(guess)
        
        if guess<low or guess>high:
            print("Enter a value within the given range \nTry again.")
            attempts(attempt)

        elif guess > answer:
            print("Too high! Try again")
            attempts(attempt)

        elif guess < answer:
            print("Too low! Try again")
            attempts(attempt)

        else:
            print(f"You won!! The number was {answer}!!")
            print(f"Finished in {attempt_count} attempts")   
            break           

    else:
        print(f"Invalid input! Enter a valid integer between {low} and {high}.")

else:
     print(f"Youre out of attempts! The number was {answer}.")

