def two_letter_combinations(characters):
    for first in characters:
        for second in characters:
            yield first + second

def main():
    letters = ['a', 'b', 'c', 'd', 'e']
    for combo in two_letter_combinations(letters):
        print(combo)

main()
