This project is a simple command-line Budget Tracker built in Python.
It lets the user add incomes and expenses, view all their transactions, filter them, see a summary, and undo the last entry.
Everything runs in one terminal session, and all data stays in memory.

The goal of the project was to practise Python basics together with OOP and inheritance by building something practical.

                                        FEATURES OF THE PROJECT

(1) The project allows you to ADD TRANSACTIONS

You can add both income and expense entries.

Each entry includes date, amount, category, and description.

The system uses IncomeTransaction and ExpenseTransaction classes.

(2) The project also allows you to LIST ALL TRANSACTIONS

In essence, it shows every transaction recorded in the session in a clean format.

(3) It allows you to FILTER TRANSACTIONS

You can filter by:

Type (income or expense)

Category (eg, Food, Salary, etc)

Month (e.g., 2025-10)

(4) It also gives a SUMMARY of all transactions.

    It displays:

       i) Total income

      ii) Total expenses

      iii) Net balance

      iv)  Spending totals by category

(5) It also allows you to UNDO LAST TRANSACTION

    In essence, if you make a mistake, you can remove the last entry.

(6) Finally, the project checks INPUT VALIDATION

In essence, the program protects against invalid menu choices and invalid numbers.


                                        HOW TO RUN THE PROGRAM
REQUIREMENTS : Python 3

Steps

    1) Clone the project repository:{git clone https://github.com/Pincessis17/Programming1.git}

    2) Open the folder:{cd Assignment}

    3) Run the program:{python Week7Assignment.py}

That’s it — the menu will appear in your terminal.

                                        MENU STRUCTURE
1) Add income
2) Add expense
3) List transactions
4) Filter (type/category/month)
5) Show summary
6) Undo last transaction
0) Exit


                                        SAMPLE INTERACTIONS 
Adding an Income
    --- Add Income ---
    Enter date (YYYY-MM-DD): 2025-11-26
    Enter amount: 500
    Enter source/category: Salary
    Enter description: Part-time job
    Income transaction added.

Listing Transactions
    --- All Transactions ---
    2025-11-26 | salary | Part-time job | Income | MUR 500.00 | Balance: MUR 500.00

Filtering by Category
    --- Filtered Transactions ---
    2025-11-26 | salary | Part-time job | Income | MUR 500.00 | Balance: MUR 500.00

Summary Example
    ===== Budget Summary =====
    Total Income:   MUR 500.00
    Total Expenses: MUR 0.00
    Net Balance:    MUR 500.00

--- Category Totals ---
    Salary: MUR 500.00

Undo Example
    --- Undo Last Transaction ---
    Removed:
    2025-11-26 | salary | Part-time job | Income | MUR 500.00 | Balance: MUR 500.00
    New balance: MUR 0.00