records = []                # Store all transactions
total_balance = 0.0  

# Defining the menu Function.
def menu(): 
    try:  
        
        print("Welcome to the Income and Expense Tracker!")
        while True:
            print("\nMenu:")
            print("1. Add Income Transaction")
            print("2. Add Expense Transaction")
            print("3. List All Transactions")
            print("4. Filter Transactions")
            print("5. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                trans_type = "income"
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount: "))
                source = input("Enter source/category: ")
                description = input("Enter description: ")
                records.append({
            "Date": date,
            "Source": source,             # for expenses, this will be the category
            "Description": description,
            "Type": trans_type.capitalize(),  # "Income" or "Expense"
            "Amount": amount,
            "Balance": total_balance
        })
                print("Income transaction added.")
            elif choice == "2":
                trans_type = "expense"
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                description = input("Enter description: ")

                records.append({
            "Date": date,
            "Source": source,             # for expenses, this will be the category
            "Description": description,
            "Type": trans_type.capitalize(),  # "Income" or "Expense"
            "Amount": amount,
            "Balance": total_balance
        })
                print("Expense transaction added.")
            elif choice == "3":
                list_transactions()
            elif choice == "4":
                filter_transactions(filter_value=None)
            else:
                print("Exiting the tracker. Goodbye!")
                break

    #Defining the income tracker function
    def add_transaction(date, source, description, trans_type, amount):
        """Append a transaction and update the running balance."""
        global total_balance
        if trans_type.lower() == "income":
            total_balance += amount
        else:
            total_balance -= amount
except:
    print("Invalid input. Please try again.")

def list_transactions():
    print("\nAll Transactions:")
    if not records: 
        print("(no records yet)")
        return
    for r in records:
        print(f"{r['Date']} | {r['Source']} | {r['Description']} | "
              f"{r['Type']} | {r['Amount']:.2f} | Balance: {r['total_balance']:.2f}")
        
#This is what thisfunction does:Find and show only the records that match what you searched for"""
def filter_transactions(filter_value=None):  
    print(f"\nFilter transactions  by: ({filter_value})")
    found = False
    for r in records:
        if r["Type"].lower() == filter_value.lower():
            pass
        elif r["Source"].lower() == filter_value.lower():
            pass
        elif r["Date"] == filter_value:
            pass
        else:
            continue

        found = True
        print(f"{r['Date']} | {r['Source']} | {r['Description']} | "
              f"{r['Type']} | {r['Amount']:.2f} | Balance: {r['Balance']:.2f}")
    if not found:
        print("No matching records found.")
menu()




           
        
"""choice = input("Choose an option: ")

    if choice == "1":  
        val = input("Enter type (Income/Expense): ")
        filter_transactions("type", val)
    elif choice == "2":
        val = input("Enter source/category (e.g., Food, Work): ")
        filter_transactions("source", val)
    elif choice == "3":
        val = input("Enter date (YYYY-MM-DD): ")
        filter_transactions("date", val)
    else:
        print("Invalid option.")

        
    # Summary Output
    

"""