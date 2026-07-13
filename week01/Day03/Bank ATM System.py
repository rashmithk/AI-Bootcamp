import math
bal=1000
def check_balance():
    global bal
    print(f"Balance in your account is: {bal}")
    
    
def deposit():
    global bal
    credit=int(input("Enter the amount to be credited: "))
    updbal=bal+credit
    print(f"Updated balance in your account is: {updbal}")
    bal=updbal

    
def withdraw():
    global bal
    debit=int(input("Enter the amount to be debited: "))
    if debit > bal:
        print("You do not have sufficient ammount in your account")
    else:
        updbal=bal-debit
        print(f"Updated balance in your account is: {updbal}")
        bal=updbal

print("====== R Bank ATM ======")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
print("====== *********** ======")
choice=int(input("Choose an option: "))
if choice == 1:
    check_balance()
elif choice == 2:
    deposit()
elif choice == 3:
    withdraw()
elif choice == 4:
    print("Thank You for using R Bank ATM")
else:
    print("Invalid Entry!!")
    
