import math

def is_prime(n):

    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
            
    return True

try:
    user_num = int(input("Enter an integer to check: "))
    
    if is_prime(user_num):
        print(f"✨ {user_num} is a prime number!")
    else:
        print(f"❌ {user_num} is NOT a prime number.")
        
except ValueError:
    print("Oops! Please enter a valid whole number.")
