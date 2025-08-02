import random

def guess_the_number():
    print(" Welcome to SkillCraft's Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1

            if guess < 1 or guess > 100:
                print(" Please enter a number between 1 and 100.")
            elif guess < number_to_guess:
                print(" Too low! Try again.")
            elif guess > number_to_guess:
                print(" Too high! Try again.")
            else:
                print(f" Correct! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print(" Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
