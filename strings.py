def main():
    example_string = "Hello, Python programmers!"

    print("Iterating through the string:")
    for char in example_string:
        print(char)

    print("\nCharacter with the minimum ASCII value:")
    print(min(example_string))

    print("\nCharacter with the maximum ASCII value:")
    print(max(example_string))

    print("\nIndex of 'o':")
    print(example_string.index('o'))

    print("\nConverting string to a list of characters:")
    print(list(example_string))

    print("\nCount of 'o' in the string:")
    print(example_string.count('o'))
main()