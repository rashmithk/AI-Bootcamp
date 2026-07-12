def is_eligible(age):
    age = int(input("Enter Your Age: "))
    if age >= 18:
        print("Eligible to Vote")
    else:
         print("Not Eligible")
     
is_eligible(18)
