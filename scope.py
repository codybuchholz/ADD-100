POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

def main():
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))

    weight = weight * POUNDS_TO_KG
    height = height * INCHES_TO_METERS

    bmi = weight / (height * height)

    if bmi < 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "normal weight"
    elif bmi < 30:
        category = "overweight"
    else:
        category = "obese"

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are in the {category} category.")

main()