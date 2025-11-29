# This project uses OOP + inheritance:
# - Transaction as the base class
# - IncomeTransaction & ExpenseTransaction (child classes)
# - BudgetTracker (main controller class with all methods)


#            Transaction Base Class 
# This class represents a general transaction.
# It stores attributes common to ALL transactions.
# Child classes (IncomeTransaction, ExpenseTransaction) will inherit from this.
class Transaction:
    def __init__(self, date, amount, category, description, ttype):
        # These are the required attributes of every transaction
        self.date = date
        self.amount = float(amount)
        self.category = category.strip()
        self.description = description
        self.type = ttype.lower().strip()    # income or expense

    def apply_to_balance(self, current_balance):
        """
        This method MUST be overridden by child classes.
        Each child class will define how it changes the balance.
        """
        raise NotImplementedError("Subclasses must implement apply_to_balance()")

    def to_dict(self, new_balance):

        """Convert the transaction object into a dictionary.
        This allows us to store transactions in a list and print them easily."""

        return {
            "Date": self.date,
            "Source": self.category,
            "Description": self.description,
            "Type": self.type.capitalize(),
            "Amount": self.amount,
            "Balance": new_balance
        }


#            Child Classes Using Inheritance 
# These classes represent specific transaction behaviours.
# IncomeTransaction inherits from Transaction and defines how income affects the balance.

class IncomeTransaction(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "income")

    def apply_to_balance(self, current_balance):
        return current_balance + self.amount


# ExpenseTransaction inherits from Transaction and defines how expenses affect the balance.

class ExpenseTransaction(Transaction):
    def __init__(self, date, amount, category, description):
        super().__init__(date, amount, category, description, "expense")

    def apply_to_balance(self, current_balance):
        return current_balance - self.amount


