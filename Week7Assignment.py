records = []                   # Store all transactions
total_balance = 0.0            # Track the overall balance
# Defining the menu Function.
# Defining the base class
class Transaction:
    def __init__(self, date, amount, category, description, trans_type):
        self.date = date
        self.amount = float(amount)
        self.category = category.strip()
        self.description = description
        self.type = trans_type.lower().strip() 


    def apply_to_balance(self, current_balance):
        #Apply this transaction to the given balance and return the new balance.
        raise NotImplementedError("Subclasses must implement this method")


    def to_dict(self, new_balance):
        """Convert this transaction to your dictionary structure."""
        return {
            "Date": self.date,
            "Source": self.category,
            "Description": self.description,
            "Type": self.type.capitalize(),    
            "Amount": self.amount,
            "Balance": new_balance
        }
    
    #Defining the Child class for Income Transaction

class IncomeTransaction(Transaction):
    def __init__(self, date, amount, category, description):
        # Call parent constructor with type='income'
        super().__init__(date, amount, category, description, "income")

    def apply_to_balance(self, current_balance):
        return current_balance + self.amount
    
#Defining the Child class for Expense Transaction
class ExpenseTransaction(Transaction):
    def __init__(self, date, amount, category, description):
        # Call parent constructor with type='expense'
        super().__init__(date, amount, category, description, "expense")

    def apply_to_balance(self, current_balance):
        return current_balance - self.amount
    
    #Defining the menu function and flow of the code

def menu(): 
    global total_balance

    print("Welcome to the Income and Expense Tracker!")
    while True:
        print("\nMenu:")
        print("1. Add Income Transaction")
        print("2. Add Expense Transaction")
        print("3. List All Transactions")
        print("4. Filter Transactions")
        print("5. Exit")
        print("6.Summarize Budget")
        choice = input("Choose an option: ")

        try:

            if choice == "1":
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount: "))
                source = input("Enter source/category: ")
                description = input("Enter description: ")

                t = IncomeTransaction(date, amount, source, description)
                new_balance = t.apply_to_balance(total_balance)
                record_dict = t.to_dict(new_balance)


                records.append(record_dict)
                total_balance = new_balance


                print("Income transaction added.")


            elif choice == "2":
            # ---- Add Expense ----
                date = input("Enter date (YYYY-MM-DD): ")
                amount = float(input("Enter amount: "))
                source = input("Enter category: ")
                description = input("Enter description: ")

                # Use inheritance: ExpenseTransaction child class
                t = ExpenseTransaction(date, amount, source, description)
                new_balance = t.apply_to_balance(total_balance)
                record_dict = t.to_dict(new_balance)

                records.append(record_dict)
                total_balance = new_balance

                print("Expense transaction added.")

            elif choice == "3":
                list_transactions()

            elif choice == "4":
                filter_value = input("Enter filter value (type/source/date): ")
                filter_transactions(filter_value)

            elif choice == "5":
                print("Exiting the tracker. Goodbye!")
                break

            elif choice == "6":
                summarize_budget()

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Invalid input. Please enter numeric values for amount.")
        except Exception as e:
            print(f"An error occurred: {e}")


            #defining the Helper functions    

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

def summarize_budget():
    if not records:
        print("\nNo transactions to summarize yet.")
        return

    total_income = 0.0
    total_expense = 0.0
    category_totals = {}    # e.g. { "food": 200, "salary": 5000 }

    for r in records:
        amount = r["Amount"]
        category = r["Source"].lower()

        # Update category totals (regardless of type)
        if category not in category_totals:
            category_totals[category] = 0.0
        category_totals[category] += amount

        # Update income/expense totals
        if r["Type"].lower() == "income":
            total_income += amount
        else:
            total_expense += amount

    net_balance = total_income - total_expense

    #Defining what the summary will display
    print("\n===== Budget Summary =====")
    print(f"Total Income:   {total_income:.2f}")
    print(f"Total Expenses: {total_expense:.2f}")
    print(f"Net Balance:    {net_balance:.2f}")

    print("\n--- Category Totals ---")
    for category, amount in category_totals.items():
        print(f"{category.capitalize()}: {amount:.2f}")

if __name__ == "__main__":
    menu()

menu()
