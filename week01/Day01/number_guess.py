secretnum= 9
guesscount= 0
limit= 3
while guesscount < limit:
    guessednum = int(input("Guess: "))
    guesscount +=1
    if guessednum == secretnum:
        print("You won!")
        break
else:
    print("You ran out of limits")
