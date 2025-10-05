a=int(input("Enter an integer. "))
b=int(input("Enter a second integer. "))
c= 50
d= 0
if a>b and b>c: 
    print (f"{a} and {b} are greater than 50. ")
else:
    print (f"{a} and {b} are less than 50. ")

if b>a or a<d:
    print (f"{b} is greater than 50.")

if d>a or d>b:
    print (f"{a} and {b} are both positive numbers.")

if a>b and b>d:
    print (f"{a} is not over than 0")
else:
    print (f"{a} is more than 0")

if not a>b:
    print (f"{b} is greater than {a}.")
else:
    print (f"{a} is greater than {b}.")

if not a>d: 
    print (f"{a} is a negative number.")