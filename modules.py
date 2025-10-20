import random

def main():
    responses = [
        "Yes.",
        "No.",
        "You may rely on it.",
        "Signs point to yes.",
        "Signs point to no.",
        "Undecided",
        "Most likely.",
        "Unlikely.",
        "Try again another time.",
        "Concentrate and ask again.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]
    print("Virtual Magic 8-Ball!")
    while True:
        question = input("\nAsk the Magic 8-Ball a yes-or-no question: ")
        answer = random.choice(responses)
        print(f"Magic 8-Ball says: {answer}")
        
        again = input("\nDo you want to ask another question? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()