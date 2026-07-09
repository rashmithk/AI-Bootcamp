weight= int(input("Enter your weight in kgs: "))
height= float(input("Enter your height in mts: "))
bmi= round((weight/(height*height)),2)
if bmi <18.5:
    res="Underweight"
elif bmi > 18.5 and bmi <24.9:
    res="Normal"
elif bmi >25 and bmi <29.9:
    res="Overweight"
else:
    res="Obsese"
print(f"Your BMI is {res}")  
