time_of_day = ["Morning","Noon", "evening"]
heart_rate = []
total = 0
for time in time_of_day:
    rate = int(input(f"Enter your heart rate (in BPM) in the {time}: "))
    heart_rate.append([time, rate])
    total += rate
    average = total / len(time_of_day)
for entry in heart_rate:
    print(f"At {entry[0]}, your heart rate was {entry[1]} BPM")

print(f"\nAverage heart rate today: {average:2f} BPM")