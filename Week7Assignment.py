#Defining the income tracker function
def income_tracker():
    records = []          # Store all transactions
    total_balance = 0.0   # Running total

    while True:
        print("\n=== Income Tracker ===")
        date = input("Enter date (YYYY-MM-DD): ")
        source = input("Enter income source: ")
        description = input("Enter description: ")
        type_ = input("Enter type (income/expense): ").lower()
        amount = float(input("Enter amount: "))

        # Update balance based on type
        if type_ == "income":
            total_balance += amount
        elif type_ == "expense":
            total_balance -= amount
        else:
            print("Invalid type. Please enter 'income' or 'expense'.")
            continue

        # Store record
        records.append({
            "Date": date,
            "Source": source,
            "Description": description,
            "Type": type_,
            "Amount": amount,
            "Balance": total_balance
        })

        print(f"\n✅ Entry added successfully!")
        print(f"💰 Current Balance: {total_balance:.2f}")

        another = input("\nAdd another entry? (y/n): ").lower()
        if another != "y":
            break

    # Summary Output
    print("\n=== Income Summary ===")
    for r in records:
        print(f"{r['Date']} | {r['Source']} | {r['Description']} | {r['Type']} | {r['Amount']:.2f} | Balance: {r['Balance']:.2f}")

    print(f"\nFinal Total Balance: {total_balance:.2f}")

    return records, total_balance


# Run the function
if __name__ == "__main__":
    all_records, final_balance = income_tracker()
