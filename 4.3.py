def main():
    try:
        total = 0.0
        count = 0

        with open("sales_totals.txt", "r") as file:
            for line in file:
                amount = float(line.strip())
                print(f"{amount:,.2f}")
                total += amount
                count += 1
        average = total / count
        print(f"Total: {total:,.2f}")
        print(f"Number of entries: {count}")
        print(f"Average: {average:,.2f}")
    except Exception as e:
        print("Error:", e)
main()