seats = list(range(1, 21))

print("Welcome, please reserve your seat!\n")

while True:
    print("Available seats:")
    print(seats)

    seat_choice = int(input(" Enter the seat number you'd like to purchase : "))

    if seat_choice == 0:
        print(" Thank you for using selecting your seat. Enjoy ")
        break

    if seat_choice < 1 or seat_choice > 20:
        print("  That seat number is unavailable. Please choose between 1 and 20.\n")
        continue

    if seat_choice in seats:
        seats.remove(seat_choice)
        print(f" {seat_choice} successfully purchased!\n")
    else:
        print(f" {seat_choice} is already sold or invalid. Please try another seat.\n")