days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

steps = []      

for day in days:
    step_count = int(input(f"How many steps did you take on {day}:"))
    steps.append (step_count)
print("Steps recorded for each day:")
for x in range(len(days)):
    print(f"{days[x]}: {steps[x]} steps")
total = sum(steps)
print(f"You took {total} steps this week")  
average = total / len(steps)
print(f"You take on average {average} steps a week")