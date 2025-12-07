def main_menu():
    print("Menu:")
    while True:
        try:
            print("\nWelcome! You can create new email entries, change email addresses, delete entries, or display entries.")
            print("1. Create a new entry")
            print("2. Display an entry by last name")
            print("3. Update an existing entry")
            print("4. Remove an entry")
            print("5. Quit")
            choice = int(input("Please enter the number of your selection: "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("That is not a valid number. Try again.")
        except ValueError:
            print("That is not a valid number. Try again.")


def check():
    try:
        with open("customer_list.txt", "r") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        print("Customer list does not exist. Creating a new file...")
        return []


def save(output):
    with open("customer_list.txt", "w") as file:
        for line in output:
            file.write(line)
    print("File updated.")


def create():
    customer = check()
    fname = input("Please enter the customer's first name: ")
    lname = input("Please enter the customer's last name: ")
    phone = input("Please enter the customer's phone: ")
    email = input("Please enter the customer's email: ")
    entry = f"{fname}, {lname}, {phone}, {email}\n"
    customer.append(entry)
    save(customer)


def read():
    customers = check()
    lname = input("Enter the last name to search: ")
    found = False
    for person in customers:
        if person.split(",")[1].strip().lower() == lname.lower():
            print(person.strip())
            found = True
    if not found:
        print("No customer found with that last name.")


def delete():
    customers = check()
    lname = input("Enter the last name of the entry to delete: ")
    updated_list = []
    removed = False
    for person in customers:
        if person.split(",")[1].strip().lower() == lname.lower():
            removed = True
        else:
            updated_list.append(person)
    if removed:
        save(updated_list)
    else:
        print("No matching customer found.")


def update():
    customers = check()
    lname = input("Enter the last name of the customer to update: ")
    updated_list = []
    updated = False
    for person in customers:
        fields = person.strip().split(",")
        if fields[1].strip().lower() == lname.lower():
            new_fname = input(f"First name [{fields[0].strip()}]: ") or fields[0].strip()
            new_lname = input(f"Last name [{fields[1].strip()}]: ") or fields[1].strip()
            new_phone = input(f"Phone [{fields[2].strip()}]: ") or fields[2].strip()
            new_email = input(f"Email [{fields[3].strip()}]: ") or fields[3].strip()
            new_entry = f"{new_fname}, {new_lname}, {new_phone}, {new_email}\n"
            updated_list.append(new_entry)
            updated = True
        else:
            updated_list.append(person)
    if updated:
        save(updated_list)
    else:
        print("No customer found with that last name.")


def main():
    check()
    while True:
        option = main_menu()
        if option == 1:
            create()
        elif option == 2:
            read()
        elif option == 3:
            update()
        elif option == 4:
            delete()
        elif option == 5:
            break


if __name__ == "__main__":
    main()

