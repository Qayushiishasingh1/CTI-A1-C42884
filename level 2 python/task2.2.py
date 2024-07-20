import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    print(f"I have generated a number between {lower_bound} and {upper_bound}. Try to guess it!")
    attempts = 0
    
    while True:
        
        user_guess = int(input("Enter your guess: "))
        attempts += 1
        
        
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")
            break

number_guessing_game()
