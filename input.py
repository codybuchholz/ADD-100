income = int(input("What is your net monthly income? "))
print(f"You intake ${income} a month.")

housing = int(input("How much do you spend on housing a month? "))
print(f"You spend ${housing} a month on housing.")

utilities = int(input("How much do you spend on utilities a month? "))
print(f"You spend ${utilities} a month on utilities.")

groceries = int(input("How much do you spend on groceries a month? "))
print(f"You spend ${groceries} a month on groceries.")

transportation = int(input("How much do you spend on transportation a month? "))
print(f"You spend ${transportation} a month on transportation.")

health = int(input("How much do you spend on health care a month? "))
print(f"You spend ${health} a month on health care.")

personal = int(input("How much do you spend on personal care a month? "))
print(f"You spend ${personal} a month on personal care.")

clothing = int(input("How much do you spend on clothing a month? "))
print(f"You spend ${clothing} a month on clothing.")

debt = int(input("How much do you spend on debt a month? "))
print(f"You spend ${debt} a month on debt.")


total_spent = housing + utilities + groceries + transportation + health + personal + clothing + debt

leftover = income - total_spent

print(f"Total spent this month: ${total_spent}")

print(f" - Housing: {(housing / income) * 100}%")
print(f" - Utilities: {(utilities / income) * 100}%")
print(f" - Groceries: {(groceries / income) * 100}%")
print(f" - Transportation: {(transportation / income) * 100}%")
print(f" - Health care: {(health / income) * 100}%")
print(f" - Personal care: {(personal / income) * 100}%")
print(f" - Clothing: {(clothing / income) * 100}%")
print(f" - Debt: {(debt / income) * 100}%")