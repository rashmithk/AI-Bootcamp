number = int(input("Enter a number whose Multiplication Table to be written: "))
count=1
while count<11:
    result= number*count
    print(f"{number}*{count}={result}")
    count+=1
