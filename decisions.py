age = int(input("What is your age? "))
#First I need their age input, this determines the answers
#Then I take their input and plug it into greater than or less than equations that then prints the correct response to their input
if age >= 16:
    print ("You are old enough to drive")
else:
    print("You are not old enough to drive")
    
if age >= 18:
    print ("You are old enough to vote")
else:
    print("You are not old enough to vote")

if age >= 21:
    print ("You are old enough to buy alcohol")
else:
    print("You are not old enough to buy alcohol")

if age >= 55:
    print ("You are old enough to get a senior discount")
else:
    print("You are not old enough to get a senior discount.")