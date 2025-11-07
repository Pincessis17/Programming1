records = []                # Store all transactions
total_balance = 0.0         # Running total

#Defining the income tracker function

def income_tracker():
    while True:
        trans_type = "income"  # Since this is an income tracker, we set type to income
        date = input("Enter date (YYYY-MM-DD): ")
        source = input("Enter income source: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))      

def expense_tracker():
    while True:
        trans_type = "expense"  # Since this is an expense tracker, we set type to expense
        date = input("Enter date (YYYY-MM-DD): ")
        expense_category = input("Enter expense category(food,tansport,etc): ").capitalize()
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

def add_transaction(date, source, description, trans_type, amount, total_balance):
    records.append({
        "Date": date,
        "Source": source,
        "Description": description,
        "Type": trans_type,
        "Amount": amount,
        "Balance": total_balance
    })

def list_transactions():
    print("\nAll Transactions:")
    for r in records:
        print(f"{r['Date']} | {r['Source']} | {r['Description']} | {r['Type']} | {r['Amount']:.2f} | Balance: {r['Balance']:.2f}")        
    
       
        
    # Summary Output
    

    print(f"\nFinal Total Balance: {total_balance:.2f}")

    return records, total_balance


# Run the function
if __name__ == "__main__":
    all_records, final_balance = income_tracker()

"""if type_ == "income":
            total_balance += amount
        elif type_ == "expense":
            total_balance -= amount
        else:
            print("Invalid type. Please enter 'income' or 'expense'.")
            continue
            "_____________"

        print(f"\n✅ Entry added successfully!")
        print(f"💰 Current Balance: {total_balance:.2f}")

        another = input("\nAdd another entry? (y/n): ").lower()
        if another != "y":
            break
"""