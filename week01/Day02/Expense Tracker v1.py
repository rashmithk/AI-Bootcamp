income = 0.0
expenses = []

while True:
    print("\n======== Expense Tracker ========")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. Show Balance")
    print("4. Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        income = float(input("Enter income amount: "))
        print("Income added successfully!")
        break
    elif choice == '2':
        expense = float(input("Enter expense amount: "))
        expenses.append(expense)
        print("Expense added successfully!")
        break
    elif choice == '3':
        total_expense = sum(expenses)
        balance = income - total_expense
        print(f"\nTotal Income: ${income:.2f}")
        print(f"Total Expenses: ${total_expense:.2f}")
        print(f"Remaining Balance: ${balance:.2f}")
        
    elif choice == '4':
        print("Exiting Expense Tracker. Goodbye!")
        break
        
    else:
        print("Invalid choice. Please choose between 1 and 4.")
