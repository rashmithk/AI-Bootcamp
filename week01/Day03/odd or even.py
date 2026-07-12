def is_even(number):
    number = int(input("Enter the number: "))
    result = number%2
    if result == 0:
        print("Entered number is an Even Number")
    else:
         print("Entered number is an Odd Number")
     
is_even(20)
