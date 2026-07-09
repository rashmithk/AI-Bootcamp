number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
number3 = int(input("Enter a number3: "))
result=max(number1,number2,number3)
if number1==number2 and number2==number3:
    print("All the numbers are same")
else:
    print(result)
