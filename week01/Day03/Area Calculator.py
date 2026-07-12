import math
def area_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is: {area:.2f}\n")

def area_circle():
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * (radius ** 2)
    print(f"The area of the circle is: {area:.2f}\n")

def area_triangle():
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is: {area:.2f}\n")

print("=== Area Calculator ===")
print("1. Rectangle")
print("2. Circle")
print("3. Triangle")
print("4. Exit")
    
choice = input("Choose a shape to calculate (1-4): ")
    
if choice == '1':
    area_rectangle()
elif choice == '2':
    area_circle()
elif choice == '3':
    area_triangle()
elif choice == '4':
    print("Goodbye!")
else:
    print("Invalid choice. Please run the program again.")
