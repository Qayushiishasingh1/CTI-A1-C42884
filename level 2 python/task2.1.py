import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You've guessed the correct number.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
