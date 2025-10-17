nato_dict = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
    'Z': 'Zulu'}
def spell_nato(word):
    print("\nNATO Phonetic Spelling:")
    for letter in word.upper():
        if letter.isalpha():
            print(f"{letter} → {nato_dict[letter]}")
def main():
    user_word = input("Enter a word that you want to translate to the NATO alphabet: ")
    spell_nato(user_word)
if __name__ == "__main__":
    main()