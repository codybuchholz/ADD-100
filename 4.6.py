import calendar
import datetime

def main():
    current_year = datetime.datetime.now().year
    user_input = input("Enter your birth month (1-12): ")

    try:
        month = int(user_input)
        if month < 1 or month > 12:
            print("Invalid month. Please enter a number between 1 and 12.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    print(calendar.month(current_year, month))

main()