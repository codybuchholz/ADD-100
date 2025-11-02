import random

WORD_LIST = (
    "Slide", "Wrist", "Flight", "Domination", "Fillet",
    "Instant", "Chamber", "Flowing", "Freezer", "October",
    "Hinge", "Closet", "Music", "Garbage", "Alphabet"
)


def game(answer, display):
    wrong = 0
    right = 0
    guessed_letters = []

    print("Welcome to Code of Fortune")
    print("You will guess letters until you have the word")
    print("If you have 5 wrong guesses you will lose!")

    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)

        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                right += 1
                bad_guess = False

        if bad_guess:
            print("Wrong!")
            wrong += 1
            print(f"You have {5 - wrong} incorrect guesses left.")
            if wrong >= 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if "_" not in display:
            print("You Win!")
            print("The word was:", answer)
            break


def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()