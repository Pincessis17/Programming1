records = []                # Store all transactions
 

"""def add_transaction():
        Append a transaction and update the running balance.
        global total_balance
        if trans_type == "income":
            total_balance += amount
        else:
            total_balance -= amount"""
# Defining the menu Function.
def menu(): 
    global total_balance
    total_balance = 0.0 
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
            "Balance": total_balance + amount
        
        })
                total_balance += amount

                print("Income transaction added.")
            elif choice == "2":
                trans_type = "expense"
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount: "))
                source = input("Enter category: ")
                description = input("Enter description: ")

                records.append({
            "Date": date,
            "Source": source,             # for expenses, this will be the category
            "Description": description,
            "Type": trans_type.capitalize(),  # "Income" or "Expense"
            "Amount": amount,
            "Balance": total_balance - amount
        })
                total_balance -= amount
                print("Expense transaction added.")
                
            elif choice == "3":
                list_transactions()
            elif choice == "4":
                filter_value = input("Enter filter value (type/source/date): ")
                filter_transactions(filter_value)
            else:
                print("Exiting the tracker. Goodbye!")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
        menu()
    #Defining the income tracker function
    

def list_transactions():
    print("\nAll Transactions:")
    if not records: 
        print("(no records yet)")
        return
    for r in records:
        print(f"{r['Date']} | {r['Source']} | {r['Description']} | "
              f"{r['Type']} | {r['Amount']:.2f} | Balance: {r['Balance']:.2f}")
        
#This is what thisfunction does:Find and show only the records that match what you searched for"""
def filter_transactions(filter_value):  
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