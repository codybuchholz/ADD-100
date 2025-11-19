import datetime

def main():
    birthday_input = input("Enter your birthday (MM-DD-YYYY): ")
    birthday = datetime.datetime.strptime(birthday_input, "%m-%d-%Y")
    now = datetime.datetime.now()
    age_delta = now - birthday

    years = age_delta.days // 365
    months = age_delta.days // 30
    weeks = age_delta.days // 7
    days = age_delta.days
    hours = age_delta.total_seconds() // 3600
    minutes = age_delta.total_seconds() // 60

    print("\n--- Your Age ---")
    print(f"Years:   {years}")
    print(f"Months:  {months}")
    print(f"Weeks:   {weeks}")
    print(f"Days:    {days}")
    print(f"Hours:   {int(hours)}")
    print(f"Minutes: {int(minutes)}")

main()