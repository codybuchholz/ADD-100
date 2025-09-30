score = int(input("What is your numeric grade? "))

if score >= 101:
    print ("There was no extra credit, try again. ")

elif score >= 90:
    print ("Your letter grade is an A. ")

elif score >= 80:
    print ("Your letter grade is a B. ")

elif score >= 70:
    print ("Your letter grade is a C. ")

elif score >= 60:
    print ("Your letter grade is a D. ")

elif score <= -1:
    print ("Getting less than a 0% is not possible.")

else:
    print ("Your letter score is a F. ")

