def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    n = int(input("Enter a positive number: "))
    print("The factorial of", n, "is", factorial(n))

main()