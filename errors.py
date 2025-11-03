import random

def main():
    print("I'm thinking of a number between 1 and 100, can you guess it?")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                raise ValueError("Your guess must be between 1 and 100.")

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f" Correct, you guessed the number in {attempts} tries.")
                break

        except ValueError as ve:
            print(f"Invalid input: {ve}")
if __name__ == "__main__":
    main()