typeval=int(input(" Enter the conversion type 1. OMR to INR 2. INR to OMR: "))
amount=int(input(" Enter the amount: "))
if typeval==1:
    result=amount*250
    print (f"{amount} OMR in INR is {result} ")
else:
    result=amount/250
    print (f"{amount} INR in OMR is {result}")