#            BudgetTracker Class 
# This class controls the entire program.
# It stores all transactions and provides methods for:
# - adding transactions
# - listing them
# - filtering
# - summarizing
# - undoing
# - running the menu loop
class BudgetTracker:
    def __init__(self):
        self.records = []          # This will store the list of all transactions which are dictionaries
        self.total_balance = 0.0   # This will give the running balance after each transaction. So it is updated each time.


    #               Helper Functions 
    # Helper functions are small, reusable tools that support the main features.
    # They keep the code clean by preventing repetition and isolating common tasks.
    # These functions do NOT directly implement project features, but they make the add/list/filter/summary methods easier to write and maintain.

    def _get_float_input(self, prompt):
        """ this function ensures the user enters a valid number by repeatedly asking until the input can be converted to float.
            It prevents crashes from invalid input and avoids repeating validation code in multiple places.(e.g., typing 'ten' instead of 10
        would normally crash the program) so this repeats the prompt until a float is entered
            Provides clean numeric data for calculations and keeps add_income() and add_expense() simpler.
        """
        while True:
            value = input(prompt)
            try:
                return float(value)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

    def _print_transaction(self, r):
        """This helper function just gives a Standardized way the transactions are displayed."""
        print(f"{r['Date']} | {r['Source']} | {r['Description']} | "
              f"{r['Type']} | {r['Amount']:.2f} | Balance: {r['Balance']:.2f}")


    # Defining the various core features of the budget tracker.
    # This will be done by creating methods and every method below  one major feature of the project.

    def add_income(self):
        """This method adds an income transaction using the IncomeTransaction class."""
        print("\n--- Add Income ---")
        date = input("Enter date (YYYY-MM-DD): ")
        amount = self._get_float_input("Enter amount: ")
        category = input("Enter source/category: ")
        description = input("Enter description: ")

        
        t = IncomeTransaction(date, amount, category, description) # this will create an income object

        
        new_balance = t.apply_to_balance(self.total_balance) # This will calculate new balance after adding income


        # Convert the transaction object into a dictionary and store it in the list of records.
        # This makes the transaction easier to print, filter, and work with throughout the program.
        self.records.append(t.to_dict(new_balance))
        self.total_balance = new_balance

        print("Income transaction added.")

    def add_expense(self):
        """This adds an expense transaction using the ExpenseTransaction class."""
        print("\n--- Add Expense ---")
        date = input("Enter date (YYYY-MM-DD): ")
        amount = self._get_float_input("Enter amount: ")
        category = input("Enter category: ")
        description = input("Enter description: ")

        t = ExpenseTransaction(date, amount, category, description)
        new_balance = t.apply_to_balance(self.total_balance)

        self.records.append(t.to_dict(new_balance))
        self.total_balance = new_balance

        print("Expense transaction added.")


    def list_transactions(self):
        """This function will display all transactions in the order they were added."""
        print("\n--- All Transactions ---")
        if not self.records:
            print("(no records yet)")
            return

        for r in self.records:
            self._print_transaction(r)


    #          Defining the Filtering method
    # Allows filtering by:
    # - type (income/expense)
    # - category (food/salary/etc.)
    # - month (YYYY-MM)
    def filter_menu(self):
        if not self.records:
            print("\nNo transactions to filter.")
            return

        print("\nFilter options:")
        print("1) By type (income/expense)")
        print("2) By category")
        print("3) By month (YYYY-MM)")
        print("0) Back to main menu")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            v = input("Enter type: ")
            self.filter_transactions("type", v)
        elif choice == "2":
            v = input("Enter category: ")
            self.filter_transactions("category", v)
        elif choice == "3":
            v = input("Enter month (YYYY-MM): ")
            self.filter_transactions("month", v)
        elif choice == "0":
            return
        else:
            print("Invalid option.")

    def filter_transactions(self, mode, value):
        """Filters records based on the user’s chosen mode."""
        print("\n--- Filtered Transactions ---")
        found = False

        for r in self.records:
            match = False

            if mode == "type" and r["Type"].lower() == value.lower():
                match = True
            elif mode == "category" and r["Source"].lower() == value.lower():
                match = True
            elif mode == "month" and r["Date"].startswith(value):
                match = True

            if match:
                found = True
                self._print_transaction(r)

        if not found:
            print("No matching results.")



    #               Defining the method for Summarizing the Budget 
    # This calculates:
    # - Total income
    # - Total expenses
    # - Net balance
    # - Per-category totals
    def summarize_budget(self):
        if not self.records:
            print("\nNo transactions to summarize yet.")
            return

        total_income = 0
        total_expense = 0
        category_totals = {}

        for r in self.records:
            amt = r["Amount"]
            cat = r["Source"].lower()

            # Track per-category totals
            category_totals[cat] = category_totals.get(cat, 0) + amt

            # Track overall totals
            if r["Type"].lower() == "income":
                total_income += amt
            else:
                total_expense += amt

        net_balance = total_income - total_expense

        print("\n===== Budget Summary =====")
        print(f"Total Income:   {total_income:.2f}Rs")
        print(f"Total Expenses: {total_expense:.2f}Rs")
        print(f"Net Balance:    {net_balance:.2f}Rs")

        print("\n--- Category Totals ---")
        for cat, amt in category_totals.items():
            print(f"{cat.capitalize()}: {amt:.2f}Rs")


    #               Defining the Undo Last Transaction method
    # This will removes the most recent transaction and recalculates balance.
    def undo_last_transaction(self):
        if not self.records:
            print("\nNo transactions to undo.")
            return

        last = self.records.pop()
        print("\n--- Undo Last Transaction ---")
        print("Removed:")
        self._print_transaction(last)

        # Update balance
        self.total_balance = self.records[-1]["Balance"] if self.records else 0.0
        print(f"New balance: {self.total_balance:.2f}Rs")


    #            Defining the main Menu Loop 
    # This loop keeps running until the user chooses "Exit".
    def run(self):
        print("Welcome to the Budget Tracker!")

        while True:
            print("\nMain Menu:")
            print("1) Add income")
            print("2) Add expense")
            print("3) List transactions")
            print("4) Filter (type/category/month)")
            print("5) Show summary")
            print("6) Undo last transaction")
            print("0) Exit")

            choice = input("Choose option: ").strip()

            if choice == "1": self.add_income()
            elif choice == "2": self.add_expense()
            elif choice == "3": self.list_transactions()
            elif choice == "4": self.filter_menu()
            elif choice == "5": self.summarize_budget()
            elif choice == "6": self.undo_last_transaction()
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, try again.")


if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.run()
